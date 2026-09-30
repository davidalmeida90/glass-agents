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


def latest_filing(ticker: str, form: str = "10-K") -> dict[str, str]:
    """Latest filing of *form* for *ticker*, from EDGAR's submissions API."""
    tickers = json.loads(sec_get("https://www.sec.gov/files/company_tickers.json", "company_tickers.json"))
    co = next((v for v in tickers.values() if v["ticker"].upper() == ticker.upper()), None)
    if co is None:
        raise ValueError(f"unknown ticker {ticker}")
    cik = co["cik_str"]
    rec = json.loads(sec_get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))["filings"]["recent"]
    i = next((i for i, f in enumerate(rec["form"]) if f == form), None)
    if i is None:
        raise ValueError(f"no {form} in {ticker}'s recent filings")
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
    def from_text(cls, meta: dict[str, str], text: str) -> FilingIndex:
        passages = [(f"P{i:03d}", text[s:s + STEP]) for i, s in enumerate(range(0, len(text), STEP))]
        return cls(meta=meta, passages=passages)

    def search(self, query: str, k: int) -> list[tuple[str, str]]:
        """Top *k* passages for *query*, skipping ones this run has already been shown."""
        ranking = bm25_rank(query, [t for _, t in self.passages])
        hits = [self.passages[i] for i in ranking if self.passages[i][0] not in self.served][:k]
        self.served.update(pid for pid, _ in hits)
        return hits

    def text_of(self, pid: str) -> str | None:
        return next((t for p, t in self.passages if p == pid), None)


_INDEXES: dict[str, FilingIndex] = {}


def load_index(ticker: str, form: str = "10-K") -> FilingIndex:
    """Load (once per process) the latest *form* of *ticker* as a searchable index."""
    key = f"{ticker.upper()}:{form}"
    if key not in _INDEXES:
        meta = latest_filing(ticker, form)
        _INDEXES[key] = FilingIndex.from_text(meta, filing_text(meta))
    return _INDEXES[key]
