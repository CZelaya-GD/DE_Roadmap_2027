# Phase B Resources: Warehouse & Transformation

---

## Week 6 — BigQuery Fundamentals

**Primary:**
- [Google Cloud Skills Boost — "BigQuery Fundamentals" quest](https://www.cloudskillsboost.google/) — search this exact title on the platform; hands-on labs inside real BigQuery, no separate setup needed.
- [BigQuery official docs — "Introduction to BigQuery"](https://cloud.google.com/bigquery/docs/introduction) — short, precise, written by the people who built it.

**Practice datasets:**
- [BigQuery Public Datasets](https://cloud.google.com/bigquery/public-data) — free to query (within the free tier), realistic size, good for this week's staging-layer exercises.
- [Kaggle Learn: Advanced SQL](https://www.kaggle.com/learn/advanced-sql) — runs directly on BigQuery, reinforces both SQL and BigQuery-specific syntax simultaneously.

**Cost/partitioning specifically:**
- [BigQuery docs — "Introduction to partitioned tables"](https://cloud.google.com/bigquery/docs/partitioned-tables) — this is worth reading slowly on Thursday before you write your own partitioned table.

---

## Week 7 — dbt Fundamentals

**Primary:**
- [dbt Labs' own free course platform](https://courses.getdbt.com/) — search for "dbt Fundamentals," their official, current, free course. This is the most authoritative source since it's built by the tool's own creators.
- [dbt official docs — "Quickstart guides"](https://docs.getdbt.com/guides) — pick the BigQuery quickstart specifically, so your setup matches Week 6's warehouse.

**Alternative/supplementary:**
- [DataCamp — "dbt Fundamentals" track](https://www.datacamp.com/tracks/dbt-fundamentals) — free tier available, updated regularly (last update May 2026), good if you prefer a structured video-plus-exercise format over reading docs directly.

**Staging/intermediate/marts pattern:**
- Search "dbt best practices staging models" — dbt Labs publishes an official style guide covering exactly this layering pattern; it's short and worth reading before Monday.

---

## Week 8 — Query Optimization + Production Load

**Primary:**
- [BigQuery docs — "Query optimization overview"](https://cloud.google.com/bigquery/docs/query-optimization) — the official guide to EXPLAIN plans, slot usage, and cost.
- [BigQuery docs — "Introduction to clustered tables"](https://cloud.google.com/bigquery/docs/clustered-tables) — pairs directly with Tuesday's clustering work.

**Dashboard tool (Friday):**
- [Metabase — "Getting Started" docs](https://www.metabase.com/docs/latest/) — free, open-source, connects directly to BigQuery, reasonable to have running same-day.

**Cost awareness:**
- [Google Cloud — "Control BigQuery costs" docs](https://cloud.google.com/bigquery/docs/best-practices-costs) — read this before Thursday's cost-optimization work, not after.

---

## Week 9 — DuckDB + Local Dev + Sprint Review

**Primary:**
- [DuckDB official documentation](https://duckdb.org/docs/) — genuinely one of the best-written docs of any data tool; the "SQL Introduction" and "Data Import" pages cover everything Monday–Tuesday need.
- [DuckDB + dbt integration guide](https://docs.getdbt.com/docs/core/connect-data-platform/duckdb-setup) — official dbt docs page for exactly Thursday's task.

**Local-to-cloud pipeline pattern:**
- Search "DuckDB to BigQuery pipeline" — this is a common enough pattern that recent blog walkthroughs exist; look for anything from 2025–2026 specifically, since DuckDB's ecosystem moves fast.

**For your Sprint 1 review (Friday):**
- No new resource — this is entirely about revisiting Weeks 6–9's own Anki cards and rebuilding a pipeline from memory. Resist the urge to learn something new this day.