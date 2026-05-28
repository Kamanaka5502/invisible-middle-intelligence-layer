from invisible_middle.models import (
    BurdenEnvelope,
    FlourishingImpact,
    Interpretation,
    StructuralCondition,
)


TRUST_SIGNALS = {
    "repeated checking",
    "repeated confirmation requests",
    "reassurance seeking",
}

AI_TRANSFER_SIGNALS = {
    "repeated human override",
    "verification loop",
    "confidence uncertainty",
}


def classify(case: dict) -> Interpretation:
    signals = case.get("signals", [])
    signal_names = {s["signal"] for s in signals}

    primary = "context_fragmentation"
    secondary = ["hidden_compensation"]
    finding = "FRICTION"

    if signal_names & TRUST_SIGNALS:
        primary = "trust_instability"
        finding = "RECHECK LOOP"

    if signal_names & AI_TRANSFER_SIGNALS:
        primary = "ai_burden_transfer"
        finding = "AI BURDEN TRANSFER"
        secondary.append("authority_burden")

    return Interpretation(
        case_id=case.get("case_id", "UNKNOWN"),
        structural_condition=StructuralCondition(
            primary=primary,
            secondary=secondary,
        ),
        burden=BurdenEnvelope(
            carriers=case.get("burden_carriers", ["human_operator"]),
            burden_domains=case.get(
                "burden_domains",
                [
                    "verification_burden",
                    "context_reconstruction_burden",
                ],
            ),
        ),
        flourishing=FlourishingImpact(
            agency="strained",
            confidence="unstable",
            continuity="weak",
            participation="degraded",
            recovery_capacity="reduced",
        ),
        evidence_strength=case.get("evidence_strength", "moderate"),
        finding=finding,
        rebalance_guidance=(
            "Reduce hidden compensation by strengthening context continuity, "
            "closure confidence, ownership clarity, and trust stability."
        ),
        notes=(
            "Visible operational completion does not guarantee reduced human burden."
        ),
    )
