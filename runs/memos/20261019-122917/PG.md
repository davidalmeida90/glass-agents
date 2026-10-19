# PG: Hold

Desk memo, 2026-10-19. Price 159.35 (2026-10-16). Noise meter agreement 100% (Hold). Target weight 0.0%.

## Why

- price / base fair value 1.04 at Low uncertainty (volatility 20%, range 1.31x base, DCF / industry multiples 1.21): Buy at or below 0.80, Overweight to 0.95, Underweight from 1.05, Sell from 1.25

## Valuation

Method: FCFF DCF at company WACC (maturing toward beta 1 from above): trailing revenue growth held 5 years if at most 10%, otherwise decaying to 10% by year 5, then fading to terminal growth = risk-free rate over 5 years; reinvestment = change in revenue / operating sales-to-capital; SBC expensed; R&D capitalized where material; leases as debt; terminal ROIC keeps the moat share (from 5-year ROIC history) of today's excess return; bear/base/bull shift growth -/+4 points, margin -/+10% relative, WACC +/-0.5 points, moat share 0/history/1

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 65.19 | 153.60 | 266.13 | 1.04 |

| Cost of capital | Value |
|---|---:|
| Risk-free (2026-09-01 (rate in Damodaran's ERP computation)) | 4.8% |
| Beta (Household Products; regression 0.8) | 0.794 |
| Equity risk premium | 4.1% |
| Cost of equity | 8.0% |
| Synthetic rating (coverage 22.52) | AAA |
| Cost of debt, pre-tax | 5.1% |
| Equity weight | 91.4% |
| **WACC** (maturing to 7.7%) | **7.7%** |

- Revenue growth: last twelve months 3.3%, 3-year CAGR 2.0%, blend 2.6% (used 2.6%); the price implies 3.2%
- Operating margin 22.8% (reported 22.7% + R&D adjustment 0.1%), ROIC 18.4%, sales-to-capital 3.69, SBC 0.6% of revenue
- Moat: wide: ROIC beat WACC by 5%+ in all 5 years (min +10.8%)
- What must be true: at the modelled growth the price needs a constant operating margin of 23.3% (reported basis), at the 80% point of its own 10-year range (8.1% to 24.3%)
- Industry multiples check: Household Products EV/EBIT 16.3x gives 127.21 per share; DCF / multiples 1.207
- Terminal value 69.0% of enterprise value; EV/EBIT at base 19.3x vs market 19.9x
- Period: trailing twelve months to 2026-06-30 (revenue growth: twelve months to 2026-06-30 vs to 2025-06-30), from 10-K and 10-Q XBRL; the readers' evidence comes from the latest 10-K, 10-Q and earnings release

Base value per share, WACC by terminal growth:

| | g -0.5% | g +0.0% | g +0.5% |
|---|---:|---:|---:|
| wacc -1.0% | 147.11 | 162.64 | 184.21 |
| wacc +0.0% | 138.98 | 153.60 | 173.91 |
| wacc +1.0% | 131.38 | 145.14 | 164.26 |

- Data note: R&D capitalized over 5 years: research asset 6.2B, EBIT +0.1B (R&D 2.1B - amortization 2.0B)

## Evidence from the latest 10-K (every quote checked against the filing)

## Cost

0 tokens, $0.0000 across 0 model runs.

## Parameters

| Parameter | Value | Source | Verified |
|---|---|---|---|
| risk_free | erp_date | FRED series DGS10 | no |
| equity_risk_premium | 0.0414 | Damodaran, implied ERP update of 2026-09-01 (pages.stern.nyu.edu/~adamodar) | yes |
| erp_date | 2026-09-01 | Damodaran's monthly update | no |
| erp_risk_free | 0.0475 | Damodaran ERP update 2026-09-01 (rf 4.75%) | yes |
| beta_method | bottom_up | Damodaran betas.xls (2026-01-05) and his company-to-industry file indname.xls (2026-01-08); he prefers bottom-up because regression betas carry standard errors near 0.2 | yes |
| beta_bounds | (0.8, 2.0) | Simply Wall St's published bounds (0.8 to 2.0) | no |
| beta_bounds_bottom_up | (0.5, 2.0) | Damodaran applies no bounds to bottom-up betas | no |
| beta_disagreement | 0.3 | own guard; Damodaran notes the industry mix must match the business | no |
| min_terminal_spread | 0.03 | FinRobot enforces WACC - g of at least 1.5 points; a thin Gordon denominator makes value explode (at a 2-point spread each 0.1 point moves value about 5%) | no |
| mature_wacc | True | Damodaran Ginzu (cost of capital moves to rf + mature ERP by year 10) | no |
| marginal_tax | 0.25 | Damodaran uses 25% (betas.xls, Ginzu); Tax Foundation 25.63% (2026-01-05) | yes |
| rating_spreads | damodaran_large | Damodaran, ratings and spreads table for large non-financial firms (market cap of $5bn or more), January 2026 | yes |
| high_growth_years | 5 | Damodaran Ginzu default | no |
| fade_years | 5 | Damodaran Ginzu default | no |
| year5_growth_cap | 0.1 | base rates: Mauboussin and Callahan, The Base Rate Book (2016), sales growth mean-reverts fast and few large companies sustain 20%+ for five years | no |
| growth_bounds | (-0.05, 0.3) | own choice | no |
| red_team_model | google/gemini-3.1-flash-lite | deliberation helps only across different models (Schneider and Schramm 2025); voting explains most debate gains among copies of one model (Choi, Zhu, Li, NeurIPS 2025) | no |
| margin_correction_band | 0.3 | own rule after Visa, 2026-10-01: operating expenses / revenue (32%) was submitted as the operating margin (reported 61%) and cost a notch in one repeat | no |
| forward_drivers | {'guidance_weight': 0.5, 'guidance_cap': 0.05, 'mix_horizon': 5, 'segment_growth_bounds': (-0.1, 0.4), 'mix_ratio_bounds': (0.67, 1.5), 'segment_coverage': (0.7, 1.3), 'margin_years': 5} | anchor and adjust on verified guidance (CAME, Wu et al., EMNLP 2026); Damodaran's Ginzu target operating margin by a convergence year | no |
| growth_blend | {'ttm': 0.5, 'cagr_3y': 0.5} | base rates: one year of growth is noisy and mean-reverts (Mauboussin and Callahan, 2016) | no |
| terminal_growth_cap | 0.0475 | Damodaran Ginzu and Simply Wall St: g = rf; never above it | no |
| terminal_excess_return | moat_from_roic_history | Morningstar ties the fade of excess returns to moat; Damodaran's default is 0 (ROIC = WACC) | no |
| moat_margin | 0.05 | own choice, in the spirit of Morningstar's moat test | no |
| mature_beta | toward_one_from_above | Damodaran moves mature firms toward beta 1; applying that to low-beta staples raises their cost of capital, so only high-beta firms converge here | no |
| capital_for_reinvestment | operating | McKinsey Valuation: ROIC with and without goodwill | no |
| sbc_as_expense | True | Damodaran; McKinsey Valuation | no |
| capitalize_rd | {'min_share_of_revenue': 0.02, 'lives': {'Drug': 10, 'Biotech': 10, 'Software': 3, 'Semiconductor': 5, 'Computer': 5, 'Electronic': 5, 'Internet': 3, 'Entertainment': 3, 'default': 5}} | Damodaran R&D converter (R&DConv.xls): Drug 10 years, software 3, semiconductors and computers 5; industry names mapped by keyword to his current industries | no |
| captive_finance | {'min_share_of_assets': 0.1} | common practice: net debt excluding financial services (industrial companies with captive finance arms) | no |
| leases_as_debt | True | Damodaran; McKinsey | no |
| mid_year | True | McKinsey Valuation | no |
| cash_conversion | ocf_over_nopat | NOPAT excludes non-operating gains that inflate net income (Alphabet's equity stakes) | no |
| bank_model | excess_return | Damodaran, excess return model for financial firms (finfirm09.pdf, eqexret.xls) | no |
| model_routes | {'excess_return': 'banks 6021/6022/6029/6035/6036, broker-dealers 6211, insurers 6311/6321/6331/6351/6361/6399', 'dividend_discount': 'REITs 6798, utilities 4911/4931/4932/4941'} | Damodaran on financial firms and on REITs and regulated utilities (dividend and excess return models) | no |
| financial_ke_floor | industry_implied | found on the 2026-10-01 run by the multiples cross-check; insurers' low market betas understate risk the market prices (catastrophe and reserve risk) | no |
| financial_moat_cap | 0.5 | Damodaran fades financial firms' excess returns toward the cost of equity | no |
| normalized_financial_roe | True | Damodaran: normalize earnings for cyclical firms | no |
| utility_model | {'growth_bounds': (0.0, 0.07), 'signal_range': (-0.05, 0.15), 'max_age_days': 456} | practice: utilities are valued on rate base growth and allowed ROE (NARUC ratemaking; Damodaran's DDM with payout tied to growth and ROE); Duke guides 5 to 7% EPS growth against a 2% dividend trend | no |
| ddm | {'stage1_years': 5, 'growth_bounds': (-0.05, 0.08), 'bear_bull': (0.02, 0.005)} | Damodaran, dividend discount models for REITs and utilities | no |
| sanity | {'fair_to_price': (0.25, 4.0), 'wacc': (0.05, 0.15), 'terminal_share': 0.95} | own choice | no |
| rating_bands | {'Low': (0.8, 1.25), 'Medium': (0.7, 1.35), 'High': (0.6, 1.55), 'Very High': (0.5, 1.75), 'Extreme': (0.25, 4.0)} | Morningstar star rating bands (methodology, Sept 2022) | no |
| multiples_check | {'agree': (0.67, 1.5)} | practice: analysts triangulate DCF with relative value; Damodaran vebitda.xls industry averages | no |
| multiples_check_financials | roe_adjusted_pbv | Damodaran pbvdata.xls industry averages (January 2026); P/B scales with ROE | no |
| uncertainty | {'volatility': (0.2, 0.3, 0.45, 0.6), 'range_overlay': 1.5} | Morningstar starts from return volatility and adds an analyst overlay; the thresholds here are own choice | no |
