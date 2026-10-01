# CB: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Chubb's total net premiums earned were $53,014 million in fiscal 2025. (P480: "Total net premiums earned $ 53,014 $ 49,846 $ 45,712")
- Total net premiums earned rose to $53,014 million in 2025 from $49,846 million in 2024. (P480: "Total net premiums earned $ 53,014 $ 49,846 $ 45,712")
- Net income was $10,622 million for the year ended December 31, 2025. (P277: "Net income $ 10,622 $ 9,640 $ 9,015")
- Net income attributable to Chubb was $10,310 million in 2025, with diluted earnings per share of $25.68. (P275: "Net income attributable to Chubb $ 10,310 $ 9,272 $ 9,028")
- Net cash flows from operating activities were $12,816 million in 2025. (P277: "Net cash flows from operating activities 12,816 16,182 12,632")
- For the six months ended June 30, 2026, net cash provided by operating activities was $7,677 million versus $5,117 million a year earlier. (Q145: "Net cash provided by operating activities $ 7,677 $ 5,117")

**capital**
- Total financial debt was $17,227 million at December 31, 2025. (P221: "Short-term debt $ 1,499 $ 800 Long-term debt 15,728 14,379 Total financial debt 17,227 15,179")
- Short-term debt was $1,499 million and long-term debt was $15,728 million at December 31, 2025. (P221: "Short-term debt $ 1,499 $ 800 Long-term debt 15,728 14,379")
- Total hybrid debt was $422 million at December 31, 2025. (P221: "Trust preferred securities 309 309 Subordinated debt (1) 113 110 Total hybrid debt 422 419")
- The ratio of financial debt to total adjusted capitalization was 18.4% at December 31, 2025. (P222: "Ratio of financial debt and hybrid debt to total adjusted capitalization (2) (3) 18.8 % 18.5 %")
- Total investments other than investments in related parties were $170,225 million at December 31, 2025. (P488: "Total investments - other than investments in related parties $ 170,225 $ 168,265 $ 168,231")
- Shareholders approved an annual dividend of up to $3.88 per share, paid in four quarterly installments of $0.97 per share. (P440: "our shareholders approved an annual dividend for the following year of up to $ 3.88 per share, expected to be paid in four quarterly installments of $ 0.97 per ")

**risks**
- Several nations in Asia are considering legislation or regulatory guidance affecting the company's insurance and reinsurance business. (R001: "Several nations in Asia are also considering legislation or regulatory guidance.")
- Bermuda operations are subject to taxation in Bermuda because of the newly effective Bermuda Corporate Income Tax Act. (R001: "Our Bermuda operations are subject to taxation in Bermuda because of the newly effective Bermuda Corporate Income Tax Act.")
- Capital levels and risk-based capital requirements may increase or decrease depending on factors including the mix of business written, business growth, the value of securities in the investment portfolio, changes in interest rates and foreign currency exchange rates, and changes to regulatory and rating agency models. (R000: "capital levels and risk-based capital requirements may increase or decrease depending on a variety of factors including the mix of business written by our insur")
- Insurance regulators and rating agencies evaluate company capital through financial models that calculate minimum capitalization requirements based on risk-based capital formulas. (R000: "Insurance regulators and rating agencies evaluate company capital through financial models that calculate minimum capitalization requirements based on risk-base")
- Regulatory agencies and self-regulatory organizations have broad rulemaking and enforcement powers, including the power to limit or restrict the business for failure to comply with applicable laws and regulations. (R001: "the power to limit or restrict our business for failure to comply with applicable laws and regulations")

**accounting**
- Net income for 2025 was $10,622 million. (P277: "Net income $ 10,622 $ 9,640 $ 9,015")
- Net cash flows from operating activities for 2025 were $12,816 million. (P277: "Net cash flows from operating activities 12,816 16,182 12,632")
- Operating cash flows were $12.8 billion in 2025, compared to $16.2 billion in 2024. (P219: "Operating cash flows were $12.8 billion in 2025, compared to $16.2 billion in 2024.")
- PwC's opinion states the consolidated financial statements present fairly, in all material respects, the financial position and results of operations and cash flows in conformity with accounting principles generally accepted in the United States of America. (P265: "In our opinion, the consolidated financial statements referred to above present fairly, in all material respects, the financial position of the Company as of De")
- PwC expressed an unqualified opinion that the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P266: "Also in our opinion, the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")
- Management concluded that Chubb's internal control over financial reporting was effective as of December 31, 2025. (P264: "management has concluded that Chubb's internal control over financial reporting was effective as of December 31, 2025")

## Cost

38,630 tokens, $0.0062 across 6 model runs.

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
