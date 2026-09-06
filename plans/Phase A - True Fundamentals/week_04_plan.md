# Week 4 Plan: Python for Data Engineers

## Overview

- **Phase:** A — True Fundamentals
- **Focus:** Software-engineering habits for data code
- **Goal:** Close the gap your own pitfalls.md flags (mistakes #6–10: no type hints, credentials in code, no error handling, loops instead of vectorization, no logging) before PySpark makes those habits expensive to fix
- **Anki Target:** 25 cards

---

## Monday–Friday

### Daily Objectives

- **Monday:** Type hints, dataclasses, intro to pydantic for data validation → Deliverable: 1 script validating a messy CSV's schema with pydantic
- **Tuesday:** Error handling (try/except patterns), retries with exponential backoff, writing idempotent functions → Deliverable: 1 script that safely retries a flaky operation (simulate with a function that randomly fails)
- **Wednesday:** Environment variables & secrets management (never hardcode credentials), virtual environments, requirements files → Deliverable: 1 script reading a fake API key from an env var, with a .env.example committed instead of real secrets
- **Thursday:** Vectorization with pandas (why loops are slow), basic profiling → Deliverable: 1 script rewritten from a for-loop to vectorized pandas, with a timing comparison
- **Friday:** Logging module (structured logs, log levels), git basics (init, commit, .gitignore for a data project) → Deliverable: 1 script with proper logging, committed to a new git repo

### Anki Targets

- Monday: 5 cards tagged `python::validation`
- Tuesday: 5 cards tagged `python::error-handling`
- Wednesday: 5 cards tagged `python::secrets`
- Thursday: 5 cards tagged `python::performance`
- Friday: 5 cards tagged `python::logging`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Rebuild one error-handling pattern from memory
- Draft next week's objectives

---

## Week 4 Success Metrics
- [ ] 25 Anki cards created
- [ ] 5 scripts written, each demonstrating one habit above
- [ ] Zero hardcoded credentials anywhere in your practice repo
- [ ] Week 5 plan drafted