"""The decision, in code: price against the fair value range, then flags from verified evidence.

Base rating from where the price sits: below the bear value Buy, below base Overweight, up to bull Hold,
up to 25% above bull Underweight, beyond that Sell. A red flag (material weakness, controls not effective,
adverse opinion, going concern, restatement) caps the rating at Underweight. Each caution flag (cash
conversion under 0.8, more than a quarter of the risk factor sentences new this year) takes one notch off.
Only claims the verifier accepted can raise a flag.
"""

from __future__ import annotations

import re
from typing import Any

RATINGS = ["Sell", "Underweight", "Hold", "Overweight", "Buy"]
RED = re.compile(r"material weakness|not effective|ineffective|adverse opinion|going concern|restat", re.I)
CLEAN = re.compile(r"(no|not identify any|did not identify|without any?|free of)\s+(\w+\s+){0,2}material weakness", re.I)
OK_STATUSES = ("verified", "number in passage")


def flags(value: dict[str, Any], evidence: dict[str, list[dict]], risk_stats: dict[str, Any] | None) -> dict[str, list[str]]:
    red, caution = [], []
    for c in evidence.get("accounting", []):
        text = f"{c.get('quote', '')} {c.get('statement', '')}"
        if c["check"]["status"] in OK_STATUSES and RED.search(text) and not CLEAN.search(text):
            red.append(f"{c.get('topic')}: {c.get('quote', '')[:120]}")
    conv = value.get("cash_conversion")
    if conv is not None and conv < 0.8:
        caution.append(f"cash conversion {conv:.2f} (operating cash flow / net income under 0.8)")
    if risk_stats and risk_stats.get("sentences_now"):
        changed = risk_stats["new_count"] / risk_stats["sentences_now"]
        if changed > 0.25:
            caution.append(f"{changed:.0%} of risk factor sentences are new this year")
    return {"red": red, "caution": caution}


def decide(value: dict[str, Any], flag_set: dict[str, list[str]]) -> dict[str, Any]:
    fv, price = value.get("fair_value"), value["price"]
    if not fv:
        return {"rating": "No rating", "why": [value.get("note") or "no fair value"], "upside_to_base": None}
    if price < fv["bear"]:
        step, where = 4, "below the bear value"
    elif price < fv["base"]:
        step, where = 3, "between bear and base"
    elif price <= fv["bull"]:
        step, where = 2, "between base and bull"
    elif price <= fv["bull"] * 1.25:
        step, where = 1, "up to 25% above the bull value"
    else:
        step, where = 0, "more than 25% above the bull value"
    why = [f"price {price:,.2f} is {where} (bear {fv['bear']:,.2f}, base {fv['base']:,.2f}, bull {fv['bull']:,.2f})"]
    if flag_set["red"]:
        step = min(step, 1)
        why.append("red flag caps the rating at Underweight")
    for c in flag_set["caution"]:
        step = max(step - 1, 0)
        why.append(f"one notch off: {c}")
    return {"rating": RATINGS[step], "why": why, "upside_to_base": round(fv["base"] / price - 1, 4)}


def adjust(decision: dict[str, Any], step: int, reason: str | None) -> dict[str, Any]:
    """Move a rating by *step* notches (the red team's at most one), keeping the reason."""
    if not step or decision["rating"] not in RATINGS:
        return decision
    i = min(max(RATINGS.index(decision["rating"]) + step, 0), len(RATINGS) - 1)
    return dict(decision, rating=RATINGS[i], why=decision["why"] + [reason or f"{step:+d} notch"])
