# BAC: Overweight

Desk memo, 2026-10-01. Price 54.43 (2026-09-30). Noise meter agreement 100% (Overweight, Overweight, Overweight). Target weight 3.4%.

## Why

- price / base fair value 0.85 at Medium uncertainty (volatility 22%, range 1.32x base): Buy at or below 0.70, Overweight to 0.93, Underweight from 1.07, Sell from 1.35

## Valuation

Method: justified price-to-book on common equity: P/B = (ROE - g) / (cost of equity - g), cost of equity = risk-free + beta x ERP; bear/bull: ROE -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 43.50 | 64.28 | 128.65 | 0.85 |

- ROE 10.7%; the price implies 8.7%; book value per share 43.06; cost of equity 7.9%; narrow: ROIC beat WACC on average over 5 years (+1.6%)


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Bank of America reported consolidated net income of $30,509 million for 2025. (P323: "Net income $ 30,509 $ 26,973 $ 26,305")
- Net cash provided by operating activities was $12,613 million in 2025. (P323: "Net cash provided by (used in) operating activities 12,613 ( 8,805 ) 44,982")
- Global Wealth & Investment Management total revenue, net of interest expense, was $24,883 million in 2025, up 9% from 2024. (P148: "Total revenue, net of interest expense 24,883 22,929 9")
- Merrill Wealth Management revenue was $20.7 billion, up nine percent. (P151: "Merrill Wealth Management revenue of $20.7 billion increased nine percent")
- Bank of America Private Bank revenue was $4.2 billion, up eight percent. (P151: "Bank of America Private Bank revenue of $4.2 billion increased eight percent")
- All Other recorded a net loss of $310 million in 2025. (P162: "Net loss $ (310) $ (1,655) (81)")

**capital**
- Cash and cash equivalents at December 31, 2025 were $231,845 million, down from $290,114 million at December 31, 2024. (P319: "Cash and cash equivalents 231,845 290,114")
- Total debt securities at December 31, 2025 were $925,635 million, versus $917,284 million at December 31, 2024. (P319: "Total debt securities 925,635 917,284")
- Long-term debt was $317,816 million at December 31, 2025, up $34,537 million from $283,279 million at December 31, 2024. (P125: "Long-term debt 317,816 283,279 34,537 12")
- Short-term borrowings were $48,088 million at December 31, 2025, up $4,697 million from $43,391 million at December 31, 2024. (P125: "Short-term borrowings 48,088 43,391 4,697 11")
- Common stock repurchased in 2025 totaled $21,433 million, compared with $13,104 million in 2024. (P324: "Common stock repurchased ( 21,433 ) ( 13,104 ) ( 4,576 )")
- The Corporation repurchased 451.9 million common shares in 2025 for $21,433 million. (P323: "Common stock repurchased ( 451.9 ) ( 21,433 ) ( 21,433 )")

**risks**
- The interconnectedness and complexity of AI models may complicate oversight and compliance, and reliance on third-party AI models increases risk due to limited visibility into their training data, methodologies and safeguards. (R004: "The interconnectedness and complexity of AI models may complicate oversight and compliance, and reliance on third‑party AI models further increases our risks du")
- Inaccurate AI outputs, unintended or unauthorized exposure of confidential information, biases and possible infringement of intellectual property rights through the use of AI increase this risk. (R004: "Inaccurate AI outputs, unintended or unauthorized exposure of confidential information, biases and possible infringement of intellectual property rights through")
- AI lowers the entry barriers to plan and execute cyberattacks, enables more personalized and harder to detect social engineering, and improves vulnerability discovery, increasing the likelihood and sophistication of cyberattacks. (R002: "AI lowers the entry barriers to plan and execute cyberattacks, enables more personalized and harder to detect social engineering, and improves vulnerability dis")
- Expanded use of AI, including emerging third-party AI services and autonomous AI agents, may result in increased data risk, unpredictable system interactions, inadequate controls or safeguards, AI failure, or unintended operations or consequences. (R001: "Expanded use of AI, including emerging third‑party AI services and autonomous AI agents, may result in increased data risk, unpredictable system interactions, i")
- Advances in quantum computing may introduce cryptography risks that threaten the security of the company's information systems. (R002: "Advances in quantum computing may introduce cryptography risks that threaten the 15 Bank of America security of our i")
- U.S. banking regulators are expected to release proposals in 2026 to revise methodologies for measuring and reporting risk-based capital adequacy, including the calculation of RWA and G-SIB surcharge, and final rules could adversely impact capital requirements. (R005: "U.S. banking regulators are expected to release proposals in 2026 to revise methodologies for measuring and reporting risk-based capital adequacy, including the")

**accounting**
- Bank of America reported consolidated net income of $30,509 million for 2025. (P318: "Net income $ 30,509 $ 26,973 $ 26,305")
- Net cash provided by operating activities was $12,613 million in 2025 on the consolidated statement of cash flows. (P323: "Net cash provided by (used in) operating activities 12,613 ( 8,805 ) 44,982")
- The auditor expressed an opinion that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations and cash flows in conformity with U.S. GAAP. (P311: "In our opinion, the consolidated financial statements referred to above present fairly, in all material respects, the financial position of the Corporation as o")
- The auditor stated that the Corporation maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P311: "Also in our opinion, the Corporation maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")
- Management concluded that the Corporation's internal control over financial reporting was effective as of December 31, 2025. (P310: "management concluded that, as of December 31, 2025, the Corporation’s internal control over financial reporting is effective")
- The critical audit matter communicated related to the Allowance for Loan and Lease Losses - Commercial and Consumer Card Loans. (P314: "Allowance for Loan and Lease Losses - Commercial and Consumer Card Loans")

## Red team

- [method, high, rating too high, supported] The bank_model excess-return formula uses roe 0.1067, but the desk's own implied_roe is 0.0873 — barely above cost_of_equity 0.079. On the implied ROE the excess-return spread is ~0.8pt, not 2.8pt, so base fair value collapses toward book (43.06) and price/BV 1.26 is expensive, not cheap. (cites implied_roe, roe, cost_of_equity, book_value_per_share)
- [method, medium, rating too low, supported] The bear/bull levers move ROE only +/-2 points and cost of equity +/-0.5 points, yet the resulting range (43.5 to 128.65) is 1.32x base, forcing Medium uncertainty. A bank with 22% volatility and this lever sensitivity arguably deserves a wider band, which would lower the Overweight threshold and make the rating too low. (cites fair_value, uncertainty, rating_bands)
- [business, medium, rating too low, supported] Evidence shows GWIM revenue $24,883m up 9%, Merrill $20.7bn up 9%, Private Bank $4.2bn up 8%, and noninterest income up $3.2bn to $53.0bn — fee-based, capital-light growth the ROE-based model treats as generic balance-sheet earnings, understating sustainable profitability. (cites PERF-3, PERF-4, PERF-5, ACC-7)
- [business, medium, rating too high, supported] Operating cash flow of $12,613m is far below net income of $30,509m, and buybacks of $21,433m plus dividends of $9,563m exceed operating cash flow. Capital return is being funded by balance-sheet shrinkage (cash down $58bn), which is not repeatable and weakens the ROE the model capitalizes. (cites PERF-2, ACC-1, CAP-5, CAP-7, CAP-1)

## Cost

61,259 tokens, $0.0096 across 9 model runs.

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
