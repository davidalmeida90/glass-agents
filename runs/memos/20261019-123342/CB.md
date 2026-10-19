# CB: Sell

Desk memo, 2026-10-19. Price 359.79 (2026-10-16). Noise meter agreement 100% (Sell, Sell, Sell). Target weight 0.0%.

## Why

- price / base fair value 1.31 at Low uncertainty (volatility 20%, range 0.52x base, DCF / industry multiples 0.97): Buy at or below 0.80, Overweight to 0.95, Underweight from 1.05, Sell from 1.25

**Audit:** only 33 of 42 claims check out against the filing

## Valuation

Method: justified price-to-book on common equity: P/B = (ROE - g) / (cost of equity - g), cost of equity = risk-free + beta x ERP; bear/bull: ROE -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 199.45 | 275.15 | 343.33 | 1.31 |

- Industry check: Insurance (Prop/Cas.) P/B 2.02x at ROE 18.7%, ROE-adjusted 282.39 per share; model / multiples 0.974
- ROE 13.7% (5-year average; latest 15.3%); the price implies 14.4%; book value per share 190.24; cost of equity 9.9%; narrow: ROIC beat WACC on average over 5 years (+3.9%)


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Consolidated net income for the year ended December 31, 2025 was $10,622 million. (P277: "Net income $ 10,622 $ 9,640 $ 9,015")
- Net cash flows from operating activities were $12,816 million in 2025, down from $16,182 million in 2024. (P277: "Net cash flows from operating activities 12,816 16,182 12,632")
- Net cash provided by operating activities for the six months ended June 30, 2026 was $7,677 million versus $5,117 million in 2025. (Q145: "Net cash provided by operating activities $ 7,677 $ 5,117")
- Net cash provided by operating activities increased $2.6 billion, primarily due to higher net premiums collected, lower net losses paid, and higher net investment income collected. (Q146: "Net cash provided by operating activities increased $2.6 billion primarily due to higher net premiums collected, lower net losses paid, and higher net investmen")
- The six business segments are North America Commercial P&C Insurance, North America Personal P&C Insurance, North America Agricultural Insurance, Overseas General Insurance, Global Reinsurance, and Life Insurance. (P161: "We operate through six business segments: North America Commercial P&C Insurance, North America Personal P&C Insurance, North America Agricultural Insurance, Ov")
- Policy benefits were $5,460 million in 2025 and $4,714 million in 2024, with the increase primarily due to growth in international life operations. (P161: "Policy benefits were $5,460 million and $4,714 million in 2025 and 2024, respectively.")

**capital**
- Chubb reported short-term debt of $1,499 million at December 31, 2025. (P221: "Short-term debt $ 1,499 $ 800")
- Chubb reported long-term debt of $15,728 million at December 31, 2025. (P221: "Long-term debt 15,728 14,379")
- Total financial debt was $17,227 million at December 31, 2025. (P221: "Total financial debt 17,227 15,179")
- Total hybrid debt was $422 million at December 31, 2025. (P221: "Total hybrid debt 422 419")
- Ratio of financial debt to total adjusted capitalization was 18.8% at December 31, 2025. (P222: "Ratio of financial debt and hybrid debt to total adjusted capitalization (2) (3) 18.8 % 18.5 %")
- Total investments other than investments in related parties were $170,225 million at December 31, 2025. (P488: "Total investments - other than investments in related parties $ 170,225 $ 168,265 $ 168,231")

**risks**
- Capital requirements for insurance subsidiaries are set by insurance regulators while rating agencies set requirements informing ratings, and can vary significantly over time. (R000: "The amount of capital that our insurance subsidiaries have and must hold to maintain their financial strength and credit ratings and meet other requirements can")
- Insurance regulators and rating agencies evaluate company capital through financial models calculating minimum capitalization requirements based on risk-based capital formulas. (R000: "Insurance regulators and rating agencies evaluate company capital through financial models that calculate minimum capitalization requirements based on risk-base")
- In any particular year, capital levels and risk-based capital requirements may increase or decrease depending on a variety of factors. (R000: "In any particular year, capital levels and risk-based capital requirements may increase or decrease depending on a variety of factors")
- Regulatory agencies and self-regulatory organizations have broad rulemaking and enforcement powers, including the power to limit or restrict the business for failure to comply with applicable laws and regulations. (R001: "as well as the power to limit or restrict our business for failure to comply with applicable laws and regulations")
- Several nations in Asia are considering legislation or regulatory guidance. (R001: "Several nations in Asia are also considering legislation or regulatory guidance.")
- Bermuda operations are subject to taxation in Bermuda because of the newly effective Bermuda Corporate Income Tax Act. (R001: "Our Bermuda operations are subject to taxation in Bermuda because of the newly effective Bermuda Corporate Income Tax Act.")

**segments**
- North America Agricultural Insurance net premiums earned were $2,705 million in 2025 versus $3,169 million in 2023. (P477: "Net premiums earned 20,008 6,188 2,705 13,400 1,272 6,273 49,846")

**accounting**
- Net income for 2025 was USD 10,622 million. (P277: "Cash flows from operating activities Net income $ 10,622 $ 9,640 $ 9,015")
- Net cash flows from operating activities for 2025 were USD 12,816 million. (P277: "Net cash flows from operating activities 12,816 16,182 12,632")
- Operating cash flows were USD 12.8 billion in 2025, compared to USD 16.2 billion in 2024, a decrease of USD 3.4 billion. (P219: "Operating cash flows were $12.8 billion in 2025, compared to $16.2 billion in 2024. The decrease of $3.4 billion is primarily due to higher net losses, expenses")
- PwC's opinion states the consolidated financial statements present fairly, in all material respects, the financial position, results of operations and cash flows in conformity with accounting principles generally accepted in the United States of America. (P265: "In our opinion, the consolidated financial statements referred to above present fairly, in all material respects, the financial position of the Company as of De")
- The auditor opined that the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P266: "Also in our opinion, the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")
- Management concluded that Chubb's internal control over financial reporting was effective as of December 31, 2025. (P264: "management has concluded that Chubb's internal control over financial reporting was effective as of December 31, 2025")

## Red team

- [data_conflict, medium, rating too low, supported] The desk's valuation uses an implied ROE of 14.43% and a cost of equity of 9.87%. However, the company's 2025 net income of $10.622 billion (PERF-1) on a book value of $190.24 per share suggests a significantly higher ROE potential, especially given the strong growth in operating cash flows in 2026 (PERF-3). The rating is too low. (cites PERF-1, PERF-3)
- [business, medium, rating too high, supported] The desk uses a beta of 0.642 for an insurance company. Given the regulatory risks mentioned in RISK-1 and RISK-4, and the potential for increased capital requirements, this beta likely underestimates the company's risk profile. A higher cost of equity would lower the fair value, supporting a Sell rating, but the current valuation may be overly optimistic on risk. (cites RISK-1, RISK-4)

## Cost

81,229 tokens, $0.0160 across 9 model runs.

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
| red_team_model | google/gemini-3.1-flash-lite | deliberation helps only across different models (Schneider and Schramm 2025); voting explains most debate gains among copies of one model (Choi, Zhu, Li, NeurIPS 2025) | no |
| margin_correction_band | 0.3 | own rule after Visa, 2026-10-01: operating expenses / revenue (32%) was submitted as the operating margin (reported 61%) and cost a notch in one repeat | no |
| forward_drivers | {'guidance_weight': 0.5, 'guidance_cap': 0.05, 'mix_horizon': 5, 'segment_growth_bounds': (-0.1, 0.4), 'mix_ratio_bounds': (0.67, 1.5), 'segment_coverage': (0.7, 1.3), 'margin_years': 5} | anchor and adjust on verified guidance (CAME, Wu et al., EMNLP 2026); Damodaran's Ginzu target operating margin by a convergence year | no |
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
| financial_ke_floor | industry_implied | found on the 2026-10-01 run by the multiples cross-check; insurers' low market betas understate risk the market prices (catastrophe and reserve risk) | no |
| financial_moat_cap | 0.5 | Damodaran fades financial firms' excess returns toward the cost of equity | no |
| normalized_financial_roe | True | Damodaran: normalize earnings for cyclical firms | no |
| utility_model | {'growth_bounds': (0.0, 0.07), 'signal_range': (-0.05, 0.15), 'max_age_days': 456} | practice: utilities are valued on rate base growth and allowed ROE (NARUC ratemaking; Damodaran's DDM with payout tied to growth and ROE); Duke guides 5 to 7% EPS growth against a 2% dividend trend | no |
| ddm | {'stage1_years': 5, 'growth_bounds': (-0.05, 0.08), 'bear_bull': (0.02, 0.005)} | Damodaran, dividend discount models for REITs and utilities | no |
| sanity | {'fair_to_price': (0.25, 4.0), 'wacc': (0.05, 0.15), 'terminal_share': 0.95} | own choice | no |
| rating_bands | {'Low': (0.8, 1.25), 'Medium': (0.7, 1.35), 'High': (0.6, 1.55), 'Very High': (0.5, 1.75), 'Extreme': (0.25, 4.0)} | Morningstar star rating bands (methodology, Sept 2022) | no |
| multiples_check | {'agree': (0.67, 1.5)} | practice: analysts triangulate DCF with relative value; Damodaran vebitda.xls industry averages | no |
| multiples_check_financials | roe_adjusted_pbv | Damodaran pbvdata.xls industry averages (January 2026); P/B scales with ROE | no |
| uncertainty | {'volatility': (0.2, 0.3, 0.45, 0.6), 'range_overlay': 1.5} | Morningstar starts from return volatility and adds an analyst overlay; the thresholds here are own choice | no |
