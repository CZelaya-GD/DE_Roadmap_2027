# Week 25 Plan: CI/CD for Data Pipelines

## Overview

- **Phase:** I — Advanced Cloud & CI/CD
- **Focus:** Automated testing and deployment for data pipelines specifically
- **Goal:** Set up real continuous integration on your own roadmap repo, so pipeline changes are tested automatically before they can break anything — closing a gap that's existed silently since Phase B
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** CI/CD concepts for data specifically (why testing data pipelines differs from testing typical application code — data itself can be wrong even when the code is correct), GitHub Actions fundamentals → Deliverable: 1 basic GitHub Actions workflow running on push (even something trivial, like a linter)
- **Tuesday:** Running Python tests automatically — `pytest` in CI, testing the Phase A Python scripts (Week 4) with real unit tests for the first time → Deliverable: 1 GitHub Actions workflow running a pytest suite on your Phase A scripts
- **Wednesday:** Running dbt tests in CI — connect GitHub Actions to your Phase B dbt project (Week 14's data quality tests), triggered on pull request → Deliverable: 1 CI workflow that runs `dbt test` automatically on every PR
- **Thursday:** Linting and code quality gates (`ruff` or `flake8` for Python, `sqlfluff` for SQL) as required CI checks → Deliverable: CI workflow that blocks a merge if linting fails, tested with a deliberately bad commit
- **Friday:** Continuous deployment basics — automatically deploying a Docker image (Phase F) to a registry on merge to main → Deliverable: 1 workflow that builds and pushes a Docker image automatically on merge

### Anki Targets

- Monday: 5 cards tagged `devops::ci-cd::fundamentals`
- Tuesday: 5 cards tagged `devops::ci-cd::testing`
- Wednesday: 5 cards tagged `devops::ci-cd::dbt`
- Thursday: 5 cards tagged `devops::ci-cd::linting`
- Friday: 5 cards tagged `devops::ci-cd::deployment`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Explain out loud why testing data pipelines needs both code tests (pytest) and data tests (dbt test) — they catch different classes of problems
- Draft next week's objectives (GCP Deep-Dive: Dataflow, Cloud Composer)

---

## Week 25 Success Metrics
- [ ] 25 Anki cards created
- [ ] 1 working CI pipeline testing Python code
- [ ] 1 working CI pipeline testing dbt models on every PR
- [ ] 1 CI gate that successfully blocks a bad commit
- [ ] 1 automated Docker image build/push on merge
- [ ] Week 26 plan drafted