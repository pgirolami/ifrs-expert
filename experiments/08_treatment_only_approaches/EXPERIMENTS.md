# 2026-03-26

# Scope
Tightened Prompt A and B to enforce a strict separation: 
- A now extracts only canonical accounting treatments (no decision or analysis steps)
- B evaluates applicability strictly in the context of the question and assumptions.

The goal is to reduce spurious approaches and improve consistency in applicability and final recommendations.

# Analysis result

## Summary

| Metric | Value (per-question avg) | Value (aggregate loose) |
|--------|-------------------------|----------------------|
| **Average Strict Score** | **85.4** | 84.3 |
| **Average Loose Score** | **93.0** | 92.7 |
| **Questions Analyzed** | 22 | 22 |
| **Total Runs** | 68 | 68 |

> Note: The per-question averages (85.4 strict, 93.0 loose) are computed by averaging each question's score. The aggregate values (84.3 strict, 92.7 loose) treat each of the 68 runs as equal, computing pairwise similarity across all runs.

## Detailed Results

| Question | Runs | Strict Score | Loose Score | Approach (orig) | Approach (mapped) | Applicability | Applicability (loose) | Recommendation |
|----------|------|-------------|-------------|-----------------|---------------------|----------------|----------------------|----------------|
| Q1    | 3 | **90.0** | **90.0** | 1.00 | 1.00 | 0.67 | 0.67 | 1.00 |
| Q1.1  | 3 | **58.9** | **92.2** | 0.78 | 0.78 | 0.33 | 1.00 | 0.33 |
| Q1.2  | 3 | **92.2** | **92.2** | 0.78 | 0.78 | 1.00 | 1.00 | 1.00 |
| Q1.3  | 3 | **90.0** | **90.0** | 1.00 | 1.00 | 0.67 | 0.67 | 1.00 |
| Q1.4  | 3 | **88.3** | **88.3** | 0.67 | 0.67 | 1.00 | 1.00 | 1.00 |
| Q1.5  | 3 | **66.7** | **100.0** | 1.00 | 1.00 | 0.33 | 1.00 | 0.33 |
| Q1.6  | 2 | **100.0** | **100.0** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Q1.7  | 3 | **88.3** | **88.3** | 0.67 | 0.67 | 1.00 | 1.00 | 1.00 |
| Q1.8  | 3 | **100.0** | **100.0** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Q1.9  | 3 | **55.0** | **88.3** | 0.67 | 0.67 | 0.33 | 1.00 | 0.33 |
| Q1.10 | 3 | **60.0** | **88.3** | 0.67 | 0.67 | 0.50 | 0.50 | 0.33 |
| Q1.11 | 3 | **76.7** | **100.0** | 1.00 | 1.00 | 0.67 | 1.00 | 0.33 |
| Q1.12 | 3 | **88.3** | **88.3** | 0.67 | 0.67 | 1.00 | 1.00 | 1.00 |
| Q1.13 | 3 | **88.3** | **88.3** | 0.67 | 0.67 | 1.00 | 1.00 | 1.00 |
| Q1.14 | 3 | **76.7** | **100.0** | 1.00 | 1.00 | 0.67 | 1.00 | 0.33 |
| Q1.15 | 3 | **56.7** | **56.7** | 0.33 | 0.67 | 0.33 | 0.33 | 1.00 |
| Q1.16 | 3 | **100.0** | **100.0** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Q1.17 | 3 | **100.0** | **100.0** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Q1.18 | 3 | **100.0** | **100.0** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Q1.19 | 3 | **100.0** | **100.0** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Q1.20 | 3 | **100.0** | **100.0** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Q1.21 | 3 | **100.0** | **100.0** | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Q1.22 | 3 | **88.3** | **88.3** | 0.67 | 0.67 | 1.00 | 1.00 | 1.00 |

## Interpretation

- **Score (strict)**: 85.4 average (aggregate: 84.3) — measures exact consistency in approaches, applicability values, and recommendations
- **Score (loose)**: 93.0 average (aggregate: 92.7) — treats "oui" and "oui_sous_conditions" as equivalent

### Key observations:
1. **8 questions achieve perfect stability (100.0)**: Q1.16, Q1.17, Q1.18, Q1.19, Q1.20, Q1.21, Q1.6, Q1.8
2. **Strong improvement over experiment 07**: 85.4 vs 51.3 (strict), 93.0 vs 71.1 (loose)
3. **Loose score higher than strict** for Q1.11, Q1.14, Q1.5, Q1.10, Q1.1, Q1.9 — mainly "oui" ↔ "oui_sous_conditions" variations
4. **Lowest strict scores**: Q1.9 (55.0), Q1.15 (56.7), Q1.1 (58.9) — these show variability in approach selection

### Component breakdown (average across questions):
- **Approach stability**: ~0.75 (mapped: ~0.75)
- **Applicability stability**: ~0.61 (loose: ~0.83)
- **Recommendation stability**: ~0.72 (loose: ~0.93)

### Canonical Label Mapping

The model uses different normalized_labels that are in fact semantically equivalent. The following mapping groups these variants under canonical labels:

| normalized_label | canonical_label |
|------------------|-----------------|
| cash_flow_hedge | cash_flow_hedge |
| fair_value_hedge | fair_value_hedge |
| intragroup_monetary_hedge | intragroup_monetary_hedge |
| net_investment_hedge | net_investment_hedge |

## Comparison of Top vs Low Performers

### Top Performers (loose score = 100.0)

| Question | Runs | Score | Score (loose) | Top Chunk | Low Chunk |
|----------|------|-------|---------------|-----------|-----------|
| Q1.11 | 3 | 76.7 | 100.0 | 0.6746 | 0.6056 |
| Q1.14 | 3 | 76.7 | 100.0 | 0.6376 | 0.5564 |
| Q1.16 | 3 | 100.0 | 100.0 | 0.6406 | 0.5645 |
| Q1.17 | 3 | 100.0 | 100.0 | 0.6447 | 0.5636 |

### Low Performers (loose score < 70)

| Question | Runs | Score | Score (loose) | Top Chunk | Low Chunk |
|----------|------|-------|---------------|-----------|-----------|
| Q1.15 | 3 | 56.7 | 56.7 | 0.6069 | 0.5275 |

### Key Observations
- **Top performers avg top chunk**: 0.6494
- **Low performers avg top chunk**: 0.6069

The gap between top and low performers correlates with retrieval quality — questions with higher top chunk scores tend to produce more stable outputs.

## Aggregate Metrics (across all 68 runs, treating each run equally)

| Component | Strict | Loose |
|-----------|--------|-------|
| **Score** | **84.3** | **92.7** |
| Approach (Jaccard) | 0.8246 | 0.8371 |
| Applicability | 0.8059 | 0.9455 |
| Recommendation | 0.8126 | 1.0000 |

| Retrieval Metric | Value |
|-----------------|-------|
| Avg Top Score | 0.6243 |
| Avg Low Score | 0.5495 |

**Interpretation:**
- **Strict**: Uses exact matching for all fields (approach labels, applicability values, recommendation answers)
- **Loose**: Treats "oui" and "oui_sous_conditions" as equivalent for applicability, recommendation, and maps semantic label variants to canonical forms

The 8-point gap between strict (84.3) and loose (92.7) confirms that most instability comes from variations between "oui" and "oui_sous_conditions" rather than fundamental disagreements about approach selection.

**Component-level insights:**
- **Recommendation loose (100%)** is perfect — the model always gives the same directional answer (positive vs negative)
- **Approach stability (~83%)** is high — the model consistently selects the same accounting treatments
- **Applicability strict (81%)** vs loose (95%) shows some variance in whether conditions apply

## Label Frequency by Question

| normalized_label | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1 | Q1.6 | Q1.7 | Q1.8 | Q1.9 | Q1.10 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Q1.15 | Q1.16 | Q1.17 | Q1.18 | Q1.19 | Q1.20 | Q1.21 | Q1.22 | Total |
|------------------|------|------|------|------|------|-----|------|------|------|------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|------|
| cash_flow_hedge | 3 | 2 | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 2 | 2 | 3 | 2 | 1 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 58 |
| fair_value_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 67 |
| intragroup_monetary_hedge | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| net_investment_hedge | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |

### Observations

- **Experiment 07** retrieved more diverse labels (10 different labels) including analysis-only approaches like `cartographie_des_entites_et_devises_fonctionnelles` and various hedge variants
- **Experiment 08** retrieves fewer, more focused labels (only 4) — `fair_value_hedge`, `cash_flow_hedge`, `net_investment_hedge`, and `intragroup_monetary_hedge`
- `net_investment_hedge` appears only in Q1.1 and Q1.2 (4 runs total) — the tight prompts have eliminated it for most other questions
- `intragroup_monetary_hedge` appears only once (Q1.15) — this is a spurious label not related to hedge accounting for this question

## Next Steps
- Investigate why `net_investment_hedge` is not being retrieved for most questions and rerun a new round of experiments
