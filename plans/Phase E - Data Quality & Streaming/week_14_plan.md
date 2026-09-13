# Week 14 Plan: Data Quality / Observability

## Overview

- **Phase:** E — Data Quality & Streaming
- **Focus:** Implementing data quality checks and observability into pipelines you've already built
- **Goal:** Move data quality from "a checklist you read" (your own `dq_checklist.md`) to "code that actually runs and blocks bad data automatically"
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** Data quality dimensions (completeness, uniqueness, validity, timeliness, consistency), re-read your own `dq_checklist.md` and map each dimension to a concrete check → Deliverable: written mapping of your checklist's items to the 5 dimensions
- **Tuesday:** Great Expectations setup, first Expectations against a real dataset (one of your Phase B staging tables) → Deliverable: 5 Expectations written and passing/failing correctly against real data
- **Wednesday:** dbt data tests (schema tests + custom singular tests) added to your Phase B dbt project → Deliverable: 5 dbt tests added, at least one custom singular test
- **Thursday:** Anomaly detection basics — simple statistical checks (row count deltas day-over-day, null rate spikes) → Deliverable: 1 script that flags an anomaly in a sample dataset you intentionally corrupt
- **Friday:** Build a simple data quality dashboard showing pass/fail status across your checks → Deliverable: working DQ status view (Metabase or a simple script-generated report)

### Anki Targets

- Monday: 5 cards tagged `quality::dimensions`
- Tuesday: 5 cards tagged `quality::great-expectations`
- Wednesday: 5 cards tagged `quality::dbt-tests`
- Thursday: 5 cards tagged `quality::anomaly-detection`
- Friday: 5 cards tagged `quality::observability`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Explain out loud the difference between "data quality" and "data observability"
- Draft next week's objectives (Kafka Basics)

---

## Week 14 Success Metrics
- [ ] 25 Anki cards created
- [ ] 5+ Great Expectations checks running against real data
- [ ] 5+ dbt tests added to your existing project
- [ ] 1 anomaly-detection script that correctly flags corrupted data
- [ ] 1 working DQ status dashboard/report
- [ ] Week 15 plan drafted