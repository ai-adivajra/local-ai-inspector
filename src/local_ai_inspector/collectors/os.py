from pathlib import Path

from local_ai_inspector.collectors.base import Collector
from local_ai_inspector.domain.observation import Observation


class OSCollector(Collector):
    """Collect operating system information."""

    OS_RELEASE = Path("/etc/os-release")

    def collect(self) -> list[Observation]:

        data = {}

        if self.OS_RELEASE.exists():

            for line in self.OS_RELEASE.read_text().splitlines():

                if "=" not in line:
                    continue

                key, value = line.split("=", 1)

                data[key] = value.strip('"')

        return [

            Observation(
                source="os",
                key="distribution",
                value=data.get("NAME", "Unknown"),
            ),

            Observation(
                source="os",
                key="version",
                value=data.get("VERSION_ID", "Unknown"),
            ),

            Observation(
                source="os",
                key="pretty_name",
                value=data.get("PRETTY_NAME", "Unknown"),
            ),
        ]
