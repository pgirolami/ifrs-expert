# 2026-03-26

# Goal
This experiment addresses the problem uncovered in experiment 08: the model prematurely narrowed to the most immediately applicable accounting treatment, losing credible alternatives that should have been evaluated.

In experiment 09, we changed Prompt B to first extract all candidate approaches, then evaluate applicability for each — rather than just evaluating applicability on a pre-narrowed set.

This experiment was interrupted before the end because NIH still wasn't being surfaced enough.

# Analysis of results

## Summary

| Metric | Value (per-question avg) | Value (aggregate loose) |
|--------|-------------------------|----------------------|
| **Average Strict Score** | **80.9** | 78.4 |
| **Average Loose Score** | **89.7** | 89.3 |
| **Questions Analyzed** | 7 | 7 |
| **Total Runs** | 21 | 21 |

> Note: Q1.15 had no valid runs and was excluded.

## Detailed Results

| Question | Runs | Strict Score | Loose Score | Approach (orig) | Approach (mapped) | Applicability | Applicability (loose) | Recommendation |
|----------|------|-------------|-------------|-----------------|-------------------|---------------|----------------------|----------------|
| Q1.1 | 3 | **93.3** | **93.3** | 1.00 | 1.00 | 0.78 | 0.78 | 1.00 |
| Q1.0 | 3 | **90.0** | **90.0** | 1.00 | 1.00 | 0.67 | 0.67 | 1.00 |
| Q1.14 | 3 | **90.0** | **90.0** | 1.00 | 1.00 | 0.67 | 0.67 | 1.00 |
| Q1.10 | 3 | **82.2** | **82.2** | 0.78 | 0.78 | 0.67 | 0.67 | 1.00 |
| Q1.12 | 3 | **82.2** | **82.2** | 0.78 | 0.78 | 0.67 | 0.67 | 1.00 |
| Q1.13 | 3 | **66.7** | **100.0** | 1.00 | 1.00 | 0.33 | 1.00 | 0.33 |
| Q1.11 | 3 | **61.7** | **90.0** | 1.00 | 1.00 | 0.17 | 1.00 | 0.33 |

## Interpretation

- **Score (strict)**: 80.9 average (aggregate: 78.4) — measures exact consistency in approaches, applicability values, and recommendations
- **Score (loose)**: 89.7 average (aggregate: 89.3) — treats "oui" and "oui_sous_conditions" as equivalent

### Key observations:
1. **3 questions achieve perfect approach stability (1.00)**: Q1.1, Q1.0, Q1.14, Q1.13
2. **Lower than experiment 08**: 80.9 vs 85.4 (strict), 89.7 vs 93.0 (loose)
3. **Loose score significantly higher than strict** for Q1.13 (66.7 → 100.0), Q1.11 (61.7 → 90.0) — mainly "oui" ↔ "oui_sous_conditions" variations
4. **Lowest strict scores**: Q1.11 (61.7), Q1.13 (66.7) — these show variability in applicability evaluation
5. **Recommendation loose (100%)** is perfect — the model always gives the same directional answer

### Component breakdown (average across questions):
- **Approach stability**: ~0.94 (mapped: ~0.94)
- **Applicability stability**: ~0.55 (loose: ~0.79)
- **Recommendation stability**: ~0.74 (loose: ~1.00)

## Comparison with Experiment 08

| Metric | Exp 08 | Exp 09 | Delta |
|--------|--------|--------|-------|
| Strict Score (avg) | 85.4 | 80.9 | -4.5 |
| Loose Score (avg) | 93.0 | 89.7 | -3.3 |
| Approach Stability | 0.75 | 0.94 | +0.19 |
| Applicability Stability | 0.61 | 0.55 | -0.06 |
| Recommendation Stability | 0.72 | 0.74 | +0.02 |

**Analysis:**
- Experiment 09 has **higher approach stability** (0.94 vs 0.75) — the model is more consistent in selecting approaches
- But **lower overall scores** because applicability stability dropped
- The trade-off: more candidate approaches = more to evaluate = more variance in applicability judgments

## Aggregate Metrics (across all 21 runs, treating each run equally)

| Component | Strict | Loose |
|-----------|--------|-------|
| **Score** | **78.4** | **89.3** |
| Approach (Jaccard) | 0.8730 | 0.8730 |
| Applicability | 0.6000 | 0.7905 |
| Recommendation | 0.7429 | 1.0000 |

| Retrieval Metric | Value |
|-----------------|-------|
| Avg Top Score | 0.6244 |
| Avg Low Score | 0.5514 |

**Interpretation:**
- **Strict**: Uses exact matching for all fields (approach labels, applicability values, recommendation answers)
- **Loose**: Treats "oui" and "oui_sous_conditions" as equivalent for applicability, recommendation, and maps semantic label variants to canonical forms

The 11-point gap between strict (78.4) and loose (89.3) confirms that most instability comes from variations between "oui" and "oui_sous_conditions" rather than fundamental disagreements about approach selection.

**Component-level insights:**
- **Recommendation loose (100%)** is perfect — the model always gives the same directional answer (positive vs negative)
- **Approach stability (~87%)** is high — the model consistently selects the same accounting treatments
- **Applicability strict (60%)** vs loose (79%) shows significant variance in whether conditions apply

## Label Frequency by Question

| normalized_label | Q1.0 | Q1.1 | Q1.10 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Total |
|------------------|------|------|-------|-------|-------|-------|-------|------|
| cash_flow_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| fair_value_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 21 |
| net_investment_hedge | 0 | 3 | 1 | 0 | 1 | 0 | 0 | 5 |

### Observations

- **Only 3 unique labels** (vs 4 in experiment 08) — `cash_flow_hedge`, `fair_value_hedge`, `net_investment_hedge`
- `net_investment_hedge` appears more frequently than in experiment 08 (5 vs 4), appearing in Q1.1, Q1.10, Q1.12
- All runs consistently retrieve both `cash_flow_hedge` and `fair_value_hedge` (21/21 each)
- The new approach evaluation prompts are extracting more consistent approach sets

## Comparison: Top vs Low Performers

### Top Performers (strict score >= 85)

| Question | Runs | Score | Score (loose) | Top Chunk | Low Chunk |
|----------|------|-------|---------------|-----------|-----------|
| Q1.1 | 3 | 93.3 | 93.3 | - | - |
| Q1.0 | 3 | 90.0 | 90.0 | - | - |
| Q1.14 | 3 | 90.0 | 90.0 | - | - |

### Low Performers (strict score < 70)

| Question | Runs | Score | Score (loose) | Top Chunk | Low Chunk |
|----------|------|-------|---------------|-----------|-----------|
| Q1.11 | 3 | 61.7 | 90.0 | - | - |
| Q1.13 | 3 | 66.7 | 100.0 | - | - |

### Key Observations
- Q1.11 and Q1.13 have low applicability stability (0.17 and 0.33 respectively)
- These questions show high variance in whether conditions apply to the approaches
- The loose score is much higher, indicating the model consistently says "yes" but sometimes with conditions
- NIH still not surfaced consistently

- Discussion with LLM regarding why NIH wasn't surfaced consistently uncovered the following ideas
    - updating the prompt to constrain approach discovery less
    - constraining approach discovery to the retrieved chunks only, without the question
    - splitting prompt A into two passes to combine these ideas

## Next Steps
- Rework prompt A to surface NIH

- A good next experiment would be to compare three Prompt A variants on the same benchmark:
    - current question-sensitive version
    - question-light, document-led version
    - later, the two-pass version