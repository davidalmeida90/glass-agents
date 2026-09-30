"""Tools exposed to the reader.

The template's web search and scraping are replaced by one tool over the company's own filing:
keyword search returns a few numbered passages, never the whole document.
"""

from langchain_core.runnables import RunnableConfig
from langchain_core.tools import InjectedToolArg
from langgraph.prebuilt import InjectedState
from typing_extensions import Annotated

from underwriter.configuration import Configuration
from underwriter.edgar import load_index
from underwriter.state import State


async def search_filing(
    query: str,
    *,
    state: Annotated[State, InjectedState],
    config: Annotated[RunnableConfig, InjectedToolArg],
) -> str:
    """Search the company's latest 10-K and return the best matching passages with their IDs.

    Use specific wording from financial statements or MD&A. Passages already shown in this run are not repeated.
    """
    configuration = Configuration.from_runnable_config(config)
    index = load_index(state.ticker)
    hits = index.search(query, configuration.passages_per_search)
    if not hits:
        return "No new passages match this search."
    return "\n\n".join(f"[{pid}] {text}" for pid, text in hits)
