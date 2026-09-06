# Week 6 Plan: BigQuery Fundamentals

## Overview

- **Phase:** B — Warehouse & Transformation
- **Focus:** Understanding a cloud warehouse from the ground up
- **Goal:** Build and query BigQuery tables with an understanding of *why* a warehouse behaves differently from the local SQLite/DuckDB work in Phase A
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** Warehouse vs. OLTP database (columnar storage, why warehouses are built for scans not row lookups), creating your first BigQuery dataset and table → Deliverable: 1 dataset with 2 tables loaded from CSV
- **Tuesday:** Schema design for a warehouse — staging layer concept, why raw data should never sit directly in production tables → Deliverable: raw → staging table pair with documented transformation
- **Wednesday:** Querying at scale — running queries against BigQuery public datasets, reading query cost estimates before running → Deliverable: 5 queries against a public dataset, cost noted for each
- **Thursday:** Partitioning fundamentals — date-partitioned tables, partition pruning, why it matters for both cost and speed → Deliverable: 1 partitioned table with a before/after cost comparison on a filtered query
- **Friday:** Bring it together — build a small staging pipeline (raw CSV → staged, partitioned BigQuery table) → Deliverable: working raw-to-staged pipeline

### Anki Targets

- Monday: 5 cards tagged `cloud::bigquery::fundamentals`
- Tuesday: 5 cards tagged `cloud::bigquery::schema`
- Wednesday: 5 cards tagged `cloud::bigquery::querying`
- Thursday: 5 cards tagged `cloud::bigquery::partitioning`
- Friday: 5 cards tagged `cloud::bigquery::pipeline`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Explain out loud why a warehouse uses columnar storage and why that matters for analytics queries
- Draft next week's objectives (dbt Fundamentals)

---

## Week 6 Success Metrics
- [ ] 25 Anki cards created
- [ ] 1 working raw-to-staged BigQuery pipeline
- [ ] 1 partitioned table with documented cost comparison
- [ ] Comfortable reading a query's estimated cost before running it
- [ ] Week 7 plan drafted