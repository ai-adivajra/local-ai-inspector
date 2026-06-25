from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Observation:
    """
    Represents one collected fact about the inspected system.
    """

    source: str
    key: str
    value: Any
    unit: str | None = None
