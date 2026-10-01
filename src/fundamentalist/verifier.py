"""Check every claim against the filing, in code.

A claim is verified when its quote appears in the passage it cites (after normalising whitespace,
quotes and dashes) and its value appears among the quote's numbers. When the quote is not verbatim
but the value is printed in the cited passage, the claim is "number in passage": the number is real,
the wording was paraphrased.
"""

from __future__ import annotations

import re
from typing import Any, Callable

_TRANS = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"', "–": "-", "—": "-"})


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.translate(_TRANS)).strip().lower()


def numbers(s: str) -> list[float]:
    """Numbers printed in *s*: 245,122 / 1.5 / (3,210) / 16% all come back as floats."""
    out = []
    for m in re.finditer(r"\(?-?\d[\d,]*(?:\.\d+)?\)?", s):
        raw = m.group()
        neg = raw.startswith("(") and raw.endswith(")")
        try:
            v = float(raw.strip("()").replace(",", ""))
        except ValueError:
            continue
        out.append(-v if neg else v)
    return out


def _close(a: float, b: float) -> bool:
    return abs(a - b) <= max(1e-6, 0.005 * abs(b)) or abs(abs(a) - abs(b)) <= max(1e-6, 0.005 * abs(b))


NUMBER_FIELDS = ("value", "value_prior", "low", "high", "compared_with")


def check(claim: dict[str, Any], passage_text: Callable[[str], str | None]) -> dict[str, Any]:
    """Status of one claim: verified, number in passage, unverified or no passage."""
    pid = str(claim.get("passage_id", "")).strip("[] ")
    text = passage_text(pid)
    values = []
    for key in NUMBER_FIELDS:  # every number the claim states must be printed: a range's ends, last year's figure
        try:
            if claim.get(key) is not None:
                values.append(float(claim[key]))
        except (TypeError, ValueError):  # a date or a word in a number field: check the quote alone
            pass
    if text is None:
        return {"status": "no passage", "passage_id": pid}
    quote_ok = bool(claim.get("quote")) and norm(claim["quote"]) in norm(text)
    q_nums, t_nums = numbers(claim.get("quote", "")), numbers(text)
    in_quote = all(any(_close(v, x) for v in q_nums) for x in values)
    in_passage = all(any(_close(v, x) for v in t_nums) for x in values)
    if quote_ok and in_quote:
        status = "verified"
    elif in_passage and values:
        status = "number in passage"
    else:
        status = "unverified"
    return {"status": status, "passage_id": pid, "quote_verbatim": quote_ok, "value_in_quote": in_quote,
            "value_in_passage": in_passage}


def verify(claims: list[dict[str, Any]], passage_text: Callable[[str], str | None]) -> dict[str, Any]:
    """Check every claim and count the outcomes."""
    results = [dict(claim, check=check(claim, passage_text)) for claim in claims]
    counts: dict[str, int] = {}
    for r in results:
        counts[r["check"]["status"]] = counts.get(r["check"]["status"], 0) + 1
    return {"claims": results, "counts": counts, "total": len(results)}
