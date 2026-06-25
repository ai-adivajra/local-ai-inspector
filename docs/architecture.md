# Architecture

**Version:** 1.0
**Status:** Draft
**Last updated:** 2026-06-25

---

# Overview

Local AI Inspector is designed as a modular inspection engine.

Its architecture separates data collection, validation, analysis and reporting into independent layers.

Each layer has a single responsibility and communicates only with adjacent layers.

This separation makes the project easier to extend, test and maintain.

---

# Design Principles

The architecture follows several fundamental principles.

* Single responsibility
* Modular components
* Local-first
* Evidence-based analysis
* No automatic system modifications
* Minimal resource consumption
* LLM-independent core engine

---

# Inspection Lifecycle

Every inspection follows the same workflow.

```text
User
    │
    ▼
Inspection Request
    │
    ▼
Discovery
    │
    ▼
Collection
    │
    ▼
Normalization
    │
    ▼
Validation
    │
    ▼
Analysis
    │
    ▼
Recommendations
    │
    ▼
Report
```

Each stage is isolated and independently testable.

---

# Architectural Layers

## User Interface

Responsible for interacting with the user.

Examples:

* CLI
* future Web UI
* future Desktop UI

The user interface never performs inspections directly.

---

## Discovery Layer

Discovers available hardware and software components.

Examples:

* CPU
* Memory
* GPU
* Storage
* Operating system
* AI runtimes

---

## Collection Layer

Collects raw information from the operating system.

Typical sources include:

* procfs
* sysfs
* system commands
* configuration files
* runtime APIs

Collectors never interpret data.

They only gather information.

---

## Normalization Layer

Transforms raw collected information into a common internal representation.

This isolates the rest of the application from platform-specific differences.

---

## Validation Layer

Verifies whether collected information is complete, coherent and internally consistent.

Examples:

* missing drivers
* incompatible versions
* incomplete installations
* invalid configurations

---

## Analysis Layer

Produces technical observations.

Examples:

* bottlenecks
* inconsistencies
* missing optimizations
* unsupported configurations

The analysis layer only produces facts.

---

## Recommendation Layer

Transforms validated observations into actionable recommendations.

Every recommendation must reference the evidence that produced it.

Recommendations are never generated without supporting observations.

---

## Report Layer

Produces human-readable reports.

Possible formats include:

* terminal output
* Markdown
* HTML
* JSON

Future formats may be added without affecting the inspection engine.

---

# LLM Integration

Language models are optional.

They may improve explanations and summaries but never participate in:

* data collection;
* validation;
* analysis;
* recommendation generation.

The inspection engine remains entirely functional without an LLM.

---

# Performance Objectives

The inspector must never interfere with AI workloads.

Target objectives:

* execution on demand;
* minimal CPU usage;
* no GPU usage by default;
* no persistent background process;
* no automatic monitoring unless explicitly requested.

---

# Repository Responsibilities

The project is organised around clear responsibilities.

* src/ contains the implementation.
* tests/ contains automated tests.
* docs/ contains project documentation.
* examples/ contains usage examples.
* tools/ contains development utilities.

---

# Future Extensions

The architecture is intentionally modular.

Future extensions may include:

* additional operating systems;
* NVIDIA support;
* Intel support;
* additional AI runtimes;
* plugin-based collectors;
* optional monitoring mode;
* graphical user interfaces.

These extensions should not require modifications to the inspection pipeline itself.
