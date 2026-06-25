from local_ai_inspector.core.inspector import Inspector


def main() -> None:
    print("Local AI Inspector 0.1.0")
    print()

    print("Starting inspection...")

    inspector = Inspector()
    inspection = inspector.run()

    print("Inspection completed.")
    print()

    print(f"Observations     : {len(inspection.observations)}")
    print(f"Findings         : {len(inspection.findings)}")
    print(f"Recommendations  : {len(inspection.recommendations)}")
