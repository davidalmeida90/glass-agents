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
