# Week 26 Plan: GCP Deep-Dive (Dataflow, Cloud Composer)

## Overview

- **Phase:** I — Advanced Cloud & CI/CD (final week)
- **Focus:** GCP's managed data processing and orchestration services
- **Goal:** Understand Dataflow (managed Apache Beam) and Cloud Composer (managed Airflow) — and understand *why* a company chooses managed services over self-hosting the same tools you built by hand in Phases C and D
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** Apache Beam programming model (PCollections, PTransforms, unified batch/streaming model) → Deliverable: 1 simple Beam pipeline run locally (DirectRunner)
- **Tuesday:** Dataflow specifically — running the same Beam pipeline on Google's managed runner, autoscaling behavior → Deliverable: 1 pipeline deployed and run on actual Dataflow (not just local)
- **Wednesday:** Dataflow templates — using a pre-built template vs. writing custom Beam code, when each approach makes sense → Deliverable: 1 Dataflow job run from a template
- **Thursday:** Cloud Composer — set up a Composer environment, understand it as "managed Airflow," migrate one Phase D DAG to run on it → Deliverable: 1 of your Week 12–13 Airflow DAGs running on Composer instead of locally
- **Friday:** Managed vs. self-hosted trade-offs — cost, operational burden, control — write a comparison connecting this week to Phases C, D, and F → Deliverable: written comparison: PySpark+Airflow+Docker (self-managed) vs. Dataflow+Composer (managed), with a recommendation for a hypothetical small team vs. a large one

### Anki Targets

- Monday: 5 cards tagged `cloud::gcp::dataflow`
- Tuesday: 5 cards tagged `cloud::gcp::dataflow`
- Wednesday: 5 cards tagged `cloud::gcp::dataflow-templates`
- Thursday: 5 cards tagged `cloud::gcp::composer`
- Friday: 5 cards tagged `cloud::gcp::managed-vs-self-hosted`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Phase
- Review all Anki cards from the week
- Explain out loud, unprompted, when you'd recommend a team use Dataflow+Composer versus self-managed PySpark+Airflow
- Write a Phase I retrospective: how has your sense of "what running something in production actually requires" changed since Phase F?
- Draft Phase J objectives (CDC/Debezium, Flink Fundamentals)

---

## Week 26 Success Metrics
- [ ] 25 Anki cards created
- [ ] 1 Beam pipeline run both locally and on Dataflow
- [ ] 1 Airflow DAG successfully migrated to Cloud Composer
- [ ] Written managed-vs-self-hosted comparison completed
- [ ] Phase I retrospective written
- [ ] Phase J (Week 27) plan drafted