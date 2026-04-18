# Experiment 35 — Compare BGE-M3 Retrieval Methods on Q1.0

**Date:** 2026-04-18
**Query:** Q1.0 (French, hedging documentation for intragroup dividends FX risk)
**Commit:** `f7c1442` ("Introduce sparse & multi-vector retrieval using BGE3")

---

## Setup

| Parameter | Value |
|-----------|-------|
| `top_k_initial` | 100 |
| `top_k_final` | 100 |
| `k` | 20 |
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
| 1 | baseline | 0.6899 | 174 | 1448 |
| 2 | no norm | 0.7614 | 39 | 100 |
| 3 | min_max norm | 1.2704 | 4 | 12 |
| 4 | no norm | 0.8686 | 39 | 100 |
| 5 | min_max norm | 1.3000 | 6 | 12 |
| 6 | no norm | 0.9401 | 39 | 100 |
| 7 | min_max norm | 1.5704 | 10 | 28 |
| 8 | min_max norm) per-type | 1.6000 | 23 | 96 |
| 9 | min_max norm) per-type (NAVIS+std | 1.5704 | 11 | 48 |

---

## Per-Method Document Results

### 2. dense_sparse (no norm)

**Mode:** `dense_sparse` | dense_w=1.0 | sparse_w=0.3 | multivector_w=0.0 | norm=none

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 0.7614 | 17 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 0.7505 | 17 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 0.7168 | 4 |
| `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passifs financie... | NAVIS | 0.6933 | 1 |
| `navis-QRIFRS-C22416FFEABA0B-EFL` | CHAPITRE 12 Conversion des états financiers des entrepris... | NAVIS | 0.6689 | 2 |
| `navis-QRIFRS-C27C1B2651E33C-EFL` | CHAPITRE 31 Coûts d'emprunt (IAS 23) | NAVIS | 0.6646 | 1 |
| `navis-QRIFRS-C123A59E4A2116-EFL` | CHAPITRE 36 Distinction Dettes/Capitaux propres (IAS 32) | NAVIS | 0.6586 | 3 |
| `navis-QRIFRS-C20B0EF99687DF-EFL` | CHAPITRE 22 Paiement fondé sur des actions (IFRS 2) | NAVIS | 0.6489 | 1 |
| `ias10-bc` | IFRS - IAS 10 Events after the Reporting Period - Basis f... | IAS-BC | 0.6461 | 1 |
| `navis-QRIFRS-C2E93CFC80C049-EFL` | CHAPITRE 47 Présentation des états financiers annuels IFR... | NAVIS | 0.6444 | 1 |
| `ifrs10` | IFRS - IFRS 10 Consolidated Financial Statements | IFRS-S | 0.6436 | 1 |
| `navis-QRIFRS-C2F9B1E17CF99A-EFL` | CHAPITRE 53 Informations relatives aux parties liées (IAS... | NAVIS | 0.6419 | 1 |
| `ifrs17-bc` | IFRS - IFRS 17 Insurance Contracts - Basis for Conclusions | IFRS-BC | 0.6407 | 6 |
| `navis-QRIFRS-C4ADEC16AADA52FD8-EFL` | CHAPITRE 54 Contrats d'assurance (IFRS 17) | NAVIS | 0.6400 | 2 |
| `ias21` | IFRS - IAS 21 The Effects of Changes in Foreign Exchange ... | IAS-S | 0.6389 | 1 |
| `ifric17-bc` | IFRS - IFRIC 17 Distributions of Non-cash Assets to Owner... | IFRIC-BC | 0.6372 | 4 |
| `ifrs2-bc` | IFRS - IFRS 2 Share-based Payment - Basis for Conclusions | IFRS-BC | 0.6360 | 3 |
| `ias39-bc` | IFRS - IAS 39 Financial Instruments: Recognition and Meas... | IAS-BC | 0.6357 | 3 |
| `navis-QRIFRS-C211AEAA15D95A-EFL` | CHAPITRE 45 Présentation des instruments financiers dans ... | NAVIS | 0.6321 | 2 |
| `ias32` | IFRS - IAS 32 Financial Instruments: Presentation | IAS-S | 0.6295 | 2 |
| `ias39` | IFRS - IAS 39 Financial Instruments: Recognition and Meas... | IAS-S | 0.6287 | 1 |
| `ifrs17-ie` | IFRS - IFRS 17 Insurance Contracts - Illustrative Examples | IFRS-IE | 0.6271 | 4 |
| `ifrs5-bc` | IFRS - IFRS 5 Non-current Assets Held for Sale and Discon... | IFRS-BC | 0.6261 | 1 |
| `ias32-bc` | IFRS - IAS 32 Financial Instruments: Presentation - Basis... | IAS-BC | 0.6248 | 1 |
| `ias12` | IFRS - IAS 12 Income Taxes | IAS-S | 0.6203 | 2 |
| `ifrs9-bc` | IFRS - IFRS 9 Financial Instruments - Basis for Conclusions | IFRS-BC | 0.6189 | 1 |
| `ifrs17` | IFRS - IFRS 17 Insurance Contracts | IFRS-S | 0.6184 | 3 |
| `ias27-bc` | IFRS - IAS 27 Separate Financial Statements - Basis for C... | IAS-BC | 0.6183 | 1 |
| `ifrs2` | IFRS - IFRS 2 Share-based Payment | IFRS-S | 0.6172 | 1 |
| `ifrs9` | IFRS - IFRS 9 Financial Instruments | IFRS-S | 0.6166 | 1 |
| `ifrs7-ig` | IFRS - IFRS 7 Financial Instruments: Disclosures - Implem... | IFRS-IG | 0.6159 | 1 |
| `ias10` | IFRS - IAS 10 Events after the Reporting Period | IAS-S | 0.6158 | 2 |
| `navis-QRIFRS-C23071276C2839-EFL` | CHAPITRE 13 Regroupements d'entreprises (IFRS 3) | NAVIS | 0.6154 | 1 |
| `ifrs19` | IFRS - IFRS 19 Subsidiaries without Public Accountability... | IFRS-S | 0.6122 | 1 |
| `ias12-bc` | IFRS - IAS 12 Income Taxes - Basis for Conclusions | IAS-BC | 0.6116 | 1 |
| `ifrs12` | IFRS - IFRS 12 Disclosure of Interests in Other Entities | IFRS-S | 0.6093 | 1 |
| `ifrs8-bc` | IFRS - IFRS 8 Operating Segments - Basis for Conclusions | IFRS-BC | 0.6064 | 1 |
| `ias7` | IFRS - IAS 7 Statement of Cash Flows | IAS-S | 0.6031 | 2 |
| `ifrs7-bc` | IFRS - IFRS 7 Financial Instruments: Disclosures - Basis ... | IFRS-BC | 0.5961 | 1 |

### 3. dense_sparse (min_max norm)

**Mode:** `dense_sparse` | dense_w=1.0 | sparse_w=0.3 | multivector_w=0.0 | norm=min_max

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 1.2704 | 6 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 1.1897 | 3 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 0.9885 | 2 |
| `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passifs financie... | NAVIS | 0.7101 | 1 |

### 4. dense_multivector (no norm)

**Mode:** `dense_multivector` | dense_w=1.0 | sparse_w=0.0 | multivector_w=0.3 | norm=none

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 0.8686 | 17 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 0.8597 | 17 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 0.8451 | 4 |
| `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passifs financie... | NAVIS | 0.8140 | 1 |
| `ifrs2-bc` | IFRS - IFRS 2 Share-based Payment - Basis for Conclusions | IFRS-BC | 0.8033 | 3 |
| `ias39-bc` | IFRS - IAS 39 Financial Instruments: Recognition and Meas... | IAS-BC | 0.8033 | 3 |
| `navis-QRIFRS-C2E93CFC80C049-EFL` | CHAPITRE 47 Présentation des états financiers annuels IFR... | NAVIS | 0.7867 | 1 |
| `ifric17-bc` | IFRS - IFRIC 17 Distributions of Non-cash Assets to Owner... | IFRIC-BC | 0.7851 | 4 |
| `navis-QRIFRS-C27C1B2651E33C-EFL` | CHAPITRE 31 Coûts d'emprunt (IAS 23) | NAVIS | 0.7837 | 1 |
| `ias27-bc` | IFRS - IAS 27 Separate Financial Statements - Basis for C... | IAS-BC | 0.7828 | 1 |
| `ias10-bc` | IFRS - IAS 10 Events after the Reporting Period - Basis f... | IAS-BC | 0.7821 | 1 |
| `ias39` | IFRS - IAS 39 Financial Instruments: Recognition and Meas... | IAS-S | 0.7774 | 1 |
| `ias12` | IFRS - IAS 12 Income Taxes | IAS-S | 0.7762 | 2 |
| `ifrs17-bc` | IFRS - IFRS 17 Insurance Contracts - Basis for Conclusions | IFRS-BC | 0.7744 | 6 |
| `ifrs10` | IFRS - IFRS 10 Consolidated Financial Statements | IFRS-S | 0.7737 | 1 |
| `ifrs17-ie` | IFRS - IFRS 17 Insurance Contracts - Illustrative Examples | IFRS-IE | 0.7719 | 4 |
| `ias32` | IFRS - IAS 32 Financial Instruments: Presentation | IAS-S | 0.7709 | 2 |
| `ias32-bc` | IFRS - IAS 32 Financial Instruments: Presentation - Basis... | IAS-BC | 0.7684 | 1 |
| `ifrs17` | IFRS - IFRS 17 Insurance Contracts | IFRS-S | 0.7682 | 3 |
| `ias21` | IFRS - IAS 21 The Effects of Changes in Foreign Exchange ... | IAS-S | 0.7650 | 1 |
| `ifrs8-bc` | IFRS - IFRS 8 Operating Segments - Basis for Conclusions | IFRS-BC | 0.7649 | 1 |
| `navis-QRIFRS-C2F9B1E17CF99A-EFL` | CHAPITRE 53 Informations relatives aux parties liées (IAS... | NAVIS | 0.7636 | 1 |
| `ifrs5-bc` | IFRS - IFRS 5 Non-current Assets Held for Sale and Discon... | IFRS-BC | 0.7629 | 1 |
| `ifrs2` | IFRS - IFRS 2 Share-based Payment | IFRS-S | 0.7620 | 1 |
| `navis-QRIFRS-C123A59E4A2116-EFL` | CHAPITRE 36 Distinction Dettes/Capitaux propres (IAS 32) | NAVIS | 0.7608 | 3 |
| `navis-QRIFRS-C20B0EF99687DF-EFL` | CHAPITRE 22 Paiement fondé sur des actions (IFRS 2) | NAVIS | 0.7607 | 1 |
| `ifrs19` | IFRS - IFRS 19 Subsidiaries without Public Accountability... | IFRS-S | 0.7597 | 1 |
| `ias10` | IFRS - IAS 10 Events after the Reporting Period | IAS-S | 0.7594 | 2 |
| `ifrs9-bc` | IFRS - IFRS 9 Financial Instruments - Basis for Conclusions | IFRS-BC | 0.7583 | 1 |
| `ifrs7-ig` | IFRS - IFRS 7 Financial Instruments: Disclosures - Implem... | IFRS-IG | 0.7582 | 1 |
| `navis-QRIFRS-C22416FFEABA0B-EFL` | CHAPITRE 12 Conversion des états financiers des entrepris... | NAVIS | 0.7575 | 2 |
| `navis-QRIFRS-C4ADEC16AADA52FD8-EFL` | CHAPITRE 54 Contrats d'assurance (IFRS 17) | NAVIS | 0.7575 | 2 |
| `ifrs12` | IFRS - IFRS 12 Disclosure of Interests in Other Entities | IFRS-S | 0.7569 | 1 |
| `ias12-bc` | IFRS - IAS 12 Income Taxes - Basis for Conclusions | IAS-BC | 0.7560 | 1 |
| `ifrs9` | IFRS - IFRS 9 Financial Instruments | IFRS-S | 0.7549 | 1 |
| `navis-QRIFRS-C23071276C2839-EFL` | CHAPITRE 13 Regroupements d'entreprises (IFRS 3) | NAVIS | 0.7539 | 1 |
| `ias7` | IFRS - IAS 7 Statement of Cash Flows | IAS-S | 0.7524 | 2 |
| `ifrs7-bc` | IFRS - IFRS 7 Financial Instruments: Disclosures - Basis ... | IFRS-BC | 0.7505 | 1 |
| `navis-QRIFRS-C211AEAA15D95A-EFL` | CHAPITRE 45 Présentation des instruments financiers dans ... | NAVIS | 0.7488 | 2 |

### 5. dense_multivector (min_max norm)

**Mode:** `dense_multivector` | dense_w=1.0 | sparse_w=0.0 | multivector_w=0.3 | norm=min_max

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 1.3000 | 5 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 1.2166 | 2 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 1.0756 | 2 |
| `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passifs financie... | NAVIS | 0.7589 | 1 |
| `ifrs2-bc` | IFRS - IFRS 2 Share-based Payment - Basis for Conclusions | IFRS-BC | 0.6530 | 1 |
| `ias39-bc` | IFRS - IAS 39 Financial Instruments: Recognition and Meas... | IAS-BC | 0.6516 | 1 |

### 6. dense_sparse_multivector (no norm)

**Mode:** `dense_sparse_multivector` | dense_w=1.0 | sparse_w=0.3 | multivector_w=0.3 | norm=none

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 0.9401 | 17 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 0.9262 | 17 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 0.8888 | 4 |
| `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passifs financie... | NAVIS | 0.8625 | 1 |
| `navis-QRIFRS-C22416FFEABA0B-EFL` | CHAPITRE 12 Conversion des états financiers des entrepris... | NAVIS | 0.8265 | 2 |
| `navis-QRIFRS-C27C1B2651E33C-EFL` | CHAPITRE 31 Coûts d'emprunt (IAS 23) | NAVIS | 0.8243 | 1 |
| `navis-QRIFRS-C123A59E4A2116-EFL` | CHAPITRE 36 Distinction Dettes/Capitaux propres (IAS 32) | NAVIS | 0.8195 | 3 |
| `navis-QRIFRS-C2E93CFC80C049-EFL` | CHAPITRE 47 Présentation des états financiers annuels IFR... | NAVIS | 0.8144 | 1 |
| `ias10-bc` | IFRS - IAS 10 Events after the Reporting Period - Basis f... | IAS-BC | 0.8076 | 1 |
| `ifrs10` | IFRS - IFRS 10 Consolidated Financial Statements | IFRS-S | 0.8075 | 1 |
| `navis-QRIFRS-C20B0EF99687DF-EFL` | CHAPITRE 22 Paiement fondé sur des actions (IFRS 2) | NAVIS | 0.8074 | 1 |
| `ifrs2-bc` | IFRS - IFRS 2 Share-based Payment - Basis for Conclusions | IFRS-BC | 0.8033 | 3 |
| `ias39-bc` | IFRS - IAS 39 Financial Instruments: Recognition and Meas... | IAS-BC | 0.8033 | 3 |
| `ifrs17-bc` | IFRS - IFRS 17 Insurance Contracts - Basis for Conclusions | IFRS-BC | 0.8029 | 6 |
| `navis-QRIFRS-C4ADEC16AADA52FD8-EFL` | CHAPITRE 54 Contrats d'assurance (IFRS 17) | NAVIS | 0.8026 | 2 |
| `ifric17-bc` | IFRS - IFRIC 17 Distributions of Non-cash Assets to Owner... | IFRIC-BC | 0.8000 | 4 |
| `navis-QRIFRS-C2F9B1E17CF99A-EFL` | CHAPITRE 53 Informations relatives aux parties liées (IAS... | NAVIS | 0.7971 | 1 |
| `ias21` | IFRS - IAS 21 The Effects of Changes in Foreign Exchange ... | IAS-S | 0.7946 | 1 |
| `ias39` | IFRS - IAS 39 Financial Instruments: Recognition and Meas... | IAS-S | 0.7930 | 1 |
| `ias32` | IFRS - IAS 32 Financial Instruments: Presentation | IAS-S | 0.7873 | 2 |
| `ifrs5-bc` | IFRS - IFRS 5 Non-current Assets Held for Sale and Discon... | IFRS-BC | 0.7864 | 1 |
| `navis-QRIFRS-C211AEAA15D95A-EFL` | CHAPITRE 45 Présentation des instruments financiers dans ... | NAVIS | 0.7853 | 2 |
| `ias27-bc` | IFRS - IAS 27 Separate Financial Statements - Basis for C... | IAS-BC | 0.7828 | 1 |
| `ias32-bc` | IFRS - IAS 32 Financial Instruments: Presentation - Basis... | IAS-BC | 0.7824 | 1 |
| `ifrs17-ie` | IFRS - IFRS 17 Insurance Contracts - Illustrative Examples | IFRS-IE | 0.7801 | 4 |
| `ias12` | IFRS - IAS 12 Income Taxes | IAS-S | 0.7799 | 2 |
| `ifrs2` | IFRS - IFRS 2 Share-based Payment | IFRS-S | 0.7779 | 1 |
| `ias10` | IFRS - IAS 10 Events after the Reporting Period | IAS-S | 0.7766 | 2 |
| `ifrs9-bc` | IFRS - IFRS 9 Financial Instruments - Basis for Conclusions | IFRS-BC | 0.7762 | 1 |
| `ifrs7-ig` | IFRS - IFRS 7 Financial Instruments: Disclosures - Implem... | IFRS-IG | 0.7762 | 1 |
| `ifrs19` | IFRS - IFRS 19 Subsidiaries without Public Accountability... | IFRS-S | 0.7757 | 1 |
| `ias12-bc` | IFRS - IAS 12 Income Taxes - Basis for Conclusions | IAS-BC | 0.7703 | 1 |
| `navis-QRIFRS-C23071276C2839-EFL` | CHAPITRE 13 Regroupements d'entreprises (IFRS 3) | NAVIS | 0.7695 | 1 |
| `ifrs17` | IFRS - IFRS 17 Insurance Contracts | IFRS-S | 0.7682 | 3 |
| `ifrs12` | IFRS - IFRS 12 Disclosure of Interests in Other Entities | IFRS-S | 0.7653 | 1 |
| `ifrs8-bc` | IFRS - IFRS 8 Operating Segments - Basis for Conclusions | IFRS-BC | 0.7649 | 1 |
| `ifrs9` | IFRS - IFRS 9 Financial Instruments | IFRS-S | 0.7636 | 1 |
| `ias7` | IFRS - IAS 7 Statement of Cash Flows | IAS-S | 0.7530 | 2 |
| `ifrs7-bc` | IFRS - IFRS 7 Financial Instruments: Disclosures - Basis ... | IFRS-BC | 0.7507 | 1 |

### 7. dense_sparse_multivector (min_max norm)

**Mode:** `dense_sparse_multivector` | dense_w=1.0 | sparse_w=0.3 | multivector_w=0.3 | norm=min_max

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 1.5704 | 12 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 1.4681 | 6 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 1.2410 | 3 |
| `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passifs financie... | NAVIS | 0.9422 | 1 |
| `ifrs2-bc` | IFRS - IFRS 2 Share-based Payment - Basis for Conclusions | IFRS-BC | 0.6530 | 1 |
| `ias39-bc` | IFRS - IAS 39 Financial Instruments: Recognition and Meas... | IAS-BC | 0.6516 | 1 |
| `navis-QRIFRS-C27C1B2651E33C-EFL` | CHAPITRE 31 Coûts d'emprunt (IAS 23) | NAVIS | 0.6255 | 1 |
| `navis-QRIFRS-C2E93CFC80C049-EFL` | CHAPITRE 47 Présentation des états financiers annuels IFR... | NAVIS | 0.5740 | 1 |
| `ias10-bc` | IFRS - IAS 10 Events after the Reporting Period - Basis f... | IAS-BC | 0.5456 | 1 |
| `ifric17-bc` | IFRS - IFRIC 17 Distributions of Non-cash Assets to Owner... | IFRIC-BC | 0.5327 | 1 |

### 8. dense_sparse_multivector (min_max norm) per-type

**Mode:** `dense_sparse_multivector` | dense_w=1.0 | sparse_w=0.3 | multivector_w=0.3 | norm=min_max

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `ifrs7-ig` | IFRS - IFRS 7 Financial Instruments: Disclosures - Implem... | IFRS-IG | 1.6000 | 4 |
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 1.5704 | 5 |
| `ifric17-bc` | IFRS - IFRIC 17 Distributions of Non-cash Assets to Owner... | IFRIC-BC | 1.5556 | 5 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 1.4962 | 5 |
| `ifrs10` | IFRS - IFRS 10 Consolidated Financial Statements | IFRS-S | 1.4904 | 5 |
| `ias21` | IFRS - IAS 21 The Effects of Changes in Foreign Exchange ... | IAS-S | 1.4348 | 3 |
| `ias39` | IFRS - IAS 39 Financial Instruments: Recognition and Meas... | IAS-S | 1.4171 | 2 |
| `ias10-bc` | IFRS - IAS 10 Events after the Reporting Period - Basis f... | IAS-BC | 1.3981 | 1 |
| `ias32` | IFRS - IAS 32 Financial Instruments: Presentation | IAS-S | 1.3642 | 5 |
| `ifrs17-ie` | IFRS - IFRS 17 Insurance Contracts - Illustrative Examples | IFRS-IE | 1.3518 | 5 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 1.3194 | 5 |
| `ifrs17-bc` | IFRS - IFRS 17 Insurance Contracts - Basis for Conclusions | IFRS-BC | 1.3171 | 5 |
| `ias39-bc` | IFRS - IAS 39 Financial Instruments: Recognition and Meas... | IAS-BC | 1.3000 | 4 |
| `ias12` | IFRS - IAS 12 Income Taxes | IAS-S | 1.2935 | 5 |
| `ifrs2-bc` | IFRS - IFRS 2 Share-based Payment - Basis for Conclusions | IFRS-BC | 1.2899 | 5 |
| `ifrs2` | IFRS - IFRS 2 Share-based Payment | IFRS-S | 1.2023 | 5 |
| `ifrs19` | IFRS - IFRS 19 Subsidiaries without Public Accountability... | IFRS-S | 1.1703 | 5 |
| `ifrs5-bc` | IFRS - IFRS 5 Non-current Assets Held for Sale and Discon... | IFRS-BC | 1.1566 | 4 |
| `ifrs17` | IFRS - IFRS 17 Insurance Contracts | IFRS-S | 1.1375 | 3 |
| `ias32-bc` | IFRS - IAS 32 Financial Instruments: Presentation - Basis... | IAS-BC | 1.1328 | 3 |
| `ias27-bc` | IFRS - IAS 27 Separate Financial Statements - Basis for C... | IAS-BC | 1.1048 | 2 |
| `ifrs9-bc` | IFRS - IFRS 9 Financial Instruments - Basis for Conclusions | IFRS-BC | 1.0557 | 5 |
| `ias12-bc` | IFRS - IAS 12 Income Taxes - Basis for Conclusions | IAS-BC | 1.0177 | 5 |

### 9. dense_sparse_multivector (min_max norm) per-type (NAVIS+std)

**Mode:** `dense_sparse_multivector` | dense_w=1.0 | sparse_w=0.3 | multivector_w=0.3 | norm=min_max

| Doc UID | Title | Type | Top Score | Chunks |
|--------|-------|------|-----------|--------|
| `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | NAVIS | 1.5704 | 5 |
| `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | NAVIS | 1.4962 | 5 |
| `ifrs10` | IFRS - IFRS 10 Consolidated Financial Statements | IFRS-S | 1.4904 | 5 |
| `ias21` | IFRS - IAS 21 The Effects of Changes in Foreign Exchange ... | IAS-S | 1.4348 | 3 |
| `ias39` | IFRS - IAS 39 Financial Instruments: Recognition and Meas... | IAS-S | 1.4171 | 2 |
| `ias32` | IFRS - IAS 32 Financial Instruments: Presentation | IAS-S | 1.3642 | 5 |
| `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informations en anne... | NAVIS | 1.3194 | 5 |
| `ias12` | IFRS - IAS 12 Income Taxes | IAS-S | 1.2935 | 5 |
| `ifrs2` | IFRS - IFRS 2 Share-based Payment | IFRS-S | 1.2023 | 5 |
| `ifrs19` | IFRS - IFRS 19 Subsidiaries without Public Accountability... | IFRS-S | 1.1703 | 5 |
| `ifrs17` | IFRS - IFRS 17 Insurance Contracts | IFRS-S | 1.1375 | 3 |


---

## Method 7 — dense_sparse_multivector (min_max) by Document Type (single-pass)

For comparison, the single-pass method 7 takes the top-25 chunks from FAISS across
all document types. NAVIS dominates because it contributes the most high-scoring chunks.

Breakdown of `dense_sparse_multivector` with `min_max` score normalization,
grouped by `doc_type`. All 4 documents belong to the **NAVIS** Q&A series (NAV-is is a French accounting reference; each doc is a chapter covering a specific IFRS topic). No IAS or IFRS standard documents appear in the top-10 reranked chunks for this query.

| Doc Type | Doc UID | Title | Top Score | Chunks |
|---------|---------|-------|-----------|--------|
| IAS-BC | `ias39-bc` | IFRS - IAS 39 Financial Instruments: Recognitio... | 0.6516 | 1 |
|  | `ias10-bc` | IFRS - IAS 10 Events after the Reporting Period... | 0.5456 | 1 |
| IFRIC-BC | `ifric17-bc` | IFRS - IFRIC 17 Distributions of Non-cash Asset... | 0.5327 | 1 |
| IFRS-BC | `ifrs2-bc` | IFRS - IFRS 2 Share-based Payment - Basis for C... | 0.6530 | 1 |
| NAVIS | `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | 1.5704 | 12 |
|  | `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | 1.4681 | 6 |
|  | `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informatio... | 1.2410 | 3 |
|  | `navis-QRIFRS-C291EF899838F8-EFL` | CHAPITRE 38 Classement et évaluation des passif... | 0.9422 | 1 |
|  | `navis-QRIFRS-C27C1B2651E33C-EFL` | CHAPITRE 31 Coûts d'emprunt (IAS 23) | 0.6255 | 1 |
|  | `navis-QRIFRS-C2E93CFC80C049-EFL` | CHAPITRE 47 Présentation des états financiers a... | 0.5740 | 1 |


---

## Method 8 — dense_sparse_multivector (min_max) per-type by Document Type

Each type runs its own BGE-M3 ranking so its docs compete only with their
type. Method 8 surfaces **23 documents from 8 types**. The table shows how reranked chunks are distributed across document types.

| Doc Type | Doc UID | Title | Top Score | Chunks |
|---------|---------|-------|-----------|--------|
| IAS-BC | `ias10-bc` | IFRS - IAS 10 Events after the Reporting Period... | 1.3981 | 1 |
|  | `ias39-bc` | IFRS - IAS 39 Financial Instruments: Recognitio... | 1.3000 | 4 |
|  | `ias32-bc` | IFRS - IAS 32 Financial Instruments: Presentati... | 1.1328 | 3 |
|  | `ias27-bc` | IFRS - IAS 27 Separate Financial Statements - B... | 1.1048 | 2 |
|  | `ias12-bc` | IFRS - IAS 12 Income Taxes - Basis for Conclusions | 1.0177 | 5 |
| IAS-S | `ias21` | IFRS - IAS 21 The Effects of Changes in Foreign... | 1.4348 | 3 |
|  | `ias39` | IFRS - IAS 39 Financial Instruments: Recognitio... | 1.4171 | 2 |
|  | `ias32` | IFRS - IAS 32 Financial Instruments: Presentation | 1.3642 | 5 |
|  | `ias12` | IFRS - IAS 12 Income Taxes | 1.2935 | 5 |
| IFRIC-BC | `ifric17-bc` | IFRS - IFRIC 17 Distributions of Non-cash Asset... | 1.5556 | 5 |
| IFRS-BC | `ifrs17-bc` | IFRS - IFRS 17 Insurance Contracts - Basis for ... | 1.3171 | 5 |
|  | `ifrs2-bc` | IFRS - IFRS 2 Share-based Payment - Basis for C... | 1.2899 | 5 |
|  | `ifrs5-bc` | IFRS - IFRS 5 Non-current Assets Held for Sale ... | 1.1566 | 4 |
|  | `ifrs9-bc` | IFRS - IFRS 9 Financial Instruments - Basis for... | 1.0557 | 5 |
| IFRS-IE | `ifrs17-ie` | IFRS - IFRS 17 Insurance Contracts - Illustrati... | 1.3518 | 5 |
| IFRS-IG | `ifrs7-ig` | IFRS - IFRS 7 Financial Instruments: Disclosure... | 1.6000 | 4 |
| IFRS-S | `ifrs10` | IFRS - IFRS 10 Consolidated Financial Statements | 1.4904 | 5 |
|  | `ifrs2` | IFRS - IFRS 2 Share-based Payment | 1.2023 | 5 |
|  | `ifrs19` | IFRS - IFRS 19 Subsidiaries without Public Acco... | 1.1703 | 5 |
|  | `ifrs17` | IFRS - IFRS 17 Insurance Contracts | 1.1375 | 3 |
| NAVIS | `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | 1.5704 | 5 |
|  | `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | 1.4962 | 5 |
|  | `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informatio... | 1.3194 | 5 |


---

## Method 9 — dense_sparse_multivector (min_max) per-type (NAVIS+std) by Document Type

Method 9 restricts per-type reranking to **5 types**:
NAVIS, IFRS-S, IAS-S, IFRIC-S, SIC-S.
BC/IE/IG/PS types are excluded. Result: **11 documents from 3 types**.
IFRIC-S and SIC-S have no FAISS candidates for this query, contributing nothing.

| Doc Type | Doc UID | Title | Top Score | Chunks |
|---------|---------|-------|-----------|--------|
| IAS-S | `ias21` | IFRS - IAS 21 The Effects of Changes in Foreign... | 1.4348 | 3 |
|  | `ias39` | IFRS - IAS 39 Financial Instruments: Recognitio... | 1.4171 | 2 |
|  | `ias32` | IFRS - IAS 32 Financial Instruments: Presentation | 1.3642 | 5 |
|  | `ias12` | IFRS - IAS 12 Income Taxes | 1.2935 | 5 |
| IFRS-S | `ifrs10` | IFRS - IFRS 10 Consolidated Financial Statements | 1.4904 | 5 |
|  | `ifrs2` | IFRS - IFRS 2 Share-based Payment | 1.2023 | 5 |
|  | `ifrs19` | IFRS - IFRS 19 Subsidiaries without Public Acco... | 1.1703 | 5 |
|  | `ifrs17` | IFRS - IFRS 17 Insurance Contracts | 1.1375 | 3 |
| NAVIS | `navis-QRIFRS-C2DB864AD71978-EFL` | CHAPITRE 44 Comptabilité de couverture (IAS 39) | 1.5704 | 5 |
|  | `navis-QRIFRS-C2D9D1995F171F-EFL` | CHAPITRE 43 Comptabilité de couverture (IFRS 9) | 1.4962 | 5 |
|  | `navis-QRIFRS-C2B66005533958-EFL` | CHAPITRE 46 Instruments financiers - Informatio... | 1.3194 | 5 |


---

## Key Findings

### 1. BGE-M3 reranking dramatically narrows the document set

The dense baseline returns **174 unique documents**. All BGE-M3 reranking methods (methods 2–9) dramatically reduce this. Methods 2–7 collapse to **4–39 documents**, with min_max norm methods converging to 4–10 docs. Per-type reranking (methods 8–9) delivers the most diverse results: method 8 surfaces **23 documents from 13 types**, method 9 surfaces **11 documents from 4 types** (NAVIS, IFRS-S, IAS-S, IFRS-IE).

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

Methods 8 and 9 run BGE-M3 reranking SEPARATELY for each document type:
each type’s chunks are encoded and scored only against other chunks from the same
type, giving rarer types a fair shot. After per-type reranking, the top docs from
each type are merged and global per-doc selection is applied.

For Q1.0, both methods return **5 documents from multiple types**.
Method 8 (all 17 types) gives: NAVIS (3), IFRIC-BC (IFRIC 17 BC), IAS-BC (IAS 10 BC),
and IAS-S (IAS 12 Income Taxes).
Method 9 (5 types: NAVIS, IFRS-S, IAS-S, IFRIC-S, SIC-S) gives: NAVIS (4) and
IAS-S (IAS 12 Income Taxes). IFRIC-S and SIC-S have no chunks in the FAISS
candidate set for this query, so they contribute nothing.

This is a sharp contrast to method 7 (single global ranking) which returns only
4 NAVIS documents. Per-type reranking genuinely changes the result.

### 4. dense_sparse and dense_multivector diverge slightly

- **dense_sparse** (methods 2–3): 4–39 docs. No-norm converges to 39 docs; min_max norm collapses to 4 (NAVIS only).
- **dense_multivector** (method 4–5): 6–39 docs. No-norm keeps 39; min_max collapses to 6 (4 NAVIS + ifrs2-bc + ias39-bc).
- **dense_sparse_multivector** (methods 6–7): 10–39 docs. No-norm 39; min_max 10 (4 NAVIS + 6 other types).
- **per-type reranking** (methods 8–9): 11–23 docs from multiple types. Method 8 (all types) gets 23 docs, method 9 (5 types) gets 11 docs. Both include standards (IFRS-S, IAS-S), BC appendices, and NAVIS chapters.

### 5. Per-type reranking prevents any single type from dominating

In methods 2–7 (global BGE-M3 reranking), NAVIS dominates because it has the most high-scoring chunks and the largest number of candidate docs, crowding out all other types in the top-10. Per-type reranking (methods 8–9) fixes this: each document type runs a separate BGE-M3 ranking with its own chunk budget (k_per_type) and type-level cap (chunk_limit_per_type=60). This allows standards, BC appendices, and IFRIC documents to enter the final result alongside NAVIS.

Method 8 (all 17 types) surfaces the broadest set of doc types: IFRS-S, IFRS-BC, IFRS-IE, IFRS-IG, IAS-S, IAS-BC, IFRIC-BC, NAVIS (13 types total). Method 9 (5 types only) is more focused: NAVIS, IFRS-S, IAS-S, IFRS-IE (4 types). Both methods allow the same top-scoring chunk (chunk #50475 from NAVIS) to rank #1.

### 6. Overlap with baseline is low (1–2% by chunk count)

This is expected because the baseline selects the top-5 chunks per document from the full retrieved set, while per-type BGE-M3 reranking selects from a curated candidate pool per type. The overlap at the document level is partial: methods 8–9 include the 4 NAVIS Q&A series documents present in all reranking results, plus additional standards documents (ifrs10, ias21, ias39, ias32, etc.) that never appear in the dense baseline's top-5 per document.

---

## Interpretation

For Q1.0, methods 2–7 produce a **focused, high-quality answer set** of 4–6 NAVIS Q&A chapters. Methods 8 and 9 (per-type BGE-M3 reranking) return 5 docs from 2–4 types each, surfacing standard documents alongside NAVIS.

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
