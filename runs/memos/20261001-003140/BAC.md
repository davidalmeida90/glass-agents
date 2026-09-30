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
- Total revenue, net of interest expense, for the total corporation was $31,721 million for the three months ended June 30, 2026. (Q272: "Total revenue, net of interest expense 31,721 27,588 11,336 10,813 6,871 5,937")
- Total revenue, net of interest expense, rose to $31,721 million from $27,588 million in the prior-year quarter. (Q272: "Total revenue, net of interest expense 31,721 27,588")
- Total corporation net income was $9,074 million for the three months ended June 30, 2026, up from $7,170 million. (Q272: "Net income $ 9,074 $ 7,170 $ 3,281 $ 2,973 $ 1,413 $ 993")
- Net income for fiscal 2025 was $30,509 million, compared with $26,973 million in 2024. (P323: "Net income $ 30,509 $ 26,973 $ 26,305")
- Net cash provided by operating activities was $12,613 million in 2025, compared with net cash used of $8,805 million in 2024. (P323: "Net cash provided by (used in) operating activities 12,613 ( 8,805 ) 44,982")
- Net cash provided by operating activities was $70,813 million for the six months ended June 30, 2026, versus net cash used of $11,316 million in the prior-year period. (Q142: "Net cash provided by (used in) operating activities 70,813 ( 11,316 )")

**capital**
- Common stock repurchased in 2025 was $21,433 million. (P324: "Common stock repurchased ( 21,433 ) ( 13,104 ) ( 4,576 )")
- Total share repurchases, including CCAR capital plan repurchases, were 452 million shares in 2025. (P474: "Total share repurchases, including CCAR capital plan repurchases 452 332 147")
- Purchase price of shares repurchased and retired was $21,433 million in 2025. (P474: "Purchase price of shares repurchased and retired (1) $ 21,433 $ 13,104")
- Cash dividends paid were $9,563 million in 2025. (P324: "Cash dividends paid ( 9,563 ) ( 9,503 ) ( 9,087 )")
- Cash dividends paid per share of common stock were $1.08 in 2025. (P474: "The cash dividends paid per share of common stock were $ 1.08 , $ 1.00 and $ 0.92 for 2025, 2024 and 2023, respectively.")
- Cash dividends declared on preferred stock were $1.4 billion in 2025. (P475: "The cash dividends declared on preferred stock were $ 1.4 billion in 2025 and $ 1.6 billion in both 2024 and 2023.")

**risks**
- The interconnectedness and complexity of AI models may complicate oversight and compliance, and reliance on third-party AI models increases risk due to limited visibility into their training data, methodologies and safeguards. (R004: "The interconnectedness and complexity of AI models may complicate oversight and compliance, and reliance on third‑party AI models further increases our risks du")
- Inaccurate AI outputs, unintended or unauthorized exposure of confidential information, biases and possible infringement of intellectual property rights through the use of AI increase this risk. (R004: "Inaccurate AI outputs, unintended or unauthorized exposure of confidential information, biases and possible infringement of intellectual property rights through")
- AI lowers the entry barriers to plan and execute cyberattacks, enables more personalized and harder to detect social engineering, and improves vulnerability discovery, increasing the likelihood of exploitation and the speed, scope, scale and sophistication of cyberattacks. (R002: "AI lowers the entry barriers to plan and execute cyberattacks, enables more personalized and harder to detect social engineering, and improves vulnerability dis")
- Expanded use of AI, including emerging third-party AI services and autonomous AI agents, may result in increased data risk, unpredictable system interactions, inadequate controls or safeguards, AI failure, or produce unintended operations or consequences. (R001: "Expanded use of AI, including emerging third‑party AI services and autonomous AI agents, may result in increased data risk, unpredictable system interactions, i")
- U.S. banking regulators are expected to release proposals in 2026 to revise methodologies for measuring and reporting risk-based capital adequacy, including the calculation of RWA and G-SIB surcharge, and final rules could adversely impact capital requirements. (R005: "U.S. banking regulators are expected to release proposals in 2026 to revise methodologies for measuring and reporting risk-based capital adequacy, including the")
- As new technologies evolve, including the nonbank digital asset ecosystem such as nonbank stablecoins or digital asset trading, and new competitors emerge, businesses and results of operations could be adversely impacted and the company could experience increased volatility in deposits or significant long-term reduction in deposits (financial disintermediation). (R006: "As new technologies evolve and mature, including the further development of the nonbank digital asset ecosystem (e.g., related to nonbank stablecoins or digital")

**accounting**
- Bank of America reported consolidated net income of $30,509 million for 2025. (P318: "Net income $ 30,509 $ 26,973 $ 26,305")
- Net cash provided by operating activities was $12,613 million in 2025 on the consolidated statement of cash flows. (P323: "Net cash provided by (used in) operating activities 12,613 ( 8,805 ) 44,982")
- The auditor expressed an opinion that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations in conformity with U.S. GAAP. (P311: "In our opinion, the consolidated financial statements referred to above present fairly, in all material respects, the financial position of the Corporation as o")
- The auditor stated the Corporation maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P311: "Also in our opinion, the Corporation maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")
- Management concluded that the Corporation's internal control over financial reporting was effective as of December 31, 2025. (P310: "management concluded that, as of December 31, 2025, the Corporation’s internal control over financial reporting is effective")
- The critical audit matter communicated related to the Allowance for Loan and Lease Losses - Commercial and Consumer Card Loans. (P314: "Allowance for Loan and Lease Losses - Commercial and Consumer Card Loans")

## Red team

- [data_conflict, high, rating too low, supported] The model's ROE (10.67%) and implied_roe (8.73%) sit below the actual run-rate: six-month net income of $17,658m (PERF-7) annualises to ~$35.3bn on equity of ~$43.06 x shares, and Q2 net income of $9,074m (PERF-3) is up 27% y/y. A higher starting ROE lifts fair value well above base. (cites PERF-7, PERF-3, roe, implied_roe)
- [business, medium, rating too low, supported] Revenue growth is running far above the terminal 4.75%: Q2 revenue rose to $31,721m from $27,588m, +15% y/y (PERF-2), with Wealth Management revenue up 16% (PERF-9) and Global Markets revenue up $2.6bn (PERF-10). The fade to rf understates a franchise still compounding double digits. (cites PERF-2, PERF-9, PERF-10, terminal_growth)
- [business, medium, rating too high, supported] Capital return is shrinking the equity base the P/B model capitalises: $21,433m of buybacks (CAP-1, CAP-3) plus $9,563m of common dividends (CAP-4) and $1.4bn preferred (CAP-6) exceed net income, so book value per share growth — and the excess-return stream — is being paid out rather than retained. (cites CAP-1, CAP-3, CAP-4, CAP-6)
- [method, medium, rating too high, supported] The bank_model excess-return formula uses a single ROE fading to Ke plus moat share, but the capital build-up uses a bottom-up industry levered beta of 0.761 (regression 1.141) and a 4.75% risk-free rate; a 0.5pt higher cost of equity in the bear case cuts fair value to 43.5, below the 54.43 price, so the Overweight rests on the beta choice. (cites cost_of_equity, beta_method, fair_value)

## Cost

58,208 tokens, $0.0092 across 9 model runs.

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
