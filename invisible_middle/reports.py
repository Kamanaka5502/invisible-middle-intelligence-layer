from invisible_middle.models import Interpretation


def generate_markdown_report(interpretation: Interpretation) -> str:
    secondary = ", ".join(interpretation.structural_condition.secondary)
    carriers = ", ".join(interpretation.burden.carriers)
    burdens = ", ".join(interpretation.burden.burden_domains)

    return f"""# Invisible Middle Report

## Case

**Case ID:** {interpretation.case_id}  
**Finding:** {interpretation.finding}  
**Evidence strength:** {interpretation.evidence_strength}

## Structural Interpretation

**Primary condition:** {interpretation.structural_condition.primary}  
**Secondary conditions:** {secondary}

## Human Compensation Map

**Burden carriers:** {carriers}

**Burden domains:** {burdens}

## Flourishing Impact

| Dimension | Reading |
|---|---|
| Agency | {interpretation.flourishing.agency} |
| Confidence | {interpretation.flourishing.confidence} |
| Continuity | {interpretation.flourishing.continuity} |
| Participation | {interpretation.flourishing.participation} |
| Recovery Capacity | {interpretation.flourishing.recovery_capacity} |

## Rebalance Guidance

{interpretation.rebalance_guidance}

## Note

{interpretation.notes}
"""
