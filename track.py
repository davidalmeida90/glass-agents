"""Forward track record: every full run's ratings are kept, and scored against later prices. No backtest.

    python track.py score                 # ratings at least 90 days old, return vs SPY by rating
    python track.py score --min-days 30
    python track.py show                  # what is recorded so far

desk.py appends to data/track_record.csv after each full run (not after --valuation-only). Scoring fetches today's
closes from Yahoo; excess return = stock return minus SPY return over the same dates. A rating works when Buy and
Overweight beat SPY on average and Underweight and Sell lag it. With few records the numbers mean little; the
script says so.
"""

from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
TRACK = HERE / "data" / "track_record.csv"
FIELDS = ["run", "date", "ticker", "rating", "confidence", "uncertainty", "model", "price", "price_date", "bear", "base",
          "bull", "price_to_fair", "target_weight"]
ORDER = ["Buy", "Overweight", "Hold", "Underweight", "Sell"]


def record(run: str, memos: list[dict]) -> int:
    """Append one row per rated company; a run already recorded is skipped."""
    seen = set()
    if TRACK.exists():
        with open(TRACK, encoding="utf-8") as fh:
            seen = {(r["run"], r["ticker"]) for r in csv.DictReader(fh)}
    rows = []
    for m in memos:
        v, fv = m["valuation"], m["valuation"].get("fair_value") or {}
        if not fv or (run, m["ticker"]) in seen:
            continue
        first = m["repeats"][0]["final"]
        rows.append({"run": run, "date": date.today().isoformat(), "ticker": m["ticker"], "rating": m["rating"],
                     "confidence": m["confidence"], "uncertainty": first.get("uncertainty", ""), "model": v.get("model", ""),
                     "price": round(v["price"], 4), "price_date": v.get("price_date"), "bear": fv["bear"], "base": fv["base"],
                     "bull": fv["bull"], "price_to_fair": round(v["price"] / fv["base"], 4),
                     "target_weight": m["sizing"]["weight"]})
    if rows:
        new = not TRACK.exists()
        TRACK.parent.mkdir(exist_ok=True)
        with open(TRACK, "a", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=FIELDS)
            if new:
                w.writeheader()
            w.writerows(rows)
    return len(rows)


def _close(ticker: str, day: str | None = None) -> tuple[float, str]:
    import yfinance as yf

    hist = yf.Ticker(ticker).history(period="10d" if day is None else "max", auto_adjust=True).dropna(subset=["Close"])
    if day is not None:
        hist = hist[hist.index.strftime("%Y-%m-%d") <= day]
    return float(hist["Close"].iloc[-1]), hist.index[-1].strftime("%Y-%m-%d")


def score(min_days: int) -> None:
    if not TRACK.exists():
        print("no ratings recorded yet: run desk.py without --valuation-only first")
        return
    with open(TRACK, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    today = date.today()
    due = [r for r in rows if (today - date.fromisoformat(r["date"])).days >= min_days]
    if not due:
        first = min(date.fromisoformat(r["date"]) for r in rows)
        print(f"{len(rows)} ratings recorded, none {min_days} days old yet; the first can be scored from "
              f"{first.fromordinal(first.toordinal() + min_days)}")
        return
    by_rating: dict[str, list[float]] = {}
    for r in due:
        start = r["price_date"]
        p1, _ = _close(r["ticker"], start)
        p2, _ = _close(r["ticker"])
        s1, _ = _close("SPY", start)
        s2, _ = _close("SPY")
        excess = (p2 / p1 - 1) - (s2 / s1 - 1)
        by_rating.setdefault(r["rating"], []).append(excess)
        print(f"{r['date']} {r['ticker']:<6} {r['rating']:<11} excess vs SPY {excess:+.1%}")
    print()
    for rating in ORDER:
        xs = by_rating.get(rating, [])
        if xs:
            beat = sum(x > 0 for x in xs)
            print(f"{rating:<11} n={len(xs):>3}  mean excess {sum(xs) / len(xs):+.1%}  beat SPY {beat}/{len(xs)}")
    if len(due) < 30:
        print(f"\nonly {len(due)} scored ratings: too few to say whether the ratings work")


def show() -> None:
    if not TRACK.exists():
        print("no ratings recorded yet")
        return
    with open(TRACK, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    print(f"{len(rows)} ratings over {len({r['run'] for r in rows})} runs")
    for r in rows[-25:]:
        print(f"{r['date']} {r['ticker']:<6} {r['rating']:<11} P/FV {float(r['price_to_fair']):.2f} ({r['uncertainty']})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["score", "show"])
    ap.add_argument("--min-days", type=int, default=90)
    a = ap.parse_args()
    score(a.min_days) if a.command == "score" else show()
