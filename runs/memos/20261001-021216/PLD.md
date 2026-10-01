# PLD: Overweight

Desk memo, 2026-10-01. Price 132.61 (2026-09-29). Noise meter agreement 100% (Overweight, Overweight, Overweight). Target weight 3.5%.

## Why

- price / base fair value 0.90 at Medium uncertainty (volatility 21%, range 0.54x base): Buy at or below 0.70, Overweight to 0.93, Underweight from 1.07, Sell from 1.35

## Valuation

Method: two-stage dividend discount: dividends per share grow at the revenue growth blend (bounded -5% to 8%) for 5 years, fading to terminal growth = risk-free rate, at the CAPM cost of equity; bear/bull growth -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 114.59 | 147.50 | 194.09 | 0.90 |

- Dividend per share 4.10 (yield 3.1%), growth 8.0% fading to 4.8%, cost of equity 8.3%


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Real Estate Segment rental revenues were $8,159 million in 2025. (P089: "Rental revenues $ 8,159 $ 7,515")
- Real Estate Segment NOI was $6,188 million in 2025 versus $5,717 million in 2024. (P089: "Real Estate Segment – NOI $ 6,188 $ 5,717")
- Operating income was $4,358 million in 2025 compared with $4,416 million in 2024. (P089: "Operating income $ 4,358 $ 4,416")
- Net cash provided by operating activities was $5,008 million in 2025 and $4,912 million in 2024. (P110: "Net cash provided by (used in) operating activities $ 5,008 $ 4,912")
- Real estate segment rental revenues were $4,302 million for the six months ended June 30, 2026 versus $4,013 million in 2025. (Q081: "Rental revenues $ 4,302 $ 4,013")
- Real estate segment rental revenues grew from $4,013 million to $4,302 million for the six months ended June 30, 2026. (Q081: "Rental revenues $ 4,302 $ 4,013")

**capital**
- Cash and cash equivalents at December 31, 2025 were $1,145,647 thousand. (P156: "Cash and cash equivalents, end of year $ 1,145,647 $ 1,318,591 $ 530,388")
- Available unrestricted cash balances were $1.1 billion at December 31, 2025. (P108: "available unrestricted cash balances ($1.1 billion at December 31, 2025)")
- Total debt was $35,037,073 thousand at December 31, 2025, up from $30,879,263 thousand at December 31, 2024. (P156: "Debt $ 35,037,073 $ 30,879,263")
- Net cash provided by operating activities was $5,008 million in 2025. (P110: "Net cash provided by (used in) operating activities $ 5,008 $ 4,912")
- Real estate development spending was $2,781,260 thousand in 2025. (P162: "Real estate development ( 2,781,260 ) ( 3,206,231 ) ( 3,399,114 )")
- Real estate acquisitions were $1,800,527 thousand in 2025. (P162: "Real estate acquisitions ( 1,800,527 ) ( 2,327,605 ) ( 4,195,714 )")

**risks**
- The company's business and operations could suffer in the event of system failures, cybersecurity attacks or risks associated with AI. (R000: "Our business and operations could suffer in the event of system failures, cybersecurity attacks or risks associated with AI.")
- The company has formed publicly traded investment vehicles, such as Nippon Prologis REIT, Inc., China AMC Prologis Logistics REIT and FIBRA Prologis, for which it serves as sponsor or manager. (R000: "We have formed publicly traded investment vehicles, such as Nippon Prologis REIT, Inc., China AMC Prologis Logistics REIT and FIBRA Prologis, for which we serve")

**accounting**
- Net earnings for fiscal 2025 were USD 3,565,299 thousand. (P154: "net earnings $ 3,565,299 $ 3,947,935 $ 3,253,145")
- Net cash provided by operating activities for fiscal 2025 was USD 5,008,434 thousand. (P154: "Net cash provided by (used in) operating activities 5,008,434 4,912,209 5,373,058")
- Net cash provided by operating activities was USD 5,008 million in 2025, compared with USD 4,912 million in 2024. (P110: "Net cash provided by (used in) operating activities $ 5,008 $ 4,912")
- KPMG expressed an unqualified opinion on the consolidated financial statements, dated February 13, 2026. (P146: "our report dated February 13, 2026 expressed an unqualified opinion on those consolidated financial statements")
- The critical audit matter was the assessment of the Operating Partnership's evaluation of the expected holding period for operating properties, with USD 80,561 million of operating properties as of December 31, 2025. (P144: "Assessment of the Operating Partnership’s evaluation of the expected holding period for operating properties As discussed in Notes 2 and 3 to the consolidated f")
- KPMG concluded the Company maintained effective internal control over financial reporting as of December 31, 2025. (P146: "In our opinion, the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")

## Red team

- [method, high, rating too high, supported] The DDM grows dividends at the revenue growth blend, but PLD's payout is already near the limit: $4.04 DPS against $3.57bn net earnings on ~950m shares leaves almost no retention, and REITs must distribute 90% of taxable income. Growth_used of 8% (the cap) is not fundable from retained cash; the model's own ddm note says growth should be tied to payout. (cites CAP-7, ACC-1, growth_used, ddm)
- [data_conflict, medium, rating too low, supported] The 10-Q shows accelerating momentum the 10-K-based blend misses: rental revenues +7.2% and NOI +6.6% in H1 2026, operating income up 37% to $2,462m, and Strategic capital revenues up 40% to $402m. Growth_used of 8% is at the cap, but the underlying trend supports the bull case rather than a fade. (cites PERF-5, PERF-6, PERF-7, PERF-8, PERF-9, growth_used)
- [business, medium, rating too low, supported] The rating ignores the balance-sheet and capital-recycling engine: debt rose to $35.0bn from $30.9bn funding $2.78bn of development and $1.80bn of acquisitions, while operating cash flow of $5.0bn comfortably covers the $4.04 dividend. Value creation comes from development yields, not the dividend stream the DDM capitalises. (cites CAP-3, CAP-5, CAP-6, CAP-4, CAP-7)
- [method, medium, rating too high, supported] The DDM discounts dividends at the CAPM cost of equity of 8.29%, but the beta build uses a bottom-up unlevered beta of 0.401 relevered to 0.855 while the regression beta is 1.209 — a 0.35 gap above the 0.3 guard. A higher beta raises the discount rate and lowers fair value; the desk's own beta_disagreement rule should have averaged them. (cites cost_of_equity, beta_disagreement, beta_method)

## Cost

61,902 tokens, $0.0098 across 9 model runs.

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
