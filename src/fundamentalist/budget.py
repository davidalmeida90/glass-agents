"""Token ledger: every model call is logged as it happens, and the run stops at the budget.

Two checks per call. Before the request, the prompt's size is estimated (characters / 4) and the
call is refused if it would push the run past its token cap. After the reply, the real usage is
added up; crossing either the token cap or the dollar cap stops the run.
"""

from __future__ import annotations

import time
from typing import Any
from uuid import UUID

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult

# $ per million tokens (input, output). DeepSeek Flash from Glassbench's price table; the input price
# is charged on every input token, cache hits included, so the estimate errs high.
PRICES = {"deepseek-flash": (0.14, 0.28),
          "gemini-2.5-flash-lite": (0.10, 0.40)}  # Google paid standard tier, ai.google.dev pricing, 2026-10-01


class BudgetExceeded(RuntimeError):
    """Raised when a run reaches its token or dollar cap."""


class TokenLedger(BaseCallbackHandler):
    """Count tokens and dollars per model call and stop the run at its caps."""

    raise_error = True  # LangChain swallows callback errors unless this is set

    def __init__(self, model: str, max_tokens: int, max_usd: float, echo: bool = True) -> None:
        self.model = model
        self.max_tokens = max_tokens
        self.max_usd = max_usd
        self.echo = echo
        self.calls: list[dict[str, Any]] = []
        self._open: dict[UUID, dict[str, Any]] = {}

    # ------------------------------------------------------------------ totals
    @property
    def tokens(self) -> int:
        return sum(c["input"] + c["output"] for c in self.calls)

    @property
    def usd(self) -> float:
        return sum(c["usd"] for c in self.calls)

    def price(self, inp: int, out: int, model: str | None = None) -> float:
        name = (model or self.model).removeprefix("models/")
        pin, pout = PRICES.get(name, PRICES.get(self.model, (0.14, 0.28)))
        return inp * pin / 1e6 + out * pout / 1e6

    # ------------------------------------------------------------------ callbacks
    def on_chat_model_start(self, serialized: dict[str, Any], messages: list[list[Any]], *, run_id: UUID,
                            metadata: dict[str, Any] | None = None, **kwargs: Any) -> None:
        chars = sum(len(str(getattr(m, "content", m))) for batch in messages for m in batch)
        estimate = chars // 4
        node = (metadata or {}).get("langgraph_node") or (metadata or {}).get("purpose") or "call"
        self._open[run_id] = {"node": node, "estimate_in": estimate, "t0": time.time()}
        if self.tokens + estimate > self.max_tokens:
            raise BudgetExceeded(f"refused before sending: {node} would bring the run to about "
                                 f"{self.tokens + estimate:,} tokens (cap {self.max_tokens:,})")

    def on_llm_end(self, response: LLMResult, *, run_id: UUID, **kwargs: Any) -> None:
        info = self._open.pop(run_id, {"node": "call", "estimate_in": 0, "t0": time.time()})
        gen = response.generations[0][0]
        msg = getattr(gen, "message", None)
        usage = dict(getattr(msg, "usage_metadata", None) or {})
        raw = dict((response.llm_output or {}).get("token_usage") or
                   (getattr(msg, "response_metadata", {}) or {}).get("token_usage") or {})
        inp = int(usage.get("input_tokens") or raw.get("prompt_tokens") or 0)
        out = int(usage.get("output_tokens") or raw.get("completion_tokens") or 0)
        cached = int(raw.get("prompt_cache_hit_tokens") or 0)
        reasoning = int((raw.get("completion_tokens_details") or {}).get("reasoning_tokens") or 0)
        tool_calls = [tc.get("name") for tc in (getattr(msg, "tool_calls", None) or [])]
        served = (getattr(msg, "response_metadata", None) or {}).get("model_name")  # priced by the model that answered
        call = {"n": len(self.calls) + 1, "node": info["node"], "input": inp, "cached": cached, "output": out,
                "reasoning": reasoning, "usd": self.price(inp, out, served), "model": served, "seconds": round(time.time() - info["t0"], 1),
                "estimate_in": info["estimate_in"], "tool_calls": tool_calls}
        self.calls.append(call)
        if self.echo:
            print(f"  call {call['n']:>2} {call['node']:<16} in {inp:>6,} (cached {cached:>5,})  out {out:>5,}"
                  f"{f' (reasoning {reasoning:,})' if reasoning else ''}  ${call['usd']:.5f}  {call['seconds']:>4}s"
                  f"  {','.join(t for t in tool_calls if t) or '-':<22}| run {self.tokens:>6,} tok ${self.usd:.4f}"
                  f" of ${self.max_usd:.2f}", flush=True)
        if self.tokens > self.max_tokens:
            raise BudgetExceeded(f"token cap reached: {self.tokens:,} of {self.max_tokens:,}")
        if self.usd > self.max_usd:
            raise BudgetExceeded(f"dollar cap reached: ${self.usd:.4f} of ${self.max_usd:.2f}")

    def summary(self) -> dict[str, Any]:
        return {"calls": len(self.calls), "input": sum(c["input"] for c in self.calls),
                "cached": sum(c["cached"] for c in self.calls), "output": sum(c["output"] for c in self.calls),
                "reasoning": sum(c["reasoning"] for c in self.calls), "tokens": self.tokens,
                "usd": round(self.usd, 6), "max_tokens": self.max_tokens, "max_usd": self.max_usd}
