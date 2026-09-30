"""Red team: one model call that argues against the desk's rating, using only the evidence the desk verified.

Every objection must cite evidence IDs (e.g. CAP-2) or valuation figures by name. Code then checks the
citations: an objection whose citations do not all exist is ignored. Only a supported objection of high
severity can move the rating, by one notch at most, in the direction of the red team's verdict. The model
argues; the rule decides.
"""

from __future__ import annotations

from typing import Any

from langchain_core.messages import HumanMessage

from underwriter.utils import init_model

VALUATION_FIELDS = ["price", "fair_value", "growth_used", "revenue_growth", "implied_growth", "owner_earnings",
                    "net_debt", "cash_conversion", "roe", "implied_roe", "book_value_per_share"]

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
                        "category": {"type": "string",
                                      "enum": ["valuation", "growth", "accounting", "risk", "capital", "data_gap"]},
                        "severity": {"type": "string", "enum": ["low", "medium", "high"]},
                        "argument": {"type": "string", "description": "At most 60 words."},
                        "cites": {"type": "array", "items": {"type": "string"},
                                  "description": "Evidence IDs such as PERF-1, or valuation figure names such as implied_growth."},
                    },
                    "required": ["category", "severity", "argument", "cites"],
                },
            },
            "verdict": {"type": "string", "enum": ["rating stands", "rating too high", "rating too low"]},
        },
        "required": ["objections", "verdict"],
    },
}

PROMPT = """You are the red team on an equity research desk. Argue against the desk's rating below: find the strongest reasons it could be wrong, in either direction.

Rules:
- Use only the evidence lines and valuation figures given here. Cite evidence by its ID (for example CAP-2) and valuation figures by their name (for example implied_growth).
- Severity "high" only when the objection alone should change the rating and the cited evidence supports it. Otherwise "medium" or "low".
- No outside knowledge, no news, no prices other than the one given.
- Submit with the Objections tool.

{memo}"""


def memo_text(ticker: str, valuation: dict[str, Any], decision: dict[str, Any], lines: list[str]) -> str:
    fv = valuation.get("fair_value") or {}
    figures = [f"{k}: {valuation[k]}" for k in VALUATION_FIELDS if k in valuation and k != "fair_value"]
    if fv:
        figures.append(f"fair_value: bear {fv['bear']}, base {fv['base']}, bull {fv['bull']}")
    return (f"Company: {ticker}\nDesk rating: {decision['rating']}\nWhy: {'; '.join(decision['why'])}\n"
            f"Method: {valuation.get('method', '')}\n\nValuation figures:\n" + "\n".join(figures) +
            "\n\nEvidence (verified against the 10-K):\n" + "\n".join(lines))


async def red_team(ticker: str, valuation: dict[str, Any], decision: dict[str, Any], lines: list[str],
                   evidence_ids: set[str], config: dict[str, Any]) -> dict[str, Any]:
    """Run the red team once and check its citations."""
    model = init_model(config).bind_tools([OBJECTIONS_TOOL], tool_choice="any")
    msg = await model.ainvoke([HumanMessage(content=PROMPT.format(memo=memo_text(ticker, valuation, decision, lines)))],
                              config=config)
    args = next((tc["args"] for tc in msg.tool_calls if tc["name"] == "Objections"), None) or {}
    known = evidence_ids | set(VALUATION_FIELDS)
    objections = []
    for o in args.get("objections") or []:
        cites = [str(c).strip() for c in o.get("cites") or []]
        o["supported"] = bool(cites) and all(c in known for c in cites)
        objections.append(o)
    return {"objections": objections, "verdict": args.get("verdict", "rating stands")}


def adjustment(result: dict[str, Any]) -> tuple[int, str | None]:
    """+1, 0 or -1 notch: only a supported high-severity objection, in the verdict's direction."""
    strong = [o for o in result["objections"] if o.get("supported") and o.get("severity") == "high"]
    if not strong or result["verdict"] == "rating stands":
        return 0, None
    step = -1 if result["verdict"] == "rating too high" else 1
    return step, f"red team ({result['verdict']}): {strong[0]['argument'][:140]}"
