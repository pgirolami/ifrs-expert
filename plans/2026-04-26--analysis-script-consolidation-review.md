# Plan -- analysis script consolidation review

Date: 2026-04-26
Scope: `experiments/analysis` and closely related experiment diagnostics scripts

## Goal

Consolidate the current diagnostics scripts around stable diagnostic layers instead of one-off experiment scripts.

The target shape is:

- run-level generators that produce diagnostics inside an experiment directory
- comparison scripts that consume existing diagnostics across runs or experiments
- analysis scripts that consume generated or comparison diagnostics and append reproducible interpretation to `EXPERIMENTS.md`
- canonical artifact names that are stable across experiment numbers
- clear separation between document routing, target chunk retrieval, and approach detection

## Proposed Diagnostic Layers

| Layer | Question it answers | Scripts | Primary artifact |
| --- | --- | --- | --- | 
| `document_routing` | Did the right documents enter the candidate set, and at what rank/score? | `document_routing/generate_document_routing_diagnostics.py`<br>`document_routing/compare_document_routing_diagnostics.py`<br>`document_routing/analyze_document_routing_diagnostics.py` | `document_routing_diagnostics.md` |
| `target_chunk_retrieval` | Did the required authoritative chunks/paragraphs get retrieved for the target documents? | `generate_target_chunk_retrieval_diagnostics.py`<br>`compare_target_chunk_retrieval_diagnostics.py`<br>`analyze_target_chunk_retrieval_diagnostics.py` | `target_chunk_retrieval_diagnostics.md` |
| `approach_detection` | Did Prompt B emit the expected approaches, and do wrong approaches correlate with retrieved sections? | `generate_approach_detection_diagnostics.py`<br>`compare_approach_detection_diagnostics.py`<br>`analyze_approach_detection_diagnostics.py` | `approach_detection_diagnostics.html` |

Comparison scripts should not rerun retrieval or LLM calls. They should consume artifacts produced by the run-level generators. Analyze scripts should not rerun retrieval or LLM calls either; they should consume generated diagnostics, produce an interpretation that is reproducible, and write or append that interpretation to the experiment's `EXPERIMENTS.md`.

## Canonical Artifact Names

| Layer | Run-level artifacts | Comparison artifacts |
| --- | --- | --- |
| `document_routing` | `document_routing_diagnostics.md`, `document_routing_diagnostics.json`, `document_routing_raw/*.retrieve.json` | `document_routing_comparison.md`, `document_routing_comparison.json` |
| `target_chunk_retrieval` | `target_chunk_retrieval_diagnostics.md`, `target_chunk_retrieval_diagnostics.json`, `target_chunk_retrieval_raw/*.retrieve.json` | `target_chunk_retrieval_comparison.md`, `target_chunk_retrieval_comparison.json` |
| `approach_detection` | `approach_detection_diagnostics.html`, `approach_detection_diagnostics.md`, `approach_detection_diagnostics.json` | `approach_detection_comparison.md`, `approach_detection_comparison.json` |

Secondary artifacts can exist, but each layer should have one primary artifact that humans open first.

## Current Artifact Writers

The table below is one row per script-artifact pair. Examples are checked against the current checkout.

| Script | Goal | Layer | Current artifact | Example |
| --- | --- | --- | --- | --- |
| `generate_spurious_approaches_sections_matrix.py` | Diagnose wrong approaches by showing emitted labels against retrieved sections. | `approach_detection` | `spurious_approaches_vs_sections_matrix.html` | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/31_new_A_with_less_context_in_B/spurious_approaches_vs_sections_matrix.html) |
| `rebuild_document_field_table.py` | Rebuild an ingestion verification table from document representation fields. | corpus/ingestion metadata | `EXPERIMENTS.md` at `experiments/39_exhaustive_ifrs_ingestion_verification/EXPERIMENTS.md` | not present in checkout |
| `run_q1_retrieve_target_matrix.py` | Diagnose document routing for each Q1 variant. | `document_routing` | `generated_q1_retrieve_target_matrix.md` | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/39_more_retrieval_investigations/generated_q1_retrieve_target_matrix.md) |
| `run_q1_retrieval_mode_comparison.py` | Compare raw, enriched, and English-control document routing. | `document_routing` comparison | `generated_fr_raw_target_matrix.md` | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/40_compare_q1_retrieval_modes/generated_fr_raw_target_matrix.md) |
| `run_q1_retrieval_mode_comparison.py` | Compare raw, enriched, and English-control document routing. | `document_routing` comparison | `generated_fr_enriched_target_matrix.md` | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/40_compare_q1_retrieval_modes/generated_fr_enriched_target_matrix.md) |
| `run_q1_retrieval_mode_comparison.py` | Compare raw, enriched, and English-control document routing. | `document_routing` comparison | `generated_en_control_target_matrix.md` | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/40_compare_q1_retrieval_modes/generated_en_control_target_matrix.md) |
| `run_q1_retrieval_mode_comparison.py` | Compare raw, enriched, and English-control document routing. | `document_routing` comparison | `generated_merged_delta_report.md` | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/40_compare_q1_retrieval_modes/generated_merged_delta_report.md) |
| `run_q1_retrieval_mode_comparison.py` | Compare raw, enriched, and English-control document routing. | `document_routing` comparison | `generated_merged_delta_report.json` | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/40_compare_q1_retrieval_modes/generated_merged_delta_report.json) |
| `run_q1_retrieval_mode_comparison.py` | Compare raw, enriched, and English-control document routing. | `document_routing` comparison | `generated_summary.md` | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/40_compare_q1_retrieval_modes/generated_summary.md) |
| `run_q1_retrieval_mode_comparison.py` | Compare raw, enriched, and English-control document routing. | `document_routing` comparison | `generated_summary.json` | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/40_compare_q1_retrieval_modes/generated_summary.json) |
| `run_q1_retrieval_non_regression.py` | Run deterministic retrieval gates and diagnostics from a fixture. | `target_chunk_retrieval` / gate runner | `summary.md` | not present under its default generated output path |
| `run_q1_retrieval_non_regression.py` | Run deterministic retrieval gates and diagnostics from a fixture. | `target_chunk_retrieval` / gate runner | `summary.json` | not present under its default generated output path |
| `run_q1_retrieval_non_regression.py` | Run deterministic retrieval gates and diagnostics from a fixture. | `target_chunk_retrieval` / gate runner | raw retrieve JSON | not present under its default generated output path |
| `run_q1_target_recall_summary.py` | Summarize target-document recall for one retrieval policy. | `target_chunk_retrieval` | `summary.md` | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/43_standards_only_through_chunks/runs/summary/summary.md) |
| `run_q1_target_recall_summary.py` | Summarize target-document recall for one retrieval policy. | `target_chunk_retrieval` | `summary.json` | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/43_standards_only_through_chunks/runs/summary/summary.json) |
| `run_q1_target_recall_summary.py` | Summarize target-document recall for one retrieval policy. | `target_chunk_retrieval` | raw retrieve JSON | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/43_standards_only_through_chunks/runs/summary/runs/policy.default/standards_only_through_chunks__enriched/Q1.0.retrieve.json) |
| `run_q1_variant_similarity_table.py` | Show document representation scores in a compact table. | document routing / representation diagnostics | `variant_similarity_table.md` | [example](/Users/philippe/Documents/workspace/ifrs-expert/experiments/analysis/variant_similarity_table.md) |
| `run_q1_variant_similarity_table.py` | Compare target matrices. | `document_routing` comparison | `q1-target-retrieval__documents2-through-chunks__comparison.md` | not present in checkout |

## Stdout-Only Scripts

These scripts currently print reports and do not write artifacts unless shell redirection is used.

| Script | Goal | Current stdout output | Layer fit | Reuse decision |
| --- | --- | --- | --- | --- |
| `analyze_labels.py` | Inspect normalized approach labels and hard-coded canonical mappings for experiment 08. | Canonical label mapping table and label frequency by question. | `approach_detection` | Fold label mapping/frequency into `approach_detection_diagnostics.md/json`. |
| `compare_chunks.py` | Compare retrieval chunks for high and low performers in experiment 07. | Markdown chunk tables, expansion tables, and aggregate stability metrics. | overlaps with `approach_detection`; cross-checks retrieval context quality | Do not keep as a standalone script. Reuse only the extra metrics that the spurious matrix does not provide: strict/loose stability aggregates, top/low retrieval score ranges, and expansion-section context. |
| `generate_label_table.py` | Generate label frequency tables for experiments 07 and 08. | Markdown label-frequency tables by question. | `approach_detection` | Merge with label-frequency output from `run_promptfoo_analysis.py`. |
| `run_promptfoo_analysis.py` | Analyze Promptfoo answer artifacts for stability, labels, citations, and retrieval context. | Rich markdown report: per-question stability, detailed breakdown, aggregate metrics, label frequency, citation frequency, top/low performers. | `approach_detection` | Best source for `generate_approach_detection_diagnostics.py` and `compare_approach_detection_diagnostics.py`. |
| `run_stability_scoring.py` | Score repeated Prompt B outputs and compare retrieval context for experiment 08. | Stability summary, aggregate metrics, top/low performer comparison. | `approach_detection`, with retrieval-context correlation | Fold into the canonical approach diagnostics; keep `stability_scorer.py` as reusable library code. |

## Feedback Incorporated

### Approach detection

`spurious_approaches_vs_sections_matrix.html` is a strong artifact and should become the primary HTML view for `approach_detection`.

Earmarked improvement:

- when expected paragraphs are defined in `family.yaml`, highlight them directly in the section/paragraph matrix

The stdout-only scripts add useful approach diagnostics:

- label frequency by question
- canonical label mapping
- citation frequency by question
- stability score by question
- top/low performer comparison

These should become secondary sections in `approach_detection_diagnostics.md` and machine-readable fields in `approach_detection_diagnostics.json`.

The label frequency table should be produced by `generate_approach_detection_diagnostics.py`, not by a separate long-lived script.

`compare_chunks.py` overlaps with the spurious-approaches matrix because both connect retrieved context to answer behavior. The spurious matrix is the better primary diagnostic because it shows the run-level relationship between emitted labels and retrieved sections. `compare_chunks.py` brings three reusable additions: aggregate strict/loose stability scores, top/low retrieval score ranges, and expansion-section context. Those should be folded into `generate_approach_detection_diagnostics.py` or `analyze_approach_detection_diagnostics.py`.

### Document routing

`generated_q1_retrieve_target_matrix.md` is a strong document-routing diagnostic. It should become the basis for `document_routing_diagnostics.md`.

`run_q1_retrieval_mode_comparison.py` overlaps heavily with `run_q1_retrieve_target_matrix.py`. It should stop recomputing the same retrieval work. The comparison script should consume saved run-level `document_routing_diagnostics.json` or target matrices produced by the generator.

`generated_merged_delta_report.md` is useful but hard to read. Earmarked improvement:

- replace or supplement it with a compact variant-similarity-style comparison table
- keep verbose row-level detail in JSON and optionally in an appendix section

`generated_summary.md` makes sense for comparisons, not as the main run-level artifact. The per-row detail currently in comparison outputs should live at the bottom of each run-level target matrix.

### Target chunk retrieval

`run_q1_target_recall_summary.py` and `run_q1_retrieval_non_regression.py` belong in the target chunk retrieval layer, but they currently mix run generation, summary rendering, raw JSON capture, and gate logic.

The canonical split should be:

- `generate_target_chunk_retrieval_diagnostics.py`: produce raw retrieve JSON, recall summaries, and expected-paragraph coverage
- `compare_target_chunk_retrieval_diagnostics.py`: compare already-generated diagnostics across policies/runs/experiments
- gate evaluation can be a mode or wrapper over the generated diagnostics, not a separate data model

### Representation and corpus metadata diagnostics

`variant_similarity_table.md` is useful mainly because of its display style, not because the representation-comparison experiment still needs to exist as-is.

Going forward:

- retire the standalone representation-comparison purpose unless a new retrieval experiment needs it
- reuse the table style for document routing comparisons
- keep representation diagnostics as a secondary document-routing view when debugging why a policy routed to the wrong document

`rebuild_document_field_table.py` is not part of the three runtime diagnostic layers. It belongs to corpus/ingestion metadata verification. It should either stay separate or move under a future `corpus_metadata_diagnostics` layer.

## Consolidation Plan

### 1. Define artifact contracts first

Before moving code, pin the output contract for each canonical artifact:

- required inputs
- output directory layout
- markdown sections
- JSON schema
- whether it is run-level or comparison-level
- how the layer-specific `analyze_*` script writes reproducible findings into `EXPERIMENTS.md`

### 2. Extract common readers and parsers

Shared helpers should cover:

- Promptfoo run discovery
- `A-prompt.txt` chunk extraction
- `B-response.md` and `B-response.json` loading
- retrieve JSON parsing
- target document/rank extraction
- expected documents and expected paragraphs from `family.yaml`

### 3. Consolidate document routing scripts

Target:

- `document_routing/generate_document_routing_diagnostics.py`
- `document_routing/compare_document_routing_diagnostics.py`
- `document_routing/analyze_document_routing_diagnostics.py`

Migration:

- fold `run_q1_retrieve_target_matrix.py` into the generator
- make `run_q1_retrieval_mode_comparison.py` call or consume generator outputs
- reuse the `variant_similarity_table.md` display style for comparisons
- add an analyzer that summarizes routing failures, improvements/regressions, and notable rank/score movements into `EXPERIMENTS.md`

### 4. Consolidate target chunk retrieval scripts

Target:

- `generate_target_chunk_retrieval_diagnostics.py`
- `compare_target_chunk_retrieval_diagnostics.py`
- `analyze_target_chunk_retrieval_diagnostics.py`

Migration:

- fold `run_q1_target_recall_summary.py` into the generator
- fold the useful parts of `run_q1_retrieval_non_regression.py` into gate evaluation over generated diagnostics
- add expected paragraph coverage from `family.yaml`
- add an analyzer that summarizes missing target chunks, expected-paragraph misses, and retrieval gate failures into `EXPERIMENTS.md`

### 5. Consolidate approach detection scripts

Target:

- `generate_approach_detection_diagnostics.py`
- `compare_approach_detection_diagnostics.py`
- `analyze_approach_detection_diagnostics.py`

Migration:

- fold `generate_spurious_approaches_sections_matrix.py` into the generator
- fold `run_promptfoo_analysis.py`, `run_stability_scoring.py`, `analyze_labels.py`, and `generate_label_table.py` into markdown/JSON secondary sections
- fold useful non-overlapping parts of `compare_chunks.py` into generated diagnostics or the analyzer
- keep `stability_scorer.py` as reusable library code
- add an analyzer that summarizes spurious approach patterns, label-frequency anomalies, and context correlations into `EXPERIMENTS.md`

### 6. Decide what to retire

Likely retire or convert to wrappers:

- `analyze_labels.py`
- `generate_label_table.py`
- `compare_chunks.py`
- `run_stability_scoring.py`

Already removed:

- `analyze.py`, because no current script imports or calls it; historical experiment commands should call `run_promptfoo_analysis.py` directly

Likely keep as library code:

- `stability_scorer.py`

Likely rewrite as canonical scripts:

- `run_promptfoo_analysis.py`
- `generate_spurious_approaches_sections_matrix.py`
- `run_q1_retrieve_target_matrix.py`
- `run_q1_retrieval_mode_comparison.py`
- `run_q1_target_recall_summary.py`
- `run_q1_retrieval_non_regression.py`

## Test Contract

Add tests for:

- default artifact paths
- JSON schema shape for each canonical diagnostics layer
- markdown section presence
- comparison scripts consuming saved artifacts without recomputing retrieval
- expected paragraph highlighting when `family.yaml` defines paragraph expectations
- backward-compatible wrappers, if any are retained

## Intended Outcome

The diagnostics surface should become:

- easier to run against one experiment directory
- easier to compare across experiments
- stable enough to link from experiment notes
- structured enough to support future automated regression checks

## Implementation

### document_routing contract

Run-level generator:

- `document_routing/generate_document_routing_diagnostics.py`
- default output root: `<experiment>/runs/<run_id>/diagnostics/document_routing/`
- run markdown artifact: `document_routing_diagnostics.md`
- run JSON artifact: `document_routing_diagnostics.json`
- raw retrieval payloads: `raw/<question_id>.retrieve.json`
- experiment index artifact: `<experiment>/diagnostics/document_routing_index.md`
- experiment index JSON: `<experiment>/diagnostics/document_routing_index.json`

Generator CLI arguments:

- `--experiment`: required experiment directory or experiment number
- `--run-id`: required only when the experiment directory contains more than one run

Generator-derived inputs:

- provider label comes from the selected run's `promptfooconfig.yaml`
- question files come from `promptfooconfig.yaml:tests[*].metadata.question_path`
- question family ids come from `promptfooconfig.yaml:tests[*].metadata.family`
- fail fast if any test lacks a readable `metadata.family` or `metadata.question_path`
- policy file path comes from `promptfooconfig.yaml:providers.config.policy-config`
- policy file contents come from the selected run's `effective/` directory
- policy name comes from `promptfooconfig.yaml:providers.config.retrieval-policy`
- glossary file comes from the selected run's `effective/` directory
- target documents come from each resolved question family's `family.yaml`

Artifact granularity:

- one artifact per run is better for provenance, reproducibility, and comparisons because it records the exact policy, glossary, questions, raw retrieval payloads, and generated timestamp for one execution
- one artifact per experiment is better for browsing and linking from `EXPERIMENTS.md`, especially when an experiment has many runs
- the recommended shape is both: per-run artifacts are canonical data, and the experiment-level index is a lightweight rollup that links to each run
- comparison and analysis scripts should consume per-run JSON artifacts; they may use the experiment index only to discover available runs

Markdown contract:

- one matrix table with a `Question` column, a `Total` column, one column per retrieved document, and a bottom `Total` row
- each question row shows candidate count plus `score / rank` for each retrieved document when present
- the total row shows per-document coverage and score range
- keep the markdown compact and scan-friendly, matching the historical single-run matrix style
- reuse the single-run matrix styling: rank-colored cells, target-document columns left-most in family-file order, remaining retrieved-document columns sorted by coverage, and the same HTML span formatting for populated cells

JSON contract:

- `experiment_name`
- `provider_name`
- `run_id`
- `generated_at`
- `question_families`
- `question_sources`
- `question_ids`
- `policy_file`
- `effective_policy_file`
- `policy_name`
- `policy`
- `glossary_file`
- `effective_glossary_file`
- `target_documents`
- `rows`
- `document_summaries`

Each row should include:

- `question_id`: stable question variant id, for example `Q1.0`
- `run_id`: id of the retrieval run that produced the row; for a single-run artifact this repeats the top-level `run_id`
- `question_path`: source question file used for retrieval
- `question_text_sha256`: hash of the question text, so analysis can detect stale diagnostics without storing duplicate full text everywhere
- `document_hits`: ordered unique document hits returned by retrieval; each hit should include `doc_uid`, display label, rank, score, and any available representation metadata
- `selected_document`: target document selected for the row when evaluating a specific expected document; `null` when the row is a general candidate-set row
- `selected_rank`: rank of `selected_document` in `document_hits`; `null` when absent or not applicable
- `selected_score`: score of `selected_document` in `document_hits`; `null` when absent or not applicable
- `in_candidate_set`: whether `selected_document` was retrieved
- `candidate_count`: number of unique document candidates in `document_hits`
- `target_documents_present`: map of configured target document uid to boolean candidate-set presence
- `target_document_ranks`: map of configured target document uid to rank or `null`
- `target_document_scores`: map of configured target document uid to score or `null`

Compare-level script:

- `document_routing/compare_document_routing_diagnostics.py`

Compare CLI arguments:

- `--input`: required; repeatable path to a per-run `document_routing_diagnostics.json` or experiment `index.json`
- `--label`: optional; repeatable display label aligned with `--input`
- `--output-dir`: required directory for comparison artifacts
- `--target-documents`: optional comma-separated list limiting the target documents shown in the comparison

- input can be two or more per-run `document_routing_diagnostics.json` files
- input can also be one or more experiment index JSON files, which expand to their listed per-run JSON artifacts
- accepts explicit labels for each input so comparisons are readable across experiments
- requires an explicit `--output-dir`
- writes to `<output-dir>/document_routing_comparison.md`
- writes companion JSON to `<output-dir>/document_routing_comparison.json`
- supports two-way comparisons and N-way comparisons
- two-way comparisons should show direct deltas for rank and candidate presence, with score retained in JSON for downstream analysis if needed
- N-way comparisons should use compact table summaries first, with detailed rows in JSON and appendix sections
- does not rerun retrieval

Analyze-level script:

- `document_routing/analyze_document_routing_diagnostics.py`

Analyze CLI arguments:

- `--experiment`: required experiment directory or experiment number; determines the `EXPERIMENTS.md` destination
- `--input`: required only when the experiment has more than one diagnostics run, or when analyzing a comparison; path to one per-run `document_routing_diagnostics.json`, one experiment `index.json`, or one `document_routing_comparison.json`
- `--section-title`: optional heading for the generated `EXPERIMENTS.md` section

- input can be one per-run `document_routing_diagnostics.json`, one experiment `index.json`, or one `document_routing_comparison.json`
- if the experiment has exactly one diagnostics run and `--input` is omitted, the script uses that run's `document_routing_diagnostics.json`
- requires explicit `--input` when multiple diagnostics runs exist for the experiment
- when given an experiment index, it analyzes all runs listed in that index
- when given comparison JSON, it analyzes routing changes across the compared runs
- writes the analysis section directly to `<experiment>/EXPERIMENTS.md`
- reports target-document regressions, wins, and notable score/rank changes
- cites the exact artifact paths it used
- does not rerun retrieval
