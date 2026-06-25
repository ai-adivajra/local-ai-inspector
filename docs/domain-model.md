# Domain Model

**Version:** 1.0
**Status:** Accepted
**Last updated:** 2026-06-25

---

# Purpose

This document defines the core business objects manipulated by Local AI Inspector.

The domain model is independent of the programming language, operating system and user interface.

It describes **what the software knows**, not **how it is implemented**.

---

# Core Principle

Everything begins with an **Inspection**.

An inspection represents the complete observation of one local AI environment at a specific point in time.

```text
Inspection
    │
    ├── System
    ├── AI Stack
    ├── Observations
    ├── Findings
    ├── Recommendations
    └── Report
```

The Inspection is the root object of the domain.

---

# Inspection

Represents one execution of Local AI Inspector.

Responsibilities:

* identify the inspected machine;
* store collected observations;
* store validation results;
* store recommendations;
* generate reports.

An Inspection never modifies the inspected system.

---

# System

Represents the host environment.

It contains factual information only.

Typical components include:

* Operating System
* Kernel
* CPU
* Memory
* GPU
* Storage
* Motherboard
* Network

The System object never contains recommendations.

---

# AI Stack

Represents software used for local AI workloads.

Examples include:

* ROCm
* Ollama
* llama.cpp
* Python
* PyTorch
* Open WebUI
* ComfyUI
* vLLM

Each component exposes factual information such as:

* version
* installation status
* configuration
* availability

---

# Collector

Collectors obtain raw information from the system.

Examples:

* CPU Collector
* GPU Collector
* ROCm Collector
* Python Collector
* Ollama Collector

Collectors never interpret information.

They only observe.

---

# Observation

An Observation is one normalized piece of collected information.

Examples:

* CPU model
* GPU VRAM
* Installed Python version
* Installed ROCm version
* Ollama service status

Observations are immutable.

They represent facts.

---

# Validation

Validation verifies that observations are complete and internally consistent.

Examples:

* missing packages;
* incompatible versions;
* unavailable services;
* incomplete installations.

Validation produces Findings.

---

# Finding

A Finding is a technical conclusion derived from validated observations.

Examples:

* ROCm not detected;
* GPU driver mismatch;
* unsupported kernel;
* Python virtual environments unavailable.

Findings remain objective.

They never suggest actions.

---

# Recommendation

Recommendations transform Findings into practical actions.

Every Recommendation must reference one or more Findings.

Without Findings there can be no Recommendations.

---

# Report

Reports present inspection results.

Supported formats may include:

* Terminal
* Markdown
* HTML
* JSON

Reports never perform analysis.

They only present results.

---

# Relationships

```text
Inspection
│
├── System
├── AI Stack
│
├── Collectors
│
├── Observations
│
├── Validation
│
├── Findings
│
├── Recommendations
│
└── Reports
```

Every layer depends only on the previous one.

---

# Design Rules

The following rules are fundamental.

* Collectors never analyze.
* Validation never collects.
* Findings never recommend.
* Recommendations always reference Findings.
* Reports never modify collected data.
* LLMs never replace the inspection engine.
* Every recommendation must be traceable to collected evidence.

---

# Future Evolution

The domain model has been designed to evolve without breaking its core concepts.

Future versions may introduce **Capabilities**.

A Capability represents something the inspected system is able to provide rather than a specific software package.

Examples include:

* Python Capability
* ROCm Capability
* GPU Compute Capability
* Container Capability
* AI Runtime Capability

Capabilities make it possible to answer questions such as:

* Is this machine ready for Ollama?
* Can this system support ComfyUI?
* Is the Python environment suitable for AI development?

Capabilities are derived from existing Observations and Findings.

They do not replace the inspection model.

---

# Validation Profiles

Future versions may also introduce Validation Profiles.

A Validation Profile defines the requirements for a specific workload or application.

Examples include:

* Ollama Profile
* Open WebUI Profile
* ComfyUI Profile
* Stable Diffusion Profile
* vLLM Profile

Profiles evaluate existing Capabilities rather than collecting new data.

This allows the inspection engine to remain generic while supporting multiple AI ecosystems.

---

# Long-term Stability

The concepts defined in this document are expected to remain stable over the lifetime of the project.

Supporting new hardware, operating systems or AI runtimes should normally require implementing new Collectors rather than modifying the core domain model.
