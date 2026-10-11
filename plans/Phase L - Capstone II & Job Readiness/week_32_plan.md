# Week 32 Plan: Flagship Project II

## Overview

- **Phase:** L — Capstone II & Job Readiness
- **Focus:** A more ambitious, production-minded integration project
- **Goal:** Build a second portfolio-defining system that demonstrates what Flagship I could not — proper data modeling, automated testing/CI, CDC-based ingestion, governance, and cost discipline
- **Anki Target:** 10 cards (building week, not new-concept week)
- **How it differs from Flagship I:** Flagship I proved you can *build* a working pipeline. Flagship II proves you can build one a team could *trust, maintain, and afford*.

---

## Suggested Architecture

Adapt freely to your own idea, but aim to touch each of these:

1. **Ingestion via CDC:** A Postgres source database changing continuously, streamed through Debezium into Kafka (Phase J, Week 27)
2. **Processing:** Stream processing in Spark Structured Streaming or Flink for real-time metrics, plus batch transforms into the warehouse (Phases C, E, J)
3. **Modeling:** A proper star schema in the warehouse with at least one SCD Type 2 dimension, built with dbt and enforced with model contracts (Phase H, Weeks 21–22)
4. **Orchestration:** Airflow or Dagster scheduling the batch layer, with retries, alerting, and idempotent backfills (Phases D, H)
5. **CI/CD:** GitHub Actions running pytest and `dbt test` on every pull request, with linting gates (Phase I, Week 25)
6. **Infrastructure:** Everything containerized; core cloud resources provisioned with Terraform, labeled for cost attribution (Phases F, K)
7. **Governance:** Catalog with column-level lineage, PII columns identified and access-restricted, and a short cost report (Phase K, Weeks 29–31)
8. **Documentation:** Architecture diagram plus 3–5 short Architecture Decision Records explaining your key choices

---

## Monday–Friday

### Daily Objectives

- **Monday:** Design before building — architecture diagram, data model (fact/dimension design on paper), and ADRs for your 3 biggest decisions → Deliverable: architecture diagram, star schema diagram, 3 written ADRs
- **Tuesday:** Build the ingestion layer — source Postgres database, Debezium CDC into Kafka, verify changes flowing end-to-end → Deliverable: working CDC pipeline with a simulated, continuously changing source
- **Wednesday:** Build the processing and modeling layers — streaming metrics plus dbt star schema with SCD Type 2 and model contracts → Deliverable: working transformation layer with passing dbt tests
- **Thursday:** Wire in orchestration, CI/CD, and containerization — GitHub Actions on every PR, Docker Compose for the full system, Terraform for core cloud resources → Deliverable: a pull request that triggers automated tests, and a system that starts with one command
- **Friday:** Governance and polish — catalog ingestion with lineage, PII protection applied, cost report written, README completed → Deliverable: complete, documented, publicly viewable repository

### Anki Targets

- 10 cards total this week, tagged `capstone::flagship-2`, covering only genuinely new integration lessons

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Write a brief self-review of the project: what would a senior engineer criticize first? Note it honestly — this becomes next week's practice material for explaining trade-offs
- Draft next week's objectives (System Design Practice & Mock Interviews)

---

## Week 32 Success Metrics
- [ ] End-to-end system running: CDC → streaming → warehouse → catalog
- [ ] Star schema with SCD Type 2 and model contracts
- [ ] CI pipeline running automatically on pull requests
- [ ] PII columns identified and access-restricted
- [ ] 3+ ADRs and an architecture diagram in the repo
- [ ] Project pushed to GitHub, publicly viewable
- [ ] Week 33 plan drafted