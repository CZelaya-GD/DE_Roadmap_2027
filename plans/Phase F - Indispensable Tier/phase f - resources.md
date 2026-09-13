# Phase F Resources: Indispensable Tier (Docker, IaC, Security)

This is the tier your own `skill_tree.md` ranked above "New-Tech/AI Multiplier" — and it's arriving here, before the RAG/vector work in Phase G, on purpose.

---

## Week 17 — Docker & Containerization

**Primary:**
- [Docker's own official "Get Started" guide](https://docs.docker.com/get-started/) — this is the canonical starting point; walks through running your first container, building an image, and Docker Compose for multi-container setups.
- Search "Docker Tutorial for Beginners 2026" (KodeKloud's version, or similar current guides) — worth using a 2026-dated tutorial specifically, since Docker has added newer tooling (`docker init`, `docker scout` for vulnerability scanning) that older tutorials won't mention.

**Dockerfile best practices:**
- [Docker docs — "Dockerfile best practices"](https://docs.docker.com/build/building/best-practices/) — read this before Wednesday; small, secure images (non-root users, minimal base images, specific version tags instead of `latest`) are the difference between a Dockerfile that works and one a team would actually accept in a PR review.

**Connecting to your own work:**
- Once comfortable with the basics, containerize one of your existing pipelines (a Phase B dbt project or a Phase C PySpark script) — there isn't a single canonical tutorial for this since it depends on your exact tool, but Docker's official docs' "Containerize an application" walkthrough is close enough to adapt.

---

## Week 18 — Infra-as-Code + Cloud Security Basics

**Primary:**
- [HashiCorp's official Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials) — choose the Google Cloud track specifically, since it lines up with your existing GCP work from Phase B. Free, official, hands-on.
- [Terraform official docs — "Configuration Language"](https://developer.hashicorp.com/terraform/language) — reference material for HCL syntax as you go.

**IAM in practice (deeper than Phase A's introduction):**
- [Google Cloud IAM docs — "Understanding roles"](https://cloud.google.com/iam/docs/understanding-roles) — this week is about actually writing least-privilege policies via Terraform, not just reading about the concept as in Week 5.

**Cost tagging/FinOps basics:**
- Search "GCP resource labels cost tracking" — labeling resources so costs can be attributed to a project/team is a small, concrete practice worth building now, ahead of the deeper FinOps work in Phase K.

**A genuinely important habit to build this week:**
- `terraform plan` before every `terraform apply`, and `terraform destroy` any practice infrastructure the same day you're done with it — free-tier cloud accounts can still accrue real charges if resources are left running. Building this habit now, while stakes are low, prevents an expensive surprise later.