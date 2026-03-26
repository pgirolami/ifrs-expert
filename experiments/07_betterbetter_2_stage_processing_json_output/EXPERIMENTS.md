# 2026-03-25

# Scope
New versions of Prompt A and Prompt B because didn't yet solve the issue I was trying to solve in experiment 06

# Analysis result

## Summary

| Metric | Value (per-question avg) | Value (aggregate loose) |
|--------|-------------------------|----------------------|
| **Average Strict Score** | **51.3** | 54.2 |
| **Average Loose Score** | **71.1** | 77.4 |
| **Questions Analyzed** | 15 | 15 |
| **Total Runs** | 43 | 43 |

> Note: The per-question averages (51.3 strict, 71.1 loose) are computed by averaging each question's score. The aggregate values (54.2 strict, 77.4 loose) treat each of the 43 runs as equal, computing pairwise similarity across all runs.

## Detailed Results

| Question | Runs | Strict Score | Loose Score | Approach (orig) | Approach (canonical) | Applicability | Applicability (loose) | Recommendation |
|----------|------|-------------|-------------|-----------------|---------------------|----------------|----------------------|----------------|
| Q1.20 | 3 | **90.0** | **100.0** | 1.00 | 1.00 | 0.67 | 1.00 | 1.00 |
| Q1.11 | 3 | **66.7** | **100.0** | 1.00 | 1.00 | 0.33 | 1.00 | 0.33 |
| Q1.12 | 3 | **66.7** | **100.0** | 1.00 | 1.00 | 0.33 | 1.00 | 0.33 |
| Q1.14 | 3 | **66.7** | **100.0** | 1.00 | 1.00 | 0.33 | 1.00 | 0.33 |
| Q1.16 | 3 | **66.7** | **100.0** | 1.00 | 1.00 | 0.33 | 1.00 | 0.33 |
| Q1.1 | 3 | **58.9** | **92.2** | 0.78 | 0.78 | 0.33 | 1.00 | 0.33 |
| Q1.13 | 3 | **56.7** | **56.7** | 0.33 | 0.67 | 0.33 | 0.33 | 1.00 |
| Q1.17 | 3 | **56.7** | **56.7** | 0.33 | 0.67 | 0.33 | 0.33 | 1.00 |
| Q1.21 | 3 | **38.3** | **56.7** | 0.33 | 0.67 | 0.17 | 0.67 | 0.33 |
| Q1.2 | 3 | **34.6** | **34.6** | 0.08 | 0.22 | 0.33 | 0.33 | 0.33 |
| Q1.10 | 3 | **33.3** | **56.7** | 0.33 | 0.67 | 0.00 | 0.33 | 0.33 |
| Q1.15 | 3 | **33.3** | **56.7** | 0.33 | 0.67 | 0.00 | 0.33 | 0.33 |
| Q1.19 | 3 | **27.5** | **50.8** | 0.17 | 0.33 | 0.00 | 0.33 | 0.33 |
| Q1.18 | 3 | **21.7** | **35.0** | 0.00 | 0.44 | 0.00 | 0.44 | 0.33 |

## Failure analysis
### Canonical Label Mapping

The model uses different normalized_labels that are in fact semantically equivalent. The following mapping groups these variants under canonical labels and is used to define "loose" scoring:

| normalized_label | canonical_label |
|------------------|-----------------|
| fair_value_hedge | fair_value_hedge |
| cash_flow_hedge | cash_flow_hedge |
| net_investment_hedge | net_investment_hedge |
| foreign_currency_hedge | cash_flow_hedge |
| foreign_currency_component_hedge | cash_flow_hedge |
| intragroup_monetary_hedge | cash_flow_hedge |
| monetary_item_hedge | cash_flow_hedge |
| cartographie_des_entites_et_devises_fonctionnelles | analysis_only |
| choix_entre_creance_de_dividende_et_couverture_d_investissement_net | analysis_only |
| qualification_du_solde_comme_reglement_proche_ou_investissement_net | analysis_only |


### Interpretation

- **Strict Score**: Uses exact matching for all fields:
  - Approach: original normalized_label from model (no canonical mapping)
  - Applicability: "oui" vs "oui_sous_conditions" vs "non" are all distinct
  - Recommendation: "oui" vs "oui_sous_conditions" vs "non" are all distinct
- **Loose Score**: Treats semantically equivalent items as the same:
  - Approach: maps variant labels to canonical forms (e.g., "monetary_item_hedge" → "cash_flow_hedge")
  - Applicability: "oui" and "oui_sous_conditions" are both treated as "positive"
  - Recommendation: "oui" and "oui_sous_conditions" are both treated as "positive"
- **Approach (orig)**: Jaccard similarity using raw normalized_label from model output
- **Approach (canonical)**: Jaccard similarity using canonical label mapping (groups semantically equivalent variants)

#### Key Findings

1. **Gap of ~20 points** between strict (51.3) and loose (71.1) scores indicates most instability comes from "oui" ↔ "oui_sous_conditions" variations
2. **Canonical approach stability** is significantly higher than original — the mapping substantially improves approach stability (e.g., Q1.18: 0.00→0.44, Q1.10: 0.33→0.67)
3. **Applicability (loose)** is much higher than strict applicability — most differences are "oui" vs "oui_sous_conditions", not "non" vs positive answers
4. **High performers** (Q1.20, Q1.11, Q1.12, Q1.14, Q1.16) show full stability on loose measure (100.0)
5. **Low performers** (Q1.18, Q1.19) still have lower canonical approach stability, suggesting genuinely different approach combinations
6. **Recommendation stability** is generally low (0.33), suggesting the model frequently flips between "oui" and "oui_sous_conditions"
7. **Q1.20** is the only question with high recommendation stability (1.00), indicating consistent final answer across all runs

## Possible Next Steps
1. **Tighten `answer_prompt_A.txt`** to extract only canonical accounting treatments (no decision or analysis steps) 

### Comparison of Top vs Low Performers

#### Top Retrieval Chunks by Question (Loose Score)

| Question | Runs | Top Score | Low Score | Loose Score |
|----------|------|-----------|-----------|-------------|
| Q1.11 (high) | 3 | 0.6746 | 0.6056 | 100.0 |
| Q1.20 (high) | 3 | 0.6545 | 0.5904 | 100.0 |
| Q1.19 (low) | 3 | 0.6450 | 0.5598 | 50.8 |
| Q1.18 (low) | 3 | 0.6027 | 0.5435 | 35.0 |

#### IFRS 9 Retrieval Sections (non-expansion, alphabetical with scores)

| Question | Section | Score |
|----------|---------|-------|
| Q1.11 | 6.3.5 | 0.6746 |
| Q1.11 | 6.3.6 | 0.6593 |
| Q1.11 | B6.3.3 | 0.6056 |
| Q1.11 | B6.3.5 | 0.6576 |
| Q1.11 | B6.3.6 | 0.6723 |
| Q1.19 | 6.3.6 | 0.6450 |
| Q1.19 | B4.3.4 | 0.5763 |
| Q1.19 | B6.3.3 | 0.5773 |
| Q1.19 | B6.3.5 | 0.6392 |
| Q1.19 | B6.3.6 | 0.6009 |

#### IFRIC 16 Retrieval Sections (non-expansion, alphabetical with scores)

| Question | Section | Score |
|----------|---------|-------|
| Q1.11 | 13 | 0.6633 |
| Q1.11 | 14 | 0.6211 |
| Q1.11 | 5 | 0.6560 |
| Q1.11 | AG4 | 0.6181 |
| Q1.11 | AG7 | 0.6201 |
| Q1.19 | 13 | 0.5956 |
| Q1.19 | 14 | 0.5664 |
| Q1.19 | 5 | 0.5925 |
| Q1.19 | 7 | 0.5598 |
| Q1.19 | 9 | 0.5898 |

#### Key Observations

1. **Q1.11 vs Q1.19 comparison**:
   - **Q1.11** retrieves 6.3.5 (the critical intragroup monetary item exception) with the highest score (0.6746)
   - **Q1.19** does NOT retrieve 6.3.5 in the top chunks — it only appears in expansion (score=0)
   - Q1.19 retrieves B4.3.4 (irrelevant impairment section) in the top 5, which may confuse the model
   - IFRIC 16: Q1.11 gets higher scores on all sections (0.66-0.62) vs Q1.19 (0.60-0.56)

2. **Question wording impact**: Q1.11 ("peut-elle être couverte") vs Q1.19 ("éligible à la comptabilité de couverture") may have different semantic alignment with the core sections

3. **Cascade effect**: Even though 6.3.5 IS present in expansion for Q1.19, the LLM may not weight it as heavily when generating Prompt A output, leading to weaker assumptions and unstable Prompt B outputs

## Aggregate Metrics (across all 43 runs, treating each run equally)

| Component | Strict | Loose |
|-----------|--------|-------|
| **Score** | **54.2** | **77.4** |
| Approach (Jaccard) | 0.5533 | 0.7231 |
| Applicability | 0.3040 | 0.5991 |
| Recommendation | 0.5360 | 0.9535 |

| Retrieval Metric | Value |
|-----------------|-------|
| Avg Top Score | 0.6295 |
| Avg Low Score | 0.5528 |

**Interpretation:**
- **Strict**: Uses exact matching for all fields (approach labels, applicability values, recommendation answers)
- **Loose**: Treats "oui" and "oui_sous_conditions" as equivalent for applicability, recommendation, and maps semantic label variants to canonical forms

The 23-point gap between strict (54.2) and loose (77.4) confirms that most instability comes from variations between "oui" and "oui_sous_conditions" rather than fundamental disagreements about approach selection.

**Component-level insights:**
- **Recommendation loose (95%)** is nearly perfect — the model almost always gives the same directional answer (positive vs negative)
- **Applicability strict (30%)** is very low — the model frequently disagrees on whether conditions apply
- **Approach strict (55%)** vs canonical (72%) shows significant label variation but decent semantic agreement

## Next Steps

1. **Investigate retrieval tuning**: The min-score=0.5 threshold may be too permissive — consider increasing to 0.6 to filter out marginal matches
2. **Check question similarity**: Q1.18 and Q1.19 may have different semantic patterns that don't align well with the core hedge sections (6.3.5, 6.3.6)
3. **Prompt A refinement**: The prompt may need explicit instructions to prioritize the intragroup monetary item exception (6.3.5) over detailed hedge mechanics
4. **Try different k values**: Some questions may benefit from fewer chunks (k=3) vs more chunks (k=10)

## Label Frequency by Question

| normalized_label | Q1.1 | Q1.2 | Q1.10 | Q1.11 | Q1.12 | Q1.13 | Q1.14 | Q1.15 | Q1.16 | Q1.17 | Q1.18 | Q1.19 | Q1.20 | Q1.21 | Q1.22 | Total |
|------------------|------|------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|------|
| cartographie_des_entites_et_devises_fonctionnelles | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| cash_flow_hedge | 3 | 1 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 1 | 1 | 3 | 2 | 1 | 32 |
| choix_entre_creance_de_dividende_et_couverture_d_investissement_net | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| fair_value_hedge | 3 | 1 | 2 | 3 | 3 | 2 | 3 | 2 | 3 | 2 | 1 | 2 | 3 | 2 | 1 | 33 |
| foreign_currency_component_hedge | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| foreign_currency_hedge | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| intragroup_monetary_hedge | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 3 |
| monetary_item_hedge | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 4 |
| net_investment_hedge | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 4 |
| qualification_du_solde_comme_reglement_proche_ou_investissement_net | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |