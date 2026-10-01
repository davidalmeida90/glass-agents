# CAT: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x

- Data note: debt from Yahoo totalDebt (45.1B): XBRL tags gave 0.7B
- Data note: captive finance: 25.2B of finance receivables netted against debt
- Data note: R&D capitalized over 5 years: research asset 6.3B, EBIT +0.4B (R&D 2.3B - amortization 1.8B)

## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Consolidated sales and revenues were $64.809 billion in 2025. (P090: "Consolidated Sales and Revenues $ 34,397 $ 6,708 $ 12,316 $ 11,388 $ 64,809 $ — $ 64,809")
- Operating profit margin was 16.5 percent in 2025. (P090: "Operating profit margin was 16.5 percent in 2025, compa")
- Profit of consolidated and affiliated companies was $8.882 billion in 2025. (P161: "es $ 8,882 $ 10,788 $ 10,332")
- Net cash provided by operating activities was $11.739 billion in 2025. (P161: "Net cash provided by (used for) operating activities 11,739 12,035 12,885")
- Total sales and revenues for the second quarter of 2026 were $20.543 billion, an increase of 24 percent versus the second quarter of 2025. (Q092: "Total sales and revenues for the second quarter of 2026 were $20.543 billion, an increase of $3.974 billion, or 24 percent, compared with $16.569 billion in the")
- Operating profit for the six months ended June 30, 2026 was $7.380 billion, an increase of 36 percent versus the six months ended June 30, 2025. (Q106: "Operating profit for the six months ended June 30, 2026, was $7.380 billion, an increase of $1.941 billion, or 36 percent, compared with $5.439 billion for the ")

**capital**
- Cash and cash equivalents at December 31, 2025 were $9,980 million. (P157: "Cash and cash equivalents $ 9,980 $ 6,889")
- The company reported cash and cash equivalents of $9.980 billion and available-for-sale debt securities of $1.230 billion as of December 31, 2025. (P110: "balances of cash and cash equivalents of $9.980 billion and available-for-sale debt securities of $1.230 billion as of December 31, 2025")
- Total short-term borrowings were $5,514 million at December 31, 2025. (P229: "Total short-term borrowings $ 5,514 $ 4,393")
- Long-term debt maturities for 2026 total $7,120 million. (P231: "$ 7,120 $ 8,920 $ 7,747 $ 3,112 $ 1,261")
- Payments to purchase common stock were $5,190 million in 2025. (P162: "Payments to purchase common stock ( 5,190 ) ( 7,697 ) ( 4,975 )")
- Dividends paid were $2,749 million in 2025. (P162: "Dividends paid ( 2,749 ) ( 2,646 ) ( 2,563 )")

**risks**
- The comparison of the Item 1A risk factors in the 10-K for the period ended 2025-12-31 with the 10-K for 2024-12-31 yields no new risk factor sentences. (R000: "No new risk factor sentences.")
- No new or expanded risk factor sentences were identified in this year's Item 1A relative to last year's. (R000: "No new risk factor sentences.")

**accounting**
- Caterpillar's profit (net income) was $8,882 million in 2025. (P161: "es $ 8,882 $ 10,788 $ 10,332 Adjustments to reconcile profit to net cash provided by operating activities:")
- Net cash provided by operating activities was $11,739 million in 2025. (P161: "Net cash provided by (used for) operating activities 11,739 12,035 12,885")
- Machinery, Power & Energy net cash provided by operating activities was $12.278 billion in 2025, compared with $11.437 billion in 2024. (P111: "Net cash provided by operating activities was $12.278 billion in 2025, compared with $11.437 billion in 2024.")
- PricewaterhouseCoopers LLP opined that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations and cash flows in conformity with U.S. GAAP. (P150: "In our opinion, the consolidated financial statements referred to above present fairly, in all material respects, the financial position of the Company as of De")
- The auditor opined that the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P150: "Also in our opinion, the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025, based on cri")
- Management concluded that the company's internal control over financial reporting was effective as of December 31, 2025. (P149: "Based on our assessment we concluded that, as of December 31, 2025, the company’s internal control over financial reporting was effective based on those criteri")

## Cost

64,042 tokens, $0.0102 across 6 model runs.

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
