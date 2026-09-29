# Week 21 Plan: Dimensional Modeling (Kimball, Star Schemas, SCDs)

## Overview

- **Phase:** H — Data Modeling & Advanced Orchestration
- **Focus:** Designing warehouse schemas deliberately instead of organically
- **Goal:** Learn to model a business process into facts and dimensions — the skill that determines whether a warehouse stays usable after two years or becomes an unmaintainable tangle
- **Anki Target:** 25 cards
- **Why this comes after Phase B, not during it:** You needed to build a few dbt marts first to feel the problem this solves. Now the "why" lands instead of feeling abstract.

---

## Monday–Friday

### Daily Objectives

- **Monday:** Facts vs. dimensions, grain (revisit Week 2's concept, now at schema level), Kimball's 4-step design process → Deliverable: 1 business process modeled on paper — grain declared, facts and dimensions identified
- **Tuesday:** Star schema vs. snowflake schema, surrogate keys, denormalized dimension hierarchies, why analytics tolerates redundancy that OLTP wouldn't → Deliverable: 1 star schema designed and diagrammed for the Monday business process
- **Wednesday:** Slowly Changing Dimensions — Types 1, 2, and 3, with Type 2 built hands-on using dbt snapshots → Deliverable: 1 working SCD Type 2 dimension in your existing dbt project
- **Thursday:** Fact table types — transaction, periodic snapshot, accumulating snapshot, factless — and when each applies → Deliverable: 2 different fact table types implemented against the same source data
- **Friday:** Conformed dimensions and the bus matrix — how multiple business processes share dimensions across a warehouse → Deliverable: 1 bus matrix mapping 3+ business processes against shared dimensions

### Anki Targets

- Monday: 5 cards tagged `modeling::kimball::fundamentals`
- Tuesday: 5 cards tagged `modeling::star-schema`
- Wednesday: 5 cards tagged `modeling::scd`
- Thursday: 5 cards tagged `modeling::fact-tables`
- Friday: 5 cards tagged `modeling::conformed-dimensions`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Explain out loud, from memory, the difference between SCD Type 1 and Type 2, and when you'd choose each
- Draft next week's objectives (Data Contracts & Schema Evolution)

---

## Week 21 Success Metrics
- [ ] 25 Anki cards created
- [ ] 1 complete star schema designed and diagrammed
- [ ] 1 working SCD Type 2 dimension implemented in dbt
- [ ] 2 fact table types implemented
- [ ] 1 bus matrix built
- [ ] Can declare a fact table's grain in one sentence, unprompted
- [ ] Week 22 plan drafted