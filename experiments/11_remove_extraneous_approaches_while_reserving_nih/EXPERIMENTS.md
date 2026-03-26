# 2026-03-26

# Goal
Preserving broad recall of relevant IFRS models while preventing the model from mixing true accounting approaches with subordinate features that belong in the later applicability step. This experiment analyzes the consistency of approaches surfaced in Prompt A (before evaluating applicability).

# Analysis of results

## Label Frequency by Question

| normalized_label | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Q1.8 | Q1.9 | Q1.10 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Q1.15 | Q1.16 | Q1.17 | Q1.18 | Q1.19 | Q1.20 | Q1.21 | Q1.22 | Total |
|------------------|------|------|------|------|------|------|------|------|------|------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|------|
| cash_flow_hedge | 3 | 3 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 68 |
| fair_value_hedge | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 67 |
| net_investment_hedge | 3 | 3 | 3 | 3 | 1 | 2 | 3 | 3 | 3 | 1 | 2 | 3 | 3 | 1 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 61 |
| foreign_currency_translation | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| foreign_exchange_recognition | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| hedge_accounting | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |

### Observations
- **Only 4 unique labels** (ignoring spurious single-occurrence ones) — extremely focused: `cash_flow_hedge`, `fair_value_hedge`, `net_investment_hedge`
- Very high consistency: `cash_flow_hedge` appears 68/69 runs, `fair_value_hedge` appears 67/69 runs, `net_investment_hedge` appears 61/69 runs
- Only 3 spurious labels appear once each: `foreign_currency_translation`, `foreign_exchange_recognition`, `hedge_accounting`
    - Q1.5 has 2 good runs and one really bad one which returns `foreign_currency_translation` and `hedge_accounting`
    - Q1.2 has 1 run with `foreign_exchange_recognition`
- This is the most focused experiment yet — similar to experiment 08 but with even cleaner results

## Detailed Results

| Question | Runs | Approach Stability | Avg Approaches |
|----------|------|-------------------|----------------|
| Q1.0 | 3 | 1.00 | 3.0 |
| Q1.1 | 3 | 1.00 | 3.0 |
| Q1.2 | 3 | 0.67 | 3.0 |
| Q1.3 | 3 | 1.00 | 3.0 |
| Q1.4 | 3 | 0.78 | 2.3 |
| Q1.5 | 3 | 0.33 | 2.7 |
| Q1.6 | 3 | 1.00 | 3.0 |
| Q1.7 | 3 | 1.00 | 3.0 |
| Q1.8 | 3 | 1.00 | 3.0 |
| Q1.9 | 3 | 0.78 | 2.3 |
| Q1.10 | 3 | 0.78 | 2.7 |
| Q1.11 | 3 | 1.00 | 3.0 |
| Q1.12 | 3 | 1.00 | 3.0 |
| Q1.13 | 3 | 0.78 | 2.3 |
| Q1.14 | 3 | 1.00 | 3.0 |
| Q1.15 | 3 | 1.00 | 3.0 |
| Q1.16 | 3 | 1.00 | 3.0 |
| Q1.17 | 3 | 1.00 | 3.0 |
| Q1.18 | 3 | 1.00 | 3.0 |
| Q1.19 | 3 | 1.00 | 3.0 |
| Q1.20 | 3 | 1.00 | 3.0 |
| Q1.21 | 3 | 1.00 | 3.0 |
| Q1.22 | 3 | 1.00 | 3.0 |

> Note: This experiment analyzes Prompt A output (approach extraction) since Prompt B was not executed.

## Aggregate Metrics (across all 69 runs, treating each run equally)

| Component | Value |
|-----------|-------|
| **Approach Stability (Jaccard)** | **0.8963** |
| Avg Top Score | 0.6243 |
| Avg Low Score | 0.5495 |
| Total Runs | 69 |

## Interpretation

- **Approach stability**: 0.90 (aggregate) — very high consistency in the approaches the model surfaces
- **Average per-question stability**: 0.92 — 17 out of 23 questions have perfect stability (1.00)
- **Only 4 core labels** — extremely focused approach set

### Key observations:
1. **17 questions achieve perfect stability (1.00)** — the model consistently surfaces the same approaches
2. **Lowest stability**: Q1.5 (0.33), Q1.2 (0.67) — these show variability in approach selection
3. **Most stable questions**: Q1.0, Q1.1, Q1.3, Q1.6-Q1.22 — all with 1.00 stability
4. **Few spurious labels** — only 3 single-occurrence labels vs 10+ in previous experiments

### Component breakdown:
- **Approach stability**: ~0.92 average
- **Avg approaches per question**: ~2.9 (close to the 3 core hedge types)

## Comparison with Experiment 10

| Metric | Exp 10 | Exp 11 | Delta |
|--------|--------|--------|-------|
| Approach Stability | 0.67 | 0.90 | +0.23 |
| Unique Labels | 13 | 4 | -9 |
| Spurious Labels | 10+ | 3 | -7+ |
| Avg Approaches | ~2.5 | ~2.9 | +0.4 |

**Analysis:**
- Experiment 11 has **significantly higher approach stability** (0.90 vs 0.67) — the model is much more consistent
- **Far fewer unique labels** (4 vs 13) — focused on the core hedge accounting types
- **Fewer spurious labels** — only 3 single-occurrence ones vs 10+ in exp 10
- The approach of "removing extraneous approaches while reserving NIH" is working — it surfaces the 3 core hedge types consistently

## Comparison: Top vs Low Performers

### Top Performers (stability = 1.00)

| Question | Runs | Approach Stability | Avg Approaches |
|----------|------|-------------------|----------------|
| Q1.0 | 3 | 1.00 | 3.0 |
| Q1.1 | 3 | 1.00 | 3.0 |
| Q1.3 | 3 | 1.00 | 3.0 |
| Q1.6 | 3 | 1.00 | 3.0 |
| Q1.7 | 3 | 1.00 | 3.0 |
| Q1.8 | 3 | 1.00 | 3.0 |
| Q1.11 | 3 | 1.00 | 3.0 |
| Q1.12 | 3 | 1.00 | 3.0 |
| Q1.14 | 3 | 1.00 | 3.0 |
| Q1.15 | 3 | 1.00 | 3.0 |
| Q1.16 | 3 | 1.00 | 3.0 |
| Q1.17 | 3 | 1.00 | 3.0 |
| Q1.18 | 3 | 1.00 | 3.0 |
| Q1.19 | 3 | 1.00 | 3.0 |
| Q1.20 | 3 | 1.00 | 3.0 |
| Q1.21 | 3 | 1.00 | 3.0 |
| Q1.22 | 3 | 1.00 | 3.0 |

### Low Performers (stability < 0.80)

| Question | Runs | Approach Stability | Avg Approaches |
|----------|------|-------------------|----------------|
| Q1.5 | 3 | 0.33 | 2.7 |
| Q1.2 | 3 | 0.67 | 3.0 |
| Q1.4 | 3 | 0.78 | 2.3 |
| Q1.9 | 3 | 0.78 | 2.3 |
| Q1.10 | 3 | 0.78 | 2.7 |
| Q1.13 | 3 | 0.78 | 2.3 |

### Key Observations
- **17/23 questions (74%) have perfect stability** — the model is highly consistent
- **Low performers** tend to have slightly fewer approaches (~2.3-2.7 vs 3.0) — sometimes missing one of the three core hedge types
- **Q1.5 is an outlier** with only 0.33 stability — significant variability in which approaches are surfaced

## Next Steps
- This approach is now good enough, the next step is to test the pipeline on other questions