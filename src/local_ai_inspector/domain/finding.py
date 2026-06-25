from dataclasses import dataclass


@dataclass(slots=True)
class Finding:
    """Represents one validated finding."""
