# MET: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- MetLife's net cash provided by operating activities was $17,092 million for the year ended December 31, 2025. (P324: "Net cash provided by (used in) operating activities 17,092 14,598 13,721")
- MetLife's net income was $3,403 million for the year ended December 31, 2025. (P324: "Net income (loss) $ 3,403 $ 4,444 $ 1,602")
- Consolidated net income available to MetLife, Inc.'s common shareholders was $3,173 million for the year ended December 31, 2025. (P293: "Consolidated net income (loss) available to MetLife, Inc.’s common shareholders $ 3,173 $ 4,226")
- MetLife, Inc. (parent company only) net cash provided by operating activities was $2,840 million for the year ended December 31, 2025. (P292: "MetLife, Inc. (parent company only) net cash provided by operating activities $ 2,840 $ 4,735")
- Total other revenues were $2,827 million for the year ended December 31, 2025. (P652: "Total other revenues $ 2,827 $ 2,601 $ 2,526")
- Total revenues related to service contracts from customers were $2,436 million for the year ended December 31, 2025. (P652: "Total revenues related to service contracts from customers 2,436 2,245 2,229")

**capital**
- Total short-term debt outstanding at December 31, 2025 was $355 million. (P268: "Short-term debt (1) $ 355 $ 465")
- Total long-term debt outstanding at December 31, 2025 was $14,467 million. (P268: "Long-term debt (2) $ 14,467 $ 15,086")
- Subordinated debt securities outstanding at December 31, 2025 were $4,155 million. (P268: "Subordinated debt securities $ 4,155 $ 3,164")
- Collateral financing arrangement outstanding at December 31, 2025 was $352 million. (P268: "Collateral financing arrangement $ 352 $ 476")
- MetLife repurchased 35,295,854 shares of its common stock for $2.9 billion in 2025, excluding applicable excise tax. (P623: "MetLife, Inc. repurchased 35,295,854 shares, 43,955,023 shares and 50,269,483 shares of its common stock, respectively, through open market purchases for $ 2.9 ")
- MetLife paid dividends on its common stock of $1.5 billion in 2025. (P623: "MetLife, Inc. paid dividends on its common stock of $ 1.5 billion, $ 1.5 billion a")

**risks**
- Competitive pressures include technology and AI as factors that may adversely affect product persistency and future sales. (R001: "Competitive pressures, based on a number of factors including service, product features, scale, price, commission structure, financial strength, investment perf")
- Competition may result in fee compression or a shift toward lower-fee passive products, reducing profit margins of the institutional asset management business. (R001: "Competition may also result in fee compression or a shift toward lower-fee passive products, which could reduce the profit margins of our institutional asset ma")
- Failure to adopt new technologies as effectively or efficiently as others may lead to competitive harm, or failure to adjust investments may result in stranded assets. (R001: "We may fail to adopt new technologies as effectively or efficiently as others, leading to competitive harm, or we may fail to adjust our investments accordingly")
- The personnel and financial resources committed to maintaining and upgrading information systems may be insufficient to address all potential issues. (R002: "The personnel and financial resources we commit to maintaining and upgrading our information systems may not be sufficient to address all potential issues.")
- Costs associated with legacy systems or efforts to address system degradation, including developing or onboarding new systems, may increase over time and adversely affect business results and operations. (R002: "For instance, costs associated with the use of legacy systems or efforts to address system degradation, including the development or onboarding of new systems, ")
- Inability to attract or retain personnel with the appropriate skillset to maintain legacy systems, and third-party providers decreasing or sunsetting support for legacy applications, may impair the ability to identify, prevent, patch or respond to vulnerabilities. (R002: "Moreover, we may be unable to attract or retain personnel with the appropriate skillset to maintain such legacy systems, and/or third-party providers may decrea")

**accounting**
- Consolidated net income (loss) for fiscal 2025 was USD 3,403 million. (P324: "Net income (loss) $ 3,403 $ 4,444 $ 1,602")
- Net cash provided by operating activities for fiscal 2025 was USD 17,092 million. (P324: "Net cash provided by (used in) operating activities 17,092 14,598 13,721")
- Consolidated net income available to MetLife, Inc.'s common shareholders for fiscal 2025 was USD 3,173 million. (P293: "Consolidated net income (loss) available to MetLife, Inc.’s common shareholders $ 3,173 $ 4,226")
- MetLife, Inc. (parent company only) net cash provided by operating activities for fiscal 2025 was USD 2,840 million. (P293: "MetLife, Inc. (parent company only) net cash provided by operating activities $ 2,840 $ 4,735")
- Deloitte expressed an unqualified opinion that the financial statements present fairly, in all material respects, the financial position and results of operations and cash flows in conformity with U.S. GAAP. (P314: "in all material respects, the financial position of the Company as of December 31, 2025 and 2024, and the results of its operations and its cash flows for each ")
- The critical audit matter was the valuation of market risk benefits, specifically certain assumptions related to certain guaranteed minimum benefits associated with variable annuity contracts. (P316: "We have identified certain assumptions related to the valuation of market risk benefits, more specifically certain guaranteed minimum benefits associated with v")

## Cost

51,957 tokens, $0.0084 across 6 model runs.

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
