# Week 8 Plan: Query Optimization + Production Load

## Overview

- **Phase:** B — Warehouse & Transformation
- **Focus:** BigQuery performance and cost discipline
- **Goal:** Optimize the pipeline built in Weeks 6–7 and understand cost/performance trade-offs well enough to explain them to a non-technical stakeholder
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** Reading EXPLAIN plans, understanding slot usage, identifying partition pruning in a query plan → Deliverable: 5 queries with EXPLAIN output documented and explained in your own words
- **Tuesday:** Clustering (in addition to partitioning), materialized views, before/after cost comparison → Deliverable: 3 optimized queries with documented cost reduction
- **Wednesday:** Take the pipeline built in Weeks 6–7 and harden it for production: schema enforcement, incremental materialization in dbt → Deliverable: hardened, incremental version of your Week 7 mart model
- **Thursday:** Cost optimization pass — apply partitioning/clustering to the hardened pipeline, document total cost reduction → Deliverable: cost report comparing Week 6 baseline to now
- **Friday:** Build a simple dashboard (Metabase) on top of your mart models, stakeholder-readable → Deliverable: working dashboard with 3–5 charts

### Anki Targets

- Monday: 5 cards tagged `sql::advanced::optimization`
- Tuesday: 5 cards tagged `cloud::bigquery::clustering`
- Wednesday: 5 cards tagged `transformation::dbt::incremental`
- Thursday: 5 cards tagged `cloud::bigquery::cost`
- Friday: 5 cards tagged `analytics::dashboards`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Rebuild one optimized query from memory, explaining the reasoning behind each optimization
- Draft next week's objectives (DuckDB + Sprint Review)

---

## Week 8 Success Metrics
- [ ] 25 Anki cards created
- [ ] 8 optimized queries written with documented before/after
- [ ] Weeks 6–7 pipeline hardened into a production-style incremental model
- [ ] 1 dashboard built on top of it
- [ ] Week 9 plan drafted