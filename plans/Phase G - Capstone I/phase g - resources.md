# Phase G Resources: Vector DBs, RAG & Flagship Project I

---

## Week 19 — Vector DBs, Embeddings & RAG

**Primary:**
- [LangChain Academy](https://academy.langchain.com/) — free, official, maintained directly by the LangChain team; good spine for the whole week since it stays current with the fast-moving RAG ecosystem.
- Search "DataCamp Retrieval-Augmented Generation with LangChain" — a well-regarded, actively updated course (part of DataCamp's broader "AI Engineering with LangChain" track) if you prefer structured video content.

**Vector database (start local, free, zero setup):**
- [ChromaDB official docs](https://docs.trychroma.com/) — the standard choice for learning: runs locally, no account or cloud setup required, integrates directly with LangChain.
- Once comfortable, look at [Qdrant](https://qdrant.tech/documentation/) or [Pinecone](https://docs.pinecone.io/) docs for the cloud-scale, production version of the same concepts — free tiers are available on both.

**Embeddings specifically:**
- Search "sentence-transformers documentation" — a free, open-source embeddings library that doesn't require an API key, good for Monday/Tuesday experimentation before you touch a paid API.
- If using OpenAI's embeddings API later in the week: their `text-embedding-3-small` model is the cost-efficient current default worth knowing about specifically.

**Conceptual grounding before you write code:**
- Search "RAG vs fine-tuning when to use" — worth understanding why retrieval is usually the right first move for grounding an LLM in your own data, before ever reaching for fine-tuning.

---

## Week 20 — Flagship Project I

**No single resource this week** — this week is about integration, not new learning. Pull directly from your own repo:
- Your Phase B pipeline (BigQuery + dbt) for the batch layer
- Your Phase E pipeline (Kafka + Spark Structured Streaming) for the real-time layer
- Your Phase F work (Docker + Terraform) to package and provision it properly
- Your Week 19 RAG work for the AI-powered layer

**If you get stuck on integration specifically:**
- Search "end to end data pipeline project architecture example" for inspiration on how these pieces typically fit together — but resist copying a specific architecture wholesale; the point of this week is assembling *your own* pieces, not following someone else's tutorial project.

**For presenting it well (portfolio value):**
- A clear architecture diagram and a README explaining the "why" behind each design decision matters as much as the code itself — search "system design README template GitHub" for a structure to adapt.