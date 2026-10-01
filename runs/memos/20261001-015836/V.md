# V: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Visa's net revenue for fiscal 2025 was $40,000 million. (P131: "Net revenue $ 40,000 $ 35,926 $ 32,653 11 % 10 %")
- Net revenue grew 11% in fiscal 2025 versus fiscal 2024. (P131: "Net revenue $ 40,000 $ 35,926 $ 32,653 11 % 10 %")
- U.S. net revenue was $15,633 million in fiscal 2025, up 6% year over year. (P131: "U.S. $ 15,633 $ 14,780 $ 14,138 6 % 5 %")
- International net revenue was $24,367 million in fiscal 2025, up 15% year over year. (P131: "International 24,367 21,146 18,515 15 % 14 %")
- Service revenue was $17,539 million in fiscal 2025, up 9% year over year. (P131: "Service revenue $ 17,539 $ 16,114 $ 14,826 9 % 9 %")
- Data processing revenue was $19,993 million in fiscal 2025, up 13% year over year. (P131: "Data processing revenue 19,993 17,714 16,007 13 % 11 %")

**capital**
- Cash and cash equivalents were $17,164 million as of September 30, 2025. (P161: "Cash and cash equivalents $ 17,164 $ 11,975")
- Cash and cash equivalents balance was $17.2 billion and available-for-sale debt securities was $2.4 billion as of September 30, 2025. (P138: "As of September 30, 2025, our cash and cash equivalents balance was $17.2 billion and our available-for-sale debt securities was $2.4 billion.")
- Investment securities were $1,833 million current and $999 million non-current as of September 30, 2025. (P161: "Investment securities 1,833 3,200")
- Total debt was $25,392 million as of September 30, 2025, with a total carrying value of $25,171 million. (P215: "Total debt 25,392 21,111")
- Current maturities of debt were $5,569 million and long-term debt was $19,602 million as of September 30, 2025. (P161: "Current maturities of debt 5,569 —")
- The share repurchase program had remaining authorized funds of $24.9 billion. (P142: "hase program had remaining authorized funds of $24.9 billion.")

**risks**
- The adoption of agentic commerce, where autonomous AI agents initiate and execute transactions, presents novel regulatory, privacy and cybersecurity risks. (R003: "the adoption of agentic commerce, in which autonomous AI agents initiate and execute transactions on behalf of users, presents novel and complex regulatory, pri")
- The EU AI Act establishes harmonized rules across Europe, with key provisions for high-risk AI systems taking effect in August 2026. (R004: "the EU has adopted a comprehensive AI Act that establishes harmonized rules across Europe, with key provisions for high-risk AI systems taking effect in August ")
- Visa's own use and deployment of GenAI technologies could expand its cybersecurity attack surface, increasing exposure to breaches, fraud and unauthorized transactions. (R009: "Our own use and deployment of GenAI technologies could expand our cybersecurity attack surface, increasing exposure to breaches, fraud, unauthorized transaction")
- In August 2025 the District Court for the District of North Dakota ruled the Federal Reserve exceeded its authority in implementing Regulation II and vacated its debit interchange fee standard. (R000: "in August 2025, the District Court for the District of North Dakota ruled that the Federal Reserve exceeded its authori ty in implementing Regulation II, which ")
- In July 2025 New Zealand adopted interchange caps on cross-border transactions including commercial credit transactions. (R001: "in July 2025, New Zealand adopted interchange caps on cross-border transactions including commercial credit transactions")
- Geopolitical trends toward nationalism, protectionism and restrictive visa requirements, along with sanctions, tariffs and trade restrictions, could impact expansion and have resulted in Visa suspending operations in some regions. (R007: "Geopolitical trends towards nationalism, protectionism and restrictive visa requirements, as well as continued activity and uncertainty around economic sanction")

**accounting**
- Visa reported net income of $20,058 million for fiscal 2025. (P168: "Net income $ 20,058 $ 19,743 $ 17,273")
- Net cash provided by operating activities was $23,059 million in fiscal 2025. (P168: "Net cash provided by (used in) operating activities 23,059 19,950 20,755")
- Cash provided by operating activities increased in fiscal 2025 over the prior year primarily due to growth in the underlying business and timing of income tax payments. (P138: "Cash provided by operating activities increased in fiscal 2025 over the prior year primarily due to growth in our underlying business and the timing of payments")
- KPMG LLP audited the consolidated financial statements and the effectiveness of internal control over financial reporting and expressed opinions on both. (P156: "Our responsibility is to express an opinion on the Company’s consolidated financial statements and an opinion on the Company’s internal control over financial r")
- The critical audit matter was the assessment of the litigation accrual for class members opting out of the Damages Class settlement in the Interchange Multidistrict Litigation (MDL). (P159: "Assessment of the litigation accrual for class members opting out of the Damages Class settlement in the Interchange Multidistrict Litigation (MDL)")
- The Company recorded a litigation accrual of $2,698 million as of September 30, 2025 related to the MDL Individual Merchant Actions. (P159: "the Company has recorded a litigation accrual of $2,698 million as of September 30, 2025")

## Cost

46,685 tokens, $0.0075 across 6 model runs.

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
