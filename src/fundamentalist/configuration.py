"""Define the configurable parameters for the agent."""

from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import Annotated, Optional

from langchain_core.runnables import RunnableConfig, ensure_config

from fundamentalist import prompts


@dataclass(kw_only=True)
class Configuration:
    """The configuration for the agent."""

    model: Annotated[str, {"__template_metadata__": {"kind": "llm"}}] = field(
        default="deepseek/deepseek-flash",
        metadata={
            "description": "The name of the language model to use for the agent. "
            "Should be in the form: provider/model-name."
        },
    )

    prompt: str = field(
        default=prompts.MAIN_PROMPT,
        metadata={
            "description": "The main prompt template. Expects {info}, {topic}, {company}, "
            "{ticker}, {period}, {filed} and {max_searches}."
        },
    )

    passages_per_search: int = field(
        default=4,
        metadata={
            "description": "Passages returned by one search of the filing (about 350 tokens each)."
        },
    )

    max_searches: int = field(
        default=3,
        metadata={
            "description": "Searches allowed in one run. After that only the Info tool is offered."
        },
    )

    max_loops: int = field(
        default=4,
        metadata={
            "description": "Agent turns allowed. The last turn may only submit Info, "
            "so a run always ends with the evidence it has."
        },
    )

    max_output_tokens: int = field(
        default=1500,
        metadata={"description": "Output cap for every model call."},
    )

    min_verified: int = field(
        default=4,
        metadata={"description": "Claims that must check out against the filing before the evidence is accepted."},
    )

    tool_choice: Optional[str] = field(
        default="any",
        metadata={
            "description": "Forced tool choice; None lets the model answer freely "
            "(needed if the provider rejects tool_choice)."
        },
    )

    @classmethod
    def from_runnable_config(
        cls, config: Optional[RunnableConfig] = None
    ) -> Configuration:
        """Load configuration w/ defaults for the given invocation."""
        config = ensure_config(config)
        configurable = config.get("configurable") or {}
        _fields = {f.name for f in fields(cls) if f.init}
        return cls(**{k: v for k, v in configurable.items() if k in _fields})
