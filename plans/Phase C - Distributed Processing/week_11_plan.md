# Week 11 Plan: PySpark Performance (Joins, Shuffles, Skew, Caching)

## Overview

- **Phase:** C — Distributed Processing (final week)
- **Focus:** PySpark optimization
- **Goal:** Take the Week 10 pipeline from "works" to "works well at scale," and understand shuffles/skew well enough to diagnose them in the Spark UI without guessing
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** Shuffles — what triggers them (wide vs. narrow transformations), how to minimize unnecessary ones → Deliverable: 3 examples comparing a shuffle-heavy vs. shuffle-light version of the same logic, viewed side-by-side in the Spark UI
- **Tuesday:** Join strategies (broadcast, sort-merge, shuffle hash), when Spark picks each one and when to override it with join hints → Deliverable: 3 join optimizations with `.explain()` output showing the chosen strategy
- **Wednesday:** Data skew — detecting it (via the Spark UI's task duration spread), fixing it with salting or broadcast joins → Deliverable: 2 skew-handling examples, before/after task duration compared
- **Thursday:** Caching, checkpointing, persistence levels (memory vs. disk vs. both) — and when caching actually helps vs. wastes memory → Deliverable: cached pipeline with a documented performance comparison
- **Friday:** Apply everything this week to optimize the Week 10 pipeline end-to-end → Deliverable: optimized pipeline with before/after runtime and shuffle metrics

### Anki Targets

- Monday: 5 cards tagged `scale::pyspark::shuffles`
- Tuesday: 5 cards tagged `scale::pyspark::joins`
- Wednesday: 5 cards tagged `scale::pyspark::skew`
- Thursday: 5 cards tagged `scale::pyspark::caching`
- Friday: 5 cards tagged `scale::pyspark::optimization`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Phase
- Review all Anki cards from the week
- Rebuild one optimized join from memory, explaining which strategy you'd choose and why
- Draft Phase D objectives (Airflow Fundamentals — the on-ramp week we added specifically to avoid the old plan's gap)

---

## Week 11 Success Metrics
- [ ] 25 Anki cards created
- [ ] 10 optimization examples written, each with a documented before/after
- [ ] Week 10 pipeline fully optimized with measured improvement
- [ ] Comfortable opening the Spark UI and identifying a shuffle or skew problem unprompted
- [ ] Phase D (Week 12) plan drafted