"""Offline tests: no network, no API key, no cost."""

from uuid import uuid4

import pytest
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.outputs import ChatGeneration, LLMResult

from fundamentalist.budget import BudgetExceeded, TokenLedger
from fundamentalist.edgar import FilingIndex
from fundamentalist.graph import route_after_agent
from fundamentalist.state import State
from fundamentalist.verifier import numbers, verify

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

    from fundamentalist import edgar
    from fundamentalist.graph import reflect

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
    from fundamentalist.edgar import risk_changes

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



def _inputs(**kw):
    from fundamentalist.dcf import Inputs

    base = dict(revenue=100.0, ebit=20.0, effective_tax=0.0, marginal_tax=0.0, invested_capital=100.0,
                operating_capital=100.0, growth=0.0,
                terminal_growth=0.0, wacc=0.10, terminal_excess_return=0.0, high_growth_years=5, fade_years=5,
                mid_year=False, debt=0.0, cash=0.0, minority=0.0, shares=1.0, mature_wacc=None)
    return Inputs(**(base | kw))


def test_fcff_dcf_matches_a_perpetuity():
    from fundamentalist.dcf import value_per_share

    # no growth, no reinvestment, no tax: 20 a year forever at 10% is 200
    assert abs(value_per_share(_inputs())["per_share"] - 200.0) < 1e-6
    # the equity bridge: debt 50 and cash 30 take 20 off
    assert abs(value_per_share(_inputs(debt=50.0, cash=30.0))["per_share"] - 180.0) < 1e-6


def test_growth_without_excess_return_adds_no_terminal_value():
    from fundamentalist.dcf import value_per_share

    # terminal ROIC = WACC: the terminal value is next year's NOPAT / WACC, whatever the terminal growth
    for g in (0.0, 0.03):
        out = value_per_share(_inputs(terminal_growth=g))
        rev = 100.0
        for k in range(1, 6):
            rev *= 1 + g * k / 5
        expected = rev * (1 + g) * 0.2 / 0.10
        undiscounted = out["terminal_share"] * out["enterprise_value"] * 1.10 ** 10
        assert abs(undiscounted - expected) < 1e-6


def test_reverse_dcf_inverts_the_value():
    from fundamentalist.dcf import implied_growth, value_per_share

    x = _inputs(growth=0.12, terminal_growth=0.02)
    price = value_per_share(x)["per_share"]
    assert abs(implied_growth(_inputs(terminal_growth=0.02), price) - 0.12) < 1e-6

def test_decision_bands_and_flags():
    from fundamentalist.decision import decide, flags

    fv = {"bear": 90.0, "base": 100.0, "bull": 110.0}           # narrow range: no overlay
    none = {"red": [], "caution": []}
    low = 0.15                                                    # Low uncertainty: Buy <= 0.80, Sell >= 1.25
    assert decide({"price": 78.0, "fair_value": fv}, none, low)["rating"] == "Buy"
    assert decide({"price": 92.0, "fair_value": fv}, none, low)["rating"] == "Overweight"   # <= 0.95
    assert decide({"price": 100.0, "fair_value": fv}, none, low)["rating"] == "Hold"
    assert decide({"price": 110.0, "fair_value": fv}, none, low)["rating"] == "Underweight"  # >= 1.05
    assert decide({"price": 130.0, "fair_value": fv}, none, low)["rating"] == "Sell"
    # Very High uncertainty needs a deeper discount: 0.65 of fair value is Overweight, not Buy
    assert decide({"price": 65.0, "fair_value": fv}, none, 0.55)["rating"] == "Overweight"
    # a wide range moves uncertainty up one level
    wide = {"bear": 20.0, "base": 100.0, "bull": 190.0}      # width 1.7x base, above the 1.5x overlay
    assert decide({"price": 78.0, "fair_value": wide}, none, low)["uncertainty"] == "Medium"
    ok = {"status": "verified"}
    ev = {"accounting": [{"topic": "internal_control", "quote": "our internal control was not effective", "check": ok},
                         {"topic": "internal_control", "quote": "there were no material weaknesses", "check": ok}]}
    f = flags({"cash_conversion": 0.5}, ev, {"sentences_now": 100, "new_count": 30})
    assert len(f["red"]) == 1 and len(f["caution"]) == 2
    assert decide({"price": 78.0, "fair_value": fv}, f, low)["rating"] == "Sell"  # Buy capped at Underweight, 2 notches off
    assert decide({"price": 10.0, "fair_value": None, "note": "banks"}, none)["rating"] == "No rating"


def test_clean_control_wording_raises_no_red_flag():
    from fundamentalist.decision import flags

    ok = {"status": "verified"}
    ev = {"accounting": [{"topic": "internal_control", "check": ok,
                          "quote": "Management did not identify any material weaknesses in internal control"},
                         {"topic": "internal_control", "check": ok, "quote": "there were no identified material weaknesses"}]}
    assert flags({"cash_conversion": 1.1}, ev, None)["red"] == []


def test_red_team_moves_a_rating_only_with_supported_high_objections():
    from fundamentalist.decision import adjust
    from fundamentalist.redteam import adjustment

    base = {"rating": "Buy", "why": ["x"], "upside_to_base": 0.3}
    def o(**kw):
        return dict({"type": "business", "direction": "rating too high", "severity": "high", "supported": True,
                     "cites_evidence": True, "argument": "a"}, **kw)
    weak = {"objections": [o(supported=False), o(severity="medium"), o(type="method"), o(cites_evidence=False)]}
    assert adjustment(weak) == (0, None)                      # unsupported, medium, method, no filing fact cited
    balanced = {"objections": [o(), o(direction="rating too low")]}
    assert adjustment(balanced) == (0, None)                  # opposite directions cancel
    strong = {"objections": [o(argument="capex"), o(type="data_conflict")]}
    step, reason = adjustment(strong)
    assert step == -1 and adjust(base, step, reason)["rating"] == "Overweight"
    assert adjust(dict(base, rating="Sell"), -1, "r")["rating"] == "Sell"  # never below the scale
    assert adjust(dict(base, rating="No rating"), -1, "r")["rating"] == "No rating"


def test_sizing_scales_by_volatility_and_confidence():
    from fundamentalist.sizing import size

    assert size("Hold", 1.0, 0.2)["weight"] == 0.0
    assert size("Buy", 1.0, 0.25)["weight"] == 0.05
    assert size("Buy", 1.0, 0.50)["weight"] == 0.025          # twice as volatile, half the weight
    assert size("Buy", 2 / 3, 0.25)["weight"] == round(0.05 * 2 / 3, 4)
    assert size("Buy", 1.0, 0.05)["weight"] == 0.075           # scaling capped at 1.5x


def test_justified_price_to_book():
    # ROE 15%, g 3%, r 10%: P/B = 0.12 / 0.07
    assert abs((0.15 - 0.03) / (0.10 - 0.03) - 1.7142857) < 1e-6



def test_moat_from_roic_history():
    from fundamentalist.valuation import moat

    wide = [{"roic": r} for r in (0.30, 0.28, 0.25, 0.27, 0.31)]
    assert moat(wide, 0.09)[0] == 1.0
    narrow = [{"roic": r} for r in (0.12, 0.08, 0.11, 0.10, 0.09)]
    assert moat(narrow, 0.09)[0] == 0.5
    none = [{"roic": r} for r in (0.05, 0.06, 0.04)]
    assert moat(none, 0.09)[0] == 0.0



def test_excess_return_model():
    from fundamentalist.valuation import excess_return_value

    # ROE equal to Ke: worth exactly book value
    assert abs(excess_return_value(100.0, 0.10, 0.10, 0.03, 1.0) - 100.0) < 1e-9
    # higher ROE adds value, and more when the excess survives (moat share 1 vs 0)
    assert excess_return_value(100.0, 0.16, 0.10, 0.03, 1.0) > excess_return_value(100.0, 0.16, 0.10, 0.03, 0.0) > 100.0


def test_high_growth_decays_by_year_five():
    from fundamentalist.dcf import value_per_share

    out = value_per_share(_inputs(growth=0.30, terminal_growth=0.03, year5_growth_cap=0.10))
    growth = [row["growth"] for row in out["forecast"]]
    assert abs(growth[0] - 0.30) < 1e-9 and abs(growth[4] - 0.10) < 1e-9 and abs(growth[-1] - 0.03) < 1e-9
    slow = value_per_share(_inputs(growth=0.06, terminal_growth=0.03, year5_growth_cap=0.10))
    assert all(abs(r["growth"] - 0.06) < 1e-9 for r in slow["forecast"][:5])  # plateau below the cap


def test_period_mismatch_is_not_a_data_conflict():
    from fundamentalist.redteam import counts

    base = {"type": "data_conflict", "severity": "high", "supported": True, "cites_evidence": True}
    assert not counts(dict(base, cites=["growth_used", "PERF-2"]))            # TTM growth vs a 10-K figure
    assert counts(dict(base, cites=["net_debt", "CAP-1"]))                    # a real figure against evidence


def test_verifier_survives_a_date_in_the_value_field():
    out = verify([{"value": "2024-01-01", "passage_id": "P001", "quote": "Revenue was $281.7 billion"}], PASSAGES.get)
    assert out["claims"][0]["check"]["status"] == "verified"



def test_red_team_corrections_take_the_median_of_counting_objections():
    from fundamentalist.redteam import corrections

    ok = {"type": "business", "severity": "high", "supported": True, "cites_evidence": True, "cites": ["PERF-3"]}
    result = {"objections": [dict(ok, correction={"field": "growth", "value": 0.06}),
                             dict(ok, correction={"field": "growth", "value": 0.08}),
                             dict(ok, correction={"field": "growth", "value": 0.10}),
                             dict(ok, severity="medium", correction={"field": "operating_margin", "value": 0.5})]}
    assert corrections(result) == {"growth": 0.08}



def test_research_asset_straight_line():
    from fundamentalist.valuation import research_asset

    # flat R&D of 10 a year over a 5-year life: asset = 10 x (5+4+3+2+1)/5 = 30, amortization = 10
    annual = {f"20{y}-12-31": 10.0 for y in range(10, 26)}
    asset, amortization = research_asset(10.0, annual, 5)
    assert abs(asset - 30.0) < 1e-9 and abs(amortization - 10.0) < 1e-9
