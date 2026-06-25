from local_ai_inspector.collectors.base import Collector
from local_ai_inspector.collectors.cpu import CPUCollector
from local_ai_inspector.collectors.memory import MemoryCollector
from local_ai_inspector.collectors.system import SystemCollector
from local_ai_inspector.domain.inspection import Inspection
from local_ai_inspector.collectors.os import OSCollector


class Inspector:
    """Main inspection engine."""

    def __init__(self) -> None:
        self.collectors: list[Collector] = [
            CPUCollector(),
            MemoryCollector(),
            SystemCollector(),
            OSCollector(),
        ]

    def run(self) -> Inspection:

        inspection = Inspection()

        for collector in self.collectors:
            inspection.observations.extend(
                collector.collect()
            )

        return inspection
