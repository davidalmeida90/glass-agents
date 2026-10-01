# NEE: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- NEE total consolidated revenues for 2024 were $24,753 million. (P321: "Total consolidated revenues $ 24,753")
- NEE total consolidated revenues for 2023 were $28,114 million. (P322: "Total consolidated revenues $ 28,114")
- FPL segment operating revenues were $17,019 million in 2024. (P321: "Operating revenues $ 17,019 $ 7,542 $ 24,561")
- NEER segment operating revenues were $7,542 million in 2024. (P321: "Operating revenues $ 17,019 $ 7,542 $ 24,561")
- FPL segment operating revenues were $18,365 million in 2023. (P322: "Operating revenues $ 18,365 $ 9,672 $ 28,037")
- NEER segment operating revenues were $9,672 million in 2023. (P322: "Operating revenues $ 18,365 $ 9,672 $ 28,037")

**capital**
- NEE's cash, cash equivalents and restricted cash at end of 2025 was $3,006 million. (P190: "Cash, cash equivalents and restricted cash at end of year $ 3,006 $ 1,402 $ 3,420")
- NEE's long-term debt including current portion had a carrying amount of $93,056 million at December 31, 2025. (P260: "Long-term debt, including current portion $ 93,056 $ 91,614 (c) $ 80,446 $ 76,428 (c)")
- NEE issued $23,394 million of long-term debt, including premiums and discounts, in 2025. (P189: "Issuances of long-term debt, including premiums and discounts 23,394 24,769 13,857")
- NEE retired $10,347 million of long-term debt in 2025. (P189: "Retirements of long-term debt ( 10,347 ) ( 10,113 ) ( 7,978 )")
- NEE's capital expenditures, independent power and other investments and nuclear fuel purchases totaled $24,606 million in 2025. (P134: "Capital expenditures, independent power and other investments and nuclear fuel purchases (24,606) (24,729) (25,113)")
- NEE paid $4,680 million of dividends on common stock in 2025. (P190: "Dividends on common stock ( 4,680 ) ( 4,235 ) ( 3,782 )")

**risks**
- NEE and FPL's planned productivity increases and competitive advantages from AI technologies may not be realized, and reliance on AI may present risks that could materially adversely affect their business, financial condition, results of operations and prospects. (R000: "The productivity increases and competitive advantages NEE and FPL plan to achieve through the use of artificial intelligence (AI) technologies may not be realiz")
- NEE and FPL use AI technologies in various aspects of their operations, including financial analysis, strategic planning, field work intelligence, work scheduling, grid optimization, energy forecasting, customer service and operations management. (R000: "NEE and FPL use AI technologies in various aspects of their operations, including, without limitation, financial analysis, strategic planning, field work intell")
- AI tools may malfunction, produce inaccurate or biased outputs, or behave unpredictably, and introduce NEE and FPL to additional cybersecurity threats and data privacy risks. (R001: "AI tools may malfunction, produce inaccurate or biased outputs, or behave unpredictably, and introduce NEE and FPL to additional cybersecurity threats and data ")
- Because NEE and FPL rely on third-party vendors for certain AI tools, platforms and collaborations, they could experience vendor issues such as disruptions in vendor relationships, performance issues, cybersecurity threats or disputes over intellectual property rights. (R001: "NEE and FPL could experience third-party vendor issues such as disruptions in vendor relationships, performance issues, cybersecurity threats or disputes over i")
- The regulatory environment governing AI is evolving, and future legislation or agency rulemaking may impose new compliance obligations or restrict certain AI applications, increasing compliance costs, with failure resulting in regulatory enforcement, penalties or reputational harm. (R001: "the regulatory environment governing AI is also evolving, and future legislation or agency rulemaking may impose new compliance obligations or restrict certain ")
- NEER is actively pursuing the restart of the Duane Arnold nuclear generation facility, which is subject to regulatory approvals including NRC safety and environmental reviews and state and local permits, and failure to obtain approvals could result in impairment of amounts capitalized. (R000: "NEER is actively pursuing the restart of the Duane Arnold nuclear generation facility. The restart is subject to certain regulatory approvals, including NRC saf")

**accounting**
- Net income attributable to NEE for 2025 was $6.84 billion, down from $6.95 billion in 2024. (P120: "Net income attributable to NEE for 2025 was $6.84 billion compared to $6.95 billion in 2024.")
- NEE's consolidated statement of cash flows starts from net income of $5,332 million for 2025. (P188: "CASH FLOWS FROM OPERATING ACTIVITIES Net income $ 5,332 $ 5,698 $ 6,282")
- FPL's net cash provided by operating activities was $8,533 million in 2025. (P194: "Net cash provided by operating activities 8,533 8,506 8,296")
- Deloitte & Touche LLP expressed unqualified opinions on NEE's and FPL's consolidated financial statements for the year ended December 31, 2025. (P175: "our report dated February 13, 2026, expressed unqualified opinions on those financial statements")
- In the auditor's opinion, NEE and FPL maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P175: "In our opinion, NEE and FPL maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")
- Management believes NEE's and FPL's internal control over financial reporting was effective as of December 31, 2025. (P174: "management believes that NEE's and FPL's internal control over financial reporting was effective as of December 31, 2025")

## Cost

39,503 tokens, $0.0063 across 6 model runs.

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
