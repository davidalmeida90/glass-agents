# DUK: Sell

Desk memo, 2026-10-01. Price 114.21 (2026-09-29). Noise meter agreement 100% (Sell, Sell, Sell). Target weight 0.0%.

## Why

- price / base fair value 1.40 at Low uncertainty (volatility 16%, range 0.44x base): Buy at or below 0.80, Overweight to 0.95, Underweight from 1.05, Sell from 1.25
- red flag caps the rating at Underweight

## Valuation

Method: two-stage dividend discount: dividends per share grow at the revenue growth blend (bounded -5% to 8%) for 5 years, fading to terminal growth = risk-free rate, at the CAPM cost of equity; bear/bull growth -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 66.21 | 81.77 | 102.22 | 1.40 |

- Dividend per share 4.08 (yield 3.6%), growth 2.0% fading to 2.0%, cost of equity 7.1%


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Duke Energy's net income for fiscal year 2025 was USD 5,071 million. (P240: "Net Income $ 5,071 $ 4,614 $ 2,874")
- Net income available to Duke Energy Corporation common stockholders was USD 6.31 per basic and diluted share in 2025. (P240: "Net income available to Duke Energy Corporation common stockholders Basic and Diluted $ 6.31 $ 5.71 $ 3.54")
- Net income attributable to Duke Energy Corporation for the six months ended June 30, 2026 was USD 2,642 million. (Q016: "Net Income Attributable to Duke Energy Corporation 1,092 984 2,642 2,363")
- Net income for the six months ended June 30, 2026 was USD 2,722 million. (Q016: "Net Income 1,145 1,007 2,722 2,411")
- Net income available to Duke Energy common stockholders for the six months ended June 30, 2026 was USD 2,613 million. (Q183: "Net Income available to Duke Energy common stockholders $ 1,077 $ 971 $ 2,613 $ 2,336")
- Duke Energy Florida's operating revenues were USD 7,105 million in 2025 versus USD 6,595 million in 2024, a variance of USD 510 million. (P173: "Operating Revenues $ 7,105 $ 6,595 $ 510")

**capital**
- Duke Energy's cash, cash equivalents and restricted cash at end of period was $363 million. (P200: "Cash, cash equivalents and restricted cash at end of period $ 363")
- Duke Energy's cash, cash equivalents and restricted cash at beginning of period was $421 million. (P200: "Cash, cash equivalents and restricted cash at beginning of period 421 357")
- Net decrease in cash, cash equivalents and restricted cash was $58 million. (P200: "Net (decrease) increase in cash, cash equivalents and restricted cash (58) 64")
- Cash flows provided by operating activities were $12,330 million. (P200: "Operating activities $ 12,330 $ 12,328")
- Cash flows used in investing activities were $14,338 million. (P200: "Investing activities (14,338) (13,123)")
- Total long-term debt, including current maturities, was $86,865 million. (P448: "Total long-term debt, including current maturities $ 86,865")

**risks**
- AI, including generative AI, may be used to facilitate or perpetrate cybersecurity threats against Duke Energy. (R002: "Furthermore, AI, including generative AI, may be used to facilitate or perpetrate these cybersecurity threats.")
- Duke Energy's use of generative AI, and use by its vendors and agents, may subject it to data privacy, legal, regulatory and security risks. (R002: "Duke Energy’s use of generative AI (and use by their vendors and agents) may subject them to data privacy, legal, regulatory and security risks.")
- Advances in emerging technologies such as quantum computing could over time be used to break standard encryption methods and compromise secure connections. (R002: "advances in emerging technologies such as quantum computing could, over time, be used to break standa")
- Rising demand for electric infrastructure and international trade developments, including potential export controls on rare earth materials and technologies, may further constrain supply availability. (R002: "Rising demand for electric infrastructure and international trade developments, including potential export controls on certain rare earth materials and technolo")
- Federal legislation enacted in 2025 eliminated the long-term extension of certain residential solar tax credits, causing these incentives to expire after 2025. (R002: "Federal legislation enacted in 2025 eliminated the long‑term extension of certain residential solar tax credits, causing these incentives to expire after 2025")
- Emerging large loads such as hyperscale data centers and industrial facilities present unique risks due to high demand, rapid fluctuations and unpredictable operational profiles that can strain bulk power system reliability and grid stability. (R001: "emerging large loads – such as hyperscale data centers and industrial facilities – present unique risks due to their high demand, rapid fluctuations, and unpred")

**accounting**
- Duke Energy reported net income of $5,071 million for 2025. (P239: "Net Income 5,071 4,614 2,874")
- Net income attributable to Duke Energy Corporation was $4,968 million in 2025. (P239: "Net Income Attributable to Duke Energy Corporation 4,968 4,524 2,841")
- Net income available to Duke Energy Corporation common stockholders was $4,912 million in 2025. (P239: "Net Income Available to Duke Energy Corporation Common Stockholders $ 4,912 $ 4,402 $ 2,735")
- Net cash provided by operating activities was $893 million in 2025 for the subsidiary whose statements are shown. (P290: "Net cash provided by operating activities 893 905 506")
- The auditor states the company is not required to have, nor was the auditor engaged to perform, an audit of internal control over financial reporting, and expresses no such opinion. (P301: "The Company is not required to have, nor were we engaged to perform, an audit of its internal control over financial reporting.")
- A critical audit matter was communicated arising from the current-period audit of the financial statements. (P301: "The critical audit matter communicated below is a matter arising from the current-period audit of the financial statements")

## Red team

- [method, medium, rating too high, supported] The DDM grows dividends at the revenue growth blend (1.97%), but the payout is already ~67% of EPS ($4.22 vs $6.31) and the company funds a $14.3bn capex program against $12.3bn operating cash flow (CAP-5, CAP-4). Growth above the dividend's own history is unfunded; the model's own ddm rule caps growth at the company's dividend growth. (cites CAP-8, CAP-5, CAP-4, PERF-2)
- [method, medium, rating too low, supported] The cost of equity of 7.06% uses a bottom-up beta of 0.557 for a regulated utility with market D/E of 1.028 and a regression beta of 0.8. The regression cross-check is 44% higher; averaging the two (beta_disagreement guard) would raise the discount rate and cut fair value well below base, deepening the Sell. (cites cost_of_equity, beta_disagreement)
- [business, medium, rating too low, supported] Evidence shows revenue momentum the 1.97% growth_used ignores: Duke Energy Florida revenues rose $510m to $7,105m in 2025 (PERF-6), Ohio/Kentucky fuel revenues +$132m (PERF-7), Carolinas retail +$32m on weather (PERF-8), and data-center load risk (RISK-6) implies a rising rate base. Faster dividend growth would lift fair value toward the bull case. (cites PERF-6, PERF-7, PERF-8, RISK-6)
- [data_conflict, low, rating too high, supported] The valuation period is dividends paid over the twelve months to 2022-12-31, yet the evidence is fiscal 2025 (dividends declared $4.22, CAP-8). The DDM is anchored to a stale payout base three years before the 10-K, so the starting dividend and hence fair value may be understated or misaligned with the current business. (cites CAP-8, valuation_period)

## Cost

59,381 tokens, $0.0093 across 9 model runs.

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
