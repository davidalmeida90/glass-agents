"""Red team: one model call that argues against the desk's rating, using only the evidence the desk verified.

Every objection has a type, a direction and citations: evidence IDs (e.g. CAP-2) or valuation figures by
name, and may carry a numeric correction to one valuation input (starting growth or operating margin). Code
checks the citations. A correction from a supported, high-severity business or data objection that cites a
filing fact is applied by revaluing in code, and the new price / fair value sets the rating (one notch at
most): the direction comes from the arithmetic, not from the model's label, which proved unreliable (Pfizer,
2026-10-01: an argument that growth was understated labelled "rating too high"). Criticism of the method itself (discount rate, growth cap, fade, how owner
earnings are defined) applies to every company alike, so it goes to a method review list and never moves a
single rating. A data conflict or business objection moves the rating only when it is high severity, all
its citations exist and at least one is a verified filing fact; the net direction of those decides, one
notch at most. The model argues; the rule decides.

First version (2026-09-30) used one overall verdict and let any supported high objection move the rating:
it said "too high" on 5 of 6 companies, mostly over the method, and once contradicted its own objections.
"""

from __future__ import annotations

import ast
import operator
import re
from typing import Any

from langchain_core.messages import HumanMessage

from fundamentalist.utils import init_model

from fundamentalist.parameters import PARAMS

VALUATION_FIELDS = ["price", "fair_value", "growth_used", "revenue_growth", "implied_growth", "wacc", "operating_margin",
                    "operating_margin_reported", "rd_margin_adjustment",
                    "roic", "sales_to_capital", "effective_tax", "terminal_growth", "terminal_roic", "terminal_share",
                    "ev_to_ebit", "market_ev_to_ebit", "net_debt", "cash_conversion", "sbc_to_revenue", "roe",
                    "implied_roe", "book_value_per_share", "cost_of_equity", "valuation_period"] + list(PARAMS)
EVIDENCE_PREFIXES = ("PERF-", "ACC-", "CAP-", "RISK-", "GUID-", "SEG-")
REF = re.compile(r"\b([A-Z]{2,5}-\d+)(?:\.(value|prior|low|high|mid))?\b")
OPERATING_INCOME = re.compile(r"operating (income|profit|earnings)|income from operations", re.I)
OPEX = re.compile(r"operating (expenses|costs)|costs and expenses|total expenses", re.I)
REVENUE = re.compile(r"revenue|net sales|total sales|\bsales\b", re.I)
GROWTH = re.compile(r"revenue|sales|growth", re.I)

OBJECTIONS_TOOL = {
    "name": "Objections",
    "description": "Submit the strongest objections to the rating and your verdict.",
    "parameters": {
        "type": "object",
        "properties": {
            "objections": {
                "type": "array",
                "maxItems": 4,
                "items": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string", "enum": ["data_conflict", "business", "method"],
                                 "description": "data_conflict: a figure the desk used disagrees with the evidence; "
                                                "business: evidence about the business the rating ignores; method: the "
                                                "valuation method or its fixed assumptions."},
                        "direction": {"type": "string", "enum": ["rating too high", "rating too low"]},
                        "severity": {"type": "string", "enum": ["low", "medium", "high"]},
                        "argument": {"type": "string", "description": "At most 60 words."},
                        "cites": {"type": "array", "items": {"type": "string"},
                                  "description": "Evidence IDs such as PERF-1, or valuation figure names such as implied_growth."},
                        "correction": {"type": ["object", "null"],
                                       "description": "Optional: a formula over evidence IDs that gives the value one "
                                                      "input should take; the desk computes it.",
                                       "properties": {"field": {"type": "string", "enum": ["growth", "operating_margin"]},
                                                      "formula": {"type": "string",
                                                                  "description": "For example 'PERF-4 / PERF-1' or "
                                                                                 "'SEG-2 / SEG-2.prior - 1' or 'GUID-1.mid'."}},
                                       "required": ["field", "formula"]},
                    },
                    "required": ["type", "direction", "severity", "argument", "cites"],
                },
            },
        },
        "required": ["objections"],
    },
}

PROMPT = """You are the red team on an equity research desk. Argue against the desk's rating below: find the strongest reasons it could be wrong, in either direction.

Rules:
- Use only the evidence lines and valuation figures given here. Cite evidence by its ID (for example CAP-2) and valuation figures by their name (for example implied_growth).
- Give each objection its own direction. Look for reasons the rating is too low as hard as for reasons it is too high.
- The valuation uses trailing twelve months from the latest 10-K and 10-Q filings (see valuation_period); the evidence comes from the latest 10-K's fiscal year. A difference between the two periods (for example growth_used vs a 10-K growth figure) is expected and is not a data_conflict.
- Criticism of the valuation method or its fixed assumptions (discount rate, growth cap, the fade, how owner earnings are defined) is type "method": it applies to every company alike and goes to the desk's method review.
- Severity "high" only when the objection alone should change the rating and the cited evidence supports it. Otherwise "medium" or "low".
- Start with "Where to look": it names the input that moves fair value most and what the price needs. Test whether the evidence supports that input before anything else.
- When the evidence supports a different starting revenue growth or operating margin, put a "correction" with a formula over evidence IDs; the desk computes it and revalues. Each ID stands for its number in base units (dollars; a percentage as a decimal); add .prior for the prior-year figure and .low, .high or .mid for an outlook range. Operating margin = operating income / revenue, or 1 - operating expenses / revenue. Growth = revenue / revenue.prior - 1, or a stated growth percentage. Do not compute the number yourself. The direction label is informational.
- operating_margin is R&D-adjusted when R&D is capitalized (operating_margin = operating_margin_reported + rd_margin_adjustment). A margin correction is read on the reported (GAAP) basis, so a reported margin that matches operating_margin_reported is not a correction.
- growth_used is the latest twelve months; passages with IDs starting with Q come from the latest 10-Q and cover that recent period. A 10-K fiscal-year growth figure is older and is not a correction to growth_used.
- No outside knowledge, no news, no prices other than the one given.
- Submit with the Objections tool.

{memo}"""


def focus(valuation: dict[str, Any]) -> list[str]:
    """Where the red team should look first, chosen by code: the input that moves the value most and what the price needs."""
    out = []
    swings = (valuation.get("sensitivity") or {}).get("swings") or {}
    if swings:
        lever, (lo, hi) = max(swings.items(), key=lambda kv: max(abs(v) for v in kv[1]))
        out.append(f"the input that moves fair value most: {lever} (its bear and bull shifts change the base value by "
                   f"{lo:+,.2f} and {hi:+,.2f} per share)")
    if valuation.get("implied_growth") is not None and valuation.get("growth_used") is not None:
        out.append(f"the price implies starting growth of {valuation['implied_growth']:.1%} against {valuation['growth_used']:.1%} used")
    if valuation.get("what_must_be_true"):
        out.append(valuation["what_must_be_true"])
    fw = valuation.get("forward") or {}
    if fw.get("growth"):
        out.append(f"guidance moved starting growth from {fw['growth']['model']:.1%} to {fw['growth']['used']:.1%}")
    if fw.get("margin"):
        out.append(f"segment mix sets a margin path from {fw['margin']['today']:.1%} to {fw['margin']['target']:.1%}")
    return out


def memo_text(ticker: str, valuation: dict[str, Any], decision: dict[str, Any], lines: list[str]) -> str:
    fv = valuation.get("fair_value") or {}
    figures = [f"{k}: {valuation[k]}" for k in VALUATION_FIELDS if k in valuation and k != "fair_value"]
    if fv:
        figures.append(f"fair_value: bear {fv['bear']}, base {fv['base']}, bull {fv['bull']}")
    cap = valuation.get("capital") or {}
    if cap:
        figures.append(f"capital (cost of capital build-up): {cap}")
    params = [f"{p.name}: {p.value} ({p.method}; source {p.source}{'' if p.verified else '; not yet verified'})"
              for p in PARAMS.values()]
    return (f"Company: {ticker}\nDesk rating: {decision['rating']}\nWhy: {'; '.join(decision['why'])}\n"
            f"Method: {valuation.get('method', '')}\n\nWhere to look (computed by the desk):\n- " +
            "\n- ".join(focus(valuation) or ["nothing flagged"]) + "\n\nValuation figures:\n" + "\n".join(figures) +
            "\n\nParameters (cite by name in method objections):\n" + "\n".join(params) +
            "\n\nEvidence (verified against the filings):\n" + "\n".join(lines))


async def red_team(ticker: str, valuation: dict[str, Any], decision: dict[str, Any], lines: list[str],
                   evidence_ids: set[str], config: dict[str, Any]) -> dict[str, Any]:
    """Run the red team once and check its citations."""
    model = init_model(config).bind_tools([OBJECTIONS_TOOL], tool_choice="any")
    msg = await model.ainvoke([HumanMessage(content=PROMPT.format(memo=memo_text(ticker, valuation, decision, lines)))],
                              config=config)
    args = next((tc["args"] for tc in msg.tool_calls if tc["name"] == "Objections"), None) or {}
    known = set(evidence_ids) | set(VALUATION_FIELDS)
    objections = []
    for o in args.get("objections") or []:
        cites = [str(c).strip() for c in o.get("cites") or []]
        o["supported"] = bool(cites) and all(c in known for c in cites)
        o["cites_evidence"] = any(c.startswith(EVIDENCE_PREFIXES) and c in evidence_ids for c in cites)
        objections.append(o)
    return {"objections": objections}


PERIOD_FIELDS = {"growth_used", "revenue_growth", "implied_growth"}


def counts(o: dict[str, Any]) -> bool:
    """Can this objection move the rating?

    A data conflict that only sets a trailing-twelve-month growth figure against 10-K evidence compares two
    periods, not two versions of one fact, so it does not count (first seen on Visa and Meta, 2026-10-01).
    """
    cites = set(o.get("cites") or [])
    period_only = o.get("type") == "data_conflict" and cites & PERIOD_FIELDS and not cites - PERIOD_FIELDS - {
        c for c in cites if c.startswith("PERF-")}
    return bool(o.get("type") in ("data_conflict", "business") and o.get("severity") == "high"
                and o.get("supported") and o.get("cites_evidence") and not period_only)


_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}


def _safe_eval(expr: str) -> float:
    """Arithmetic only: numbers, + - * / and parentheses."""
    def ev(n: ast.AST) -> float:
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return float(n.value)
        if isinstance(n, ast.BinOp) and type(n.op) in _OPS:
            return _OPS[type(n.op)](ev(n.left), ev(n.right))
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, (ast.USub, ast.UAdd)):
            return -ev(n.operand) if isinstance(n.op, ast.USub) else ev(n.operand)
        raise ValueError("only numbers and + - * / are allowed")
    return ev(ast.parse(expr, mode="eval"))


def _unit(unit: str | None) -> float:
    u = (unit or "").lower()
    return (1e9 if "billion" in u else 1e6 if "million" in u else 1e3 if "thousand" in u
            else 0.01 if "%" in u or "percent" in u else 1.0)


def evaluate(formula: str, claims: dict[str, dict[str, Any]]) -> tuple[float, list[dict[str, Any]]]:
    """Value of a correction formula over verified claims, each ID in base units; and the claims it used."""
    used: list[dict[str, Any]] = []

    def sub(m: re.Match) -> str:
        c = claims.get(m.group(1))
        if c is None:
            raise ValueError(f"{m.group(1)} is not a verified evidence ID")
        part = m.group(2) or "value"
        ends = [v for v in (c.get("low"), c.get("high")) if isinstance(v, (int, float))]
        raw = {"value": c.get("value"), "prior": c.get("value_prior"), "low": c.get("low"), "high": c.get("high"),
               "mid": sum(ends) / len(ends) if ends else None}[part]
        if not isinstance(raw, (int, float)):
            raise ValueError(f"{m.group(0)} has no number")
        used.append(c)
        return repr(float(raw) * _unit(c.get("unit")))

    return _safe_eval(REF.sub(sub, formula)), used


def identity(field: str, formula: str, used: list[dict[str, Any]]) -> str | None:
    """Why a correction formula does not compute the field it claims to, or None when it does."""
    text = [f"{c.get('topic', '')} {c.get('statement', '')}" for c in used]
    shape = re.sub(r"\s+", "", REF.sub("X", formula))
    if field == "operating_margin":
        if shape == "X/X" and OPERATING_INCOME.search(text[0]) and not OPEX.search(text[0]) and REVENUE.search(text[1]):
            return None
        if shape == "1-X/X" and OPEX.search(text[0]) and REVENUE.search(text[1]):
            return None
        return "an operating margin must be operating income / revenue or 1 - operating expenses / revenue"
    if all(GROWTH.search(t) for t in text):
        return None
    return "a growth correction may use only revenue or growth figures"


def corrections(result: dict[str, Any], reported_margin: float | None = None,
                claims: dict[str, dict[str, Any]] | None = None) -> dict[str, float]:
    """Numeric corrections from objections that count, the median per field, each computed by code from its
    formula over verified claims. A formula that does not compute its field (Visa: operating expenses / revenue
    sent as the margin), a value without a formula, or a margin far from the reported one is dropped and listed
    in result["rejected"].
    """
    from fundamentalist.parameters import value as param

    band = param("margin_correction_band")
    by_field: dict[str, list[float]] = {}
    result.setdefault("computed", [])
    for o in result["objections"]:
        c = o.get("correction") or {}
        if counts(o) and c.get("field") in ("growth", "operating_margin"):
            if not c.get("formula") or claims is None:
                result.setdefault("rejected", []).append(f"{c['field']} correction without a formula the desk can compute")
                continue
            try:
                v, used = evaluate(str(c["formula"]), claims)
                why = identity(c["field"], str(c["formula"]), used)
            except (ValueError, SyntaxError, ZeroDivisionError) as e:
                v, why = None, f"formula {c['formula']!r} does not compute: {e}"
            result["computed"].append({"field": c["field"], "formula": c["formula"], "value": v, "rejected": why})
            if why or v is None:
                result.setdefault("rejected", []).append(f"{c['field']} = {c['formula']}: {why}")
                continue
            if c["field"] == "operating_margin" and reported_margin and abs(v / reported_margin - 1) > band:
                result.setdefault("rejected", []).append(
                    f"operating margin {v:.1%} is {v / reported_margin - 1:+.0%} from the reported {reported_margin:.1%}")
                continue
            by_field.setdefault(c["field"], []).append(v)
    return {k: sorted(v)[len(v) // 2] for k, v in by_field.items()}


def adjustment(result: dict[str, Any]) -> tuple[int, str | None]:
    """+1, 0 or -1 notch: the net direction of the objections that count."""
    strong = [o for o in result["objections"] if counts(o)]
    net = sum(1 if o.get("direction") == "rating too low" else -1 for o in strong)
    if net == 0:
        return 0, None
    step = 1 if net > 0 else -1
    lead = next(o for o in strong if (o.get("direction") == "rating too low") == (step > 0))
    return step, f"red team ({lead['direction']}, {lead['type']}): {lead['argument'][:140]}"


def method_review(result: dict[str, Any]) -> list[str]:
    return [o["argument"] for o in result["objections"] if o.get("type") == "method"]
