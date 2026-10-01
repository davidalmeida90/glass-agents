# KO: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Net operating revenues for the six months ended July 3, 2026 were $25,852 million. (Q087: "net operating revenues were $25,852 million, compared to $23,664 million during the six months ended June 27, 2025")
- Net operating revenues increased $2,188 million, or 9%, for the six months ended July 3, 2026 versus the prior-year period. (Q087: "an increase of $2,188 million, or 9%")
- Gross profit margin increased to 61.6% in 2025 from 61.1% in 2024. (P171: "Our gross profit margin increased to 61.6% in 2025 from 61.1% in 2024.")
- Consolidated net income for the year ended December 31, 2025 was $13,137 million. (P213: "Consolidated net income $ 13,137 $ 10,649 $ 10,703")
- Net cash provided by operating activities for the year ended December 31, 2025 was $7,408 million. (P213: "Net Cash Provided by Operating Activities 7,408 6,805 11,599")
- Net cash provided by operating activities for the six months ended July 3, 2026 was $7,543 million. (Q114: "Net cash provided by operating activities during the six months ended July 3, 2026 was $7,543 million")

**capital**
- Cash and cash equivalents were $10,270 million at December 31, 2025. (P212: "Cash and cash equivalents $ 10,270 $ 10,828")
- Total cash, cash equivalents and short-term investments were $13,872 million at December 31, 2025. (P212: "Total Cash, Cash Equivalents and Short-Term Investments 13,872 12,848")
- Cash, cash equivalents, short-term investments and marketable securities totaled $15.8 billion as of December 31, 2025. (P185: "The Company’s cash, cash equivalents, short-term investments and marketable securities totaled $15.8 billion as of December 31, 2025.")
- Long-term debt was $42,119 million at December 31, 2025, with current maturities of long-term debt of $1,822 million and loans and notes payable of $1,551 million. (P212: "Loans and notes payable 1,551 1,499 Current maturities of long-term debt 1,822 648 ... Long-term debt 42,119 42,375")
- The carrying value and fair value of long-term debt, including the current portion, were $43,941 million and $39,385 million as of December 31, 2025. (P342: "As of December 31, 2025, the carrying value and fair value of our long-term debt, including the current portion, were $ 43,941 million and $ 39,385 million, res")
- Purchases of stock for treasury were $746 million in 2025 on the cash flow statement, and $634 million of treasury stock purchases in the equity statement. (P214: "Purchases of stock for treasury ( 746 ) ( 1,795 ) ( 2,289 )")

**risks**
- Recent U.S. federal and state government activities and initiatives have focused on potential drivers behind the rise in childhood chronic diseases, adding to governmental and public pressure on sweetened beverages. (R000: "Recent activities and proposals by U.S. federal and state government agencies and initiatives have focused on potential drivers behind the rise in childhood chr")
- Ongoing public concern about obesity and other health-related concerns surrounding consumption of sweetened beverages are cited as risks that may reduce demand for or increase the cost of the company's sweetened beverages. (R000: "ongoing public concern about obesity; other health-related public concerns surrounding consumption of sweetened beverages")
- The effects or perceived effects of weight-loss drug usage on consumption patterns are cited as a risk to demand for the company's sweetened beverages. (R000: "the effects or perceived effects of the usage of weight-loss drugs on consumption patterns")
- Potential new or increased governmental regulations on particular ingredients or additives in the company's beverages and packaging, or on manufacturing processes, are cited as risks. (R000: "potential new or increased governmental regulations on particular ingredients or additives in our beverages and packaging, or on manufacturing processes")
- The increasing use of data analytics, automation and artificial intelligence across digital platforms is reshaping how consumers discover, evaluate and engage with brands. (R000: "The increasing use of data analytics, automation and artificial intelligence across digital platforms is further reshaping how consumers discover, evaluate and")
- For the year ended December 31, 2025, one bottler accounted for 10% of the company's net operating revenues, reflected in the EMEA and Asia Pacific operating segments. (R001: "For the year ended December 31, 2025, one bottler accounted for 10% of our net operating revenues, which are reflected in our EMEA and Asia Pacific operating se")

**accounting**
- Consolidated net income for 2025 was $13,137 million. (P213: "Consolidated net income $ 13,137 $ 10,649 $ 10,703")
- Net cash provided by operating activities for 2025 was $7,408 million. (P213: "Net Cash Provided by Operating Activities 7,408 6,805 11,599")
- The auditor expressed an unqualified opinion on the consolidated financial statements. (P363: "our report dated February 20, 2026 expressed an unqualified opinion thereon")
- The auditor concluded the Company maintained effective internal control over financial reporting as of December 31, 2025. (P362: "In our opinion, The Coca-Cola Company and subsidiaries (the Company) maintained, in all material respects, effective internal control over financial reporting a")
- A critical audit matter concerned accounting for uncertain tax positions, with gross unrecognized tax benefits of $857 million as of December 31, 2025. (P359: "As of December 31, 2025, the gross amount of unrecognized tax benefits was $857 million.")
- The Company recognizes revenue when performance obligations under the terms of the contracts with customers are satisfied. (P220: "Our Company recognizes revenue when performance obligations under the terms of the contracts with our customers are satisfied.")

## Cost

38,098 tokens, $0.0061 across 6 model runs.

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
