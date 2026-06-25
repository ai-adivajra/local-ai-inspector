from pathlib import Path

import psutil

from local_ai_inspector.domain.observation import Observation

from local_ai_inspector.collectors.base import Collector


class CPUCollector(Collector):
    """Collect CPU information."""

    CPUINFO = Path("/proc/cpuinfo")

    def collect(self) -> list[Observation]:
        return [
            Observation(
                source="cpu",
                key="model",
                value=self._cpu_model(),
            ),
            Observation(
                source="cpu",
                key="architecture",
                value=self._architecture(),
            ),
            Observation(
                source="cpu",
                key="physical_cores",
                value=psutil.cpu_count(logical=False) or 0,
                unit="cores",
            ),
            Observation(
                source="cpu",
                key="logical_cores",
                value=psutil.cpu_count(logical=True) or 0,
                unit="threads",
            ),
        ]

    @staticmethod
    def _architecture() -> str:
        import platform

        return platform.machine()

    def _cpu_model(self) -> str:
        if not self.CPUINFO.exists():
            return "Unknown"

        for line in self.CPUINFO.read_text().splitlines():
            if line.startswith("model name"):
                return line.split(":", 1)[1].strip()

        return "Unknown"
