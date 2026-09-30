# NVDA: Underweight

Desk memo, 2026-10-01. Price 228.38 (2026-09-30). Noise meter agreement 100% (Underweight, Underweight, Underweight). Target weight 0.0%.

## Why

- price / base fair value 0.81 at High uncertainty (volatility 38%, range 0.91x base): Buy at or below 0.60, Overweight to 0.90, Underweight from 1.11, Sell from 1.55
- one notch off: cash conversion 0.75 (operating cash flow / net income under 0.8)
- red team correction {'operating_margin': 0.604}: base value 235.14, P/FV 0.97

## Valuation

Method: FCFF DCF at company WACC (maturing toward beta 1 from above): trailing revenue growth held 5 years if at most 10%, otherwise decaying to 10% by year 5, then fading to terminal growth = risk-free rate over 5 years; reinvestment = change in revenue / operating sales-to-capital; SBC expensed; R&D capitalized where material; leases as debt; terminal ROIC keeps the moat share (from 5-year ROIC history) of today's excess return; bear/base/bull shift growth -/+4 points, margin -/+10% relative, WACC +/-0.5 points, moat share 0/history/1

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 146.85 | 281.89 | 404.23 | 0.81 |

| Cost of capital | Value |
|---|---:|
| Risk-free (2026-09-01 (rate in Damodaran's ERP computation)) | 4.8% |
| Beta (Semiconductor; regression 1.815) | 1.513 |
| Equity risk premium | 4.1% |
| Cost of equity | 11.0% |
| Synthetic rating (coverage 425.82) | AAA |
| Cost of debt, pre-tax | 5.1% |
| Equity weight | 99.3% |
| **WACC** (maturing to 8.8%) | **11.0%** |

- Revenue growth 83.4% (used 30.0%); the price implies 19.1%
- Operating margin 70.5%, ROIC 62.1%, sales-to-capital 1.146, SBC 2.4% of revenue
- Moat: narrow: ROIC beat WACC on average over 5 years (+34.3%)
- Terminal value 70.5% of enterprise value; EV/EBIT at base 31.9x vs market 25.9x
- Period: trailing twelve months to 2026-07-26 (revenue growth: twelve months to 2026-07-26 vs to 2025-07-27), from 10-K and 10-Q XBRL; the readers' evidence comes from the latest 10-K only

Base value per share, WACC by terminal growth:

| | g -0.5% | g +0.0% | g +0.5% |
|---|---:|---:|---:|
| wacc -1.0% | 273.90 | 297.47 | 327.48 |
| wacc +0.0% | 259.67 | 281.89 | 310.18 |
| wacc +1.0% | 246.33 | 267.28 | 293.97 |

- Data note: R&D capitalized over 5 years: research asset 43.1B, EBIT +16.0B (R&D 23.6B - amortization 7.6B)

## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total revenue for fiscal 2026 was $215,938 million. (P134: "Total $ 215,938 $ 130,497 $ 85,441 65 %")
- Total revenue grew 65% in fiscal 2026 versus fiscal 2025. (P134: "Total $ 215,938 $ 130,497 $ 85,441 65 %")
- Gross margin was 71.1% of revenue in fiscal 2026, down from 75.0% in fiscal 2025. (P134: "Gross profit 71.1 75.0")
- Operating income was 60.4% of revenue in fiscal 2026. (P134: "Operating income 60.4 62.4")
- Net income for fiscal 2026 was $120,067 million. (P164: "Net income — — — — 120,067 120,067")
- Net cash provided by operating activities was $102,718 million in fiscal 2026. (P140: "Net cash provided by operating activities $ 102,718 $ 64,089")

**capital**
- Cash, cash equivalents, and marketable securities totaled $62,556 million as of January 25, 2026. (P140: "Cash, cash equivalents, and marketable securities $ 62,556 $ 43,210")
- Cash and cash equivalents were $10,605 million as of January 25, 2026. (P140: "Cash and cash equivalents $ 10,605 $ 8,589")
- Marketable securities were $51,951 million as of January 25, 2026. (P140: "Marketable securities 51,951 34,621")
- Net carrying amount of debt was $8,468 million as of January 25, 2026, with $999 million short-term and $7,469 million long-term. (P143: "Net carrying amount $ 8,468 Less short-term portion 999 Total long-term portion $ 7,469")
- In fiscal year 2026, the company repurchased 282 million shares of its common stock for $40.4 billion. (P120: "In fiscal year 2026, we repurchased 282 million shares of our common stock for $40.4 billion.")
- In fiscal year 2026, the company paid cash dividends to shareholders of $974 million. (P120: "In fiscal year 2026, we paid cash dividends to our shareholders of $974 million.")

**risks**
- NVIDIA incurred a $4.5 billion charge in the first quarter of fiscal year 2026 associated with H20 for excess inventory and purchase obligations after the USG required a license for H20 exports to China. (R003: "we incurred a $4.5 billion charge in the first quarter of fiscal year 2026 associated with H20 for excess inventory and purchase obliga")
- NVIDIA generated approximately $60 million in H20 revenue under licenses granted in August 2025 allowing shipment of certain H20 products to certain China-based customers. (R004: "We generated approximately $60 million in H20 revenue under those licenses.")
- USG officials expressed an expectation that the USG will receive 15% or more of the revenue generated from licensed sales of NVIDIA products, though no regulation codified such requirement. (R004: "USG officials expressed an expectation that the USG will receive 15% or more of the revenue generated from licensed sales of our products")
- Any H200 shipped under the new licensing program will be subject to a 25% tariff upon importation into the United States. (R004: "any H200 shipped under the new licensing program will be subject to a 25% tariff upon importation into the United States.")
- As of the end of fiscal year 2026, NVIDIA was effectively foreclosed from competing in China's data center computing/compute market, which helped competitors build larger developer and customer ecosystems. (R005: "As of the end of fiscal year 2026, we were effectively foreclosed from competing in China's data center computing/compute market, and our effective foreclosure ")
- On September 15, 2025, China's antitrust regulators published a preliminary finding that NVIDIA's compliance with U.S. export controls discriminated unfairly against customers in the China market and violated the terms of China's approval of the Mellanox acquisition. (R003: "On September 15, 2025, China’s antitrust regulators published their preliminary finding that our compliance with applicable U.S. export controls, which required")

**accounting**
- Net income for fiscal year 2026 was $120,067 million. (P162: "Net income $ 120,067 $ 72,880 $ 29,760")
- Net cash provided by operating activities for fiscal year 2026 was $102,718 million. (P165: "Net cash provided by operating activities 102,718 64,089 28,090")
- The auditor's opinion states the consolidated financial statements present fairly, in all material respects, the financial position and results of operations and cash flows in conformity with U.S. GAAP. (P156: "of its operations and its cash flows for each of the three years in the period ended January 25, 2026 in conformity with accounting principles generally accepte")
- The auditor opined that the Company maintained, in all material respects, effective internal control over financial reporting as of January 25, 2026. (P156: "Also in our opinion, the Company maintained, in all material respects, effective internal control over financial reporting as of January 25, 2026, based on crit")
- Management concluded that internal control over financial reporting was effective as of January 25, 2026. (P149: "our management concluded that our internal control over financial reporting was effective as of January 25, 2026.")
- The critical audit matter was the valuation of inventories, including provisions for excess or obsolete inventories and excess product purchase commitments. (P159: "Valuation of Inventories - Provisions for Excess or Obsolete Inventories and Excess Product Purchase Commitments")

## Red team

- [data_conflict, high, rating too high, supported] The desk's operating_margin of 70.5% is far above the 10-K's 60.4% operating income margin (PERF-4) and above the 71.1% gross margin (PERF-3). A 70% operating margin leaves almost nothing for R&D and SG&A, overstating NOPAT and base fair value; the rating should be lower. (cites PERF-4, PERF-3)
- [data_conflict, medium, rating too low, supported] growth_used of 30% is the clipped bound, but the 10-K shows 65% revenue growth (PERF-2) and the trailing figure is 83.4%. Even after the year-5 decay rule, starting growth is understated, so base fair value and the rating are too low. (cites PERF-2, growth_used, revenue_growth)
- [business, medium, rating too high, supported] Cash conversion is 0.749, below the desk's own 0.8 caution (net income $120.1bn vs operating cash flow $102.7bn, PERF-5/PERF-6), and the desk already flags a one-notch downgrade. Earnings quality is weaker than the base case implies. (cites PERF-5, PERF-6, cash_conversion)
- [business, medium, rating too low, supported] The 10-K shows a $4.5bn H20 charge and effective foreclosure from China's data center market (RISK-1, RISK-5), yet Compute & Networking still grew 67% with $130bn operating income (PERF-7, PERF-8). The base case may understate durable non-China demand. (cites RISK-1, RISK-5, PERF-7, PERF-8)
- Correction applied in code: {'fixes': {'operating_margin': 0.604}, 'fair_value': {'bear': 123.53, 'base': 235.14, 'bull': 340.15}, 'step': -1}

## Cost

57,331 tokens, $0.0091 across 9 model runs.

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
