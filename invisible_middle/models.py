from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Signal:
    family: str
    signal: str
    description: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class StructuralCondition:
    primary: str
    secondary: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class BurdenEnvelope:
    carriers: list[str]
    burden_domains: list[str]


@dataclass(frozen=True)
class FlourishingImpact:
    agency: str = "unknown"
    confidence: str = "unknown"
    continuity: str = "unknown"
    participation: str = "unknown"
    recovery_capacity: str = "unknown"


@dataclass(frozen=True)
class Interpretation:
    case_id: str
    structural_condition: StructuralCondition
    burden: BurdenEnvelope
    flourishing: FlourishingImpact
    evidence_strength: str
    finding: str
    rebalance_guidance: str
    notes: str = ""
