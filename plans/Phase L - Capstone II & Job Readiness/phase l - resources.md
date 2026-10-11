# Phase L Resources: Capstone II & Job Readiness

---

## Week 32 — Flagship Project II

**No new learning resource this week** — like Week 20, this is integration. But this time the bar is higher, so pull from the specific phases that came *after* Flagship I:
- Phase H: dimensional modeling (fact/dimension design, SCD Type 2) and data contracts
- Phase I: CI/CD (GitHub Actions running tests on every PR) and optionally Kubernetes/Composer
- Phase J: CDC (Debezium) feeding your streaming layer
- Phase K: catalog/lineage, PII protection, and a cost audit

**For architecture inspiration (study, don't copy):**
- Engineering blogs from Netflix, Uber, and Airbnb publish real pipeline architectures — search "[company] data platform engineering blog" and read one or two to see how real teams describe their design decisions and trade-offs.

**For documentation:**
- Search "architecture decision record ADR template" — writing short ADRs ("we chose X over Y because...") is a professional habit that makes a portfolio project read like real engineering work.

---

## Week 33 — System Design Practice & Mock Interviews

**Primary book (the standard reference):**
- *Designing Data-Intensive Applications* by Martin Kleppmann — the most widely recommended book for exactly this material. You don't need to finish it this week; read the chapters on replication, partitioning, and stream processing alongside your practice.

**Data-engineering-specific system design:**
- [Data Engineer Academy — "Data Engineer Interview Preparation: System Design Basics"](https://dataengineeracademy.com/) — search this title; it frames the round around data producers, consumers, raw vs. curated layers, and trade-offs, which is the right lens for DE (rather than generic web-scale design).
- [DataDriven — "Data Engineer System Design Interview Guide 2026"](https://datadriven.io/blog/data-engineer-system-design-interview-guide-2026) — worth reading for one key insight: DE system design optimizes for throughput, durability, cost, and governance, whereas software-engineering system design optimizes for latency and requests-per-second. Prep for the right one.

**General system design practice:**
- [Codemia.io](https://codemia.io/) — LeetCode-style system design problems with worked solutions.
- [ByteByteGo](https://bytebytego.com/) — Alex Xu's visual, structured system design content.

**Mock interviews:**
- [Pramp](https://www.pramp.com/) — free peer-to-peer mock interviews. Doing even two or three real mock interviews with another human is worth more than any amount of solo reading.

**What to practice designing (2026 trends):**
- Real-time analytics pipeline, CDC-based warehouse sync, multi-tenant analytics dashboard, a RAG/vector search service — notice how closely these match what you've already built.

**SQL and coding rounds (don't neglect these):**
- [LeetCode Database problems](https://leetcode.com/problemset/database/) — keep your Phase A–B SQL sharp; a short daily practice beats a cram session.

---

## Week 34 — Portfolio, Resume & Retrospective

**Portfolio:**
- Search "data engineering portfolio README examples" — look at how strong repos present architecture, setup instructions, and design decisions.
- Pin your two Flagship projects on your GitHub profile; write a profile README that links to them with a one-line description of what each demonstrates.

**Resume:**
- Search "data engineer resume examples 2026" — focus on how projects are described with concrete outcomes ("reduced query cost 60% via partitioning") instead of tool lists.

**Writing:**
- Publishing one technical write-up (on dev.to, Medium, or your own site) about something you actually built — for example, the Spark vs. Flink comparison from Week 28 — is a strong, durable signal of depth.

**Community:**
- Join the Data Engineering community on Reddit (r/dataengineering) and the dbt, Airflow, or Dagster Slack communities — real exposure to how practitioners talk about problems.