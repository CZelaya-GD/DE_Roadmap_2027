# Week 15 Plan: Kafka Basics

## Overview

- **Phase:** E — Data Quality & Streaming
- **Focus:** Event streaming fundamentals
- **Goal:** Understand Kafka's core model (topics, partitions, producers, consumers) well enough to build a simple real-time data flow — this is the foundation Week 16's aggregations sit on
- **Anki Target:** 25 cards
- **Version note:** Use Kafka 4.x with KRaft mode. If any resource has you installing ZooKeeper, skip it — that's outdated.

---

## Monday–Friday

### Daily Objectives

- **Monday:** What Kafka actually is (distributed log, not a queue), topics, partitions, brokers, install Kafka locally in KRaft mode → Deliverable: local Kafka instance running, 1 topic created via CLI
- **Tuesday:** Producers — writing messages to a topic via CLI and via Python (`confluent-kafka-python`) → Deliverable: 1 Python producer script sending real messages
- **Wednesday:** Consumers — reading messages, consumer groups, offsets (and what "replaying" a stream actually means) → Deliverable: 1 Python consumer script, tested by replaying from the beginning of a topic
- **Thursday:** Message serialization (JSON to start, brief intro to Avro/Schema Registry conceptually), partitioning strategy (how keys affect which partition a message lands in) → Deliverable: 1 producer/consumer pair using structured (JSON) messages with a defined key strategy
- **Friday:** Build a simple end-to-end flow — a Python script simulating an event source (e.g. fake "orders" or "clicks") producing continuously, and a consumer printing them in real time → Deliverable: working producer/consumer pair running simultaneously

### Anki Targets

- Monday: 5 cards tagged `streaming::kafka::fundamentals`
- Tuesday: 5 cards tagged `streaming::kafka::producers`
- Wednesday: 5 cards tagged `streaming::kafka::consumers`
- Thursday: 5 cards tagged `streaming::kafka::serialization`
- Friday: 5 cards tagged `streaming::kafka::pipeline`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Explain out loud why Kafka is a "distributed log" rather than a traditional message queue, and why that distinction matters
- Draft next week's objectives (Real-Time Aggregations with Spark Structured Streaming)

---

## Week 15 Success Metrics
- [ ] 25 Anki cards created
- [ ] Local Kafka running in KRaft mode (no ZooKeeper)
- [ ] Working Python producer and consumer
- [ ] 1 continuously running producer/consumer demo
- [ ] Can explain consumer groups and offsets without notes
- [ ] Week 16 plan drafted