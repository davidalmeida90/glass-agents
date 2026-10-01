"""Utility functions used in our graph."""

import os
from typing import Optional

from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AnyMessage
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI

from fundamentalist.configuration import Configuration

DEEPSEEK_URL = "https://api.deepseek.com"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"  # Google's OpenAI-compatible endpoint


def get_message_text(msg: AnyMessage) -> str:
    """Get the text content of a message."""
    content = msg.content
    if isinstance(content, str):
        return content
    elif isinstance(content, dict):
        return content.get("text", "")
    else:
        txts = [c if isinstance(c, str) else (c.get("text") or "") for c in content]
        return "".join(txts).strip()


def init_model(config: Optional[RunnableConfig] = None) -> BaseChatModel:
    """Initialize the configured chat model, with an output cap on every call.

    DeepSeek runs with thinking disabled: no hidden reasoning tokens, and no reasoning_content that
    would have to be sent back on every later turn.
    """
    configuration = Configuration.from_runnable_config(config)
    provider, _, model = configuration.model.partition("/")
    if not model:
        provider, model = "", provider
    if provider == "deepseek":
        return ChatOpenAI(
            model=model,
            base_url=DEEPSEEK_URL,
            api_key=os.environ["DEEPSEEK_API_KEY"],
            max_tokens=configuration.max_output_tokens,
            temperature=0,
            max_retries=2,
            timeout=120,
            extra_body={"thinking": {"type": "disabled"}},
        )
    if provider == "google":
        # the free-tier key first: the paid project's prepaid credit ran out on 2026-10-01 (HTTP 402)
        key = os.environ.get("FREETIER_API_KEY") or os.environ["GEMINI_API_KEY"]
        return ChatOpenAI(model=model, base_url=GEMINI_URL, api_key=key,
                          max_tokens=configuration.max_output_tokens, temperature=0, max_retries=2, timeout=120)
    return init_chat_model(model, model_provider=provider or None, max_tokens=configuration.max_output_tokens)
