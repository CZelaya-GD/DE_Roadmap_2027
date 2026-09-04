# Incident Response Playbook

## Severity Levels

- **P0 (Critical):** Data loss, complete outage, security breach
- **P1 (High):** Major pipeline failure, SLA breach, downstream impact
- **P2 (Medium):** Partial failure, degraded performance, no downstream impact
- **P3 (Low):** Minor issue, cosmetic, no user impact

---

## Immediate Response (First 15 Minutes)

### Step 1: Acknowledge & Triage
- [ ] Acknowledge alert in Slack/Teams
- [ ] Identify severity (P0–P3)
- [ ] Assign incident owner (if not you)

### Step 2: Assess Impact
- [ ] Which pipelines are affected?
- [ ] Which downstream consumers are impacted?
- [ ] Is data lost or just delayed?

### Step 3: Communicate
- [ ] Post status update: "Investigating [pipeline] failure, ETA 30 min"
- [ ] Tag stakeholders (data consumers, product owners)

---

## Resolution Steps

### Step 4: Diagnose
- [ ] Check logs (Airflow UI, Cloud Logging, application logs)
- [ ] Identify root cause (schema change, API failure, resource exhaustion)
- [ ] Document findings in incident channel

### Step 5: Rollback or Fix
- [ ] If recent deployment caused it → Rollback immediately
- [ ] If data issue → Pause pipeline, prevent further corruption
- [ ] If infrastructure → Scale up, restart, or failover

### Step 6: Backfill
- [ ] Determine affected time range
- [ ] Run backfill with idempotent logic
- [ ] Verify data quality post-backfill

---

## Post-Incident

### Step 7: Stakeholder Communication
- [ ] Send resolution update: "Resolved, root cause: X, prevention: Y"
- [ ] Update status page (if applicable)

### Step 8: Post-Mortem (Within 48 Hours)
- [ ] Write incident report:
  - Timeline (what happened when)
  - Root cause
  - Impact (rows affected, downtime duration)
  - Prevention (what we'll do differently)
- [ ] Schedule follow-up (implement prevention items)

### Step 9: Update Runbooks
- [ ] Add new failure mode to this playbook
- [ ] Update monitoring/alerting if gap identified

---

## Template: Incident Report

## Incident: [Pipeline Name] Failure

Date: YYYY-MM-DD
Severity: P0 / P1 / P2 / P3
Duration: X hours Y minutes

### Timeline

- HH:MM — Alert triggered
- HH:MM — Triage started
- HH:MM — Root cause identified
- HH:MM — Fix deployed
- HH:MM — Backfill completed

### Root Cause

[Describe what caused the failure]

### Impact

- Rows affected: X
- Downstream consumers: [list]
- SLA breach: Yes / No

### Prevention

- [ ] Action item 1 (owner, due date)
- [ ] Action item 2 (owner, due date)

---

## Contacts

- On-call: [Your name/rotation]
- Escalation: [Manager/Stakeholder]
- Slack Channel: #data-incidents