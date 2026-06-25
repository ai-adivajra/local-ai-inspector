"""
Domain model: Inspection

The Inspection object is the root entity of the Local AI Inspector domain model.
It represents a complete inspection executed on a local machine.
"""

from dataclasses import dataclass, field
from datetime import datetime

from .finding import Finding
from .observation import Observation
from .recommendation import Recommendation


@dataclass(slots=True)
class Inspection:
    """
    Represents a complete inspection.

    Every execution of Local AI Inspector produces exactly one Inspection.
    """

    started_at: datetime = field(default_factory=datetime.now)

    observations: list[Observation] = field(default_factory=list)

    findings: list[Finding] = field(default_factory=list)

    recommendations: list[Recommendation] = field(default_factory=list)

    def add_observation(self, observation: Observation) -> None:
        """Register a new observation."""
        self.observations.append(observation)

    def add_finding(self, finding: Finding) -> None:
        """Register a new finding."""
        self.findings.append(finding)

    def add_recommendation(self, recommendation: Recommendation) -> None:
        """Register a new recommendation."""
        self.recommendations.append(recommendation)
