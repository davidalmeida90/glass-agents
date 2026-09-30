# AMZN: Sell

Desk memo, 2026-10-01. Price 249.15 (2026-09-30). Noise meter agreement 100% (Sell, Sell, Sell). Target weight 0.0%.

## Why

- price / base fair value 1.71 at High uncertainty (volatility 34%, range 1.24x base): Buy at or below 0.60, Overweight to 0.90, Underweight from 1.11, Sell from 1.55

## Valuation

Method: FCFF DCF at company WACC (maturing toward beta 1 from above): trailing revenue growth held 5 years if at most 10%, otherwise decaying to 10% by year 5, then fading to terminal growth = risk-free rate over 5 years; reinvestment = change in revenue / operating sales-to-capital; SBC expensed; R&D capitalized where material; leases as debt; terminal ROIC keeps the moat share (from 5-year ROIC history) of today's excess return; bear/base/bull shift growth -/+4 points, margin -/+10% relative, WACC +/-0.5 points, moat share 0/history/1

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 84.57 | 145.33 | 264.70 | 1.71 |

| Cost of capital | Value |
|---|---:|
| Risk-free (2026-09-01 (rate in Damodaran's ERP computation)) | 4.8% |
| Beta (Retail (General); regression 1.305) | 0.831 |
| Equity risk premium | 4.1% |
| Cost of equity | 8.2% |
| Synthetic rating (coverage 28.13) | AAA |
| Cost of debt, pre-tax | 5.1% |
| Equity weight | 92.2% |
| **WACC** (maturing to 7.8%) | **7.8%** |

- Revenue growth 15.8% (used 15.8%); the price implies 53.2%
- Operating margin 12.1%, ROIC 11.0%, sales-to-capital 1.241, SBC 2.5% of revenue
- Moat: narrow: ROIC beat WACC on average over 5 years (+5.5%)
- Terminal value 87.7% of enterprise value; EV/EBIT at base 17.9x vs market 29.8x
- Period: trailing twelve months to 2026-06-30 (revenue growth: twelve months to 2026-06-30 vs to 2025-06-30), from 10-K and 10-Q XBRL; the readers' evidence comes from the latest 10-K only

Base value per share, WACC by terminal growth:

| | g -0.5% | g +0.0% | g +0.5% |
|---|---:|---:|---:|
| wacc -1.0% | 146.50 | 155.00 | 166.47 |
| wacc +0.0% | 137.33 | 145.33 | 156.12 |
| wacc +1.0% | 128.76 | 136.30 | 146.46 |


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Consolidated net sales were $716,924 million in 2025. (P074: "Consolidated $ 637,959 $ 716,924")
- Consolidated net sales increased 12% in 2025 compared to the prior year. (P074: "Consolidated 11 12")
- Operating income was $79,975 million in 2025. (P099: "Operating income 36,852 68,593 79,975")
- Net income was $77,670 million in 2025. (P099: "Net income $ 30,425 $ 59,248 $ 77,670")
- Net cash provided by operating activities was $139,514 million in 2025. (P068: "Operating activities $ 115,877 $ 139,514")
- North America net sales were $426,305 million in 2025. (P074: "North America $ 387,497 $ 426,305")

**capital**
- Total cash, cash equivalents, and marketable securities were $123,029 million at December 31, 2025. (P137: "Total cash, cash equivalents, and marketable securities $ 123,029")
- Cash and cash equivalents on the balance sheet were $86,810 million at December 31, 2025. (P100: "Cash and cash equivalents $ 78,779 $ 86,810")
- Marketable securities on the balance sheet were $36,219 million at December 31, 2025. (P100: "Marketable securities 22,423 36,219")
- Long-term debt was $65,648 million at December 31, 2025. (P100: "Long-term debt 52,623 65,648")
- Proceeds from long-term debt were $15,673 million in 2025, with repayments of long-term debt of $5,021 million. (P098: "Proceeds from long-term debt — — 15,673 Repayments of long-term debt ( 3,676 ) ( 9,182 ) ( 5,021 )")
- There were no repurchases of common stock in 2023, 2024, or 2025, and $6.1 billion remained under the repurchase program as of December 31, 2025. (P158: "There were no repurchases of our common stock in 2023, 2024, or 2025. As of December 31, 2025, we have $ 6.1 billion remaining under the repurchase program.")

**risks**
- Profitability or other intended benefits in newer activities, including development and adoption of automation, artificial intelligence, and machine learning technologies for customer and internal use, may not meet expectations, and the company may not recoup its often significant investments. (R000: "profitability or other intended benefits, if any, in our newer activities (including development and adoption of automation, artificial intelligence, and machin")
- The company experiences significant competition in the technology industry, particularly for software engineers, computer scientists, and other technical staff, including for artificial intelligence and machine learning technologies. (R000: "we experience significant competition in the technology industry, particularly for software engineers, computer scientists, and other technical staff (including")

**accounting**
- Net income for fiscal 2025 was USD 77,670 million. (P097: "Net income 30,425 59,248 77,670")
- Net cash provided by operating activities for fiscal 2025 was USD 139,514 million. (P097: "Net cash provided by (used in) operating activities 84,946 115,877 139,514")
- Cash provided by operating activities was USD 139.5 billion in 2025, up from USD 115.9 billion in 2024. (P068: "Cash provided by (used in) operating activities was $115.9 billion and $139.5 billion in 2024 and 2025.")
- Ernst & Young LLP expressed an unqualified opinion that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations in conformity with U.S. GAAP. (P093: "In our opinion, the consolidated financial statements present fairly, in all material respects, the financial position of the Company at December 31, 2025 and 2")
- Management concluded that internal control over financial reporting was effective as of December 31, 2025. (P175: "management concluded that, as of December 31, 2025, our internal control over financial reporting was effective in providing reasonable assurance regarding the ")
- Ernst & Young LLP opined that Amazon maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P176: "In our opinion, Amazon.com, Inc. (the Company) maintained, in all material respects, effective internal control over financial reporting as")

## Red team

- [data_conflict, high, rating too high, supported] The desk's starting growth of 15.77% is a trailing-twelve-month figure, but the 10-K shows fiscal 2025 net sales growth of 12% (PERF-2) on $716,924m revenue (PERF-1). The 10-K is the verified anchor; the TTM number is inflated by a favorable comparison base. Using 12% lowers the base fair value and widens the gap to price. (cites PERF-2, PERF-1, growth_used)
- [data_conflict, medium, rating too low, supported] The desk's operating margin of 12.08% understates the 10-K: operating income of $79,975m on $716,924m revenue is 11.16%... but cost of sales at 49.7% (PERF-10) implies a gross margin far above the 12% operating margin, and AWS at 20% growth (PERF-9) is the margin-accretive engine. If the TTM margin is depressed by mix, the base value is too low. (cites PERF-3, PERF-10, PERF-9)
- [business, high, rating too low, supported] AWS grew 20% to $128,725m (PERF-9, PERF-8), roughly 18% of revenue, and is the highest-margin segment. A single blended 15.77% growth rate and 12.08% margin ignore that the mix shift toward AWS mechanically lifts both growth and margin for years. The Sell rating treats a structurally improving mix as a maturing business. (cites PERF-8, PERF-9, PERF-3)
- [method, medium, rating too high, supported] The moat share of 0.877 (terminal_share) keeps 87.7% of today's excess return forever, and terminal ROIC of 9.44% still exceeds WACC of 7.85%. That is a generous terminal assumption for a firm whose ROIC of 11.03% barely clears WACC; a lower moat share would cut the base value and justify the Sell more strongly. (cites terminal_share, terminal_roic, roic, wacc)

## Cost

53,123 tokens, $0.0084 across 9 model runs.

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
