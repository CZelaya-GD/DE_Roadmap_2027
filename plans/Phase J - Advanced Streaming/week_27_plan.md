# Week 27 Plan: CDC Deep-Dive (Debezium)

## Overview

- **Phase:** J — Advanced Streaming
- **Focus:** Change Data Capture
- **Goal:** Understand how database changes become a real-time event stream without polling — connecting a traditional database (like your Phase B/dbt work) into your existing Kafka pipeline (Phase E) for the first time
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** What CDC actually solves (why polling for changes is inefficient and misses deletes), write-ahead logs / binlogs conceptually, log-based vs. trigger-based CDC → Deliverable: written explanation of why Debezium reads the WAL instead of querying tables directly
- **Tuesday:** Kafka Connect fundamentals (Debezium runs as a Kafka Connect source connector), install and configure Kafka Connect locally → Deliverable: Kafka Connect running locally, verified via its REST API
- **Wednesday:** Configure a Debezium connector against a PostgreSQL database containing one of your own Phase B tables → Deliverable: working Debezium connector streaming real row-level changes into a Kafka topic
- **Thursday:** Event message format — understanding the before/after payload structure Debezium produces, handling inserts/updates/deletes differently downstream → Deliverable: 1 consumer script that correctly distinguishes and handles all three change types
- **Friday:** Replication slots and offset tracking — what happens if Debezium goes down and comes back up (does it lose changes?) — test this deliberately → Deliverable: documented test showing Debezium correctly resumes from where it left off after a restart

### Anki Targets

- Monday: 5 cards tagged `streaming::cdc::fundamentals`
- Tuesday: 5 cards tagged `streaming::cdc::kafka-connect`
- Wednesday: 5 cards tagged `streaming::cdc::debezium-setup`
- Thursday: 5 cards tagged `streaming::cdc::event-format`
- Friday: 5 cards tagged `streaming::cdc::fault-tolerance`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Explain out loud why log-based CDC has near-zero performance impact on the source database, compared to polling
- Draft next week's objectives (Flink Fundamentals)

---

## Week 27 Success Metrics
- [ ] 25 Anki cards created
- [ ] Working Debezium connector streaming real changes from one of your own tables
- [ ] 1 consumer correctly handling insert/update/delete events differently
- [ ] Verified restart-recovery test (no lost changes after a restart)
- [ ] Week 28 plan drafted