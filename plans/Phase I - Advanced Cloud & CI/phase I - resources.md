# Phase I Resources: Advanced Cloud & CI/CD

---

## Week 24 — Kubernetes Fundamentals

**Primary:**
- [Official Kubernetes documentation — "Kubernetes Basics" tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/) — the canonical, official, browser-based interactive tutorial. Start here.
- [KodeKloud — free Kubernetes labs](https://kodekloud.com/) — browser-based, no local setup required, widely recommended for hands-on practice in 2026 roundups.

**Local cluster setup (if you want to run things on your own machine):**
- `kind` (Kubernetes in Docker) — the fastest way to spin up a local cluster in 2026; search "kind Kubernetes quickstart" for the current install/setup steps.
- Alternative: `minikube` — slightly heavier but also well-documented and commonly used for local learning.

**Core concepts to prioritize (in order):**
- Pods → Deployments → Services → Ingress. Official docs' "Kubernetes Basics" tutorial covers exactly this progression; don't skip ahead to more advanced topics (Helm, operators) until these four are solid.

**Connecting to your own work:**
- Once comfortable, deploy one of your Phase F Docker images (Week 17) to your local `kind` cluster as a real exercise — more valuable than a generic tutorial app.

---

## Week 25 — CI/CD for Data Pipelines

**Primary:**
- [GitHub Actions official documentation — "Quickstart"](https://docs.github.com/en/actions/quickstart) — free for public repos (and generous free tier for private ones), directly usable on your existing roadmap repo.
- Search "GitHub Actions for data pipelines dbt testing" — CI/CD applied specifically to data (running `dbt test` on every pull request, for example) is a slightly different pattern than typical software CI/CD; look for content specifically discussing data pipeline testing, not just generic app deployment.

**Testing pipelines specifically:**
- [dbt docs — "Continuous integration"](https://docs.getdbt.com/docs/deploy/continuous-integration) — dbt's own official guide to running tests automatically in CI, directly applicable to your Phase B project.

**Connecting to your own work:**
- Set up a GitHub Actions workflow that runs your Phase B dbt tests (Week 14) automatically on every push — this is the single most useful, portfolio-relevant deliverable this week can produce.

---

## Week 26 — GCP Deep-Dive (Dataflow, Cloud Composer)

**Primary:**
- [Apache Beam Programming Guide](https://beam.apache.org/documentation/programming-guide/) — Dataflow is Google's managed runner for Apache Beam pipelines, so understanding Beam's programming model first makes Dataflow make sense.
- [Google Cloud — Dataflow documentation](https://cloud.google.com/dataflow/docs) — official docs, including the "Dataflow templates" concept for common pipeline patterns.
- [KodeKloud — "Cloud Composer: Orchestrating Data Workflows"](https://notes.kodekloud.com/) — search this exact title; a clear, current lesson explaining Composer as "Google's managed Airflow" — directly relevant since you already know Airflow from Phase D.

**Understanding Composer vs. self-managed Airflow:**
- Composer is genuinely just Airflow, run and maintained by Google — the DAG-writing skills from Phase D transfer directly. This week is about the operational differences (who manages upgrades, scaling, infrastructure) rather than learning DAG syntax again.

**A real project pattern worth studying:**
- Search "GCP ETL Composer Dataflow BigQuery project" — several complete example projects (GCS → Composer orchestrating Dataflow → BigQuery → BI tool) are publicly documented on GitHub; useful for seeing how these three services combine in a realistic architecture before you build your own version.