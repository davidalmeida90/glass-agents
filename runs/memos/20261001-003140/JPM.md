# JPM: Overweight

Desk memo, 2026-10-01. Price 330.83 (2026-09-30). Noise meter agreement 100% (Overweight, Overweight, Overweight). Target weight 3.3%.

## Why

- price / base fair value 0.90 at High uncertainty (volatility 23%, range 1.57x base): Buy at or below 0.60, Overweight to 0.90, Underweight from 1.11, Sell from 1.55

## Valuation

Method: justified price-to-book on common equity: P/B = (ROE - g) / (cost of equity - g), cost of equity = risk-free + beta x ERP; bear/bull: ROE -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 176.19 | 368.87 | 756.96 | 0.90 |

- ROE 17.0%; the price implies 12.2%; book value per share 140.92; cost of equity 7.9%; narrow: ROIC beat WACC on average over 5 years (+7.0%)


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total net revenue for fiscal 2025 was $182,447 million. (P130: "Total net revenue $ 182,447 $ 177,556 (g) $ 158,104")
- Total net revenue rose from $177,556 million in 2024 to $182,447 million in 2025. (P130: "Total net revenue $ 182,447 $ 177,556 (g) $ 158,104")
- Pre-provision profit was $86,807 million in 2025, against total net revenue of $182,447 million and total noninterest expense of $95,640 million. (P130: "Total noninterest expense 95,640 91,797 (g) 87,172 Pre-provision profit (a) 86,807 85,759 70,932")
- Net income for fiscal 2025 was $57,048 million. (P130: "Net income $ 57,048 $ 58,471 $ 49,552")
- Net cash used in operating activities was $147,782 million in 2025. (P411: "Net cash (used in)/provided by operating activities ( 147,782 ) ( 42,012 ) 12,974")
- Net income for the six months ended June 30, 2026 was $37,649 million, versus $29,630 million in the prior-year period. (Q341: "Net income $ 21,155 $ 14,987 $ 37,649 $ 29,630")

**capital**
- Cash and due from banks and deposits with banks decreased by $125,979 million in 2025. (P159: "Net increase/(decrease) in cash and due from banks and deposits with banks $ (125,979) $ (154,834) $ 56,917")
- Total assets were $4,424,900 million at December 31, 2025, up 11% from $4,002,814 million. (P154: "Total assets $ 4,424,900 $ 4,002,814 11 %")
- Investment securities, net of allowance for credit losses, were $777,332 million at December 31, 2025. (P154: "Investment securities, net of allowance for credit losses 777,332 681,320 14")
- Available-for-sale securities were $507,198 million and held-to-maturity securities were $270,134 million at December 31, 2025. (P154: "Available-for-sale securities 507,198 406,852 25 Held-to-maturity securities 270,134 274,468 (2)")
- Proceeds from long-term borrowings were $120,761 million and payments of long-term borrowings were $108,100 million in 2025. (P412: "Proceeds from long-term borrowings 120,761 109,915 75,417 Payments of long-term borrowings ( 108,100 ) ( 96,605 ) ( 64,880 )")
- The Firm repurchased 114.4 million common shares for an aggregate purchase price of $31,640 million in 2025. (P246: "Total number of shares of common stock repurchased 114.4 91.7 69.5 Aggregate purchase price of common stock repurchases (a) $ 31,640 $ 18,841 $ 9,898")

**risks**
- New risk factor states that rapid development and deployment of advanced technologies, including generative and agentic AI systems, present a range of risks to JPMorganChase's businesses and operations. (R013: "The rapid development and deployment of advanced technologies, including generative and agentic AI systems, present a range of risks to JPMorganChase’s business")
- New risk factor warns that AI system failures, inappropriate use, lack of transparency, or inaccurate or biased output could disrupt operations, cause erroneous transactions, compromise data privacy, infringe intellectual property and harm clients. (R013: "AI system failures, inappropriate use of AI systems, lack of transparency in AI systems, or inaccurate or biased output from AI systems resulting from rapid dep")
- New risk factor states that if JPMorganChase does not keep pace with rapidly changing technological advances, including the adoption of generative AI, it risks losing clients and market share to competitors. (R013: "s, including the adoption of generative AI, it risks losing clients and market share to competitors, which could negatively impact revenues, operating costs and")
- New risk factor states that advocacy by non-banking competitors for exemptions from regulatory requirements could significantly disadvantage traditional financial institutions. (R013: "In addition, advocacy by non-banking competitors for exemptions from regulatory requirements could significantly disadvantage traditional financial institutions")
- New risk factor states that regulatory uncertainty regarding new technologies, including inconsistent regulatory approaches within and across jurisdictions, could require JPMorganChase to modify or restrict offerings, incur higher costs or forgo business opportunities. (R013: "Furthermore, regulatory uncertainty regarding new technologies, including inconsistent regulatory approaches within and across jurisdictions, could require JPMo")
- New risk factor states that technological advances such as artificial intelligence and quantum computing may enable malicious actors to develop more advanced social engineering attacks, including targeted phishing attacks. (R008: "technological advances such as artificial intelligence (“AI”) and quantum computing that may enable malicious actors to develop more advanced social engineering")

**accounting**
- JPMorgan Chase reported net income of $57,048 million for the year ended December 31, 2025. (P411: "Net income $ 57,048 $ 58,471 $ 49,552")
- Net cash used in operating activities was $147,782 million for the year ended December 31, 2025. (P411: "Net cash (used in)/provided by operating activities ( 147,782 ) ( 42,012 ) 12,974")
- Consolidated operating activities used $147,782 million of cash in 2025, versus $42,012 million used in 2024. (P159: "Operating activities $ (147,782) $ (42,012) $ 12,974")
- PricewaterhouseCoopers LLP opined that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations and cash flows in conformity with U.S. GAAP. (P397: "In our opinion, the consolidated financial statements referred to above present fairly, in all material respects, the financial position of the Firm as of Decem")
- The auditor opined that the Firm maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P397: "Also in our opinion, the Firm maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")
- Management concluded that internal control over financial reporting was effective as of December 31, 2025 and determined there were no material weaknesses. (P396: "management concluded that as of December 31, 2025, JPMorganChase’s internal control over financial reporting was effective based upon the COSO 2013 framework")

## Red team

- [method, high, rating too high, supported] The bank_model excess-return formula uses ROE fading to Ke + moat share x (ROE - Ke), but the moat share is set from ROIC-WACC history, a non-financial test. For a bank the relevant spread is ROE - Ke, and the desk's own implied_roe of 0.1215 sits barely above cost_of_equity 0.079, so the terminal excess return is thin and the base fair value is inflated by the starting roe of 0.1699. (cites bank_model, implied_roe, roe, cost_of_equity)
- [method, medium, rating too low, supported] The rating bands are applied to a High-uncertainty name whose range is 1.57x base, above the 1.5 overlay threshold, yet the desk keeps High rather than stepping up. A wider band would raise the Overweight ceiling above 0.90, so the same price could still be Overweight rather than drifting toward Underweight. (cites uncertainty, rating_bands)
- [business, medium, rating too high, supported] PERF-5 and ACC-3 show operating cash flow of -$147,782m in 2025 versus -$42,012m in 2024, and PERF-8 shows -$237,044m for the first half of 2026. The cash_conversion parameter is ocf_over_nopat with a caution below 0.8; here it is deeply negative, so the earnings backing the ROE are not converting to cash. (cites PERF-5, ACC-3, PERF-8, cash_conversion)
- [business, medium, rating too low, supported] PERF-6 and PERF-7 show net income of $37,649m for the six months to June 2026 and $21,155m in the June quarter, up from $14,987m. That is a sharp acceleration versus the fiscal 2025 run-rate, so the trailing ROE of 0.1699 and the implied_roe of 0.1215 may understate the earnings power the rating is built on. (cites PERF-6, PERF-7, roe, implied_roe)

## Cost

65,698 tokens, $0.0104 across 9 model runs.

## Parameters

| Parameter | Value | Source | Verified |
|---|---|---|---|
| risk_free | erp_date | FRED series DGS10 | no |
| equity_risk_premium | 0.0414 | Damodaran, implied ERP update of 2026-09-01 (pages.stern.nyu.edu/~adamodar) | yes |
| erp_date | 2026-09-01 | Damodaran's monthly update | no |
| erp_risk_free | 0.0475 | Damodaran ERP update 2026-09-01 (rf 4.75%) | yes |
| beta_method | bottom_up | Damodaran betas.xls (2026-01-05) and his company-to-industry file indname.xls (2026-01-08); he prefers bottom-up because regression betas carry standard errors near 0.2 | yes |
| beta_bounds | (0.8, 2.0) | Simply Wall St's published bounds (0.8 to 2.0) | no |
| mature_wacc | True | Damodaran Ginzu (cost of capital moves to rf + mature ERP by year 10) | no |
| marginal_tax | 0.25 | Damodaran uses 25% (betas.xls, Ginzu); Tax Foundation 25.63% (2026-01-05) | yes |
| rating_spreads | damodaran_large | Damodaran, ratings and spreads table for large non-financial firms (market cap of $5bn or more), January 2026 | yes |
| high_growth_years | 5 | Damodaran Ginzu default | no |
| fade_years | 5 | Damodaran Ginzu default | no |
| year5_growth_cap | 0.1 | base rates: Mauboussin and Callahan, The Base Rate Book (2016), sales growth mean-reverts fast and few large companies sustain 20%+ for five years | no |
| growth_bounds | (-0.05, 0.3) | own choice; one year of history is noisy | no |
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
| sanity | {'fair_to_price': (0.25, 4.0), 'wacc': (0.05, 0.15), 'terminal_share': 0.95} | own choice | no |
| rating_bands | {'Low': (0.8, 1.25), 'Medium': (0.7, 1.35), 'High': (0.6, 1.55), 'Very High': (0.5, 1.75), 'Extreme': (0.25, 4.0)} | Morningstar star rating bands (methodology, Sept 2022) | no |
| uncertainty | {'volatility': (0.2, 0.3, 0.45, 0.6), 'range_overlay': 1.5} | Morningstar starts from return volatility and adds an analyst overlay; the thresholds here are own choice | no |
