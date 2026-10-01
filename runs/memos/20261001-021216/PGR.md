# PGR: Hold

Desk memo, 2026-10-01. Price 210.52 (2026-09-29). Noise meter agreement 100% (Hold, Hold, Hold). Target weight 0.0%.

## Why

- price / base fair value 0.93 at High uncertainty (volatility 27%, range 0.89x base, DCF / industry multiples 1.57): Buy at or below 0.60, Overweight to 0.90, Underweight from 1.11, Sell from 1.55

## Valuation

Method: justified price-to-book on common equity: P/B = (ROE - g) / (cost of equity - g), cost of equity = risk-free + beta x ERP; bear/bull: ROE -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 87.58 | 225.17 | 287.65 | 0.93 |

- Industry check: Insurance (Prop/Cas.) P/B 2.02x at ROE 18.7%, ROE-adjusted 143.82 per share; model / multiples 1.566
- ROE 22.5% (5-year average; latest 34.1%); the price implies 15.1%; book value per share 59.06; cost of equity 7.4%; narrow: ROIC beat WACC on average over 5 years (+15.1%)


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total underwriting revenue for the six months ended June 30, 2026 was $43,143 million. (Q038: "Total underwriting revenue 37,828 5,312 3 43,143")
- Total underwriting revenue for the six months ended June 30, 2025 was $40,309 million. (Q038: "Total underwriting revenue 34,766 5,542 1 40,309")
- Net premiums written for total underwriting operations grew 6% for the six months ended June 30, 2026 versus the prior-year period. (Q076: "Total Personal Lines 18,609 17,713 5 38,214 35,986 6")
- Companywide pretax underwriting profit was $5,582 million for the six months ended June 30, 2026. (Q038: "Pretax underwriting profit (loss) $ 4,921 $ 681 $ ( 20 ) 5,582")
- Net income for the six months ended June 30, 2026 was $6,129 million. (Q005: "Net income 3,311 3,175 6,129 5,742")
- Net income for the year ended December 31, 2025 was $11,308 million. (P109: "Net income $ 11,308 $ 8,480 $ 3,903")

**capital**
- Total investments at fair value were $97,373 million at December 31, 2025. (P107: "Total investments $ 93,947 $ 97,373 $ 97,373")
- Short-term investments were $10,005 million at December 31, 2025. (P107: "Short-term investments 10,005 10,005 10,005")
- Parent company debt was $6,897 million at December 31, 2025, consisting solely of long-term debt. (P108: "Debt 1 6,897 6,893")
- Dividends paid to common shareholders by the parent company were $2,871 million in 2025. (P109: "Dividends paid to common shareholders ( 2,871 ) ( 674 ) ( 234 )")
- The parent company paid $92 million in 2025 to acquire treasury shares for restricted stock tax liabilities. (P109: "Acquisition of treasury shares for restricted stock tax liabilities ( 92 ) ( 121 )")
- The parent company paid $74 million in 2025 to acquire treasury shares in the open market. (P110: "Acquisition of treasury shares acquired in open market ( 74 ) ( 13 ) ( 46 )")

**risks**
- Consolidations and strategic relationships in the independent agent channel in the Personal Lines business have increased competition and could continue to do so. (R000: "Consolidations and strategic relationships in the independent agent channel in our Personal Lines business have increased competition and could continue to do s")
- Competitors or other third parties may be able to replace legacy systems, incorporate Advanced AI into their products and operations, or optimize or redesign their processes more quickly, or more successfully, than the company. (R000: "our competitors or other third parties may be able to replace legacy systems, incorporate Advanced AI into their products and operations, or optimize or redesig")
- Inconsistencies in requirements among the various states, or between state and federal requirements, or changes in regulatory priorities or funding, may further complicate compliance efforts and potentially damage reputation or brand, resulting in additional costs or impacting ability to participate in certain government funded programs such as the National Flood Insurance Program. (R000: "inconsistencies in requirements among the various states, or between state and federal requirements, or changes in regulatory priorities or funding, may further")

**accounting**
- Parent company net income for 2025 was $11,308 million. (P109: "Net income $ 11,308 $ 8,480 $ 3,903")
- Parent company net cash provided by operating activities for 2025 was $9,843 million. (P109: "Net cash provided by operating activities 9,843 3,519 236")
- Parent company net income for 2024 was $8,480 million. (P108: "Net income 11,308 8,480 3,903")
- There were no changes in internal control over financial reporting during the most recent fiscal quarter that materially affected, or were reasonably likely to materially affect, internal control over financial reporting. (P100: "There have not been any changes in our internal control over financial reporting during our most recent fiscal quarter that has materially affected, or is reaso")
- Management's Report on Internal Control over Financial Reporting and the attestation of the independent registered public accounting firm are incorporated by reference from the Annual Report. (P100: "e attestation of the independent registered public accounting firm are incorporated by reference from our Annual Report.")
- The Report of Independent Registered Public Accounting Firm (PCAOB ID: 238) is included in Item 8. (P106: "Report of Independent Registered Public Accounting Firm (PCAOB ID: 238 )")

## Red team

- [method, high, rating too high, supported] The model normalizes ROE to a 5-year average and caps the terminal excess return at half the spread, but the desk's own roe of 0.2252 sits far above implied_roe 0.151 and the industry's 0.1871. If the hard-market ROE is truly cyclical, base fair value 225.17 is inflated and Hold is too generous. (cites roe, implied_roe, normalized_financial_roe, financial_moat_cap)
- [method, high, rating too low, supported] The excess-return model fades ROE to Ke plus only half the spread, yet PERF-4 shows $5,582m of underwriting profit in six months and PERF-5 $6,129m net income — a run-rate far above the normalized base. If that profitability persists, fair value is understated and the rating should be higher. (cites PERF-4, PERF-5, financial_moat_cap, normalized_financial_roe)
- [data_conflict, medium, rating too low, supported] PERF-3 shows net premiums written grew 6% in the latest six months, while the model's starting growth blend leans on a 3-year fiscal CAGR that includes slower years. The growth input may understate current momentum, depressing fair value and biasing the rating low. (cites PERF-3, growth_blend, growth_used)
- [business, medium, rating too high, supported] RISK-1 and RISK-2 flag rising independent-agent competition and AI-driven disruption to legacy underwriting. The model's moat_from_roic_history and financial_moat_cap assume past ROE spreads persist; if competition compresses underwriting margins, base fair value 225.17 is too high. (cites RISK-1, RISK-2, terminal_excess_return, financial_moat_cap)

## Cost

57,599 tokens, $0.0090 across 9 model runs.

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
| financial_moat_cap | 0.5 | Damodaran fades financial firms' excess returns toward the cost of equity | no |
| normalized_financial_roe | True | Damodaran: normalize earnings for cyclical firms | no |
| ddm | {'stage1_years': 5, 'growth_bounds': (-0.05, 0.08), 'bear_bull': (0.02, 0.005)} | Damodaran, dividend discount models for REITs and utilities | no |
| sanity | {'fair_to_price': (0.25, 4.0), 'wacc': (0.05, 0.15), 'terminal_share': 0.95} | own choice | no |
| rating_bands | {'Low': (0.8, 1.25), 'Medium': (0.7, 1.35), 'High': (0.6, 1.55), 'Very High': (0.5, 1.75), 'Extreme': (0.25, 4.0)} | Morningstar star rating bands (methodology, Sept 2022) | no |
| multiples_check | {'agree': (0.67, 1.5)} | practice: analysts triangulate DCF with relative value; Damodaran vebitda.xls industry averages | no |
| multiples_check_financials | roe_adjusted_pbv | Damodaran pbvdata.xls industry averages (January 2026); P/B scales with ROE | no |
| uncertainty | {'volatility': (0.2, 0.3, 0.45, 0.6), 'range_overlay': 1.5} | Morningstar starts from return volatility and adds an analyst overlay; the thresholds here are own choice | no |
