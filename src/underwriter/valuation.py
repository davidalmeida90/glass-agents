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

EQUITY = ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"]
PREFERRED = ["PreferredStockValue", "PreferredStockValueOutstanding"]
NI_COMMON = ["NetIncomeLossAvailableToCommonStockholdersBasic", "NetIncomeLoss"]
BANK_SIC = {"6021", "6022", "6029", "6035", "6036", "6211"}  # commercial and savings banks, broker-dealers
BANK_SCENARIOS = {"bear": (-0.02, 0.11), "base": (0.0, 0.10), "bull": (0.02, 0.09)}  # ROE points, cost of equity

SCENARIOS = {"bear": -0.05, "base": 0.0, "bull": 0.05}  # points added to the company's own growth
GROWTH_CAP = 0.25
DISCOUNT = 0.09
TERMINAL_GROWTH = 0.03
YEARS = 10


# ------------------------------------------------------------------ SEC XBRL (adapted from Glassbench)
def _cik(ticker: str) -> int:
    tickers = json.loads(sec_get("https://www.sec.gov/files/company_tickers.json", "company_tickers.json"))
    co = next((v for v in tickers.values() if v["ticker"].upper() == ticker.upper()), None)
    if co is None:
        raise ValueError(f"unknown ticker {ticker}")
    return co["cik_str"]


def industry(ticker: str) -> tuple[str, str]:
    """SEC industry code and description from the submissions API."""
    cik = _cik(ticker)
    sub = json.loads(sec_get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json",
                             f"submissions-{cik}-{date.today().isoformat()}.json"))
    return str(sub.get("sic", "")), sub.get("sicDescription", "")


def company_facts(ticker: str) -> dict[str, Any]:
    cik = _cik(ticker)
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


def _ttm(data: dict, concepts: list[str], as_of: str, near_end: str | None = None) -> dict | None:
    """Trailing twelve months known on as_of: the fiscal year, or last FY + year-to-date - prior year-to-date.

    With *near_end*, the twelve months ending within 10 days of that date instead of the latest ones.
    """
    concept, rows = _facts(data, concepts, as_of)
    flows = [r for r in rows if r.get("start")]
    if near_end:
        target = date.fromisoformat(near_end)
        flows_near = [r for r in flows if abs((date.fromisoformat(r["end"]) - target).days) <= 10]
        if not flows_near:
            return None
        end = max(r["end"] for r in flows_near)
    elif not flows:
        return None
    else:
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
    """Cover-page count, else balance sheet count, else diluted weighted average of the latest period.

    Companies with several share classes (Meta: A and B) report the cover count per class only, which
    the XBRL API leaves out, so the diluted weighted average is the last resort.
    """
    found = (_instant(data, ["EntityCommonStockSharesOutstanding"], as_of, taxonomy="dei", unit="shares")
             or _instant(data, ["CommonStockSharesOutstanding"], as_of, unit="shares"))
    if found:
        return found
    concept, rows = _facts(data, ["WeightedAverageNumberOfDilutedSharesOutstanding"], as_of, unit="shares")
    if not rows:
        return None
    return {**max(rows, key=lambda r: (r["end"], r["filed"])), "concept": concept}


def yahoo_shares(ticker: str) -> float | None:
    """Share count implied by Yahoo's market cap and price (all classes, as Yahoo counts them)."""
    import yfinance as yf

    info = yf.Ticker(ticker).info
    price = info.get("currentPrice") or info.get("regularMarketPrice")
    return info["marketCap"] / price if info.get("marketCap") and price else None


def checked_shares(ticker: str, xbrl: dict | None, as_of: str) -> tuple[float | None, str]:
    """XBRL share count unless it is over a year old or more than 10% away from Yahoo's implied count.

    Visa's only undivided cover-page count is from 2010 (later ones are per class), 4x too few shares.
    """
    stale = xbrl is None or xbrl["end"] < (date.fromisoformat(as_of) - timedelta(days=400)).isoformat()
    try:
        yahoo = yahoo_shares(ticker)
    except Exception:  # noqa: BLE001 - Yahoo is only the cross-check
        yahoo = None
    if not stale and (yahoo is None or abs(xbrl["val"] / yahoo - 1) <= 0.10):
        return xbrl["val"], f"XBRL {xbrl['concept']} at {xbrl['end']}"
    if yahoo:
        why = "XBRL count missing or over a year old" if stale else f"XBRL count {xbrl['val'] / 1e9:.3f}B differs by over 10%"
        return yahoo, f"Yahoo market cap / price ({why})"
    return (None, "no share count") if stale else (xbrl["val"], f"XBRL {xbrl['concept']} at {xbrl['end']} (no Yahoo check)")


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
    cash = _instant(data, CASH, as_of)
    securities = _instant(data, SECURITIES, as_of)
    parts = [p for p in (_instant(data, c, as_of) for c in DEBT_PARTS) if p and cash and p["end"] == cash["end"]]
    total_debt = _instant(data, DEBT_TOTAL, as_of)
    debt = sum(p["val"] for p in parts) if parts else (total_debt["val"] if total_debt else None)
    liquid = (cash["val"] if cash else 0) + (
        securities["val"] if securities and cash and securities["end"] == cash["end"] else 0)
    revenue = _ttm(data, REVENUE, as_of)
    revenue_year_ago = None
    if revenue:
        prior_end = (date.fromisoformat(revenue["end"]) - timedelta(days=364)).isoformat()
        revenue_year_ago = _ttm(data, [revenue["concept"]], as_of, near_end=prior_end)
    return {
        "revenue": revenue, "revenue_year_ago": revenue_year_ago,
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


def bank_value(ticker: str, as_of: str, price: float, price_date: str, sic: str) -> dict[str, Any]:
    """Justified price-to-book for banks: P/B = (ROE - g) / (r - g) on common equity."""
    data = company_facts(ticker)
    equity, preferred = _instant(data, EQUITY, as_of), _instant(data, PREFERRED, as_of)
    ni = _ttm(data, NI_COMMON, as_of)
    count, count_source = checked_shares(ticker, _shares(data, as_of), as_of)
    shares = {"val": count, "source": count_source} if count else None
    out: dict[str, Any] = {"ticker": ticker.upper(), "as_of": as_of, "price": price, "price_date": price_date,
                           "sic": sic, "fair_value": None, "note": None,
                           "method": "justified price-to-book: P/B = (ROE - 3%) / (cost of equity - 3%), ROE +/-2 points "
                                     "and cost of equity 11/10/9% for bear/base/bull"}
    if not (equity and ni and shares):
        out["note"] = "equity, net income or share count not available from XBRL"
        return out
    common = equity["val"] - (preferred["val"] if preferred and preferred["end"] == equity["end"] else 0)
    roe = ni["value"] / common
    bvps = common / shares["val"]
    fair = {}
    for name, (d_roe, r) in BANK_SCENARIOS.items():
        pb = max((roe + d_roe - TERMINAL_GROWTH) / (r - TERMINAL_GROWTH), 0.0)
        fair[name] = round(bvps * pb, 2)
    out["valuation_period"] = (f"net income to common, twelve months to {ni['end']}; equity at {equity['end']}; "
                               f"the readers' evidence comes from the latest 10-K only")
    out.update(fair_value=fair, roe=round(roe, 4), book_value_per_share=round(bvps, 2),
               implied_roe=round(price / bvps * (0.10 - TERMINAL_GROWTH) + TERMINAL_GROWTH, 4),
               shares_outstanding=shares["val"], cash_conversion=None,
               inputs={"common_equity": common, "net_income_to_common": ni, "equity": equity, "preferred": preferred})
    return out


def value(ticker: str, as_of: str | None = None) -> dict[str, Any]:
    """Fair value range per share, the inputs behind it, and why it is missing when it is."""
    as_of = as_of or date.today().isoformat()
    price, price_date = last_price(ticker, as_of)
    sic, _ = industry(ticker)
    if sic in BANK_SIC:
        return bank_value(ticker, as_of, price, price_date, sic)
    f = fundamentals(ticker, as_of)
    out: dict[str, Any] = {"ticker": ticker.upper(), "as_of": as_of, "price": price, "price_date": price_date,
                           "sic": sic, "inputs": f, "fair_value": None, "note": None,
                           "method": "owner earnings (operating cash flow - D&A), 10 years fading to 3%, 9% discount; "
                                     "bear/base/bull = own revenue growth capped at 25% -5/0/+5 points; "
                                     "implied_growth = starting growth the price implies"}
    ocf, capex, da = f["operating_cash_flow"], f["capex"], f["d_and_a"]
    count, count_source = checked_shares(ticker, f["shares"], as_of)
    shares = {"val": count, "source": count_source} if count else None
    rev, rev_ago = f["revenue"], f["revenue_year_ago"]
    missing = [n for n, v in (("operating cash flow", ocf), ("share count", shares),
                               ("depreciation or capex", da or capex)) if not v]
    if missing:
        out["note"] = f"not available from XBRL: {', '.join(missing)}"
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
    out["valuation_period"] = (f"trailing twelve months to {ocf['end']} (revenue growth: twelve months to "
                               f"{rev['end'] if rev else '?'} vs to {rev_ago['end'] if rev_ago else '?'}), from 10-K and "
                               f"10-Q XBRL; the readers' evidence comes from the latest 10-K only")
    out.update(fair_value=fair, owner_earnings=owner, owner_earnings_basis=basis, revenue_growth=round(growth, 4),
               growth_used=round(base_growth, 4), net_debt=net_debt, shares_outstanding=shares["val"],
               shares_source=shares["source"],
               implied_growth=round(implied_growth(owner, price * shares["val"] + net_debt), 4),
               fcf=(ocf["value"] - capex["value"]) if capex and capex["end"] == ocf["end"] else None,
               cash_conversion=round(ocf["value"] / f["net_income"]["value"], 3)
               if f["net_income"] and f["net_income"]["value"] > 0 else None)
    return out
