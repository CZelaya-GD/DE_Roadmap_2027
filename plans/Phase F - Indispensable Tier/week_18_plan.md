# Week 18 Plan: Infra-as-Code + Cloud Security Basics

## Overview

- **Phase:** F — Indispensable Tier (final week)
- **Focus:** Terraform fundamentals, IAM in practice, cost awareness
- **Goal:** Provision real cloud infrastructure through code instead of clicking through a console, and write least-privilege IAM policies deliberately rather than defaulting to broad permissions
- **Anki Target:** 25 cards
- **Why this week matters more than it might seem:** This is precisely the tier your own skill tree ranked as "Indispensable" — above the flashier AI/vector work coming in Phase G. Security and infra mistakes are also the kind that cause real incidents, not just inconvenient bugs.

---

## Monday–Friday

### Daily Objectives

- **Monday:** Terraform core concepts — providers, resources, state, the `init` → `plan` → `apply` workflow → Deliverable: 1 simple resource (e.g. a Cloud Storage bucket) provisioned entirely through Terraform
- **Tuesday:** Variables, outputs, and structuring a small Terraform project across multiple files → Deliverable: 1 reusable Terraform configuration with variables for environment-specific values
- **Wednesday:** IAM as code — writing a least-privilege custom role via Terraform (revisit Week 5's IAM concepts, now implemented properly) → Deliverable: 1 service account + custom role provisioned via Terraform, tested to confirm it can't do more than intended
- **Thursday:** Cost tagging/labeling resources for attribution, setting a budget alert via Terraform instead of the console → Deliverable: all Week 18 resources labeled, 1 budget alert provisioned as code
- **Friday:** Provision a small piece of real infrastructure for an earlier pipeline (e.g. the Cloud Storage bucket your Week 5 script wrote to) entirely via Terraform, then practice `terraform destroy` to tear it down cleanly → Deliverable: 1 real infra piece fully managed as code, destroyed cleanly at the end

### Anki Targets

- Monday: 5 cards tagged `infra::terraform::fundamentals`
- Tuesday: 5 cards tagged `infra::terraform::structure`
- Wednesday: 5 cards tagged `infra::terraform::iam`
- Thursday: 5 cards tagged `infra::terraform::cost`
- Friday: 5 cards tagged `infra::terraform::lifecycle`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Phase
- Review all Anki cards from the week
- Explain out loud the `init` → `plan` → `apply` → `destroy` lifecycle and why `plan` matters before `apply`
- Write a short Phase F retrospective: how did having Docker + Terraform change how confident you feel about "shipping" something, versus just building it?
- Draft Phase G objectives (Vector DBs/Embeddings/RAG, then the flagship project)

---

## Week 18 Success Metrics
- [ ] 25 Anki cards created
- [ ] 1 reusable Terraform configuration written
- [ ] 1 least-privilege IAM role provisioned and tested via Terraform
- [ ] 1 budget alert provisioned as code
- [ ] All practice infrastructure cleanly destroyed (no lingering cloud costs)
- [ ] Phase F retrospective written
- [ ] Phase G (Week 19) plan drafted