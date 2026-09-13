# Phase E Resources: Data Quality & Streaming
 
---
 
## Week 14 — Data Quality / Observability
 
**Primary:**
- [Great Expectations official docs — "Get started"](https://docs.greatexpectations.io/docs/) — the current open-source GX Core library; start with their quickstart before anything else.
- [DataCamp — "Introduction to Data Quality with Great Expectations"](https://www.datacamp.com/courses/introduction-to-data-quality-with-great-expectations) — free-tier accessible, hands-on, updated April 2026.
**Connecting back to your own docs:**
- Re-read your own `docs/dq_checklist.md` from the original roadmap before Monday — you already have a solid, practical checklist; this week is about implementing it in actual code (Great Expectations / dbt tests) rather than learning the concepts from scratch.
**Observability/monitoring specifically:**
- Search "data observability vs data quality" — worth understanding the distinction (quality = is this specific data correct; observability = do I have visibility into the health of the whole system) before Thursday/Friday's dashboard work.
- [dbt docs — "Data tests"](https://docs.getdbt.com/docs/build/data-tests) — since you already have dbt models from Phase B, this is the fastest path to adding quality checks to work you've already built.

---
 
## Week 15 — Kafka Basics
 
**Version note:** Kafka is now on version 4.x, which fully removed ZooKeeper in favor of KRaft mode for metadata management. If a tutorial tells you to install and run ZooKeeper, it's outdated — skip that step entirely.
 
**Primary:**
- [Apache Kafka official Quickstart](https://kafka.apache.org/quickstart) — short, current, and directly from the source. Confirm you're following the KRaft-mode instructions, not the legacy ZooKeeper ones.
- [freeCodeCamp — "The Apache Kafka Handbook"](https://www.freecodecamp.org/news/apache-kafka-handbook/) — free, long-form, written for exactly this stage of learning.
**Hands-on practice:**
- [DataCamp — "Introduction to Apache Kafka"](https://www.datacamp.com/courses/introduction-to-apache-kafka) — free tier available, covers topics/producers/consumers and basic architecture.
**Python client:**
- Search "confluent-kafka-python quickstart" — this is the standard Python client library; its own README has a minimal producer/consumer example that's the fastest way to get Python talking to Kafka.
---
 
## Week 16 — Real-Time Aggregations (Spark Structured Streaming)
 
**Engine choice, stated explicitly:** Spark Structured Streaming — because it builds directly on the PySpark skills from Phase C, rather than requiring you to learn an entirely separate engine (Flink) this early. Flink comes later, in Phase J, specifically as a point of comparison once you have a real baseline to compare it against.
 
**Primary:**
- [Official Structured Streaming Programming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) — this is genuinely one of the best-written guides in the whole Spark documentation; read the "Quick Example" and "Window Operations" sections closely.
- Search "Spark Structured Streaming Kafka integration guide" — official Spark docs include a dedicated Kafka integration guide; you'll need this to connect Week 15's Kafka topics to this week's streaming jobs.
**Windowing/watermarks specifically:**
- The Programming Guide's "Handling Late Data and Watermarking" section — read this twice; watermarking is the single most conceptually tricky part of this week and is worth slow, careful reading rather than skimming.
**Exactly-once semantics:**
- Search "Spark Structured Streaming exactly-once guarantees checkpointing" — this connects directly to Phase D's idempotency lessons from Airflow backfills; the underlying problem (don't process the same data twice) is the same one, just in a different tool.
 