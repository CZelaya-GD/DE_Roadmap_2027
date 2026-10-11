# Week 33 Plan: System Design Practice & Mock Interviews

## Overview

- **Phase:** L — Capstone II & Job Readiness
- **Focus:** Explaining and defending design decisions out loud, under time pressure
- **Goal:** Convert everything you've built into the ability to design a data system on a whiteboard in 45 minutes, and to answer SQL, modeling, and behavioral questions fluently
- **Anki Target:** 25 cards (interview-pattern cards: design frameworks, trade-off phrases, common questions)
- **Key insight to carry all week:** Data engineering interviews weight system design and data modeling far more than coding. Data-engineering system design optimizes for throughput, durability, cost, and governance — not the latency and requests-per-second focus of general software design.

---

## A Repeatable Framework for Design Questions

Use the same steps every time so you never freeze:

1. **Clarify:** Who produces the data? Who consumes it? What volume, freshness, and accuracy are required?
2. **Define sources and sinks:** Where does data originate and where must it end up?
3. **Layer it:** Raw → cleaned → modeled/curated. Say where each lives.
4. **Choose batch vs. streaming** and justify it with the freshness requirement.
5. **Cover the "-ilities":** failure handling, idempotency, data quality, schema changes, governance/PII, cost.
6. **Name trade-offs out loud** — there is rarely one correct design, only defensible ones.

---

## Monday–Friday

### Daily Objectives

- **Monday:** Learn the framework above, then practice it on a design you already know deeply — your own Flagship II. Present it aloud as if to an interviewer → Deliverable: a recorded or written 10-minute walkthrough of Flagship II using the six steps
- **Tuesday:** Practice 1 — "Design a real-time analytics pipeline for a food-delivery app" (timed, 45 minutes, whiteboard or diagram) → Deliverable: 1 completed design with a written list of trade-offs you named
- **Wednesday:** Practice 2 — "Design a CDC-based sync from an operational database into a warehouse, including how deletes and schema changes are handled" → Deliverable: 1 completed design, plus a self-critique of what you missed
- **Thursday:** Practice 3 — "Design a vector search / RAG service over company documents, including cost and PII concerns" → Deliverable: 1 completed design; also spend 30 minutes on SQL practice (LeetCode Database) and 3 data modeling questions
- **Friday:** Mock interview with a real human (Pramp or a peer) — one system design round, ideally also one SQL round → Deliverable: notes on feedback received and 3 specific things to improve

### Anki Targets

- Monday: 5 cards tagged `interview::framework`
- Tuesday: 5 cards tagged `interview::design-patterns`
- Wednesday: 5 cards tagged `interview::cdc-tradeoffs`
- Thursday: 5 cards tagged `interview::rag-tradeoffs`
- Friday: 5 cards tagged `interview::feedback`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Write answers (3–4 sentences each) to these behavioral prompts, using real examples from your own roadmap: "Tell me about a time something broke," "Tell me about a technical trade-off you made," "Tell me about something you learned the hard way"
- Draft next week's objectives (Portfolio, Resume & Retrospective)

---

## Week 33 Success Metrics
- [ ] 25 Anki cards created
- [ ] 3 timed design practices completed with named trade-offs
- [ ] 1 real mock interview completed with written feedback
- [ ] Behavioral answers drafted using real project examples
- [ ] Can walk through the six-step framework from memory
- [ ] Week 34 plan drafted