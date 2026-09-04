# Top 20 Beginner Data Engineering Mistakes

## SQL Mistakes

1. **Using SELECT * everywhere**
   - Problem: Wastes I/O, breaks schemas, prevents partition pruning
   - Fix: Always name columns explicitly

2. **Wrong grain joins (fan-out)**
   - Problem: Duplicates rows, inflates metrics
   - Fix: Understand join keys, verify row counts before/after

3. **No timeout on API requests**
   - Problem: Scripts hang indefinitely
   - Fix: Always set `timeout=` in `requests.get()`

4. **Treating warehouses like OLTP databases**
   - Problem: Row-by-row updates, frequent small writes
   - Fix: Batch loads, bulk upserts, append-only patterns

5. **Skipping staging layer**
   - Problem: Raw data directly in production tables
   - Fix: Always land raw first, then transform to staged/curated

## Python Mistakes

6. **No type hints or data validation**
   - Problem: Silent schema drift, hard-to-debug errors
   - Fix: Use `pydantic`, type hints, assert schemas

7. **Storing credentials in code**
   - Problem: Security risk, accidental commits
   - Fix: Use environment variables, secrets managers

8. **No error handling or retries**
   - Problem: Pipelines fail silently or crash on transient errors
   - Fix: Try/except, exponential backoff, idempotent writes

9. **Using loops instead of vectorization**
   - Problem: 100x slower on large datasets
   - Fix: Use pandas/polars vectorized operations

10. **No logging or monitoring**
    - Problem: Can't debug failures in production
    - Fix: Use `logging` module, structured logs, alerting

## Architecture Mistakes

11. **Building real-time when batch is enough**
    - Problem: Unnecessary complexity, cost, maintenance
    - Fix: Ask: "Do we need sub-second freshness?" If no, use batch

12. **No idempotency in pipelines**
    - Problem: Re-runs create duplicates
    - Fix: Use `INSERT OVERWRITE`, `MERGE`, or deduplication logic

13. **Overengineering early (Kubernetes, microservices)**
    - Problem: Premature optimization, hard to maintain
    - Fix: Start simple (Docker Compose), scale when needed

14. **No data quality checks**
    - Problem: Bad data propagates downstream
    - Fix: Add validation gates (null checks, dupe checks, schema validation)

15. **Ignoring cost optimization**
    - Problem: Surprise bills, inefficient queries
    - Fix: Use partitioning, clustering, EXPLAIN, cost attribution

## Operational Mistakes

16. **No documentation or handover**
    - Problem: Bus factor = 1, hard to onboard
    - Fix: SOPs, architecture diagrams, decision logs

17. **No incident runbooks**
    - Problem: Panic during outages, slow recovery
    - Fix: Pre-written triage steps, rollback procedures

18. **No SLAs or SLOs**
    - Problem: Unclear expectations, constant fire drills
    - Fix: Define freshness, availability, error budgets

19. **Skipping testing**
    - Problem: Broken pipelines in production
    - Fix: Unit tests, integration tests, data tests (dbt, Great Expectations)

20. **Tutorial hell (no end-to-end projects)**
    - Problem: Can't demonstrate real skills
    - Fix: Build one complete pipeline > ten tutorials

---

## Weekly Review
Every Sunday, review this list. Ask: "Did I make any of these mistakes this week? How do I prevent them next week?"