# Methodology

This document describes how I approached building a reliable LLM-based system in a real expert domain.

Rather than starting from architecture or best practices, the approach was driven by:
- real user questions
- observed failure modes
- iterative refinement of retrieval, prompting, and evaluation

Two key constraints shaped this approach:
- it is not guaranteed that current LLM systems can reach the level of reliability required by a subject-matter expert
- SMEs cannot fully specify their needs upfront — they refine them through interaction with the system

As a result, the development process was explicitly experimental and iterative, in collaboration with an IFRS expert working in a large CAC 40 company.

---

## 1. Discovery

**Goal**  
Show feasibility and identify complexity at a minimum cost.

**Measure of success**  
The SME signs off on answers produced in a repeatable way for multiple out-of-sample questions.

**Mechanics**

### 1.1 Get to a good answer on one question
- Start with one real question and a correct answer provided by the SME
- Limit the corpus to the minimal set of standards containing the answer (IFRS 9, IFRIC 16)
- Iterate on prompts and grounding data with the SME until the answer is acceptable in:
  - content
  - structure
  - presentation
  - tone

This phase defines the scope and expectations of the assistant.

---

### 1.2 Generalize across question variants
- Test multiple formulations of the same question
- Identify whether failures come from:
  - retrieval
  - generation

Typical improvements include:
- better embeddings
- retrieval expansion and thresholding strategies
- structuring retrieved context (hierarchical vs flat)
- adding constraints in prompts
- splitting reasoning into multiple stages

---

### 1.3 Expand evaluation scope
- Add new questions from the SME
- Add more standards documents to test robustness to noise
- Evaluate generalization across topics
- Introduce overlapping and potentially conflicting sources

---

## 2. Delivery of V1 - TO DO

**Goal**  
The assistant is used by the SME in practice.

**Measure of success**  
The assistant is used as a first step to answer a meaningful share of real questions.

**Mechanics**

Upgrade the prototype into a usable system:

- UI for ingestion and question answering
- observability (including LLM calls)
- error handling on critical paths
- evaluation for non-regression when models change

Engineering hygiene:
- typing
- tests
- configuration management
- secrets handling
- logging

Packaging:
- Docker image
- documentation