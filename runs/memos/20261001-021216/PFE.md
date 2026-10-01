# PFE: Hold

Desk memo, 2026-10-01. Price 28.72 (2026-09-29). Noise meter agreement 67% (Hold, Hold, Underweight). Target weight 0.0%.

## Why

- price / base fair value 1.54 at High uncertainty (volatility 23%, range 1.17x base, DCF / industry multiples 0.48): Buy at or below 0.60, Overweight to 0.90, Underweight from 1.11, Sell from 1.55
- red team correction {'growth': 0.04}: base value 28.42, P/FV 1.01

## Valuation

Method: FCFF DCF at company WACC (maturing toward beta 1 from above): trailing revenue growth held 5 years if at most 10%, otherwise decaying to 10% by year 5, then fading to terminal growth = risk-free rate over 5 years; reinvestment = change in revenue / operating sales-to-capital; SBC expensed; R&D capitalized where material; leases as debt; terminal ROIC keeps the moat share (from 5-year ROIC history) of today's excess return; bear/base/bull shift growth -/+4 points, margin -/+10% relative, WACC +/-0.5 points, moat share 0/history/1

| Bear | Base | Bull | Price / base |
|---:|---:|---:|---:|
| 12.22 | 18.67 | 34.08 | 1.54 |

| Cost of capital | Value |
|---|---:|
| Risk-free (2026-09-01 (rate in Damodaran's ERP computation)) | 4.8% |
| Beta (Drugs (Pharmaceutical); regression 0.8) | 0.996 |
| Equity risk premium | 4.1% |
| Cost of equity | 8.9% |
| Synthetic rating (coverage 5.12) | A |
| Cost of debt, pre-tax | 5.5% |
| Equity weight | 71.4% |
| **WACC** (maturing to 7.5%) | **7.5%** |

- Revenue growth: last twelve months -0.2%, 3-year CAGR -14.8%, blend -7.5% (used -5.0%); the price implies 4.2%
- Operating margin 24.7% (reported 21.7% + R&D adjustment 3.0%), ROIC 7.9%, sales-to-capital 0.795, SBC 1.5% of revenue
- Moat: only 0 years of ROIC history: narrow by default
- Industry multiples check: Drugs (Pharmaceutical) EV/EBIT 20.3x gives 39.14 per share; DCF / multiples 0.477
- Terminal value 41.7% of enterprise value; EV/EBIT at base 10.4x vs market 14.1x
- Period: trailing twelve months to 2026-06-28 (revenue growth: twelve months to 2026-06-28 vs to 2025-06-29), from 10-K and 10-Q XBRL; the readers' evidence comes from the latest 10-K only

Base value per share, WACC by terminal growth:

| | g -0.5% | g +0.0% | g +0.5% |
|---|---:|---:|---:|
| wacc -1.0% | 19.65 | 19.95 | 20.30 |
| wacc +0.0% | 18.39 | 18.67 | 19.00 |
| wacc +1.0% | 17.21 | 17.47 | 17.78 |

- Data note: EBIT built as pre-tax income - NonoperatingIncomeExpense (no OperatingIncomeLoss)
- Data note: R&D capitalized over 10 years: research asset 55.9B, EBIT +1.9B (R&D 11.1B - amortization 9.1B)

## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total revenues were $62.6 billion in 2025. (P163: "Total revenues decreased $1.0 billion, or 2%, to $62.6 billion in 2025 from $63.6 billion in 2024")
- Total revenues decreased 2% in 2025, reflecting an operational decrease of 2%, partially offset by favorable foreign exchange of $247 million. (P163: "reflecting an operational decrease of $1.3 billion, or 2%, partially offset by a favorable impact of foreign exchange of $247 million")
- Excluding Comirnaty and Paxlovid, total revenues increased 6% operationally in 2025. (P163: "Excluding contributions from Comirnaty and Paxlovid, Total revenues increased 6% operationally.")
- Net income before allocation to noncontrolling interests was $7,812 million in 2025. (P239: "Net income before allocation to noncontrolling interests $ 7,812 $ 8,062 $ 2,158")
- Net cash provided by operating activities was $11,704 million in 2025. (P240: "Net cash provided by/(used in) operating activities 11,704 12,744 8,700")
- 2025 net cash flow from operations was $11.7 billion, a decrease of 8% compared to 2024. (P158: "2025 Net Cash Flow from Operations––$11.7 billion A decrease of 2% compared to 2024 A decrease of 8% compared to 2024")

**capital**
- Total short-term investments were $12,454 million as of December 31, 2025. (P315: "Total Short-term investments $ 12,454 $ 19,434")
- Short-term available-for-sale debt securities were $9,183 million as of December 31, 2025. (P315: "Available-for-sale debt securities 9,183 10,881")
- The carrying value of long-term debt, excluding the current portion, was $62 billion as of December 31, 2025. (P315: "The carrying value of Long-term debt, excluding the current portion, was $ 62 billion as of December 31, 2025")
- Remaining share-purchase authorization was $3.3 billion as of December 31, 2025, with no repurchases in 2025. (P222: "As of December 31, 2025, our remaining share-purchase authorization was $3.3 billion with no repurchases in 2025.")
- The Board declared a first-quarter dividend of $0.43 per share on December 12, 2025, payable March 6, 2026. (P222: "On December 12, 2025, our BOD declared a first-quarter dividend of $0.43 per share, payable on March 6, 2026")
- Cash dividends declared on common stock were $9,577 million in 2024 at $1.69 per share. (P238: "Cash dividends declared, per share: $ 1.69 Common stock ( 9,577 )")

**risks**
- Pfizer's future results could be adversely affected by changes in laws, regulations or policies or their interpretation, including new or changes in accounting standards, tariffs, tax laws and regulations internationally and in the U.S. (R000: "Our future results could be adversely affected by changes in laws, regulations or policies, or their interpretation, including, among others, new or changes in ")
- The OBBBA is cited as a law whose changes could affect Pfizer and is still subject to further guidance. (R000: "including, without limitation, the IRA, and the OBBBA, which is still subject to further guidance")
- Global minimum taxation requirements outside the U.S. have generally been effective in most jurisdictions since January 1, 2024. (R000: "the adoption of global minimum taxation requirements outside the U.S. generally effective in most jurisdictions since January 1, 2024")
- Government cost-cutting measures and related impacts on government staffing, resources and ability to timely review and process regulatory or other submissions could affect Pfizer. (R000: "government cost-cutting measures and related impacts on, among other matters, government staffing, resources and ability to timely review and process regulatory")
- Restrictions related to certain data transfers, including data security, data localization and cross border data transfer regulations, and transactions involving certain countries, are cited as risks. (R000: "restrictions related to certain data transfers, including data security, data localization and cross border data transfer regulations, and transactions involvin")
- The EU Data Act and the EU Health Data Space Regulation are among the EU legislative initiatives that may affect Pfizer's business. (R001: "Data Act, and the EU Health Data Space Regulation, among others.")

**accounting**
- Net income before allocation to noncontrolling interests was USD 7,812 million in 2025. (P239: "Net income before allocation to noncontrolling interests $ 7,812 $ 8,062 $ 2,158")
- Net cash provided by operating activities was USD 11,704 million in 2025. (P240: "Net cash provided by/(used in) operating activities 11,704 12,744 8,700")
- KPMG expressed an unqualified opinion on the consolidated financial statements, dated February 26, 2026. (P405: "our report dated February 26, 2026 expressed an unqualified opinion on those consolidated financial statements")
- A critical audit matter involved the liability for unrecognized tax positions, including interpretation of tax law and estimation of gross unrecognized tax benefits. (P232: "We evaluated the design and tested the operating effectiveness of an internal control over the Company’s liability for unrecognized tax position process")
- A critical audit matter involved evaluation of product liability and other product-related litigation. (P232: "Evaluation of product liability and other product-related litigation")
- The auditor concluded the Company maintained effective internal control over financial reporting as of December 31, 2025. (P404: "In our opinion, the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")

## Red team

- [data_conflict, high, rating too high, supported] The desk's growth_used of -5% is contradicted by the 10-K's own ex-Comirnaty/Paxlovid base business, which grew 6% operationally in 2025 (PERF-3), and by 4% growth in H1 2026 (PERF-7). The decline is two COVID products rolling off, not the franchise. A -5% start understates the ongoing business. (cites PERF-3, PERF-7, PERF-2)
- [method, medium, rating too low, supported] growth_bounds clips the starting blend at -5%, and growth_blend averages TTM with a 3-year CAGR that still contains the 2022-23 COVID spike-down. For a company whose non-COVID revenue grew 6% (PERF-3), the floor mechanically forces the most negative defensible input, biasing the DCF low. (cites growth_bounds, growth_blend, PERF-3)
- [business, medium, rating too high, supported] The DCF's terminal value rests on a 41.7% moat share of today's excess return, but ROIC is 7.9% against a 7.5% WACC — a 0.4-point spread, far below the 5-point moat_margin. The moat is essentially absent, so terminal_share should be 0, cutting base fair value well below 18.67. (cites roic, wacc, terminal_share, moat_margin, terminal_excess_return)
- [business, medium, rating too low, supported] The rating ignores the balance sheet and cash returns: $12.5bn short-term investments (CAP-1), $11.7bn operating cash flow (PERF-5) against $2.6bn capex (CAP-7), and a $0.43 quarterly dividend (CAP-5). Cash conversion of 0.852 and a 10.4x EV/EBIT versus the industry's 20.3x suggest the DCF is too harsh. (cites CAP-1, PERF-5, CAP-7, CAP-5, cash_conversion, ev_to_ebit)
- Correction applied in code: {'fixes': {'growth': 0.04}, 'fair_value': {'bear': 17.65, 'base': 28.42, 'bull': 55.07}, 'step': 1}

## Cost

62,124 tokens, $0.0098 across 9 model runs.

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
