# Phase J Resources: Advanced Streaming (CDC & Flink)

---

## Week 27 — CDC Deep-Dive (Debezium)

**Primary:**
- [Debezium official documentation](https://debezium.io/documentation/) — the authoritative source, actively maintained.
- [OneUptime — "How to Set Up Debezium for Change Data Capture"](https://oneuptime.com/blog/post/2026-01-27-debezium-change-data-capture/view) — a current (Jan 2026), practical, step-by-step guide covering Kafka Connect setup and PostgreSQL/MySQL connector configuration — good as a hands-on companion to the official docs.

**PostgreSQL-specific (recommended starting database, since it's what you've used since Phase A):**
- [OneUptime — "How to Stream Changes with Debezium CDC in PostgreSQL"](https://oneuptime.com/blog/post/2026-01-25-debezium-cdc-postgresql/view) — walks through the exact setup this week needs.

**Core concepts to prioritize:**
- Write-ahead logs (WAL) / binlogs, replication slots, and why log-based CDC has near-zero impact on the source database compared to polling — this is the "why" that makes the rest of the week's syntax make sense.

**Connecting to your own work:**
- Set up Debezium against a Postgres instance containing one of your Phase B tables, and stream its changes into a Kafka topic (Phase E) — this directly reuses your existing Kafka knowledge rather than treating CDC as an isolated topic.

---

## Week 28 — Flink Fundamentals (Contrast with Spark Structured Streaming)

**Primary:**
- [Apache Flink official docs — "Getting Started"](https://flink.apache.org/getting-started/with-flink) — start with the Docker Playgrounds option; it's the fastest way to see a real Flink cluster running without a manual install.
- [Apache Flink DataStream API Tutorial](https://nightlies.apache.org/flink/flink-docs-stable/docs/try-flink/datastream/) — official, hands-on, walks through building a real streaming application.
- Search "PyFlink getting started" — since you've been working in Python throughout the roadmap, PyFlink (Flink's Python API) is the more directly relevant entry point than Java/Scala, though it's worth knowing Flink's most mature APIs are still Java-based.

**Current version note:** Flink 2.2 is the current stable release as of 2026 (1.20 is the LTS line) — prefer docs/tutorials referencing 1.18+ or 2.x, since Flink's API has evolved meaningfully over the years.

**The comparison to Spark Structured Streaming — the actual point of this week:**
- Flink is built stream-first (batch is treated as a special case of streaming); Spark Structured Streaming is built batch-first (streaming is micro-batches under the hood). This affects latency characteristics and how naturally each handles certain problems (Flink generally offers lower latency and more sophisticated state management out of the box). Rebuilding your Phase E Week 16 aggregation pipeline in Flink and comparing the two directly is more valuable than reading about the difference abstractly.

**State management specifically:**
- Search "Flink state management keyed state" — this is Flink's standout feature relative to Spark Structured Streaming and worth understanding in some depth, since it's often the deciding factor in real-world engine choice.