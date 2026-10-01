# CB: Underweight

Desk memo, 2026-10-01. Price 325.25 (2026-09-30). Noise meter agreement 100% (Underweight, Underweight, Underweight). Target weight 0.0%.

## Why

- price / base fair value 1.18 at Low uncertainty (volatility 19%, range 0.52x base, DCF / industry multiples 0.97): Buy at or below 0.80, Overweight to 0.95, Underweight from 1.05, Sell from 1.25

## Valuation

Method: justified price-to-book on common equity: P/B = (ROE - g) / (cost of equity - g), cost of equity = risk-free + beta x ERP; bear/bull: ROE -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 199.45 | 275.15 | 343.33 | 1.18 |

- Industry check: Insurance (Prop/Cas.) P/B 2.02x at ROE 18.7%, ROE-adjusted 282.39 per share; model / multiples 0.974
- ROE 13.7% (5-year average; latest 15.3%); the price implies 13.5%; book value per share 190.24; cost of equity 9.9%; narrow: ROIC beat WACC on average over 5 years (+3.9%)


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Chubb's net income for the year ended December 31, 2025 was $10,622 million. (P277: "Net income $ 10,622 $ 9,640 $ 9,015")
- Net cash flows from operating activities were $12,816 million in 2025. (P277: "Net cash flows from operating activities 12,816 16,182 12,632")
- Net cash flows from operating activities were $7,677 million for the six months ended June 30, 2026. (Q009: "Net cash flows from operating activities 7,677 5,117")
- Net cash provided by operating activities increased $2.6 billion in the 2026 year-to-date period. (Q146: "Net cash provided by operating activities increased $2.6 billion primarily due to higher net premiums collected")
- Parent-company-only total revenues were $10,452 million in 2025. (P489: "Total revenues 10,452 9,361 9,044")
- Parent-company-only net income attributable to Chubb was $10,310 million in 2025. (P489: "Net income attributable to Chubb $ 10,310 $ 9,272 $ 9,028")

**capital**
- Total financial debt was $17,227 million at December 31, 2025. (P221: "Short-term debt $ 1,499 $ 800 Long-term debt 15,728 14,379 Total financial debt 17,227 15,179")
- Short-term debt was $1,499 million and long-term debt was $15,728 million at December 31, 2025. (P221: "Short-term debt $ 1,499 $ 800 Long-term debt 15,728 14,379")
- Total hybrid debt was $422 million at December 31, 2025. (P221: "Trust preferred securities 309 309 Subordinated debt (1) 113 110 Total hybrid debt 422 419")
- The ratio of financial debt to total adjusted capitalization was 18.4% at December 31, 2025. (P222: "Ratio of financial debt and hybrid debt to total adjusted capitalization (2) (3) 18.8 % 18.5 %")
- Chubb established a commercial paper program in the second quarter of 2025 with the ability to borrow a total of $2.0 billion, and no commercial paper was outstanding as of December 31, 2025. (P421: "We have the ability to borrow a total of $ 2.0 billion, supported by our $ 3.0 billion group syndicated credit facility which expires in December 2030.")
- Shareholders approved an annual dividend for the following year of up to $3.88 per share, paid in four quarterly installments of $0.97 per share. (P440: "our shareholders approved an annual dividend for the following year of up to $ 3.88 per share, expected to be paid in four quarterly installments of $ 0.97 per ")

**risks**
- Capital requirements for the insurance subsidiaries are prescribed by applicable insurance regulators, while rating agencies set requirements that inform ratings. (R000: "Capital requirements for our insurance subsidiaries are prescribed by the applicable insurance regulators, while rating agencies establish requirements that inf")
- In any particular year, capital levels and risk-based capital requirements may increase or decrease depending on a variety of factors, including the mix of business written and correlation or diversification in the business profile. (R000: "In any particular year, capital levels and risk-based capital requirements may increase or decrease depending on a variety of factors including the mix of busin")
- Several nations in Asia are considering legislation or regulatory guidance. (R001: "Several nations in Asia are also considering legislation or regulatory guidance.")
- Bermuda operations are subject to taxation in Bermuda because of the newly effective Bermuda Corporate Income Tax Act. (R001: "Our Bermuda operations are subject to taxation in Bermuda because of the newly effective Bermuda Corporate Income Tax Act.")

**accounting**
- Chubb reported net income of $10,622 million for fiscal 2025. (P277: "Net income $ 10,622 $ 9,640 $ 9,015")
- Net cash flows from operating activities were $12,816 million in fiscal 2025. (P277: "Net cash flows from operating activities 12,816 16,182 12,632")
- Operating cash flows were $12.8 billion in 2025, compared to $16.2 billion in 2024. (P219: "Operating cash flows were $12.8 billion in 2025, compared to $16.2 billion in 2024.")
- PricewaterhouseCoopers LLP expressed an unqualified opinion that the consolidated financial statements present fairly, in all material respects, the financial position and results of operations and cash flows in conformity with accounting principles generally accepted in the United States of America. (P265: "In our opinion, the consolidated financial statements referred to above present fairly, in all material respects, the financial position of the Company as of De")
- The auditor stated that the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P266: "Also in our opinion, the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")
- Management concluded that Chubb's internal control over financial reporting was effective as of December 31, 2025. (P264: "management has concluded that Chubb's internal control over financial reporting was effective as of December 31, 2025")

## Red team

- [data_conflict, high, rating too low, supported] The desk's valuation uses an implied ROE of 13.5% for the excess return model, but Chubb's 2025 net income of $10,622M [PERF-1] on a book value of $190.24/share suggests a significantly higher ROE. The desk's ROE assumption is too conservative, leading to an undervalued fair price. (cites PERF-1, book_value_per_share, implied_roe)
- [business, medium, rating too high, supported] The desk uses an industry beta of 0.642, which is low for an insurer. Given the regulatory risks in Bermuda [RISK-4] and Asia [RISK-3], the cost of equity is likely higher than 9.87%, which would lower the fair value and justify a Sell rating rather than Underweight. (cites RISK-3, RISK-4, cost_of_equity)

## Cost

65,869 tokens, $0.0129 across 9 model runs.

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
