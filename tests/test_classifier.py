from invisible_middle.classifier import classify


def test_repeated_checking_maps_to_trust_instability():
    case = {
        "case_id": "TEST-TRUST-001",
        "signals": [
            {
                "family": "behavioural",
                "signal": "repeated checking",
                "description": "User repeatedly checks completion state.",
            }
        ],
    }

    result = classify(case)

    assert result.structural_condition.primary == "trust_instability"
    assert result.finding == "RECHECK LOOP"


def test_ai_override_maps_to_ai_burden_transfer():
    case = {
        "case_id": "TEST-AI-001",
        "signals": [
            {
                "family": "ai_interaction",
                "signal": "repeated human override",
                "description": "Human repeatedly overrides AI output.",
            }
        ],
    }

    result = classify(case)

    assert result.structural_condition.primary == "ai_burden_transfer"
    assert result.finding == "AI BURDEN TRANSFER"
    assert "authority_burden" in result.structural_condition.secondary


def test_default_case_maps_to_context_fragmentation():
    case = {
        "case_id": "TEST-CONTEXT-001",
        "signals": [
            {
                "family": "workflow",
                "signal": "handoff failure",
                "description": "Context fails across transition.",
            }
        ],
    }

    result = classify(case)

    assert result.structural_condition.primary == "context_fragmentation"
    assert result.finding == "FRICTION"
