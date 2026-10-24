"""Point-in-time backtest of the code core: valuation and rating, no model calls.

    python backtest.py fetch                                   # universe, prices, XBRL facts (gzipped); once
    python backtest.py run --start 2016-01 --end 2025-09       # value every member at every month end
    python backtest.py report                                  # latest results: rank IC, quintiles, ratings

What it replays: on the last trading day of each month, every current S&P 500 member that was already in the
index on that day is valued with the XBRL facts filed before it (companyfacts 'filed' dates), that day's
close, a beta and volatility from prices up to that day, and Damodaran's implied ERP and T-bond rate from the
end of the year before. No language model runs, so nothing is remembered from the future. The readers and the
red team are left out: they read today's filings.

Leaks left, printed in every report: Damodaran's industry tables (betas, rating spreads, multiples, P/B) are
the January 2026 vintage; SIC codes are today's; the universe holds only today's members, so companies that
left the index are missing (survivorship); share counts come from XBRL alone, adjusted for later splits, so
companies whose only undivided count is old (Visa) drop out.

Baselines, computed on the same rows: book-to-market, EBIT / EV, and the industry multiples value / price.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import os
import subprocess
import sys
import time
import types
import urllib.request
from datetime import date, timedelta
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))
CACHE = HERE / "cache" / "backtest"  # prices.pkl here is written by fetch() on this machine, never downloaded as is
FACTS = CACHE / "facts"
OUT = HERE / "runs" / "backtest"
LEAKS = ("industry EV/EBIT, P/B and P/E are point in time (Damodaran's January file of each year, from 2015); "
         "industry betas and rating spreads are the January 2026 vintage; SIC codes and the industry each company "
         "maps to are today's; universe = today's S&P 500 members from the day each joined (members that left are "
         "missing: survivorship); XBRL share counts only")
RATING_NUM = {"Sell": -2, "Underweight": -1, "Hold": 0, "Overweight": 1, "Buy": 2}


# ---------------------------------------------------------------------------------------------------- fetch
def fetch() -> None:
    import pandas as pd
    import yfinance as yf

    from run import load_keys

    load_keys()
    CACHE.mkdir(parents=True, exist_ok=True)
    FACTS.mkdir(exist_ok=True)
    wiki = CACHE / "sp500_wiki.html"
    if not wiki.exists():
        req = urllib.request.Request("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
                                     headers={"User-Agent": os.environ["SEC_USER_AGENT"]})
        wiki.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    table = pd.read_html(wiki)[0]
    universe = [{"symbol": str(r["Symbol"]).replace(".", "-"), "cik": int(r["CIK"]), "added": str(r["Date added"])[:10],
                 "sector": r["GICS Sector"]} for _, r in table.iterrows()]
    with open(CACHE / "universe.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(universe[0]))
        w.writeheader()
        w.writerows(universe)
    print(f"universe: {len(universe)} members")

    prices = CACHE / "prices.pkl"
    if not prices.exists():
        symbols = [u["symbol"] for u in universe] + ["^GSPC"]
        close, adj, splits = {}, {}, {}
        for i in range(0, len(symbols), 100):
            chunk = symbols[i:i + 100]
            df = yf.download(chunk, start="2009-01-01", auto_adjust=False, actions=True, group_by="ticker",
                             threads=True, progress=False)
            for s in chunk:
                if s not in df.columns.get_level_values(0):
                    continue
                sub = df[s]
                if sub["Close"].dropna().empty:
                    continue
                close[s], adj[s] = sub["Close"], sub["Adj Close"]
                splits[s] = sub["Stock Splits"][sub["Stock Splits"] > 0] if "Stock Splits" in sub else pd.Series(dtype=float)
            print(f"prices: {min(i + 100, len(symbols))} of {len(symbols)}")
        pd.to_pickle({"close": pd.DataFrame(close), "adj": pd.DataFrame(adj), "splits": splits}, prices)

    agent = os.environ["SEC_USER_AGENT"]
    sic: dict[str, str] = json.loads((CACHE / "sic.json").read_text()) if (CACHE / "sic.json").exists() else {}
    for n, u in enumerate(universe, 1):
        target = FACTS / f"{u['symbol']}.json.gz"
        for url, kind in ((f"https://data.sec.gov/api/xbrl/companyfacts/CIK{u['cik']:010d}.json", "facts"),
                          (f"https://data.sec.gov/submissions/CIK{u['cik']:010d}.json", "sic")):
            if (kind == "facts" and target.exists()) or (kind == "sic" and u["symbol"] in sic):
                continue
            for attempt in range(3):
                try:
                    raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": agent}), timeout=120).read()
                    break
                except Exception as e:  # noqa: BLE001 - SEC throttles with 429; wait and retry
                    print(f"  {u['symbol']} {kind}: {e}; retry")
                    time.sleep(5 * (attempt + 1))
            else:
                continue
            if kind == "facts":
                target.write_bytes(gzip.compress(raw))
            else:
                sic[u["symbol"]] = str(json.loads(raw).get("sic") or "")
            time.sleep(0.12)  # SEC fair access: under 10 requests a second
        if n % 25 == 0:
            (CACHE / "sic.json").write_text(json.dumps(sic))
            print(f"facts: {n} of {len(universe)}")
    (CACHE / "sic.json").write_text(json.dumps(sic))
    print(f"facts: {len(list(FACTS.glob('*.json.gz')))} companies cached")


# ---------------------------------------------------------------------------------------------- point in time
_P: dict = {}
_ERP: dict[int, tuple[float, float]] = {}
_SIC: dict[str, str] = {}
_HIST: dict = {}
_IND: dict = {"multiples": {}, "pbv": {}}
_ORIG: dict = {}


def _vintage(year: int) -> None:
    """Point the industry tables at Damodaran's January file for *year* (the 2026 one when there is none)."""

    h = _HIST.get(str(year))
    if h is None:
        _IND.update(multiples=_ORIG["multiples"](), pbv=_ORIG["pbv"]())
        return
    nan = float("nan")
    _IND["multiples"] = {n: {"ev_ebit": r.get("ev_ebit") or nan, "ev_ebitda": r.get("ev_ebitda") or nan,
                             "pe": (h.get("pedata", {}).get(n) or {}).get("pe") or nan, "firms": 0}
                         for n, r in h.get("vebitda", {}).items()}
    _IND["pbv"] = {n: {"pbv": r["pbv"], "roe": r["roe"]} for n, r in h.get("pbvdata", {}).items()
                   if r.get("pbv") and r.get("roe") is not None}


def _install() -> None:
    """Worker set-up: every Yahoo and SEC call in the desk's code is replaced by a point-in-time read."""
    import pandas as pd

    stub = types.ModuleType("yfinance")
    stub.Ticker = lambda *a, **k: types.SimpleNamespace(info={})  # any Yahoo call left sees no data
    sys.modules["yfinance"] = stub
    os.environ.setdefault("FRED_API_KEY", "unused-in-backtest")  # risk_free() checks the key before the ERP branch

    from fundamentalist import market as M
    from fundamentalist import sizing as S
    from fundamentalist import valuation as V

    _P.update(pd.read_pickle(CACHE / "prices.pkl"))
    with open(HERE / "data" / "damodaran_implied_erp_history.csv", encoding="utf-8") as fh:
        _ERP.update({int(r["year_end"]): (float(r["erp_fcfe"]), float(r["tbond"])) for r in csv.DictReader(fh)
                     if r["erp_fcfe"] and r["tbond"]})
    _SIC.update(json.loads((CACHE / "sic.json").read_text()))
    _HIST.update(json.loads((HERE / "data" / "damodaran_industry_history.json").read_text()))
    _ORIG.update(multiples=M._industry_multiples, pbv=M._industry_pbv)
    M._industry_multiples = lambda: _IND["multiples"]
    M._industry_pbv = lambda: _IND["pbv"]
    V.company_facts = _facts
    V.industry = lambda t: (_SIC.get(t.upper(), ""), "")
    V.last_price = _price
    V.checked_shares = _shares
    V.beta = M.beta = _beta
    S.annual_volatility = _vol


@lru_cache(maxsize=2)
def _facts(ticker: str) -> dict:
    return json.loads(gzip.decompress((FACTS / f"{ticker.upper()}.json.gz").read_bytes()))


def _series(kind: str, ticker: str, as_of: str):
    s = _P[kind].get(ticker)
    if s is None:
        raise ValueError(f"no cached prices for {ticker}")
    return s.loc[:as_of].dropna()


def _price(ticker: str, as_of: str) -> tuple[float, str]:
    s = _series("close", ticker, as_of)
    if s.empty or (date.fromisoformat(as_of) - s.index[-1].date()).days > 10:
        raise ValueError(f"no close for {ticker} near {as_of}")
    return float(s.iloc[-1]), s.index[-1].date().isoformat()


def _shares(ticker: str, xbrl: dict | None, as_of: str) -> tuple[float | None, str]:
    """XBRL cover-page count (or, when it is missing or over 400 days old, the latest weighted-average diluted
    count from the income statement), times every split between its date and as_of."""
    from fundamentalist.valuation import _facts as facts_of

    if xbrl is None or xbrl["end"] < (date.fromisoformat(as_of) - timedelta(days=400)).isoformat():
        concept, rows = facts_of(_facts(ticker), ["WeightedAverageNumberOfDilutedSharesOutstanding"], as_of, unit="shares")
        recent = [r for r in rows if r["end"] >= (date.fromisoformat(as_of) - timedelta(days=200)).isoformat()]
        if not recent:
            return None, "no recent XBRL share count"
        r = max(recent, key=lambda r: (r["end"], -((date.fromisoformat(r["end"]) - date.fromisoformat(r["start"])).days
                                                     if r.get("start") else 0)))
        xbrl = {"val": r["val"], "end": r["end"], "concept": concept}
    sp = _P["splits"].get(ticker)
    factor = 1.0
    if sp is not None and len(sp):
        for d, ratio in sp.items():
            if xbrl["end"] < d.date().isoformat() <= as_of:
                factor *= float(ratio)
    return xbrl["val"] * factor, f"XBRL {xbrl['concept']} at {xbrl['end']}" + (f" x {factor:g} splits" if factor != 1 else "")


def _beta(ticker: str, as_of: str | None = None) -> dict:
    """Same rule as market.beta (Blume-adjusted, 5 years of monthly returns on the S&P 500), from cached prices."""
    from fundamentalist.parameters import value as param

    start = (date.fromisoformat(as_of) - timedelta(days=5 * 365 + 40)).isoformat()
    s = _series("adj", ticker, as_of).loc[start:].resample("ME").last()
    m = _series("adj", "^GSPC", as_of).loc[start:].resample("ME").last()
    both = s.to_frame("s").join(m.to_frame("m"), how="inner").dropna().pct_change().dropna()
    if len(both) < 36:
        raise ValueError(f"only {len(both)} months of prices for {ticker}")
    raw = float(both["s"].cov(both["m"]) / both["m"].var())
    lo, hi = param("beta_bounds")
    adjusted = 0.67 * raw + 0.33
    return {"raw": round(raw, 3), "adjusted": round(adjusted, 3), "used": round(min(max(adjusted, lo), hi), 3),
            "months": len(both), "bounded": not lo <= adjusted <= hi}


def _vol(ticker: str, as_of: str | None = None) -> float | None:
    s = _series("adj", ticker, as_of).loc[(date.fromisoformat(as_of) - timedelta(days=370)).isoformat():]
    s = s[s > 0]
    if len(s) < 60:
        return None
    r = (s / s.shift(1)).dropna().apply(math.log)
    return float(r.std() * math.sqrt(252))


def _value_one(args: tuple[str, list[str]]) -> list[dict]:
    """Every month end for one company (one worker, one company's facts in memory at a time)."""
    ticker, dates = args
    from fundamentalist import market as M
    from fundamentalist import parameters as P
    from fundamentalist.decision import decide, flags
    from fundamentalist.valuation import EQUITY, _instant, value

    rows = []
    for as_of in dates:
        erp, tbond = _ERP.get(int(as_of[:4]) - 1, (None, None))
        P.OVERRIDES.update({"equity_risk_premium": erp, "erp_risk_free": tbond, "terminal_growth_cap": tbond,
                            "erp_date": f"{int(as_of[:4]) - 1}-12-31"})
        M._RF_CACHE.clear()
        _vintage(int(as_of[:4]))
        row = {"date": as_of, "ticker": ticker}
        try:
            val = value(ticker, as_of)
            vol = _vol(ticker, as_of)
            fv = val.get("fair_value") or {}
            row.update(model=val.get("model") or "fcff", price=val.get("price"), note=(val.get("note") or "")[:120])
            if fv and val.get("price"):
                dec = decide(val, flags(val, {}, None), vol)
                mkt = val["price"] * (val.get("shares_outstanding") or 0)
                eq = _instant(_facts(ticker), EQUITY, as_of)
                mc = val.get("multiples_check") or {}
                row.update(base=fv["base"], bear=fv["bear"], bull=fv["bull"], vp=fv["base"] / val["price"],
                           rating=dec["rating"], uncertainty=dec.get("uncertainty"), vol=vol,
                           bm=(eq["val"] / mkt) if eq and mkt > 0 else None,
                           ey=(1 / val["market_ev_to_ebit"]) if (val.get("market_ev_to_ebit") or 0) > 0 else None,
                           peer_vp=(mc["value_per_share"] / val["price"]) if mc.get("value_per_share") else None)
        except Exception as e:  # noqa: BLE001 - a missing fact or price leaves the row unrated, with the reason
            row.update(error=f"{type(e).__name__}: {str(e)[:100]}")
        rows.append(row)
    return rows


def shard(tasks_file: Path) -> None:
    """One child process: value its share of the companies, write the rows next to the task file."""
    _install()
    rows, tasks, t0 = [], json.loads(tasks_file.read_text(encoding="utf-8")), time.time()
    for n, task in enumerate(tasks, 1):
        rows += _value_one(tuple(task))
        print(f"{n} of {len(tasks)} companies, {len(rows):,} rows, {time.time() - t0:.0f}s", flush=True)
    fields = sorted({k for r in rows for k in r}, key=lambda k: (k not in ("date", "ticker"), k))
    with open(tasks_file.with_suffix(".csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def month_ends(start: str, end: str) -> list[str]:
    import pandas as pd

    idx = pd.read_pickle(CACHE / "prices.pkl")["close"]["^GSPC"].dropna().index
    last = pd.Series(idx, index=idx).groupby([idx.year, idx.month]).max()
    return [d.date().isoformat() for d in last if start <= d.strftime("%Y-%m") <= end]


def run(start: str, end: str, workers: int, limit: int | None) -> Path:
    with open(CACHE / "universe.csv", encoding="utf-8") as fh:
        universe = list(csv.DictReader(fh))
    dates = month_ends(start, end)
    have = {p.name.removesuffix(".json.gz") for p in FACTS.glob("*.json.gz")}
    tasks = [(u["symbol"], [d for d in dates if (u["added"] or "1900") <= d]) for u in universe if u["symbol"] in have]
    tasks = [t for t in tasks if t[1]][:limit]
    print(f"{len(tasks)} companies x up to {len(dates)} month ends ({dates[0]} to {dates[-1]}), {workers} shards")
    # Child processes, one shard each, results through files: multiprocessing pipes are refused in some sandboxes.
    t0, rows, procs = time.time(), [], []
    work = OUT / "shards"
    work.mkdir(parents=True, exist_ok=True)
    for i in range(workers):
        part = tasks[i::workers]
        if not part:
            continue
        (work / f"tasks-{i}.json").write_text(json.dumps(part), encoding="utf-8")
        log = open(work / f"shard-{i}.log", "w", encoding="utf-8")
        procs.append((i, log, subprocess.Popen([sys.executable, __file__, "shard", "--file", str(work / f"tasks-{i}.json")],
                                               stdout=log, stderr=subprocess.STDOUT, env=dict(os.environ, PYTHONUTF8="1"))))
    for i, log, proc in procs:
        proc.wait()
        log.close()
        out = work / f"tasks-{i}.csv"
        if proc.returncode or not out.exists():
            raise RuntimeError(f"shard {i} failed; see {work / f'shard-{i}.log'}")
        with open(out, encoding="utf-8") as fh:
            rows += list(csv.DictReader(fh))
        print(f"  shard {i} done: {len(rows):,} valuations so far, {time.time() - t0:.0f}s")
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"valuations-{start}-{end}-{time.strftime('%Y%m%d-%H%M')}.csv"
    fields = sorted({k for r in rows for k in r}, key=lambda k: (k not in ("date", "ticker"), k))
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows):,} valuations in {time.time() - t0:.0f}s -> {path.relative_to(HERE)}")
    return path


# --------------------------------------------------------------------------------------------------- report
def _nw_t(x, lags: int) -> float:
    """t statistic of the mean with Newey-West errors (overlapping horizons)."""
    import numpy as np

    x = np.asarray(x, dtype=float)
    n = len(x)
    e = x - x.mean()
    s = e @ e / n + 2 * sum((1 - k / (lags + 1)) * (e[k:] @ e[:-k]) / n for k in range(1, lags + 1))
    return float(x.mean() / math.sqrt(s / n)) if s > 0 else float("nan")


def report(path: Path | None) -> Path:
    import pandas as pd

    path = path or max(OUT.glob("valuations-*.csv"), key=lambda p: p.stat().st_mtime)
    df = pd.read_csv(path)
    adj = pd.read_pickle(CACHE / "prices.pkl")["adj"]
    horizons = {"1m": 21, "3m": 63, "12m": 252}
    fwd = {h: [] for h in horizons}
    for t, d in zip(df["ticker"], df["date"]):
        s = adj[t].dropna() if t in adj else None
        i = s.index.searchsorted(pd.Timestamp(d), side="right") - 1 if s is not None else -1
        for h, n in horizons.items():
            fwd[h].append(s.iloc[i + n] / s.iloc[i] - 1 if s is not None and 0 <= i and i + n < len(s) else None)
    for h in horizons:
        df[f"r{h}"] = pd.to_numeric(pd.Series(fwd[h], index=df.index), errors="coerce")
        df[f"x{h}"] = df[f"r{h}"] - df.groupby("date")[f"r{h}"].transform("mean")  # excess over the universe average
    df["rating_num"] = df["rating"].map(RATING_NUM)
    rated = df.dropna(subset=["vp"])
    lines = [f"# Backtest of the code core, {path.name}", "",
             f"{df['date'].nunique()} month ends, {df['ticker'].nunique()} companies, {len(df):,} company-months; "
             f"{len(rated):,} rated ({len(rated) / len(df):.0%}). No model calls.", "", f"Leaks left: {LEAKS}.", ""]
    lines += ["## Rank IC: signal vs forward return (Spearman, per month, then averaged)", "",
              "| signal | 1m IC | t | 3m IC | t (NW) | 12m IC | t (NW) | months |", "|---|---|---|---|---|---|---|---|"]
    signals = {"fair value / price (desk)": "vp", "rating (desk)": "rating_num", "industry multiples value / price": "peer_vp",
               "book-to-market": "bm", "EBIT / EV": "ey"}
    ics: dict = {}
    for label, col in signals.items():
        cells, months = [], 0
        for h, lag in (("1m", 0), ("3m", 2), ("12m", 11)):
            per = rated.dropna(subset=[col, f"r{h}"]).groupby("date").apply(
                lambda g: g[col].rank().corr(g[f"r{h}"].rank()) if len(g) >= 20 else float("nan"), include_groups=False).dropna()
            ics[(col, h)] = per
            cells += [f"{per.mean():+.3f}" if len(per) else "n/a", f"{_nw_t(per, lag):.1f}" if len(per) > 3 else "n/a"]
            months = max(months, len(per))
        lines.append(f"| {label} | " + " | ".join(cells) + f" | {months} |")
    lines += ["", "## Quintiles of fair value / price, 1-month returns (equal weight, rebalanced monthly)", "",
              "| quintile | mean 1m excess | annualised |", "|---|---|---|"]
    q = rated.dropna(subset=["x1m"]).copy()
    q["q"] = q.groupby("date")["vp"].transform(lambda s: pd.qcut(s.rank(method="first"), 5, labels=False) + 1)
    by_q = q.groupby(["date", "q"])["x1m"].mean().unstack()
    for k in range(1, 6):
        lines.append(f"| Q{k}{' (cheapest)' if k == 5 else ' (dearest)' if k == 1 else ''} | {by_q[k].mean():+.2%} | "
                     f"{(1 + by_q[k].mean()) ** 12 - 1:+.1%} |")
    spread = (by_q[5] - by_q[1]).dropna()
    lines += ["", f"Q5 - Q1: {spread.mean():+.2%} a month ({(1 + spread.mean()) ** 12 - 1:+.1%} a year), "
                  f"t {_nw_t(spread, 0):.1f}, {len(spread)} months.", ""]
    lines += ["## Ratings: 12-month excess return over the universe average", "",
              "| rating | company-months | mean excess | median | beat the average |", "|---|---|---|---|---|"]
    for r in ("Buy", "Overweight", "Hold", "Underweight", "Sell"):
        g = rated[(rated["rating"] == r)].dropna(subset=["x12m"])
        if len(g):
            lines.append(f"| {r} | {len(g):,} | {g['x12m'].mean():+.1%} | {g['x12m'].median():+.1%} | {(g['x12m'] > 0).mean():.0%} |")
    lines += ["", "## By valuation route and period (fair value / price, 12-month rank IC)", "",
              "| slice | IC | t (NW) | months |", "|---|---|---|---|"]
    slices = {f"route {m}": rated[rated["model"] == m] for m in sorted(rated["model"].dropna().unique())}
    slices.update({"2016-2020": rated[rated["date"] < "2021"], "2021-2025": rated[rated["date"] >= "2021"]})
    for label, g in slices.items():
        per = g.dropna(subset=["vp", "r12m"]).groupby("date").apply(
            lambda x: x["vp"].rank().corr(x["r12m"].rank()) if len(x) >= 15 else float("nan"), include_groups=False).dropna()
        if len(per):
            lines.append(f"| {label} | {per.mean():+.3f} | {_nw_t(per, 11):.1f} | {len(per)} |")
    corr = rated.dropna(subset=["vp", "ey"]).groupby("date").apply(
        lambda g: g["vp"].rank().corr(g["ey"].rank()), include_groups=False).mean()
    lines += ["", f"Average rank correlation of the desk's fair value / price with EBIT / EV: {corr:+.2f} "
                  "(how much of the signal is a plain value factor).", ""]
    errors = df["error"].dropna().str.split(":").str[0].value_counts().head(6) if "error" in df else []
    if len(errors):
        lines += ["Unrated rows by reason: " + ", ".join(f"{k} {v:,}" for k, v in errors.items()), ""]
    out = path.with_suffix(".md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["fetch", "run", "report", "shard"])
    ap.add_argument("--start", default="2016-01")
    ap.add_argument("--end", default="2025-09")
    ap.add_argument("--workers", type=int, default=max((os.cpu_count() or 4) - 4, 1))
    ap.add_argument("--limit", type=int, default=None, help="first N companies only (smoke test)")
    ap.add_argument("--file", default=None)
    a = ap.parse_args()
    if a.command == "fetch":
        fetch()
    elif a.command == "run":
        report(run(a.start, a.end, a.workers, a.limit))
    elif a.command == "shard":
        shard(Path(a.file))
    else:
        report(Path(a.file) if a.file else None)
