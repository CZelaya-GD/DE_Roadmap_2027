# Week 3 Plan: SQL Intermediate (CTEs, Window Functions)

## Overview

- **Phase:** A — True Fundamentals
- **Focus:** Query readability and analytical SQL
- **Goal:** Write complex, multi-step queries that are still readable — the skill that separates "can query" from "can build production transformations"
- **Anki Target:** 30 cards
- **Note:** This is the old Week 1 content, moved here because it assumes fluency you now have from Weeks 1–2 instead of assuming it on day one.

---

## Monday–Friday

### Daily Objectives

- **Monday:** Common Table Expressions (CTEs) — single and chained, why they beat nested subqueries for readability → Deliverable: 5 queries refactored from subqueries into CTEs
- **Tuesday:** Window functions I — ROW_NUMBER, RANK, DENSE_RANK, PARTITION BY → Deliverable: 5 ranking/dedup queries
- **Wednesday:** Window functions II — LAG, LEAD, running totals, moving averages → Deliverable: 5 time-series style queries
- **Thursday:** Recursive CTEs (hierarchies, sequences), combining CTEs with window functions → Deliverable: 3 queries combining both techniques
- **Friday:** Rebuild a "messy" 40-line nested-subquery query as a clean, readable CTE chain → Deliverable: before/after query pair with a short note on why the after version is easier to maintain

### Anki Targets

- Monday: 6 cards tagged `sql::advanced::cte`
- Tuesday: 6 cards tagged `sql::advanced::window-functions`
- Wednesday: 6 cards tagged `sql::advanced::window-functions`
- Thursday: 6 cards tagged `sql::advanced::recursive-cte`
- Friday: 6 cards tagged `sql::advanced::readability`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Rebuild one window-function query from memory
- Draft next week's objectives

---

## Week 3 Success Metrics
- [ ] 30 Anki cards created
- [ ] 20+ CTE/window-function queries written
- [ ] 1 messy query successfully refactored for readability
- [ ] Week 4 plan drafted