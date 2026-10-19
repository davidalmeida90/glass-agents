"""Forward track record: every run's ratings are kept, and scored against later prices. No backtest.

    python track.py score                     # 90, 180 and 365 days: long-short excess return vs SPY, by variant
    python track.py score --horizons 30,90
    python track.py show                      # what is recorded so far

The forward test asks one question: does the LLM layer add anything over the code-only valuation? desk.py records
every rating with its variant, `code` (valuation, flags and rating from SEC, FRED and Yahoo data, no model call) or
`full` (readers, forward drivers, red team and noise meter on top), and the snapshot of the readers' model
(`model_snapshot`, empty for code). DeepSeek moves its `deepseek-flash` alias to a new snapshot every few weeks and
its API answers with the alias name only, so the snapshot is declared in SNAPSHOTS, and each (variant, snapshot)
is scored as its own series: an alias move starts a new one.

Rows recorded before 2026-10-19 carry neither column. All came from full runs whose readers ran on DeepSeek V4.1
Flash as served before the 2026-10-17 update (released 2026-09-10, as reports of DeepSeek's change log date it),
so they read as variant full, snapshot deepseek-v4.1-flash-0910 (LEGACY). The file is rewritten with the two
columns the first time a run records into it.

Scoring, for a horizon of h days: a rating counts once its price date is more than h days old. Its excess return
is the stock's total return (adjusted closes) from the price date to the last close on or before the price date
plus h days, minus SPY's over the same dates. A series' long-short return is the equal-weight mean excess return
of its Buy and Overweight ratings minus that of its Underweight and Sell ratings; hits are longs that beat SPY
and shorts that lagged it. Each full series is also set against the code ratings of the same companies on the
same days, the one comparison that holds names and dates fixed. One rating per company, day and variant counts:
the day's last run.
"""

from __future__ import annotations

import argparse
import bisect
import csv
from collections.abc import Callable
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
TRACK = HERE / "data" / "track_record.csv"
FIELDS = ["run", "date", "ticker", "rating", "confidence", "uncertainty", "model", "price", "price_date", "bear", "base",
          "bull", "price_to_fair", "target_weight", "variant", "model_snapshot"]
ORDER = ["Buy", "Overweight", "Hold", "Underweight", "Sell"]
LONG, SHORT = ("Buy", "Overweight"), ("Underweight", "Sell")
HORIZONS = (90, 180, 365)
LEGACY = {"variant": "full", "model_snapshot": "deepseek-v4.1-flash-0910"}
# alias -> the snapshot it serves; update when DeepSeek moves the alias (about every five weeks)
SNAPSHOTS = {"deepseek-flash": "deepseek-v4.1-flash-1017"}  # since 2026-10-17

Closes = Callable[[str], list[tuple[str, float]]]


def snapshot(served: list[str], alias: str) -> str:
    """The readers' snapshot: the names the API reported when they say more than the alias, else the declared one."""
    named = sorted({s for s in served if s and s != alias})
    return "+".join(named) if named else SNAPSHOTS.get(alias, alias)


def load(path: Path = TRACK) -> list[dict]:
    """Every recorded row, with variant and snapshot filled in for rows recorded before the columns existed."""
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    for r in rows:
        if not r.get("variant"):
            r["variant"], r["model_snapshot"] = LEGACY["variant"], r.get("model_snapshot") or LEGACY["model_snapshot"]
        r["model_snapshot"] = r.get("model_snapshot") or ""
    return rows


def migrate(path: Path = TRACK) -> int:
    """Rewrite a file recorded before the variant and snapshot columns; returns the rows rewritten (0: already current)."""
    if not path.exists():
        return 0
    with open(path, encoding="utf-8") as fh:
        header = next(csv.reader(fh), [])
    if header == FIELDS:
        return 0
    rows = load(path)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows({k: r.get(k, "") for k in FIELDS} for r in rows)
    return len(rows)


def record(run: str, memos: list[dict], variant: str = "full", model_snapshot: str = "", path: Path = TRACK) -> int:
    """Append one row per rated company; a (run, ticker, variant) already recorded, or a memo cut by the budget, is skipped."""
    migrate(path)
    seen = {(r["run"], r["ticker"], r["variant"]) for r in load(path)}
    rows = []
    for m in memos:
        v, fv = m["valuation"], m["valuation"].get("fair_value") or {}
        if not fv or m.get("cut_by_budget") or (run, m["ticker"], variant) in seen:
            continue
        first = m["repeats"][0]["final"]
        rows.append({"run": run, "date": date.today().isoformat(), "ticker": m["ticker"], "rating": m["rating"],
                     "confidence": m["confidence"], "uncertainty": first.get("uncertainty", ""), "model": v.get("model", ""),
                     "price": round(v["price"], 4), "price_date": v.get("price_date"), "bear": fv["bear"], "base": fv["base"],
                     "bull": fv["bull"], "price_to_fair": round(v["price"] / fv["base"], 4),
                     "target_weight": m["sizing"]["weight"], "variant": variant,
                     "model_snapshot": model_snapshot if variant == "full" else ""})
    if rows:
        new = not path.exists()
        path.parent.mkdir(exist_ok=True)
        with open(path, "a", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=FIELDS)
            if new:
                w.writeheader()
            w.writerows(rows)
    return len(rows)


def close_on(series: list[tuple[str, float]], day: str) -> tuple[str, float] | None:
    """The last (date, close) on or before *day*; *series* is sorted by date."""
    i = bisect.bisect_right([d for d, _ in series], day)
    return series[i - 1] if i else None


def excess_return(row: dict, days: int, closes: Closes) -> float | None:
    """Stock minus SPY total return from the rating's price date to the last close on or before it plus *days*."""
    start = row["price_date"]
    end = (date.fromisoformat(start) + timedelta(days=days)).isoformat()
    stock, spy = closes(row["ticker"]), closes("SPY")
    p1, p2, s1, s2 = close_on(stock, start), close_on(stock, end), close_on(spy, start), close_on(spy, end)
    if None in (p1, p2, s1, s2) or p2[0] <= start:
        return None
    return (p2[1] / p1[1] - 1) - (s2[1] / s1[1] - 1)


def long_short(rated: list[tuple[str, float]]) -> dict:
    """Equal-weight Buy + Overweight minus Underweight + Sell, from (rating, excess return) pairs, with hit counts."""
    longs = [x for r, x in rated if r in LONG]
    shorts = [x for r, x in rated if r in SHORT]
    out = {"n": len(rated), "long_n": len(longs), "short_n": len(shorts), "hold_n": len(rated) - len(longs) - len(shorts),
           "long": sum(longs) / len(longs) if longs else None, "short": sum(shorts) / len(shorts) if shorts else None,
           "long_hits": sum(x > 0 for x in longs), "short_hits": sum(x < 0 for x in shorts)}
    out["long_short"] = None if out["long"] is None or out["short"] is None else out["long"] - out["short"]
    out["hits"] = out["long_hits"] + out["short_hits"]
    return out


def latest(rows: list[dict]) -> list[dict]:
    """One rating per company, day and variant: the day's last run."""
    return list({(r["date"], r["ticker"], r["variant"]): r for r in rows}.values())


def series_key(r: dict) -> str:
    return r["variant"] if r["variant"] == "code" else f"{r['variant']} / {r['model_snapshot'] or 'snapshot unknown'}"


def score_rows(rows: list[dict], days: int, closes: Closes, today: date) -> dict[str, dict]:
    """Per series: the long-short over all due ratings, by rating day, and (full series) the code ratings on the same days."""
    rows = latest(rows)
    due = [r for r in rows if date.fromisoformat(r["price_date"]) + timedelta(days=days) < today]
    xs = {id(r): excess_return(r, days, closes) for r in due}
    scored = [r for r in due if xs[id(r)] is not None]
    code = {(r["date"], r["ticker"]): r for r in scored if r["variant"] == "code"}
    out: dict[str, dict] = {}
    for key in sorted({series_key(r) for r in scored}):
        mine = [r for r in scored if series_key(r) == key]
        res = {"all": long_short([(r["rating"], xs[id(r)]) for r in mine]),
               "by_date": {d: long_short([(r["rating"], xs[id(r)]) for r in mine if r["date"] == d])
                           for d in sorted({r["date"] for r in mine})},
               "missing": sum(1 for r in due if series_key(r) == key and xs[id(r)] is None)}
        if not key.startswith("code"):
            same = [code[(r["date"], r["ticker"])] for r in mine if (r["date"], r["ticker"]) in code]
            res["code_same"] = long_short([(r["rating"], xs[id(r)]) for r in same]) if same else None
            res["full_same"] = long_short([(r["rating"], xs[id(r)]) for r in mine if (r["date"], r["ticker"]) in code]) \
                if same else None
        out[key] = res
    return out


def yahoo_closes(start: str) -> Closes:
    """Adjusted daily closes from Yahoo, fetched once per ticker from *start*."""
    cache: dict[str, list[tuple[str, float]]] = {}

    def closes(ticker: str) -> list[tuple[str, float]]:
        if ticker not in cache:
            import yfinance as yf

            hist = yf.Ticker(ticker).history(start=start, auto_adjust=True).dropna(subset=["Close"])
            cache[ticker] = [(d.strftime("%Y-%m-%d"), float(c)) for d, c in zip(hist.index, hist["Close"])]
        return cache[ticker]

    return closes


def _pct(v: float | None) -> str:
    return "n/a" if v is None else f"{v:+.1%}"


def _line(s: dict) -> str:
    return (f"long {s['long_n']} (mean {_pct(s['long'])}, {s['long_hits']} beat SPY)  short {s['short_n']} (mean "
            f"{_pct(s['short'])}, {s['short_hits']} lagged SPY)  hold {s['hold_n']}  long-short {_pct(s['long_short'])}"
            f"  hits {s['hits']}/{s['long_n'] + s['short_n']}")


def score(horizons: tuple[int, ...] = HORIZONS, path: Path = TRACK, closes: Closes | None = None,
          today: date | None = None) -> None:
    rows = load(path)
    if not rows:
        print("no ratings recorded yet: run desk.py first")
        return
    today = today or date.today()
    counts: dict[str, int] = {}
    for r in latest(rows):
        counts[series_key(r)] = counts.get(series_key(r), 0) + 1
    print(f"{len(latest(rows))} ratings (one per company, day and variant): "
          + ", ".join(f"{k} {n}" for k, n in sorted(counts.items())))
    first = min(date.fromisoformat(r["price_date"]) for r in rows)
    closes = closes or yahoo_closes((first - timedelta(days=10)).isoformat())
    for days in horizons:
        print(f"\nhorizon {days} days")
        res = score_rows(rows, days, closes, today)
        if not res:
            print(f"  nothing due yet: the first ratings can be scored from {first + timedelta(days=days + 1)}")
            continue
        for key, s in res.items():
            print(f"  {key}: {s['all']['n']} ratings scored" + (f" ({s['missing']} without prices)" if s["missing"] else ""))
            print(f"    {_line(s['all'])}")
            if len(s["by_date"]) > 1:
                for d, sd in s["by_date"].items():
                    print(f"    rated {d}: long-short {_pct(sd['long_short'])}, hits {sd['hits']}/{sd['long_n'] + sd['short_n']}")
            if "code_same" in s:
                if s["code_same"] is None:
                    print("    no code ratings of the same companies on the same days")
                else:
                    f, c = s["full_same"], s["code_same"]
                    gap = None if f["long_short"] is None or c["long_short"] is None else f["long_short"] - c["long_short"]
                    print(f"    same {c['n']} companies and days, code only: {_line(c)}")
                    print(f"    full minus code on them: {_pct(gap)}")
        n = sum(s["all"]["n"] for s in res.values())
        if n < 30:
            print(f"  only {n} scored ratings at {days} days: too few to say whether the ratings work")


def show(path: Path = TRACK) -> None:
    rows = load(path)
    if not rows:
        print("no ratings recorded yet")
        return
    print(f"{len(rows)} ratings over {len({r['run'] for r in rows})} runs")
    for r in rows[-25:]:
        print(f"{r['date']} {r['ticker']:<6} {r['rating']:<11} P/FV {float(r['price_to_fair']):.2f} ({r['uncertainty']})"
              f"  {series_key(r)}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["score", "show"])
    ap.add_argument("--horizons", default=",".join(map(str, HORIZONS)), help="days, comma separated")
    a = ap.parse_args()
    score(tuple(int(h) for h in a.horizons.split(","))) if a.command == "score" else show()
