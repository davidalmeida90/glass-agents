"""The readers: each one is a task plus the evidence schema it fills in."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


def evidence_schema(topics: list[str], max_items: int) -> dict[str, Any]:
    """Claims with a topic, a number when there is one, and the exact quote it comes from."""
    return {
        "type": "object",
        "properties": {
            "claims": {
                "type": "array",
                "maxItems": max_items,
                "description": "Evidence from the filing, one fact per claim.",
                "items": {
                    "type": "object",
                    "properties": {
                        "topic": {"type": "string", "enum": topics},
                        "statement": {"type": "string", "description": "One short sentence stating the fact."},
                        "value": {"type": ["number", "null"],
                                  "description": "The number as printed, no unit; null for a fact without a number."},
                        "unit": {"type": ["string", "null"], "description": "For example 'USD millions' or '%'."},
                        "period": {"type": ["string", "null"], "description": "For example 'fiscal 2026'."},
                        "passage_id": {"type": "string", "description": "ID of the passage it comes from, e.g. P102."},
                        "quote": {"type": "string",
                                  "description": "Exact words from that passage, containing the number if there is one, "
                                                 "at most 200 characters."},
                    },
                    "required": ["topic", "statement", "value", "passage_id", "quote"],
                },
            }
        },
        "required": ["claims"],
    }


def guidance_schema(max_items: int) -> dict[str, Any]:
    """Management's outlook: a range per metric and period, with the prior-period figure when one is given."""
    return {
        "type": "object",
        "properties": {
            "claims": {
                "type": "array",
                "maxItems": max_items,
                "description": "Forward-looking guidance only, one metric and period per claim; empty when there is none.",
                "items": {
                    "type": "object",
                    "properties": {
                        "topic": {"type": "string", "enum": ["revenue", "revenue_growth", "operating_income",
                                                             "operating_margin", "gross_margin", "eps", "capex", "other"]},
                        "statement": {"type": "string", "description": "One short sentence stating the outlook."},
                        "low": {"type": ["number", "null"], "description": "Low end of the range as printed, no unit."},
                        "high": {"type": ["number", "null"], "description": "High end as printed; equal to low for a point."},
                        "unit": {"type": ["string", "null"], "description": "For example 'USD billions' or '%'."},
                        "period": {"type": "string", "description": "For example 'Q4 2026' or 'full year 2026'."},
                        "basis": {"type": "string", "enum": ["GAAP", "non-GAAP", "unspecified"]},
                        "compared_with": {"type": ["number", "null"],
                                          "description": "The prior-period figure the outlook is compared with, as printed "
                                                         "in the same sentence; null when none is printed."},
                        "passage_id": {"type": "string", "description": "ID of the passage, e.g. E004."},
                        "quote": {"type": "string", "description": "Exact words containing every number you give, at most "
                                                                   "250 characters."},
                    },
                    "required": ["topic", "statement", "low", "high", "period", "passage_id", "quote"],
                },
            }
        },
        "required": ["claims"],
    }


def segments_schema(max_items: int) -> dict[str, Any]:
    """Segment revenue and operating income, this year and last, as printed in one row of the segment note."""
    return {
        "type": "object",
        "properties": {
            "claims": {
                "type": "array",
                "maxItems": max_items,
                "description": "One claim per segment and measure; empty when the company reports a single segment.",
                "items": {
                    "type": "object",
                    "properties": {
                        "topic": {"type": "string", "enum": ["revenue", "operating_income"]},
                        "segment": {"type": "string", "description": "Segment name as the filing writes it."},
                        "statement": {"type": "string", "description": "One short sentence."},
                        "value": {"type": "number", "description": "Latest fiscal year, as printed, no unit."},
                        "value_prior": {"type": ["number", "null"], "description": "The year before, as printed."},
                        "unit": {"type": "string", "description": "For example 'USD millions'."},
                        "period": {"type": "string", "description": "For example 'fiscal 2026'."},
                        "passage_id": {"type": "string", "description": "ID of the passage, e.g. P230."},
                        "quote": {"type": "string", "description": "Exact words or table row containing both numbers, at "
                                                                   "most 250 characters."},
                    },
                    "required": ["topic", "segment", "statement", "value", "value_prior", "unit", "passage_id", "quote"],
                },
            }
        },
        "required": ["claims"],
    }


@dataclass(frozen=True)
class Reader:
    name: str
    task: str
    schema: dict[str, Any]
    min_verified: int
    corpus: str = "10-K"


READERS: dict[str, Reader] = {
    "performance": Reader(
        name="performance",
        task=("Collect the company's financial performance for its latest fiscal year and, when a 10-Q is included, "
              "its latest year-to-date period. Cover each of these once before adding anything else: total revenue, "
              "revenue growth, gross or operating margin, net income, operating cash flow, the latest year-to-date "
              "revenue growth from the 10-Q, then the largest segments' revenue or operating income."),
        schema=evidence_schema(["revenue", "growth", "margin", "net_income", "cash_flow", "segment", "other"], 10),
        min_verified=4,
        corpus="10-K+10-Q",
    ),
    "accounting": Reader(
        name="accounting",
        task=("Collect evidence on the quality of the company's reporting for its latest fiscal year: net income and "
              "net cash from operating activities (so code can compare them), the auditor's opinion and any critical "
              "audit matters, whether internal control over financial reporting was effective, the revenue "
              "recognition policy, and any change in accounting policy, restatement or material weakness. "
              "A fact without a number still needs its exact quote."),
        schema=evidence_schema(["net_income", "cash_flow", "audit_opinion", "critical_audit_matter",
                                "internal_control", "revenue_recognition", "policy_change", "other"], 8),
        min_verified=3,
    ),
    "capital": Reader(
        name="capital",
        task=("Collect evidence on the company's balance sheet and capital allocation for its latest fiscal year: "
              "cash and investments, total debt, share repurchases, dividends paid, capital expenditures, the change "
              "in shares outstanding, and any large acquisition."),
        schema=evidence_schema(["cash", "debt", "buyback", "dividend", "capex", "shares", "acquisition", "other"], 8),
        min_verified=4,
    ),
    "risks": Reader(
        name="risks",
        task=("The passages hold only the sentences that are new in this year's risk factors compared with last "
              "year's. Collect the most material new or expanded risks, one per claim, each with the exact words "
              "that state it. Skip boilerplate and sentences that only restate an old risk."),
        schema=evidence_schema(["ai", "regulation", "competition", "supply_chain", "macro", "cybersecurity",
                                "legal", "geopolitical", "financial", "other"], 6),
        min_verified=2,
        corpus="risk_changes",
    ),
    "guidance": Reader(
        name="guidance",
        task=("Collect management's forward-looking guidance from the latest earnings release and 10-Q: revenue or "
              "revenue growth, operating income or operating margin, earnings per share and capital expenditure, each "
              "as a range with its period (next quarter or full year) and whether it is GAAP. When the same sentence "
              "gives the prior-period figure the outlook is compared with, put it in compared_with. Only outlook "
              "statements (expects, anticipates, guidance, outlook, targets), never historical results. If the "
              "documents give no numeric guidance, submit an empty list."),
        schema=guidance_schema(8),
        min_verified=0,
        corpus="guidance",
    ),
    "segments": Reader(
        name="segments",
        task=("From the segment note of the latest 10-K, collect each reportable segment's revenue and its operating "
              "income (or segment profit) for the latest fiscal year and the year before: one claim per segment and "
              "measure, value = latest year and value_prior = the year before, both from the same table row. Skip "
              "corporate, eliminations and reconciling items. If the company reports a single segment, submit an "
              "empty list."),
        schema=segments_schema(10),
        min_verified=0,
    ),
}

# Kept for the first runs' records
PERFORMANCE_TASK = READERS["performance"].task
EVIDENCE_SCHEMA = READERS["performance"].schema
