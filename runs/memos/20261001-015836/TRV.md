# TRV: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total revenues were $48,828 million in 2025. (P379: "Total revenues $ 48,828 $ 46,423 $ 41,364")
- Total revenues rose from $46,423 million in 2024 to $48,828 million in 2025. (P379: "Total revenues $ 48,828 $ 46,423 $ 41,364")
- Net income was $6,288 million in 2025. (P343: "Net income $ 6,288 $ 4,999 $ 2,991")
- Net cash provided by operating activities was $10,606 million in 2025. (P343: "Net cash provided by operating activities 10,606 9,074 7,711")
- Net cash provided by operating activities was $10.61 billion in 2025 and $9.07 billion in 2024. (P256: "et cash provided by operating activities was $10.61 billion and $9.07 billion in 2025 and 2024, respectively.")
- Business Insurance earned premiums were $22,412 million in 2025. (P379: "Total Business Insurance 22,412 21,345 19,144")

**capital**
- Total investments were $101.18 billion at year-end 2025, with fixed maturities and short-term securities comprising 94% of total investments. (P184: "Total investments of $101.18 billion; fixed maturities and short-term securities comprised 94% of total investments")
- TRV held total cash and short-term invested assets in the United States of $2.41 billion as of December 31, 2025. (P254: "As of December 31, 2025, TRV held total cash and short-term invested assets in the United States aggregating $2.41 billion")
- Total debt was $9.27 billion at December 31, 2025, a debt-to-total capital ratio of 22.0%. (P184: "Total debt of $9.27 billion, resulting in a debt-to-total capital ratio of 22.0%")
- Total debt comprised $300 million short-term and $9,054 million long-term debt at December 31, 2025. (P262: "Short-term $ 300 $ 100 Long-term 9,054 8,004 Net unamortized fair value adjustments and debt issuance costs (87) (71) Total debt 9,267 8,033")
- Common share repurchases totaled $3.03 billion under the Company's share repurchase authorizations in 2025. (P262: "common share repurchases totaling $3.03 billion under the Company’s share repurchase authorizations")
- Total capital returned to shareholders was $4.18 billion, comprising $3.20 billion of share repurchases and $987 million of dividends. (P184: "Total capital returned to shareholders of $4.18 billion, comprising $3.20 billion of share repurchases and $987 million of dividends")

**risks**
- Emerging intellectual property-related rights and issues relating to artificial intelligence are being interpreted by courts and addressed by regulations. (R001: "With respect to artificial intelligence, emerging intellectual property-related rights and issues are being interpreted by courts and addressed by regulations.")
- Legal and regulatory frameworks regarding artificial intelligence are developing and subject to change. (R001: "Regarding artificial intelligence, legal and regulatory frameworks are developing and subject to change.")
- Losses from a cyber event can be magnified where the event impacts shared geographies, platforms, systems or vulnerabilities, or where threat actors expand their use of new and developing technologies including artificial intelligence. (R000: "the potential for losses from a cyber event can be magnified to the extent that the event impacts geographies, platforms, systems or vulnerabilities shared by a")
- Models and technology are used in the claim estimation process, which can present risks of model inaccuracy. (R000: "Additionally, models and technology are used in the claim estimation process, which can present risks of model inaccuracy.")
- Artificial intelligence may become more expensive in the future given the resources necessary to develop that technology. (R000: "Artificial intelligence, in particular, may become more expensive in the future given the resources necessary to develop that technology.")
- The risk of cyber-attacks could be exacerbated by geopolitical tensions, including hostile actions by cyber criminals, nation-states or terrorist organizations, and increased use of artificial intelligence by threat actors. (R000: "The risk of cyber-attacks could be exacerbated by geopolitical tensions, including hostile actions taken by cyber criminals, nation-states or terrorist organiza")

**accounting**
- Net income for 2025 was $6,288 million. (P343: "Net income $ 6,288 $ 4,999 $ 2,991")
- Net cash provided by operating activities was $10,606 million in 2025. (P343: "Net cash provided by operating activities 10,606 9,074 7,711")
- Net cash provided by operating activities was $10.61 billion in 2025 and $9.07 billion in 2024. (P256: "et cash provided by operating activities was $10.61 billion and $9.07 billion in 2025 and 2024, respectively.")
- KPMG expressed an unqualified opinion that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations in conformity with U.S. GAAP. (P335: "In our opinion, the consolidated financial statements present fairly, in all material respects, the financial position of the Company as of December 31, 2025 an")
- The critical audit matter was the evaluation of the estimate of claims and claim adjustment expense reserves. (P337: "Evaluation of the estimate of claims and claim adjustment expense reserves")
- The claims and claim adjustment expense reserves balance at December 31, 2025 was $65.7 billion. (P338: "The Company’s claims and claim adjustment expense reserves balance at December 31, 2025 was $65.7 billion.")

## Cost

37,405 tokens, $0.0060 across 6 model runs.

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
