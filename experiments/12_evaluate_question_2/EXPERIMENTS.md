# 2026-03-27

# Goal

Evaluate whether correctness and stability achieved on initial question transfers to 2 new questions still related to IFRS 9.

## Analysis of results

### Observations
- **4 unique labels** (after canonicalization) — the model surfaces the 3 core classification approaches: `amortised_cost`, `fair_value_oci`, `fair_value_pl`
- The model uses slightly different label variations across runs (e.g., `fair_value_pl` vs `fair_value_profit_loss` vs `fair_value_pnl`) but these map to the same canonical forms
- Very high applicability and recommendation consistency: all runs return "oui_sous_conditions" for all three approaches

### Label Variants (before canonicalization)

| Canonical | Variants |
|-----------|----------|
| amortised_cost | amortised_cost |
| fair_value_oci | fair_value_oci, fvoci_measurement |
| fair_value_pl | fair_value_pl, fair_value_profit_loss, fair_value_pnl, fvtpl_measurement |

### Label Frequency by Question

| normalized_label | Q2.0 | Q2.1 | Q2.2 | Q2.3 | Q2.4 | Total |
|------------------|------|------|------|------|------|-------|
| amortised_cost | 3 | 3 | 3 | 3 | 3 | 15 |
| fair_value_oci | 3 | 3 | 3 | 3 | 2 | 14 |
| fair_value_pl | 2 | 2 | 3 | 2 | 1 | 10 |
| fair_value_profit_loss | 1 | 1 | 0 | 1 | 2 | 5 |
| fair_value_pnl | 0 | 1 | 0 | 0 | 0 | 1 |
| fvtpl_measurement | 0 | 0 | 0 | 0 | 1 | 1 |
| fvoci_measurement | 0 | 0 | 0 | 0 | 1 | 1 |

> Note: All applicability values are "oui_sous_conditions" across all runs

## Detailed Results

| Question | Runs | Approach Stability | Approach (Canonical) | Applicability | Recommendation | Avg Approaches |
|----------|------|-------------------|---------------------|---------------|----------------|----------------|
| Q2.0 | 3 | 0.67 | 1.00 | 1.00 | 1.00 | 3.0 |
| Q2.1 | 3 | 0.50 | 1.00 | 1.00 | 1.00 | 3.0 |
| Q2.2 | 3 | 1.00 | 1.00 | 1.00 | 1.00 | 3.0 |
| Q2.3 | 3 | 0.67 | 1.00 | 1.00 | 1.00 | 3.0 |
| Q2.4 | 3 | 0.47 | 1.00 | 1.00 | 1.00 | 3.0 |

## Aggregate Metrics (across all 15 runs, treating each run equally)

| Component | Value |
|-----------|-------|
| **Approach Stability (Jaccard, Original)** | **0.6314** |
| **Approach Stability (Jaccard, Canonical)** | **1.0000** |
| Applicability Stability | 1.0000 |
| Recommendation Stability | 1.0000 |
| Avg Top Score | 0.6326 |
| Avg Low Score | 0.0000 |
| Total Runs | 15 |

## Interpretation

- **Approach stability (canonical)**: 1.00 — after canonicalization, the model is perfectly consistent in the approaches it surfaces
- **Approach stability (original)**: 0.63 — there's some variability in how the model names the approaches across runs (e.g., `fair_value_pl` vs `fair_value_profit_loss`)
- **Applicability stability**: 1.00 — all runs correctly identify all three approaches as applicable "under conditions"
- **Recommendation stability**: 1.00 — the overall recommendation is consistent across all runs (oui_sous_conditions)
- **3 core approaches** per question — consistent with the hedge accounting experiment (Exp 11)

### Key observations:
1. **All questions achieve perfect canonical stability** — the model consistently surfaces the same 3 classification approaches
2. **Label naming variability** is the only source of instability — different runs use different but equivalent label variants
3. **Perfect applicability and recommendation consistency** — all runs agree on "oui_sous_conditions"
4. **Transfer of stability** — the correctness and stability patterns from the original questions (Exp 11) transfer well to these new questions

### Why canonical stability matters:
- The model correctly identifies the three core IFRS 9 classification approaches: amortised_cost, fair_value_oci, fair_value_pl
- The label variants are just syntactic differences — they all refer to the same accounting treatments
- This shows the model has learned the underlying concepts, not just specific label strings

## Comparison with Experiment 11 (Hedge Accounting)

| Metric | Exp 11 | Exp 12 | Delta |
|--------|--------|--------|-------|
| Approach Stability (Original) | 0.90 | 0.63 | -0.27 |
| Approach Stability (Canonical) | 0.90 | 1.00 | +0.10 |
| Applicability Stability | 0.83 | 1.00 | +0.17 |
| Recommendation Stability | 0.88 | 1.00 | +0.12 |
| Unique Labels (original) | 4 | 7 | +3 |
| Unique Labels (canonical) | 4 | 3 | -1 |

**Analysis:**
- Experiment 12 has **higher canonical approach stability** (1.00 vs 0.90) — the new questions are even more consistent after canonicalization
- **Higher applicability stability** (1.00 vs 0.83) — all new question runs agree perfectly on applicability
- **Higher recommendation stability** (1.00 vs 0.88) — recommendations are perfectly consistent
- The slight decrease in original stability is due to more label variants (7 vs 4), but these all map to the same 3 canonical forms
- The transfer is successful — the pipeline maintains (and even improves) stability on new questions

## Comparison: Top vs Low Performers

### Top Performers (canonical stability = 1.00)

All questions achieve perfect canonical stability.

### Low Performers (original stability < 0.70)

| Question | Runs | Approach Stability (Original) | Approach Stability (Canonical) | Avg Approaches |
|----------|------|--------------------------------|--------------------------------|----------------|
| Q2.4 | 3 | 0.47 | 1.00 | 3.0 |
| Q2.1 | 3 | 0.50 | 1.00 | 3.0 |
| Q2.0 | 3 | 0.67 | 1.00 | 3.0 |
| Q2.3 | 3 | 0.67 | 1.00 | 3.0 |

### Key Observations
- **All questions achieve perfect canonical stability** — the model is highly consistent in surfacing the correct approaches
- **Low performers** are only low due to label variant differences, not different approaches
- **Q2.2 is perfect** (1.00 on both original and canonical) — no label variation across runs

## Retrieval Quality

| Question | Top Chunk Score | Low Chunk Score |
|----------|-----------------|-----------------|
| Q2.0 | 0.6250 | 0.0000 |
| Q2.1 | 0.6350 | 0.0000 |
| Q2.2 | 0.6383 | 0.0000 |
| Q2.3 | 0.6317 | 0.0000 |
| Q2.4 | 0.6312 | 0.0000 |

- **Average top chunk score**: 0.6326 — consistent with previous experiments
- **Low chunk scores are 0** — this is expected as some chunks in the expansion have score 0 (they're from the "expanded" context)

## Next Steps
- Review with SME
- Test on more questions