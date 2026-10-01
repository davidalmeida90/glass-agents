# Fundamentalist Agents

A first-pass equity underwriting memo for any US-listed company, in about 40 seconds and one cent: evidence read from its own SEC filings and checked against them in code, a sourced valuation, a rating a person can recompute, and the points where it could be wrong.

## The problem it solves

LLM trading agents give a rating you cannot check, cannot afford at scale and cannot trust twice:

- **Unverifiable.** In our Glassbench runs of TradingAgents, only 25 of 35 valuation multiples the agents quoted matched the true figure, and without served valuation data the reports stated it was missing 55 times in 12 runs.
- **Unstable.** Two TradingAgents runs on Microsoft, same inputs, started two minutes apart, returned Underweight and Overweight.
- **Expensive.** A full TradingAgents run costs about $0.06, 320,000 tokens and 8 minutes per stock and date.
- **Opaque.** The rating comes from a language model's judgment, so no one can say which assumption drove it.

An analyst screening a watchlist needs the opposite: numbers traced to the filing, a valuation whose every input has a source, a rating rule that is arithmetic, a measure of how much the answer moves on a rerun, and the cheapest possible cost per company.

## What it does

For each company:

1. **Readers** (a language model with bounded tasks) search the latest 10-K, and the latest 10-Q for recent performance, and return structured claims with the exact quote and passage ID: financial performance, accounting quality, capital allocation, and the risk factors that are new this year.
2. **Code checks every claim** against the filing: the quote must be in the cited passage and the number in the quote.
3. **Code values the company**, with the model picked by its SEC industry code:
   - operating companies: FCFF DCF at its own WACC (bottom-up beta, implied ERP paired with its risk-free rate, synthetic-rating cost of debt), stock-based compensation expensed, R&D capitalized where material, leases as debt, growth paid for by reinvestment, a moat share taken from 5-year ROIC history, and a reverse DCF;
   - banks and insurers: excess return model on a normalized 5-year ROE, with at most half of today's excess return kept in the terminal value;
   - REITs and utilities: two-stage dividend discount model on their own dividend per share growth.

   Starting growth blends the last twelve months with the 3-year CAGR. A second method checks the first: industry EV/EBIT (price to book adjusted for ROE for financials) from Damodaran's January 2026 tables; when the two disagree by more than half, uncertainty goes up a level.
4. **Code rates it:** price over base fair value against Morningstar-style bands that widen with uncertainty, minus notches for flags raised by verified evidence (material weakness, weak cash conversion, a large share of new risk factors).
5. **A red team** (one model call) argues against the rating using only the verified evidence. It can propose a corrected input, which code revalues; its criticism of the method goes to a review list and never moves a rating.
6. **A noise meter** repeats the model-driven steps three times and reports the median rating and the agreement.
7. **An audit** recomputes each memo (value, equity bridge, WACC, scenario order, share of claims verified) and the batch's median price to fair value.
8. **A memo** in Markdown per company: rating and why, valuation build-up, sensitivity grid, evidence with quotes, red team, noise, data notes, parameters, cost.

## Evidence, 21 companies, 2026-10-01

Thirteen large caps plus two REITs, two utilities and four insurers, so every valuation route ran.

| Measure | Result |
|---|---|
| Claims checked against the filings | 992 of 994 (the code verifier rejected the other 2) |
| Audit | 21 of 21 memos add up |
| Median price / fair value | 1.01 (consistent with the market on average) |
| Agreement across 3 repeats | 100% on 19 companies, 67% on 2 (Visa, Pfizer) |
| Cost per company | $0.0101, 64,070 tokens, 16 model calls, 63% of input cached |
| Time per company | about 44 seconds |

| Rating | Companies |
|---|---|
| Buy | Meta, Realty Income |
| Overweight | Visa, Prologis, NextEra, Chubb |
| Hold | Microsoft, Nvidia, Alphabet, JPMorgan, Pfizer, Progressive, Travelers |
| Underweight | Apple, Walmart, Caterpillar, Bank of America, MetLife |
| Sell | Amazon, Coca-Cola, Duke Energy |

They are the model's reading under the stated parameters, not investment advice, and no backtest has been run. The run found three faults, fixed since: false red flags from 10-K boilerplate (the auditor's PCAOB paragraph, the cover page check boxes), a red team margin correction that was really operating expenses over revenue (Visa, now bounded against the reported margin), and trimmed tool calls sent back to the API (a 400 on Pfizer's risk reader).

## Run it

```
python desk.py --tickers MSFT,AAPL --budget-usd 0.50       # full desk, memos in runs/memos/
python desk.py --tickers MSFT --valuation-only             # free: SEC, FRED and Yahoo only
python run.py --tickers MSFT --readers performance         # one reader, for testing
python track.py show                                       # ratings recorded by full runs
python track.py score --min-days 90                         # excess return vs SPY by rating, once they age
python -m pytest tests/unit_tests                           # offline tests, no key, no cost
```

Every full run appends its ratings to `data/track_record.csv`. They are scored later against SPY, so the track record builds forward, without a backtest and without the look-ahead a backtest on today's filings would carry.

Glassbench (the local run viewer next to TradingAgents and AI Hedge Fund) drives the same `Desk.company()` through its own driver and shows each reader, the valuation, the red team and the noise meter as lanes on the run page.

Keys come from `Agents_model/.env` through `FIDCS/backend/chaves.py` (DeepSeek, FRED, SEC contact email) and are never printed. Every model call prints a line; each run stops at `--max-tokens` and each batch at `--budget-usd`.

## Every choice can be questioned

`src/fundamentalist/parameters.py` holds each parameter with its value, method, source, alternatives and whether it was verified on a primary source: risk-free rate and ERP pairing (Damodaran, 2026-09-01), beta method, rating spreads (January 2026), tax, growth bounds and base-rate decay, terminal growth, moat rule, R&D lives, captive finance, sanity bounds, rating bands. The memo prints them; the red team cites them by name in its method review. The docstrings record the versions that were rejected and why (a plain DCF that rated every large cap a Sell; a 3.5% terminal cap that made the model bearish by construction).

## Known limits

- Operating margin is held at today's level; margin expansion enters only through a red team correction backed by evidence (Amazon's technology spending sits under a company tag the XBRL API does not carry, so it is not capitalized).
- Starting growth comes from reported revenue only; no analyst consensus and no forward guidance.
- Pharma pipelines are not valued; banks and insurers use an excess return model without a separate look at reserves or credit losses.
- The readers read the latest filings, so the desk runs live only.
- Ratings are not backtested; the forward track record needs months before it says anything.

## Credits

Started from LangChain's [data-enrichment](https://github.com/langchain-ai/data-enrichment) LangGraph template (MIT, see `LICENSE-langchain-template` and `NOTICE`); its agent loop remains, everything else is new. Market data: SEC EDGAR, FRED, Yahoo Finance. Valuation datasets: Aswath Damodaran (industry betas, rating spreads, implied ERP, R&D lives, company industries), saved in `data/` with their dates.
