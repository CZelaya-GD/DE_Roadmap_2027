# Data Engineering Decision Trees

## 1. Batch vs Streaming

Is sub-second freshness required?

├─ Yes → Streaming (Kafka + Flink/Spark Structured Streaming)

└─ No → Batch (Airflow + dbt + Warehouse)

    └─ Is near-real-time (minutes) needed?

        ├─ Yes → Micro-batch (Airflow every 5–15 min)

        └─ No → Standard batch (hourly/daily)

## 2. CDC vs Full Load

Can you identify changed rows (updated_at, version, log)?

├─ Yes → CDC (incremental load, MERGE statement)

└─ No → Full load (truncate + insert, or INSERT OVERWRITE)

    └─ Is data small (<1M rows)?

        ├─ Yes → Full load acceptable

        └─ No → Add CDC capability (audit columns, change tracking)

## 3. Warehouse vs Lakehouse

Do you need ACID transactions + ML on same data?

├─ Yes → Lakehouse (Databricks, Delta Lake, Iceberg)

└─ No → Warehouse (BigQuery, Snowflake)

    └─ Do you need complex transformations before loading?

        ├─ Yes → Lakehouse (transform in-place)

        └─ No → Warehouse (ELT: load raw, transform in SQL)

## 4. Orchestration Tool Selection

Do you need asset-based lineage + data-aware scheduling?

├─ Yes → Dagster (assets, dependencies, materialization)

└─ No → Airflow (DAGs, operators, XComs)

    └─ Do you need simple cron jobs only?

        ├─ Yes → Cron + scripts (no orchestration)

        └─ No → Airflow (industry standard, flexible)

## 5. Real-Time Necessity

What's the business impact of 1-hour delay?

├─ Critical (fraud detection, monitoring) → Real-time streaming

├─ Moderate (dashboards, reporting) → Micro-batch (5–15 min)

└─ Low (weekly reports, analytics) → Standard batch (hourly/daily)

Do you have resources for 24/7 monitoring?

├─ Yes → Real-time feasible

└─ No → Batch (simpler, less operational overhead)

---

## Usage

Before starting any project, run through these trees. Document your decision in `notes/<project_name>_decisions.md`.