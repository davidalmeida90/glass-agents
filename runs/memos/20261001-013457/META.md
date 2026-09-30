# META: Buy

Desk memo, 2026-10-01. Price 725.18 (2026-09-30). Noise meter agreement 100% (Buy). Target weight 3.0%.

## Why

- price / base fair value 0.55 at High uncertainty (volatility 42%, range 0.92x base, DCF / industry multiples 1.45): Buy at or below 0.60, Overweight to 0.90, Underweight from 1.11, Sell from 1.55

## Valuation

Method: FCFF DCF at company WACC (maturing toward beta 1 from above): trailing revenue growth held 5 years if at most 10%, otherwise decaying to 10% by year 5, then fading to terminal growth = risk-free rate over 5 years; reinvestment = change in revenue / operating sales-to-capital; SBC expensed; R&D capitalized where material; leases as debt; terminal ROIC keeps the moat share (from 5-year ROIC history) of today's excess return; bear/base/bull shift growth -/+4 points, margin -/+10% relative, WACC +/-0.5 points, moat share 0/history/1

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 653.67 | 1,311.72 | 1,865.89 | 0.55 |

| Cost of capital | Value |
|---|---:|
| Risk-free (2026-09-01 (rate in Damodaran's ERP computation)) | 4.8% |
| Beta (Software (Entertainment); regression 1.124) | 1.067 |
| Equity risk premium | 4.1% |
| Cost of equity | 9.2% |
| Synthetic rating (coverage 45.34) | AAA |
| Cost of debt, pre-tax | 5.1% |
| Equity weight | 94.3% |
| **WACC** (maturing to 8.6%) | **8.9%** |

- Revenue growth: last twelve months 27.7%, 3-year CAGR 19.9%, blend 23.8% (used 23.8%); the price implies 3.3%
- Operating margin 52.3% (reported 38.1% + R&D adjustment 14.2%), ROIC 23.4%, sales-to-capital 0.617, SBC 11.0% of revenue
- Moat: wide: ROIC beat WACC by 5%+ in all 5 years (min +9.1%)
- Industry multiples check: Software (Entertainment) EV/EBIT 27.0x gives 905.60 per share; DCF / multiples 1.448
- Terminal value 77.9% of enterprise value; EV/EBIT at base 28.4x vs market 15.8x
- Period: trailing twelve months to 2026-06-30 (revenue growth: twelve months to 2026-06-30 vs to 2025-06-30), from 10-K and 10-Q XBRL; the readers' evidence comes from the latest 10-K only

Base value per share, WACC by terminal growth:

| | g -0.5% | g +0.0% | g +0.5% |
|---|---:|---:|---:|
| wacc -1.0% | 1,272.46 | 1,389.08 | 1,540.04 |
| wacc +0.0% | 1,201.89 | 1,311.72 | 1,453.89 |
| wacc +1.0% | 1,135.84 | 1,239.33 | 1,373.28 |

- Data note: R&D capitalized over 3 years: research asset 113.7B, EBIT +32.4B (R&D 71.6B - amortization 39.2B)

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
| mature_wacc | True | Damodaran Ginzu (cost of capital moves to rf + mature ERP by year 10) | no |
| marginal_tax | 0.25 | Damodaran uses 25% (betas.xls, Ginzu); Tax Foundation 25.63% (2026-01-05) | yes |
| rating_spreads | damodaran_large | Damodaran, ratings and spreads table for large non-financial firms (market cap of $5bn or more), January 2026 | yes |
| high_growth_years | 5 | Damodaran Ginzu default | no |
| fade_years | 5 | Damodaran Ginzu default | no |
| year5_growth_cap | 0.1 | base rates: Mauboussin and Callahan, The Base Rate Book (2016), sales growth mean-reverts fast and few large companies sustain 20%+ for five years | no |
| growth_bounds | (-0.05, 0.3) | own choice | no |
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
| ddm | {'stage1_years': 5, 'growth_bounds': (-0.05, 0.08), 'bear_bull': (0.02, 0.005)} | Damodaran, dividend discount models for REITs and utilities | no |
| sanity | {'fair_to_price': (0.25, 4.0), 'wacc': (0.05, 0.15), 'terminal_share': 0.95} | own choice | no |
| rating_bands | {'Low': (0.8, 1.25), 'Medium': (0.7, 1.35), 'High': (0.6, 1.55), 'Very High': (0.5, 1.75), 'Extreme': (0.25, 4.0)} | Morningstar star rating bands (methodology, Sept 2022) | no |
| multiples_check | {'agree': (0.67, 1.5)} | practice: analysts triangulate DCF with relative value; Damodaran vebitda.xls industry averages | no |
| uncertainty | {'volatility': (0.2, 0.3, 0.45, 0.6), 'range_overlay': 1.5} | Morningstar starts from return volatility and adds an analyst overlay; the thresholds here are own choice | no |
