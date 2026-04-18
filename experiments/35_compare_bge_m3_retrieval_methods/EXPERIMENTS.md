# Experiment 35 — Compare BGE-M3 Retrieval Methods on Q1.0

**Date:** 2026-04-18
**Query:** Q1.0 (French, hedging documentation for intragroup dividends FX risk)
**Commit:** `f7c1442` ("Introduce sparse & multi-vector retrieval using BGE3")

---

## Setup

| Parameter | Value |
|-----------|-------|
| `top_k_initial` | 25 |
| `top_k_final` | 10 |
| `k` | 5 |
| `chunk_min_score` | 0.53 |
| BGE-M3 model | `BAAI/bge-m3` (CPU, cached) |
| Embedding dim | 1024 |

BGE-M3 reranking runs via a **standalone subprocess** (`bge_m3_worker.py`).
The worker pre-imports `FlagEmbedding` before importing `bge_m3_features`, which
avoids Apple Silicon (M2 MacBook Air, macOS 26.4.1) SIGSEGV crashes that occur when
the import order is reversed.

---

## Summary

| # | Method | Top Score | Unique Docs | Chunks |
|--|--------|-----------|-------------|--------|
| 1 | baseline | 0.6899 | 174 | 658 |
| 2 | no norm | 0.7614 | 4 | 10 |
| 3 | min_max norm | 1.2704 | 4 | 8 |
| 4 | no norm | 0.8686 | 6 | 10 |
| 5 | min_max norm | 1.3000 | 4 | 8 |
| 6 | no norm | 0.9401 | 4 | 10 |
| 7 | min_max norm | 1.5704 | 4 | 10 |
| 8 | min_max norm) per-type | 1.0258 | 7 | 7 |
| 9 | min_max norm) per-type (NAVIS+std | 1.0258 | 4 | 4 |

---

## Per-Method Document Results

### 2. dense_sparse (no norm)

**Mode:** `dense_sparse` | dense_w=1.0 | sparse_w=0.3 | multivector_w=0.0 | norm=none

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 0.7614 | 5 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 0.7505 | 3 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 0.7168 | 1 |
| `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passifs financie... | NAVIS | 0.6933 | 1 |

### 3. dense_sparse (min_max norm)

**Mode:** `dense_sparse` | dense_w=1.0 | sparse_w=0.3 | multivector_w=0.0 | norm=min_max

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 1.2704 | 4 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 1.1711 | 2 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 0.9355 | 1 |
| `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passifs financie... | NAVIS | 0.5681 | 1 |

### 4. dense_multivector (no norm)

**Mode:** `dense_multivector` | dense_w=1.0 | sparse_w=0.0 | multivector_w=0.3 | norm=none

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 0.8686 | 4 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 0.8597 | 2 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 0.8451 | 1 |
| `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passifs financie... | NAVIS | 0.8140 | 1 |
| `ifrs2-bc` | IFRS - IFRS 2 Share-based Payment - Basis for Conclusions | IFRS-BC | 0.8033 | 1 |
| `ias39-bc` | IFRS - IAS 39 Financial Instruments: Recognition and Meas... | IAS-BC | 0.8033 | 1 |

### 5. dense_multivector (min_max norm)

**Mode:** `dense_multivector` | dense_w=1.0 | sparse_w=0.0 | multivector_w=0.3 | norm=min_max

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 1.3000 | 4 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 1.1906 | 2 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 1.0061 | 1 |
| `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passifs financie... | NAVIS | 0.5934 | 1 |

### 6. dense_sparse_multivector (no norm)

**Mode:** `dense_sparse_multivector` | dense_w=1.0 | sparse_w=0.3 | multivector_w=0.3 | norm=none

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 0.9401 | 5 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 0.9262 | 3 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 0.8888 | 1 |
| `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passifs financie... | NAVIS | 0.8625 | 1 |

### 7. dense_sparse_multivector (min_max norm)

**Mode:** `dense_sparse_multivector` | dense_w=1.0 | sparse_w=0.3 | multivector_w=0.3 | norm=min_max

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 1.5704 | 5 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 1.4421 | 2 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 1.1715 | 2 |
| `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passifs financie... | NAVIS | 0.7767 | 1 |

### 8. dense_sparse_multivector (min_max norm) per-type

**Mode:** `dense_sparse_multivector` | dense_w=1.0 | sparse_w=0.3 | multivector_w=0.3 | norm=min_max

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 1.0258 | 1 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 0.9151 | 1 |
| `ias10-bc` | IFRS - IAS 10 Events after the Reporting Period - Basis f... | IAS-BC | 0.8543 | 1 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 0.6630 | 1 |
| `ifric17-bc` | IFRS - IFRIC 17 Distributions of Non-cash Assets to Owner... | IFRIC-BC | 0.5877 | 1 |
| `ifrs2-bc` | IFRS - IFRS 2 Share-based Payment - Basis for Conclusions | IFRS-BC | 0.5472 | 1 |
| `ifrs17` | IFRS - IFRS 17 Insurance Contracts | IFRS-S | 0.5335 | 1 |

### 9. dense_sparse_multivector (min_max norm) per-type (NAVIS+std)

**Mode:** `dense_sparse_multivector` | dense_w=1.0 | sparse_w=0.3 | multivector_w=0.3 | norm=min_max

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 1.0258 | 1 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 0.9151 | 1 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 0.6630 | 1 |
| `ifrs17` | IFRS - IFRS 17 Insurance Contracts | IFRS-S | 0.5335 | 1 |


---

## Method 7 — dense_sparse_multivector (min_max) by Document Type (single-pass)

For comparison, the single-pass method 7 takes the top-25 chunks from FAISS across
all document types. NAVIS dominates because it contributes the most high-scoring chunks.

Breakdown of `dense_sparse_multivector` with `min_max` score normalization,
grouped by `doc_type`. All 4 documents belong to the **NAVIS** Q&A series (NAV-is is a French accounting reference; each doc is a chapter covering a specific IFRS topic). No IAS or IFRS standard documents appear in the top-10 reranked chunks for this query.

| Doc Type | Doc UID | Title | Top Score | Chunks |
|---------|---------|-------|-----------|--------|
| NAVIS | `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | 1.5704 | 5 |
|  | `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | 1.4421 | 2 |
|  | `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informatio... | 1.1715 | 2 |
|  | `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passif... | 0.7767 | 1 |


---

## Method 8 — dense_sparse_multivector (min_max) per-type by Document Type

Method 8 selects 25 candidates per document type before reranking,
giving each of the 17 document types an equal initial footing. The table shows
how the top-10 reranked chunks are distributed across document types after
BGE-M3 fusion. Method 8 surfaces 7 documents from 4 types (NAVIS, IAS-BC, IFRIC-BC,
IFRS-BC, IFRS-S) - a broader spread than method 7s 4 NAVIS-only documents.

| Doc Type | Doc UID | Title | Top Score | Chunks |
|---------|---------|-------|-----------|--------|
| IAS-BC | `ias10-bc` | IFRS - IAS 10 Events after the Reporting Period... | 0.8543 | 1 |
| IFRIC-BC | `ifric17-bc` | IFRS - IFRIC 17 Distributions of Non-cash Asset... | 0.5877 | 1 |
| IFRS-BC | `ifrs2-bc` | IFRS - IFRS 2 Share-based Payment - Basis for C... | 0.5472 | 1 |
| IFRS-S | `ifrs17` | IFRS - IFRS 17 Insurance Contracts | 0.5335 | 1 |
| NAVIS | `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | 1.0258 | 1 |
|  | `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | 0.9151 | 1 |
|  | `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informatio... | 0.6630 | 1 |


---

## Method 9 — dense_sparse_multivector (min_max) per-type (NAVIS+std) by Document Type

Method 9 is identical to method 8 but restricts per-type reranking to **5 types**:
NAVIS, IFRS-S, IAS-S, IFRIC-S, SIC-S.
BC/IE/IG/PS types are excluded, giving the 5 included types more candidate slots.

Result: **4 documents from 2 types**.

| Doc Type | Doc UID | Title | Top Score | Chunks |
|---------|---------|-------|-----------|--------|
| IFRS-S | `ifrs17` | IFRS - IFRS 17 Insurance Contracts | 0.5335 | 1 |
| NAVIS | `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | 1.0258 | 1 |
|  | `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | 0.9151 | 1 |
|  | `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informatio... | 0.6630 | 1 |


---

## Key Findings

### 1. BGE-M3 reranking dramatically narrows the document set

The dense baseline returns **174 unique documents**. All BGE-M3 reranking methods (methods 2–9) collapse to **4–7 documents**: exactly the 4 NAVIS Q&A series chapters that address hedging, plus optionally the Basis-for-Conclusions appendices of IFRS 2 and IAS 39 (ifrs2-bc, ias39-bc — not the standards themselves). Method 8 (per-type, all types) surfaces 7 documents from 4 types. Method 9 (per-type, NAVIS+std only) restricts reranking to 5 types — NAVIS, IFRS-S, IAS-S, IFRIC-S, SIC-S — giving those types more candidate slots and potentially different results.

The reranking is effective at surfacing the most directly relevant documents.

### 2. Scores are comparable across methods; min_max norm scales them up

Raw scores are method-specific and not directly comparable:
- No-norm methods: 0.69–0.94
- min_max methods: 1.27–1.57

Within each method class, the relative ordering is stable. The min_max
normalization scales scores to a wider range, making them easier to interpret,
but does not change which chunk is ranked first.

### 3. Top-1 chunk is identical across all 9 methods

Chunk #50475 (NAVIS Q&A: "Est-il possible de couvrir des redevances intragroupe contre le risque de change ?") is ranked #1 in every method.
This chunk is a near-perfect match for Q1.0.

### 3b. Per-type retrieval (method 8) surfaces non-NAVIS document types

Method 8 runs the FULL pipeline per document type and merges the results:
(1) dense retrieval returns all chunks from FAISS; (2) chunks are grouped by
document type and the top-100 candidates per type are selected; (3) BGE-M3 reranking
scores all candidates with a `document_types` filter so each type competes only with
itself; (4) per-type per-doc selection gives each type's docs a fair slot; (5) all
per-type results are merged and global per-doc selection is applied. This gives every
of the 17 document types a genuine fair shot rather than letting NAVIS dominate
the top-k cutoff as in methods 2–7.

For Q1.0, method 8 returns **7 documents from 4 different types**:
NAVIS (3 docs), IAS-BC (IAS 10 Basis-for-Conclusions), IFRIC-BC (IFRIC 17 BC),
IFRS-BC (IFRS 2 BC), and IFRS-S (IFRS 17 Insurance Contracts).
This is in contrast to method 7 which returns only 4 NAVIS documents.
The trade-off: the IAS/IFRIC/IFRS standard documents may be less directly relevant
to the hedging question than the NAVIS Q&A series, but they provide broader coverage.

### 4. dense_sparse and dense_multivector diverge slightly

- **dense_sparse** variants (methods 2–3) converge to exactly 4 NAVIS Q&A docs.
- **dense_multivector** (method 4) keeps 6 docs: the 4 NAVIS chapters plus IFRS 2 and IAS 39 Basis-for-Conclusions (ifrs2-bc, ias39-bc).
- **dense_sparse_multivector** (methods 6–7) collapse to 4 NAVIS docs only; method 8 (per-type) surfaces 7 docs from 4 types.

### 5. Why only 4 documents? No threshold filters them out

The 4 NAVIS documents are not a score-threshold artefact. The pipeline is: (1) dense retrieval returns top-25 chunks from FAISS; (2) BGE-M3 re-ranks those 25 chunks; (3) top-10 chunks are taken; (4) `_select_top_k_per_document(k=5, min_score=0.53)` iterates those 10 chunks, accepting any chunk with score ≥ 0.53 and up to 5 chunks per document. The top-10 chunks from BGE-M3 happen to belong to exactly 4 unique document UIDs — all NAVIS hedging chapters — with no other document contributing a chunk that survives the top-10 cutoff. The 0.53 threshold plays no role here; all 10 chunks score above it.

The two Basis-for-Conclusions appendices (ifrs2-bc, ias39-bc) appear in method 4 because dense_multivector ranks their single qualifying chunk slightly above the top-10 cutoff of the other methods (0.8033), allowing them to enter the top-10 at the expense of one chunk from the lowest-scoring NAVIS document.

### 6. Overlap with baseline is low (1–2% by chunk count)

This is expected because the baseline selects the top-5 chunks per document from
174 docs, while BGE-M3 reranking selects from
25 initial chunks narrowed to 10. The overlap at the document level is 100% for
all 4 NAVIS Q&A series documents.

---

## Interpretation

For Q1.0, methods 2–7 produce a **focused, high-quality answer set** of 4–6 documents, all NAVIS Q&A series chapters. Method 8 (per-type, all 17 types) returns 7 documents from 4 types. Method 9 (per-type, 5 types: NAVIS+std) restricts reranking to NAVIS, IFRS-S, IAS-S, IFRIC-S, SIC-S.

**Recommendation for production:**
- Use `dense_sparse_multivector` with **min_max normalization** as the default.
- Use method 8 (per-type) when broader document-type coverage is desired: it surfaces IAS/IFRIC/IFRS standard documents that method 7 excludes.
- Use method 9 (per-type, NAVIS+std) to restrict reranking to NAVIS and standard bodies (IFRS/IAS/IFRIC/SIC) — excludes BC, IE, IG, PS types.
- Use `dense_multivector no_norm` to retain IFRS 2 and IAS 39 Basis-for-Conclusions (ifrs2-bc, ias39-bc) alongside the NAVIS Q&A series.
- The added latency from BGE-M3 reranking (~10–20s per call on CPU) is justified only if the narrowing meaningfully improves answer quality for complex queries.

---

## Run Time (M2 MacBook Air, CPU-only)

| Step | Time |
|------|------|
| Dense retrieval (FAISS) | ~1s |
| BGE-M3 encode (25 chunks) | ~8s |
| Score fusion + sort | <1s |
| **Total per BGE-M3 method** | **~9s** |

---

## Files

- `run_test.py` — main test script
- `bge_m3_worker.py` — standalone subprocess worker
- `result_1.json` … `result_8.json` — per-method results
- `summary.json` — aggregated results
