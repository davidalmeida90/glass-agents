"""Forward drivers from verified reader claims: the readers' facts reach the valuation through here.

Two drivers, both anchored on the code's own numbers and moved only part of the way (anchor and adjust, as in
CAME, Wu et al., EMNLP 2026):

- guided growth: management's revenue outlook (a growth range, or a full-year revenue range set against the
  last fiscal year's revenue from XBRL) moves the starting growth halfway toward the guided midpoint, at most 5
  points. The comparison base is never the reader's: on Pfizer (2026-10-01) it took the previous guidance for
  last year's revenue. An outlook for a year already past is ignored;
- segment mix: each segment grows at its own latest rate with its own margin for 5 years; the change in the
  mix-weighted margin sets a target the consolidated margin converges to by year 5 (Damodaran's Ginzu target
  margin, chosen from the company's own segments instead of by judgment).

A driver is used only when its numbers passed the code verifier.
"""

from __future__ import annotations

import re
from dataclasses import replace
from typing import Any

from fundamentalist import dcf
from fundamentalist.parameters import value as param

OK = ("verified", "number in passage")
FULL_YEAR = re.compile(r"full[- ]year|fiscal|\bFY|\byear\b|annual", re.I)
SKIP_SEGMENT = re.compile(r"corporate|elimination|unallocated|reconcil|total|other", re.I)


def _ok(c: dict[str, Any]) -> bool:
    return (c.get("check") or {}).get("status") in OK


def _mid(c: dict[str, Any]) -> float | None:
    vals = [float(v) for v in (c.get("low"), c.get("high")) if isinstance(v, (int, float))]
    return sum(vals) / len(vals) if vals else None


def _scale(unit: str | None) -> float:
    u = (unit or "").lower()
    return 1e9 if "billion" in u else 1e6 if "million" in u else 1e3 if "thousand" in u else 1.0


def guided_growth(claims: list[dict[str, Any]], fy_revenue: float | None = None,
                  year: int | None = None) -> tuple[float, str] | None:
    """Midpoint of the revenue outlook as a growth rate; a full-year outlook wins over a quarter's."""
    found = []
    for c in claims:
        mid = _mid(c)
        if not _ok(c) or mid is None:
            continue
        years = [int(y) for y in re.findall(r"20\d\d", str(c.get("period") or ""))]
        if year and years and max(years) < year:
            continue  # an outlook for a year already over
        full = bool(FULL_YEAR.search(str(c.get("period") or "")))
        if c.get("topic") == "revenue_growth":
            g = mid / 100 if "%" in str(c.get("unit") or "%") or abs(mid) > 1 else mid
        elif c.get("topic") == "revenue" and full and fy_revenue:
            g = mid * _scale(c.get("unit")) / fy_revenue - 1
        else:
            continue
        if abs(g) <= 0.6:
            found.append((full, g, f"{c.get('period')}: {c.get('statement', '')[:120]} [{c.get('passage_id')}]"))
    if not found:
        return None
    full, g, why = max(found, key=lambda f: f[0])
    return g, why


def mix_ratio(claims: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Year-5 mix-weighted segment margin over today's, with the segment revenue it covers (in dollars)."""
    cfg = param("forward_drivers")
    seg: dict[str, dict[str, Any]] = {}
    for c in claims:
        name = str(c.get("segment") or "").strip()
        if not _ok(c) or not name or SKIP_SEGMENT.search(name) or not isinstance(c.get("value"), (int, float)):
            continue
        s = seg.setdefault(name.lower(), {"name": name})
        k = _scale(c.get("unit"))
        if c.get("topic") == "revenue" and isinstance(c.get("value_prior"), (int, float)):
            s["rev"], s["rev_prior"] = float(c["value"]) * k, float(c["value_prior"]) * k
        elif c.get("topic") == "operating_income":
            s["oi"] = float(c["value"]) * k
    full = [s for s in seg.values() if s.get("rev", 0) > 0 and s.get("rev_prior", 0) > 0 and "oi" in s]
    if len(full) < 2:
        return None
    rev0, oi0 = sum(s["rev"] for s in full), sum(s["oi"] for s in full)
    if oi0 <= 0:
        return None
    lo, hi = cfg["segment_growth_bounds"]
    h = cfg["mix_horizon"]
    rev5 = {s["name"]: s["rev"] * (1 + min(max(s["rev"] / s["rev_prior"] - 1, lo), hi)) ** h for s in full}
    m5 = sum(s["oi"] / s["rev"] * rev5[s["name"]] for s in full) / sum(rev5.values())
    r_lo, r_hi = cfg["mix_ratio_bounds"]
    ratio = min(max(m5 / (oi0 / rev0), r_lo), r_hi)
    parts = ", ".join(f"{s['name']} margin {s['oi'] / s['rev']:.1%} growth {s['rev'] / s['rev_prior'] - 1:+.1%}" for s in full)
    return {"ratio": ratio, "segment_revenue": rev0, "segments": len(full),
            "why": f"segment mix in {h} years moves the margin by {ratio - 1:+.1%} ({parts})"}


def drivers(evidence: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    guidance = [c for c in evidence.get("guidance") or [] if _ok(c) and c.get("topic") in ("revenue", "revenue_growth")]
    if guidance:
        out["guidance"] = guidance
    m = mix_ratio(evidence.get("segments") or [])
    if m:
        out["mix"] = m
    return out


def apply(x: dcf.Inputs, drv: dict[str, Any] | None, fy_revenue: float | None = None,
          year: int | None = None) -> tuple[dcf.Inputs, dict[str, Any]]:
    """Move the DCF inputs by the drivers; returns the new inputs and what changed, for the memo."""
    if not drv:
        return x, {}
    cfg = param("forward_drivers")
    notes: dict[str, Any] = {}
    guided = guided_growth(drv.get("guidance") or [], fy_revenue, year)
    if guided:
        drv = dict(drv, guided_growth=guided[0], guided_growth_source=guided[1])
        gap = drv["guided_growth"] - x.growth
        step = max(min(cfg["guidance_weight"] * gap, cfg["guidance_cap"]), -cfg["guidance_cap"])
        lo, hi = param("growth_bounds")
        used = min(max(x.growth + step, lo), hi)
        notes["growth"] = {"model": round(x.growth, 4), "guided": round(drv["guided_growth"], 4), "used": round(used, 4),
                           "source": drv.get("guided_growth_source")}
        x = replace(x, growth=used)
    mix = drv.get("mix")
    if mix:
        cover = mix["segment_revenue"] / x.revenue if x.revenue else 0
        c_lo, c_hi = cfg["segment_coverage"]
        if c_lo <= cover <= c_hi:
            target = x.margin * mix["ratio"]
            notes["margin"] = {"today": round(x.margin, 4), "target": round(target, 4), "by_year": cfg["margin_years"],
                               "segments": mix["segments"], "coverage": round(cover, 2), "source": mix["why"]}
            x = replace(x, target_margin=target, margin_years=cfg["margin_years"])
        else:
            notes["margin_skipped"] = f"segments cover {cover:.0%} of revenue (needs {c_lo:.0%} to {c_hi:.0%})"
    return x, notes
