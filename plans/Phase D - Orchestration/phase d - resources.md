# Phase D Resources: Orchestration (Apache Airflow)

**Version note:** Airflow is now on major version 3.x as of 2026, which changed some internals (task execution model, API) from the Airflow 2.x tutorials that dominate older search results. Prefer resources explicitly labeled "Airflow 3" where possible — the DAG-writing fundamentals mostly transfer, but some syntax and setup steps have changed.

---

## Week 12 — Airflow Fundamentals (the on-ramp week)

**Primary:**
- [Astronomer — "Learn Airflow 3"](https://www.astronomer.io/docs/learn/) — free, written by the core Airflow maintainers' company, explicitly updated for Airflow 3. This should be your main spine for the week.
- [Astro CLI documentation](https://www.astronomer.io/docs/astro/cli/overview) — install this first. It runs Airflow locally in Docker for you, so you're not fighting a manual Airflow install on day one. (You'll have Docker fundamentals properly by Phase F, but running `astro dev start` this week doesn't require deep Docker knowledge — just install Docker Desktop and let the CLI handle it.)

**Official docs (for reference, not linear reading):**
- [Apache Airflow official docs — "Concepts"](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html) — DAGs, tasks, operators, the scheduler. Read this after Astronomer's tutorial, as reinforcement.

**Your first DAG:**
- [Astronomer — "Get started with Apache Airflow" tutorial](https://www.astronomer.io/docs/learn/get-started-with-airflow/) — walks through writing a DAG with the `@task` decorator and BashOperator, exactly what Monday/Tuesday need.

---

## Week 13 — Airflow Hardening (DAG Design, Retries, Backfills, SLAs)

**Primary:**
- [Astronomer — "Airflow Operators 101"](https://www.astronomer.io/docs/learn/what-is-an-operator/) — read before Tuesday's custom operator work.
- [Astronomer — "Managing your connections in Apache Airflow"](https://www.astronomer.io/docs/learn/connections) — needed for Tuesday's hooks/connection pooling work.
- [Official docs — "Executor" and "Scheduler" concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/index.html) — for understanding what actually happens during a retry or backfill under the hood.

**Backfills specifically:**
- Search "Astronomer backfill best practices" — backfills are one of the areas where doing it wrong causes real duplicate-data incidents; Astronomer's own written guides on this are current and specific.

**DAG design patterns:**
- [Astronomer — "DAG Writing Best Practices"](https://www.astronomer.io/docs/learn/dag-best-practices) — covers task groups, dynamic task mapping, and idempotency patterns directly relevant to this week's daily objectives.

**Observability/alerting (Friday):**
- [Official docs — "Logging & Monitoring"](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/index.html) — for the logging half; for Slack/email alerting specifically, search "Airflow Slack notifier" for the current provider package setup.

---

## A note on why this phase is only now happening

You'll notice Weeks 6–11 never touched orchestration at all. That's intentional — Airflow's job is to *schedule and monitor* the pipelines you already know how to build. Doing it in the old order (orchestration before you'd built anything worth orchestrating) is why the original roadmap's Airflow week felt disconnected. Now it isn't.