# JPM: Hold

Desk memo, 2026-10-01. Price 334.98 (2026-09-29). Noise meter agreement 100% (Hold, Hold, Hold). Target weight 0.0%.

## Why

- price / base fair value 1.06 at Medium uncertainty (volatility 23%, range 0.80x base, DCF / industry multiples 1.20): Buy at or below 0.70, Overweight to 0.93, Underweight from 1.07, Sell from 1.35

## Valuation

Method: justified price-to-book on common equity: P/B = (ROE - g) / (cost of equity - g), cost of equity = risk-free + beta x ERP; bear/bull: ROE -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 165.04 | 316.61 | 419.85 | 1.06 |

- Industry check: Bank (Money Center) P/B 1.62x at ROE 12.9%, ROE-adjusted 264.95 per share; model / multiples 1.195
- ROE 14.9% (5-year average; latest 17.0%); the price implies 12.2%; book value per share 140.92; cost of equity 7.9%; narrow: ROIC beat WACC on average over 5 years (+7.0%)


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total net revenue for fiscal 2025 was $182,447 million. (P130: "Total net revenue $ 182,447 $ 177,556 (g) $ 158,104")
- Total net revenue for fiscal 2024 was $177,556 million. (P130: "Total net revenue $ 182,447 $ 177,556 (g) $ 158,104")
- Total net revenue grew from $177,556 million in 2024 to $182,447 million in 2025. (P130: "Total net revenue $ 182,447 $ 177,556 (g) $ 158,104")
- Pre-provision profit for fiscal 2025 was $86,807 million. (P130: "Pre-provision profit (a) 86,807 85,759 70,932")
- Net income for fiscal 2025 was $57,048 million. (P130: "Net income $ 57,048 $ 58,471 $ 49,552")
- Net income for fiscal 2024 was $58,471 million. (P130: "Net income $ 57,048 $ 58,471 $ 49,552")

**capital**
- Cash and due from banks and deposits with banks decreased by $125,979 million in 2025. (P159: "Net increase/(decrease) in cash and due from banks and deposits with banks $ (125,979) $ (154,834) $ 56,917")
- Total assets were $4,424,900 million at December 31, 2025. (P154: "Total assets $ 4,424,900 $ 4,002,814 11 %")
- Investment securities, net of allowance for credit losses, were $777,332 million at December 31, 2025. (P154: "Investment securities, net of allowance for credit losses 777,332 681,320 14")
- Proceeds from long-term borrowings were $120,761 million in 2025. (P412: "Proceeds from long-term borrowings 120,761 109,915 75,417")
- Payments of long-term borrowings were $108,100 million in 2025. (P412: "Payments of long-term borrowings ( 108,100 ) ( 96,605 ) ( 64,880 )")
- The Firm repurchased 114.4 million common shares for an aggregate purchase price of $31,640 million in 2025. (P246: "Total number of shares of common stock repurchased 114.4 91.7 69.5 Aggregate purchase price of common stock repurchases (a) $ 31,640 $ 18,841 $ 9,898")

**risks**
- New risk factor states that if JPMorganChase does not keep pace with rapidly changing technological advances, including the adoption of generative AI, it risks losing clients and market share to competitors. (R013: "s, including the adoption of generative AI, it risks losing clients and market share to competitors, which could negatively impact revenues, operating costs and")
- New risk factor describes risks from rapid development and deployment of advanced technologies, including generative and agentic AI systems, such as AI system failures, inappropriate use, lack of transparency, and inaccurate or biased output. (R013: "The rapid development and deployment of advanced technologies, including generative and agentic AI systems, present a range of risks to JPMorganChase’s business")
- New risk factor states that AI systems, particularly agentic systems, increase exposure to cyber attacks, system manipulation, or data loss if not designed and implemented with appropriate safeguards. (R014: "increased exposure to cyber attacks, system manipulation, or data loss if AI systems, particularly agentic systems, are not designed and implemented with approp")
- New risk factor states that intensified AI-enabled cyber threats may allow malicious actors to exploit vulnerabilities, reverse-engineer security patches, and conduct sophisticated social engineering attacks. (R014: "intensified AI-enabled cyber threats, which may allow malicious actors to exploit vulnerabilities, reverse-engineer security patches, and conduct sophisticated ")
- New risk factor states that competitive disadvantage could arise if competitors deploy AI more quickly or effectively, potentially resulting in a loss of market share. (R014: "competitive disadvantage if competitors are able to deploy AI more quickly or effectively, potentially gaining advantages in cost efficiency, client and custome")
- New risk factor states that AI agents autonomously managing or intermediating financial decisions or product selection could cause replacement or disintermediation of direct customer relationships. (R014: "replacement or disintermediation of direct customer relationships if AI agents autonomously manage or intermediate financial decisions and product selection")

**accounting**
- JPMorgan Chase reported net income of $57,048 million for the year ended December 31, 2025. (P411: "Net income $ 57,048 $ 58,471 $ 49,552")
- Net cash used in operating activities was $147,782 million for the year ended December 31, 2025. (P411: "Net cash (used in)/provided by operating activities ( 147,782 ) ( 42,012 ) 12,974")
- Consolidated net cash used in operating activities was $147,782 million in 2025, versus $42,012 million used in 2024. (P159: "Operating activities $ (147,782) $ (42,012) $ 12,974")
- PricewaterhouseCoopers LLP opined that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations and cash flows in conformity with U.S. GAAP. (P397: "In our opinion, the consolidated financial statements referred to above present fairly, in all material respects, the financial position of the Firm as of Decem")
- The auditor opined that the Firm maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P397: "Also in our opinion, the Firm maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")
- Management concluded that internal control over financial reporting was effective as of December 31, 2025 and determined there were no material weaknesses. (P396: "management concluded that as of December 31, 2025, JPMorganChase’s internal control over financial reporting was effective based upon the COSO 2013 framework. A")

## Red team

- [data_conflict, high, rating too low, supported] The model starts ROE at 14.9% (roe) but the bank model's own rule, normalized_financial_roe, requires a 5-year average. The 10-K shows net income falling from $58,471m (PERF-6) to $57,048m (PERF-5), and the latest six months jumped to $37,649m from $29,630m (PERF-9, PERF-10) — a run-rate well above the trailing figure. Using the depressed trailing ROE understates the excess-return stream. (cites PERF-5, PERF-6, PERF-9, PERF-10, roe, normalized_financial_roe)
- [method, medium, rating too low, supported] The excess-return model fades ROE to Ke plus only financial_moat_cap (0.5) of today's spread, and terminal_excess_return is set from ROIC history. For a money-center bank with a durable franchise, halving the spread plus a 4.75% terminal growth cap (terminal_growth) mechanically compresses fair value; the base 316.61 sits barely above price, so any less aggressive fade flips the rating to Overweight. (cites financial_moat_cap, terminal_excess_return, terminal_growth, fair_value)
- [method, medium, rating too high, unsupported] The cost of equity of 7.9% uses an industry levered beta of 0.761 (capital), far below the company's own regression beta of 1.018. For a bank whose earnings are levered to credit and rates, the low bottom-up beta understates risk; at beta 1.018 the cost of equity is ~8.96%, cutting fair value and pushing price/base toward Underweight. (cites capital, cost_of_equity, beta_disagreement, fair_value)
- [business, medium, rating too high, supported] The rating ignores the 10-K's new AI and cyber risk factors (RISK-1 to RISK-6): disintermediation of financial decisions by AI agents and AI-enabled attacks threaten the franchise that justifies any excess return above Ke. Combined with the allowance-for-loan-losses critical audit matter (ACC-8), the terminal moat assumption looks optimistic. (cites RISK-1, RISK-5, RISK-6, ACC-8)

## Cost

74,501 tokens, $0.0117 across 9 model runs.

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
