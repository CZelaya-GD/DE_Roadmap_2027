# Week 24 Plan: Kubernetes Fundamentals

## Overview

- **Phase:** I — Advanced Cloud & CI/CD
- **Focus:** Container orchestration at scale
- **Goal:** Understand why Docker (Phase F) alone isn't enough once you have more than a couple of containers to manage, and deploy a real container to a Kubernetes cluster
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** Why Kubernetes exists (the problem of managing many containers across many machines), core architecture (control plane, nodes), install `kind` and create a local cluster → Deliverable: local Kubernetes cluster running, `kubectl` verified working
- **Tuesday:** Pods — the smallest deployable unit, writing your first Pod YAML manifest → Deliverable: 1 Pod deployed and inspected via `kubectl`
- **Wednesday:** Deployments — managing replicas, rolling updates, self-healing (kill a pod manually, watch Kubernetes replace it) → Deliverable: 1 Deployment with 3 replicas, tested by manually deleting a pod and observing recovery
- **Thursday:** Services — exposing pods on a stable network endpoint, load balancing across replicas → Deliverable: 1 Service exposing your Deployment, tested with repeated requests showing load distribution
- **Friday:** Deploy one of your own Phase F Docker images (Week 17) to your local cluster, end to end → Deliverable: your own containerized pipeline running on Kubernetes, not just a tutorial app

### Anki Targets

- Monday: 5 cards tagged `infra::kubernetes::fundamentals`
- Tuesday: 5 cards tagged `infra::kubernetes::pods`
- Wednesday: 5 cards tagged `infra::kubernetes::deployments`
- Thursday: 5 cards tagged `infra::kubernetes::services`
- Friday: 5 cards tagged `infra::kubernetes::applied`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Explain out loud why a Deployment is usually preferred over managing bare Pods directly
- Draft next week's objectives (CI/CD for Data Pipelines)

---

## Week 24 Success Metrics
- [ ] 25 Anki cards created
- [ ] Local Kubernetes cluster running via `kind`
- [ ] 1 Deployment demonstrating self-healing behavior
- [ ] 1 Service correctly load-balancing across replicas
- [ ] 1 of your own Docker images successfully deployed to the cluster
- [ ] Week 25 plan drafted