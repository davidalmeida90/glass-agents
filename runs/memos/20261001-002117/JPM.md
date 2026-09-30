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
- Total net revenue for fiscal 2025 was $182,447 million. (P137: "Total net revenue 182,447 177,556 3")
- Total net revenue increased 3% in 2025 versus 2024. (P137: "Total net revenue 182,447 177,556 3")
- Net interest income was $95,443 million in 2025. (P137: "Net interest income 95,443 92,583 3")
- Noninterest revenue was $87,004 million in 2025. (P137: "Noninterest revenue $ 87,004 $ 84,973 2%")
- Pre-provision profit was $86,807 million in 2025, with total noninterest expense of $95,640 million. (P130: "Pre-provision profit (a) 86,807 85,759 70,932")
- Net income for 2025 was $57,048 million, down 2% from 2024. (P137: "Net income 57,048 58,471 (2)")

**capital**
- Cash and due from banks and deposits with banks decreased by $125,979 million in 2025. (P159: "Net increase/(decrease) in cash and due from banks and deposits with banks $ (125,979) $ (154,834) $ 56,917")
- Total assets were $4,424,900 million at December 31, 2025, up 11% from $4,002,814 million. (P154: "Total assets $ 4,424,900 $ 4,002,814 11 %")
- Investment securities, net of allowance for credit losses, were $777,332 million at December 31, 2025. (P154: "Investment securities, net of allowance for credit losses 777,332 681,320 14")
- Available-for-sale securities were $507,198 million and held-to-maturity securities were $270,134 million at December 31, 2025. (P154: "Available-for-sale securities 507,198 406,852 25 Held-to-maturity securities 270,134 274,468 (2)")
- Proceeds from long-term borrowings were $120,761 million and payments of long-term borrowings were $108,100 million in 2025. (P412: "Proceeds from long-term borrowings 120,761 109,915 75,417 Payments of long-term borrowings ( 108,100 ) ( 96,605 ) ( 64,880 )")
- The firm repurchased 114,408,296 common shares for an aggregate purchase price of $31,640 million in 2025, at an average price of $276.55 per share. (P108: "Full year 114,408,296 $ 276.55 $ 31,640 $ 33,423")

**risks**
- New risk factor: rapid development and deployment of advanced technologies such as generative and agentic AI presents a range of risks to JPMorganChase's businesses and operations. (R013: "JPMorganChase’s operations, results, and competitive standing could be adversely affected by the development of advanced technologies such as AI.")
- AI system failures, inappropriate use, lack of transparency, or inaccurate or biased output could disrupt operations, cause erroneous transactions, compromise data privacy, infringe intellectual property and harm clients. (R013: "AI system failures, inappropriate use of AI systems, lack of transparency in AI systems, or inaccurate or biased output from AI systems resulting from rapid dep")
- If JPMorganChase does not keep pace with rapidly changing technological advances, including the adoption of generative AI, it risks losing clients and market share to competitors. (R013: "including the adoption of generative AI, it risks losing clients and market share to competitors, which could negatively impact revenues, operating costs and it")
- Advocacy by non-banking competitors for exemptions from regulatory requirements could significantly disadvantage traditional financial institutions. (R013: "advocacy by non-banking competitors for exemptions from regulatory requirements could significantly disadvantage traditional financial institutions.")
- Regulatory uncertainty regarding new technologies, including inconsistent regulatory approaches within and across jurisdictions, could require JPMorganChase to modify or restrict offerings or incur higher compliance costs. (R013: "regulatory uncertainty regarding new technologies, including inconsistent regulatory approaches within and across jurisdictions, could require JPMorganChase to ")
- Technological advances such as AI and quantum computing may enable malicious actors to develop more advanced social engineering attacks, including targeted phishing attacks. (R008: "technological advances such as artificial intelligence (“AI”) and quantum computing that may enable malicious actors to develop more advanced social engineering")

**accounting**
- JPMorgan Chase reported net income of $57,048 million for the year ended December 31, 2025. (P411: "Net income $ 57,048 $ 58,471 $ 49,552")
- Net cash used in operating activities was $147,782 million for the year ended December 31, 2025. (P411: "Net cash (used in)/provided by operating activities ( 147,782 ) ( 42,012 ) 12,974")
- Consolidated operating activities cash flow was $(147,782) million for 2025, versus $(42,012) million in 2024. (P159: "Operating activities $ (147,782) $ (42,012) $ 12,974")
- PricewaterhouseCoopers LLP opined that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations and cash flows in conformity with U.S. GAAP. (P397: "In our opinion, the consolidated financial statements referred to above present fairly, in all material respects, the financial position of the Firm as of Decem")
- The auditor identified the fair value of certain level 3 financial instruments as a critical audit matter. (P404: "The principal considerations for our determination that performing procedures relating to the fair value of certain level 3 financial instruments is a critical ")
- Management concluded that the Firm's internal control over financial reporting was effective as of December 31, 2025, and determined there were no material weaknesses. (P396: "management concluded that as of December 31, 2025, JPMorganChase’s internal control over financial reporting was effective based upon the COSO 2013 framework. A")

## Red team

- [method, high, rating too high, supported] The bank_model excess-return formula uses ROE 16.99% and Ke 7.9%, but the desk's own implied_roe is 12.15% — the ROE the market price already embeds. Valuing off a 4.8-point higher ROE than the price implies inflates base fair value; at implied_roe the base would sit near the current price, not 12% above it. (cites implied_roe, roe, fair_value, bank_model)
- [method, medium, rating too high, supported] The excess-return model fades ROE only to Ke + moat share x (ROE - Ke), so a wide-moat share keeps a permanent positive spread. For a money-center bank whose ROE is cyclical and whose 2025 net income fell 2% (PERF-6), assuming the 16.99% spread persists in perpetuity is the single most aggressive fixed assumption. (cites PERF-6, terminal_excess_return, bank_model, roe)
- [data_conflict, medium, rating too low, supported] The model's cash_conversion is None, yet the 10-K shows operating cash flow of -$147,782m (PERF-8, ACC-2/ACC-3) against $57,048m net income. If the desk treated that as a cash-conversion failure it would penalize the rating; for a bank, deposit and trading flows make OCF meaningless, so the omission is right but the negative figure should not be read as a red flag. (cites PERF-8, ACC-3, cash_conversion, PERF-6)
- [business, medium, rating too low, supported] Evidence the rating ignores: revenue grew 3% to $182.4bn (PERF-1/PERF-2), Markets revenue rose 19% (PERF-9), pre-provision profit was $86.8bn (PERF-5), and the firm bought back $31.6bn of stock at $276.55 (CAP-6) while book value per share is $140.92. Buybacks below intrinsic value compound book value per share, supporting a higher rating than Overweight-to-0.90 implies. (cites PERF-1, PERF-2, PERF-9, PERF-5, CAP-6, book_value_per_share)

## Cost

64,887 tokens, $0.0103 across 9 model runs.

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
