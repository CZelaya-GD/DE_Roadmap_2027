# Week 17 Plan: Docker & Containerization

## Overview

- **Phase:** F — Indispensable Tier
- **Focus:** Building and running containers for real
- **Goal:** Move from Week 5's conceptual "what is a container" to actually building, running, and shipping containerized versions of your own pipelines
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** Images vs. containers (real depth this time), running official images, `docker run` flags that matter (ports, volumes, env vars) → Deliverable: 3 different official images run locally with correct port/volume/env configuration
- **Tuesday:** Writing your first Dockerfile from scratch for a simple Python script → Deliverable: 1 custom image built and run, containing a script from an earlier phase
- **Wednesday:** Dockerfile best practices — minimal base images, `.dockerignore`, non-root users, specific version tags → Deliverable: previous day's Dockerfile refactored to follow all four practices, with a before/after image size comparison
- **Thursday:** Docker Compose — running multi-container setups (e.g. a Python app + a database) → Deliverable: 1 working `docker-compose.yml` running at least 2 services together
- **Friday:** Containerize a real pipeline — pick one script or dbt project from Phases B or C and package it as a Docker image → Deliverable: 1 of your own real pipelines now runs identically via `docker run`, regardless of what's installed on the host machine

### Anki Targets

- Monday: 5 cards tagged `infra::docker::fundamentals`
- Tuesday: 5 cards tagged `infra::docker::dockerfile`
- Wednesday: 5 cards tagged `infra::docker::best-practices`
- Thursday: 5 cards tagged `infra::docker::compose`
- Friday: 5 cards tagged `infra::docker::real-pipeline`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Explain out loud why "it works on my machine" stops being a valid excuse once something is containerized
- Draft next week's objectives (Infra-as-Code + Cloud Security Basics)

---

## Week 17 Success Metrics
- [ ] 25 Anki cards created
- [ ] 1 custom Dockerfile written and refactored for best practices
- [ ] 1 working multi-container Compose setup
- [ ] 1 real pipeline from an earlier phase successfully containerized
- [ ] Comfortable explaining images vs. containers to someone else
- [ ] Week 18 plan drafted