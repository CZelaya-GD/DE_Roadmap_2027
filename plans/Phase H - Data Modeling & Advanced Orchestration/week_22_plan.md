# Week 22 Plan: Data Contracts & Schema Evolution

## Overview

- **Phase:** H — Data Modeling & Advanced Orchestration
- **Focus:** Managing change safely across system boundaries
- **Goal:** Understand how to let schemas evolve without silently breaking every downstream consumer — the problem that causes a disproportionate share of real production data incidents
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** What a data contract actually is (an agreement between producer and consumer, enforced in code), and why "just tell people before you change a column" fails at scale → Deliverable: 1 written data contract for one of your existing pipelines, specifying schema, semantics, SLAs, and ownership
- **Tuesday:** Schema evolution compatibility types — backward, forward, full, none — and what each actually permits → Deliverable: 4 worked examples, one per compatibility type, showing a change that passes and one that fails
- **Wednesday:** Avro and Schema Registry in practice, applied to your Week 15 Kafka topics → Deliverable: 1 Kafka topic with a registered schema, plus 1 successful and 1 rejected schema evolution attempt
- **Thursday:** dbt model contracts — enforcing column names and types on your existing dbt models → Deliverable: contracts added to 3 existing dbt models, with a deliberate breaking change caught by the contract
- **Friday:** Breaking-change workflow — how to actually deprecate a column in a system with real consumers (versioning, dual-write periods, deprecation notices) → Deliverable: 1 written migration plan for a breaking change to one of your own models

### Anki Targets

- Monday: 5 cards tagged `governance::data-contracts`
- Tuesday: 5 cards tagged `governance::schema-evolution`
- Wednesday: 5 cards tagged `governance::schema-registry`
- Thursday: 5 cards tagged `governance::dbt-contracts`
- Friday: 5 cards tagged `governance::breaking-changes`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Explain out loud the difference between backward and forward compatibility, with a concrete example of each
- Draft next week's objectives (Dagster)

---

## Week 22 Success Metrics
- [ ] 25 Anki cards created
- [ ] 1 written data contract for a real pipeline of yours
- [ ] 1 Kafka topic with schema registry enforcement, tested with a rejected evolution
- [ ] Contracts added to 3 dbt models
- [ ] 1 breaking-change migration plan written
- [ ] Week 23 plan drafted