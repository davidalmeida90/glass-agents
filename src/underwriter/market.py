"""Market inputs for the cost of capital: risk-free rate, beta, synthetic rating and credit spread."""

from __future__ import annotations

import csv
import json
import os
import urllib.request
from datetime import date, timedelta
from functools import lru_cache
from pathlib import Path
from typing import Any

from underwriter.parameters import value as param

# Interest coverage (EBIT / interest expense) floor -> (rating, default spread), large non-financial firms
# (market cap of $5bn or more). Damodaran, ratings.xls, January 2026 (read 2026-09-30).
RATING_TABLE: list[tuple[float, str, float]] = [
    (8.5, "AAA", 0.0040), (6.5, "AA", 0.0055), (5.5, "A+", 0.0070), (4.25, "A", 0.0078), (3.0, "A-", 0.0089),
    (2.5, "BBB", 0.0111), (2.25, "BB+", 0.0138), (2.0, "BB", 0.0184), (1.75, "B+", 0.0275), (1.5, "B", 0.0321),
    (1.25, "B-", 0.0509), (0.8, "CCC", 0.0885), (0.65, "CC", 0.1261), (0.2, "C", 0.1600), (float("-inf"), "D", 0.1900),
]


_RF_CACHE: dict[str, tuple[float, str]] = {}


def risk_free(mode: str | None = None) -> tuple[float, str]:
    """10-year Treasury yield from FRED (DGS10), as a decimal, with its date.

    mode "erp_date": the yield on (or just before) the ERP's date, so the pair is consistent. "spot": the latest.
    """
    mode = mode or param("risk_free")
    if mode in _RF_CACHE:
        return _RF_CACHE[mode]
    key = os.environ.get("FRED_API_KEY", "")
    if not key:
        raise RuntimeError("FRED_API_KEY is not set")
    if mode == "erp_date":  # the exact rate the ERP was computed on
        _RF_CACHE[mode] = (param("erp_risk_free"), f"{param('erp_date')} (rate in Damodaran's ERP computation)")
        return _RF_CACHE[mode]
    end = date.today().isoformat()
    url = ("https://api.stlouisfed.org/fred/series/observations?series_id=DGS10&file_type=json&sort_order=desc"
           f"&observation_end={end}&limit=10&api_key={key}")
    rows = json.loads(urllib.request.urlopen(url, timeout=30).read())["observations"]
    row = next(r for r in rows if r["value"] not in (".", ""))
    _RF_CACHE[mode] = (float(row["value"]) / 100, row["date"])
    return _RF_CACHE[mode]


def beta(ticker: str, as_of: str | None = None) -> dict[str, Any]:
    """Blume-adjusted OLS beta of 5 years of monthly returns on the S&P 500, bounded."""
    import yfinance as yf

    end = date.fromisoformat(as_of) if as_of else date.today()
    start = (end - timedelta(days=5 * 365 + 40)).isoformat()
    closes = {}
    for sym in (ticker, "^GSPC"):
        hist = yf.Ticker(sym).history(start=start, end=(end + timedelta(days=1)).isoformat(), interval="1mo",
                                      auto_adjust=True)
        closes[sym] = {d.strftime("%Y-%m"): float(c) for d, c in zip(hist.index, hist["Close"]) if c and c > 0}
    months = sorted(set(closes[ticker]) & set(closes["^GSPC"]))
    if len(months) < 36:
        raise ValueError(f"only {len(months)} months of prices for {ticker}")
    rs = [closes[ticker][b] / closes[ticker][a] - 1 for a, b in zip(months, months[1:])]
    rm = [closes["^GSPC"][b] / closes["^GSPC"][a] - 1 for a, b in zip(months, months[1:])]
    ms, mm = sum(rs) / len(rs), sum(rm) / len(rm)
    cov = sum((a - ms) * (b - mm) for a, b in zip(rs, rm)) / (len(rs) - 1)
    var = sum((b - mm) ** 2 for b in rm) / (len(rm) - 1)
    raw = cov / var
    lo, hi = param("beta_bounds")
    adjusted = 0.67 * raw + 0.33
    return {"raw": round(raw, 3), "adjusted": round(adjusted, 3), "used": round(min(max(adjusted, lo), hi), 3),
            "months": len(rs), "bounded": not lo <= adjusted <= hi}


DATA = Path(__file__).resolve().parents[2] / "data"


@lru_cache(maxsize=1)
def _industry_betas() -> dict[str, dict[str, float]]:
    with open(DATA / "damodaran_us_industry_betas_2026-01.csv", encoding="utf-8") as fh:
        return {r["Industry Name"].strip(): {"levered": float(r["Beta"]),
                                             "unlevered_cash_corrected": float(r["Unlevered beta corrected for cash"]),
                                             "firms": int(float(r["Number of firms"]))} for r in csv.DictReader(fh)}


@lru_cache(maxsize=1)
def _ticker_industries() -> dict[str, str]:
    with open(DATA / "damodaran_ticker_industry_2026-01.csv", encoding="utf-8") as fh:
        return {r["ticker"].upper(): r["Industry Group"].strip() for r in csv.DictReader(fh)}


def bottom_up_beta(ticker: str, debt_to_equity: float, bank: bool = False) -> dict[str, Any] | None:
    """Industry unlevered beta (cash-corrected), relevered at the firm's market D/E: bu x (1 + (1 - t) x D/E).

    Banks take their industry's levered beta: debt is a bank's raw material, not financing (Damodaran).
    """
    industry = _ticker_industries().get(ticker.upper())
    row = _industry_betas().get(industry or "")
    if row is None:
        return None
    if bank:
        return {"industry": industry, "firms": row["firms"], "used": round(row["levered"], 3),
                "method": "industry levered beta (bank)"}
    levered = row["unlevered_cash_corrected"] * (1 + (1 - param("marginal_tax")) * debt_to_equity)
    lo, hi = param("beta_bounds")
    return {"industry": industry, "firms": row["firms"], "unlevered": round(row["unlevered_cash_corrected"], 3),
            "debt_to_equity": round(debt_to_equity, 3), "used": round(min(max(levered, lo), hi), 3),
            "method": "bottom-up: industry unlevered beta (cash-corrected) relevered at market D/E"}


def synthetic_rating(ebit: float, interest: float) -> dict[str, Any]:
    """Rating and default spread from interest coverage; no interest expense reads as the top band."""
    coverage = ebit / interest if interest and interest > 0 else float("inf")
    for floor, rating, spread in RATING_TABLE:
        if coverage >= floor:
            return {"coverage": round(coverage, 2) if coverage != float("inf") else None, "rating": rating,
                    "spread": spread}
    return {"coverage": coverage, "rating": "D", "spread": RATING_TABLE[-1][2]}
