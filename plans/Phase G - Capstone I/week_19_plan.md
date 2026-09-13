# Week 19 Plan: Vector DBs, Embeddings & RAG

## Overview

- **Phase:** G — Capstone I
- **Focus:** AI-augmented data systems
- **Goal:** Understand embeddings and vector search well enough to build a working RAG pipeline — and understand it as a data engineering problem (chunking, storage, retrieval quality), not just an AI demo
- **Anki Target:** 25 cards
- **Why now, not earlier:** This sits on top of Docker (Phase F) and everything else you've built — you now have the infra discipline to build this responsibly instead of as an unsecured, uncontainerized script.

---

## Monday–Friday

### Daily Objectives

- **Monday:** What embeddings actually are (text → vectors capturing meaning), cosine similarity, experimenting with `sentence-transformers` locally → Deliverable: 5 examples showing semantically similar text producing similar embeddings
- **Tuesday:** Vector databases — why you can't just use a regular SQL index for similarity search, ChromaDB setup and basic operations → Deliverable: 1 ChromaDB collection storing embeddings, with 5 similarity searches run against it
- **Wednesday:** Document chunking strategies (fixed-size vs. semantic chunking) and why chunking quality directly determines retrieval quality → Deliverable: 2 chunking strategies compared on the same document, with retrieval quality noted for each
- **Thursday:** Building a RAG pipeline with LangChain — retrieval + augmented prompt + LLM generation, end to end → Deliverable: 1 working RAG pipeline answering questions about a document set you provide
- **Friday:** RAG evaluation basics — is the retrieved context actually relevant, is the answer actually grounded in it (not hallucinated) → Deliverable: 5 test questions with retrieval relevance and answer groundedness manually assessed

### Anki Targets

- Monday: 5 cards tagged `ai::embeddings`
- Tuesday: 5 cards tagged `ai::vector-db`
- Wednesday: 5 cards tagged `ai::chunking`
- Thursday: 5 cards tagged `ai::rag-pipeline`
- Friday: 5 cards tagged `ai::rag-evaluation`

---

## Saturday

### Rest
- No study, no Anki

---

## Sunday

### Review + Map Next Week
- Review all Anki cards from the week
- Explain out loud why chunking strategy affects retrieval quality, with a concrete example
- Draft next week's objectives (Flagship Project I)

---

## Week 19 Success Metrics
- [ ] 25 Anki cards created
- [ ] 1 working RAG pipeline built end-to-end
- [ ] 2 chunking strategies compared with documented results
- [ ] 5 test questions manually evaluated for retrieval relevance and groundedness
- [ ] Can explain, unprompted, why RAG is a data engineering problem as much as an AI one
- [ ] Week 20 plan drafted