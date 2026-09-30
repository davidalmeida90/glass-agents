"""The memo an analyst reads, and the audit that checks it before it is written.

audit() recomputes what can be recomputed from the memo's own inputs and says what does not add up.
write_memo() turns one company's result into a Markdown page: rating and why, valuation build-up,
sensitivity, verified evidence with its quotes, red team, noise meter, data notes, parameters and cost.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from fundamentalist import dcf
from fundamentalist.decision import RATINGS
from fundamentalist.parameters import PARAMS

OK = ("verified", "number in passage")


def audit(memo: dict[str, Any]) -> list[str]:
    """Consistency checks on one company's result; an empty list means everything adds up."""
    issues = []
    val, rating = memo["valuation"], memo["rating"]
    fv, x = val.get("fair_value"), val.get("dcf_inputs")
    if fv and isinstance(x, dcf.Inputs):
        base = dcf.value_per_share(dcf.scenario(x, "base"))
        if abs(base["per_share"] - fv["base"]) > 0.01 * abs(fv["base"]) + 0.01:
            issues.append(f"base value does not recompute: {base['per_share']:.2f} vs {fv['base']:.2f}")
        bridge = base["enterprise_value"] - x.debt - x.minority + x.cash
        if abs(bridge - base["equity_value"]) > 1e-6 * max(abs(bridge), 1):
            issues.append("equity bridge does not add up")
        if not x.terminal_growth < (x.mature_wacc if x.mature_wacc is not None else x.wacc):
            issues.append("terminal growth is not below the terminal cost of capital")
        if not fv["bear"] <= fv["base"] <= fv["bull"]:
            issues.append(f"scenarios out of order: {fv}")
    cap = val.get("capital") or {}
    if cap.get("wacc") is not None:
        w = cap["weight_equity"]
        wacc = w * cap["cost_of_equity"] + (1 - w) * cap["cost_of_debt_pre_tax"] * (1 - cap["tax_shield_rate"])
        if abs(wacc - cap["wacc"]) > 0.0005:
            issues.append(f"WACC does not recompute: {wacc:.4f} vs {cap['wacc']:.4f}")
    if rating not in RATINGS and rating != "No rating":
        issues.append(f"unknown rating {rating}")
    if fv and rating == "No rating":
        issues.append("a fair value exists but no rating was given")
    claims = []
    for reader, cl in memo["evidence"].items():
        claims += (cl[0] if cl else []) if reader == "accounting" else cl
    if claims:
        ok = sum(c["check"]["status"] in OK for c in claims)
        if ok / len(claims) < 0.9:
            issues.append(f"only {ok} of {len(claims)} claims check out against the filing")
    return issues


def _pct(v: Any) -> str:
    return "n/a" if v is None else f"{v:.1%}"


def _money(v: Any) -> str:
    if v is None:
        return "n/a"
    return f"{v / 1e9:,.1f}B" if abs(v) >= 1e9 else f"{v / 1e6:,.0f}M"


def write_memo(memo: dict[str, Any], out_dir: Path, as_of: str) -> Path:
    t, val, first = memo["ticker"], memo["valuation"], memo["repeats"][0]
    fv, cap = val.get("fair_value") or {}, val.get("capital") or {}
    b, rating_info = cap.get("beta") or {}, cap.get("rating") or {}
    lines = [f"# {t}: {memo['rating']}", "",
             f"Desk memo, {as_of}. Price {val.get('price', 0):,.2f} ({val.get('price_date')}). Noise meter agreement "
             f"{memo['confidence']:.0%} ({', '.join(r['final']['rating'] for r in memo['repeats'])}). Target weight "
             f"{memo['sizing']['weight']:.1%}.", ""]
    lines += ["## Why", ""] + [f"- {w}" for w in first["final"]["why"]] + [""]
    if memo.get("audit"):
        lines += ["**Audit:** " + "; ".join(memo["audit"]), ""]
    if fv:
        lines += ["## Valuation", "", f"Method: {val.get('method')}", "",
                  "| Bear | Base | Bull | Price / base |", "|---:|---:|---:|---:|",
                  f"| {fv['bear']:,.2f} | {fv['base']:,.2f} | {fv['bull']:,.2f} | {val['price'] / fv['base']:.2f} |", ""]
        if val.get("model") == "bank":
            lines += [f"- ROE {_pct(val['roe'])}; the price implies {_pct(val['implied_roe'])}; book value per share "
                      f"{val['book_value_per_share']:,.2f}; cost of equity {_pct(val['cost_of_equity'])}; {val.get('moat')}", ""]
        else:
            lines += ["| Cost of capital | Value |", "|---|---:|",
                      f"| Risk-free ({cap.get('risk_free_date')}) | {_pct(cap.get('risk_free'))} |",
                      f"| Beta ({b.get('industry') or 'regression'}; regression {b.get('regression')}) | {b.get('used')} |",
                      f"| Equity risk premium | {_pct(cap.get('erp'))} |",
                      f"| Cost of equity | {_pct(cap.get('cost_of_equity'))} |",
                      f"| Synthetic rating (coverage {rating_info.get('coverage')}) | {rating_info.get('rating')} |",
                      f"| Cost of debt, pre-tax | {_pct(cap.get('cost_of_debt_pre_tax'))} |",
                      f"| Equity weight | {_pct(cap.get('weight_equity'))} |",
                      f"| **WACC** (maturing to {_pct(cap.get('mature_wacc'))}) | **{_pct(cap.get('wacc'))}** |", "",
                      f"- Revenue growth {_pct(val['revenue_growth'])} (used {_pct(val['growth_used'])}); the price implies "
                      f"{_pct(val['implied_growth'])}",
                      f"- Operating margin {_pct(val['operating_margin'])} (reported {_pct(val.get('operating_margin_reported'))}"
                      f" + R&D adjustment {_pct(val.get('rd_margin_adjustment'))}), ROIC {_pct(val['roic'])}, sales-to-capital "
                      f"{val['sales_to_capital']}, SBC {_pct(val['sbc_to_revenue'])} of revenue",
                      f"- Moat: {val.get('moat')}",
                      f"- Terminal value {_pct(val['terminal_share'])} of enterprise value; EV/EBIT at base {val['ev_to_ebit']}x "
                      f"vs market {val['market_ev_to_ebit']}x", f"- Period: {val.get('valuation_period')}", ""]
            grid = (val.get("sensitivity") or {}).get("grid") or {}
            if grid:
                cols = list(next(iter(grid.values())))
                lines += ["Base value per share, WACC by terminal growth:", "",
                          "| | " + " | ".join(cols) + " |", "|---|" + "---:|" * len(cols)]
                lines += [f"| {row} | " + " | ".join(f"{v:,.2f}" for v in grid[row].values()) + " |" for row in grid]
                lines += [""]
    else:
        lines += ["## Valuation", "", f"Not valued: {val.get('note')}", ""]
    for note in val.get("data_notes") or []:
        lines.append(f"- Data note: {note}")
    lines += [""]
    lines += ["## Evidence from the latest 10-K (every quote checked against the filing)", ""]
    for reader, claims in memo["evidence"].items():
        if reader == "accounting":
            claims = claims[0] if claims else []
        shown = [c for c in claims if c["check"]["status"] in OK][:6]
        if shown:
            lines.append(f"**{reader}**")
            lines += [f"- {c.get('statement')} ({c.get('passage_id')}: \"{str(c.get('quote', ''))[:160]}\")" for c in shown]
            lines.append("")
    rt = first.get("red_team")
    if rt:
        lines += ["## Red team", ""]
        for o in rt["objections"]:
            lines.append(f"- [{o.get('type')}, {o.get('severity')}, {o.get('direction')}, "
                         f"{'supported' if o.get('supported') else 'unsupported'}] {o.get('argument')} "
                         f"(cites {', '.join(o.get('cites') or [])})")
        if rt.get("revalued"):
            lines.append(f"- Correction applied in code: {rt['revalued']}")
        lines.append("")
    spent = sum(c.get("usd", 0) for c in memo["costs"].values())
    tokens = sum(c.get("tokens", 0) for c in memo["costs"].values())
    lines += ["## Cost", "", f"{tokens:,} tokens, ${spent:.4f} across {len(memo['costs'])} model runs.", "",
              "## Parameters", "", "| Parameter | Value | Source | Verified |", "|---|---|---|---|"]
    lines += [f"| {p.name} | {p.value} | {p.source} | {'yes' if p.verified else 'no'} |" for p in PARAMS.values()]
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{t}.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
