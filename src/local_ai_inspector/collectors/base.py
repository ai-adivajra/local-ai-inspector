from abc import ABC, abstractmethod

from local_ai_inspector.domain.observation import Observation


class Collector(ABC):
    """Base class for all collectors."""

    @abstractmethod
    def collect(self) -> list[Observation]:
        """Collect observations from the host system."""
        raise NotImplementedError
