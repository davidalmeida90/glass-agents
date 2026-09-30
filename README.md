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
3. **Code values the company:** FCFF DCF at its own WACC (bottom-up beta, implied ERP paired with its risk-free rate, synthetic-rating cost of debt), stock-based compensation expensed, R&D capitalized where material, leases as debt, growth paid for by reinvestment, a moat share taken from 5-year ROIC history, and a reverse DCF. Banks use an excess return model.
4. **Code rates it:** price over base fair value against Morningstar-style bands that widen with uncertainty, minus notches for flags raised by verified evidence (material weakness, weak cash conversion, a large share of new risk factors).
5. **A red team** (one model call) argues against the rating using only the verified evidence. It can propose a corrected input, which code revalues; its criticism of the method goes to a review list and never moves a rating.
6. **A noise meter** repeats the model-driven steps three times and reports the median rating and the agreement.
7. **An audit** recomputes each memo (value, equity bridge, WACC, scenario order, share of claims verified) and the batch's median price to fair value.
8. **A memo** in Markdown per company: rating and why, valuation build-up, sensitivity grid, evidence with quotes, red team, noise, data notes, parameters, cost.

## Evidence, 13 large caps, 2026-10-01

| Measure | Result |
|---|---|
| Claims checked against the filings | 410 of 410 |
| Audit | 13 of 13 memos add up |
| Median price / fair value | 1.00 (consistent with the market on average) |
| Agreement across 3 repeats | 100% on 10 companies, 67% on 3 |
| Cost per company | $0.0098, 61,569 tokens, 16 model calls, 60% of input cached |
| Time per company | about 42 seconds |

Ratings that day: Meta Buy; Visa, JPMorgan, Bank of America Overweight; Microsoft, Nvidia, Alphabet Hold; Apple, Pfizer, Caterpillar Underweight; Amazon, Walmart, Coca-Cola Sell. They are the model's reading under the stated parameters, not investment advice, and no backtest has been run.

## Run it

```
python desk.py --tickers MSFT,AAPL --budget-usd 0.50       # full desk, memos in runs/memos/
python desk.py --tickers MSFT --valuation-only             # free: SEC, FRED and Yahoo only
python run.py --tickers MSFT --readers performance         # one reader, for testing
python -m pytest tests/unit_tests                           # offline tests, no key, no cost
```

Keys come from `Agents_model/.env` through `FIDCS/backend/chaves.py` (DeepSeek, FRED, SEC contact email) and are never printed. Every model call prints a line; each run stops at `--max-tokens` and each batch at `--budget-usd`.

## Every choice can be questioned

`src/fundamentalist/parameters.py` holds each parameter with its value, method, source, alternatives and whether it was verified on a primary source: risk-free rate and ERP pairing (Damodaran, 2026-09-01), beta method, rating spreads (January 2026), tax, growth bounds and base-rate decay, terminal growth, moat rule, R&D lives, captive finance, sanity bounds, rating bands. The memo prints them; the red team cites them by name in its method review. The docstrings record the versions that were rejected and why (a plain DCF that rated every large cap a Sell; a 3.5% terminal cap that made the model bearish by construction).

## Known limits

- Operating margin is held at today's level; margin expansion enters only through a red team correction backed by evidence (Amazon's technology spending sits under a company tag the XBRL API does not carry, so it is not capitalized).
- One year of revenue growth starts the forecast; no analyst consensus.
- Pharma pipelines are not valued; banks use a simple excess return model.
- Ratings are not backtested.

## Credits

Started from LangChain's [data-enrichment](https://github.com/langchain-ai/data-enrichment) LangGraph template (MIT, see `LICENSE-langchain-template` and `NOTICE`); its agent loop remains, everything else is new. Market data: SEC EDGAR, FRED, Yahoo Finance. Valuation datasets: Aswath Damodaran (industry betas, rating spreads, implied ERP, R&D lives, company industries), saved in `data/` with their dates.
