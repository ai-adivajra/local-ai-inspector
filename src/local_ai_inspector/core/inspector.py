from local_ai_inspector.domain.inspection import Inspection


class Inspector:
    """Main inspection engine."""

    def run(self) -> Inspection:
        return Inspection()
