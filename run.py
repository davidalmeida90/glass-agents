"""Run evidence readers on one or more companies with hard token and dollar budgets.

    python run.py MSFT                                           # performance reader on Microsoft
    python run.py --tickers MSFT,AAPL --readers performance,accounting,capital --budget-usd 0.50
    python run.py MSFT --preflight-only                          # only the 1-call settings check

Two budgets, both checked on every model call: each reader run stops at --max-tokens, and the whole
batch stops at --budget-usd. Every call prints one line (tokens in, cached, out, dollars, seconds,
tools called, run totals). Keys come from Agents_model/.env through FIDCS/backend/chaves.py and are
never printed. Each batch is saved in runs/ with its evidence, the code verification and every call.
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
    os.environ.setdefault("FRED_API_KEY", chaves.obter("FRED_API_KEY") or "")
    os.environ.setdefault("GEMINI_API_KEY", chaves.obter("GEMINI_API_KEY") or "")  # the red team's model family
    email = chaves.obter("SEC_EDGAR_EMAIL") or ""
    os.environ.setdefault("SEC_USER_AGENT", f"David Arias {email}".strip())
    if not os.environ["DEEPSEEK_API_KEY"]:
        sys.exit("DEEPSEEK_API_KEY is missing from Agents_model/.env")


async def preflight(callbacks, model_name: str) -> dict:
    """One tiny call: thinking disabled, and a forced tool call accepted."""
    from langchain_core.messages import HumanMessage

    from fundamentalist.utils import init_model

    ping = {"name": "Ping", "description": "Reply by calling this tool.",
            "parameters": {"type": "object", "properties": {"ok": {"type": "boolean"}}, "required": ["ok"]}}
    config = {"configurable": {"model": model_name, "max_output_tokens": 50}, "callbacks": callbacks,
              "metadata": {"purpose": "preflight"}}
    result = {"tool_choice_any": False, "error": None}
    try:
        model = init_model(config).bind_tools([ping], tool_choice="any")
        msg = await model.ainvoke([HumanMessage(content="Call the Ping tool with ok=true.")], config=config)
        result["tool_choice_any"] = bool(msg.tool_calls)
    except Exception as e:  # noqa: BLE001 - report the provider's refusal as it came
        result["error"] = f"{type(e).__name__}: {str(e)[:300]}"
    return result


async def run_reader(ticker, reader, configurable, callbacks):
    """One reader on one company. Returns the last state and the reason it stopped, if it did."""
    from fundamentalist.budget import BudgetExceeded
    from fundamentalist.edgar import load_index
    from fundamentalist.graph import graph

    load_index(ticker, reader.corpus).served.clear()  # each reader run starts with every passage available
    stopped, last = None, {}
    try:
        async for last in graph.astream(
            {"ticker": ticker, "corpus": reader.corpus, "topic": reader.task, "extraction_schema": reader.schema},
            config={"configurable": dict(configurable, min_verified=reader.min_verified),
                    "callbacks": callbacks, "recursion_limit": 20},
            stream_mode="values",
        ):
            pass
    except BudgetExceeded as e:
        stopped = str(e)
    except Exception as e:  # noqa: BLE001 - keep the ledger and the last evidence even when the run fails
        stopped = f"{type(e).__name__}: {str(e)[:300]}"
    return last, stopped


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker", nargs="?", default=None)
    ap.add_argument("--tickers", default=None, help="comma separated, e.g. MSFT,AAPL")
    ap.add_argument("--readers", default="performance", help="comma separated: performance,accounting,capital")
    ap.add_argument("--budget-usd", type=float, default=0.50, help="cap for the whole batch")
    ap.add_argument("--max-tokens", type=int, default=40_000, help="cap for each reader run")
    ap.add_argument("--model", default="deepseek/deepseek-flash")
    ap.add_argument("--preflight-only", action="store_true")
    args = ap.parse_args()
    tickers = [t.strip().upper() for t in (args.tickers or args.ticker or "").split(",") if t.strip()]
    if not tickers:
        ap.error("give a ticker or --tickers")

    load_keys()
    from fundamentalist.budget import BudgetExceeded, TokenLedger
    from fundamentalist.edgar import load_index
    from fundamentalist.schemas import READERS
    from fundamentalist.verifier import verify

    readers = [READERS[r.strip()] for r in args.readers.split(",")]
    model = args.model.split("/")[-1]
    batch = TokenLedger(model, max_tokens=10**9, max_usd=args.budget_usd, echo=False)
    print(f"batch: {len(tickers)} companies x {len(readers)} readers, model {args.model}, thinking off")
    print(f"budget: ${args.budget_usd:.2f} for the batch, {args.max_tokens:,} tokens per reader run\n")

    t_batch = time.time()
    pre = await preflight([TokenLedger(model, args.max_tokens, args.budget_usd), batch], args.model)
    print(f"  preflight: forced tool call {'accepted' if pre['tool_choice_any'] else 'NOT accepted'}"
          f"{'; ' + pre['error'] if pre['error'] else ''}\n")
    if args.preflight_only:
        return 0
    configurable = {"model": args.model}
    if not pre["tool_choice_any"]:
        configurable["tool_choice"] = None

    results, batch_stop = [], None
    for ticker in tickers:
        try:
            index = load_index(ticker)
        except Exception as e:  # noqa: BLE001 - an unknown ticker or a missing 10-K skips the company
            print(f"{ticker}: skipped, {e}\n")
            results.append({"ticker": ticker, "error": str(e)})
            continue
        m = index.meta
        print(f"{m['company']} {m['form']} period {m['period']}, filed {m['filed']}: {len(index.passages)} passages")
        for reader in readers:
            ledger = TokenLedger(model, args.max_tokens, args.budget_usd - batch.usd)
            try:
                corpus = load_index(ticker, reader.corpus)
            except Exception as e:  # noqa: BLE001 - e.g. no earlier 10-K to compare risk factors with
                print(f" reader {reader.name}: skipped, {e}")
                results.append({"ticker": ticker, "reader": reader.name, "error": str(e)})
                continue
            extra = ""
            if reader.corpus == "risk_changes":
                from fundamentalist.edgar import RISK_STATS
                rs = RISK_STATS.get(ticker, {})
                extra = (f": {rs.get('new_count')} new of {rs.get('sentences_now')} risk sentences vs {rs.get('prior_period')}"
                         f" ({rs.get('removed_count')} removed), {len(corpus.passages)} passages")
            print(f" reader {reader.name}{extra}")
            t0 = time.time()
            last, stopped = await run_reader(ticker, reader, configurable, [ledger, batch])
            claims = ((last.get("info") or {}).get("claims")) or []
            check = verify(claims, corpus.text_of)
            s = ledger.summary()
            ok = check["counts"].get("verified", 0) + check["counts"].get("number in passage", 0)
            row = {"ticker": ticker, "reader": reader.name, "calls": s["calls"], "tokens": s["tokens"],
                   "cached": s["cached"], "output": s["output"], "usd": s["usd"], "seconds": round(time.time() - t0, 1),
                   "turns": last.get("loop_step", 0), "claims": check["total"], "checked_ok": ok,
                   "counts": check["counts"], "stopped": stopped, "passages_shown": len(corpus.served),
                   "verification": check, "ledger": ledger.calls}
            results.append(row)
            print(f"   {'STOPPED: ' + stopped if stopped else 'done'}: {s['calls']} calls, {s['tokens']:,} tokens,"
                  f" ${s['usd']:.4f}, {row['seconds']}s | claims {check['total']}, checked {ok}"
                  f" ({', '.join(f'{k} {v}' for k, v in sorted(check['counts'].items()))})"
                  f" | batch ${batch.usd:.4f} of ${args.budget_usd:.2f}\n")
            if batch.usd >= args.budget_usd or (stopped and "dollar cap" in stopped):
                batch_stop = f"batch dollar cap reached at ${batch.usd:.4f}"
                break
        if batch_stop:
            break

    runs = [r for r in results if "reader" in r and "error" not in r]
    print(f"{'BATCH STOPPED: ' + batch_stop if batch_stop else 'batch finished'} in {time.time() - t_batch:.0f}s")
    print(f"\n{'ticker':<6} {'reader':<11} {'calls':>5} {'tokens':>7} {'cached':>7} {'$':>8} {'sec':>5} {'claims':>6} {'ok':>3}  stopped")
    for r in runs:
        print(f"{r['ticker']:<6} {r['reader']:<11} {r['calls']:>5} {r['tokens']:>7,} {r['cached']:>7,} {r['usd']:>8.4f}"
              f" {r['seconds']:>5} {r['claims']:>6} {r['checked_ok']:>3}  {(r['stopped'] or '')[:40]}")
    bs = batch.summary()
    print(f"\ntotal: {bs['calls']} calls incl. preflight, {bs['tokens']:,} tokens ({bs['cached']:,} cached),"
          f" ${bs['usd']:.4f} of ${args.budget_usd:.2f}")
    for r in runs:
        for c in r["verification"]["claims"]:
            print(f"  {r['ticker']:<5} {r['reader']:<11} [{c['check']['status']:<17}] {c.get('topic', ''):<21}"
                  f" {c.get('value')} {c.get('unit') or ''} {c.get('passage_id')}: {str(c.get('statement', ''))[:70]}")

    out = HERE / "runs"
    out.mkdir(exist_ok=True)
    path = out / f"batch-{time.strftime('%Y%m%d-%H%M%S')}.json"
    path.write_text(json.dumps({"tickers": tickers, "readers": [r.name for r in readers], "model": args.model,
                                "budget_usd": args.budget_usd, "max_tokens_per_run": args.max_tokens,
                                "preflight": pre, "batch": bs, "stopped": batch_stop, "runs": results}, indent=1),
                    encoding="utf-8")
    print(f"\nsaved {path.relative_to(HERE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
