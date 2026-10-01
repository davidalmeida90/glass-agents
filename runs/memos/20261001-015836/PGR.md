# PGR: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total premiums earned for the year ended December 31, 2025 were $81,661 million. (P113: "December 31, 2025 Premiums earned: Property and liability insurance $ 82,847 $ 1,186 $ 0 $ 81,661")
- Net premiums earned grew from $70,799 million in 2024 to $81,661 million in 2025. (P113: "December 31, 2024 Premiums earned: Property and liability insurance $ 72,169 $ 1,370 $ 0 $ 70,799")
- Personal Lines net premiums written were $72,558 million for the year ended December 31, 2025. (P112: "Year ended December 31, 2025: Personal Lines $ 70,778 $ 46,662 $ 5,070 $ 11,252 $ 72,558")
- Commercial Lines net premiums written were $10,613 million for the year ended December 31, 2025. (P112: "Commercial Lines 10,881 7,296 1,026 1,279 10,613")
- Personal Lines accounted for 87% of total net premiums written in 2025. (P004: "The Personal Lines segment accounted for 87% of our total net premiums written in 2025, 85% in 2024, and 84% in 2023.")
- Net income for the year ended December 31, 2025 was $11,308 million. (P109: "Net income $ 11,308 $ 8,480 $ 3,903")

**capital**
- Total investments at fair value were $97,373 million at December 31, 2025. (P107: "Total investments $ 93,947 $ 97,373 $ 97,373")
- Total fixed maturities at fair value were $82,866 million at December 31, 2025. (P107: "Total fixed maturities 82,704 82,866 82,866")
- Short-term investments were $10,005 million at December 31, 2025. (P107: "Short-term investments 10,005 10,005 10,005")
- Parent company debt was $6,897 million at December 31, 2025, consisting solely of long-term debt. (P108: "Debt 1 6,897 6,893")
- Dividends paid to common shareholders by the parent company were $2,871 million in 2025. (P109: "Dividends paid to common shareholders ( 2,871 ) ( 674 ) ( 234 )")
- The parent company paid $74 million in 2025 to acquire treasury shares in the open market. (P110: "Acquisition of treasury shares acquired in open market ( 74 ) ( 13 ) ( 46 )")

**risks**
- Consolidation and strategic relationships in the independent agent channel in the Personal Lines business have increased competition and could continue to do so. (R000: "Consolidations and strategic relationships in the independent agent channel in our Personal Lines business have increased competition and could continue to do s")
- Competitors or other third parties may be able to incorporate Advanced AI into their products and operations, or optimize or redesign their processes, more quickly or more successfully than the company. (R000: "our competitors or other third parties may be able to replace legacy systems, incorporate Advanced AI into their products and operations, or optimize or redesig")
- Inconsistencies in requirements among the various states, or between state and federal requirements, or changes in regulatory priorities or funding, may further complicate compliance efforts and potentially damage reputation or brand, resulting in additional costs or impacting ability to participate in certain government funded programs such as the National Flood Insurance Program. (R000: "inconsistencies in requirements among the various states, or between state and federal requirements, or changes in regulatory priorities or funding, may further")

**accounting**
- Parent company net income for the year ended December 31, 2025 was $11,308 million. (P109: "Net income $ 11,308 $ 8,480 $ 3,903")
- Parent company net cash provided by operating activities for the year ended December 31, 2025 was $9,843 million. (P109: "Net cash provided by operating activities 9,843 3,519 236")
- Parent company net income for the year ended December 31, 2024 was $8,480 million. (P109: "Net income $ 11,308 $ 8,480 $ 3,903")
- Parent company net cash provided by operating activities for the year ended December 31, 2024 was $3,519 million. (P109: "Net cash provided by operating activities 9,843 3,519 236")
- Management's Report on Internal Control over Financial Reporting and the attestation of the independent registered public accounting firm are incorporated by reference from the Annual Report. (P100: "e attestation of the independent registered public accounting firm are incorporated by reference from our Annual Report.")
- There were no changes in internal control over financial reporting during the most recent fiscal quarter that materially affected, or were reasonably likely to materially affect, internal control over financial reporting. (P100: "There have not been any changes in our internal control over financial reporting during our most recent fiscal quarter that has materially affected, or is reaso")

## Cost

38,534 tokens, $0.0061 across 6 model runs.

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
