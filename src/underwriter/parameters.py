"""Every valuation parameter in one place, each with its value, method, source, alternatives and status.

Nothing in the valuation uses a number that is not listed here or fetched live, so every choice can be
questioned: the memo prints this table, the sensitivity grid shows what each one moves, and the red team
cites parameters by name in its method review. `verified` records whether the value was checked on a
primary source on `as_of`; unverified values are printed as such.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Parameter:
    name: str
    value: Any
    method: str
    source: str
    alternatives: str
    as_of: str = ""
    verified: bool = False


PARAMS: dict[str, Parameter] = {p.name: p for p in [
    Parameter("risk_free", "erp_date", "10-year US Treasury (FRED DGS10) on the date the ERP was computed, so the pair "
              "is consistent (Damodaran computes his implied ERP against that day's yield); 'spot' uses the latest yield",
              "FRED series DGS10", "spot yield (5.26% on 2026-09-29 vs 4.79% on 2026-09-01); 5-year average (Simply Wall St); "
              "normalized 4.5% (Morningstar); 30-year Treasury"),
    Parameter("equity_risk_premium", 0.0414, "Damodaran's implied ERP for the S&P 500 (forward-looking, from index level "
              "and expected cash flows)", "Damodaran, implied ERP update of 2026-09-01 (pages.stern.nyu.edu/~adamodar)",
              "his alternative methods range 3.56% to 6.05%; FinRobot 4.23%; Alpha Spread 4.3%; Morningstar about 4.5%; "
              "GuruFocus 6%", as_of="2026-09-01", verified=True),
    Parameter("erp_date", "2026-09-01", "date of the ERP above", "Damodaran's monthly update", "update monthly"),
    Parameter("erp_risk_free", 0.0475, "the 10-year rate Damodaran computed the 4.14% ERP on, paired with it",
              "Damodaran ERP update 2026-09-01 (rf 4.75%)", "spot 10-year 5.26% (2026-09-29): pairing it with a September 1 "
              "ERP mixes dates; Kroll's 5.0% ERP pairs with the spot 20-year (5.64%), never with the 10-year",
              as_of="2026-09-01", verified=True),
    Parameter("beta_method", "bottom_up", "Damodaran industry unlevered beta corrected for cash, relevered with Hamada "
              "at the firm's market D/E (leases included) and the 25% marginal rate; banks take the industry levered "
              "beta; the regression beta is printed as a cross-check and used only when the ticker has no industry",
              "Damodaran betas.xls (2026-01-05) and his company-to-industry file indname.xls (2026-01-08); he prefers "
              "bottom-up because regression betas carry standard errors near 0.2",
              "regression: 5 years monthly on the S&P 500, Blume-adjusted (Bloomberg); 2-year weekly",
              as_of="2026-01", verified=True),
    Parameter("beta_bounds", (0.8, 2.0), "clip the adjusted beta to this range",
              "Simply Wall St's published bounds (0.8 to 2.0)", "no bounds; FinRobot's 0 to 5 plus 70% of industry beta"),
    Parameter("mature_wacc", True, "the cost of capital moves linearly over the fade years to a mature company's: "
              "cost of equity rf + 1.0 x ERP, same debt weight", "Damodaran Ginzu (cost of capital moves to rf + mature "
              "ERP by year 10)", "constant WACC for all years"),
    Parameter("marginal_tax", 0.25, "US federal 21% plus state, for the debt tax shield, unlevering betas and "
              "terminal NOPAT", "Damodaran uses 25% (betas.xls, Ginzu); Tax Foundation 25.63% (2026-01-05)",
              "21% federal only; effective rate", as_of="2026-01", verified=True),
    Parameter("rating_spreads", "damodaran_large", "synthetic rating from interest coverage (EBIT / interest expense), "
              "default spread added to the risk-free rate", "Damodaran, ratings and spreads table for large non-financial "
              "firms (market cap of $5bn or more), January 2026", "yield to maturity on the company's bonds; actual "
              "rating plus ICE BofA spread; interest expense / debt", as_of="2026-01", verified=True),
    Parameter("high_growth_years", 5, "years at the starting revenue growth before the fade", "Damodaran Ginzu default",
              "3 for mature firms; 10 for early-stage growth"),
    Parameter("fade_years", 5, "years over which growth fades linearly to the terminal rate", "Damodaran Ginzu default",
              "0 (two-stage); 10"),
    Parameter("year5_growth_cap", 0.10, "growth above this does not plateau: it decays linearly from year 1 to this "
              "rate by year 5, then fades to terminal; growth at or below it holds for 5 years (Ginzu)",
              "base rates: Mauboussin and Callahan, The Base Rate Book (2016), sales growth mean-reverts fast and few "
              "large companies sustain 20%+ for five years", "flat plateau at the trailing rate (Ginzu with no judgment); "
              "analyst consensus (not free)"),
    Parameter("growth_bounds", (-0.05, 0.30), "starting revenue growth = last twelve months' growth, clipped",
              "own choice; one year of history is noisy", "3-year revenue CAGR; analyst consensus (not free)"),
    Parameter("terminal_growth_cap", 0.0475, "terminal growth = min(risk-free rate, cap); the cap equals the paired "
              "risk-free rate, so terminal growth = rf, the assumption Damodaran's implied ERP is computed with",
              "Damodaran Ginzu and Simply Wall St: g = rf; never above it", "3.5% (conservative; on 2026-09-30 it moved "
              "the median price / fair value of 13 large caps from 1.07 to 1.27, bearish by construction)"),
    Parameter("terminal_excess_return", "moat_from_roic_history", "share of today's ROIC - WACC spread that survives "
              "in the terminal value, set from the last 5 fiscal years: 1.0 when ROIC beat WACC by at least the moat "
              "margin every year (wide moat), 0.5 when it beat WACC on average (narrow), 0 otherwise (none)",
              "Morningstar ties the fade of excess returns to moat; Damodaran's default is 0 (ROIC = WACC)",
              "0 for every company (Damodaran default); a flat 0.5"),
    Parameter("moat_margin", 0.05, "ROIC - WACC spread required in each of the last 5 years for a wide moat",
              "own choice, in the spirit of Morningstar's moat test", "3 or 10 points"),
    Parameter("mature_beta", "toward_one_from_above", "in the fade years beta moves to 1.0 only when it is above 1; "
              "a firm already below 1 keeps its own beta", "Damodaran moves mature firms toward beta 1; applying that to "
              "low-beta staples raises their cost of capital, so only high-beta firms converge here",
              "every firm to 1.0 (Ginzu default); industry bottom-up beta"),
    Parameter("capital_for_reinvestment", "operating", "sales-to-capital uses invested capital without goodwill and "
              "acquired intangibles, so organic growth is not charged acquisition premiums; ROIC keeps goodwill",
              "McKinsey Valuation: ROIC with and without goodwill", "all invested capital; industry sales-to-capital"),
    Parameter("sbc_as_expense", True, "stock-based compensation is a real cost: it stays in EBIT and is not added back "
              "to cash flow", "Damodaran; McKinsey Valuation", "add back (common in screeners), which inflates value "
              "for tech"),
    Parameter("capitalize_rd", {"min_share_of_revenue": 0.02, "lives": {"Drug": 10, "Biotech": 10, "Software": 3,
                                                                         "Semiconductor": 5, "Computer": 5, "Electronic": 5,
                                                                         "Internet": 3, "Entertainment": 3, "default": 5}},
              "R&D above 2% of revenue is capitalized: research asset = unamortized past R&D (straight line over the "
              "industry life), EBIT + R&D - amortization, invested capital + research asset",
              "Damodaran R&D converter (R&DConv.xls): Drug 10 years, software 3, semiconductors and computers 5; "
              "industry names mapped by keyword to his current industries", "expense R&D as reported"),
    Parameter("captive_finance", {"min_share_of_assets": 0.10}, "when finance receivables exceed 10% of total assets, "
              "they are netted against debt: the financing arm's debt funds its receivables",
              "common practice: net debt excluding financial services (industrial companies with captive finance arms)",
              "count all debt; value the finance arm separately"),
    Parameter("leases_as_debt", True, "operating lease liabilities (ASC 842) count as debt in the weights and the "
              "equity bridge", "Damodaran; McKinsey", "ignore leases"),
    Parameter("mid_year", True, "cash flows arrive mid-year on average", "McKinsey Valuation", "end-of-year discounting"),
    Parameter("cash_conversion", "ocf_over_nopat", "operating cash flow / NOPAT, caution below 0.8",
              "NOPAT excludes non-operating gains that inflate net income (Alphabet's equity stakes)",
              "operating cash flow / net income"),
    Parameter("bank_model", "excess_return", "equity = book value + PV of (ROE - Ke) x book value, ROE fading linearly "
              "over 10 years to Ke + moat share x (ROE - Ke), book value growing at terminal growth; moat share from 5-year "
              "ROE history against Ke", "Damodaran, excess return model for financial firms (finfirm09.pdf, eqexret.xls)",
              "justified P/B with today's ROE forever (overvalues high-ROE banks); dividend discount model"),
    Parameter("sanity", {"fair_to_price": (0.25, 4.0), "wacc": (0.05, 0.15), "terminal_share": 0.95},
              "results outside these bounds are not rated and are sent for review", "own choice", "tighter bounds"),
    Parameter("rating_bands", {"Low": (0.80, 1.25), "Medium": (0.70, 1.35), "High": (0.60, 1.55),
                               "Very High": (0.50, 1.75), "Extreme": (0.25, 4.00)},
              "price / base fair value thresholds for Buy (at or below the first) and Sell (at or above the second) by "
              "uncertainty; Overweight up to 1 - (1 - buy)/4, Underweight from 1 + (sell - 1)/5, Hold between",
              "Morningstar star rating bands (methodology, Sept 2022)", "fixed bands for all companies"),
    Parameter("uncertainty", {"volatility": (0.20, 0.30, 0.45, 0.60), "range_overlay": 1.5},
              "starting level from 12-month return volatility (Low below 20%, Medium below 30%, High below 45%, Very High "
              "below 60%, else Extreme), one level up when the fair value range (bull - bear) / base exceeds 1.5 "
              "(the four scenario levers make most ranges 1.0 to 1.3x base)",
              "Morningstar starts from return volatility and adds an analyst overlay; the thresholds here are own choice",
              "range width alone; volatility alone"),
]}


def value(name: str) -> Any:
    return PARAMS[name].value


def table() -> list[dict[str, Any]]:
    return [dict(p.__dict__) for p in PARAMS.values()]
