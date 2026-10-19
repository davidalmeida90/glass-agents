# PGR: Sell

Desk memo, 2026-10-19. Price 218.49 (2026-10-16). Noise meter agreement 100% (Sell, Sell, Sell). Target weight 0.0%.

## Why

- price / base fair value 1.50 at Medium uncertainty (volatility 27%, range 0.63x base, DCF / industry multiples 1.01): Buy at or below 0.70, Overweight to 0.93, Underweight from 1.07, Sell from 1.35

## Valuation

Method: justified price-to-book on common equity: P/B = (ROE - g) / (cost of equity - g), cost of equity = risk-free + beta x ERP; bear/bull: ROE -/+2 points, cost of equity +/-0.5 points

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 80.45 | 145.53 | 172.34 | 1.50 |

- Industry check: Insurance (Prop/Cas.) P/B 2.02x at ROE 18.7%, ROE-adjusted 143.82 per share; model / multiples 1.012
- ROE 22.5% (5-year average; latest 34.1%); the price implies 23.7%; book value per share 59.06; cost of equity 9.9%; narrow: ROIC beat WACC on average over 5 years (+12.6%)


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total revenues for the six months ended June 30, 2026 were $45,797 million. (Q002: "Total revenues 23,609 22,004 45,797 42,413")
- Total revenues rose from $42,413 million to $45,797 million year over year for the six months ended June 30. (Q002: "Total revenues 23,609 22,004 45,797 42,413")
- Total expenses were $38,022 million against total revenues of $45,797 million for the six months ended June 30, 2026. (Q002: "Total expenses 19,400 18,022 38,022 35,195")
- Net income for the six months ended June 30, 2026 was $6,129 million, up from $5,742 million. (Q002: "Net income 3,311 3,175 6,129 5,742")
- Net cash provided by operating activities was $7,974 million for the six months ended June 30, 2026, versus $9,183 million a year earlier. (Q006: "Net cash provided by operating activities 7,974 9,183")
- Personal Lines net premiums earned were $37,264 million for the six months ended June 30, 2026, versus $34,254 million in 2025. (Q038: "Net premiums earned $ 37,264 $ 5,274 $ 3 $ 42,541")

**capital**
- Total investments at fair value were $97,373 million at December 31, 2025. (P107: "Total investments $ 93,947 $ 97,373 $ 97,373")
- Short-term investments totaled $10,005 million at December 31, 2025. (P107: "Short-term investments 10,005 10,005 10,005")
- The parent company held no cash at year-end 2025; cash at end of year was $0. (P110: "Cash – end of year $ 0 $ 0 $ 0")
- $13.0 billion of marketable securities were available in the non-insurance investment subsidiary at December 31, 2025. (P110: "At December 31, 2025, 2024, and 2023, $ 13.0 billion, $ 6.2 billion, and $ 4.2 billion, respectively, of marketable securities were available in this subsidiary")
- Parent company debt was $6,897 million at December 31, 2025, consisting solely of long-term debt. (P108: "Debt 1 6,897 6,893")
- The Board authorized repurchase of up to 25 million common shares in May 2025. (P098: "In May 2025, the Board of Directors approved an authorization for the company to repurchase up to 25 million of its common shares.")

**risks**
- Consolidations and strategic relationships in the independent agent channel in Personal Lines have increased competition and could continue to do so. (R000: "Consolidations and strategic relationships in the independent agent channel in our Personal Lines business have increased competition and could continue to do s")
- Inconsistencies in requirements among states, or between state and federal requirements, or changes in regulatory priorities or funding, may complicate compliance efforts and could impact participation in government funded programs such as the National Flood Insurance Program. (R000: "inconsistencies in requirements among the various states, or between state and federal requirements, or changes in regulatory priorities or funding, may further")
- Competitors or other third parties may be able to incorporate Advanced AI into their products and operations, or optimize or redesign their processes, more quickly or more successfully than the company. (R000: "our competitors or other third parties may be able to replace legacy systems, incorporate Advanced AI into their products and operations, or optimize or redesig")

**segments**
- Personal Lines premium revenue was USD 72,558 million in 2025 versus USD 63,470 million in 2024. (P112: "Personal Lines $ 70,778 $ 46,662 $ 5,070 $ 11,252 $ 72,558")
- Commercial Lines premium revenue was USD 10,613 million in 2025 versus USD 10,953 million in 2024. (P112: "Commercial Lines 10,881 7,296 1,026 1,279 10,613")

**accounting**
- Parent company condensed statement of cash flows reports net income of $11,308 million for 2025. (P109: "Net income $ 11,308 $ 8,480 $ 3,903")
- Parent company net cash provided by operating activities was $9,843 million in 2025. (P109: "Net cash provided by operating activities 9,843 3,519 236")
- Parent company net income was $11,308 million in 2025, up from $8,480 million in 2024. (P108: "Net income 11,308 8,480 3,903")
- The audit report on the consolidated financial statements is dated March 2, 2026 and was issued by the independent registered public accounting firm (PCAOB ID: 238). (P113: "Our audits of the consolidated financial statements referred to in our report dated March 2, 2026 appearing in the 2025 Annual Report to Shareholders of The Pro")
- Management's Report on Internal Control over Financial Reporting and the independent registered public accounting firm's attestation are incorporated by reference from the Annual Report. (P099: "Management’s Report on Internal Control over Financial Reporting and th")
- No change in internal control over financial reporting during the most recent fiscal quarter materially affected, or was reasonably likely to materially affect, internal control over financial reporting. (P100: "There have not been any changes in our internal control over financial reporting during our most recent fiscal quarter that has materially affected, or is reaso")

## Red team

- [business, medium, rating too low, supported] The desk's valuation uses an implied ROE of 23.7% and a cost of equity of 9.87%, which results in a base fair value of 145.53. However, the company's actual ROE has been significantly higher, with 2025 net income of $11,308 million on a substantial equity base. The desk's model underestimates the company's ability to generate excess returns. (cites ACC-1, ACC-3)
- [method, medium, rating too high, supported] The desk uses a beta of 0.642 for the insurance industry. Given the company's strong market position and historical performance, this beta likely underestimates the company's risk profile in a volatile insurance market, leading to an artificially low cost of equity and an inflated fair value. The rating should be more cautious. (cites RISK-1, RISK-3)

## Cost

64,531 tokens, $0.0131 across 9 model runs.

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
