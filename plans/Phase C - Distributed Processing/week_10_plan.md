# Week 10 Plan: PySpark Fundamentals (RDDs vs DataFrames, Lazy Evaluation)

## Overview

- **Phase:** C — Distributed Processing
- **Focus:** PySpark core concepts
- **Goal:** Shift from "single-machine SQL thinking" to a distributed-computing mindset, and build your first PySpark pipeline
- **Anki Target:** 25 cards
- **Why this matters here:** Everything in Phases A–B ran on one machine (your laptop, or a warehouse abstracting that away from you). This week is the first time you have to actually think about data being split across multiple machines — and that changes how you reason about code.

---

## Monday–Friday

### Daily Objectives

- **Monday:** RDDs vs. DataFrames, lazy evaluation, transformations vs. actions (why nothing runs until you call `.collect()` or `.show()`) → Deliverable: 5 examples showing lazy evaluation in action, with commentary on when execution actually happens
- **Tuesday:** Read/write formats (Parquet, CSV, JSON), schema inference vs. explicit schemas → Deliverable: 3 read/write pipelines, one with an explicitly defined schema
- **Wednesday:** Partitioning, repartition vs. coalesce, and why partition count affects performance → Deliverable: 3 partitioning examples with `.explain()` output showing the difference
- **Thursday:** Core transformations — select, filter, groupBy, agg — and joins (basic join first, strategy comes next week) → Deliverable: 5 transformation pipelines including at least one join
- **Friday:** Build a small end-to-end PySpark pipeline (local mode): read raw data → transform → write out → Deliverable: working ETL pipeline in PySpark

### Anki Targets

- Monday: 5 cards tagged `scale::pyspark::fundamentals`
- Tuesday: 5 cards tagged `scale::pyspark::io`
- Wednesday: 5 cards tagged `scale::pyspark::partitioning`
- Thursday: 5 cards tagged `scale::pyspark::transformations`
- Friday: 5 cards tagged `scale::pyspark::pipeline`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Rebuild one PySpark transformation from memory, and explain out loud why it's lazy until an action triggers it
- Draft next week's objectives (PySpark Performance)

---

## Week 10 Success Metrics
- [ ] 25 Anki cards created
- [ ] 15+ PySpark examples written
- [ ] 1 end-to-end PySpark pipeline completed
- [ ] Can explain lazy evaluation to someone else without notes
- [ ] Week 11 plan drafted