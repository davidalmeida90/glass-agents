# MSFT: Hold

Desk memo, 2026-10-01. Price 512.90 (2026-09-30). Noise meter agreement 100% (Hold, Hold, Hold). Target weight 0.0%.

## Why

- price / base fair value 1.00 at High uncertainty (volatility 32%, range 0.89x base): Buy at or below 0.60, Overweight to 0.90, Underweight from 1.11, Sell from 1.55

## Valuation

Method: FCFF DCF at company WACC (maturing toward beta 1 from above): trailing revenue growth held 5 years if at most 10%, otherwise decaying to 10% by year 5, then fading to terminal growth = risk-free rate over 5 years; reinvestment = change in revenue / operating sales-to-capital; SBC expensed; R&D capitalized where material; leases as debt; terminal ROIC keeps the moat share (from 5-year ROIC history) of today's excess return; bear/base/bull shift growth -/+4 points, margin -/+10% relative, WACC +/-0.5 points, moat share 0/history/1

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 268.41 | 514.44 | 724.51 | 1.00 |

| Cost of capital | Value |
|---|---:|
| Risk-free (2026-09-01 (rate in Damodaran's ERP computation)) | 4.8% |
| Beta (Software (System & Application); regression 1.068) | 1.28 |
| Equity risk premium | 4.1% |
| Cost of equity | 10.1% |
| Synthetic rating (coverage 50.88) | AAA |
| Cost of debt, pre-tax | 5.1% |
| Equity weight | 96.7% |
| **WACC** (maturing to 8.7%) | **9.8%** |

- Revenue growth 17.8% (used 17.8%); the price implies 17.6%
- Operating margin 48.5%, ROIC 23.1%, sales-to-capital 0.784, SBC 3.7% of revenue
- Moat: wide: ROIC beat WACC by 5%+ in all 5 years (min +15.4%)
- Terminal value 73.4% of enterprise value; EV/EBIT at base 24.0x vs market 24.0x
- Period: trailing twelve months to 2026-06-30 (revenue growth: twelve months to 2026-06-30 vs to 2025-06-30), from 10-K and 10-Q XBRL; the readers' evidence comes from the latest 10-K only

Base value per share, WACC by terminal growth:

| | g -0.5% | g +0.0% | g +0.5% |
|---|---:|---:|---:|
| wacc -1.0% | 501.78 | 543.86 | 597.80 |
| wacc +0.0% | 474.79 | 514.44 | 565.26 |
| wacc +1.0% | 449.50 | 486.88 | 534.78 |

- Data note: debt from Yahoo totalDebt (128.8B): XBRL tags gave 56.8B
- Data note: R&D capitalized over 3 years: research asset 67.1B, EBIT +5.8B (R&D 35.6B - amortization 29.7B)

## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total revenue for fiscal 2026 was $331,839 million. (P130: "tal revenue 331,839 281,724 245,122")
- Total revenue grew 18% in fiscal 2026 compared with fiscal 2025. (P104: "Total Revenue $ 331,839 $ 281,724 18%")
- Gross margin for fiscal 2026 was $225,465 million. (P130: "Gross margin 225,465 193,893 171,008")
- Operating income for fiscal 2026 was $155,237 million, up 21%. (P130: "Operating income 155,237 128,528 109,433")
- Net income for fiscal 2026 was $133,749 million. (P130: "Net income $ 133,749 $ 101,832 $ 88,136")
- Net cash from operations for fiscal 2026 was $182,935 million. (P132: "Net cash from operations 182,935 136,162 118,548")

**capital**
- Cash, cash equivalents, and short-term investments totaled $76.8 billion as of June 30, 2026. (P113: "Cash, cash equivalents, and short-term investments totaled $76.8 billion and $94.6 billion as of June 30, 2026 and 2025, respectively.")
- Cash and cash equivalents were $20,935 million and short-term investments $55,908 million at June 30, 2026. (P130: "Cash and cash equivalents $ 20,935 $ 30,242 Short-term investments 55,908 64,323")
- Equity and other investments were $36.3 billion as of June 30, 2026. (P113: "Equity and other investments were $36.3 billion and $15.4 billion as of June 30, 2026 and 2025, respectively.")
- Repayments of debt were $3,000 million in fiscal 2026. (P132: "Repayments of debt ( 3,000 ) ( 3,216 ) ( 29,070 )")
- The company repurchased 36 million shares for $16.7 billion in fiscal 2026 through its share repurchase program. (P118: "During fiscal years 2026 and 2025, we repurchased 36 million shares and 31 million shares of our common stock for $16.7 billion and $13.0 billion, respectively,")
- Cash used for common stock repurchased was $22,271 million in fiscal 2026. (P132: "Common stock repurchased ( 22,271 ) ( 18,420 ) ( 17,254 )")

**risks**
- Microsoft's AI offerings compete with AI products from hyperscalers, open-source offerings, and frontier model providers, some of which are also current or potential partners. (R000: "Our AI offerings compete with AI products from hyperscalers, open-source offerings, and frontier model providers, some of which are also current or potential pa")
- Microsoft's significant capital and operational investments to develop, train, deploy, and support AI models and related cloud services are made at significant scale and in advance of fully developed revenue streams. (R001: "These investments are being made at significant scale and on an accelerated timeline, require substantial and increasing capital expenditures and continued acce")
- Microsoft's AI strategy depends in part on strategic relationships with third parties providing technologies, models, products, and services, and many of these partners compete with Microsoft. (R003: "Our AI strategy also depends in part on strategic relationships with third parties that provide technologies, models, products, and services that enhance our of")
- Increasing use of AI, including models, algorithms, copilots, and autonomous or semi-autonomous agents, in internal or third-party systems may create new attack surfaces or methods for adversaries. (R006: "Increasing use of AI, including models, algorithms, copilots, and autonomous or semi-autonomous agents, in our internal or third-party systems may create new at")
- Microsoft has experienced and may continue to experience supply constraints, including shortages of semiconductors, networking equipment, power systems, cooling equipment, and other key components. (R010: "We have experienced and may continue to experience supply constraints, including shortages of semiconductors, networking equipment, power systems, cooling equip")
- Governments may impose restrictions on the development, deployment, availability, or cross-border access to advanced AI models based on safety, cybersecurity, or national security. (R012: "In addition, governments may impose restrictions on the development, deployment, availability, or cross-border access to advanced AI models based on safety, cyb")

**accounting**
- Microsoft reported net income of $133,749 million for fiscal 2026. (P130: "Net income $ 133,749 $ 101,832 $ 88,136")
- Net cash from operations was $182,935 million for fiscal 2026. (P132: "Net cash from operations 182,935 136,162 118,548")
- The auditor expressed an unqualified opinion that the financial statements present fairly, in all material respects, the financial position and results of operations and cash flows, in conformity with U.S. GAAP. (P193: "opinion, the financial statements present fairly, in all material respects, the financial position of the Company as of June 30, 2026 and 2025, and the results ")
- The auditor reported a critical audit matter relating to revenue recognition, referencing Note 1 to the financial statements. (P194: "Critical Audit Matters The critical audit matters communicated below are matters arising from the current-period audit of the financial statements")
- The critical audit matter described is Revenue Recognition, referring to Note 1 to the financial statements. (P194: "Revenue Recognition – Refer to Note 1 to the financial statements Critical Audit Matter Description")
- Management concluded that the company's internal control over financial reporting was effective as of June 30, 2026. (P200: "management concluded that the Company’s internal control over financial reporting was effective as of June 30, 2026")

## Red team

- [method, medium, rating too high, supported] The desk holds 17.8% growth for five years, but the 10-K shows the mix is already decelerating: More Personal Computing revenue fell 1% (PERF-10) and Productivity grew 16% (PERF-9), below the consolidated rate. Only Intelligent Cloud (PERF-7, +30%) carries the number, so the plateau assumption is generous. (cites PERF-7, PERF-9, PERF-10, growth_used)
- [business, medium, rating too low, supported] Operating income rose 21% to $155,237m (PERF-4) on 18% revenue growth, and Intelligent Cloud operating income rose 28% (PERF-8) — margins are expanding, not fading. The base case holds operating_margin at 48.5% flat, ignoring the operating leverage the 10-K shows. (cites PERF-4, PERF-8, operating_margin)
- [business, medium, rating too low, supported] Cash from operations was $182,935m (PERF-6) against $133,749m net income (PERF-5) and $115,948m capex (CAP-8). The desk's cash_conversion of 1.409 shows earnings are cash-backed; the bear case (0.52x base) treats a cash-generative franchise as if its cash flows were at risk. (cites PERF-6, PERF-5, CAP-8, cash_conversion)
- [method, medium, rating too high, supported] Terminal value assumes 73.4% of today's excess return survives forever (terminal_share, terminal_roic 23.1% vs wacc 9.85%), yet the 10-K flags AI competition, third-party model dependence, supply constraints and regulation (RISK-1, RISK-3, RISK-5, RISK-6) — risks that erode moats precisely in the terminal period. (cites RISK-1, RISK-3, RISK-5, RISK-6, terminal_share, terminal_roic)

## Cost

60,225 tokens, $0.0095 across 9 model runs.

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
