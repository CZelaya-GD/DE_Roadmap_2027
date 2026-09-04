# Data Quality Checklist

## Pre-Load Validation

- [ ] **Schema Validation**
  - Column names match expected schema
  - Data types correct (INT, STRING, TIMESTAMP)
  - No unexpected columns added

- [ ] **Null Checks**
  - Primary keys: 0% nulls allowed
  - Critical columns: <1% nulls (or business threshold)
  - Document acceptable null rates per column

- [ ] **Duplicate Checks**
  - Primary keys: 0% duplicates allowed
  - Business keys: verify deduplication logic
  - Document acceptable dupe rates

---

## Post-Load Validation

- [ ] **Row Count Checks**
  - Expected vs actual row count (within tolerance)
  - Day-over-day change: <X% variance (or alert)
  - Source vs target: row counts match

- [ ] **Freshness Checks**
  - Data timestamp within SLA (e.g., <1 hour old)
  - Pipeline completed within expected window
  - Alert on SLA breach

- [ ] **Value Range Checks**
  - Numeric columns within expected min/max
  - Categorical columns contain only allowed values
  - Timestamps within reasonable range (no year 1900 or 2099)

---

## Anomaly Detection

- [ ] **Statistical Thresholds**
  - Mean/stddev monitoring (alert on >3σ deviation)
  - Percentile checks (p50, p95, p99)
  - Trend detection (sudden drops/spikes)

- [ ] **Business Logic Checks**
  - Revenue = sum of line items
  - Funnel stages: each stage ≤ previous stage
  - Referential integrity (foreign keys valid)

---

## Implementation Patterns

### dbt Tests
```yaml
# models/schema.yml
models:
  - name: orders
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
      - name: status
        tests:
          - accepted_values:
              values: ['pending', 'shipped', 'delivered']
```

### Great Expectations
```python
# expectations.json
{
  "expect_column_values_to_not_be_null": {"column": "order_id"},
  "expect_column_values_to_be_unique": {"column": "order_id"},
  "expect_column_values_to_be_in_set": {"column": "status", "value_set": ["pending", "shipped", "delivered"]}
}
```

### Custom SQL Checks
```sql
-- Null check
SELECT COUNT(*) as null_count
FROM orders
WHERE order_id IS NULL;
-- Expect: 0

-- Duplicate check
SELECT order_id, COUNT(*) as cnt
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;
-- Expect: 0 rows

-- Freshness check
SELECT MAX(order_timestamp) as latest_order
FROM orders;
-- Expect: within last 1 hour
```

---

## Alerting Thresholds

| Check Type | Warning | Critical |
|------------|---------|----------|
| Null rate (critical column) | >0.1% | >1% |
| Duplicate rate (primary key) | >0 | >0 |
| Freshness SLA breach | >30 min | >1 hour |
| Row count variance | >10% | >50% |
| Value out of range | >1% | >5% |

---

## Weekly Review
Every Sunday, review DQ alerts from the week. Ask:
- Which checks fired most often?
- Are thresholds too strict/loose?
- What new checks should we add?