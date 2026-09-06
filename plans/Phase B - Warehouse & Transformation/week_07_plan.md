# Week 7 Plan: dbt Fundamentals (Staging → Intermediate → Marts)

## Overview

- **Phase:** B — Warehouse & Transformation
- **Focus:** dbt transformation layer
- **Goal:** Build a complete dbt project with staging, intermediate, and mart models on top of Week 6's BigQuery tables
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** dbt setup, project initialization, connecting to Week 6's BigQuery dataset, first staging model → Deliverable: working dbt project, 1 staging model
- **Tuesday:** Staging models for all source tables, `ref()` and `source()` patterns → Deliverable: 3–5 staging models
- **Wednesday:** Intermediate models (business logic, joins, aggregations) → Deliverable: 2–3 intermediate models
- **Thursday:** Mart models (final business-ready tables), materialization strategies (view vs. table vs. incremental) → Deliverable: 2 mart models
- **Friday:** dbt tests (schema tests + custom data tests), documentation generation (`dbt docs generate`) → Deliverable: all models tested, docs site generated and viewed locally

### Anki Targets

- Monday: 5 cards tagged `transformation::dbt::setup`
- Tuesday: 5 cards tagged `transformation::dbt::staging`
- Wednesday: 5 cards tagged `transformation::dbt::intermediate`
- Thursday: 5 cards tagged `transformation::dbt::marts`
- Friday: 5 cards tagged `transformation::dbt::testing`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Rebuild one dbt model from memory (staging → mart)
- Draft next week's objectives (Query Optimization + Production Load)

---

## Week 7 Success Metrics
- [ ] 25 Anki cards created
- [ ] 5–10 dbt models written across staging/intermediate/marts
- [ ] dbt project with passing tests and generated docs
- [ ] Can explain the staging → intermediate → marts pattern without notes
- [ ] Week 8 plan drafted