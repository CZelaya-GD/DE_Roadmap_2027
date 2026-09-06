# Phase C Resources: Distributed Processing (PySpark)

---

## Week 10 — PySpark Fundamentals

**Primary:**
- [Official PySpark Documentation — "PySpark Overview"](https://spark.apache.org/docs/latest/api/python/index.html) — current version as of 2026 is Spark 4.1.x; start here for the quickstart guide, it's more precise than any third-party tutorial.
- [Databricks Free Edition](https://www.databricks.com/product/faq/community-edition) — free, hosted PySpark environment. This matters more than it sounds: you don't need to fight local Java/Spark installation issues before you've even written your first DataFrame.

**Structured learning:**
- [freeCodeCamp — "PySpark Full Course"](https://www.freecodecamp.org/news/) — search their site or YouTube channel for the current PySpark full course; freeCodeCamp's data engineering content is free, long-form, and project-based.

**Concept-first (if you want the "why" before the "how"):**
- Search "Apache Spark in 100 Seconds" (Fireship) on YouTube — a genuinely useful 3-minute framing of why Spark exists before you spend a week in its syntax.

**RDD vs. DataFrame concept:**
- [Official docs — "RDD Programming Guide"](https://spark.apache.org/docs/latest/rdd-programming-guide.html) — read only the introduction/motivation section; you'll work almost entirely in DataFrames day-to-day, but understanding what they're built on matters for debugging later.

---

## Week 11 — PySpark Performance (Joins, Shuffles, Skew, Caching)

**Primary:**
- [Official docs — "Performance Tuning"](https://spark.apache.org/docs/latest/sql-performance-tuning.html) — the authoritative source on join strategies, broadcast thresholds, and caching.
- Search "PySpark Optimization Full Course" (Ansh Lamba, or similar current creators) on YouTube — several long-form, hands-on optimization courses are actively maintained and frequently recommended in 2025–2026 roundups; look for anything explicitly using Spark 3.5+ or 4.x syntax so it matches what you installed in Week 10.

**Data skew specifically:**
- Search "PySpark data skew salting technique" — this is a narrow enough topic that a few well-explained blog posts (rather than one canonical doc page) will serve you better; read at least two different explanations since the salting technique is explained inconsistently across sources.

**Spark UI (for diagnosing shuffles/skew visually):**
- [Official docs — "Web UI"](https://spark.apache.org/docs/latest/web-ui.html) — learn to read this now; it's the single most useful diagnostic tool you'll return to for the rest of your PySpark work.

---

## A note on Spark versions

Spark's Python API has moved fast in recent years (Spark Connect, new pandas-API integration, Declarative Pipelines). Whatever tutorial you use, check that it's using Spark 3.5 or later — anything built on Spark 2.x syntax will teach you patterns that are now discouraged or removed.