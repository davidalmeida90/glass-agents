"""Valuation in code: point-in-time figures from SEC XBRL, a company WACC, and an FCFF DCF.

The XBRL functions are adapted from David's own Glassbench (desk/backend/deskapp/edgar.py): facts filed
before the as-of date, trailing twelve months built from the fiscal year and year-to-date filings, and the
share count checked against Yahoo. The valuation follows Damodaran's FCFF structure (dcf.py): revenue growth
paid for by reinvestment through sales-to-capital, stock-based compensation as an expense, leases as debt, a
WACC from CAPM (FRED risk-free rate, regression beta, implied ERP) and a synthetic-rating cost of debt, and a
terminal value that keeps a stated share of today's excess return. Every parameter lives in parameters.py.

History, kept so the choices can be questioned: a plain five-year DCF on trailing free cash flow rated every
large cap a Sell; an owner earnings DCF at a flat 9% then made capex-heavy companies look very cheap (Meta
+141%) and counted debt twice (after-interest cash flow minus net debt). Both were replaced by this one.
"""

from __future__ import annotations

import json
from dataclasses import replace
from datetime import date, timedelta
from typing import Any

from fundamentalist import dcf
from fundamentalist.edgar import sec_get
from fundamentalist.market import beta, bottom_up_beta, industry_ev_ebit, industry_pbv, risk_free, synthetic_rating
from fundamentalist.parameters import value as param

REVENUE = ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet",
           "RevenueFromContractWithCustomerIncludingAssessedTax"]
NET_INCOME = ["NetIncomeLoss", "ProfitLoss"]
EBIT = ["OperatingIncomeLoss"]
PRETAX = ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
          "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
          "IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic"]
TAX = ["IncomeTaxExpenseBenefit"]
NONOPERATING = ["NonoperatingIncomeExpense", "OtherNonoperatingIncomeExpense"]
EQUITY_WITH_NCI = ["StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"]
INTEREST = ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt", "InterestAndDebtExpense",
            "InterestCostsIncurred"]
INTEREST_PAID = ["InterestPaidNet", "InterestPaid"]
SBC = ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"]
OCF = ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"]
CAPEX = ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"]
CASH = ["CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"]
SECURITIES = ["MarketableSecuritiesCurrent", "AvailableForSaleSecuritiesDebtSecuritiesCurrent", "ShortTermInvestments"]
DEBT_PARTS = [["LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations"],
              ["LongTermDebtCurrent", "LongTermDebtAndCapitalLeaseObligationsCurrent", "DebtCurrent"],
              ["CommercialPaper"], ["ShortTermBorrowings"]]
DEBT_TOTAL = ["LongTermDebt", "DebtAndCapitalLeaseObligations", "DebtInstrumentCarryingAmount"]
LEASES = [["OperatingLeaseLiabilityNoncurrent"], ["OperatingLeaseLiabilityCurrent"]]
LEASE_TOTAL = ["OperatingLeaseLiability"]
MINORITY = ["MinorityInterest"]
EQUITY = ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"]
GOODWILL = ["Goodwill"]
RD = ["ResearchAndDevelopmentExpense", "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost",
      "ResearchAndDevelopmentExpenseSoftwareExcludingAcquiredInProcessCost"]
FIN_RECEIVABLES = [["NotesAndLoansReceivableNetCurrent"], ["NotesAndLoansReceivableNetNoncurrent"],
                   ["FinancingReceivableExcludingAccruedInterestAfterAllowanceForCreditLoss"]]
ASSETS = ["Assets"]
INTANGIBLES = ["IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet"]
PREFERRED = ["PreferredStockValue", "PreferredStockValueOutstanding"]
NI_COMMON = ["NetIncomeLossAvailableToCommonStockholdersBasic", "NetIncomeLoss"]
BANK_SIC = {"6021", "6022", "6029", "6035", "6036", "6211"}  # commercial and savings banks, broker-dealers
INSURANCE_SIC = {"6311", "6321", "6331", "6351", "6361", "6399"}
DDM_SIC = {"6798", "4911", "4931", "4932", "4941"}  # REITs, electric and gas utilities, water
DIVIDENDS = ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends", "DividendsCommonStockCash", "DividendsCommonStock"]
DPS = ["CommonStockDividendsPerShareDeclared", "CommonStockDividendsPerShareCashPaid"]


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
    """Cover-page count, else balance sheet count, else diluted weighted average of the latest period."""
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
    # Yahoo can list the latest session with its volume but no close yet (seen 2026-10-01 for the 30 Sep
    # session on 19 of 21 tickers): such rows are skipped, so the price is the last session with a close.
    hist = yf.Ticker(ticker).history(start=start, end=end, auto_adjust=False).dropna(subset=["Close"])
    if hist.empty:
        raise ValueError(f"no Yahoo price for {ticker} near {as_of}")
    return float(hist["Close"].iloc[-1]), hist.index[-1].date().isoformat()


def _sum_instants(data: dict, groups: list[list[str]], total: list[str], as_of: str) -> dict | None:
    """Sum of component instants at their latest common date, else the total concept."""
    parts = [p for p in (_instant(data, c, as_of) for c in groups) if p]
    if parts:
        end = max(p["end"] for p in parts)
        same = [p for p in parts if p["end"] == end]
        return {"val": sum(p["val"] for p in same), "end": end, "concept": " + ".join(p["concept"] for p in same)}
    return _instant(data, total, as_of)


# ------------------------------------------------------------------ inputs
def fundamentals(ticker: str, as_of: str) -> dict[str, Any]:
    """Every figure the valuation uses, each with its concept and period."""
    data = company_facts(ticker)
    revenue = _ttm(data, REVENUE, as_of)
    revenue_year_ago = None
    if revenue:
        prior_end = (date.fromisoformat(revenue["end"]) - timedelta(days=364)).isoformat()
        revenue_year_ago = _ttm(data, [revenue["concept"]], as_of, near_end=prior_end)
    cash = _instant(data, CASH, as_of)
    securities = _instant(data, SECURITIES, as_of)
    debt_parts = [p for p in (_instant(data, c, as_of) for c in DEBT_PARTS) if p and cash and p["end"] == cash["end"]]
    total_debt = _instant(data, DEBT_TOTAL, as_of)
    return {
        "revenue": revenue, "revenue_year_ago": revenue_year_ago, "ebit": _ttm(data, EBIT, as_of),
        "pretax": _ttm(data, PRETAX, as_of), "tax": _ttm(data, TAX, as_of),
        "interest": _ttm(data, INTEREST, as_of) or _ttm(data, INTEREST_PAID, as_of),
        "sbc": _ttm(data, SBC, as_of), "net_income": _ttm(data, NET_INCOME, as_of),
        "operating_cash_flow": _ttm(data, OCF, as_of), "capex": _ttm(data, CAPEX, as_of),
        "cash": cash, "securities": securities if securities and cash and securities["end"] == cash["end"] else None,
        "debt": {"val": sum(p["val"] for p in debt_parts), "end": cash["end"],
                 "concept": " + ".join(p["concept"] for p in debt_parts)} if debt_parts else total_debt,
        "leases": _sum_instants(data, LEASES, LEASE_TOTAL, as_of), "minority": _instant(data, MINORITY, as_of),
        "equity": _instant(data, EQUITY, as_of), "preferred": _instant(data, PREFERRED, as_of),
        "ni_common": _ttm(data, NI_COMMON, as_of), "shares": _shares(data, as_of),
        "goodwill": _instant(data, GOODWILL, as_of), "intangibles": _instant(data, INTANGIBLES, as_of),
        "nonoperating": _ttm(data, NONOPERATING, as_of), "equity_with_nci": _instant(data, EQUITY_WITH_NCI, as_of),
        "roic_history": roic_history(data, as_of), "rd_ttm": _ttm(data, RD, as_of), "rd_annual": _annual(data, RD, as_of),
        "finance_receivables": sum(p["val"] for p in (_instant(data, c, as_of) for c in FIN_RECEIVABLES) if p) or None,
        "assets": _instant(data, ASSETS, as_of),
    }


def _annual(data: dict, concepts: list[str], as_of: str) -> dict[str, float]:
    """Fiscal-year values by period end, filed before as_of."""
    _, rows = _facts(data, concepts, as_of)
    return {r["end"]: r["val"] for r in rows if r.get("start") and 350 <= _days(r) <= 380}


def _at_ends(data: dict, concepts: list[str], as_of: str) -> dict[str, float]:
    _, rows = _facts(data, concepts, as_of)
    return {r["end"]: r["val"] for r in rows if not r.get("start")}


def roic_history(data: dict, as_of: str, years: int = 5) -> list[dict[str, float]]:
    """After-tax ROIC for the last fiscal years: EBIT x (1 - 25%) / (equity + debt - cash) at the year end."""
    ebit = _annual(data, EBIT, as_of)
    equity, cash = _at_ends(data, EQUITY, as_of), _at_ends(data, CASH, as_of)
    debt_total = _at_ends(data, DEBT_TOTAL, as_of)
    parts = [_at_ends(data, group, as_of) for group in DEBT_PARTS]

    def debt_at(end: str) -> float:
        return debt_total[end] if end in debt_total else sum(p.get(end, 0.0) for p in parts)

    out = []
    for end in sorted(ebit, reverse=True)[:years]:
        if end in equity:
            ic = equity[end] + debt_at(end) - cash.get(end, 0.0)
            if ic > 0:
                out.append({"end": end, "roic": round(ebit[end] * (1 - 0.25) / ic, 4)})
    return out


def moat(history: list[dict[str, float]], wacc: float) -> tuple[float, str]:
    """Terminal excess return share from ROIC history: 1.0 wide, 0.5 narrow, 0 none."""
    if len(history) < 3:
        return 0.5, f"only {len(history)} years of ROIC history: narrow by default"
    spreads = [h["roic"] - wacc for h in history]
    margin = param("moat_margin")
    if all(s >= margin for s in spreads):
        return 1.0, f"wide: ROIC beat WACC by {margin:.0%}+ in all {len(spreads)} years (min {min(spreads):+.1%})"
    if sum(spreads) / len(spreads) > 0:
        return 0.5, f"narrow: ROIC beat WACC on average over {len(spreads)} years ({sum(spreads) / len(spreads):+.1%})"
    return 0.0, f"none: ROIC averaged {sum(spreads) / len(spreads):+.1%} against WACC"


def complete(ticker: str, f: dict[str, Any]) -> list[str]:
    """Fill gaps that XBRL leaves: EBIT from pre-tax income + interest, debt checked against Yahoo."""
    notes = []
    if not f.get("ebit") and f.get("pretax"):
        if f.get("nonoperating"):  # non-operating income includes interest, so pre-tax minus it is operating income
            f["ebit"] = {"value": _v(f, "pretax") - _v(f, "nonoperating"), "end": f["pretax"]["end"],
                         "concept": "pre-tax income - NonoperatingIncomeExpense (no OperatingIncomeLoss)"}
        else:
            f["ebit"] = {"value": _v(f, "pretax") + _v(f, "interest"), "end": f["pretax"]["end"],
                         "concept": "pre-tax income + interest expense (no OperatingIncomeLoss)"}
        notes.append(f"EBIT built as {f['ebit']['concept']}")
    if not f.get("minority") and f.get("equity_with_nci") and f.get("equity"):
        nci = f["equity_with_nci"]["val"] - f["equity"]["val"]
        if nci > 0:
            f["minority"] = {"val": nci, "end": f["equity"]["end"], "concept": "equity incl. NCI - parent equity"}
    try:
        import yfinance as yf

        yahoo_debt = yf.Ticker(ticker).info.get("totalDebt")
    except Exception:  # noqa: BLE001 - Yahoo is only the cross-check
        yahoo_debt = None
    xbrl_debt = _v(f, "debt") + _v(f, "leases")
    if yahoo_debt and yahoo_debt > 1.5 * xbrl_debt + 1e9:
        f["debt"] = {"val": yahoo_debt - _v(f, "leases"), "end": "latest", "concept": "Yahoo totalDebt minus leases"}
        notes.append(f"debt from Yahoo totalDebt ({yahoo_debt / 1e9:,.1f}B): XBRL tags gave {xbrl_debt / 1e9:,.1f}B")
    return notes


def _v(f: dict, key: str) -> float:
    item = f.get(key)
    return float(item.get("value", item.get("val", 0.0))) if item else 0.0


def rd_life(industry: str | None) -> int:
    lives = param("capitalize_rd")["lives"]
    return next((years for key, years in lives.items() if key != "default" and industry and key.lower() in industry.lower()),
                lives["default"])


def research_asset(rd_ttm: float, annual: dict[str, float], life: int) -> tuple[float, float]:
    """Unamortized R&D (this year's in full, year t-k at (life - k) / life) and this year's amortization."""
    past = [annual[e] for e in sorted(annual, reverse=True)]  # most recent fiscal year first
    history = [rd_ttm] + past[1:life + 1] if past else [rd_ttm]
    asset = sum(v * (life - k) / life for k, v in enumerate(history[:life]))
    amortization = sum(v / life for v in history[1:life + 1])
    return asset, amortization


def cost_of_capital(ticker: str, f: dict, market_cap: float, as_of: str) -> dict[str, Any]:
    """WACC build-up: CAPM cost of equity, synthetic-rating cost of debt, market-value weights."""
    rf, rf_date = risk_free()
    t = param("marginal_tax")
    debt = _v(f, "debt") + (_v(f, "leases") if param("leases_as_debt") else 0.0) - f.get("captive_offset", 0.0)
    regression = beta(ticker, as_of)
    bottom_up = bottom_up_beta(ticker, debt / market_cap if market_cap > 0 else 0.0)
    b = dict(bottom_up or regression, regression=regression["used"], regression_raw=regression["raw"])
    if not bottom_up:
        b["method"] = "regression (no industry mapping for this ticker)"
    elif abs(bottom_up["used"] - regression["used"]) > param("beta_disagreement"):
        b["used"] = round((bottom_up["used"] + regression["used"]) / 2, 3)
        b["method"] = (f"average of bottom-up {bottom_up['used']} and regression {regression['used']} (they differ by more "
                       f"than {param('beta_disagreement')})")
    erp = param("equity_risk_premium")
    ke = rf + b["used"] * erp
    rating = synthetic_rating(_v(f, "ebit"), _v(f, "interest"))
    kd_pre = rf + rating["spread"]
    weight_e = market_cap / (market_cap + debt) if market_cap + debt > 0 else 1.0
    wacc = weight_e * ke + (1 - weight_e) * kd_pre * (1 - t)
    mature_beta = min(b["used"], 1.0) if param("mature_beta") == "toward_one_from_above" else 1.0
    mature = weight_e * (rf + mature_beta * erp) + (1 - weight_e) * kd_pre * (1 - t)
    return {"risk_free": round(rf, 4), "risk_free_date": rf_date, "beta": b, "erp": erp, "cost_of_equity": round(ke, 4),
            "rating": rating, "cost_of_debt_pre_tax": round(kd_pre, 4), "tax_shield_rate": t,
            "weight_equity": round(weight_e, 4), "debt_incl_leases": debt, "wacc": round(wacc, 4),
            "mature_wacc": round(mature, 4)}


# ------------------------------------------------------------------ valuation
def _sane(out: dict[str, Any], base: dict[str, Any], price: float, wacc: float) -> list[str]:
    bounds = param("sanity")
    issues = []
    lo, hi = bounds["fair_to_price"]
    ratio = base["per_share"] / price
    if not lo <= ratio <= hi:
        issues.append(f"base value is {ratio:.2f}x the price, outside {lo}x to {hi}x")
    if not bounds["wacc"][0] <= wacc <= bounds["wacc"][1]:
        issues.append(f"WACC {wacc:.1%} outside {bounds['wacc'][0]:.0%} to {bounds['wacc'][1]:.0%}")
    if base["terminal_share"] is not None and base["terminal_share"] > bounds["terminal_share"]:
        issues.append(f"terminal value is {base['terminal_share']:.0%} of enterprise value")
    return issues


def bank_value(ticker: str, as_of: str, price: float, price_date: str, sic: str) -> dict[str, Any]:
    """Justified price-to-book: P/B = (ROE - g) / (cost of equity - g), cost of equity from CAPM."""
    data = company_facts(ticker)
    equity, preferred = _instant(data, EQUITY, as_of), _instant(data, PREFERRED, as_of)
    ni = _ttm(data, NI_COMMON, as_of)
    count, count_source = checked_shares(ticker, _shares(data, as_of), as_of)
    out: dict[str, Any] = {"ticker": ticker.upper(), "as_of": as_of, "price": price, "price_date": price_date,
                           "sic": sic, "fair_value": None, "note": None, "model": "bank",
                           "method": "justified price-to-book on common equity: P/B = (ROE - g) / (cost of equity - g), "
                                     "cost of equity = risk-free + beta x ERP; bear/bull: ROE -/+2 points, cost of "
                                     "equity +/-0.5 points"}
    if not (equity and ni and count):
        out["note"] = "equity, net income or share count not available from XBRL"
        return out
    rf, rf_date = risk_free()
    regression = beta(ticker, as_of)
    b = bottom_up_beta(ticker, 0.0, bank=True) or regression
    if b is not regression and abs(b["used"] - regression["used"]) > param("beta_disagreement"):
        b = dict(b, used=round((b["used"] + regression["used"]) / 2, 3), method="average of industry and regression betas")
    b = dict(b, regression=regression["used"], regression_raw=regression["raw"])
    ke = rf + b["used"] * param("equity_risk_premium")
    g = min(rf, param("terminal_growth_cap"), ke - param("min_terminal_spread"))
    common = equity["val"] - (preferred["val"] if preferred and preferred["end"] == equity["end"] else 0)
    roe_latest, bvps = ni["value"] / common, common / count
    history = roe_history(data, as_of)
    roe = roe_latest
    if param("normalized_financial_roe") and len(history) >= 3:
        roe = sum(h["roe"] for h in history) / len(history)
    share, moat_why = moat([{"roic": h["roe"]} for h in history], ke)
    cap_share = param("financial_moat_cap")
    if share > cap_share:
        share, moat_why = cap_share, f"{moat_why}; capped at {cap_share} for a financial firm (cyclical returns)"
    fair = {}
    for name, (d_roe, d_ke, d_share) in {"bear": (-0.02, 0.005, 0.0), "base": (0.0, 0.0, None),
                                         "bull": (0.02, -0.005, 1.0)}.items():
        fair[name] = round(excess_return_value(bvps, roe + d_roe, ke + d_ke, g,
                                               share if d_share is None else min(d_share, cap_share)), 2)
    out.update(fair_value=fair, roe=round(roe, 4), roe_latest=round(roe_latest, 4), book_value_per_share=round(bvps, 2),
               cost_of_equity=round(ke, 4),
               implied_roe=round(price / bvps * (ke - g) + g, 4), terminal_growth=g, shares_outstanding=count,
               moat=moat_why, roe_history=history,
               shares_source=count_source, cash_conversion=None,
               capital={"risk_free": round(rf, 4), "risk_free_date": rf_date, "beta": b,
                        "erp": param("equity_risk_premium"), "cost_of_equity": round(ke, 4)},
               valuation_period=f"net income to common, twelve months to {ni['end']}; equity at {equity['end']}; "
                                f"the readers' evidence comes from the latest 10-K only")
    peer_industry, peer = industry_pbv(ticker)
    if peer and peer["roe"] > 0 and roe > 0:
        per_share = bvps * peer["pbv"] * (roe / peer["roe"])
        out["multiples_check"] = {"industry": peer_industry, "pbv": round(peer["pbv"], 2), "industry_roe": round(peer["roe"], 4),
                                  "value_per_share": round(per_share, 2), "dcf_to_multiples": round(fair["base"] / per_share, 3)}
    issues = []
    ratio = fair["base"] / price
    lo, hi = param("sanity")["fair_to_price"]
    if not lo <= ratio <= hi:
        issues.append(f"base value is {ratio:.2f}x the price, outside {lo}x to {hi}x")
    if issues:
        out.update(fair_value=None, note="not rated, review: " + "; ".join(issues), review=issues, fair_value_raw=fair)
    return out


def roe_history(data: dict, as_of: str, years: int = 5) -> list[dict[str, float]]:
    """ROE for the last fiscal years: net income to common / year-end equity."""
    ni, equity = _annual(data, NI_COMMON, as_of), _at_ends(data, EQUITY, as_of)
    return [{"end": end, "roe": round(ni[end] / equity[end], 4)} for end in sorted(ni, reverse=True)[:years]
            if equity.get(end, 0) > 0]


def revenue_cagr(data: dict, concept: str, as_of: str, years: int = 3) -> float | None:
    """Fiscal-year revenue CAGR over *years*, from one XBRL concept, or None without the history."""
    annual = _annual(data, [concept], as_of)
    if not annual:
        return None
    last = max(annual)
    target = date.fromisoformat(last) - timedelta(days=365 * years)
    start = [e for e in annual if abs((date.fromisoformat(e) - target).days) <= 20]
    if not start or annual[start[0]] <= 0:
        return None
    return (annual[last] / annual[start[0]]) ** (1 / years) - 1


def excess_return_value(bvps: float, roe: float, ke: float, g: float, moat_share: float, years: int = 10) -> float:
    """Book value per share plus the present value of excess returns, ROE fading to Ke + share x (ROE - Ke)."""
    roe_end = ke + moat_share * (roe - ke)
    value, bv, discount = bvps, bvps, 1.0
    for t in range(1, years + 1):
        r = roe + (roe_end - roe) * t / years
        discount /= 1 + ke
        value += (r - ke) * bv * discount
        bv *= 1 + g
    return value + (roe_end - ke) * bv / (ke - g) * discount


def dividend_value(ticker: str, as_of: str, price: float, price_date: str, sic: str) -> dict[str, Any]:
    """Two-stage dividend discount model for REITs and utilities."""
    data = company_facts(ticker)
    cfg = param("ddm")
    count, count_source = checked_shares(ticker, _shares(data, as_of), as_of)
    dividends = _ttm(data, DIVIDENDS, as_of)
    out: dict[str, Any] = {"ticker": ticker.upper(), "as_of": as_of, "price": price, "price_date": price_date, "sic": sic,
                           "fair_value": None, "note": None, "model": "ddm",
                           "method": "two-stage dividend discount: dividends per share grow at the revenue growth blend "
                                     "(bounded -5% to 8%) for 5 years, fading to terminal growth = risk-free rate, at the "
                                     "CAPM cost of equity; bear/bull growth -/+2 points, cost of equity +/-0.5 points"}
    f = fundamentals(ticker, as_of)
    if not (dividends and count and f.get("revenue") and f.get("revenue_year_ago")):
        out["note"] = "dividends, share count or revenue history not available from XBRL"
        return out
    rf, rf_date = risk_free()
    debt = _v(f, "debt") + _v(f, "leases")
    regression = beta(ticker, as_of)
    b = bottom_up_beta(ticker, debt / (price * count)) or regression
    if b is not regression and abs(b["used"] - regression["used"]) > param("beta_disagreement"):
        b = dict(b, used=round((b["used"] + regression["used"]) / 2, 3), method="average of bottom-up and regression betas")
    b = dict(b, regression=regression["used"])
    ke = rf + b["used"] * param("equity_risk_premium")
    dps_growth = dps_cagr(data, as_of)
    if dps_growth is not None:
        g1, growth_source = dps_growth, "3-year dividend per share CAGR"
    else:
        growth_ttm = _v(f, "revenue") / _v(f, "revenue_year_ago") - 1
        cagr = revenue_cagr(data, f["revenue"]["concept"], as_of)
        w = param("growth_blend")
        g1 = growth_ttm if cagr is None else w["ttm"] * growth_ttm + w["cagr_3y"] * cagr
        growth_source = "revenue growth blend (no dividend per share history)"
    lo, hi = cfg["growth_bounds"]
    g1 = min(max(g1, lo), hi)
    g_t = min(rf, param("terminal_growth_cap"), max(g1, 0.0), ke - param("min_terminal_spread"))  # own dividend growth, spread
    d0 = dividends["value"] / count
    dg, dk = cfg["bear_bull"]
    fair = {name: round(ddm_value(d0, g1 + sg * dg, g_t, ke + sk * dk, cfg["stage1_years"]), 2)
            for name, (sg, sk) in {"bear": (-1, 1), "base": (0, 0), "bull": (1, -1)}.items()}
    out.update(fair_value=fair, dividend_per_share=round(d0, 4), growth_used=round(g1, 4), growth_source=growth_source,
               terminal_growth=g_t,
               cost_of_equity=round(ke, 4), dividend_yield=round(d0 / price, 4), shares_outstanding=count,
               shares_source=count_source, cash_conversion=None,
               capital={"risk_free": round(rf, 4), "risk_free_date": rf_date, "beta": b,
                        "erp": param("equity_risk_premium"), "cost_of_equity": round(ke, 4)},
               valuation_period=f"dividends paid, twelve months to {dividends['end']}")
    lo_s, hi_s = param("sanity")["fair_to_price"]
    ratio = fair["base"] / price
    if not lo_s <= ratio <= hi_s:
        out.update(fair_value=None, fair_value_raw=fair, review=[f"base value is {ratio:.2f}x the price"],
                   note=f"not rated, review: base value is {ratio:.2f}x the price, outside {lo_s}x to {hi_s}x")
    return out


def dps_cagr(data: dict, as_of: str, years: int = 3) -> float | None:
    """Fiscal-year dividend per share CAGR over *years*, or None without the history."""
    concept, rows = _facts(data, DPS, as_of, unit="USD/shares")
    annual = {r["end"]: r["val"] for r in rows if r.get("start") and 350 <= _days(r) <= 380}
    if not annual:
        return None
    last = max(annual)
    target = date.fromisoformat(last) - timedelta(days=365 * years)
    start = [e for e in annual if abs((date.fromisoformat(e) - target).days) <= 20]
    if not start or annual[start[0]] <= 0:
        return None
    return (annual[last] / annual[start[0]]) ** (1 / years) - 1


def ddm_value(d0: float, g1: float, g_t: float, ke: float, years: int = 5) -> float:
    """Dividends growing at g1 for *years*, fading linearly to g_t over another *years*, then a Gordon terminal value."""
    value, d, discount = 0.0, d0, 1.0
    for t in range(1, 2 * years + 1):
        g = g1 if t <= years else g1 + (g_t - g1) * (t - years) / years
        d *= 1 + g
        discount /= 1 + ke
        value += d * discount
    return value + d * (1 + g_t) / (ke - g_t) * discount


def value(ticker: str, as_of: str | None = None) -> dict[str, Any]:
    """Fair value range per share, the WACC and inputs behind it, and why it is missing when it is."""
    as_of = as_of or date.today().isoformat()
    price, price_date = last_price(ticker, as_of)
    sic, _ = industry(ticker)
    if sic in BANK_SIC or sic in INSURANCE_SIC:
        out = bank_value(ticker, as_of, price, price_date, sic)
        out["model"] = "bank" if sic in BANK_SIC else "insurer"
        return out
    if sic in DDM_SIC:
        return dividend_value(ticker, as_of, price, price_date, sic)
    f = fundamentals(ticker, as_of)
    data_notes = complete(ticker, f)
    count, count_source = checked_shares(ticker, f["shares"], as_of)
    out: dict[str, Any] = {"ticker": ticker.upper(), "as_of": as_of, "price": price, "price_date": price_date,
                           "sic": sic, "inputs": f, "fair_value": None, "note": None, "model": "fcff",
                           "method": "FCFF DCF at company WACC (maturing toward beta 1 from above): trailing revenue "
                                     "growth held 5 years if at most 10%, otherwise decaying to 10% by year 5, then fading "
                                     "to terminal growth = risk-free rate over 5 years; reinvestment = change in revenue / "
                                     "operating sales-to-capital; SBC expensed; R&D capitalized where material; leases as "
                                     "debt; terminal ROIC keeps the moat share (from 5-year ROIC history) of today's excess "
                                     "return; bear/base/bull shift growth -/+4 points, margin -/+10% relative, WACC "
                                     "+/-0.5 points, moat share 0/history/1"}
    missing = [k for k in ("revenue", "revenue_year_ago", "ebit", "equity") if not f.get(k)]
    if not count:
        missing.append("share count")
    if missing:
        out["note"] = f"not available from XBRL: {', '.join(missing)}"
        return out
    revenue, ebit = _v(f, "revenue"), _v(f, "ebit")
    if ebit <= 0:
        out["note"] = f"operating income is negative ({ebit:,.0f}): not rated by this model"
        return out
    pretax, tax = _v(f, "pretax"), _v(f, "tax")
    effective = min(max(tax / pretax, 0.0), param("marginal_tax")) if pretax > 0 else param("marginal_tax")
    receivables, assets = f.get("finance_receivables") or 0.0, _v(f, "assets")
    if assets and receivables > param("captive_finance")["min_share_of_assets"] * assets:
        f["captive_offset"] = min(receivables, _v(f, "debt"))
        data_notes.append(f"captive finance: {receivables / 1e9:,.1f}B of finance receivables netted against debt")
    debt = _v(f, "debt") + (_v(f, "leases") if param("leases_as_debt") else 0.0) - f.get("captive_offset", 0.0)
    cash = _v(f, "cash") + _v(f, "securities")
    invested = _v(f, "equity") + debt - cash
    if invested <= 0.05 * revenue:  # buybacks can push book capital near zero; fall back to operating capital
        invested = max(invested, 0.2 * revenue)
        out["invested_capital_note"] = "book invested capital near zero or negative, floored at 20% of revenue"
    operating = invested
    if param("capital_for_reinvestment") == "operating":
        operating = max(invested - _v(f, "goodwill") - _v(f, "intangibles"), 0.2 * revenue)
    rd_note, rd_margin_adjustment, reported_margin = None, 0.0, ebit / revenue
    rd_ttm = _v(f, "rd_ttm")
    if rd_ttm > param("capitalize_rd")["min_share_of_revenue"] * revenue and f.get("rd_annual"):
        from fundamentalist.market import _ticker_industries
        life = rd_life(_ticker_industries().get(ticker.upper()))
        asset, amortization = research_asset(rd_ttm, f["rd_annual"], life)
        ebit += rd_ttm - amortization
        rd_margin_adjustment = (rd_ttm - amortization) / revenue
        invested += asset
        operating += asset
        rd_note = (f"R&D capitalized over {life} years: research asset {asset / 1e9:,.1f}B, EBIT +{(rd_ttm - amortization) / 1e9:,.1f}B "
                   f"(R&D {rd_ttm / 1e9:,.1f}B - amortization {amortization / 1e9:,.1f}B)")
        data_notes.append(rd_note)
    growth_ttm = revenue / _v(f, "revenue_year_ago") - 1
    cagr = revenue_cagr(company_facts(ticker), f["revenue"]["concept"], as_of)
    weights = param("growth_blend")
    growth_raw = growth_ttm if cagr is None else weights["ttm"] * growth_ttm + weights["cagr_3y"] * cagr
    lo, hi = param("growth_bounds")
    market_cap = price * count
    capital = cost_of_capital(ticker, f, market_cap, as_of)
    wacc = capital["wacc"]
    rf = capital["risk_free"]
    excess, moat_why = moat(f["roic_history"], wacc)
    x = dcf.Inputs(
        revenue=revenue, ebit=ebit, effective_tax=effective, marginal_tax=param("marginal_tax"),
        invested_capital=invested, operating_capital=operating, growth=min(max(growth_raw, lo), hi),
        terminal_growth=min(rf, param("terminal_growth_cap"),
                            (capital["mature_wacc"] if param("mature_wacc") else wacc) - param("min_terminal_spread")),
        wacc=wacc,
        terminal_excess_return=excess,
        mature_wacc=capital["mature_wacc"] if param("mature_wacc") else None, year5_growth_cap=param("year5_growth_cap"),
        high_growth_years=param("high_growth_years"),
        fade_years=param("fade_years"), mid_year=param("mid_year"), debt=debt, cash=cash,
        minority=_v(f, "minority"), shares=count)
    out["dcf_inputs"] = x
    runs = {name: dcf.value_per_share(dcf.scenario(x, name)) for name in ("bear", "base", "bull")}
    fair = {name: round(r["per_share"], 2) for name, r in runs.items()}
    base = runs["base"]
    implied = dcf.implied_growth(x, price)
    out.update(
        fair_value=fair, capital=capital, wacc=wacc, revenue_growth=round(growth_raw, 4), growth_used=round(x.growth, 4),
        revenue_growth_ttm=round(growth_ttm, 4), revenue_cagr_3y=round(cagr, 4) if cagr is not None else None,
        implied_growth=round(implied, 4) if implied is not None else None, operating_margin=round(x.margin, 4),
        operating_margin_reported=round(reported_margin, 4), rd_margin_adjustment=round(rd_margin_adjustment, 4),
        roic=round(x.roic, 4), sales_to_capital=round(x.sales_to_capital, 3), effective_tax=round(effective, 4),
        terminal_growth=x.terminal_growth, terminal_roic=round(base["terminal_roic"], 4),
        terminal_share=round(base["terminal_share"], 3) if base["terminal_share"] else None,
        ev_to_ebit=round(base["ev_to_ebit"], 1) if base["ev_to_ebit"] else None,
        market_ev_to_ebit=round((market_cap + debt + _v(f, "minority") - cash) / ebit, 1),
        shares_outstanding=count, shares_source=count_source, net_debt=debt - cash, data_notes=data_notes,
        moat=moat_why, terminal_excess_return=excess, roic_history=f["roic_history"],
        cash_conversion=round(_v(f, "operating_cash_flow") / (ebit * (1 - effective)), 3) if ebit > 0 else None,
        sbc_to_revenue=round(_v(f, "sbc") / revenue, 4), sensitivity=dcf.sensitivity(x),
        valuation_period=(f"trailing twelve months to {f['ebit']['end']} (revenue growth: twelve months to "
                          f"{f['revenue']['end']} vs to {f['revenue_year_ago']['end']}), from 10-K and 10-Q XBRL; "
                          f"the readers' evidence comes from the latest 10-K only"))
    peer_industry, multiple = industry_ev_ebit(ticker)
    if multiple:
        reported_ebit = revenue * reported_margin
        per_share = (multiple * reported_ebit - debt - _v(f, "minority") + cash) / count
        out["multiples_check"] = {"industry": peer_industry, "ev_to_ebit": round(multiple, 1), "value_per_share": round(per_share, 2),
                                  "dcf_to_multiples": round(fair["base"] / per_share, 3) if per_share > 0 else None}
    issues = _sane(out, base, price, wacc)
    if issues:
        out.update(fair_value=None, fair_value_raw=fair, review=issues, note="not rated, review: " + "; ".join(issues))
    return out
