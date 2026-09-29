# Week 23 Plan: Dagster (Second Orchestrator, Contrasted with Airflow)

## Overview

- **Phase:** H — Data Modeling & Advanced Orchestration (final week)
- **Focus:** Asset-based orchestration
- **Goal:** Learn Dagster not as "a second tool to know" but as a different mental model for orchestration — understand deeply why it exists and what it does that Airflow doesn't do as naturally
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** Dagster's core concept — software-defined assets (`@asset`), the declarative model vs. Airflow's imperative task sequencing → Deliverable: 1 simple Dagster project with 3 dependent assets, run locally via `dg dev`
- **Tuesday:** Asset lineage and the Dagster UI's asset graph — compare this directly to how you'd visualize the same pipeline in Airflow's Grid view → Deliverable: 1 written comparison of how the same pipeline looks/behaves in each tool
- **Wednesday:** Rebuild one of your Week 12–13 Airflow DAGs as a Dagster asset graph → Deliverable: 1 pipeline implemented in both Airflow and Dagster, side by side
- **Thursday:** Schedules, sensors, and partitions in Dagster — compare to Airflow's equivalent concepts → Deliverable: 1 scheduled, partitioned Dagster asset
- **Friday:** Data quality checks as first-class Dagster concepts (asset checks) — connect back to Phase E's data quality work → Deliverable: 1 Dagster asset with an attached asset check that fails on bad data

### Anki Targets

- Monday: 5 cards tagged `orchestration::dagster::fundamentals`
- Tuesday: 5 cards tagged `orchestration::dagster::lineage`
- Wednesday: 5 cards tagged `orchestration::dagster::vs-airflow`
- Thursday: 5 cards tagged `orchestration::dagster::scheduling`
- Friday: 5 cards tagged `orchestration::dagster::quality-checks`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Phase
- Review all Anki cards from the week
- Write a short comparison note: in what situation would you reach for Airflow vs. Dagster, and why? (This is a genuinely common interview question.)
- Write a Phase H retrospective: how has your understanding of "structuring data well" changed since Phase B?
- Draft Phase I objectives (Kubernetes, CI/CD, GCP deep-dive)

---

## Week 23 Success Metrics
- [ ] 25 Anki cards created
- [ ] 1 pipeline implemented in both Airflow and Dagster for direct comparison
- [ ] 1 scheduled, partitioned Dagster asset
- [ ] 1 Dagster asset check catching bad data
- [ ] Can articulate, unprompted, when you'd choose one orchestrator over the other
- [ ] Phase H retrospective written
- [ ] Phase I (Week 24) plan drafted