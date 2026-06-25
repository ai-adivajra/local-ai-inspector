# ADR-0001 — Project Foundations

**Status:** Accepted
**Date:** 2026-06-25

---

# Context

Local AI Inspector aims to help users build, validate and optimize reliable local AI environments.

Before implementing any functionality, the project establishes a set of architectural and engineering principles intended to guide every future design decision.

These principles are considered foundational and should only change through a future Architecture Decision Record (ADR).

---

# Decision

The project adopts the following principles.

## 1. Observation first

The system observes before it analyzes.

Recommendations must always be based on collected evidence.

---

## 2. No automatic system modifications

Local AI Inspector never modifies the inspected system automatically.

Users remain fully responsible for applying recommendations.

---

## 3. Local-first

The inspection engine must work entirely offline.

Internet connectivity may enhance the user experience but must never be required for core functionality.

---

## 4. LLM optional

Language models improve explanations and summaries.

They are not part of the inspection engine itself.

The inspection engine must remain fully functional without an LLM.

---

## 5. On-demand execution

The default execution model is on-demand.

The application starts, performs an inspection, generates a report and exits.

Continuous monitoring is considered an optional future capability.

---

## 6. Zero interference

The inspector must never compete with the AI workloads it evaluates.

Resource consumption should remain minimal and predictable.

---

## 7. Incremental development

Every release must deliver practical value.

Features are added only when they solve an existing user problem.

Large speculative designs should be avoided.

---

## 8. Transparency

Every recommendation must be traceable to collected observations.

Users should always understand why a recommendation has been produced.

---

## 9. Community is not the objective

The project exists to solve real problems encountered while building local AI environments.

Community adoption is a consequence of building a useful tool, not a design objective.

---

# Consequences

These decisions imply that:

* the inspection engine remains independent from AI models;
* recommendations require supporting evidence;
* system modifications are always manual;
* documentation and code evolve together;
* simplicity is preferred over feature accumulation;
* new functionality must provide immediate value.

---

# Review

This ADR is expected to remain valid throughout the lifetime of the project.

Future changes to these principles should be introduced only through a new ADR rather than modifying this document.
