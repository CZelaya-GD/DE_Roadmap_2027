# Data Engineering Skill Tree (2027–2030)

## Foundational

### SQL
- Window functions (ROW_NUMBER, RANK, LAG/LEAD, running totals)
- CTEs & subquery refactoring (recursive CTEs, lateral joins)
- Query optimization (EXPLAIN plans, index/partition strategies, cost estimation)
- Data modeling (normalization, star/snowflake schemas, grain definition)
- Advanced patterns (pivot/unpivot, array/struct handling, JSON parsing)

### Python (data scripting)
- Data manipulation (pandas, polars, vectorization vs loops)
- API integration (requests, async aiohttp, rate limiting, pagination)
- Packaging & modularity (virtualenv, setup.py, imports, logging)
- Error handling & retries (try/except, exponential backoff, idempotency)
- Data validation (pydantic, type hints, schema enforcement)

### Linux/CLI + Git
- Shell scripting (bash, pipes, grep/awk/sed, cron jobs)
- File system & permissions (chmod, chown, symlinks, disk usage)
- Git workflows (branching, rebasing, PRs, conflict resolution)
- CI/CD basics (GitHub Actions, runners, secrets management)
- Container basics (Dockerfile, docker-compose, volume mapping)

### Data Modeling
- Normalization (1NF–3NF, denormalization trade-offs)
- Dimensional modeling (fact/dimension tables, surrogate keys)
- Schema evolution (backward/forward compatibility, migration strategies)
- Data contracts (schema/SLA agreements, breaking-change detection)
- Feature schemas (ML-ready tables, timestamp handling, leakage prevention)

### Cloud Fundamentals (one platform at depth)
- IAM & security (roles, policies, service accounts, least privilege)
- Storage (object storage, lifecycle policies, access patterns)
- Compute (VMs, serverless, containers, scaling)
- Networking (VPC, subnets, firewalls, private endpoints)
- Cost management (budgets, alerts, cost explorer, tagging)

## High-Demand

### Warehouse (BigQuery/Snowflake/Databricks)
- Loading data (COPY INTO, external tables, streaming inserts)
- Partitioning & clustering (partition keys, clustering columns, pruning)
- Query optimization (materialized views, result caching, warehouse sizing)
- Security (row-level security, column masking, data sharing)
- Cost control (slot management, credit monitoring, query cost attribution)

### Orchestration (Airflow → Dagster)
- DAG design (task dependencies, dynamic task mapping, sensor patterns)
- Operators & hooks (custom operators, connection pooling, XComs)
- Backfills & retries (idempotent backfills, retry policies, SLAs)
- Observability (task logging, alerting, lineage integration)
- Asset-based orchestration (Dagster assets, dependencies, materialization)

### Transformation (dbt)
- Model layering (staging → intermediate → marts, ref() patterns)
- Materialization strategies (table, view, incremental, ephemeral)
- Testing (schema tests, data tests, custom tests, severity levels)
- Documentation (auto-docs, descriptions, lineage graphs)
- Macro & package development (DRY patterns, Jinja templating, custom packages)

### Containerization (Docker + Kubernetes basics)
- Dockerfile optimization (multi-stage builds, layer caching, image size)
- docker-compose (profiles, healthchecks, volume persistence)
- Networking (bridge vs host, port mapping, service discovery)
- Kubernetes basics (pods, deployments, services, configmaps)
- Helm charts (templating, values overrides, chart repositories)

### Streaming (Kafka/Kinesis + Flink/Spark Structured Streaming)
- Producers & consumers (serialization, partitioning, consumer groups)
- Topic design (partitioning strategy, retention, compaction)
- Stream processing (windowing, watermarks, state management)
- Exactly-once semantics (idempotent producers, transactional writes)
- Integration (Kafka Connect, schema registry, sink connectors)

### Data Quality/Observability
- Validation frameworks (Great Expectations, dbt tests, custom checks)
- Anomaly detection (statistical thresholds, ML-based drift detection)
- Freshness monitoring (SLA breaches, lag metrics, alerting)
- Lineage tracking (column-level lineage, dependency graphs)
- Dashboards (volume, quality, freshness, error rates)

## Indispensable

### Data Governance
- Catalog & metadata (data dictionaries, business glossaries)
- Lineage (automated lineage, impact analysis, upstream/downstream tracing)
- Data contracts (schema versioning, SLA enforcement, consumer agreements)
- Access control (RBAC, ABAC, data masking, audit logging)
- Compliance (GDPR, CCPA, EU AI Act, data residency)

### Security & Compliance
- Encryption (at rest, in transit, key management, HSM)
- PII handling (discovery, masking, tokenization, right-to-erasure)
- Secrets management (Vault, cloud KMS, rotation policies)
- Audit trails (access logs, query logs, change tracking)
- Risk assessment (threat modeling, vulnerability scanning, incident classification)

### Cost Optimization & FinOps
- Query tuning (predicate pushdown, partition pruning, materialized views)
- Resource right-sizing (warehouse sizing, cluster autoscaling)
- Cost attribution (project/job/user-level cost tracking)
- Budget enforcement (alerts, quotas, spend limits)
- FinOps practices (showback/chargeback, cost allocation tags, forecasting)

### Incident Response & SLAs
- Alerting (thresholds, anomaly alerts, escalation policies)
- Runbooks (triage steps, rollback procedures, backfill strategies)
- SLAs & SLOs (freshness, availability, error budgets)
- Stakeholder communication (status pages, incident templates, post-mortems)
- On-call rotation (scheduling, handover, fatigue management)

### Documentation & Handover
- SOPs (standard operating procedures, step-by-step guides)
- Architecture diagrams (C4 model, data flow diagrams, sequence diagrams)
- Decision logs (RFCs, ADRs, trade-off documentation)
- Knowledge transfer (shadowing, recorded walkthroughs, FAQs)
- Versioned documentation (docs as code, changelogs, deprecation notices)

## New-Tech / AI Multiplier

### Agentic AI Workflows
- Agent orchestration (task decomposition, handoff design, multi-agent coordination)
- Tool integration (APIs, function calling, output validation)
- Prompt engineering (few-shot, chain-of-thought, self-correction)
- Evaluation (output quality metrics, human-in-the-loop review)
- Safety & guardrails (content filtering, rate limiting, fallback strategies)

### Vector Databases + Embedding Pipelines
- Embedding generation (model selection, batch vs streaming, dimensionality)
- Vector indexing (HNSW, IVF, quantization, recall vs speed trade-offs)
- Similarity search (k-NN, ANN, hybrid search with metadata filters)
- Pipeline integration (batch ingestion, real-time updates, CDC to vectors)
- Performance tuning (index size, query latency, memory vs disk)

### RAG Infrastructure
- Retrieval strategies (chunking, overlap, hierarchical retrieval)
- Prompt chaining (query rewriting, multi-hop retrieval, re-ranking)
- Evaluation (retrieval precision/recall, answer faithfulness, hallucination detection)
- Caching (embedding cache, response cache, TTL strategies)
- Production patterns (fallbacks, hybrid retrieval, A/B testing)

### MLOps
- Feature stores (online/offline stores, feature versioning, serving)
- Model serving (REST/gRPC endpoints, batch inference, canary deployments)
- Drift detection (feature drift, concept drift, alerting thresholds)
- Experiment tracking (MLflow, Weights & Biases, reproducibility)
- Pipeline integration (training pipelines, inference pipelines, retraining triggers)

### Edge Intelligence + Real-Time Decisioning
- Edge deployment (model compression, quantization, ONNX runtime)
- Latency optimization (inference time, batch vs streaming, caching)
- Real-time features (streaming aggregations, sessionization, TTL features)
- Decision engines (rules engines, scoring models, A/B testing)
- Monitoring (latency SLAs, error rates, fallback strategies)

### AI-Assisted Engineering
- Code generation (boilerplate, refactoring, test generation)
- Debugging (error explanation, stack trace analysis, fix suggestions)
- Documentation (docstrings, README generation, changelog drafting)
- Review assistance (PR summaries, complexity analysis, security flags)
- Output evaluation (correctness checks, test coverage, performance profiling)

### Systems Thinking + Stakeholder Translation
- Architecture trade-offs (batch vs streaming, warehouse vs lakehouse, consistency vs latency)
- Stakeholder mapping (data producers, consumers, governance, security)
- Risk assessment (single points of failure, blast radius, recovery time)
- Communication (technical → business translation, status updates, escalation)
- Strategic alignment (business goals → data strategy, ROI justification, prioritization)