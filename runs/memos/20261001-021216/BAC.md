# BAC: Underweight

Desk memo, 2026-10-01. Price 54.96 (2026-09-29). Noise meter agreement 100% (Underweight, Underweight, Underweight). Target weight 0.0%.

## Why

- price / base fair value 1.14 at Medium uncertainty (volatility 22%, range 0.54x base, DCF / industry multiples 0.93): Buy at or below 0.70, Overweight to 0.93, Underweight from 1.07, Sell from 1.35
- red flag caps the rating at Underweight

## Valuation

Method: justified price-to-book on common equity: P/B = (ROE - g) / (cost of equity - g), cost of equity = risk-free + beta x ERP; bear/bull: ROE -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 40.38 | 48.20 | 66.58 | 1.14 |

- Industry check: Bank (Money Center) P/B 1.62x at ROE 12.9%, ROE-adjusted 51.63 per share; model / multiples 0.933
- ROE 9.5% (5-year average; latest 10.7%); the price implies 9.8%; book value per share 43.06; cost of equity 8.7%; narrow: ROIC beat WACC on average over 5 years (+0.8%)


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Bank of America's net income for fiscal 2025 was $30,509 million. (P121: "Net income 30,509 26,973")
- Net income was $30.5 billion, or $3.81 per diluted share, in 2025 compared to $27.0 billion, or $3.19 per diluted share, in 2024. (P121: "Net income was $30.5 billion, or $3.81 per diluted share, in 2025 compared to $27.0 billion, or $3.19 per diluted share, in 2024.")
- Income before income taxes was $37,695 million in 2025. (P121: "come before income taxes 37,695 33,223")
- The efficiency ratio was 61.65% in 2025 versus 63.12% in 2024. (P121: "Efficiency ratio (1) 61.65 63.12")
- Return on average assets was 0.89% in 2025. (P121: "Return on average assets (1) 0.89 % 0.82 %")
- Net cash provided by operating activities was $12,613 million in 2025 on the consolidated statement of cash flows. (P323: "Net cash provided by (used in) operating activities 12,613 ( 8,805 ) 44,982")

**capital**
- Common stock repurchased in 2025 was $21,433 million. (P324: "Common stock repurchased ( 21,433 ) ( 13,104 ) ( 4,576 )")
- Total share repurchases, including CCAR capital plan repurchases, were 452 million shares in 2025. (P474: "Total share repurchases, including CCAR capital plan repurchases 452 332 147")
- Cash dividends paid were $9,563 million in 2025. (P324: "Cash dividends paid ( 9,563 ) ( 9,503 ) ( 9,087 )")
- Cash dividends paid per share of common stock were $1.08 in 2025. (P474: "The cash dividends paid per share of common stock were $ 1.08 , $ 1.00 and $ 0.92 for 2025, 2024 and 2023, respectively.")
- Total long-term debt was $317,816 million at December 31, 2025. (P208: "Total $ 317,816")
- Long-term debt issued during 2025 totaled $98.1 billion. (P455: "During 2025, the Corporation issued $ 98.1 billion of long-term debt")

**risks**
- The interconnectedness and complexity of AI models may complicate oversight and compliance, and reliance on third-party AI models increases risk due to limited visibility into their training data, methodologies and safeguards. (R004: "The interconnectedness and complexity of AI models may complicate oversight and compliance, and reliance on third‑party AI models further increases our risks du")
- Inaccurate AI outputs, unintended or unauthorized exposure of confidential information, biases and possible infringement of intellectual property rights through the use of AI increase this risk. (R004: "Inaccurate AI outputs, unintended or unauthorized exposure of confidential information, biases and possible infringement of intellectual property rights through")
- AI lowers the entry barriers to plan and execute cyberattacks, enables more personalized and harder to detect social engineering, and improves vulnerability discovery, increasing the likelihood of exploitation and the speed, scope, scale and sophistication of cyberattacks. (R002: "AI lowers the entry barriers to plan and execute cyberattacks, enables more personalized and harder to detect social engineering, and improves vulnerability dis")
- Expanded use of AI, including emerging third-party AI services and autonomous AI agents, may result in increased data risk, unpredictable system interactions, inadequate controls or safeguards, AI failure, or produce unintended operations or consequences. (R001: "Expanded use of AI, including emerging third‑party AI services and autonomous AI agents, may result in increased data risk, unpredictable system interactions, i")
- U.S. banking regulators are expected to release proposals in 2026 to revise methodologies for measuring and reporting risk-based capital adequacy, including the calculation of RWA and G-SIB surcharge, and final rules could adversely impact capital requirements. (R005: "U.S. banking regulators are expected to release proposals in 2026 to revise methodologies for measuring and reporting risk-based capital adequacy, including the")
- As new technologies evolve, including the nonbank digital asset ecosystem such as nonbank stablecoins or digital asset trading, and new competitors emerge, businesses and results of operations could be adversely impacted and the company could experience increased volatility in deposits or significant long-term reduction in deposits (financial disintermediation). (R006: "As new technologies evolve and mature, including the further development of the nonbank digital asset ecosystem (e.g., related to nonbank stablecoins or digital")

**accounting**
- Bank of America reported consolidated net income of $30,509 million for 2025. (P323: "Net income $ 30,509 $ 26,973 $ 26,305")
- Net cash provided by operating activities was $12,613 million in 2025. (P323: "Net cash provided by (used in) operating activities 12,613 ( 8,805 ) 44,982")
- PricewaterhouseCoopers LLP expressed an unqualified opinion that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations in conformity with U.S. GAAP. (P311: "In our opinion, the consolidated financial statements referred to above present fairly, in all material respects, the financial position of the Corporation as o")
- The auditor opined that the Corporation maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P311: "Also in our opinion, the Corporation maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")
- Management concluded that the Corporation's internal control over financial reporting was effective as of December 31, 2025. (P310: "management concluded that, as of December 31, 2025, the Corporation’s internal control over financial reporting is effective")
- The critical audit matter communicated was the Allowance for Loan and Lease Losses - Commercial and Consumer Card Loans. (P314: "Allowance for Loan and Lease Losses - Commercial and Consumer Card Loans")

## Red team

- [method, medium, rating too high, supported] The bank excess-return model starts from a 5-year average ROE (normalized_financial_roe) and caps terminal excess returns at half (financial_moat_cap), yet the desk's roe of 0.0951 sits barely above cost_of_equity 0.0869 — a 0.8-point spread. With such a thin spread, small ROE errors swing fair value; the model's own fade assumptions dominate the output rather than evidence. (cites roe, cost_of_equity, financial_moat_cap, normalized_financial_roe)
- [business, medium, rating too low, supported] Momentum is improving: net income rose to $30.5bn in 2025 from $27.0bn (PERF-2), efficiency ratio improved to 61.65% from 63.12% (PERF-4), and H1 2026 net income of $17,658m is up from $14,530m (PERF-8) with Global Markets revenue +$2.6bn (PERF-10). A trailing-ROE-anchored model understates this earnings trajectory. (cites PERF-2, PERF-4, PERF-8, PERF-10)
- [data_conflict, medium, rating too low, supported] The multiples check uses industry P/B 1.62 and industry ROE 0.1286, giving value_per_share 51.63 — above the base fair value of 48.2 and near the 54.96 price. The desk's own second method implies the shares are roughly fairly valued, not 14% overvalued, so the Underweight rests on the DCF leg alone. (cites multiples_check, fair_value, price)
- [method, low, rating too high, supported] The rating is capped at Underweight by a red flag, yet the cited risk evidence (RISK-1 to RISK-6) is generic AI, cyber and regulatory boilerplate that applies to every large bank. If the cap is doing the work, the rating is not evidence-driven; if it is not, the 1.14 price/fair-value already sits in the Underweight band. (cites RISK-1, RISK-3, RISK-5, RISK-6)

## Cost

60,754 tokens, $0.0096 across 9 model runs.

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
