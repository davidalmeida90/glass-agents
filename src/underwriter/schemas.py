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
        task=("Collect the company's financial performance for its latest fiscal year. Cover each of these once "
              "before adding anything else: total revenue, revenue growth, gross or operating margin, net income, "
              "operating cash flow, then the largest segments' revenue or operating income."),
        schema=evidence_schema(["revenue", "growth", "margin", "net_income", "cash_flow", "segment", "other"], 10),
        min_verified=4,
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
}

# Kept for the first runs' records
PERFORMANCE_TASK = READERS["performance"].task
EVIDENCE_SCHEMA = READERS["performance"].schema
