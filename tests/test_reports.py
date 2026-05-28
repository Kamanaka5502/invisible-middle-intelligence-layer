from invisible_middle.classifier import classify
from invisible_middle.reports import generate_markdown_report


def test_report_contains_primary_condition():
    case = {
        "case_id": "TEST-REPORT-001",
        "signals": [
            {
                "family": "behavioural",
                "signal": "repeated checking",
                "description": "User repeatedly validates completion.",
            }
        ],
    }

    interpretation = classify(case)

    report = generate_markdown_report(interpretation)

    assert "trust_instability" in report
    assert "RECHECK LOOP" in report
    assert "Rebalance Guidance" in report


def test_report_contains_hidden_compensation_note():
    case = {
        "case_id": "TEST-REPORT-002",
        "signals": [
            {
                "family": "workflow",
                "signal": "handoff failure",
                "description": "Workflow continuity breaks.",
            }
        ],
    }

    interpretation = classify(case)

    report = generate_markdown_report(interpretation)

    assert "Visible operational completion" in report
