# O: No rating

Desk memo, 2026-10-01. Price nan (2026-09-30). Noise meter agreement 100% (No rating, No rating, No rating). Target weight 0.0%.

## Why

- not rated, review: base value is nanx the price, outside 0.25x to 4.0x

## Valuation

Not valued: not rated, review: base value is nanx the price, outside 0.25x to 4.0x


## Evidence from the latest 10-K (every quote checked against the filing)

**performance**
- Total revenue for fiscal 2025 was $5,749,377 thousand. (P117: "Total revenue $ 5,749,377 $ 5,271,142 $ 478,235")
- Total revenue increased $478,235 thousand in 2025 versus 2024. (P117: "Total revenue $ 5,749,377 $ 5,271,142 $ 478,235")
- General and administrative expenses were 3.7% of total revenue (excluding client reimbursements) in 2025. (P120: "General and administrative expenses as a percentage of total revenue (1) 3.7 % 3.6 %")
- Total expenses were $4,785,982 thousand in 2025. (P120: "Total expenses $ 4,785,982 $ 4,489,294 $ 296,688")
- Net cash provided by operating activities was $3,994,754 thousand in 2025. (P157: "Net cash provided by operating activities 3,994,754 3,573,276 2,958,769")
- Net cash provided by operating activities was $2,019,585 thousand for the six months ended June 30, 2026. (Q009: "Net cash provided by operating activities 2,019,585 1,848,185")

**capital**
- Cash, cash equivalents and restricted cash at end of period was $520,756 thousand. (P158: "Cash, cash equivalents and restricted cash, end of period $ 520,756 $ 495,506 $ 292,175")
- Total outstanding borrowings of credit facilities, commercial paper, term loans, mortgages payable, and senior unsecured notes and bonds were $29.1 billion. (P105: "our total outstanding borrowings of credit facilities, commercial paper, term loans, mortgages payable, and senior unsecured notes and bonds were $29.1 billion")
- Approximately 93% of total debt was fixed rate debt. (P105: "approximately 93% of our total debt was fixed rate debt")
- Outstanding unsecured senior debt securities totaled $25.3 billion. (P070: "we also had a total of $25.3 billion of outstanding unsecured senior debt securities")
- Dividends paid per share during the year ended December 31, 2025 totaled $3.2170. (P095: "The dividends paid per share during the year ended December 31, 2025 totaled $3.2170, as compared to $3.1255 during the year ended December 31, 2024, an increas")
- Cash distributions to common stockholders were $2,920,895 thousand. (P157: "Cash distributions to common stockholders ( 2,920,895 ) ( 2,691,719 ) ( 2,111,793 )")

**risks**
- The company's reliance on innovation in IT and its use of or inability to adopt new technological capabilities, including artificial intelligence and machine learning, may put it at a competitive disadvantage. (R010: "our use of or inability to adopt and deliver new technological capabilities and enhancements in line with strategic objectives, including artificial intelligenc")
- The use of emerging technologies, including artificial intelligence, entails risks including intellectual property infringement or misappropriation, data privacy, inaccuracy, bias, and new or enhanced governmental or regulatory scrutiny. (R010: "The use of emerging technologies, including artificial intelligence, entails risks including risks relating to the possibility of intellectual property infringe")
- Instability and unpredictability from weakened institutional oversight and inconsistent regulatory enforcement can introduce legal and operational uncertainty that may hinder the company's ability to plan, operate and invest effectively. (R011: "The instability and unpredictability caused by weakened institutional oversight and inconsistent regulatory enforcement can introduce legal and operational unce")
- As the business has evolved and the scope and complexity of operations and transactions have increased, the company may be subject to an increased risk of litigation and other claims. (R009: "As our business has evolved and the scope and complexity of our operations and transactions have increased, including through mergers, acquisitions, development")
- The company has incurred significant indebtedness, including borrowings under its $4.0 billion unsecured credit facilities, its term loans and its $3.0 billion commercial paper programs. (R008: "We have incurred significant indebtedness, including borrowings under our $4.0 billion unsecured credit facilities, our term loans and our $3.0 billion commerci")
- The company relies on several resources to assist in underwriting potential investments and other opportunities, including predictive analytics, which may turn out to be inaccurate. (R002: "We rely on several resources to assist in underwriting our potential investments and other opportunities, including predictive analytics, which may turn out to ")

**accounting**
- Net income for fiscal 2025 was USD 1,069,783 thousand. (P156: "Net income $ 1,069,783 $ 867,341 $ 876,914")
- Net cash provided by operating activities for fiscal 2025 was USD 3,994,754 thousand. (P157: "Net cash provided by operating activities 3,994,754 3,573,276 2,958,769")
- KPMG LLP expressed an unqualified opinion on the consolidated financial statements, dated February 24, 2026. (P149: "our report dated February 24, 2026 expressed an unqualified opinion on those consolidated financial statements")
- The audit report included a critical audit matter relating to the estimated holding periods for long-lived assets. (P148: "the events or changes in circumstances which may indicate a shortening of the estimated holding periods for long-lived assets")
- KPMG LLP concluded the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025. (P149: "the Company maintained, in all material respects, effective internal control over financial reporting as of December 31, 2025")
- Management concluded the Company's internal control over financial reporting was effective as of the end of the most recent fiscal year. (P248: "Management has concluded that the Company’s internal control over financial reporting was effective as of the end of the most recent fiscal year.")

## Cost

41,068 tokens, $0.0065 across 6 model runs.

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
