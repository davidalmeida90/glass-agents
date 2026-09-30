"""The whole desk on one or more companies: readers, code checks, valuation, flags, decision, memo.

    python desk.py --tickers MSFT,AAPL --budget-usd 0.50
    python desk.py --tickers MSFT --valuation-only        # free: SEC and Yahoo only, no model calls

Only the readers call a model; valuation, flags and the rating are code. Both budgets from run.py apply:
each reader run stops at --max-tokens and the whole batch at --budget-usd, checked on every call.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import time
from pathlib import Path

from run import HERE, load_keys, preflight, run_reader  # noqa: E402  (run.py sets up sys.path)

READER_ORDER = ["performance", "accounting", "capital", "risks"]


def money(v: float | None) -> str:
    if v is None:
        return "n/a"
    return f"{v / 1e9:,.1f}B" if abs(v) >= 1e9 else f"{v / 1e6:,.0f}M"


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", required=True)
    ap.add_argument("--readers", default=",".join(READER_ORDER))
    ap.add_argument("--budget-usd", type=float, default=0.50)
    ap.add_argument("--max-tokens", type=int, default=40_000)
    ap.add_argument("--model", default="deepseek/deepseek-flash")
    ap.add_argument("--valuation-only", action="store_true")
    args = ap.parse_args()
    tickers = [t.strip().upper() for t in args.tickers.split(",") if t.strip()]

    load_keys()
    from underwriter.budget import TokenLedger
    from underwriter.decision import decide, flags
    from underwriter.edgar import RISK_STATS, load_index
    from underwriter.schemas import READERS
    from underwriter.valuation import value
    from underwriter.verifier import verify

    readers = [] if args.valuation_only else [READERS[r.strip()] for r in args.readers.split(",")]
    model = args.model.split("/")[-1]
    batch = TokenLedger(model, max_tokens=10**9, max_usd=args.budget_usd, echo=False)
    configurable = {"model": args.model}
    if readers:
        pre = await preflight([TokenLedger(model, args.max_tokens, args.budget_usd), batch], args.model)
        print(f"  preflight: forced tool call {'accepted' if pre['tool_choice_any'] else 'NOT accepted'}\n")
        if not pre["tool_choice_any"]:
            configurable["tool_choice"] = None

    memos, t_batch = [], time.time()
    for ticker in tickers:
        print(f"=== {ticker}")
        evidence, costs = {}, {}
        for reader in readers:
            if batch.usd >= args.budget_usd:
                print("  batch dollar cap reached, readers skipped")
                break
            ledger = TokenLedger(model, args.max_tokens, args.budget_usd - batch.usd)
            try:
                corpus = load_index(ticker, reader.corpus)
            except Exception as e:  # noqa: BLE001
                print(f"  {reader.name}: skipped, {e}")
                continue
            print(f"  reader {reader.name}")
            last, stopped = await run_reader(ticker, reader, configurable, [ledger, batch])
            check = verify(((last.get("info") or {}).get("claims")) or [], corpus.text_of)
            evidence[reader.name] = check["claims"]
            s = ledger.summary()
            costs[reader.name] = {k: s[k] for k in ("calls", "tokens", "cached", "usd")} | {"stopped": stopped}
        try:
            val = value(ticker)
        except Exception as e:  # noqa: BLE001 - a company without XBRL figures gets no rating
            val = {"ticker": ticker, "price": None, "fair_value": None, "note": f"valuation failed: {e}"}
        fl = flags(val, evidence, RISK_STATS.get(ticker)) if val.get("price") else {"red": [], "caution": []}
        dec = decide(val, fl) if val.get("price") else {"rating": "No rating", "why": [val["note"]], "upside_to_base": None}
        memos.append({"ticker": ticker, "valuation": val, "flags": fl, "decision": dec, "evidence": evidence,
                      "costs": costs})

        fv = val.get("fair_value") or {}
        inp = val.get("inputs") or {}
        print(f"\n  {ticker}: {dec['rating'].upper()}  price {val.get('price') or 0:,.2f} ({val.get('price_date')})"
              + (f"  fair value bear {fv['bear']:,.2f} / base {fv['base']:,.2f} / bull {fv['bull']:,.2f}"
                 f"  upside to base {dec['upside_to_base']:+.0%}" if fv else ""))
        if fv:
            print(f"    owner earnings {money(val['owner_earnings'])} (TTM), FCF {money(val['fcf'])}, revenue growth"
                  f" {val['revenue_growth']:+.1%} (used {val['growth_used']:.1%}), price implies {val['implied_growth']:+.1%},"
                  f" net debt {money(val['net_debt'])}, cash conversion {val['cash_conversion']}")
        elif inp:
            print(f"    {val.get('note')}")
        for w in dec["why"]:
            print(f"    - {w}")
        for f in fl["red"]:
            print(f"    RED: {f}")
        spent = sum(c["usd"] for c in costs.values())
        toks = sum(c["tokens"] for c in costs.values())
        ok = sum(1 for cl in evidence.values() for c in cl if c["check"]["status"] in ("verified", "number in passage"))
        n = sum(len(cl) for cl in evidence.values())
        print(f"    evidence {ok} of {n} claims checked against the filing; readers {toks:,} tokens, ${spent:.4f}"
              f" | batch ${batch.usd:.4f} of ${args.budget_usd:.2f}\n")

    bs = batch.summary()
    print(f"batch: {len(tickers)} companies in {time.time() - t_batch:.0f}s, {bs['calls']} model calls, {bs['tokens']:,} tokens"
          f" ({bs['cached']:,} cached), ${bs['usd']:.4f} of ${args.budget_usd:.2f}")
    print(f"\n{'ticker':<6} {'rating':<11} {'price':>9} {'bear':>9} {'base':>9} {'bull':>9} {'upside':>7} {'growth':>7} {'implied':>8}  flags")
    for m in memos:
        fv, d = m["valuation"].get("fair_value") or {}, m["decision"]
        print(f"{m['ticker']:<6} {d['rating']:<11} {m['valuation'].get('price') or 0:>9,.2f} "
              + (f"{fv['bear']:>9,.2f} {fv['base']:>9,.2f} {fv['bull']:>9,.2f} {d['upside_to_base']:>+7.0%}"
                 f" {m['valuation']['growth_used']:>7.1%} {m['valuation']['implied_growth']:>+8.1%}" if fv
                 else f"{'':>9} {'':>9} {'':>9} {'':>7} {'':>7} {'':>8}")
              + f"  {len(m['flags']['red'])} red, {len(m['flags']['caution'])} caution")
    out = HERE / "runs"
    out.mkdir(exist_ok=True)
    path = out / f"memo-{time.strftime('%Y%m%d-%H%M%S')}.json"
    path.write_text(json.dumps({"batch": bs, "budget_usd": args.budget_usd, "memos": memos}, indent=1, default=str),
                    encoding="utf-8")
    print(f"\nsaved {path.relative_to(HERE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
