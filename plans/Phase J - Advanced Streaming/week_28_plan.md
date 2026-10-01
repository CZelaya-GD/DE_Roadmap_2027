# Week 28 Plan: Flink Fundamentals (Contrast with Spark Structured Streaming)

## Overview

- **Phase:** J — Advanced Streaming (final week)
- **Focus:** A second streaming engine, deliberately compared against the first
- **Goal:** Understand Flink's stream-first model well enough to rebuild Phase E's aggregation pipeline in it, and articulate concretely when you'd choose Flink over Spark Structured Streaming
- **Anki Target:** 25 cards
- **Version note:** Flink 2.2 is current stable as of 2026 (1.20 is the LTS line) — use docs/tutorials referencing 1.18+ or 2.x

---

## Monday–Friday

### Daily Objectives

- **Monday:** Flink's architecture (JobManager, TaskManager), the Docker Playgrounds environment, stream-first vs. micro-batch philosophy (contrast directly with Spark Structured Streaming from Phase E) → Deliverable: local Flink cluster running via Docker Playgrounds, UI explored
- **Tuesday:** DataStream API basics (or PyFlink's Python equivalent), sources and sinks, your first Flink streaming job → Deliverable: 1 working Flink job reading from a socket or file source
- **Wednesday:** Connect Flink to your existing Kafka topics (Phase E, Week 15) → Deliverable: 1 Flink job consuming live from Kafka
- **Thursday:** Windowing and state management in Flink — rebuild one of your Phase E, Week 16 windowed aggregations in Flink → Deliverable: 1 aggregation pipeline implemented in both Spark Structured Streaming and Flink, side by side
- **Friday:** Direct comparison — latency, state management sophistication, operational complexity — write up when you'd choose each → Deliverable: written comparison document with a clear recommendation framework

### Anki Targets

- Monday: 5 cards tagged `streaming::flink::fundamentals`
- Tuesday: 5 cards tagged `streaming::flink::datastream-api`
- Wednesday: 5 cards tagged `streaming::flink::kafka-integration`
- Thursday: 5 cards tagged `streaming::flink::state-windowing`
- Friday: 5 cards tagged `streaming::flink::vs-spark`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Phase
- Review all Anki cards from the week
- Explain out loud, unprompted, one concrete scenario where you'd choose Flink over Spark Structured Streaming, and one where you'd choose the opposite
- Write a Phase J retrospective connecting this back to Phase D's idempotency lessons and Phase E's watermarking work — how does state management in Flink relate to those earlier concepts?
- Draft Phase K objectives (Data Cataloging/Lineage, PII/Compliance, FinOps)

---

## Week 28 Success Metrics
- [ ] 25 Anki cards created
- [ ] 1 Flink job consuming live from your existing Kafka infrastructure
- [ ] 1 windowed aggregation implemented in both Spark Structured Streaming and Flink
- [ ] Written comparison document completed
- [ ] Phase J retrospective written
- [ ] Phase K (Week 29) plan drafted