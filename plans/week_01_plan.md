# Week 1 Plan: SQL Window Functions + CTEs + BigQuery Basics

## Overview
- **Focus:** Foundational SQL (window functions, CTEs) + BigQuery setup
- **Goal:** Master advanced SQL patterns and load first dataset to BigQuery
- **Anki Target:** 50 cards total (20 this week, 30 review from prior)

---

## Monday
### Objective
SQL window functions: ROW_NUMBER, RANK, DENSE_RANK

### Tasks
1. Read documentation on window function syntax (PostgreSQL or BigQuery docs)
2. Write 10 queries using ROW_NUMBER, RANK, DENSE_RANK on a public dataset
   - Dataset options: Hacker News (BigQuery public dataset), NYC Taxi Trips, StackOverflow
3. Document each query: what it does, why window function is needed, expected output
4. Create 10 Anki cards for syntax and use cases

### Deliverable
- 10 documented queries in `learning/sql/window_functions_monday.sql`
- 10 Anki cards tagged `sql::advanced::window-functions`

### Time Allocation
- 10 min: Anki review (existing cards)
- 25 min: Sprint 1 — Read docs, write first 3 queries
- 5 min: Recall check — write syntax from memory
- 25 min: Sprint 2 — Write next 4 queries
- 5 min: Recall check — explain RANK vs DENSE_RANK aloud
- 25 min: Sprint 3 — Write final 3 queries, create Anki cards
- 5 min: Recall check — list all 3 functions and differences
- 10 min: Brain dump — what was confusing, what clicked
- 30 min: Nap

---

## Tuesday
### Objective
SQL window functions: LAG, LEAD, running totals, PARTITION BY

### Tasks
1. Study LAG/LEAD syntax and use cases
2. Write 10 queries:
   - 3 using LAG (compare current row to previous)
   - 3 using LEAD (compare current row to next)
   - 2 running totals (cumulative sum)
   - 2 using PARTITION BY (restart window per group)
3. Run EXPLAIN on 2 queries to see partition behavior
4. Create 10 Anki cards

### Deliverable
- 10 documented queries in `learning/sql/window_functions_tuesday.sql`
- 10 Anki cards tagged `sql::advanced::window-functions`

### Time Allocation
- 10 min: Anki review (Monday's cards)
- 25 min: Sprint 1 — LAG queries (3)
- 5 min: Recall check — write LAG syntax from memory
- 25 min: Sprint 2 — LEAD + running totals (5)
- 5 min: Recall check — explain running total pattern aloud
- 25 min: Sprint 3 — PARTITION BY queries (2), EXPLAIN analysis
- 5 min: Recall check — what does PARTITION BY do?
- 10 min: Brain dump
- 30 min: Nap

---

## Wednesday
### Objective
CTEs (Common Table Expressions) + subquery refactoring

### Tasks
1. Study CTE syntax: WITH clause, recursive CTEs
2. Find 5 complex queries (from Monday/Tuesday or online) that use nested subqueries
3. Refactor each into CTEs for readability
4. Document: before/after comparison, why CTE improves clarity
5. Create 5 Anki cards

### Deliverable
- 5 refactored queries in `learning/sql/ctes_wednesday.sql` with before/after comments
- 5 Anki cards tagged `sql::advanced::ctes`

### Time Allocation
- 10 min: Anki review (Mon + Tue cards)
- 25 min: Sprint 1 — Study CTE syntax, refactor first 2 queries
- 5 min: Recall check — write CTE syntax from memory
- 25 min: Sprint 2 — Refactor next 2 queries
- 5 min: Recall check — when to use CTE vs subquery?
- 25 min: Sprint 3 — Refactor final query, create Anki cards
- 5 min: Recall check — recursive CTE structure
- 10 min: Brain dump
- 30 min: Nap

---

## Thursday
### Objective
Query optimization: partitioning, clustering, cost estimation

### Tasks
1. Study BigQuery partitioning vs clustering (or your chosen warehouse)
2. Write 3 slow queries (intentionally inefficient: no WHERE, SELECT *, full table scan)
3. Optimize each query:
   - Add appropriate WHERE filters
   - Use partition/clustering columns
   - Replace SELECT * with specific columns
4. Run EXPLAIN before/after, document cost reduction
5. Create 5 Anki cards

### Deliverable
- 3 optimized queries in `learning/sql/optimization_thursday.sql` with EXPLAIN output
- 5 Anki cards tagged `sql::advanced::optimization` and `cloud::bigquery`

### Time Allocation
- 10 min: Anki review (Mon–Wed cards)
- 25 min: Sprint 1 — Study partitioning/clustering, write 1 slow query
- 5 min: Recall check — partitioning vs clustering difference
- 25 min: Sprint 2 — Optimize first 2 queries, run EXPLAIN
- 5 min: Recall check — what is predicate pushdown?
- 25 min: Sprint 3 — Optimize final query, create Anki cards
- 5 min: Recall check — how to read EXPLAIN plan?
- 10 min: Brain dump
- 30 min: Nap

---

## Friday
### Objective
Load existing ETL pipeline output to BigQuery

### Tasks
1. Choose one existing ETL pipeline from your portfolio (e.g., Hacker News, vibration data)
2. Export pipeline output as CSV (or use existing CSV)
3. Load into BigQuery via web UI:
   - Create dataset
   - Create table from CSV upload
   - Set schema (auto-detect or manual)
4. Write 3 test queries to verify data loaded correctly
5. Document steps: loading method, schema decisions, any issues
6. Create 5 Anki cards

### Deliverable
- Loaded table in BigQuery (screenshot or table name documented)
- 3 test queries in `learning/sql/bigquery_load_friday.sql`
- 5 Anki cards tagged `cloud::bigquery`
- Documentation in `projects/<pipeline_name>/bigquery_load_notes.md`

### Time Allocation
- 10 min: Anki review (Mon–Thu cards)
- 25 min: Sprint 1 — Prepare CSV, create BigQuery dataset
- 5 min: Recall check — BigQuery loading methods
- 25 min: Sprint 2 — Load table, verify schema
- 5 min: Recall check — partitioning vs clustering recap
- 25 min: Sprint 3 — Write test queries, create Anki cards
- 5 min: Recall check — how to load data into BigQuery?
- 10 min: Brain dump — Week 1 reflection
- 30 min: Nap

---

## Saturday
### Rest
- No study, no Anki, no SQL
- Physical activity, walk, disconnect

---

## Sunday
### Review + Map Week 2
#### Review Tasks
1. Rebuild 1 window function query from memory (no notes)
2. Review all 50 Anki cards (Mon–Fri + prior)
3. Write Week 1 reflection:
   - What worked well?
   - What was confusing?
   - What needs adjustment for Week 2?

#### Map Week 2
1. Open `plans/week_02_plan.md`
2. Draft daily objectives for Week 2 (dbt models: staging → intermediate → marts)
3. Pre-create Anki tags for Week 2: `transformation::dbt`

### Deliverable
- Week 1 reflection in `notes/week_01_reflection.md`
- Week 2 draft plan in `plans/week_02_plan.md`

---

## Week 1 Success Metrics
- [ ] 50 Anki cards created and reviewed
- [ ] 33 SQL queries written and documented
- [ ] 1 dataset loaded to BigQuery
- [ ] Week 2 plan drafted
- [ ] Nap routine established