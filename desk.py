"""The whole desk on one or more companies.

    python desk.py --tickers MSFT,AAPL --budget-usd 0.50
    python desk.py --tickers MSFT --valuation-only        # free: SEC and Yahoo only, no model calls

Per company: the performance, capital and risk readers run once and the accounting reader --repeats times;
valuation, flags and the base rating are code; the red team runs once per repeat and can move the rating
one notch; the noise meter is the agreement of the repeats' final ratings; sizing is code. Budgets: each
model run stops at --max-tokens and the whole batch at --budget-usd, checked on every call.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import time
from collections import Counter

from run import HERE, load_keys, preflight, run_reader  # noqa: E402  (run.py sets up sys.path)

ONCE = ["performance", "capital", "risks"]
PREFIX = {"performance": "PERF", "accounting": "ACC", "capital": "CAP", "risks": "RISK"}
OK = ("verified", "number in passage")


def money(v: float | None) -> str:
    if v is None:
        return "n/a"
    return f"{v / 1e9:,.1f}B" if abs(v) >= 1e9 else f"{v / 1e6:,.0f}M"


def evidence_lines(evidence: dict[str, list[dict]]) -> tuple[list[str], set[str]]:
    """Verified claims as short lines with IDs the red team can cite."""
    lines, ids = [], set()
    for reader, claims in evidence.items():
        for i, c in enumerate([c for c in claims if c["check"]["status"] in OK], 1):
            cid = f"{PREFIX[reader]}-{i}"
            ids.add(cid)
            num = f" (value {c.get('value')} {c.get('unit') or ''}, {c.get('period') or ''})" if c.get("value") is not None else ""
            lines.append(f"[{cid}] {c.get('topic')}: {str(c.get('statement', ''))[:160]}{num}")
    return lines, ids


def valuation_line(val: dict) -> str:
    if "roe" in val:
        return (f"bank: ROE {val['roe']:.1%}, price implies ROE {val['implied_roe']:.1%}, book value per share"
                f" {val['book_value_per_share']:,.2f}")
    return (f"owner earnings {money(val['owner_earnings'])}, FCF {money(val.get('fcf'))}, revenue growth"
            f" {val['revenue_growth']:+.1%} (used {val['growth_used']:.1%}), price implies {val['implied_growth']:+.1%},"
            f" net debt {money(val['net_debt'])}, cash conversion {val['cash_conversion']}")


async def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tickers", required=True)
    ap.add_argument("--repeats", type=int, default=3, help="noise meter: accounting reader and red team runs")
    ap.add_argument("--budget-usd", type=float, default=0.50)
    ap.add_argument("--max-tokens", type=int, default=40_000)
    ap.add_argument("--model", default="deepseek/deepseek-flash")
    ap.add_argument("--valuation-only", action="store_true")
    args = ap.parse_args()
    tickers = [t.strip().upper() for t in args.tickers.split(",") if t.strip()]

    load_keys()
    from underwriter.budget import BudgetExceeded, TokenLedger
    from underwriter.decision import RATINGS, adjust, decide, flags
    from underwriter.edgar import RISK_STATS, load_index
    from underwriter.redteam import adjustment, counts, method_review, red_team
    from underwriter.schemas import READERS
    from underwriter.sizing import annual_volatility, size
    from underwriter.valuation import value
    from underwriter.verifier import verify

    model = args.model.split("/")[-1]
    batch = TokenLedger(model, max_tokens=10**9, max_usd=args.budget_usd, echo=False)
    configurable = {"model": args.model}
    if not args.valuation_only:
        pre = await preflight([TokenLedger(model, args.max_tokens, args.budget_usd), batch], args.model)
        print(f"  preflight: forced tool call {'accepted' if pre['tool_choice_any'] else 'NOT accepted'}\n")
        if not pre["tool_choice_any"]:
            configurable["tool_choice"] = None

    def room() -> bool:
        return batch.usd < args.budget_usd

    async def read(ticker: str, name: str) -> tuple[list[dict], dict]:
        reader = READERS[name]
        corpus = load_index(ticker, reader.corpus)
        ledger = TokenLedger(model, args.max_tokens, args.budget_usd - batch.usd)
        print(f"  reader {name}")
        last, stopped = await run_reader(ticker, reader, configurable, [ledger, batch])
        check = verify(((last.get("info") or {}).get("claims")) or [], corpus.text_of)
        s = ledger.summary()
        return check["claims"], {k: s[k] for k in ("calls", "tokens", "cached", "usd")} | {"stopped": stopped}

    memos, t_batch = [], time.time()
    for ticker in tickers:
        print(f"=== {ticker}")
        once, costs, accounting_runs = {}, {}, []
        if not args.valuation_only:
            for name in ONCE:
                if not room():
                    break
                try:
                    once[name], costs[name] = await read(ticker, name)
                except Exception as e:  # noqa: BLE001 - a missing filing skips that reader
                    print(f"  {name}: skipped, {e}")
            for i in range(args.repeats):
                if not room():
                    break
                claims, cost = await read(ticker, "accounting")
                accounting_runs.append(claims)
                costs[f"accounting_{i + 1}"] = cost
        try:
            val = value(ticker)
            vol = annual_volatility(ticker)
        except Exception as e:  # noqa: BLE001 - no XBRL or no price: no rating
            val, vol = {"ticker": ticker, "price": None, "fair_value": None, "note": f"valuation failed: {e}"}, None

        repeats = []
        for i in range(max(len(accounting_runs), 1)):
            evidence = dict(once, accounting=accounting_runs[i]) if accounting_runs else dict(once)
            fl = flags(val, evidence, RISK_STATS.get(ticker)) if val.get("price") else {"red": [], "caution": []}
            base = decide(val, fl) if val.get("price") else {"rating": "No rating", "why": [val["note"]], "upside_to_base": None}
            rt, final = None, base
            if base["rating"] in RATINGS and not args.valuation_only and room():
                lines, ids = evidence_lines(evidence)
                ledger = TokenLedger(model, args.max_tokens, args.budget_usd - batch.usd)
                cfg = {"configurable": dict(configurable, max_output_tokens=800), "callbacks": [ledger, batch],
                       "metadata": {"purpose": "red_team"}}
                try:
                    rt = await red_team(ticker, val, base, lines, ids, cfg)
                    final = adjust(base, *adjustment(rt))
                except BudgetExceeded as e:
                    print(f"  red team stopped: {e}")
                costs[f"red_team_{i + 1}"] = {k: ledger.summary()[k] for k in ("calls", "tokens", "cached", "usd")}
            repeats.append({"flags": fl, "base": base, "red_team": rt, "final": final})

        ratings = [r["final"]["rating"] for r in repeats]
        top = max(Counter(ratings).values())
        modal = min((r for r in set(ratings) if ratings.count(r) == top),
                    key=lambda r: RATINGS.index(r) if r in RATINGS else -1)  # ties: the more cautious rating
        confidence = round(top / len(ratings), 2)
        sized = size(modal, confidence, vol)
        memos.append({"ticker": ticker, "rating": modal, "confidence": confidence, "sizing": sized, "valuation": val,
                      "repeats": repeats, "evidence": dict(once, accounting=accounting_runs), "costs": costs})

        fv = val.get("fair_value") or {}
        first = repeats[0]
        print(f"\n  {ticker}: {modal.upper()} (agreement {confidence:.0%}: {', '.join(ratings)})  target weight"
              f" {sized['weight']:.1%}  price {val.get('price') or 0:,.2f}"
              + (f"  fair value {fv['bear']:,.2f} / {fv['base']:,.2f} / {fv['bull']:,.2f}" if fv else ""))
        if fv:
            print(f"    {valuation_line(val)}; volatility {vol:.0%}" if vol else f"    {valuation_line(val)}")
        for w in first["final"]["why"]:
            print(f"    - {w}")
        if first["red_team"]:
            rt = first["red_team"]
            by_type = Counter(o.get("type") for o in rt["objections"])
            moving = [o for o in rt["objections"] if counts(o)]
            print(f"    red team: {len(rt['objections'])} objections ({', '.join(f'{k} {n}' for k, n in by_type.items())}),"
                  f" {len(moving)} can move the rating ({', '.join(o['direction'] for o in moving) or 'none'})")
        spent = sum(c["usd"] for c in costs.values())
        toks = sum(c["tokens"] for c in costs.values())
        print(f"    model spend {toks:,} tokens, ${spent:.4f} | batch ${batch.usd:.4f} of ${args.budget_usd:.2f}\n")
        if not room():
            print("batch dollar cap reached")
            break

    reviews = [(m["ticker"], a) for m in memos for r in m["repeats"] if r["red_team"] for a in method_review(r["red_team"])]
    if reviews:
        print(f"method review ({len(reviews)} points raised by the red team; they never move a rating):")
        for t, a in reviews[:12]:
            print(f"  {t}: {a[:150]}")
        print()
    bs = batch.summary()
    print(f"batch: {len(memos)} companies in {time.time() - t_batch:.0f}s, {bs['calls']} model calls, {bs['tokens']:,} tokens"
          f" ({bs['cached']:,} cached), ${bs['usd']:.4f} of ${args.budget_usd:.2f}")
    print(f"\n{'ticker':<6} {'rating':<11} {'agree':>5} {'weight':>6} {'price':>9} {'bear':>9} {'base':>9} {'bull':>9} {'upside':>7}  key figure")
    for m in memos:
        v, fv = m["valuation"], m["valuation"].get("fair_value") or {}
        key = (f"ROE {v['roe']:.1%} vs implied {v['implied_roe']:.1%}" if "roe" in v else
               f"growth {v['growth_used']:.1%} vs implied {v['implied_growth']:+.1%}" if fv else (v.get("note") or "")[:40])
        up = fv["base"] / v["price"] - 1 if fv else None
        print(f"{m['ticker']:<6} {m['rating']:<11} {m['confidence']:>5.0%} {m['sizing']['weight']:>6.1%} {v.get('price') or 0:>9,.2f} "
              + (f"{fv['bear']:>9,.2f} {fv['base']:>9,.2f} {fv['bull']:>9,.2f} {up:>+7.0%}" if fv else f"{'':>9} {'':>9} {'':>9} {'':>7}")
              + f"  {key}")
    out = HERE / "runs"
    out.mkdir(exist_ok=True)
    path = out / f"memo-{time.strftime('%Y%m%d-%H%M%S')}.json"
    path.write_text(json.dumps({"batch": bs, "budget_usd": args.budget_usd, "repeats": args.repeats, "memos": memos},
                               indent=1, default=str), encoding="utf-8")
    print(f"\nsaved {path.relative_to(HERE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
