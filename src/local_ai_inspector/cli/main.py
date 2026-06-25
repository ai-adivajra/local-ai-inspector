from local_ai_inspector.core.inspector import Inspector


def print_section(title: str) -> None:
    print(title)
    print("-" * 40)


def print_group(source: str, inspection) -> None:

    print_section(source.capitalize())

    for obs in inspection.observations:

        if obs.source != source:
            continue

        unit = f" {obs.unit}" if obs.unit else ""

        print(f"{obs.key:<20} : {obs.value}{unit}")

    print()


def main() -> None:

    print("Local AI Inspector 0.1.0")
    print()

    print("Inspecting system...")
    print()

    inspection = Inspector().run()

    for source in (
    "cpu",
    "memory",
    "system",
    "os",
):
        print_group(source, inspection)

    print(f"Observations : {len(inspection.observations)}")
