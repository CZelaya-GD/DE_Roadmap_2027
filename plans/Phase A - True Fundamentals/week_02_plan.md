# Week 2 Plan: SQL Fundamentals II (Joins, Subqueries, Grain)

## Overview

- **Phase:** A — True Fundamentals
- **Focus:** Multi-table querying
- **Goal:** Understand joins deeply enough to predict row counts before running a query — this is the single most common source of production bugs per your own pitfalls.md (#2: fan-out joins)
- **Anki Target:** 30 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** INNER JOIN, LEFT/RIGHT JOIN, understanding join keys → Deliverable: 6 join queries across a 3+ table sample schema
- **Tuesday:** FULL OUTER JOIN, self-joins, joining on multiple conditions → Deliverable: 5 queries including one self-join
- **Wednesday:** Understanding "grain" — what does one row represent? Predicting row-count changes before and after a join → Deliverable: 5 queries with a written row-count prediction, then verified
- **Thursday:** Subqueries (in WHERE, in FROM), correlated subqueries, EXISTS/NOT EXISTS → Deliverable: 5 subquery examples
- **Friday:** Fan-out join diagnosis drill — given 3 buggy queries with inflated row counts, find and fix the cause → Deliverable: 3 fixed queries with a one-line explanation of what caused each fan-out

### Anki Targets

- Monday: 6 cards tagged `sql::joins`
- Tuesday: 6 cards tagged `sql::joins`
- Wednesday: 6 cards tagged `sql::grain`
- Thursday: 6 cards tagged `sql::subqueries`
- Friday: 6 cards tagged `sql::joins::debugging`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Rebuild one join query from memory, predicting the row count before running it
- Draft next week's objectives

---

## Week 2 Success Metrics
- [ ] 30 Anki cards created
- [ ] 20+ join/subquery examples written
- [ ] Can correctly predict row-count direction (same/more/fewer rows) before running a join, at least 4 out of 5 times
- [ ] Week 3 plan drafted