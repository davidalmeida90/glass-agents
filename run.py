"""Run one evidence reader on one company with a hard token and dollar budget.

    python run.py MSFT                       # preflight, then the reader, capped at $0.50 and 40,000 tokens
    python run.py MSFT --preflight-only      # only the 1-call check that DeepSeek accepts the settings
    python run.py MSFT --budget-usd 0.10 --max-tokens 20000

Every model call prints one line (tokens in, cached, out, dollars, seconds, tools called, run totals).
Keys come from Agents_model/.env through FIDCS/backend/chaves.py and are never printed.
The run, its evidence, the code verification and the full ledger are saved in runs/.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))
sys.path.insert(0, str(HERE.parent / "FIDCS" / "backend"))


def load_keys() -> None:
    import chaves  # David's key reader: returns values to the program, prints nothing

    os.environ.setdefault("DEEPSEEK_API_KEY", chaves.obter("DEEPSEEK_API_KEY") or "")
    email = chaves.obter("SEC_EDGAR_EMAIL") or ""
    os.environ.setdefault("SEC_USER_AGENT", f"David Arias {email}".strip())
    if not os.environ["DEEPSEEK_API_KEY"]:
        sys.exit("DEEPSEEK_API_KEY is missing from Agents_model/.env")


async def preflight(ledger, model_name: str) -> dict:
    """One tiny call: thinking disabled, and a forced tool call accepted."""
    from langchain_core.messages import HumanMessage

    from underwriter.utils import init_model

    ping = {"name": "Ping", "description": "Reply by calling this tool.",
            "parameters": {"type": "object", "properties": {"ok": {"type": "boolean"}}, "required": ["ok"]}}
    config = {"configurable": {"model": model_name, "max_output_tokens": 50}, "callbacks": [ledger],
              "metadata": {"purpose": "preflight"}}
    result = {"tool_choice_any": False, "error": None}
    try:
        model = init_model(config).bind_tools([ping], tool_choice="any")
        msg = await model.ainvoke([HumanMessage(content="Call the Ping tool with ok=true.")], config=config)
        result["tool_choice_any"] = bool(msg.tool_calls)
    except Exception as e:  # noqa: BLE001 - report the provider's refusal as it came
        result["error"] = f"{type(e).__name__}: {str(e)[:300]}"
    return result


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker")
    ap.add_argument("--budget-usd", type=float, default=0.50)
    ap.add_argument("--max-tokens", type=int, default=40_000)
    ap.add_argument("--model", default="deepseek/deepseek-flash")
    ap.add_argument("--preflight-only", action="store_true")
    args = ap.parse_args()

    load_keys()
    from underwriter.budget import BudgetExceeded, TokenLedger
    from underwriter.edgar import load_index
    from underwriter.graph import graph
    from underwriter.schemas import EVIDENCE_SCHEMA, PERFORMANCE_TASK
    from underwriter.verifier import verify

    index = load_index(args.ticker)
    index.served.clear()
    m = index.meta
    print(f"{m['company']} {m['form']} period {m['period']}, filed {m['filed']}: {len(index.passages)} passages")
    print(f"budget: ${args.budget_usd:.2f} and {args.max_tokens:,} tokens, model {args.model}, thinking off\n")

    ledger = TokenLedger(args.model.split("/")[-1], args.max_tokens, args.budget_usd)
    t0 = time.time()
    pre = await preflight(ledger, args.model)
    print(f"  preflight: forced tool call {'accepted' if pre['tool_choice_any'] else 'NOT accepted'}"
          f"{'; ' + pre['error'] if pre['error'] else ''}\n")
    if args.preflight_only:
        print(json.dumps(ledger.summary()))
        return 0

    configurable = {"model": args.model}
    if not pre["tool_choice_any"]:
        configurable["tool_choice"] = None
    stopped, last = None, {}
    try:
        async for last in graph.astream(
            {"ticker": args.ticker, "topic": PERFORMANCE_TASK, "extraction_schema": EVIDENCE_SCHEMA},
            config={"configurable": configurable, "callbacks": [ledger], "recursion_limit": 20},
            stream_mode="values",
        ):
            pass
    except BudgetExceeded as e:
        stopped = str(e)
    except Exception as e:  # noqa: BLE001 - keep the ledger and the last evidence even when the run fails
        stopped = f"{type(e).__name__}: {str(e)[:300]}"
    info = last.get("info")
    turns = last.get("loop_step", 0)

    claims = (info or {}).get("claims") or []
    check = verify(claims, index.text_of)
    s = ledger.summary()
    print(f"\n{'STOPPED: ' + stopped if stopped else 'finished'} in {time.time() - t0:.1f}s, {turns} agent turns")
    print(f"calls {s['calls']}  tokens {s['tokens']:,} (in {s['input']:,}, cached {s['cached']:,}, out {s['output']:,}"
          f"{', reasoning ' + format(s['reasoning'], ',') if s['reasoning'] else ''})  cost ${s['usd']:.4f}"
          f" of ${args.budget_usd:.2f}  passages shown {len(index.served)} of {len(index.passages)}")
    print(f"claims {check['total']}: " + ", ".join(f"{k} {v}" for k, v in sorted(check["counts"].items())))
    for c in check["claims"]:
        print(f"  [{c['check']['status']:<17}] {c.get('topic', ''):<10} {c.get('value')} {c.get('unit') or ''}"
              f" ({c.get('period') or '?'}) {c.get('passage_id')}: {str(c.get('statement', ''))[:90]}")

    runs = HERE / "runs"
    runs.mkdir(exist_ok=True)
    path = runs / f"{time.strftime('%Y%m%d-%H%M%S')}-{args.ticker.upper()}.json"
    path.write_text(json.dumps({"ticker": args.ticker.upper(), "filing": m, "model": args.model, "stopped": stopped,
                                "preflight": pre, "ledger": {"summary": s, "calls": ledger.calls},
                                "passages_served": sorted(index.served), "verification": check}, indent=1),
                    encoding="utf-8")
    print(f"\nsaved {path.relative_to(HERE)}")
    return 0 if not stopped else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
