"""Define the reader: an agent that fills an evidence schema from one company's 10-K.

Started from LangChain's data-enrichment template (MIT). Same loop (agent, tools, reflect), with the
web tools replaced by a search over the filing and hard limits on searches and turns, so a run always
ends with the evidence it has instead of looping.
"""

import json
from typing import Any, Dict, List, Literal, Optional, cast

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, ToolMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode

from underwriter import prompts
from underwriter.configuration import Configuration
from underwriter.edgar import load_index
from underwriter.state import InputState, OutputState, State
from underwriter.tools import search_filing
from underwriter.utils import init_model
from underwriter.verifier import verify


def _main_prompt(state: State, configuration: Configuration) -> str:
    meta = load_index(state.ticker).meta
    return configuration.prompt.format(
        info=json.dumps(state.extraction_schema, indent=2), topic=state.topic, company=meta["company"],
        ticker=meta["ticker"], period=meta["period"], filed=meta["filed"], max_searches=configuration.max_searches,
    )


def _searches_done(state: State) -> int:
    return sum(1 for m in state.messages if isinstance(m, AIMessage)
               for tc in m.tool_calls if tc["name"] == "search_filing")


async def call_agent_model(
    state: State, *, config: Optional[RunnableConfig] = None
) -> Dict[str, Any]:
    """Call the model to search the filing or submit its evidence."""
    configuration = Configuration.from_runnable_config(config)

    info_tool = {
        "name": "Info",
        "description": "Call this when you have gathered all the relevant info",
        "parameters": state.extraction_schema,
    }

    messages: List[BaseMessage] = [HumanMessage(content=_main_prompt(state, configuration))] + state.messages
    searches_left = configuration.max_searches - _searches_done(state)
    last_turn = state.loop_step + 1 >= configuration.max_loops or searches_left <= 0
    tools: List[Any] = [info_tool] if last_turn else [search_filing, info_tool]
    if last_turn:
        messages.append(HumanMessage(content=prompts.LAST_TURN))

    model = init_model(config).bind_tools(tools, tool_choice=configuration.tool_choice)
    response = cast(AIMessage, await model.ainvoke(messages))

    info = None
    if response.tool_calls:
        for tool_call in response.tool_calls:
            if tool_call["name"] == "Info":
                info = tool_call["args"]
                break
    if info is not None:
        # Submitting: drop any searches asked for in the same turn
        response.tool_calls = [next(tc for tc in response.tool_calls if tc["name"] == "Info")]
    elif response.tool_calls:
        # Never run more searches than the run has left
        searches = [tc for tc in response.tool_calls if tc["name"] == "search_filing"][:max(searches_left, 0)]
        response.tool_calls = searches
    response_messages: List[BaseMessage] = [response]
    if not response.tool_calls:  # If LLM didn't respect the tool_choice
        response_messages.append(
            HumanMessage(content="Please respond by calling one of the provided tools.")
        )
    return {
        "messages": response_messages,
        "info": info,
        "loop_step": 1,
    }


async def reflect(
    state: State, *, config: Optional[RunnableConfig] = None
) -> Dict[str, Any]:
    """Check the submitted evidence in code, with no model call.

    Replaces the template's LLM checker: each quote is looked up in the passage it cites and each value in
    its quote. Claims that fail go back to the reader with the reason, while turns are left.
    """
    configuration = Configuration.from_runnable_config(config)
    last_message = state.messages[-1]
    if not isinstance(last_message, AIMessage) or not last_message.tool_calls:
        raise ValueError(f"{reflect.__name__} expects an AI message with the Info call. Got: {type(last_message)}")
    claims = (state.info or {}).get("claims") or []
    check = verify(claims, load_index(state.ticker).text_of)
    verified = sum(1 for c in check["claims"] if c["check"]["status"] in ("verified", "number in passage"))
    failed = [c for c in check["claims"] if c["check"]["status"] in ("unverified", "no passage")]
    tool_call_id = last_message.tool_calls[0]["id"]
    if verified >= configuration.min_verified and not failed:
        return {"info": state.info, "messages": [ToolMessage(
            tool_call_id=tool_call_id, name="Info", status="success",
            content=f"Accepted: {verified} of {len(claims)} claims check out against the filing.")]}
    lines = [f"- {c.get('passage_id')}: {c['check']['status']} "
             f"({'quote not found in that passage' if not c['check'].get('quote_verbatim') else 'value not in the quote'}):"
             f" {str(c.get('statement', ''))[:80]}" for c in failed]
    if verified < configuration.min_verified:
        lines.append(f"- only {verified} claims check out; at least {configuration.min_verified} are needed.")
    return {"messages": [ToolMessage(
        tool_call_id=tool_call_id, name="Info", status="error",
        content="Unsatisfactory response:\n" + "\n".join(lines)
                + "\nCopy each quote character for character from the cited passage, or drop the claim.")]}


def route_after_agent(
    state: State, config: RunnableConfig
) -> Literal["reflect", "tools", "call_agent_model", "__end__"]:
    """Schedule the next node after the agent's action, never past the turn limit."""
    configurable = Configuration.from_runnable_config(config)
    last_message = state.messages[-1]
    turns_left = state.loop_step < configurable.max_loops

    if not isinstance(last_message, AIMessage):
        return "call_agent_model" if turns_left else "__end__"
    if last_message.tool_calls and last_message.tool_calls[0]["name"] == "Info":
        # A forced final submission is accepted as is: a check there could not trigger a retry
        return "reflect" if turns_left else "__end__"
    if last_message.tool_calls:
        return "tools"
    return "__end__"


def route_after_checker(
    state: State, config: RunnableConfig
) -> Literal["__end__", "call_agent_model"]:
    """Schedule the next node after the checker's evaluation."""
    configurable = Configuration.from_runnable_config(config)
    last_message = state.messages[-1]

    if state.loop_step < configurable.max_loops:
        if not state.info:
            return "call_agent_model"
        if not isinstance(last_message, ToolMessage):
            raise ValueError(
                f"{route_after_checker.__name__} expected a tool messages. Received: {type(last_message)}."
            )
        if last_message.status == "error":
            return "call_agent_model"
        return "__end__"
    return "__end__"


workflow = StateGraph(
    State, input_schema=InputState, output_schema=OutputState, context_schema=Configuration
)
workflow.add_node(call_agent_model)
workflow.add_node(reflect)
workflow.add_node("tools", ToolNode([search_filing]))
workflow.add_edge("__start__", "call_agent_model")
workflow.add_conditional_edges("call_agent_model", route_after_agent)
workflow.add_edge("tools", "call_agent_model")
workflow.add_conditional_edges("reflect", route_after_checker)

graph = workflow.compile()
graph.name = "EvidenceReader"
