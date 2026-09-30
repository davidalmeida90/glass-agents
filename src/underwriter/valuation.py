"""Valuation in code: point-in-time figures from SEC XBRL, then a fair value range and the growth the price implies.

The XBRL functions are adapted from David's own Glassbench (desk/backend/deskapp/edgar.py): facts filed
before the as-of date, trailing twelve months built from the fiscal year and year-to-date filings, and the
share count from the cover page. The valuation is new here and deliberately plain, so every number can
be recomputed by hand. It values owner earnings (operating cash flow minus depreciation, the usual proxy
for maintenance capital spending, so a capex build-out does not read as lost value) over ten years, growth
fading linearly to 3%, discounted at 9%. Bear, base and bull use the company's own revenue growth, capped
at 25%, minus 5 points, as is, and plus 5 points. Next to it sits the reverse DCF: the starting growth the
current price implies under the same assumptions (Mauboussin and Rappaport's expectations investing).
A plain five-year DCF on trailing free cash flow was tried first and rejected: it rated every large cap
tested a Sell, so it could not tell companies apart.
"""

from __future__ import annotations

import json
from datetime import date, timedelta
from typing import Any

from underwriter.edgar import sec_get

REVENUE = ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet",
           "RevenueFromContractWithCustomerIncludingAssessedTax"]
NET_INCOME = ["NetIncomeLoss", "ProfitLoss"]
OCF = ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"]
CAPEX = ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"]
DA = ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet", "DepreciationAndAmortization",
      "Depreciation"]
CASH = ["CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"]
SECURITIES = ["MarketableSecuritiesCurrent", "AvailableForSaleSecuritiesDebtSecuritiesCurrent", "ShortTermInvestments"]
DEBT_PARTS = [["LongTermDebtNoncurrent"], ["LongTermDebtCurrent"], ["CommercialPaper"], ["ShortTermBorrowings"]]
DEBT_TOTAL = ["LongTermDebt", "DebtInstrumentCarryingAmount"]

SCENARIOS = {"bear": -0.05, "base": 0.0, "bull": 0.05}  # points added to the company's own growth
GROWTH_CAP = 0.25
DISCOUNT = 0.09
TERMINAL_GROWTH = 0.03
YEARS = 10


# ------------------------------------------------------------------ SEC XBRL (adapted from Glassbench)
def company_facts(ticker: str) -> dict[str, Any]:
    tickers = json.loads(sec_get("https://www.sec.gov/files/company_tickers.json", "company_tickers.json"))
    co = next((v for v in tickers.values() if v["ticker"].upper() == ticker.upper()), None)
    if co is None:
        raise ValueError(f"unknown ticker {ticker}")
    cik = co["cik_str"]
    name = f"companyfacts-{cik}-{date.today().isoformat()}.json"  # refreshed once a day
    return json.loads(sec_get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json", name))


def _facts(data: dict, concepts: list[str], as_of: str, taxonomy: str = "us-gaap",
           unit: str = "USD") -> tuple[str | None, list[dict]]:
    """Facts filed strictly before as_of, from the concept with the most recent period."""
    best: tuple[str, list[dict]] | None = None
    best_end = ""
    for concept in concepts:
        node = data.get("facts", {}).get(taxonomy, {}).get(concept)
        if not node:
            continue
        rows = [r for r in node.get("units", {}).get(unit, []) if r.get("filed", "9999") < as_of]
        if not rows:
            continue
        latest: dict[tuple, dict] = {}
        for r in rows:
            key = (r.get("start"), r["end"])
            if key not in latest or r["filed"] > latest[key]["filed"]:
                latest[key] = r
        end = max(r["end"] for r in latest.values())
        if end > best_end:
            best, best_end = (concept, list(latest.values())), end
    return best if best else (None, [])


def _days(r: dict) -> int:
    return (date.fromisoformat(r["end"]) - date.fromisoformat(r["start"])).days


def _instant(data: dict, concepts: list[str], as_of: str, taxonomy: str = "us-gaap", unit: str = "USD") -> dict | None:
    concept, rows = _facts(data, concepts, as_of, taxonomy, unit)
    rows = [r for r in rows if not r.get("start")]
    if not rows:
        return None
    return {**max(rows, key=lambda r: (r["end"], r["filed"])), "concept": concept}


def _ttm(data: dict, concepts: list[str], as_of: str) -> dict | None:
    """Trailing twelve months known on as_of: the fiscal year, or last FY + year-to-date - prior year-to-date."""
    concept, rows = _facts(data, concepts, as_of)
    flows = [r for r in rows if r.get("start")]
    if not flows:
        return None
    end = max(r["end"] for r in flows)
    at_end = [r for r in flows if r["end"] == end]
    annual = [r for r in at_end if 350 <= _days(r) <= 380]
    if annual:
        r = max(annual, key=lambda x: x["filed"])
        return {"value": r["val"], "end": end, "method": "fiscal year", "filed": r["filed"], "concept": concept}
    ytd = max(at_end, key=_days)
    length = _days(ytd)
    if length > 350:
        return None
    end_d = date.fromisoformat(end)
    prior = [r for r in flows if abs((date.fromisoformat(r["end"]) - (end_d - timedelta(days=364))).days) <= 10
             and abs(_days(r) - length) <= 10]
    start_d = date.fromisoformat(ytd["start"])
    fiscal = [r for r in flows if 350 <= _days(r) <= 380
              and abs((date.fromisoformat(r["end"]) - (start_d - timedelta(days=1))).days) <= 10]
    if not prior or not fiscal:
        return None
    p, f = max(prior, key=lambda x: x["filed"]), max(fiscal, key=lambda x: x["filed"])
    return {"value": f["val"] + ytd["val"] - p["val"], "end": end,
            "method": f"FY to {f['end']} + {round(length / 30.4)}-month YTD - prior YTD", "filed": ytd["filed"],
            "concept": concept}


def _shares(data: dict, as_of: str) -> dict | None:
    return (_instant(data, ["EntityCommonStockSharesOutstanding"], as_of, taxonomy="dei", unit="shares")
            or _instant(data, ["CommonStockSharesOutstanding"], as_of, unit="shares"))


def last_price(ticker: str, as_of: str) -> tuple[float, str]:
    """Close on or before as_of, from Yahoo."""
    import yfinance as yf

    start = (date.fromisoformat(as_of) - timedelta(days=10)).isoformat()
    end = (date.fromisoformat(as_of) + timedelta(days=1)).isoformat()
    hist = yf.Ticker(ticker).history(start=start, end=end, auto_adjust=False)
    if hist.empty:
        raise ValueError(f"no Yahoo price for {ticker} near {as_of}")
    return float(hist["Close"].iloc[-1]), hist.index[-1].date().isoformat()


def fundamentals(ticker: str, as_of: str) -> dict[str, Any]:
    """The figures the DCF and the flags need, each with the filing it came from."""
    data = company_facts(ticker)
    year_ago = (date.fromisoformat(as_of) - timedelta(days=365)).isoformat()
    cash = _instant(data, CASH, as_of)
    securities = _instant(data, SECURITIES, as_of)
    parts = [p for p in (_instant(data, c, as_of) for c in DEBT_PARTS) if p and cash and p["end"] == cash["end"]]
    total_debt = _instant(data, DEBT_TOTAL, as_of)
    debt = sum(p["val"] for p in parts) if parts else (total_debt["val"] if total_debt else None)
    liquid = (cash["val"] if cash else 0) + (
        securities["val"] if securities and cash and securities["end"] == cash["end"] else 0)
    return {
        "revenue": _ttm(data, REVENUE, as_of), "revenue_year_ago": _ttm(data, REVENUE, year_ago),
        "net_income": _ttm(data, NET_INCOME, as_of), "operating_cash_flow": _ttm(data, OCF, as_of),
        "capex": _ttm(data, CAPEX, as_of), "d_and_a": _ttm(data, DA, as_of), "shares": _shares(data, as_of),
        "debt": debt,
        "cash_and_securities": liquid if cash else None,
    }


# ------------------------------------------------------------------ DCF
def present_value(cash_flow: float, growth: float, discount: float = DISCOUNT, terminal: float = TERMINAL_GROWTH,
                  years: int = YEARS) -> float:
    """Cash flow for *years*, growth fading linearly from *growth* to the terminal rate, plus a Gordon terminal value."""
    pv, flow = 0.0, cash_flow
    for t in range(1, years + 1):
        g = growth + (terminal - growth) * (t - 1) / (years - 1)
        flow *= 1 + g
        pv += flow / (1 + discount) ** t
    return pv + flow * (1 + terminal) / (discount - terminal) / (1 + discount) ** years


def dcf_per_share(cash_flow: float, growth: float, discount: float, net_debt: float, shares: float,
                  terminal: float = TERMINAL_GROWTH, years: int = YEARS) -> float:
    return (present_value(cash_flow, growth, discount, terminal, years) - net_debt) / shares


def implied_growth(cash_flow: float, enterprise_value: float, discount: float = DISCOUNT) -> float:
    """Starting growth at which present_value equals the enterprise value (bisection)."""
    lo, hi = -0.5, 1.5
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if present_value(cash_flow, mid, discount) < enterprise_value else (lo, mid)
    return (lo + hi) / 2


def value(ticker: str, as_of: str | None = None) -> dict[str, Any]:
    """Fair value range per share, the inputs behind it, and why it is missing when it is."""
    as_of = as_of or date.today().isoformat()
    f = fundamentals(ticker, as_of)
    price, price_date = last_price(ticker, as_of)
    out: dict[str, Any] = {"ticker": ticker.upper(), "as_of": as_of, "price": price, "price_date": price_date,
                           "inputs": f, "fair_value": None, "note": None}
    ocf, capex, da, shares = f["operating_cash_flow"], f["capex"], f["d_and_a"], f["shares"]
    rev, rev_ago = f["revenue"], f["revenue_year_ago"]
    if not (ocf and shares and (da or capex)):
        out["note"] = "operating cash flow or depreciation not available from XBRL (typical for banks)"
        return out
    if da and da["end"] == ocf["end"]:
        owner, basis = ocf["value"] - da["value"], "operating cash flow - depreciation and amortization"
    elif capex and capex["end"] == ocf["end"]:
        owner, basis = ocf["value"] - capex["value"], "operating cash flow - capex (no depreciation figure)"
    else:
        out["note"] = "cash flow figures from different periods"
        return out
    if owner <= 0:
        out["note"] = f"owner earnings are negative ({owner:,.0f}): a cash flow valuation does not apply"
        return out
    growth = (rev["value"] / rev_ago["value"] - 1) if rev and rev_ago and rev_ago["value"] else 0.0
    base_growth = min(max(growth, 0.0), GROWTH_CAP)
    net_debt = (f["debt"] or 0) - (f["cash_and_securities"] or 0)
    fair = {name: round(dcf_per_share(owner, max(base_growth + shift, 0.0), DISCOUNT, net_debt, shares["val"]), 2)
            for name, shift in SCENARIOS.items()}
    out.update(fair_value=fair, owner_earnings=owner, owner_earnings_basis=basis, revenue_growth=round(growth, 4),
               growth_used=round(base_growth, 4), net_debt=net_debt, shares_outstanding=shares["val"],
               implied_growth=round(implied_growth(owner, price * shares["val"] + net_debt), 4),
               fcf=(ocf["value"] - capex["value"]) if capex and capex["end"] == ocf["end"] else None,
               cash_conversion=round(ocf["value"] / f["net_income"]["value"], 3)
               if f["net_income"] and f["net_income"]["value"] > 0 else None)
    return out
