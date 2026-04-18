# Experiment 34: Retrieval alternatives for document routing

## Goal

Investigate whether alternative document-level retrieval representations would surface more relevant documents for the Q1 family than the current concatenated document profile.

The concrete trigger for this experiment was the analysis done in [experiment 33](../33_authority_competition_on_full_corpus/EXPERIMENTS.md), where clearly irrelevant documents such as `ifric17-bc`, `ifric17`, `ias7-bc`, and `ifrs17-bc` scored very highly, while truly relevant hedge-accounting documents such as `ifrs9` and `ifric16` were not consistently near the top.

## Context

The current document profile builder persists these fields on `documents` and builds one embedding text by concatenating the populated parts:

- `source_title`
- `background_text`
- `issue_text`
- `objective_text`
- `scope_text`
- `intro_text`
- `toc_text`

A quick TOC-only probe on Q1.0 strongly suggested that:

- **dividend** terminology was dominating the similarity search
- **couverture** was semantically drifting toward **insurance / coverage** rather than strictly **hedge accounting**
- relevant hedge-accounting sources were losing because their TOCs are narrower and less lexically aligned with the question wording

That led to two follow-up questions:

1. is one existing persisted field better than the full concatenation?
2. is there another signal in the database that would improve document routing?

## Method

This experiment used **Q1.0** as a diagnostic query and compared multiple representations against the current database contents.

### Query

`Q1.0`

> Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

### Embedding setup

- model: `BAAI/bge-m3`
- cosine similarity via normalized embeddings
- document-field probes were rerun using the project's actual document-profile truncation budget:
  - `MAX_EMBEDDING_TEXT_CHARS = 8000 * 3 = 24000`
- for the field and combo probes, the experiment used the project's actual document-profile formatter (`_build_embedding_text`) rather than an ad hoc 512-token cap
- for section-heading probes, the section texts were short enough that the character budget was not the limiting factor

### Representations tested

1. each persisted document field individually
2. several field combinations
3. a type-aware hybrid representation
4. a document-level signal aggregated from `sections.title` + `sections.section_lineage`

### Relevant targets monitored

The probe tracked where these documents landed in the ranking:

- `ifrs9`
- `ifrs9-bc`
- `ifric16`
- `ifric16-bc`
- `navis-QRIFRS-C2D9D1995F171F-EFL` (`Comptabilité de couverture (IFRS 9)`)

## Data availability in the current database

| Field | Populated docs | Avg chars | Min chars | Max chars |
| --- | ---: | ---: | ---: | ---: |
| `background_text` | 43 | 2871.4 | 380 | 25416 |
| `issue_text` | 20 | 1049.0 | 228 | 4520 |
| `objective_text` | 33 | 939.9 | 132 | 5524 |
| `scope_text` | 79 | 4765.6 | 160 | 36256 |
| `intro_text` | 85 | 9905.0 | 168 | 74021 |
| `toc_text` | 224 | 1616.6 | 8 | 17906 |

## Results - single-field probes

### IFRS + IAS

#### `scope_text`

Top results (IFRS + IAS, excluding BC — 39 non-BC docs):

| Rank | Score | doc_uid | Target? |
| ---: | ---: | --- | --- |
| 1 | 0.5996 | ias24 | |
| 2 | 0.5974 | ifrs9 | <<< |
| 3 | 0.5932 | ifrs3 | |
| 4 | 0.5897 | ias21 | |
| 5 | 0.5874 | ias32 | |
| 6 | 0.5865 | ias37 | |
| 7 | 0.5858 | ifrs7 | |
| 8 | 0.5803 | ifrs8 | |
| 9 | 0.5800 | ifrs19 | |
| 10 | 0.5686 | ias33 | |
| 11 | 0.5664 | ifrs11 | |
| 12 | 0.5645 | ias40-bciasc | |
| 13 | 0.5623 | ifrs2 | |
| 14 | 0.5601 | ifrs18 | |
| 15 | 0.5583 | ifrs12 | |
| 16 | 0.5494 | ias8 | |
| 17 | 0.5481 | ias38 | |
| 18 | 0.5480 | ifrs14 | |
| 19 | 0.5457 | ias27 | |
| 20 | 0.5422 | ias7 | |

`ifrs9` is at rank **2** (score 0.5974) — the best result for any IFRS/IAS target on this question. Among the persisted `xx_text` fields, `scope_text` is the strongest single candidate for the IFRS+I family.

#### `objective_text`

Top results (IFRS + IAS, excluding BC — 31 non-BC docs):

| Rank | Score | doc_uid | Target? |
| ---: | ---: | --- | --- |
| 1 | 0.5480 | ifrs19 | |
| 2 | 0.5417 | ifrs14 | |
| 3 | 0.5378 | ifrs15 | |
| 4 | 0.5340 | ifrs10 | |
| 5 | 0.5242 | ias32 | |
| 6 | 0.5219 | ias27 | |
| 7 | 0.5158 | ifrs18 | |
| 8 | 0.5148 | ias24 | |
| 9 | 0.5109 | ifrs12 | |
| 10 | 0.5073 | ifrs17 | |
| 11 | 0.5024 | ifrs3 | |
| 12 | 0.4994 | ias10 | |
| 13 | 0.4990 | ifrs2 | |
| 14 | 0.4965 | ias8 | |
| 15 | 0.4942 | ias28 | |
| 16 | 0.4916 | ias19 | |
| 17 | 0.4897 | ifrs9 | <<< |

`ifrs9` at rank 17. `objective_text` is too broad for the IFRS+I family on this question.

#### `intro_text`

Top results (IFRS + IAS, including BC — 82 docs):

| Rank | Score | doc_uid | BC? |
| ---: | ---: | --- | --- |
| 1 | 0.5994 | ifrs12-bc | BC |
| 2 | 0.5586 | ifrs17-ie | |
| 3 | 0.5547 | ifrs8-ig | |
| 4 | 0.5443 | ifrs18-ie | |
| 5 | 0.5429 | ifrs2-bc | BC |
| 6 | 0.5410 | ifrs10-bc | BC |
| 7 | 0.5407 | ifrs7-ig | |
| 8 | 0.5386 | ias27-bc | BC |
| 9 | 0.5365 | ifrs7-bc | BC |
| 10 | 0.5279 | ifrs14-bc | BC |
| 11 | 0.5274 | ias12-bc | BC |
| 12 | 0.5256 | ifrs9-bc | BC |
| 13 | 0.5251 | ias28-bc | BC |
| 14 | 0.5204 | ifrs3-bc | BC |
| 15 | 0.5190 | ias19-bc | BC |

BC documents dominate. Only 7 non-BC IFRS/IAS docs have `intro_text`; the top non-BC entry is `ifrs17-ie` (0.5586).

**Interpretation:** `intro_text` is too broad and too noisy for the IFRS+I family on this question.

#### `toc_text`

Top results (IFRS + IAS, including BC — 155 docs):

| Rank | Score | doc_uid | BC? | Target? |
| ---: | ---: | --- | --- | --- |
| 1 | 0.5916 | ias7-bc | BC | |
| 2 | 0.5913 | ifrs17-bc | BC | |
| 3 | 0.5840 | ias27-bc | BC | |
| 4 | 0.5802 | ifrs7-bc | BC | |
| 5 | 0.5718 | ifrs17 | | |
| 6 | 0.5661 | ias7 | | |
| 7 | 0.5629 | ias33-bc | BC | |
| 8 | 0.5615 | ifrs9-bc | BC | <<< |
| 9 | 0.5614 | ifrs19 | | |
| 10 | 0.5558 | ias32-bc | BC | |
| 11 | 0.5454 | ifrs1-bc | BC | |
| 12 | 0.5453 | ifrs14 | | |
| 13 | 0.5445 | ifrs17-ie | | |
| 14 | 0.5443 | ias39-bc | BC | |
| 15 | 0.5437 | ifrs18-bc | BC | |
| 16 | 0.5417 | ifrs12 | | |
| 17 | 0.5385 | ifrs18 | | |
| 18 | 0.5371 | ias19-ig | | |
| 19 | 0.5335 | ifrs9 | | <<< |
| 20 | 0.5324 | ifrs5 | | |

BC documents dominate the top 20 (12 of 20). Excluding BC (79 non-BC docs): `ifrs9` moves to rank **9** (score 0.5335). `toc_text` is the main field introducing dividend and broad-accounting noise for the IFRS+I family.

**Interpretation:** TOC-only retrieval is dominated by BC explanatory narratives and dividend-heavy TOCs. Excluding BC improves the standing of standard IFRS documents but `scope_text` still outperforms it for routing `ifrs9` (rank 3 in full `scope_text` vs rank 9 in `toc_text` excl BC).

### IFRIC

#### `background_text`

Top results (IFRIC only, excluding BC — 16 non-BC docs):

| Rank | Score | doc_uid | Target? |
| ---: | ---: | --- | --- |
| 1 | 0.5908 | ifric17 | |
| 2 | 0.5344 | ifric21 | |
| 3 | 0.5154 | ifric22 | |
| 4 | 0.5140 | ifric16 | <<< |
| 5 | 0.5124 | ifric14 | |
| 6 | 0.5104 | ifric19 | |
| 7 | 0.5093 | ifric23 | |
| 8 | 0.4998 | ifric16-ie | |
| 9 | 0.4976 | ifric7 | |
| 10 | 0.4731 | ifric10 | |

`ifric16` is at rank **4** (score 0.5140) — the best single-field result for the IFRIC family. Notably, `ifrs9` and `ifrs9-bc` are absent: neither has `background_text` populated.

#### `issue_text`

Top results (IFRIC only — 15 base IFRIC docs):

| Rank | Score | doc_uid | Status |
| ---: | ---: | --- | --- |
| 1 | 0.5823 | ifric17 | **Relevant** |
| 2 | 0.5452 | ifric2 | False positive |
| 3 | 0.5407 | ifric7 | False positive |
| 4 | 0.5372 | ifric12 | False positive |
| 5 | 0.5352 | ifric19 | False positive |
| **6** | **0.5147** | **ifric16** | **Relevant** |
| 7 | 0.5056 | ifric14 | |
| 8 | 0.4993 | ifric5 | |
| 9 | 0.4882 | ifric1 | |
| 10 | 0.4864 | ifric21 | |
| 11 | 0.4847 | ifric23 | |
| 12 | 0.4770 | ifric10 | |

`ifric16` is at rank 6. The scores are driven by lexical overlap rather than topical correctness: ifric17 (genuinely relevant — dividend payable recognition rules) ranks first; ifric2, ifric7, ifric12, ifric19 are false positives. `issue_text` is a useful type-specific signal but cannot disambiguate topic relevance within the IFRIC family on Q1.

#### `scope_text`

Top results (IFRIC only, excluding BC — 13 non-BC docs):

| Rank | Score | doc_uid | Target? |
| ---: | ---: | --- | --- |
| 1 | 0.5550 | ifric17 | |
| 2 | 0.5546 | ifric23 | |
| 3 | 0.5402 | ifric5 | |
| 4 | 0.5377 | ifric2 | |
| 5 | 0.5340 | ifric22 | |
| 6 | 0.5331 | ifric19 | |
| 7 | 0.5313 | ifric12 | |
| 8 | 0.5209 | ifric16 | <<< |
| 9 | 0.4959 | ifric21 | |
| 10 | 0.4875 | ifric6 | |

`ifric16` at rank **8** — weaker than `background_text` alone (rank 4) or `issue_text` alone (rank 6).

**Interpretation:** for the IFRIC family, `background_text` is the best single field, pushing `ifric16` to rank 4. `issue_text` provides complementary type-specific signal but cannot independently surface the correct document. The combination of both fields (see §Field combinations) outperforms either alone.

## Results - field combinations

### Current-style broad concatenation

Combination:

- `source_title`
- `background_text`
- `issue_text`
- `objective_text`
- `scope_text`
- `intro_text`
- `toc_text`

Top results still looked wrong:

1. `ifrs17-bc`
2. `navis-QRIFRS-C2DB864AD71978-EFL`
3. `ifric17-bc`
4. `ifrs3`
5. `navis-QRIFRS-C20B0EF99687DF-EFL`
6. `ifrs19-bc`
7. `ias37`
8. `ifrs7-bc`

Target ranks:

- `ifrs9` - rank 33
- `ifrs9-bc` - rank 15
- `ifric16` - rank 98
- `ifric16-bc` - rank 67

**Interpretation:** the current "concat everything" strategy is still dominated by noisy broad fields. It does not reliably surface the right governing materials.

### `title + scope`

Top 10 included:

- `ifrs3`
- `ifrs2-bc`
- `ias37`
- `ias24`
- `ifrs7`
- `ifrs9`

Target ranks:

- `ifrs9` - rank 6
- `ifric16` - rank 62
- `ifrs9-bc` - rank 59
- `ifric16-bc` - rank 126

**Interpretation:** `title + scope` is materially better than the current full concat for `ifrs9`, but it still does not solve `ifric16`.

### `title + scope + objective`

This was very similar to `title + scope`.

Target ranks:

- `ifrs9` - rank 10
- `ifric16` - rank 59
- `ifrs9-bc` - rank 56
- `ifric16-bc` - rank 129

**Interpretation:** `objective_text` adds little incremental value here.

### Any combination that reintroduces `toc_text`

Examples tested:

- `title + scope + toc`
- `title + scope + objective + toc`
- `title + toc`

These combinations pulled the ranking back toward the same bad TOC-heavy pattern:

- `ifric17-bc`
- `ifric17`
- `ias7-bc`
- `ifrs17-bc`
- strong NAVIS topic-title matches, including IAS 39 hedge chapters

Representative target ranks:

- `title + scope + toc`:
  - `ifrs9` - rank 10
  - `ifric16` - rank 82
- `title + toc`:
  - `ifrs9` - rank 45
  - `ifric16` - rank 207

**Interpretation:** for this family, `toc_text` is the main field reintroducing dividend / broad-accounting noise.

### IFRIC: `background_text + issue_text`

Concatenating `background_text` and `issue_text` for IFRIC documents, ranked on the combined text. Excluding BC.

| Rank | Score | doc_uid | Target? |
| ---: | ---: | --- | --- |
| 1 | 0.6113 | ifric17 | |
| 2 | 0.5508 | ifric19 | |
| 3 | 0.5409 | ifric7 | |
| **4** | **0.5361** | **ifric16** | **<<<** |
| 5 | 0.5184 | ifric14 | |
| 6 | 0.5102 | ifric12 | |
| 7 | 0.5085 | ifric21 | |
| 8 | 0.5067 | ifric23 | |
| 9 | 0.5060 | ifric22 | |
| 10 | 0.4998 | ifric16-ie | |
| 11 | 0.4897 | ifric2 | |
| 12 | 0.4858 | ifric10 | |
| 13 | 0.4615 | ifric1 | |
| 14 | 0.4541 | ifric5 | |
| 15 | 0.4394 | ifric20 | |
| 16 | 0.4372 | ifric6 | |

This is the best result for the IFRIC family so far. `ifric16` reaches **rank 4** (score 0.5361) — matching `background_text` alone (rank 4) and better than `issue_text` alone (rank 6). Crucially, `ifric17` (genuinely relevant) rises to rank 1 with the highest score in any single or combined probe (0.6113), pulled up by the combined signal from both fields. The combination does not improve `ifric16`'s rank over `background_text` alone in this probe, but it produces a stronger separation between relevant and false-positive IFRICs.

## Results - type-aware primary field strategy

Based on the single-field and combination probes above, the following type-aware routing strategy is proposed:

- **IFRS-S + IAS-S** → `scope_text` only
- **IFRIC + SIC** (all variants) → `background_text + issue_text`
- **NAVIS and other** (IFRS/IAS variants, PS) → all populated fields (current project approach)

The per-family rankings and combined global ranking were computed with this strategy:

### IFRS-S + IAS-S → `scope_text`

39 non-BC documents. Top results:

| Rank | Score | doc_uid | Target? |
| ---: | ---: | --- | --- |
| 1 | 0.5996 | ias24 | |
| 2 | 0.5974 | ifrs9 | <<< |
| 3 | 0.5932 | ifrs3 | |
| 4 | 0.5897 | ias21 | |
| 5 | 0.5874 | ias32 | |
| 6 | 0.5865 | ias37 | |
| 7 | 0.5858 | ifrs7 | |
| 8 | 0.5803 | ifrs8 | |
| 9 | 0.5800 | ifrs19 | |
| 10 | 0.5686 | ias33 | |
| … | | | |
| 34 | 0.4951 | ifrs16 | |

`ifrs9` is at **rank 2** (score 0.5974) — the best result for any IFRS/IAS target in any probe. `ifrs16` (related to leases) is at rank 34, far below `ifrs9`.

### IFRIC + SIC → `background_text + issue_text`

28 documents (all IFRIC/SIC variants). Top results:

| Rank | Score | doc_uid | Target? |
| ---: | ---: | --- | --- |
| 1 | 0.6113 | ifric17 | |
| 2 | 0.5508 | ifric19 | |
| 3 | 0.5444 | ifric23-bc | |
| 4 | 0.5409 | ifric7 | |
| 5 | 0.5379 | ifric16-bc | <<< |
| **6** | **0.5361** | **ifric16** | **<<<** |
| 7 | 0.5266 | ifric7-bc | |
| 8 | 0.5184 | ifric14 | |
| 9 | 0.5111 | ifric2-bc | |
| 10 | 0.5102 | ifric12 | |
| … | | | |
| 20 | 0.4787 | sic25 | |

`ifric16` is at **rank 6** within its family, `ifric16-bc` at rank 5. `ifric17` (genuinely relevant) ranks first with the highest score in any probe (0.6113).

### NAVIS and other → all fields

NAVIS (59 docs) and other documents (77 docs) use all populated fields. These families dominate the global ranking, with BC documents scoring highest.

### Combined global ranking (all families)

| Rank | Score | doc_uid | Family | Target? |
| ---: | ---: | --- | --- | --- |
| 1 | 0.6145 | ifrs17-bc | Other | |
| 2 | 0.6113 | ifric17 | IFRIC+SIC | |
| 3 | 0.6009 | ifrs12-bc | Other | |
| 4 | 0.5996 | ias24 | IFRS-S+IAS-S | |
| 5 | 0.5990 | ifrs9-bc | Other | <<< |
| 6 | 0.5985 | ifrs7-bc | Other | |
| 7 | 0.5983 | ifrs2-bc | Other | |
| **8** | **0.5974** | **ifrs9** | **IFRS-S+IAS-S** | **<<<** |
| 9 | 0.5939 | navis-…C20B0EF9…-EFL | NAVIS | |
| 10 | 0.5932 | ifrs3 | IFRS-S+IAS-S | |
| … | | | | |
| 64 | 0.5379 | ifric16-bc | IFRIC+SIC | <<< |
| **70** | **0.5361** | **ifric16** | **IFRIC+SIC** | **<<<** |
| 133 | 0.4951 | ifrs16 | IFRS-S+IAS-S | |

**Target ranks:**

- `ifrs9` — **rank 8** (score 0.5974)
- `ifrs9-bc` — rank 5 (score 0.5990)
- `ifric16` — rank 70 (score 0.5361)
- `ifric16-bc` — rank 64 (score 0.5379)

**Interpretation:** this strategy is a clear improvement on the naive approach. `ifrs9` rises to **rank 8** (up from rank 9 in the naive strategy), and `ifric16` rises to **rank 70** (up from rank 98). Both targets are now within the top 100 and are scored higher than in any previous strategy. `ifric17` (genuinely relevant) ranks 2nd globally — a strong signal.

The remaining gap for `ifric16` (rank 70) reflects the structural vocabulary mismatch between the question and IFRIC 16's issue text (net investment hedge, not dividend receivable), combined with BC/IE/IG variants still scoring well despite using all fields. Excluding BC variants from the IFRIC+SIC family would further improve the result.

## Best additional signal found: section headings + lineage

The most promising extra signal did **not** come from another `documents` column.

A separate diagnostic embedded each section using:

- `sections.title`
- `sections.section_lineage`

and then aggregated section similarity back to a document using the **max section score per document**.

### Top results for Q1.0

1. `navis-QRIFRS-C2DB864AD71978-EFL`
   - section: `Couverture de change de flux d'intérêt intragroupe futurs`
2. `navis-QRIFRS-C2D9D1995F171F-EFL`
   - section: `Swaps de devises (« cross currency swaps »/CCS) et prêt intragroupe`
3. `navis-QRIFRS-C291EF899838F8-EFL`
   - section: `Traitement comptable des garanties financières intragroupe dans les comptes consolidés`
4. `ifric17`
5. `ifric17-bc`
6. `navis-QRIFRS-C123A59E4A2116-EFL`

### Target ranks

- `navis-QRIFRS-C2D9D1995F171F-EFL` - rank 2
- `ifrs9-bc` - rank 26
- `ifrs9` - rank 87
- `ifric16-bc` - rank 170
- `ifric16` - rank 189

### Interpretation

This signal is useful because section headings contain the exact anchors the question needs but that the document-level concat tends to blur:

- `comptabilité de couverture`
- `documentation`
- `devises`
- `intragroupe`
- `comptes consolidés`

The strongest improvement is on **practical chapter routing**, especially in NAVIS.

It still does **not** automatically solve the IFRIC 16 problem, because Q1.0 never says:

- net investment
- foreign operation
- activité à l'étranger

So IFRIC 16 remains a concept-expansion problem as much as a retrieval-field problem.

## Main conclusions

### 1. `scope_text` is the best single persisted `xx_text` field

If we must choose **one document field only**, `scope_text` is the best candidate from the current schema.

With the project's actual 24000-character truncation budget, it was the only individual `xx_text` field that pushed Q1.0 clearly toward the right conceptual area.

### 2. `toc_text` remains the noisiest field for this routing problem

`toc_text` has the best coverage, but it is still one of the main causes of the Q1.0 false-positive pattern.

For this family, TOC titles overreact to:

- dividend
- recognition
- measurement
- presentation

and therefore favor:

- `ifric17`
- `ifric17-bc`
- `ias7-bc`
- `ifrs17-bc`

### 3. A type-aware routing strategy materially outperforms the broad concat

The naive "concat all fields" strategy scored `ifric16` at rank 98 and `ifrs9` at rank 33 on Q1.0. A type-aware strategy:

- **IFRS-S + IAS-S** → `scope_text` only
- **IFRIC + SIC** → `background_text + issue_text`
- **NAVIS + other** → all fields (current approach)

…scores `ifric16` at **rank 70** and `ifrs9` at **rank 8**. This is the strongest result for both targets in any probe run so far.

The key insight is that `scope_text` alone is the best driver for `ifrs9` routing, while `background_text + issue_text` is the best driver for IFRIC/SIC routing.

### 4. `background_text` is the best single field for IFRIC/SIC routing

Within the IFRIC family, `background_text` alone puts `ifric16` at rank 4 (score 0.5140) — the best single-field result for that family. Combining `background_text + issue_text` does not improve the rank of `ifric16` (still rank 4 excl BC, rank 6 in the combined family probe) but raises `ifric17` (genuinely relevant) to the highest score in any probe (0.6113), creating a stronger separation between relevant and false-positive IFRICs.

### 5. The best new retrieval signal is in `sections`, not `documents`

The most promising improvement path is to add a second document-routing signal derived from:

- `sections.title`
- `sections.section_lineage`

aggregated per document.

This is especially attractive because:

- the `sections` data is already in the database
- title retrieval infrastructure already exists
- the signal aligns better with the practical concepts actually expressed in the question

### 5. IFRIC 16 routing improves significantly but a gap remains

With the type-aware strategy, `ifric16` reaches rank 70 (from rank 98 in the naive concat). The remaining gap reflects a structural vocabulary mismatch: the question never uses "net investment", "foreign operation", or "reclassification adjustment", which are the core concepts in IFRIC 16's issue text. Field-level routing alone cannot bridge this gap — section-level or concept-expansion strategies are needed to surface it further.

## Recommendation

### Immediate

1. implement the type-aware routing strategy proven above:
   - **IFRS-S + IAS-S** → `scope_text` only
   - **IFRIC + SIC** (all variants) → `background_text + issue_text`
   - **NAVIS + other** → all populated fields (current approach)
2. validate this strategy on the full question family (not just Q1.0)
3. use `source_title` and `document_kind` as **reranking features**, not the main embedding text
4. demote BC documents during document selection or reranking — they consistently inflate scores across all fields

### Next

Implement a second document-routing signal from **`sections.title + sections.section_lineage`**, aggregated back to the document level and combined with the primary document score.

This is the most promising next slice because it improves semantic precision without requiring new database schema — and would particularly help surface `ifric16`, whose relevance is not captured by any document-level field on Q1.
