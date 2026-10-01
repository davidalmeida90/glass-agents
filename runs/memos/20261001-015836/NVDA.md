# NVDA: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x

- Data note: R&D capitalized over 5 years: research asset 43.1B, EBIT +16.0B (R&D 23.6B - amortization 7.6B)

## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total revenue for fiscal year 2026 was $215,938 million. (P134: "Total $ 215,938 $ 130,497 $ 85,441 65 %")
- Total revenue grew 65% in fiscal year 2026 versus fiscal year 2025. (P134: "Total $ 215,938 $ 130,497 $ 85,441 65 %")
- Gross margin was 71.1% of revenue in fiscal year 2026. (P134: "Gross profit 71.1 75.0")
- Operating income was 60.4% of revenue in fiscal year 2026. (P134: "Operating income 60.4 62.4")
- Net income was 55.6% of revenue in fiscal year 2026. (P134: "Net income 55.6 % 55.8 %")
- Net cash provided by operating activities was $102,718 million for the year ended January 25, 2026. (P140: "Net cash provided by operating activities $ 102,718 $ 64,089")

**capital**
- Cash, cash equivalents, and marketable securities totaled $62,556 million as of January 25, 2026. (P140: "Cash, cash equivalents, and marketable securities $ 62,556 $ 43,210")
- Cash and cash equivalents were $10,605 million as of January 25, 2026. (P140: "Cash and cash equivalents $ 10,605 $ 8,589")
- Marketable securities were $51,951 million as of January 25, 2026. (P140: "Marketable securities 51,951 34,621")
- Net carrying amount of debt was $8,468 million as of January 25, 2026, with $999 million short-term and $7,469 million long-term. (P143: "Net carrying amount $ 8,468 Less short-term portion 999 Total long-term portion $ 7,469")
- In fiscal year 2026, the company repurchased 282 million shares of common stock for $40.4 billion. (P120: "In fiscal year 2026, we repurchased 282 million shares of our common stock for $40.4 billion.")
- In fiscal year 2026, the company paid cash dividends to shareholders of $974 million. (P120: "In fiscal year 2026, we paid cash dividends to our shareholders of $974 million.")

**risks**
- China's antitrust regulators published a preliminary finding that NVIDIA's compliance with U.S. export controls discriminated unfairly against customers in the China market and violated the terms of China's approval of the Mellanox acquisition. (R003: "On September 15, 2025, China’s antitrust regulators published their preliminary finding that our compliance with applicable U.S. export controls, which required")
- The USG informed NVIDIA in April 2025 that a license is required for export to China (including Hong Kong and Macau) and D:5 countries of H20 integrated circuits and any other circuits achieving the H20's memory bandwidth, interconnect bandwidth, or combination thereof. (R003: "In April 2025, the USG informed us that it requires a license for export to China (including Hong Kong and Macau) and D:5 countries, or to companies headquarter")
- NVIDIA incurred a $4.5 billion charge in the first quarter of fiscal year 2026 associated with H20 for excess inventory and purchase obligations. (R003: "As a result of these requirements, we incurred a $4.5 billion charge in the first quarter of fiscal year 2026 associated with H20 for excess inventory and purch")
- In August 2025 the USG granted licenses allowing NVIDIA to ship certain H20 products to certain China-based customers, under which NVIDIA generated approximately $60 million in H20 revenue. (R004: "In August 2025, theUSG granted licenses that would allow us to ship certain H20 products to certain China-based customers. We generated approximately $60 millio")
- In February 2026 the USG granted a license allowing NVIDIA to ship small amounts of H200 products to specific China-based customers, with any H200 shipped under the program subject to a 25% tariff upon importation into the United States. (R004: "In February 2026, the USG granted a license that would allow us to ship small amounts of H200 products to specific China-based customers. ... As a result, any H")
- As of the end of fiscal year 2026, NVIDIA was effectively foreclosed from competing in China's data center computing/compute market, which helped its competitors build larger developer and customer ecosystems to challenge it worldwide. (R005: "As of the end of fiscal year 2026, we were effectively foreclosed from competing in China's data center computing/compute market, and our effective foreclosure ")

**accounting**
- Net income for fiscal 2026 was $120,067 million. (P164: "Net income — — — — 120,067 120,067")
- Net cash provided by operating activities for fiscal 2026 was $102,718 million. (P140: "Net cash provided by operating activities $ 102,718 $ 64,089")
- The auditor's opinion states the consolidated financial statements present fairly, in all material respects, the financial position and results of operations in conformity with U.S. GAAP. (P156: "of its operations and its cash flows for each of the three years in the period ended January 25, 2026 in conformity with accounting principles generally accepte")
- The critical audit matter was the valuation of inventories, including provisions for excess or obsolete inventories and excess product purchase commitments. (P159: "Valuation of Inventories - Provisions for Excess or Obsolete Inventories and Excess Product Purchase Commitments")
- The auditor opined that the Company maintained, in all material respects, effective internal control over financial reporting as of January 25, 2026. (P156: "Also in our opinion, the Company maintained, in all material respects, effective internal control over financial reporting as of January 25, 2026, based on crit")
- Management concluded that its internal control over financial reporting was effective as of January 25, 2026. (P149: "our management concluded that our internal control over financial reporting was effective as of January 25, 2026")

## Cost

40,978 tokens, $0.0066 across 6 model runs.

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
