"""The filing is a lookup: SEC EDGAR access, passages and keyword search.

Adapted from David's own jev-for-finance/jev_rag.py (same author), without Jev: code finds the
latest filing and splits it into passages, and BM25 ranks them for each search.
"""

from __future__ import annotations

import html
import json
import math
import os
import re
import urllib.request
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

CACHE = Path(__file__).resolve().parents[2] / "cache"
STEP = 1500  # characters per passage, about 350 tokens


def sec_get(url: str, name: str | None = None) -> bytes:
    """Fetch an SEC URL once; later calls read the cached copy."""
    f = CACHE / name if name else None
    if f and f.exists():
        return f.read_bytes()
    agent = os.environ.get("SEC_USER_AGENT", "").strip()
    if not agent:
        raise RuntimeError("SEC_USER_AGENT is not set (SEC fair access asks for 'Name email')")
    req = urllib.request.Request(url, headers={"User-Agent": agent})
    data = urllib.request.urlopen(req, timeout=120).read()
    if f:
        CACHE.mkdir(exist_ok=True)
        f.write_bytes(data)
    return data


def latest_filing(ticker: str, form: str = "10-K", skip: int = 0) -> dict[str, str]:
    """Latest filing of *form* for *ticker* (skip=1: the one before it), from EDGAR's submissions API."""
    tickers = json.loads(sec_get("https://www.sec.gov/files/company_tickers.json", "company_tickers.json"))
    co = next((v for v in tickers.values() if v["ticker"].upper() == ticker.upper()), None)
    if co is None:
        raise ValueError(f"unknown ticker {ticker}")
    cik = co["cik_str"]
    sub = json.loads(sec_get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    rec = sub["filings"]["recent"]
    hits = [(rec, i) for i, f in enumerate(rec["form"]) if f == form]
    for page in sub["filings"].get("files", []):  # frequent filers: older filings sit on extra pages
        if len(hits) > skip:
            break
        older = json.loads(sec_get(f"https://data.sec.gov/submissions/{page['name']}", page["name"]))
        hits += [(older, i) for i, f in enumerate(older["form"]) if f == form]
    if len(hits) <= skip:
        raise ValueError(f"fewer than {skip + 1} {form} filings for {ticker} on EDGAR")
    rec, i = hits[skip]
    acc = rec["accessionNumber"][i]
    return dict(company=co["title"], ticker=ticker.upper(), form=form, key=acc, period=rec["reportDate"][i],
                filed=rec["filingDate"][i],
                url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{rec['primaryDocument'][i]}")


def filing_text(fil: dict[str, str]) -> str:
    """Plain text of the filing's primary document."""
    raw = sec_get(fil["url"], f"{fil['key']}.html").decode("utf-8", "ignore")
    raw = re.sub(r"(?is)<ix:header>.*?</ix:header>|<script.*?</script>|<style.*?</style>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", raw))).replace("\xa0", " ")


def tok(s: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", s.lower())


def bm25_rank(q: str, texts: list[str]) -> list[int]:
    """Indices of *texts* ordered by BM25 score for query *q*."""
    docs = [tok(t) for t in texts]
    avg, n = sum(map(len, docs)) / len(docs), len(docs)
    df = Counter(w for d in docs for w in set(d))
    scores = []
    for d in docs:
        tf, s = Counter(d), 0.0
        for w in tok(q):
            if w in tf:
                idf = math.log(1 + (n - df[w] + 0.5) / (df[w] + 0.5))
                s += idf * tf[w] * 2.5 / (tf[w] + 1.5 * (0.25 + 0.75 * len(d) / avg))
        scores.append(s)
    return sorted(range(n), key=lambda i: -scores[i])


@dataclass
class FilingIndex:
    """One filing split into passages, searchable by keyword."""

    meta: dict[str, str]
    passages: list[tuple[str, str]]
    served: set[str] = field(default_factory=set)

    @classmethod
    def from_text(cls, meta: dict[str, str], text: str, prefix: str = "P") -> FilingIndex:
        passages = [(f"{prefix}{i:03d}", text[s:s + STEP]) for i, s in enumerate(range(0, len(text), STEP))]
        meta = dict(meta)
        meta.setdefault("source", f"{meta.get('form', '10-K')} for the period ended {meta.get('period')}, "
                                  f"filed {meta.get('filed')}")
        return cls(meta=meta, passages=passages)

    def search(self, query: str, k: int) -> list[tuple[str, str]]:
        """Top *k* passages for *query*, skipping ones this run has already been shown."""
        ranking = bm25_rank(query, [t for _, t in self.passages])
        hits = [self.passages[i] for i in ranking if self.passages[i][0] not in self.served][:k]
        self.served.update(pid for pid, _ in hits)
        return hits

    def text_of(self, pid: str) -> str | None:
        return next((t for p, t in self.passages if p == pid), None)


# ------------------------------------------------------------------ risk factors: what is new this year

def _spaced(word: str) -> str:
    """A word whose letters may be split by spaces: styled headings extract as 'RIS K FACTORS'."""
    return r"\s*".join(re.escape(c) for c in word)


_ITEM_1A = re.compile(rf"item\s*1a\.?\s*[-:]?\s*{_spaced('risk')}\s*{_spaced('factors')}", re.I)
_NEXT_ITEM = re.compile(rf"item\s*(1b|1c|2)\.?\s*[-:]?\s*({_spaced('unresolved')}|{_spaced('cybersecurity')}|"
                        rf"{_spaced('properties')})", re.I)


def risk_section(text: str) -> str:
    """Item 1A of a 10-K: the longest stretch from an 'Item 1A. Risk Factors' heading to the next item.

    The table of contents names Item 1A too; taking the longest stretch skips it. Only a stretch that ends
    at the next item's heading counts, so a bank 10-K whose risk factors sit in the annual report under
    another title returns little or nothing rather than the rest of the document. When several mentions lead
    to the same next item (a cross-reference in Item 1, then the heading), the section starts at the last.
    """
    starts: dict[int, int] = {}  # next item's position -> the last Item 1A mention before it
    for m in _ITEM_1A.finditer(text):
        nxt = _NEXT_ITEM.search(text, m.end())
        if nxt is not None:  # a mention with no next item after it is not the section
            starts[nxt.start()] = m.end()  # later mentions (the real heading) replace cross-references
    chunks = [text[start:end] for end, start in starts.items() if end - start <= 300_000]
    return max(chunks, key=len, default="").strip()


def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", text) if len(s.strip()) >= 40]


def _shape(s: str) -> frozenset[str]:
    return frozenset(re.sub(r"\d+", "#", w) for w in tok(s))


def risk_changes(now_text: str, prior_text: str, covered: float = 0.8) -> dict[str, object]:
    """Sentences in this year's Item 1A that last year's did not already say, and the reverse.

    A sentence counts as already said when at least *covered* of its words (numbers ignored) appear in one
    sentence of the other year, or in two adjacent ones: updated years and figures, and sentences split or
    merged between years, stay unchanged; new wording does not.
    """
    now, prior = sentences(risk_section(now_text)), sentences(risk_section(prior_text))
    prior_shapes, now_shapes = [_shape(s) for s in prior], [_shape(s) for s in now]

    def pool(shapes: list[frozenset[str]]) -> list[frozenset[str]]:
        return shapes + [a | b for a, b in zip(shapes, shapes[1:])]

    def matched(shape: frozenset[str], candidates: list[frozenset[str]]) -> bool:
        return bool(shape) and any(len(shape & p) / len(shape) >= covered for p in candidates)

    prior_pool, now_pool = pool(prior_shapes), pool(now_shapes)
    new = [s for s, sh in zip(now, now_shapes) if not matched(sh, prior_pool)]
    removed = [s for s, sh in zip(prior, prior_shapes) if not matched(sh, now_pool)]
    return {"sentences_now": len(now), "sentences_prior": len(prior), "new": new, "removed": removed,
            "unchanged_share": round(1 - len(new) / max(1, len(now)), 3)}


_INDEXES: dict[str, FilingIndex] = {}
RISK_STATS: dict[str, dict[str, object]] = {}


def load_index(ticker: str, corpus: str = "10-K") -> FilingIndex:
    """Load (once per process) a searchable corpus for *ticker*.

    "10-K": the latest 10-K. "risk_changes": only the sentences of this year's Item 1A that were not in
    last year's, grouped into passages R000, R001 and so on.
    """
    key = f"{ticker.upper()}:{corpus}"
    if key in _INDEXES:
        return _INDEXES[key]
    if corpus == "10-K":
        meta = latest_filing(ticker, "10-K")
        _INDEXES[key] = FilingIndex.from_text(meta, filing_text(meta))
    elif corpus == "risk_changes":
        now_meta, prior_meta = latest_filing(ticker, "10-K"), latest_filing(ticker, "10-K", skip=1)
        diff = risk_changes(filing_text(now_meta), filing_text(prior_meta))
        RISK_STATS[ticker.upper()] = {k: v for k, v in diff.items() if k not in ("new", "removed")} | {
            "new_count": len(diff["new"]), "removed_count": len(diff["removed"]), "prior_period": prior_meta["period"]}
        meta = dict(now_meta, source=(f"sentences new in the Item 1A risk factors of the 10-K for the period ended "
                                      f"{now_meta['period']}, compared with the 10-K for {prior_meta['period']}"))
        _INDEXES[key] = FilingIndex.from_text(meta, " ".join(diff["new"]) or "No new risk factor sentences.", prefix="R")
    else:
        raise ValueError(f"unknown corpus {corpus}")
    return _INDEXES[key]
