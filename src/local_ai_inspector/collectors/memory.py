import psutil

from local_ai_inspector.collectors.base import Collector
from local_ai_inspector.domain.observation import Observation


class MemoryCollector(Collector):
    """Collect memory information."""

    def collect(self) -> list[Observation]:

        memory = psutil.virtual_memory()

        gib = 1024**3

        return [
            Observation(
                source="memory",
                key="installed",
                value=round(memory.total / gib, 1),
                unit="GiB",
            ),
            Observation(
                source="memory",
                key="available",
                value=round(memory.available / gib, 1),
                unit="GiB",
            ),
        ]
