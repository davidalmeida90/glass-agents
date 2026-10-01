# MSFT: Hold

Desk memo, 2026-10-01. Price 512.90 (2026-09-30). Noise meter agreement 100% (Hold, Hold, Hold). Target weight 0.0%.

## Why

- price / base fair value 1.01 at High uncertainty (volatility 32%, range 0.89x base, DCF / industry multiples 0.76): Buy at or below 0.60, Overweight to 0.90, Underweight from 1.11, Sell from 1.55

## Valuation

Method: FCFF DCF at company WACC (maturing toward beta 1 from above): trailing revenue growth held 5 years if at most 10%, otherwise decaying to 10% by year 5, then fading to terminal growth = risk-free rate over 5 years; reinvestment = change in revenue / operating sales-to-capital; SBC expensed; R&D capitalized where material; leases as debt; terminal ROIC keeps the moat share (from 5-year ROIC history) of today's excess return; bear/base/bull shift growth -/+4 points, margin -/+10% relative, WACC +/-0.5 points, moat share 0/history/1

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 264.56 | 506.35 | 713.02 | 1.01 |

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

- Revenue growth: last twelve months 17.8%, 3-year CAGR 16.1%, blend 17.0% (used 17.0%); the price implies 17.6%
- Operating margin 48.5% (reported 46.8% + R&D adjustment 1.8%), ROIC 23.1%, sales-to-capital 0.784, SBC 3.7% of revenue
- Moat: wide: ROIC beat WACC by 5%+ in all 5 years (min +15.4%)
- Industry multiples check: Software (System & Application) EV/EBIT 32.4x gives 670.61 per share; DCF / multiples 0.755
- Terminal value 73.2% of enterprise value; EV/EBIT at base 23.7x vs market 24.0x
- Period: trailing twelve months to 2026-06-30 (revenue growth: twelve months to 2026-06-30 vs to 2025-06-30), from 10-K and 10-Q XBRL; the readers' evidence comes from the latest 10-K only

Base value per share, WACC by terminal growth:

| | g -0.5% | g +0.0% | g +0.5% |
|---|---:|---:|---:|
| wacc -1.0% | 493.94 | 535.27 | 588.24 |
| wacc +0.0% | 467.41 | 506.35 | 556.27 |
| wacc +1.0% | 442.56 | 479.27 | 526.32 |

- Data note: debt from Yahoo totalDebt (128.8B): XBRL tags gave 56.8B
- Data note: R&D capitalized over 3 years: research asset 67.1B, EBIT +5.8B (R&D 35.6B - amortization 29.7B)

## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total revenue for fiscal 2026 was $331,839 million. (P130: "tal revenue 331,839 281,724 245,122")
- Total revenue grew 18% in fiscal 2026 compared with fiscal 2025. (P104: "Total Revenue $ 331,839 $ 281,724 18%")
- Gross margin for fiscal 2026 was $225,465 million. (P130: "Gross margin 225,465 193,893 171,008")
- Operating income for fiscal 2026 was $155,237 million, up 21%. (P104: "Operating income $ 155,237 $ 128,528 21%")
- Net income for fiscal 2026 was $133,749 million. (P130: "Net income $ 133,749 $ 101,832 $ 88,136")
- Net cash from operations for fiscal 2026 was $182,935 million. (P132: "Net cash from operations 182,935 136,162 118,548")

**capital**
- Cash, cash equivalents, and short-term investments totaled $76.8 billion as of June 30, 2026. (P113: "Cash, cash equivalents, and short-term investments totaled $76.8 billion and $94.6 billion as of June 30, 2026 and 2025, respectively.")
- Total cash, cash equivalents, and short-term investments on the balance sheet were $76,843 million at June 30, 2026. (P130: "Total cash, cash equivalents, and short-term investments 76,843 94,565")
- Equity and other investments were $36.3 billion as of June 30, 2026. (P113: "Equity and other investments were $36.3 billion and $15.4 billion as of June 30, 2026 and 2025, respectively.")
- Repayments of debt were $3,000 million in fiscal 2026. (P132: "Repayments of debt ( 3,000 ) ( 3,216 ) ( 29,070 )")
- Microsoft repurchased 36 million shares for $16.7 billion in fiscal 2026 through its share repurchase program. (P118: "we repurchased 36 million shares and 31 million shares of our common stock for $16.7 billion and $13.0 billion, respectively, through our share repurchase progr")
- Cash paid for common stock repurchased was $22,271 million in fiscal 2026. (P132: "Common stock repurchased ( 22,271 ) ( 18,420 ) ( 17,254 )")

**risks**
- Increasing use of AI, including models, algorithms, copilots, and autonomous or semi-autonomous agents, in internal or third-party systems may create new attack surfaces or methods for adversaries. (R006: "Increasing use of AI, including models, algorithms, copilots, and autonomous or semi-autonomous agents, in our internal or third-party systems may create new at")
- Attackers, potentially with the assistance of artificial intelligence, may reconstruct and exploit product vulnerabilities before patching. (R006: "if attackers, potentially with the assistance of artificial intelligence, reconstruct and exploit the vulnerabilities before patching")
- Code generated by AI could include errors, deficiencies, or vulnerabilities that increase exposure to cyberattacks. (R007: "code generated by AI could include errors, deficiencies, or vulnerabilities that increase our exposure to cyberattacks")
- Governments may impose restrictions on the development, deployment, availability, or cross-border access to advanced AI models based on safety, cybersecurity, or national security. (R012: "governments may impose restrictions on the development, deployment, availability, or cross-border access to advanced AI models based on safety, cybersecurity, o")
- U.S. tariffs, shifting AI export controls policies, and disagreements among governments on sanctions policies toward third countries have increased and may continue to increase operational costs and create uncertainty in the continuity of products. (R012: "U.S. tariffs, shifting AI export controls policies, and disagreements among governments on sanctions policies toward third countries, has and may continue to in")
- There are limited suppliers for certain critical device and datacenter components, and those items are in short supply, with competitors scaling infrastructure and using some of the same suppliers and materials. (R010: "There are limited suppliers for certain critical device and datacenter components, and those items are in short supply. Our competitors are also scaling their i")

**accounting**
- Microsoft reported net income of $133,749 million for fiscal 2026. (P130: "Net income $ 133,749 $ 101,832 $ 88,136")
- Net cash from operations was $182,935 million for fiscal 2026. (P132: "Net cash from operations 182,935 136,162 118,548")
- The auditor expressed an unqualified opinion that the financial statements present fairly, in all material respects, the financial position and results of operations and cash flows in conformity with U.S. GAAP. (P193: "opinion, the financial statements present fairly, in all material respects, the financial position of the Company as of June 30, 2026 and 2025, and the results ")
- The auditor communicated a critical audit matter relating to revenue recognition, referring to Note 1 to the financial statements. (P194: "Critical Audit Matters The critical audit matters communicated below are matters arising from the current-period audit of the financial statements")
- The critical audit matter described is Revenue Recognition, referencing Note 1 to the financial statements. (P194: "Revenue Recognition – Refer to Note 1 to the financial statements Critical Audit Matter Description")
- Management concluded that the Company's internal control over financial reporting was effective as of June 30, 2026. (P200: "management concluded that the Company’s internal control over financial reporting was effective as of June 30, 2026")

## Red team

- [business, high, rating too low, supported] Intelligent Cloud grew 30% to $137.8bn with segment operating income up 28% (PERF-8, PERF-9) — the fastest-growing, highest-margin engine is now ~42% of revenue. A 5-year fade to a 10% cap (year5_growth_cap) truncates the mix shift that is still accelerating, so base fair value understates the franchise. (cites PERF-8, PERF-9, year5_growth_cap, growth_used)
- [method, medium, rating too low, supported] Terminal value keeps only terminal_share 0.732 of today's ROIC-WACC spread, yet ROIC 0.2312 vs WACC 0.0985 is a 13-point spread earned every year of the 5-year history (moat_margin 0.05). The moat test should award the full 1.0 share; the haircut alone removes roughly a quarter of terminal excess return. (cites roic, wacc, terminal_share, moat_margin, terminal_excess_return)
- [method, medium, rating too high, supported] The DCF/multiples ratio of 0.755 sits outside the 0.67-1.5 agreement band, and industry EV/EBIT of 32.4 implies $670.61 per share versus the $506.35 base. The desk already raised uncertainty one level for this, but the rating still leans on a DCF that the relative-value cross-check contradicts by 25%. (cites multiples_check, ev_to_ebit, fair_value)
- [data_conflict, medium, rating too high, supported] growth_used 0.1696 blends TTM with the 3-year CAGR, but the 10-K states fiscal 2026 revenue grew 18% (PERF-2) and Intelligent Cloud 30% (PERF-8). If the blend is dragging the starting growth below the actual run-rate, the DCF is understating growth — the opposite error — so the 1.01 price/fair-value is not a stable anchor either way. (cites PERF-2, PERF-8, growth_used, growth_blend)

## Cost

60,780 tokens, $0.0095 across 9 model runs.

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
