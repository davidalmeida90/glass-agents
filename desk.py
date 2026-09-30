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


def pct(v: float | None, sign: bool = False) -> str:
    return "n/a" if v is None else (f"{v:+.1%}" if sign else f"{v:.1%}")


def valuation_line(val: dict) -> str:
    cap = val.get("capital") or {}
    b = cap.get("beta") or {}
    if val.get("model") == "ddm":
        return (f"dividend discount: dividend per share {val['dividend_per_share']:.2f} (yield {pct(val['dividend_yield'])}),"
                f" growth {pct(val['growth_used'])} fading to {pct(val['terminal_growth'])}, cost of equity"
                f" {pct(val['cost_of_equity'])} = rf {pct(cap.get('risk_free'))} + beta {b.get('used')} x ERP {pct(cap.get('erp'))}")
    if val.get("model") in ("bank", "insurer"):
        return (f"bank: ROE {pct(val['roe'])}, price implies ROE {pct(val['implied_roe'])}, book value per share"
                f" {val['book_value_per_share']:,.2f}; cost of equity {pct(val['cost_of_equity'])} = rf"
                f" {pct(cap.get('risk_free'))} + beta {b.get('used')} x ERP {pct(cap.get('erp'))}")
    rating = cap.get("rating") or {}
    return (f"WACC {pct(val['wacc'])} (rf {pct(cap['risk_free'])} {cap['risk_free_date']}, beta {b.get('used')}"
            f" [{b.get('industry') or 'regression'}; regression {b.get('regression')}], ERP {pct(cap['erp'])},"
            f" Ke {pct(cap['cost_of_equity'])}, rating {rating.get('rating')}"
            f" at coverage {rating.get('coverage')}, Kd {pct(cap['cost_of_debt_pre_tax'])}, E/V {pct(cap['weight_equity'])})\n"
            f"    growth {pct(val['revenue_growth'], True)} (used {pct(val['growth_used'])}), price implies"
            f" {pct(val['implied_growth'], True)}; margin {pct(val['operating_margin'])}, ROIC {pct(val['roic'])},"
            f" sales/capital {val['sales_to_capital']}, SBC {pct(val['sbc_to_revenue'])} of revenue; terminal"
            f" {pct(val['terminal_share'])} of EV; EV/EBIT at base {val['ev_to_ebit']}x vs market {val['market_ev_to_ebit']}x")


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
    from fundamentalist.budget import BudgetExceeded, TokenLedger
    from fundamentalist.decision import RATINGS, adjust, decide, flags
    from fundamentalist.edgar import RISK_STATS, load_index
    from dataclasses import replace
    from fundamentalist import dcf
    from fundamentalist.redteam import corrections, counts, method_review, red_team
    from fundamentalist.schemas import READERS
    from fundamentalist.sizing import annual_volatility, size
    from fundamentalist.parameters import value as param
    from fundamentalist.report import audit, write_memo
    from fundamentalist.valuation import value
    from fundamentalist.verifier import verify

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
    memo_dir = HERE / "runs" / "memos" / time.strftime("%Y%m%d-%H%M%S")
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
                try:
                    claims, cost = await read(ticker, "accounting")
                except Exception as e:  # noqa: BLE001 - e.g. no 10-K under this company's CIK
                    print(f"  accounting: skipped, {e}")
                    break
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
            base = decide(val, fl, vol) if val.get("price") else {"rating": "No rating", "why": [val["note"]], "upside_to_base": None}
            rt, final = None, base
            if base["rating"] in RATINGS and not args.valuation_only and room():
                lines, ids = evidence_lines(evidence)
                ledger = TokenLedger(model, args.max_tokens, args.budget_usd - batch.usd)
                cfg = {"configurable": dict(configurable, max_output_tokens=800), "callbacks": [ledger, batch],
                       "metadata": {"purpose": "red_team"}}
                try:
                    rt = await red_team(ticker, val, base, lines, ids, cfg)
                    fixes = corrections(rt)
                    x = val.get("dcf_inputs")
                    if fixes and x is not None:
                        g_lo, g_hi = param("growth_bounds")  # corrections pass through the same bounds as every input
                        # a margin correction is on the reported basis; add back the R&D capitalization adjustment
                        margin = min(max(fixes["operating_margin"] + val.get("rd_margin_adjustment", 0.0), 0.0), 0.8) \
                            if "operating_margin" in fixes else x.margin
                        y = replace(x, growth=min(max(fixes.get("growth", x.growth), g_lo), g_hi), ebit=x.revenue * margin)
                        fv = {n: round(dcf.value_per_share(dcf.scenario(y, n))["per_share"], 2) for n in ("bear", "base", "bull")}
                        revalued = decide(dict(val, fair_value=fv), fl, vol)
                        step = max(min(RATINGS.index(revalued["rating"]) - RATINGS.index(base["rating"]), 1), -1)
                        final = adjust(base, step, f"red team correction {fixes}: base value {fv['base']:,.2f}, "
                                                   f"P/FV {val['price'] / fv['base']:.2f}" if step else None)
                        rt["revalued"] = {"fixes": fixes, "fair_value": fv, "step": step}
                except BudgetExceeded as e:
                    print(f"  red team stopped: {e}")
                costs[f"red_team_{i + 1}"] = {k: ledger.summary()[k] for k in ("calls", "tokens", "cached", "usd")}
            repeats.append({"flags": fl, "base": base, "red_team": rt, "final": final})

        ratings = [r["final"]["rating"] for r in repeats]
        ranked = sorted(ratings, key=lambda r: RATINGS.index(r) if r in RATINGS else -1)
        modal = ranked[(len(ranked) - 1) // 2]  # the median rating (lower middle for an even count)
        confidence = round(ratings.count(modal) / len(ratings), 2)
        sized = size(modal, confidence, vol)
        memo = {"ticker": ticker, "rating": modal, "confidence": confidence, "sizing": sized, "valuation": val,
                "repeats": repeats, "evidence": dict(once, accounting=accounting_runs), "costs": costs}
        memo["audit"] = audit(memo)
        memo["memo_file"] = str(write_memo(memo, memo_dir, time.strftime("%Y-%m-%d")).relative_to(HERE))
        memos.append(memo)

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
    passed = [m["ticker"] for m in memos if not m["audit"]]
    print(f"audit: {len(passed)} of {len(memos)} memos add up")
    for m in memos:
        if m["audit"]:
            print(f"  {m['ticker']}: {'; '.join(m['audit'])}")
    ratios = sorted(m["valuation"]["price"] / m["valuation"]["fair_value"]["base"] for m in memos
                    if (m["valuation"].get("fair_value") or {}).get("base"))
    if ratios:
        median = ratios[len(ratios) // 2] if len(ratios) % 2 else (ratios[len(ratios) // 2 - 1] + ratios[len(ratios) // 2]) / 2
        verdict = "consistent with the market on average" if 0.8 <= median <= 1.25 else "check the ERP, rates or growth settings"
        print(f"market consistency: median price / fair value {median:.2f} over {len(ratios)} companies ({verdict})")
    print(f"memos: {memo_dir.relative_to(HERE)}")
    bs = batch.summary()
    print(f"batch: {len(memos)} companies in {time.time() - t_batch:.0f}s, {bs['calls']} model calls, {bs['tokens']:,} tokens"
          f" ({bs['cached']:,} cached), ${bs['usd']:.4f} of ${args.budget_usd:.2f}")
    print(f"\n{'ticker':<6} {'rating':<11} {'agree':>5} {'weight':>6} {'price':>9} {'bear':>9} {'base':>9} {'bull':>9} {'upside':>7}  key figure")
    for m in memos:
        v, fv = m["valuation"], m["valuation"].get("fair_value") or {}
        key = (f"ROE {pct(v.get('roe'))} vs implied {pct(v.get('implied_roe'))}" if v.get("model") in ("bank", "insurer") and fv else
               f"DDM: yield {pct(v.get('dividend_yield'))}, growth {pct(v.get('growth_used'))}, Ke {pct(v.get('cost_of_equity'))}"
               if v.get("model") == "ddm" and fv else
               f"WACC {pct(v.get('wacc'))}, growth {pct(v.get('growth_used'))} vs implied {pct(v.get('implied_growth'), True)}"
               if fv else (v.get("note") or "")[:60])
        up = fv["base"] / v["price"] - 1 if fv else None
        print(f"{m['ticker']:<6} {m['rating']:<11} {m['confidence']:>5.0%} {m['sizing']['weight']:>6.1%} {v.get('price') or 0:>9,.2f} "
              + (f"{fv['bear']:>9,.2f} {fv['base']:>9,.2f} {fv['bull']:>9,.2f} {up:>+7.0%}" if fv else f"{'':>9} {'':>9} {'':>9} {'':>7}")
              + f"  {key}")
    out = HERE / "runs"
    out.mkdir(exist_ok=True)
    stamp = time.strftime('%Y%m%d-%H%M%S')
    path = out / f"memo-{stamp}.json"
    if not args.valuation_only:
        from track import record
        print(f"track record: {record(stamp, memos)} ratings added to data/track_record.csv (score with: python track.py score)")
    path.write_text(json.dumps({"batch": bs, "budget_usd": args.budget_usd, "repeats": args.repeats, "memos": memos},
                               indent=1, default=str), encoding="utf-8")
    print(f"\nsaved {path.relative_to(HERE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
