"""Offline tests: no network, no API key, no cost."""

from uuid import uuid4

import pytest
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.outputs import ChatGeneration, LLMResult

from underwriter.budget import BudgetExceeded, TokenLedger
from underwriter.edgar import FilingIndex
from underwriter.graph import route_after_agent
from underwriter.state import State
from underwriter.verifier import numbers, verify

PASSAGES = {
    "P001": "Revenue was $281.7 billion, an increase of 15% compared with fiscal year 2025.",
    "P002": "Net income was $101,832 million. Operating cash flow was (3,210) in the prior year.",
}


def test_numbers_reads_commas_parentheses_and_percent():
    assert numbers("revenue of 245,122 and 16% growth, a loss of (3,210)") == [245122.0, 16.0, -3210.0]


def test_verify_statuses():
    claims = [
        {"value": 281.7, "passage_id": "P001", "quote": "Revenue was $281.7 billion"},          # verbatim
        {"value": 101832, "passage_id": "P002", "quote": "Net income reached 101,832 million"},  # paraphrased
        {"value": 99, "passage_id": "P001", "quote": "Revenue was $99 billion"},                # invented
        {"value": 15, "passage_id": "P999", "quote": "an increase of 15%"},                     # no such passage
    ]
    out = verify(claims, PASSAGES.get)
    assert [c["check"]["status"] for c in out["claims"]] == [
        "verified", "number in passage", "unverified", "no passage"]


def test_search_never_repeats_a_passage_in_a_run():
    idx = FilingIndex.from_text({"ticker": "X"}, "revenue " * 400 + "cash flow " * 400)
    first = [pid for pid, _ in idx.search("revenue", 2)]
    second = [pid for pid, _ in idx.search("revenue", 2)]
    assert first and not set(first) & set(second)


def _result(inp, out):
    msg = AIMessage(content="", usage_metadata={"input_tokens": inp, "output_tokens": out, "total_tokens": inp + out})
    return LLMResult(generations=[[ChatGeneration(message=msg)]])


def test_ledger_stops_at_the_token_cap():
    ledger = TokenLedger("deepseek-flash", max_tokens=1_000, max_usd=1.0, echo=False)
    rid = uuid4()
    ledger.on_chat_model_start({}, [[HumanMessage(content="x")]], run_id=rid)
    with pytest.raises(BudgetExceeded):
        ledger.on_llm_end(_result(900, 200), run_id=rid)


def test_ledger_refuses_a_call_before_sending_it():
    ledger = TokenLedger("deepseek-flash", max_tokens=1_000, max_usd=1.0, echo=False)
    with pytest.raises(BudgetExceeded):
        ledger.on_chat_model_start({}, [[HumanMessage(content="y" * 8_000)]], run_id=uuid4())


def test_ledger_stops_at_the_dollar_cap():
    ledger = TokenLedger("deepseek-flash", max_tokens=10**9, max_usd=0.0001, echo=False)
    rid = uuid4()
    ledger.on_chat_model_start({}, [[HumanMessage(content="x")]], run_id=rid)
    with pytest.raises(BudgetExceeded):
        ledger.on_llm_end(_result(1_000_000, 0), run_id=rid)


def _state(loop_step, last):
    return State(ticker="X", topic="t", extraction_schema={}, messages=[last], loop_step=loop_step)


def test_routing_ends_at_the_turn_limit():
    cfg = {"configurable": {"max_loops": 4}}
    nag = HumanMessage(content="Please respond by calling one of the provided tools.")
    assert route_after_agent(_state(2, nag), cfg) == "call_agent_model"
    assert route_after_agent(_state(4, nag), cfg) == "__end__"
    info = AIMessage(content="", tool_calls=[{"name": "Info", "args": {}, "id": "1"}])
    assert route_after_agent(_state(2, info), cfg) == "reflect"
    assert route_after_agent(_state(4, info), cfg) == "__end__"  # forced final submission is not re-checked


def test_code_checker_accepts_good_evidence_and_returns_specific_failures():
    import asyncio

    from underwriter import edgar
    from underwriter.graph import reflect

    idx = edgar.FilingIndex(meta={"ticker": "ZZZ"}, passages=list(PASSAGES.items()))
    edgar._INDEXES["ZZZ:10-K"] = idx
    good = [{"value": 281.7, "passage_id": "P001", "quote": "Revenue was $281.7 billion", "statement": "s"},
            {"value": 15, "passage_id": "P001", "quote": "an increase of 15%", "statement": "s"},
            {"value": 101832, "passage_id": "P002", "quote": "Net income was $101,832 million", "statement": "s"},
            {"value": -3210, "passage_id": "P002", "quote": "Operating cash flow was (3,210)", "statement": "s"}]
    call = AIMessage(content="", tool_calls=[{"name": "Info", "args": {}, "id": "i1"}])
    ok = asyncio.run(reflect(State(ticker="ZZZ", topic="t", extraction_schema={}, messages=[call],
                                   info={"claims": good}), config={"configurable": {"min_verified": 4}}))
    assert ok["messages"][0].status == "success" and ok["info"]["claims"] == good
    bad = good[:3] + [{"value": 99, "passage_id": "P001", "quote": "Revenue was $99 billion", "statement": "made up"}]
    ko = asyncio.run(reflect(State(ticker="ZZZ", topic="t", extraction_schema={}, messages=[call],
                                   info={"claims": bad}), config={"configurable": {"min_verified": 4}}))
    assert ko["messages"][0].status == "error" and "P001" in ko["messages"][0].content and "info" not in ko


def test_risk_changes_keeps_only_new_sentences():
    from underwriter.edgar import risk_changes

    old = ("Table of contents Item 1A. Risk Factors 12 Item 1B. Unresolved staff comments 20 "
           "Item 1A. Risk Factors Our business depends on consumer demand for our products worldwide. "
           "We rely on third party suppliers for components in 2025 and beyond. "
           "Item 1B. Unresolved Staff Comments None.")
    new = ("Item 1A. Risk Factors Our business depends on consumer demand for our products worldwide. "
           "We rely on third party suppliers for components in 2026 and beyond. "
           "New export controls on advanced chips could restrict our sales to certain countries. "
           "Item 1B. Unresolved Staff Comments None.")
    out = risk_changes(new, old)
    assert out["new"] == ["New export controls on advanced chips could restrict our sales to certain countries."]
    assert out["removed"] == [] and out["sentences_now"] == 3


def test_dcf_matches_a_hand_computation():
    from underwriter.valuation import dcf_per_share

    # no growth anywhere: five years of 100 then a perpetuity of 100 at 10%, minus 0 net debt, 1 share = 1,000
    assert abs(dcf_per_share(100, 0.0, 0.10, 0.0, 1.0, terminal=0.0) - 1000.0) < 1e-6


def test_decision_bands_and_flags():
    from underwriter.decision import decide, flags

    val = {"price": 100.0, "fair_value": {"bear": 110.0, "base": 130.0, "bull": 150.0}, "cash_conversion": 1.2}
    none = {"red": [], "caution": []}
    assert decide(val, none)["rating"] == "Buy"
    assert decide(dict(val, price=140.0), none)["rating"] == "Hold"
    assert decide(dict(val, price=200.0), none)["rating"] == "Sell"
    ok = {"status": "verified"}
    ev = {"accounting": [{"topic": "internal_control", "quote": "our internal control was not effective", "check": ok},
                         {"topic": "internal_control", "quote": "there were no material weaknesses", "check": ok}]}
    f = flags(dict(val, cash_conversion=0.5), ev, {"sentences_now": 100, "new_count": 30})
    assert len(f["red"]) == 1 and len(f["caution"]) == 2
    assert decide(val, f)["rating"] == "Sell"  # Buy capped at Underweight by the red flag, then 2 notches off
    assert decide(val, none)["upside_to_base"] == 0.3
    assert decide({"price": 10.0, "fair_value": None, "note": "banks"}, none)["rating"] == "No rating"


def test_implied_growth_inverts_the_present_value():
    from underwriter.valuation import implied_growth, present_value

    for g in (0.0, 0.08, 0.2):
        assert abs(implied_growth(100.0, present_value(100.0, g)) - g) < 1e-6


def test_clean_control_wording_raises_no_red_flag():
    from underwriter.decision import flags

    ok = {"status": "verified"}
    ev = {"accounting": [{"topic": "internal_control", "check": ok,
                          "quote": "Management did not identify any material weaknesses in internal control"},
                         {"topic": "internal_control", "check": ok, "quote": "there were no identified material weaknesses"}]}
    assert flags({"cash_conversion": 1.1}, ev, None)["red"] == []


def test_red_team_moves_a_rating_only_with_supported_high_objections():
    from underwriter.decision import adjust
    from underwriter.redteam import adjustment

    base = {"rating": "Buy", "why": ["x"], "upside_to_base": 0.3}
    weak = {"verdict": "rating too high", "objections": [
        {"severity": "high", "supported": False, "argument": "cites nothing real"},
        {"severity": "medium", "supported": True, "argument": "minor"}]}
    assert adjustment(weak) == (0, None)
    strong = {"verdict": "rating too high", "objections": [{"severity": "high", "supported": True, "argument": "capex"}]}
    step, reason = adjustment(strong)
    assert step == -1 and adjust(base, step, reason)["rating"] == "Overweight"
    assert adjust(dict(base, rating="Sell"), -1, "r")["rating"] == "Sell"  # never below the scale
    assert adjust(dict(base, rating="No rating"), -1, "r")["rating"] == "No rating"


def test_sizing_scales_by_volatility_and_confidence():
    from underwriter.sizing import size

    assert size("Hold", 1.0, 0.2)["weight"] == 0.0
    assert size("Buy", 1.0, 0.25)["weight"] == 0.05
    assert size("Buy", 1.0, 0.50)["weight"] == 0.025          # twice as volatile, half the weight
    assert size("Buy", 2 / 3, 0.25)["weight"] == round(0.05 * 2 / 3, 4)
    assert size("Buy", 1.0, 0.05)["weight"] == 0.075           # scaling capped at 1.5x


def test_justified_price_to_book():
    # ROE 15%, g 3%, r 10%: P/B = 0.12 / 0.07
    assert abs((0.15 - 0.03) / (0.10 - 0.03) - 1.7142857) < 1e-6
