# PLD: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Real Estate Segment rental revenues were $8,159 million in 2025 versus $7,515 million in 2024. (P089: "Rental revenues $ 8,159 $ 7,515")
- Real Estate Segment NOI was $6,188 million in 2025 versus $5,717 million in 2024. (P089: "Real Estate Segment – NOI $ 6,188 $ 5,717")
- Operating income was $4,358 million in 2025 compared with $4,416 million in 2024. (P089: "Operating income $ 4,358 $ 4,416")
- Net cash provided by operating activities was $5,008 million in 2025 and $4,912 million in 2024. (P110: "Net cash provided by (used in) operating activities $ 5,008 $ 4,912")
- Real estate segment rental revenues were $4,302 million for the six months ended June 30, 2026, up from $4,013 million in 2025. (Q081: "Rental revenues $ 4,302 $ 4,013")
- Strategic capital revenues were $402 million for the six months ended June 30, 2026 versus $288 million in 2025. (Q081: "Strategic capital revenues 402 288")

**capital**
- Cash and cash equivalents at December 31, 2025 were $1,145,647 thousand. (P149: "Cash and cash equivalents 1,145,647 1,318,591")
- Total debt at December 31, 2025 was $35,037,073 thousand, up from $30,879,263 thousand at December 31, 2024. (P149: "Debt $ 35,037,073 $ 30,879,263")
- Common stock issued and outstanding was 929,153 thousand shares at December 31, 2025 versus 926,283 thousand shares at December 31, 2024. (P149: "Common stock; $ 0.01 par value; 929,153 and 926,283 shares issued and outstanding at December 31, 2025 and 2024, respectively")
- Distributions paid on common and preferred units were $3,871,539 thousand in 2025. (P163: "Distributions paid on common and preferred units ( 3,871,539 ) ( 3,672,318 ) ( 3,320,929 )")
- Total common stock dividend per share was $4.04 in 2025. (P220: "Total dividend $ 4.04 $ 3.84 $ 3.48")
- Real estate development spending was $2,781,260 thousand in 2025. (P162: "Real estate development ( 2,781,260 ) ( 3,206,231 ) ( 3,399,114 )")

**risks**
- The company warns that its business and operations could suffer from system failures, cybersecurity attacks or risks associated with AI. (R000: "Our business and operations could suffer in the event of system failures, cybersecurity attacks or risks associated with AI.")
- The company serves as sponsor or manager for publicly traded investment vehicles, including Nippon Prologis REIT, Inc., China AMC Prologis Logistics REIT and FIBRA Prologis. (R000: "We have formed publicly traded investment vehicles, such as Nippon Prologis REIT, Inc., China AMC Prologis Logistics REIT and FIBRA Prologis, for which we serve")

**accounting**
- Prologis reported net earnings of $3,565,299 thousand for 2025. (P154: "net earnings $ 3,565,299 $ 3,947,935 $ 3,253,145")
- Net cash provided by operating activities was $5,008,434 thousand in 2025. (P154: "Net cash provided by (used in) operating activities 5,008,434 4,912,209 5,373,058")
- Net cash provided by operating activities was $5,008 million in 2025, compared with $4,912 million in 2024. (P110: "Net cash provided by (used in) operating activities $ 5,008 $ 4,912")
- KPMG expressed an unqualified opinion on the consolidated financial statements. (P146: "our report dated February 13, 2026 expressed an unqualified opinion on those consolidated financial statements")
- The critical audit matter was the assessment of the Operating Partnership's evaluation of the expected holding period for operating properties, with $80,561 million of operating properties as of December 31, 2025. (P144: "Assessment of the Operating Partnership’s evaluation of the expected holding period for operating properties As discussed in Notes 2 and 3 to the consolidated f")
- KPMG concluded the Company maintained effective internal control over financial reporting as of December 31, 2025. (P146: "In our opinion, the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")

## Cost

43,620 tokens, $0.0070 across 6 model runs.

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
