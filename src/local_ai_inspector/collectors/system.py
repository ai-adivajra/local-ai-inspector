import platform
import socket

from local_ai_inspector.collectors.base import Collector
from local_ai_inspector.domain.observation import Observation


class SystemCollector(Collector):
    """Collect operating system information."""

    def collect(self) -> list[Observation]:

        uname = platform.uname()

        return [
            Observation(
                source="system",
                key="hostname",
                value=socket.gethostname(),
            ),
            Observation(
                source="system",
                key="kernel",
                value=uname.release,
            ),
            Observation(
                source="system",
                key="architecture",
                value=uname.machine,
            ),
        ]
