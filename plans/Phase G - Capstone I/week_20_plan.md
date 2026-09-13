# Week 20 Plan: Flagship Project I

## Overview

- **Phase:** G — Capstone I (final week of the original 5-month scope)
- **Focus:** Integration — combining everything from Weeks 1–19 into one coherent, portfolio-ready system
- **Goal:** Build one project that demonstrates batch processing, streaming, AI-augmented retrieval, and production-grade infrastructure discipline — all together, all in one repo
- **Anki Target:** 10 cards (this week is building, not new-concept learning)

---

## Suggested Architecture

A concrete shape to build toward (adapt freely to your own idea, but this combination touches everything you've learned):

1. **Batch layer:** A dataset loaded and transformed through BigQuery + dbt (Phase B), following the staging → marts pattern
2. **Streaming layer:** A simulated real-time event source flowing through Kafka into a Spark Structured Streaming job computing windowed aggregations (Phase E)
3. **Orchestration:** Both layers scheduled and monitored through Airflow, with retries and alerting configured (Phase D)
4. **AI layer:** A RAG pipeline that lets a user ask natural-language questions about the data or documentation describing it (Phase G, Week 19)
5. **Infrastructure:** The whole system containerized with Docker, with at least the storage/IAM pieces provisioned via Terraform, budget alert included (Phase F)
6. **Quality:** Data quality checks running on both the batch and streaming layers, with a visible pass/fail status (Phase E, Week 14)

---

## Monday–Friday

### Daily Objectives

- **Monday:** Architecture planning — sketch the full system on paper/diagram first, identify which existing pieces from Weeks 1–19 you're reusing vs. building fresh → Deliverable: 1 architecture diagram, 1 list of reused components
- **Tuesday:** Wire together the batch + orchestration layers, confirm Airflow correctly schedules and monitors the BigQuery/dbt pipeline → Deliverable: working batch pipeline, orchestrated
- **Wednesday:** Wire together the streaming layer, confirm Kafka → Spark Structured Streaming runs alongside the batch layer without conflict → Deliverable: working streaming pipeline, running concurrently with the batch layer
- **Thursday:** Integrate the RAG layer so it can answer questions using data/documentation from the pipeline itself, containerize the full system → Deliverable: working RAG interface, full system running via Docker Compose
- **Friday:** Add data quality checks with visible status, write the project README (architecture, design decisions, how to run it), final polish → Deliverable: complete, documented, portfolio-ready project

### Anki Targets

- Just 10 cards total this week, tagged `capstone::flagship-1`, covering any genuinely new integration insight (not re-covering material from earlier weeks)

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Reflect on the First 20 Weeks
- No new Anki review this week — instead, write a longer reflection:
  - What part of this project are you proudest of?
  - What part would you do differently if starting Week 1 again?
  - Which Phase's material do you still feel least confident in? (Be honest — this becomes a standing review item for Phase H onward.)
- Draft Phase H objectives (Data Modeling & Advanced Orchestration — the start of the new 8-month territory)

---

## Week 20 / Flagship Project I Success Metrics
- [ ] Complete, working, end-to-end project combining batch, streaming, AI, and infrastructure-as-code
- [ ] Clean architecture diagram and README
- [ ] Project pushed to your GitHub, publicly viewable
- [ ] 20-week reflection written
- [ ] Phase H (Week 21) plan drafted