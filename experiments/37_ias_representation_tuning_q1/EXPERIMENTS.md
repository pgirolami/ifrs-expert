# Experiment 37: IAS-S representation tuning for Q1 variants

## Goal

Find a better **IAS-S document representation** than the current policy setting, so we can use a relatively high `min_score` and relatively low `d` while retrieving `ias39` across all Q1 variants.

Context: experiment 36 showed that with current representations, getting `ias39` on all Q1 variants required very lax settings.

## Method

### 1) IAS-only representation ranking study

For all `IAS-S` documents, we built candidate texts from persisted document fields and measured, for each Q1 query variant, where `ias39` ranks among IAS-S docs.

Candidates tested:

- `full`
- `scope`
- `toc`
- `scope_plus_toc`
- `scope_plus_title`
- `scope_plus_objective`
- `full_no_toc`

Artifacts:

- `ias_representation_rank_summary.json`
- `ias_representation_per_query_scores.json`

### 2) End-to-end retrieval simulation with best IAS representation

Because policy currently supports only `full|scope|background_and_issue`, we simulated an IAS-only representation override to `toc` while keeping all other document types/routing unchanged.

Then we searched for parameters that retrieve `ias39` across all Q1 variants.

Artifact:

- `simulated_toc_policy_results.json`

## Key findings

### IAS-only ranking quality

From `ias_representation_rank_summary.json`, best candidates by `ias39` worst-case rank:

- `toc`: best overall among tested candidates (`max_rank=12`, `min_score≈0.443`)
- `scope_plus_toc`: next best (`max_rank=16`)
- `full`: weaker (`max_rank=18`)
- `scope`: weaker (`max_rank=19`)

So for IAS on Q1, **TOC-heavy representation is materially better** than `full` or `scope` for surfacing `ias39`.

### Parameter outcome

Using IAS representation = `toc` in simulation:

- With `global_d=25`: no 23/23 solution; best was 21/23.
- With `global_d=30`: we found a 23/23 solution with:
  - `IAS-S d=12`
  - `IAS-S min_score=0.44`

This retrieves `ias39` on all Q1 variants in the simulated end-to-end selection.

## Recommended next step

Add a new policy representation option for document routing:

- `similarity_representation: toc`

Then run a real retrieval experiment (CLI, not simulation) with:

- `IAS-S similarity_representation: toc`
- `IAS-S d=12`
- `IAS-S min_score=0.44`
- `global_d=30`

and validate downstream answer quality/noise.

## Files in this experiment

- `EXPERIMENTS.md`
- `ias_representation_rank_summary.json`
- `ias_representation_per_query_scores.json`
- `simulated_toc_policy_results.json`
