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
- Operating margin 48.5% (reported 46.8% + R&D adjustment 1.8%), ROIC 23.1%, sales-to-capital 0.784, SBC 3.7% of revenue
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
- Total revenue for fiscal 2026 was $331,839 million. (P102: "Revenue $ 331,839 $ 281,724 18%")
- Revenue increased $50.1 billion or 18% in fiscal 2026 compared with fiscal 2025. (P102: "Revenue increased $50.1 billion or 18% driven by growth in Microsoft Cloud.")
- Gross margin was $225,465 million in fiscal 2026, up 16%. (P102: "Gross margin 225,465 193,893 16%")
- Operating income was $155,237 million in fiscal 2026, up 21%. (P102: "Operating income 155,237 128,528 21%")
- Net income was $133,749 million in fiscal 2026, up 31%. (P102: "Net income 133,749 101,832 31%")
- Diluted earnings per share were $17.95 in fiscal 2026, up 32%. (P102: "Diluted earnings per share 17.95 13.64 32%")

**capital**
- Cash, cash equivalents, and short-term investments totaled $76.8 billion as of June 30, 2026. (P113: "Cash, cash equivalents, and short-term investments totaled $76.8 billion and $94.6 billion as of June 30, 2026 and 2025, respectively.")
- Equity and other investments were $36.3 billion as of June 30, 2026. (P113: "Equity and other investments were $36.3 billion and $15.4 billion as of June 30, 2026 and 2025, respectively.")
- Cash and cash equivalents were $20,935 million at June 30, 2026, with short-term investments of $55,908 million. (P130: "Cash and cash equivalents $ 20,935 $ 30,242 Short-term investments 55,908 64,323")
- During fiscal 2026 the company repurchased 36 million shares for $16.7 billion through its share repurchase program. (P118: "During fiscal years 2026 and 2025, we repurchased 36 million shares and 31 million shares of our common stock for $16.7 billion and $13.0 billion, respectively,")
- As of June 30, 2026, $40.6 billion remained of the $60 billion share repurchase program. (P118: "As of June 30, 2026, $40.6 billion remained of our $60 billion share repurchase program.")
- Dividends declared by the Board totaled $27.0 billion in fiscal 2026. (P118: "During fiscal years 2026 and 2025, our Board of Directors declared dividends totaling $27.0 billion and $24.7 billion, respectively.")

**risks**
- Increasing use of AI, including models, algorithms, copilots, and autonomous or semi-autonomous agents, in internal or third-party systems may create new attack surfaces or methods for adversaries. (R006: "Increasing use of AI, including models, algorithms, copilots, and autonomous or semi-autonomous agents, in our internal or third-party systems may create new at")
- Product vulnerabilities can persist after security patches if customers have not installed updates, or if attackers, potentially with the assistance of artificial intelligence, reconstruct and exploit the vulnerabilities before patching. (R006: "Product vulnerabilities can persist even after we have issued security patches if customers have not installed the most recent updates, or if attackers, potenti")
- Code generated by AI could include errors, deficiencies, or vulnerabilities that increase exposure to cyberattacks. (R007: "code generated by AI could include errors, deficiencies, or vulnerabilities that increase our exposure to cyberattacks")
- Certain AI technologies, including conversational or emotionally engaging AI systems, may present distinct risks for children and adolescents. (R007: "In addition, certain AI technologies, including conversational or emotionally engaging AI systems, may present distinct risks for children and adolescents.")
- Governments may impose restrictions on the development, deployment, availability, or cross-border access to advanced AI models based on safety, cybersecurity, or national security. (R012: "governments may impose restrictions on the development, deployment, availability, or cross-border access to advanced AI models based on safety, cybersecurity, o")
- U.S. tariffs, shifting AI export controls policies, and disagreements among governments on sanctions policies toward third countries have increased and may continue to increase operational costs and create uncertainty in the continuity of products. (R012: "U.S. tariffs, shifting AI export controls policies, and disagreements among governments on sanctions policies toward third countries, has and may continue to in")

**accounting**
- Microsoft reported net income of $133,749 million for fiscal 2026. (P130: "Net income $ 133,749 $ 101,832 $ 88,136")
- Net cash from operations was $182,935 million for fiscal 2026. (P132: "Net cash from operations 182,935 136,162 118,548")
- The auditor expressed an unqualified opinion that the financial statements present fairly, in all material respects, the financial position and results of operations and cash flows in conformity with U.S. GAAP. (P193: "opinion, the financial statements present fairly, in all material respects, the financial position of the Company as of June 30, 2026 and 2025, and the results ")
- The auditor communicated a critical audit matter relating to revenue recognition, referring to Note 1 to the financial statements. (P194: "Critical Audit Matters The critical audit matters communicated below are matters arising from the current-period audit of the financial statements")
- The critical audit matter described is Revenue Recognition, referencing Note 1 to the financial statements. (P194: "Revenue Recognition – Refer to Note 1 to the financial statements Critical Audit Matter Description")
- Management concluded that the company's internal control over financial reporting was effective as of June 30, 2026. (P200: "management concluded that the Company’s internal control over financial reporting was effective as of June 30, 2026")

## Red team

- [method, medium, rating too high, supported] The 5-year growth cap forces 17.8% growth to decay to 10% by year 5, but the 10-K shows Intelligent Cloud up 30% (PERF-8) and total revenue up 18% (PERF-2) with capex of $116bn (CAP-8) funding that capacity. The cap may understate the durable growth runway, making the base fair value too low. (cites PERF-2, PERF-8, CAP-8, year5_growth_cap)
- [business, medium, rating too low, supported] Cash conversion is 1.409 and operating cash flow $182.9bn (PERF-7) against net income $133.7bn (PERF-5); ROIC 23.1% versus WACC 9.85% is a wide moat, and terminal_share 0.734 already credits it. If the moat persists longer than the 5-year fade, base value is understated. (cites PERF-7, PERF-5, roic, terminal_share, cash_conversion)
- [method, medium, rating too high, supported] SBC of 3.74% of revenue is expensed but buybacks of $16.7bn (CAP-4) and dividends of $27.0bn (CAP-6) return cash; the DCF's reinvestment via sales-to-capital 0.784 may not capture the $116bn capex (CAP-8) needed to sustain AI growth, understating required reinvestment and overstating value. (cites CAP-4, CAP-6, CAP-8, sales_to_capital, sbc_to_revenue)
- [data_conflict, low, rating too low, supported] The 10-K reports fiscal 2026 revenue growth of 18% (PERF-2) and operating income up 21% (PERF-4), while growth_used is 17.79% and implied_growth 17.63%; the small gap is timing, but the 10-K's stronger segment momentum (PERF-8, PERF-9) supports the higher end. (cites PERF-2, PERF-4, PERF-8, growth_used, implied_growth)

## Cost

61,473 tokens, $0.0097 across 9 model runs.

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
