# 2026-03-26

# Goal
This experiment attempts to improve recall and consistency by modifying how the model recalls accounting treatments from the IFRS standards. The key change was to ensure the model consistently extracts the full set of applicable IFRS/IAS/IFRIC references for each approach.


# Analysis of results

## Label Frequency by Question

| normalized_label | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.10 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Q1.15 | Q1.16 | Q1.17 | Q1.18 | Q1.19 | Q1.20 | Q1.21 | Q1.22 | Total |
|------------------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| cash_flow_hedge | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 2 | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 53 |
| fair_value_hedge | 3 | 3 | 2 | 3 | 3 | 3 | 2 | 3 | 3 | 3 | 1 | 2 | 3 | 3 | 2 | 3 | 3 | 2 | 3 | 50 |
| net_investment_hedge | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 51 |
| intragroup_monetary_hedge | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 2 | 8 |
| risk_component_hedge | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 3 | 7 |
| forecast_intragroup_hedge | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 3 |
| monetary_item_hedge | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| risk_component_designation | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 4 |
| fx_profit_or_loss | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| entire_item_designation | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| forecast_cash_flow_hedge | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| forecast_transaction_hedge | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| ias_39_hedge | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |

### Observations
- **13 unique labels** — significantly more diverse than experiments 08 (4) and 09 (3)
- Core hedge labels remain: `cash_flow_hedge` (53), `fair_value_hedge` (50), `net_investment_hedge` (51)
- New labels appear: `forecast_intragroup_hedge`, `risk_component_designation`, `forecast_transaction_hedge`, `ias_39_hedge`
- The model is now extracting more varied and specific supposed accounting approaches but they are not accounting _approaches_: they are elements of the approaches. The prompt currently over-rewards extraction of any context-grounded IFRS construct that looks distinct, but it does not enforce a single abstraction level for the output: the LLM mixes true hedge accounting models with lower-level constructs such as hedged-item categories, designation forms, and scoped application variants.

## Detailed Results

| Question | Runs | Strict Score | Loose Score | Approach (orig) | Approach (mapped) | Applicability | Applicability (loose) | Recommendation |
|----------|------|-------------|-------------|-----------------|-------------------|---------------|----------------------|----------------|
| Q1.3 | 3 | **93.3** | **93.3** | 1.00 | 1.00 | 0.78 | 0.78 | 1.00 |
| Q1.22 | 3 | **87.6** | **87.6** | 0.64 | 0.72 | 1.00 | 1.00 | 1.00 |
| Q1.16 | 3 | **87.5** | **87.5** | 0.83 | 1.00 | 0.78 | 0.78 | 1.00 |
| Q1.19 | 3 | **87.5** | **87.5** | 0.83 | 0.83 | 0.78 | 0.78 | 1.00 |
| Q1.17 | 3 | **87.2** | **87.2** | 0.63 | 0.73 | 1.00 | 1.00 | 1.00 |
| Q1.4 | 3 | **87.4** | **87.4** | 0.64 | 0.64 | 1.00 | 1.00 | 1.00 |
| Q1.0 | 3 | **83.9** | **83.9** | 0.78 | 0.78 | 0.72 | 0.72 | 1.00 |
| Q1.13 | 3 | **83.4** | **83.4** | 0.72 | 0.72 | 0.78 | 0.78 | 1.00 |
| Q1.2 | 3 | **80.8** | **80.8** | 0.67 | 0.67 | 0.75 | 0.75 | 1.00 |
| Q1.12 | 3 | **79.0** | **79.0** | 0.64 | 0.78 | 0.72 | 0.72 | 1.00 |
| Q1.11 | 3 | **80.0** | **100.0** | 1.00 | 1.00 | 0.78 | 1.00 | 0.33 |
| Q1.15 | 3 | **78.0** | **78.0** | 0.47 | 0.67 | 0.89 | 0.89 | 1.00 |
| Q1.18 | 3 | **78.0** | **78.0** | 0.47 | 0.67 | 0.89 | 0.89 | 1.00 |
| Q1.5 | 3 | **73.3** | **93.3** | 1.00 | 1.00 | 0.56 | 1.00 | 0.33 |
| Q1.14 | 3 | **72.0** | **72.0** | 0.20 | 0.50 | 1.00 | 1.00 | 1.00 |
| Q1.10 | 3 | **71.5** | **71.5** | 0.47 | 0.56 | 0.67 | 0.67 | 1.00 |
| Q1.1 | 3 | **70.0** | **93.3** | 1.00 | 1.00 | 0.44 | 1.00 | 0.33 |
| Q1.20 | 3 | **64.2** | **87.5** | 0.83 | 0.83 | 0.44 | 1.00 | 0.33 |
| Q1.21 | 3 | **58.3** | **78.3** | 0.67 | 0.78 | 0.44 | 1.00 | 0.33 |

> Note: Q1.6 had no valid runs and was excluded.

## Aggregate Metrics (across all 57 runs, treating each run equally)

| Component | Strict | Loose |
|-----------|--------|-------|
| **Score** | **77.0** | **83.1** |
| Approach (Jaccard) | 0.6675 | 0.6717 |
| Applicability | 0.7480 | 0.8181 |
| Recommendation | 0.8083 | 1.0000 |

| Retrieval Metric | Value |
|-----------------|-------|
| Avg Top Score | 0.6256 |
| Avg Low Score | 0.5518 |

## Interpretation

- **Score (strict)**: 77.0 aggregate — measures exact consistency in approaches, applicability values, and recommendations
- **Score (loose)**: 83.1 aggregate — treats "oui" and "oui_sous_conditions" as equivalent

### Key observations:
1. **Lower scores than experiments 08 and 09**: 77.0 vs 84.3 (exp 08) and 78.4 (exp 09)
2. **High label diversity (13 labels)** — model extracts more varied approaches but with lower consistency
3. **Loose score significantly higher than strict** for Q1.11, Q1.5, Q1.1, Q1.20, Q1.21 — mainly "oui" ↔ "oui_sous_conditions" variations
4. **Recommendation loose (100%)** is perfect — the model always gives the same directional answer

### Component breakdown (average across questions):
- **Approach stability**: ~0.67 (mapped: ~0.67)
- **Applicability stability**: ~0.75 (loose: ~0.82)
- **Recommendation stability**: ~0.81 (loose: ~1.00)

## Comparison with Experiment 09

| Metric | Exp 09 | Exp 10 | Delta |
|--------|--------|--------|-------|
| Strict Score (aggregate) | 78.4 | 77.0 | -1.4 |
| Loose Score (aggregate) | 89.3 | 83.1 | -6.2 |
| Approach Stability | 0.87 | 0.67 | -0.20 |
| Applicability Stability | 0.60 | 0.75 | +0.15 |
| Recommendation Stability | 0.74 | 0.81 | +0.07 |
| Unique Labels | 3 | 13 | +10 |

**Analysis:**
- Experiment 10 has **significantly more diverse labels** (13 vs 3) — the model is now extracting many more hedge accounting variants but that is incorrect.
- However, **approach stability dropped** (0.67 vs 0.87) — with more labels, consistency suffers
- **Applicability stability improved** (0.75 vs 0.60) — the model is more consistent in evaluating applicability
- **Overall lower loose score** — the diversity trade-off resulted in less stable outputs
- The key question: is the extra label diversity valuable enough to justify the stability loss?

## Comparison: Top vs Low Performers

### Top Performers (strict score >= 85)

| Question | Runs | Score | Score (loose) |
|----------|------|-------|---------------|
| Q1.3 | 3 | 93.3 | 93.3 |
| Q1.22 | 3 | 87.6 | 87.6 |
| Q1.16 | 3 | 87.5 | 87.5 |
| Q1.19 | 3 | 87.5 | 87.5 |
| Q1.17 | 3 | 87.2 | 87.2 |
| Q1.4 | 3 | 87.4 | 87.4 |

### Low Performers (strict score < 70)

| Question | Runs | Score | Score (loose) |
|----------|------|-------|---------------|
| Q1.21 | 3 | 58.3 | 78.3 |
| Q1.20 | 3 | 64.2 | 87.5 |
| Q1.1 | 3 | 70.0 | 93.3 |

### Key Observations
- Top performers (Q1.3, Q1.22, Q1.16, Q1.19, Q1.17, Q1.4) have high recommendation stability (1.00)
- Low performers (Q1.21, Q1.20, Q1.1) have low recommendation stability (0.33) — the model flips on the final answer
- The large loose score gaps for low performers indicate the core answer is consistent ("oui"/"non") but conditions vary

## Next Steps
- Update the prompt again to keep `net_investment_hedge` recall without all the extraneous supposed approaches identified above