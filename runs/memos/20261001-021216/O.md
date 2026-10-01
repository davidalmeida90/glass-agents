# O: Buy

Desk memo, 2026-10-01. Price 55.14 (2026-09-29). Noise meter agreement 100% (Buy, Buy, Buy). Target weight 7.5%.

## Why

- price / base fair value 0.80 at Low uncertainty (volatility 16%, range 0.46x base): Buy at or below 0.80, Overweight to 0.95, Underweight from 1.05, Sell from 1.25

## Valuation

Method: two-stage dividend discount: dividends per share grow at the revenue growth blend (bounded -5% to 8%) for 5 years, fading to terminal growth = risk-free rate, at the CAPM cost of equity; bear/bull growth -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 55.53 | 69.11 | 87.18 | 0.80 |

- Dividend per share 3.17 (yield 5.7%), growth 2.7% fading to 2.7%, cost of equity 7.4%


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total revenue for fiscal 2025 was $5,749,377 thousand, up from $5,271,142 thousand in 2024. (P117: "Total revenue $ 5,749,377 $ 5,271,142 $ 478,235")
- Total revenue increased by $478,235 thousand in fiscal 2025 versus 2024. (P117: "Total revenue $ 5,749,377 $ 5,271,142 $ 478,235")
- Rental revenue (excluding reimbursements) was $5,096,934 thousand in fiscal 2025, an increase of $356,274 thousand. (P117: "Total $ 5,096,934 $ 4,740,660 $ 356,274")
- Same store rental revenue increased 1.3% for the year ended December 31, 2025 versus 2024. (P117: "The same store rental revenue percentage increased by 1.3% for the year ended December 31, 2025 as compared to the same period in 2024.")
- Total expenses were $4,785,982 thousand in fiscal 2025 against total revenue (excluding client reimbursements) of $5,408,979 thousand. (P120: "Total expenses $ 4,785,982 $ 4,489,294 $ 296,688")
- General and administrative expenses were 3.7% of total revenue (excluding client reimbursements) in fiscal 2025. (P120: "General and administrative expenses as a percentage of total revenue (1) 3.7 % 3.6 %")

**capital**
- Cash, cash equivalents and restricted cash at end of period was $520,756 thousand. (P158: "Cash, cash equivalents and restricted cash, end of period $ 520,756 $ 495,506 $ 292,175")
- Total outstanding borrowings of credit facilities, commercial paper, term loans, mortgages payable, and senior unsecured notes and bonds were $29.1 billion. (P105: "our total outstanding borrowings of credit facilities, commercial paper, term loans, mortgages payable, and senior unsecured notes and bonds were $29.1 billion")
- Approximately 93% of total debt was fixed rate debt. (P105: "approximately 93% of our total debt was fixed rate debt")
- Total outstanding unsecured senior debt securities were $25.3 billion. (P070: "we also had a total of $25.3 billion of outstanding unsecured senior debt securities")
- Cash distributions to common stockholders were $2,920,895 thousand. (P157: "Cash distributions to common stockholders ( 2,920,895 ) ( 2,691,719 ) ( 2,111,793 )")
- Dividends paid per share during the year ended December 31, 2025 totaled $3.2170. (P095: "The dividends paid per share during the year ended December 31, 2025 totaled $3.2170, as compared to $3.1255 during the year ended December 31, 2024")

**risks**
- The company's reliance on innovation in IT and its use of or inability to adopt new technological capabilities, including artificial intelligence and machine learning, may put it at a competitive disadvantage. (R010: "our use of or inability to adopt and deliver new technological capabilities and enhancements in line with strategic objectives, including artificial intelligenc")
- The use of emerging technologies, including artificial intelligence, entails risks including intellectual property infringement or misappropriation, data privacy, potential for inaccuracy, bias, and new or enhanced governmental or regulatory scrutiny. (R010: "The use of emerging technologies, including artificial intelligence, entails risks including risks relating to the possibility of intellectual property infringe")
- Instability and unpredictability caused by weakened institutional oversight and inconsistent regulatory enforcement can introduce legal and operational uncertainty that may hinder the company's ability to plan, operate and invest effectively. (R011: "The instability and unpredictability caused by weakened institutional oversight and inconsistent regulatory enforcement can introduce legal and operational unce")
- The industries in which the company's clients operate may be directly adversely affected by inconsistent or abrupt regulatory or legal changes, such as shifts in commercial regulations, labor laws and policies or sector-specific compliance requirements. (R011: "the industries in which our clients operate may be directly adversely affected by inconsistent or abrupt regulatory or legal changes that impact their businesse")
- As the company's business has evolved and the scope and complexity of its operations and transactions have increased, including through mergers, acquisitions, development opportunities, dispositions, joint ventures, co-investment ventures, private capital transactions, debt investments, funds and other strategic transactions, it may be subject to an increased risk of litigation and other claims. (R009: "As our business has evolved and the scope and complexity of our operations and transactions have increased, including through mergers, acquisitions, development")
- The company may face extensive regulations from gaming and other regulatory authorities regarding current and future gaming properties. (R006: "We may face extensive regulations from gaming and other regulatory authorities regarding current and future gaming properties.")

**accounting**
- Net income for fiscal 2025 was $1,069,783 thousand. (P156: "Net income $ 1,069,783 $ 867,341 $ 876,914")
- Net cash provided by operating activities for fiscal 2025 was $3,994,754 thousand. (P157: "Net cash provided by operating activities 3,994,754 3,573,276 2,958,769")
- KPMG expressed an unqualified opinion that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations in conformity with U.S. GAAP. (P145: "In our opinion, the consolidated financial statements present fairly, in all material respects, the financial position of the Company as of December 31, 2025 an")
- The critical audit matter was the assessment of the expected holding period for long-lived assets, whose real estate and lease intangibles were $59.1 billion as of December 31, 2025. (P147: "Assessment of the expected holding period for long-lived assets ... which were $59.1 billion as of December 31, 2025")
- The auditor concluded the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P149: "In our opinion, the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")
- The auditor's report on internal control over financial reporting was dated February 24, 2026 and expressed an unqualified opinion on its effectiveness. (P145: "our report dated February 24, 2026 expressed an unqualified opinion on the effectiveness of the")

## Red team

- [method, high, rating too high, supported] A dividend discount model is the wrong tool for a REIT that pays out only ~$2.92bn of $3.99bn operating cash flow while investing $4.65bn in real estate (CAP-5, CAP-8, PERF-8). Value is created by retained capital compounding, not by the dividend stream; DDM structurally understates intrinsic value and the desk's own method_routes assigns dividend_discount to REITs by convention, not by economics. (cites CAP-5, CAP-8, PERF-8, model_routes)
- [method, high, rating too low, supported] The DDM caps stage-1 dividend growth at 8% and forces terminal growth to the 4.75% risk-free rate, yet the company's dividend is only ~$3.22/share against $1.06bn net income and $3.99bn operating cash flow (CAP-6, PERF-7, PERF-8). Payout is far below earnings, so the model's growth ceiling is an artificial constraint that suppresses fair value; a REIT growing dividends from a low payout should be valued higher. (cites CAP-6, PERF-7, PERF-8, ddm)
- [data_conflict, medium, rating too high, supported] growth_used of 2.73% blends TTM revenue growth with the 3-year CAGR, but same-store rental revenue grew only 1.3% in fiscal 2025 (PERF-4) and total revenue growth was 9.1% (PERF-1, PERF-2). The blend masks that organic same-store growth is barely above inflation, so the starting growth rate may be too generous for a REIT whose core rental base is nearly flat. (cites PERF-4, PERF-1, PERF-2, growth_used)
- [business, medium, rating too low, supported] The company carries $29.1bn of debt, 93% fixed rate, against $520.8m cash (CAP-2, CAP-3, CAP-1). In a falling-rate environment the fixed-rate book is a refinancing tailwind, and the DDM's cost of equity of 7.44% with a 0.65 beta may overstate the discount rate for a low-volatility (16%) REIT, understating fair value. (cites CAP-2, CAP-3, CAP-1, cost_of_equity)

## Cost

60,476 tokens, $0.0095 across 9 model runs.

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
