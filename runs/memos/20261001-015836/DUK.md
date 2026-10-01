# DUK: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Duke Energy's consolidated net income for fiscal 2025 was USD 5,071 million. (P240: "Net Income $ 5,071 $ 4,614 $ 2,874")
- Net income available to Duke Energy Corporation common stockholders was USD 6.31 per basic and diluted share in 2025. (P240: "Net income available to Duke Energy Corporation common stockholders Basic and Diluted $ 6.31 $ 5.71 $ 3.54")
- Net income attributable to Duke Energy Corporation for the six months ended June 30, 2026 was USD 2,642 million. (Q016: "Net Income Attributable to Duke Energy Corporation 1,092 984 2,642 2,363")
- Net income available to Duke Energy common stockholders for the six months ended June 30, 2026 was USD 2,613 million. (Q183: "Net Income available to Duke Energy common stockholders $ 1,077 $ 971 $ 2,613 $ 2,336")
- Duke Energy Florida's operating revenues were USD 7,105 million in 2025 versus USD 6,595 million in 2024. (P173: "Operating Revenues $ 7,105 $ 6,595 $ 510")
- Duke Energy Ohio's operating revenues rose USD 132 million in 2025 driven by fuel-related revenues. (P177: "a $132 million increase in fuel-related revenues primarily due to higher natural gas costs passed through to customers")

**capital**
- Duke Energy's cash, cash equivalents and restricted cash at end of 2025 was $363 million. (P200: "Cash, cash equivalents and restricted cash at end of period $ 363")
- Duke Energy's cash, cash equivalents and restricted cash at beginning of 2025 was $421 million. (P200: "Cash, cash equivalents and restricted cash at beginning of period 421 357")
- Net cash provided by operating activities was $12,330 million in 2025. (P244: "Net cash provided by operating activities 12,330 12,328 9,878")
- Capital expenditures were $14,024 million in 2025. (P244: "Capital expenditures ( 14,024 ) ( 12,280 ) ( 12,604 )")
- Dividends paid were $3,300 million in 2025. (P244: "Dividends paid ( 3,300 ) ( 3,213 ) ( 3,244 )")
- Duke Energy issued $11,891 million of long-term debt in 2025. (P244: "Issuance of long-term debt 11,891 8,956 10,028")

**risks**
- Emerging large loads such as hyperscale data centers and industrial facilities present unique risks due to high demand, rapid fluctuations and unpredictable operational profiles that can strain bulk power system reliability and grid stability. (R001: "emerging large loads – such as hyperscale data centers and industrial facilities – present unique risks due to their high demand, rapid fluctuations, and unpred")
- Early termination of service agreements or stranded assets could result if investments in generation, transmission and advanced grid infrastructure are not fully recovered. (R001: "early termination of service agreements or stranded assets could result if investments are not fully recovered")
- Failure to comply with evolving regulatory requirements and reliability standards, including those established or that may be established by NERC and regional entities, could result in penalties, operational restrictions or reputational harm. (R001: "failure to comply with evolving regulatory requirements and reliability standards , including those established or those that may be established in the future b")
- AI, including generative AI, may be used to facilitate or perpetrate cybersecurity threats, and Duke Energy's use of generative AI (and use by its vendors and agents) may subject it to data privacy, legal, regulatory and security risks. (R002: "Furthermore, AI, including generative AI, may be used to facilitate or perpetrate these cybersecurity threats. Duke Energy’s use of generative AI (and use by th")
- Rising demand for electric infrastructure and international trade developments, including potential export controls on certain rare earth materials and technologies used in electric utility infrastructure, may further constrain supply availability. (R002: "Rising demand for electric infrastructure and international trade developments, including potential export controls on certain rare earth materials and technolo")
- Federal legislation enacted in 2025 eliminated the long-term extension of certain residential solar tax credits, causing these incentives to expire after 2025. (R002: "Federal legislation enacted in 2025 eliminated the long‑term extension of certain residential solar tax credits, causing these incentives to expire after 2025")

**accounting**
- Duke Energy reported net income of $520 million for 2025 on its consolidated statement of cash flows. (P298: "Net income $ 520 $ 441 $ 497")
- Duke Energy reported net cash provided by operating activities of $1,045 million for 2025. (P298: "Net cash provided by operating activities 1,045 1,023 1,154")
- Deloitte & Touche LLP expressed an unqualified opinion on Duke Energy's consolidated financial statements for the year ended December 31, 2025. (P592: "expressed an unqualified opinion on those financial statements")
- The auditor reported a critical audit matter on Regulatory Matters – Impact of Rate Regulation on the Financial Statements, referring to Notes 1 and 4. (P258: "Regulatory Matters – Impact of Rate Regulation on the Financial Statements – Refer to Notes 1 and 4 to the financial statements.")
- The auditor concluded Duke Energy maintained effective internal control over financial reporting as of December 31, 2025. (P592: "the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")
- Management concluded that its internal controls over financial reporting were effective as of December 31, 2025. (P591: "management concluded that its internal controls over financial reporting were effective as of December 31, 2025")

## Cost

39,322 tokens, $0.0062 across 6 model runs.

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
