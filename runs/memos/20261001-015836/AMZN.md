# AMZN: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Consolidated net sales were $716,924 million in 2025. (P074: "Consolidated $ 637,959 $ 716,924")
- Consolidated sales increased 12% in 2025 compared to the prior year. (P074: "Sales increased 12% in 2025, compared to the prior year.")
- North America net sales were $426,305 million in 2025, up 10%. (P074: "North America $ 387,497 $ 426,305")
- AWS net sales were $128,725 million in 2025, up 20%. (P074: "AWS 107,556 128,725")
- International net sales were $161,894 million in 2025, up 13%. (P074: "International 142,906 161,894")
- North America segment operating income was $29,619 million in 2025. (P169: "Operating income $ 14,877 $ 24,967 $ 29,619")

**capital**
- Total cash, cash equivalents, and marketable securities was $123,029 million at December 31, 2025. (P137: "Total cash, cash equivalents, and marketable securities $ 123,029")
- Cash and cash equivalents on the balance sheet was $86,810 million at December 31, 2025. (P100: "Cash and cash equivalents $ 78,779 $ 86,810")
- Marketable securities on the balance sheet was $36,219 million at December 31, 2025. (P100: "Marketable securities 22,423 36,219")
- Long-term debt was $65,648 million at December 31, 2025. (P100: "Long-term debt 52,623 65,648")
- Proceeds from long-term debt were $15,673 million in 2025. (P098: "Proceeds from long-term debt — — 15,673")
- There were no repurchases of common stock in 2023, 2024, or 2025, with $6.1 billion remaining under the repurchase program as of December 31, 2025. (P158: "There were no repurchases of our common stock in 2023, 2024, or 2025. As of December 31, 2025, we have $ 6.1 billion remaining under the repurchase program.")

**risks**
- The filing states that profitability or other intended benefits in newer activities, including development and adoption of automation, artificial intelligence, and machine learning technologies for customer and internal use, may not meet expectations and investments may not be recouped. (R000: "profitability or other intended benefits, if any, in our newer activities (including development and adoption of automation, artificial intelligence, and machin")
- The filing states that the company experiences significant competition in the technology industry, particularly for software engineers, computer scientists, and other technical staff, including for artificial intelligence and machine learning technologies. (R000: "we experience significant competition in the technology industry, particularly for software engineers, computer scientists, and other technical staff (including")

**accounting**
- Net income for fiscal 2025 was USD 77,670 million. (P097: "Net income 30,425 59,248 77,670")
- Net cash provided by operating activities for fiscal 2025 was USD 139,514 million. (P097: "Net cash provided by (used in) operating activities 84,946 115,877 139,514")
- Cash provided by operating activities was USD 139.5 billion in 2025, up from USD 115.9 billion in 2024. (P068: "Cash provided by (used in) operating activities was $115.9 billion and $139.5 billion in 2024 and 2025.")
- Ernst & Young LLP expressed an unqualified opinion that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations in conformity with U.S. GAAP. (P093: "In our opinion, the consolidated financial statements present fairly, in all material respects, the financial position of the Company at December 31, 2025 and 2")
- Management concluded that internal control over financial reporting was effective as of December 31, 2025. (P175: "management concluded that, as of December 31, 2025, our internal control over financial reporting was effective in providing reasonable assurance regarding the ")
- Ernst & Young LLP opined that Amazon maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P176: "In our opinion, Amazon.com, Inc. (the Company) maintained, in all material respects, effective internal control over financial reporting as")

## Cost

38,041 tokens, $0.0061 across 6 model runs.

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
