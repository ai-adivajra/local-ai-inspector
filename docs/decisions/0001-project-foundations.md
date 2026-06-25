Local AI Inspector is intended to become a reliable tool for inspecting and understanding local AI workstations.

The project starts with a deliberately limited scope to establish solid engineering foundations before expanding.

## Decisions

- Git is the source of truth for the project.
- Documentation is written in English.
- Discussions may take place in French.
- Development is iterative and incremental.
- Observe before analyzing.
- Recommendations must always be based on collected facts.
- The core engine must work without an LLM.
- The tool never modifies the system automatically.
- Initial target platform:
  - Fedora Linux
  - AMD CPU/GPU
  - ROCm
  - Ollama

## Consequences

Future architectural and implementation decisions must remain consistent with these foundations.

Any deviation should result in a new ADR.
