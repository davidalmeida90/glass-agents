"""The decision, in code: price against base fair value with a margin of safety set by uncertainty, then flags.

Uncertainty starts from 12-month return volatility and goes one level up when the fair value range is wide
(parameters.uncertainty). The rating comes from price / base fair value against Morningstar's published bands
for that level (parameters.rating_bands): at Low uncertainty Buy needs the price at or below 0.80 of fair value
and Sell starts at 1.25; at Very High it takes 0.50 and 1.75. A red flag (material weakness, controls not
effective, adverse opinion, going concern, restatement) caps the rating at Underweight. Each caution flag (cash
conversion under 0.8, more than a quarter of the risk factor sentences new this year) takes one notch off. Only
claims the verifier accepted can raise a flag.

First version (2026-09-30) rated on where the price sat inside bear/base/bull, so a wide range read as Hold even
30% above base value (Apple).
"""

from __future__ import annotations

import re
from typing import Any

from fundamentalist.parameters import value as param

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
        caution.append(f"cash conversion {conv:.2f} (operating cash flow / NOPAT under 0.8)")
    if risk_stats and risk_stats.get("sentences_now"):
        changed = risk_stats["new_count"] / risk_stats["sentences_now"]
        if changed > 0.25:
            caution.append(f"{changed:.0%} of risk factor sentences are new this year")
    return {"red": red, "caution": caution}


LEVELS = ["Low", "Medium", "High", "Very High", "Extreme"]


def uncertainty(vol: float | None, fair: dict[str, float], dcf_to_multiples: float | None = None) -> tuple[str, float]:
    """Uncertainty from volatility (High when unknown); one level up for a wide range, one for methods disagreeing."""
    cfg = param("uncertainty")
    level = 2 if vol is None else next((i for i, c in enumerate(cfg["volatility"]) if vol < c), len(cfg["volatility"]))
    width = (fair["bull"] - fair["bear"]) / fair["base"] if fair["base"] > 0 else float("inf")
    if width > cfg["range_overlay"]:
        level = min(level + 1, len(LEVELS) - 1)
    lo, hi = param("multiples_check")["agree"]
    if dcf_to_multiples is not None and not lo <= dcf_to_multiples <= hi:
        level = min(level + 1, len(LEVELS) - 1)
    return LEVELS[level], width


def decide(value: dict[str, Any], flag_set: dict[str, list[str]], vol: float | None = None) -> dict[str, Any]:
    fv, price = value.get("fair_value"), value["price"]
    if not fv:
        return {"rating": "No rating", "why": [value.get("note") or "no fair value"], "upside_to_base": None}
    ratio = (value.get("multiples_check") or {}).get("dcf_to_multiples")
    level, width = uncertainty(vol, fv, ratio)
    buy, sell = param("rating_bands")[level]
    overweight, underweight = 1 - (1 - buy) / 4, 1 + (sell - 1) / 5
    pfv = price / fv["base"]
    step = 4 if pfv <= buy else 3 if pfv <= overweight else 2 if pfv < underweight else 1 if pfv < sell else 0
    vol_text = "volatility unknown" if vol is None else f"volatility {vol:.0%}"
    methods = "" if ratio is None else f", DCF / industry multiples {ratio:.2f}"
    why = [f"price / base fair value {pfv:.2f} at {level} uncertainty ({vol_text}, range {width:.2f}x base{methods}): Buy "
           f"at or below {buy:.2f}, Overweight to {overweight:.2f}, Underweight from {underweight:.2f}, Sell from {sell:.2f}"]
    if flag_set["red"]:
        step = min(step, 1)
        why.append("red flag caps the rating at Underweight")
    for c in flag_set["caution"]:
        step = max(step - 1, 0)
        why.append(f"one notch off: {c}")
    return {"rating": RATINGS[step], "why": why, "upside_to_base": round(fv["base"] / price - 1, 4),
            "uncertainty": level, "price_to_fair": round(pfv, 3)}


def adjust(decision: dict[str, Any], step: int, reason: str | None) -> dict[str, Any]:
    """Move a rating by *step* notches (the red team's at most one), keeping the reason."""
    if not step or decision["rating"] not in RATINGS:
        return decision
    i = min(max(RATINGS.index(decision["rating"]) + step, 0), len(RATINGS) - 1)
    return dict(decision, rating=RATINGS[i], why=decision["why"] + [reason or f"{step:+d} notch"])
