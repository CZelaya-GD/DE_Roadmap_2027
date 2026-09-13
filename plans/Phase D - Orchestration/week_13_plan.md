# Week 13 Plan: Airflow Hardening (DAG Design, Retries, Backfills, SLAs)

## Overview

- **Phase:** D — Orchestration (final week)
- **Focus:** Production-grade Airflow
- **Goal:** Harden the DAGs you built in Week 12 for reliability, monitoring, and maintainability — this now sits on real footing instead of asking you to harden something you'd never built
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** DAG design patterns — sensors, task groups, dynamic task mapping → Deliverable: 3 well-structured DAGs, at least one using a task group or dynamic mapping
- **Tuesday:** Custom operators and hooks, connection pooling → Deliverable: 1 custom operator, 1 custom hook, built by extending a pattern from Week 12's integration DAG
- **Wednesday:** Retries, backfills, idempotent backfill strategies (critical: a non-idempotent backfill can duplicate data — understand why before running one) → Deliverable: 1 DAG with retry logic configured, 1 tested backfill run
- **Thursday:** XComs (task-to-task communication), SLAs, callbacks (on_failure, on_success) → Deliverable: 1 DAG using XComs, with an SLA and failure callback configured
- **Friday:** Observability — structured logging, Slack/email alerting on failure → Deliverable: 1 fully monitored DAG that sends a real alert when a task fails (test this by deliberately failing a task)

### Anki Targets

- Monday: 5 cards tagged `orchestration::airflow::design-patterns`
- Tuesday: 5 cards tagged `orchestration::airflow::custom-operators`
- Wednesday: 5 cards tagged `orchestration::airflow::backfills`
- Thursday: 5 cards tagged `orchestration::airflow::xcoms-slas`
- Friday: 5 cards tagged `orchestration::airflow::observability`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Phase
- Review all Anki cards from the week
- Rebuild one DAG from memory with retries + SLA configured, and explain why your backfill strategy is idempotent
- Draft Phase E objectives (Data Quality/Observability)

---

## Week 13 Success Metrics
- [ ] 25 Anki cards created
- [ ] 3 production-grade DAGs written
- [ ] 1 custom operator/hook created
- [ ] 1 DAG that successfully sends a real failure alert
- [ ] Can explain, unprompted, why a non-idempotent backfill is dangerous
- [ ] Phase E (Week 14) plan drafted