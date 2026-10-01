# TRV: Hold

Desk memo, 2026-10-01. Price 363.21 (2026-09-29). Noise meter agreement 100% (Hold, Hold, Hold). Target weight 0.0%.

## Why

- price / base fair value 0.96 at Medium uncertainty (volatility 21%, range 0.84x base, DCF / industry multiples 1.49): Buy at or below 0.70, Overweight to 0.93, Underweight from 1.07, Sell from 1.35

## Valuation

Method: justified price-to-book on common equity: P/B = (ROE - g) / (cost of equity - g), cost of equity = risk-free + beta x ERP; bear/bull: ROE -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 188.98 | 379.41 | 506.56 | 0.96 |

- Industry check: Insurance (Prop/Cas.) P/B 2.02x at ROE 18.7%, ROE-adjusted 255.39 per share; model / multiples 1.486
- ROE 14.9% (5-year average; latest 24.9%); the price implies 11.3%; book value per share 158.80; cost of equity 7.4%; narrow: ROIC beat WACC on average over 5 years (+7.5%)


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total revenues were $48,828 million in 2025. (P379: "Total revenues $ 48,828 $ 46,423 $ 41,364")
- Total revenues rose to $48,828 million in 2025 from $46,423 million in 2024. (P379: "Total revenues $ 48,828 $ 46,423 $ 41,364")
- Net income was $6,288 million in 2025. (P343: "Net income $ 6,288 $ 4,999 $ 2,991")
- Net cash provided by operating activities was $10,606 million in 2025. (P343: "Net cash provided by operating activities 10,606 9,074 7,711")
- Net cash provided by operating activities was $10.61 billion in 2025 and $9.07 billion in 2024. (P256: "et cash provided by operating activities was $10.61 billion and $9.07 billion in 2025 and 2024, respectively.")
- Business Insurance earned premiums were $22,412 million in 2025. (P379: "Total Business Insurance 22,412 21,345 19,144")

**capital**
- Total debt was $9,267 million at December 31, 2025, up from $8,033 million at December 31, 2024. (P262: "Total debt 9,267 8,033")
- Short-term debt was $300 million and long-term debt was $9,054 million at December 31, 2025. (P262: "Short-term $ 300 $ 100 Long-term 9,054 8,004")
- The company repurchased 10.9 million shares in 2025 for a total of $3.03 billion, at an average cost of $277.17 per share. (P261: "repurchased 10.9 million shares under its share repurchase authorizations, for a total of $3.03 billion. The average cost per share repurchased was $277.17.")
- As of December 31, 2025, $2.02 billion of capacity remained under share repurchase authorizations. (P261: "As of December 31, 2025, the Company had $2.02 billion of capacity remaining under its share repurchase authorizations.")
- Shareholder dividends of $987 million were paid in 2025. (P262: "shareholder dividends of $987 million")
- Treasury stock was 575.9 million shares at December 31, 2025 versus 564.3 million shares at December 31, 2024. (P527: "Treasury stock, at cost ( 575.9 and 564.3 shares) ( 45,447 ) ( 42,251 )")

**risks**
- The potential for losses from a cyber event can be magnified if threat actors continue to expand their use of new and developing technologies, including artificial intelligence. (R000: "in the event threat actors continue to expand their use of new and developing technologies, including artificial intelligence")
- Models and technology used in the claim estimation process can present risks of model inaccuracy. (R000: "Additionally, models and technology are used in the claim estimation process, which can present risks of model inaccuracy.")
- Artificial intelligence may become more expensive in the future given the resources necessary to develop that technology. (R000: "Artificial intelligence, in particular, may become more expensive in the future given the resources necessary to develop that technology.")
- The risk of cyber-attacks could be exacerbated by geopolitical tensions, including hostile actions by cyber criminals, nation-states or terrorist organizations, and the increased use of artificial intelligence by threat actors. (R000: "The risk of cyber-attacks could be exacerbated by geopolitical tensions, including hostile actions taken by cyber criminals, nation-states or terrorist organiza")
- With respect to artificial intelligence, emerging intellectual property-related rights and issues are being interpreted by courts and addressed by regulations. (R001: "With respect to artificial intelligence, emerging intellectual property-related rights and issues are being interpreted by courts and addressed by regulations.")
- Regarding artificial intelligence, legal and regulatory frameworks are developing and subject to change. (R001: "Regarding artificial intelligence, legal and regulatory frameworks are developing and subject to change.")

**accounting**
- Net income for 2025 was $6,288 million. (P343: "Net income $ 6,288 $ 4,999 $ 2,991")
- Net cash provided by operating activities for 2025 was $10,606 million. (P343: "Net cash provided by operating activities 10,606 9,074 7,711")
- Net cash provided by operating activities was $10.61 billion in 2025. (P256: "et cash provided by operating activities was $10.61 billion and $9.07 billion in 2025 and 2024, respectively.")
- KPMG expressed an unqualified opinion on the consolidated financial statements, dated February 12, 2026. (P336: "our report dated February 12, 2026 expressed an unqualified opinion on the effectiveness of the Company’s internal control over financial reporting.")
- The critical audit matter was the evaluation of the estimate of claims and claim adjustment expense reserves. (P337: "Critical Audit Matter The critical audit matter communicated below is a matter arising from the current period audit")
- Management concluded the Company's internal control over financial reporting was effective at December 31, 2025, with no material weaknesses. (P502: "management has concluded that the Company’s internal control over financial reporting was effective at December 31, 2025, and that there were no material weakne")

## Red team

- [method, medium, rating too high, supported] The excess-return model starts from a 5-year average ROE (normalized_financial_roe) and caps terminal excess returns at half the spread (financial_moat_cap), yet the desk's roe of 0.1487 sits above implied_roe 0.1127 and the industry's 0.1871. If the normalized ROE is materially below 0.1487, base fair value falls and Hold becomes Underweight. (cites roe, implied_roe, normalized_financial_roe, financial_moat_cap)
- [business, medium, rating too low, supported] Personal Insurance revenue fell to $8,698m in H1 2026 from $9,021m a year earlier (PERF-9), while operating cash flow rose to $4.11bn from $3.69bn (PERF-10). The model's growth blend uses only TTM revenue and 3-year CAGR, so a shrinking top line with improving cash generation is not captured; the rating may be too low. (cites PERF-9, PERF-10, growth_blend)
- [data_conflict, low, rating too low, supported] The desk's cost_of_equity of 0.0741 uses a bottom-up beta of 0.642, but the regression beta is 0.8 (raw 0.428) and the industry average is 0.1871 ROE. A higher beta would raise the discount rate and lower fair value, so the low cost of equity is the aggressive input, not a conservative one. (cites cost_of_equity, beta_method, beta_disagreement)
- [method, low, rating too high, supported] The multiples check uses roe_adjusted_pbv with industry P/B 2.02 and industry ROE 0.1871, giving $255.39 per share versus price $363.21 — a DCF/multiples ratio of 1.486, near the 1.5 edge of the agreement band. A small change in the industry ROE or P/B pushes the second method out of agreement and raises uncertainty. (cites multiples_check, multiples_check_financials, price)

## Cost

56,744 tokens, $0.0090 across 9 model runs.

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
