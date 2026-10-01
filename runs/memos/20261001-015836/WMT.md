# WMT: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Walmart's total revenues for fiscal 2026 were $713,163 million. (P123: "Total revenues 713,163 680,985 648,125")
- Net sales increased 4.7% for fiscal 2026 compared to the previous fiscal year. (P123: "Percentage change from comparable period 4.7 % 5.0 % 6.1 %")
- Walmart's gross profit rate increased 8 basis points for fiscal 2026 compared to the previous fiscal year. (P125: "Our gross profit rate increased 8 and 40 basis points for fiscal 2026 and 2025, respectively")
- Net cash provided by operating activities was $41,565 million for fiscal 2026. (P135: "Net cash provided by operating activities $ 41,565 $ 36,443 $ 35,726")
- Net sales for the six months ended July 31, 2026 increased 6.5% from the comparable period. (Q045: "Percentage change from comparable period 5.9 % 4.8 % 6.5 % 3.7 %")
- Walmart U.S. segment net sales were $482,975 million in fiscal 2026. (P220: "Walmart U.S. Net sales $ 482,975 $ 462,415 $ 441,817")

**capital**
- Cash and cash equivalents were $10.7 billion as of January 31, 2026. (P135: "Cash and cash equivalents were $10.7 billion and $9.0 billion as of January 31, 2026 and 2025, respectively.")
- Cash, cash equivalents and restricted cash at end of year were $11,321 million in fiscal 2026. (P164: "Cash, cash equivalents and restricted cash at end of year $ 11,321 $ 9,536 $ 9,935")
- Total debt was $38,166 million as of January 31, 2026. (P196: "Total debt 38,166 35,999")
- Short-term borrowings were $6.6 billion as of January 31, 2026. (P139: "Short-term borrowings as of January 31, 2026 and 2025 were $6.6 billion and $3.1 billion, respectively, with weighted-average interest rates of 4.0% and 5.3%, r")
- Total outstanding long-term debt increased $2.2 billion, with balances of $38,166 million as of January 31, 2026. (P139: "Balances as of January 31, 2026 $ 3,542 $ 34,624 $ 38,166 Our total outstanding long-term debt increased $2.2 bill")
- The Company repurchased $8,088 million of its common stock in fiscal 2026. (P141: "Total amount paid for share repurchases $ 8,088 $ 4,494 $ 2,779")

**risks**
- Walmart warns that misuse of AI technologies or flawed AI search and discovery results could erode trust and confidence in its business. (R000: "ineffective use or misuse of AI technologies, inaccurate, biased or otherwise flawed 13 AI search and discovery results")
- Walmart states that continued advancements and increased use of AI have intensified existing cybersecurity risks by enabling faster and more automated attack techniques. (R002: "Continued advancements and increased use of AI have intensified existing cybersecurity risks by enabling faster and more automated attack techniques, lowering t")
- Advances in AI are creating novel categories of cyber threats in which attackers use AI systems to autonomously conduct reconnaissance and execute large-scale intrusion or extortion campaigns. (R002: "Advances in AI are also creating novel categories of cyber threats in which attackers use AI systems to autonomously conduct reconnaissance, generate and tailor")
- A growing patchwork of AI laws and targeted privacy and consumer protection statutes may create varying obligations around notice, customer rights and appeals, and data minimization. (R002: "A growing patchwork of AI laws and targeted privacy and consumer protection statutes may also create varying obligations around notice, customer rights and appe")
- Walmart experienced impacts from incremental import tariffs during fiscal 2026 and expects the dynamic tariff environment to continue, including in fiscal 2027. (R003: "We experienced the impacts noted above during fiscal 2026 as a result of incremental import tariffs. We expect the dynamic tariff environment to continue, inclu")
- The entry of new, well-funded competitors or more rapid development of AI capabilities and agentic tools by competitors may increase competitive pressures. (R001: "the entry of new, well-funded competitors, or more rapid development of AI capabilities and agentic tools by these competitors to enhance productivity and the s")

**accounting**
- Consolidated net income for fiscal 2026 was USD 22,270 million. (P159: "Consolidated net income $ 22,270 $ 20,157 $ 16,270")
- Consolidated net income attributable to Walmart for fiscal 2026 was USD 21,893 million. (P160: "Consolidated net income attributable to Walmart 21,893 19,436 15,511")
- Net cash provided by operating activities for fiscal 2026 was USD 41,565 million. (P135: "Net cash provided by operating activities $ 41,565 $ 36,443 $ 35,726")
- Net cash provided by operating activities increased USD 5.1 billion in fiscal 2026 versus the previous fiscal year. (P135: "Net cash provided by operating activities increased $5.1 billion for fiscal 2026 when compared to the previous fiscal year.")
- The auditor expressed an unqualified opinion that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations in conformity with U.S. GAAP. (P153: "Consolidated Financial Statements present fairly, in all material respects, the financial position of the Company at January 31, 2026 and 2025")
- The auditor opined that Walmart maintained, in all material respects, effective internal control over financial reporting as of January 31, 2026, based on the COSO criteria. (P156: "In our opinion, Walmart Inc. (the Company) maintained, in all material respects, effective internal control over financial reporting as of January 31, 2026, bas")

## Cost

39,760 tokens, $0.0064 across 6 model runs.

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
