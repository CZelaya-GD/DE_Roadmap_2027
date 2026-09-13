# Week 12 Plan: Airflow Fundamentals

## Overview

- **Phase:** D — Orchestration
- **Focus:** Core Airflow concepts and your first real DAGs
- **Goal:** Go from zero Airflow exposure to comfortably writing, running, and debugging a basic DAG — this is the on-ramp week the original roadmap skipped, added specifically so Week 13's "hardening" content lands on something you've actually built
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** What Airflow actually is (a scheduler, not a processing engine), install Astro CLI, run your first local Airflow instance, navigate the Airflow UI → Deliverable: local Airflow running via `astro dev start`, UI explored (DAGs list, Grid view, task logs)
- **Tuesday:** Core concepts — DAGs, tasks, operators, the scheduler's role — write your first DAG using the `@task` decorator and BashOperator → Deliverable: 1 working "hello world" DAG, manually triggered and observed running
- **Wednesday:** Task dependencies (`>>` and `<<`), the difference between a DAG failing and a task failing, basic scheduling (`schedule` intervals, `catchup`) → Deliverable: 1 DAG with 3+ dependent tasks, scheduled (not just manually triggered)
- **Thursday:** Connect Airflow to a real pipeline — orchestrate one of your existing dbt or PySpark scripts as a DAG task → Deliverable: 1 DAG that actually runs a piece of your Phase B or C work
- **Friday:** Reading logs and debugging a deliberately broken DAG (introduce a bug yourself, then fix it using only the Airflow UI's logs) → Deliverable: 1 broken DAG diagnosed and fixed, with notes on how you found the issue

### Anki Targets

- Monday: 5 cards tagged `orchestration::airflow::fundamentals`
- Tuesday: 5 cards tagged `orchestration::airflow::dags`
- Wednesday: 5 cards tagged `orchestration::airflow::scheduling`
- Thursday: 5 cards tagged `orchestration::airflow::integration`
- Friday: 5 cards tagged `orchestration::airflow::debugging`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Rebuild the "hello world" DAG from memory, without referencing Monday's notes
- Draft next week's objectives (Airflow Hardening)

---

## Week 12 Success Metrics
- [ ] 25 Anki cards created
- [ ] 3+ DAGs written and successfully run
- [ ] 1 real pipeline (dbt or PySpark) orchestrated through Airflow
- [ ] Comfortable navigating the Airflow UI to find a task's logs without guidance
- [ ] Week 13 plan drafted