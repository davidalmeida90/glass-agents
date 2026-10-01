# PGR: Sell

Desk memo, 2026-10-01. Price 207.31 (2026-09-30). Noise meter agreement 100% (Sell, Sell, Sell). Target weight 0.0%.

## Why

- price / base fair value 1.42 at Medium uncertainty (volatility 27%, range 0.63x base, DCF / industry multiples 1.01): Buy at or below 0.70, Overweight to 0.93, Underweight from 1.07, Sell from 1.35

## Valuation

Method: justified price-to-book on common equity: P/B = (ROE - g) / (cost of equity - g), cost of equity = risk-free + beta x ERP; bear/bull: ROE -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 80.45 | 145.53 | 172.34 | 1.42 |

- Industry check: Insurance (Prop/Cas.) P/B 2.02x at ROE 18.7%, ROE-adjusted 143.82 per share; model / multiples 1.012
- ROE 22.5% (5-year average; latest 34.1%); the price implies 22.7%; book value per share 59.06; cost of equity 9.9%; narrow: ROIC beat WACC on average over 5 years (+12.6%)


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total premiums earned (net) for fiscal 2025 were $81,661 million. (P113: "December 31, 2025 Premiums earned: Property and liability insurance $ 82,847 $ 1,186 $ 0 $ 81,661 0 %")
- Net premiums earned for fiscal 2024 were $70,799 million. (P113: "December 31, 2024 Premiums earned: Property and liability insurance $ 72,169 $ 1,370 $ 0 $ 70,799 0 %")
- Net premiums written for fiscal 2025 were $83,174 million. (P112: "Total $ 2,044 $ 43,310 $ 25,219 $ 0 $ 81,661 $ 3,549 $ 53,959 $ 6,096 $ 12,553 $ 83,174")
- Personal Lines premium revenue for fiscal 2025 was $72,558 million. (P112: "Year ended December 31, 2025: Personal Lines $ 70,778 $ 46,662 $ 5,070 $ 11,252 $ 72,558")
- Commercial Lines premium revenue for fiscal 2025 was $10,613 million. (P112: "Commercial Lines 10,881 7,296 1,026 1,279 10,613")
- Personal Lines accounted for 87% of total net premiums written in 2025. (P004: "The Personal Lines segment accounted for 87% of our total net premiums written in 2025, 85% in 2024, and 84% in 2023.")

**capital**
- Total investments at fair value were $97,373 million at December 31, 2025. (P107: "Total investments $ 93,947 $ 97,373 $ 97,373")
- Short-term investments were $10,005 million at December 31, 2025. (P107: "Short-term investments 10,005 10,005 10,005")
- Parent company debt was $6,897 million at December 31, 2025, consisting solely of long-term debt. (P108: "Debt 1 6,897 6,893")
- Dividends paid to common shareholders by the parent company were $2,871 million in 2025. (P109: "Dividends paid to common shareholders ( 2,871 ) ( 674 ) ( 234 )")
- The parent company paid $92 million in 2025 to acquire treasury shares for restricted stock tax liabilities. (P109: "Acquisition of treasury shares for restricted stock tax liabilities ( 92 ) ( 121 )")
- The parent company paid $74 million in 2025 to acquire treasury shares in the open market. (P110: "Acquisition of treasury shares acquired in open market ( 74 ) ( 13 ) ( 46 )")

**risks**
- Competitors or other third parties may be able to incorporate Advanced AI into their products and operations more quickly or more successfully than the company. (R000: "Furthermore, our competitors or other third parties may be able to replace legacy systems, incorporate Advanced AI into their products and operations, or optimi")
- Consolidations and strategic relationships in the independent agent channel in the Personal Lines business have increased competition and could continue to do so. (R000: "Consolidations and strategic relationships in the independent agent channel in our Personal Lines business have increased competition and could continue to do s")
- Inconsistencies in requirements among the various states, or between state and federal requirements, or changes in regulatory priorities or funding, may further complicate the company's compliance efforts. (R000: "Moreover, inconsistencies in requirements among the various states, or between state and federal requirements, or changes in regulatory priorities or funding, m")
- Regulatory complications could potentially damage the company's reputation or brand, result in additional costs, or impact its ability to participate in certain government funded programs such as the National Flood Insurance Program. (R000: "potentially damage our reputation in the marketplace or our brand, potentially resulting in additional costs for us or impacting our ability to participate in c")

**segments**
- Personal Lines premium revenue was $70,778 million in 2025 versus $60,091 million in 2024. (P112: "Personal Lines $ 70,778 $ 46,662 $ 5,070 $ 11,252 $ 72,558 ... Personal Lines $ 60,091 $ 41,443 $ 4,360 $ 8,341 $ 63,470")
- Commercial Lines premium revenue was $10,881 million in 2025 versus $10,707 million in 2024. (P112: "Commercial Lines 10,881 7,296 1,026 1,279 10,613 ... Commercial Lines 10,707 7,610 1,023 1,109 10,953")
- Other indemnity premium revenue was $2 million in 2025 versus $1 million in 2024. (P112: "Other indemnity 2 1 0 22 3 ... Other indemnity 1 7 0 12 1")

**accounting**
- Parent company net income for 2025 was $11,308 million. (P109: "Net income $ 11,308 $ 8,480 $ 3,903")
- Parent company net cash provided by operating activities for 2025 was $9,843 million. (P109: "Net cash provided by operating activities 9,843 3,519 236")
- No change in internal control over financial reporting during the most recent fiscal quarter materially affected, or is reasonably likely to materially affect, internal control over financial reporting. (P100: "There have not been any changes in our internal control over financial reporting during our most recent fiscal quarter that has materially affected, or is reaso")
- Management's Report on Internal Control over Financial Reporting and the attestation of the independent registered public accounting firm are incorporated by reference from the Annual Report. (P100: "e attestation of the independent registered public accounting firm are incorporated by reference from our Annual Report.")
- The CEO and CFO concluded that disclosure controls and procedures are effectively serving the stated purposes as of the end of the period covered by the report. (P099: "the Chief Executive Officer and Chief Financial Officer concluded that our disclosure controls and procedures are effectively serving the stated purposes as of ")
- There were no changes in or disagreements with accountants on accounting and financial disclosure. (P099: "ITEM 9. CHANGES IN AND DISAGREEMENTS WITH ACCOUNTANTS ON ACCOUNTING AND FINANCIAL DISCLOSURE None.")

## Red team

- [method, medium, rating too low, unsupported] The desk's valuation relies on a cost of equity of 9.87%, which is significantly higher than the CAPM-derived 7.41%. Given the company's low beta of 0.642, the desk's use of a 'financial_ke_floor' to inflate the cost of equity is overly punitive and ignores the company's strong competitive position, leading to an undervalued base fair value. (cites cost_of_equity, cost_of_equity_capm, beta)
- [data_conflict, medium, rating too low, supported] The desk's 'Sell' rating is based on a price-to-fair-value ratio of 1.42. However, the multiples check indicates an industry P/B of 2.02 and a value per share of 143.82, which is close to the base fair value of 145.53. The desk's model may be underestimating the company's ROE potential, which is currently 22.52%, well above the industry average of 18.71%. (cites roe, multiples_check, fair_value)

## Cost

63,534 tokens, $0.0131 across 9 model runs.

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
