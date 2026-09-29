# Phase H Resources: Data Modeling & Advanced Orchestration

---

## Week 21 — Dimensional Modeling (Kimball, Star Schemas, SCDs)

**Primary:**
- Search "Dimensional Modeling Explained Kimball's Star Schema Approach" on YouTube — several concise (10–35 minute), well-regarded walkthroughs exist covering fact/dimension tables with concrete retail examples; good as a first-pass conceptual overview before hands-on work.
- [DataCamp — "Mastering Slowly Changing Dimensions (SCD)"](https://www.datacamp.com/tutorial/mastering-slowly-changing-dimensions-scd) — actively updated (last refresh June 2026), hands-on examples with real code for SCD Type 1/2/3, which is exactly this week's Wednesday/Thursday focus.

**The original source material (optional but worth knowing exists):**
- Ralph Kimball's *The Data Warehouse Toolkit* is the foundational text this entire topic comes from (published 1996, still the reference nearly 30 years later). You don't need to read the whole book this week, but knowing it exists — and that "Kimball-style modeling" is a real, named, industry-standard methodology — is worth having in your vocabulary for interviews.

**Applying it to your own work:**
- Revisit your Phase B dbt marts (Week 7) and re-model at least one as a proper fact/dimension pair — this is more valuable than modeling a fresh toy dataset, since you already understand the underlying data.

---

## Week 22 — Data Contracts & Schema Evolution

**Primary:**
- Search "data contracts data engineering" — this is a newer, less textbook-standardized topic than dimensional modeling, so multiple current blog posts/talks (2024–2026) will serve better than one canonical source; look for content from dbt Labs, Monte Carlo, or similar data-quality-focused companies, since they've driven a lot of the practical thinking here.
- [dbt docs — "Model contracts"](https://docs.getdbt.com/docs/collaborate/govern/model-contracts) — dbt's own implementation of this concept, directly usable on your existing Phase B project.

**Schema evolution specifically:**
- Search "schema evolution Parquet Avro backward compatibility" — worth understanding the distinction between backward-compatible and breaking schema changes, since this is what actually causes downstream pipeline failures in the real world.

---

## Week 23 — Dagster (Second Orchestrator)

**Primary:**
- [Dagster official documentation — Quickstart/Tutorial](https://docs.dagster.io/) — go directly to their hands-on tutorial; Dagster's docs are unusually good at explaining *why* their approach differs from task-based schedulers like Airflow.
- [Dagster GitHub repository](https://github.com/dagster-io/dagster) — the README itself is a concise, current explanation of the asset-based programming model; worth reading before diving into the full docs.

**The key conceptual contrast to look for:**
- Airflow is fundamentally *task-based* (you define a sequence of tasks to run); Dagster is fundamentally *asset-based* (you declare the data assets you want to exist, and Dagster figures out how to keep them up to date). This distinction is the whole point of this week — don't just learn Dagster's syntax, understand why this different mental model exists and what problems it solves that task-based orchestration doesn't handle as naturally (like asset lineage and freshness tracking).

**Note on tooling:** Dagster's newer starter templates use the `dg dev` CLI command; older tutorials may still show `dagster dev` — both work, but prefer current docs if the two conflict.