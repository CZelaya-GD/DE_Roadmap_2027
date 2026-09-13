# Week 16 Plan: Real-Time Aggregations (Spark Structured Streaming)

## Overview

- **Phase:** E — Data Quality & Streaming (final week)
- **Focus:** Streaming transformations and windowed aggregations
- **Goal:** Connect Week 15's Kafka topics to Spark Structured Streaming and build real windowed aggregations — this closes the loop between "events exist" (Week 15) and "I can compute something useful from them in real time" (this week)
- **Anki Target:** 25 cards
- **Engine:** Spark Structured Streaming (chosen explicitly — builds on Phase C's PySpark work; Flink comes later in Phase J as a deliberate comparison point)

---

## Monday–Friday

### Daily Objectives

- **Monday:** Structured Streaming programming model (treating a stream as an "unbounded table"), reading from a socket/file source as a warm-up before Kafka → Deliverable: 1 simple streaming query reading from a local file source
- **Tuesday:** Connect Structured Streaming to Week 15's Kafka topic, basic streaming transformations (select, filter) on the incoming stream → Deliverable: 1 streaming job reading live from Kafka
- **Wednesday:** Windowed aggregations — tumbling windows, sliding windows, computing a running count/average over time → Deliverable: 2 windowed aggregation queries against your Kafka stream
- **Thursday:** Watermarking and late data handling (read the official guide's watermarking section closely before starting) → Deliverable: 1 streaming query with watermarking configured, tested with intentionally late-arriving data
- **Friday:** Exactly-once semantics via checkpointing — connect this conceptually back to Phase D's idempotent backfill lessons (same underlying problem: don't process the same data twice) → Deliverable: 1 streaming pipeline with checkpointing configured, tested by restarting it mid-stream and confirming no duplicate processing

### Anki Targets

- Monday: 5 cards tagged `streaming::spark::fundamentals`
- Tuesday: 5 cards tagged `streaming::spark::kafka-integration`
- Wednesday: 5 cards tagged `streaming::spark::windowing`
- Thursday: 5 cards tagged `streaming::spark::watermarking`
- Friday: 5 cards tagged `streaming::spark::exactly-once`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Phase
- Review all Anki cards from the week
- Explain out loud why watermarking is necessary and what happens without it
- Write a short retrospective on Phase E as a whole (Weeks 14–16): what felt solid, what still feels shaky
- Draft Phase F objectives (Docker & Containerization)

---

## Week 16 Success Metrics
- [ ] 25 Anki cards created
- [ ] 1 streaming job reading live from your Week 15 Kafka topic
- [ ] 2+ windowed aggregation queries working correctly
- [ ] 1 pipeline surviving a restart without duplicating data (exactly-once verified)
- [ ] Phase E retrospective written
- [ ] Phase F (Week 17) plan drafted