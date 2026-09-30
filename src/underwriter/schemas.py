"""Evidence schemas the readers fill in."""

PERFORMANCE_TASK = (
    "Collect the company's financial performance for its latest fiscal year: total revenue and its growth, "
    "gross or operating margin, net income, the largest segments' revenue or operating income, and operating "
    "cash flow."
)

EVIDENCE_SCHEMA = {
    "type": "object",
    "properties": {
        "claims": {
            "type": "array",
            "maxItems": 8,
            "description": "Evidence from the filing, one number per claim.",
            "items": {
                "type": "object",
                "properties": {
                    "topic": {"type": "string",
                              "enum": ["revenue", "growth", "margin", "net_income", "segment", "cash_flow", "other"]},
                    "statement": {"type": "string", "description": "One short sentence stating the fact."},
                    "value": {"type": ["number", "null"], "description": "The number as printed, no unit."},
                    "unit": {"type": ["string", "null"], "description": "For example 'USD millions' or '%'."},
                    "period": {"type": ["string", "null"], "description": "For example 'fiscal 2026'."},
                    "passage_id": {"type": "string", "description": "ID of the passage it comes from, e.g. P102."},
                    "quote": {"type": "string",
                              "description": "Exact words from that passage containing the number, at most 200 characters."},
                },
                "required": ["topic", "statement", "value", "passage_id", "quote"],
            },
        }
    },
    "required": ["claims"],
}
