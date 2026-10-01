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
    Parameter("beta_bounds_bottom_up", (0.5, 2.0), "clip for bottom-up betas; the 0.8 floor above is for noisy "
              "regression betas, and applying it to an industry average across many firms pushed a utility's cost of "
              "equity up (Duke Energy)", "Damodaran applies no bounds to bottom-up betas", "0.8 to 2.0 for both"),
    Parameter("beta_disagreement", 0.3, "when bottom-up and regression betas differ by more than this, use their average "
              "and say so: the industry can misfit the company (Damodaran files Visa with insurers and lenders)",
              "own guard; Damodaran notes the industry mix must match the business", "trust bottom-up alone"),
    Parameter("min_terminal_spread", 0.03, "terminal discount rate minus terminal growth is at least 3 points; terminal "
              "growth is lowered to meet it", "FinRobot enforces WACC - g of at least 1.5 points; a thin Gordon denominator "
              "makes value explode (at a 2-point spread each 0.1 point moves value about 5%)", "1.5 points; none"),
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
    Parameter("growth_bounds", (-0.05, 0.30), "starting revenue growth (the blend below), clipped",
              "own choice", "analyst consensus (not free)"),
    Parameter("margin_correction_band", 0.30, "a red team operating margin correction counts only within 30% "
              "(relative) of the reported trailing margin from XBRL; further away it contradicts an audited figure "
              "instead of correcting it", "own rule after Visa, 2026-10-01: operating expenses / revenue (32%) was "
              "submitted as the operating margin (reported 61%) and cost a notch in one repeat",
              "no band (corrections bounded 0 to 80% only); require the value in a cited claim (rejects every "
              "computed margin, right or wrong)"),
    Parameter("growth_blend", {"ttm": 0.5, "cagr_3y": 0.5}, "starting growth = weighted average of the last twelve "
              "months' revenue growth and the 3-year fiscal revenue CAGR (same XBRL tag); TTM alone when the history is "
              "missing", "base rates: one year of growth is noisy and mean-reverts (Mauboussin and Callahan, 2016)",
              "TTM only; 3-year CAGR only; 5-year CAGR"),
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
    Parameter("model_routes", {"excess_return": "banks 6021/6022/6029/6035/6036, broker-dealers 6211, insurers "
                                                  "6311/6321/6331/6351/6361/6399",
                                "dividend_discount": "REITs 6798, utilities 4911/4931/4932/4941"},
              "SEC industry code picks the model: FCFF needs operating debt and free cash flow that banks, insurers, "
              "REITs and utilities do not have in a meaningful form", "Damodaran on financial firms and on REITs and "
              "regulated utilities (dividend and excess return models)", "FCFF for everyone"),
    Parameter("financial_ke_floor", "industry_implied", "banks and insurers: cost of equity = the higher of CAPM and "
              "the cost of equity at which this desk's own excess return model (same fade and moat cap) prices the "
              "industry's book at the industry's price-to-book and ROE (Damodaran, January 2026). CAPM on insurers' low "
              "betas (0.64) gave 7.4%, which made every insurer 1.4 to 1.6x its own industry multiple",
              "found on the 2026-10-01 run by the multiples cross-check; insurers' low market betas understate risk "
              "the market prices (catastrophe and reserve risk)", "CAPM only; a fixed beta floor of 1.0"),
    Parameter("financial_moat_cap", 0.5, "banks and insurers keep at most half of today's ROE - cost of equity spread "
              "in the terminal value, whatever their ROE history: their returns are cyclical (Progressive's 34% ROE after a "
              "hard insurance market is priced at an implied 11.8%)", "Damodaran fades financial firms' excess returns "
              "toward the cost of equity", "the same moat rule as other companies (let a 5-year run count as a moat)"),
    Parameter("normalized_financial_roe", True, "banks and insurers start from their 5-year average ROE (at least 3 "
              "years), not the latest year: insurance and credit cycles make a single year misleading (Progressive 34%, "
              "Travelers 25% after a hard insurance market)", "Damodaran: normalize earnings for cyclical firms",
              "latest twelve months' ROE"),
    Parameter("utility_model", {"growth_bounds": (0.0, 0.07), "signal_range": (-0.05, 0.15), "max_age_days": 456},
              "regulated utilities (SIC 4911/4931/4932/4941): earnings per share grow at the median of the 3-year growth "
              "of net plant (rate base proxy; utility or general PP&E tag, latest value under 15 months old) and of "
              "earnings per share, each used only between -5% and 15% (AEP's plant tag changed scope: -78%), the result "
              "bounded 0 to 7% (the top of typical utility EPS guidance: rate base growth above it is partly funded by "
              "new shares); dividends = earnings x a payout moving to 1 - g / ROE",
              "practice: utilities are valued on rate base growth and allowed ROE (NARUC ratemaking; Damodaran's DDM "
              "with payout tied to growth and ROE); Duke guides 5 to 7% EPS growth against a 2% dividend trend",
              "dividend trend (rejected: Duke 82 vs 114); full rate base x allowed ROE model (allowed ROE tags are "
              "dimensional, not in the company facts API)"),
    Parameter("ddm", {"stage1_years": 5, "growth_bounds": (-0.05, 0.08), "bear_bull": (0.02, 0.005)},
              "two-stage dividend discount: dividends per share grow at their own 3-year growth (revenue growth blend when "
              "there is no per-share history; REITs grow revenue partly by issuing shares), bounded -5% to 8%, for "
              "5 years, fading linearly to terminal growth = risk-free rate but never above the company's own dividend growth (payout "
              "leaves little retention to fund more; Damodaran ties dividend-model growth to payout), discounted at the CAPM "
              "cost of equity; "
              "bear/bull move growth -/+2 points and cost of equity +/-0.5 points",
              "Damodaran, dividend discount models for REITs and utilities", "FFO multiples; net asset value"),
    Parameter("sanity", {"fair_to_price": (0.25, 4.0), "wacc": (0.05, 0.15), "terminal_share": 0.95},
              "results outside these bounds are not rated and are sent for review", "own choice", "tighter bounds"),
    Parameter("rating_bands", {"Low": (0.80, 1.25), "Medium": (0.70, 1.35), "High": (0.60, 1.55),
                               "Very High": (0.50, 1.75), "Extreme": (0.25, 4.00)},
              "price / base fair value thresholds for Buy (at or below the first) and Sell (at or above the second) by "
              "uncertainty; Overweight up to 1 - (1 - buy)/4, Underweight from 1 + (sell - 1)/5, Hold between",
              "Morningstar star rating bands (methodology, Sept 2022)", "fixed bands for all companies"),
    Parameter("multiples_check", {"agree": (0.67, 1.5)}, "second method: industry EV/EBIT (Damodaran, January 2026) x "
              "reported EBIT, bridged to a value per share; when DCF / multiples value falls outside 0.67 to 1.5, "
              "uncertainty goes up one level (a wider margin of safety, not a rating notch)",
              "practice: analysts triangulate DCF with relative value; Damodaran vebitda.xls industry averages",
              "EV/EBITDA or forward P/E; use the multiples value in the rating"),
    Parameter("multiples_check_financials", "roe_adjusted_pbv", "second method for banks and insurers: book value per "
              "share x industry P/B x (company ROE / industry ROE); same 0.67 to 1.5 agreement band",
              "Damodaran pbvdata.xls industry averages (January 2026); P/B scales with ROE", "plain industry P/B"),
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
