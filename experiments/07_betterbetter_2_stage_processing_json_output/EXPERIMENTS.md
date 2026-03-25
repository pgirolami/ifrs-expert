# 2026-03-25

# Scope
New versions of Prompt A and Prompt B because didn't yet solve the issue I was trying to solve in experiment 06

# Analysis result

## Summary

| Metric | Value |
|--------|-------|
| **Average Strict Score** | **51.3** |
| **Average Loose Score** | **71.1** |
| **Questions Analyzed** | 14 |
| **Skipped (insufficient runs)** | 1 (Q1.22) |

## Detailed Results

| Question | Runs | Strict Score | Loose Score | Approach | Applicability | Recommendation |
|----------|------|-------------|-------------|----------|---------------|----------------|
| Q1.20 | 3 | **90.0** | **100.0** | 1.00 | 0.67 | 1.00 |
| Q1.11 | 3 | **66.7** | **100.0** | 1.00 | 0.33 | 0.33 |
| Q1.12 | 3 | **66.7** | **100.0** | 1.00 | 0.33 | 0.33 |
| Q1.14 | 3 | **66.7** | **100.0** | 1.00 | 0.33 | 0.33 |
| Q1.16 | 3 | **66.7** | **100.0** | 1.00 | 0.33 | 0.33 |
| Q1.1 | 3 | **58.9** | **92.2** | 0.78 | 0.33 | 0.33 |
| Q1.13 | 3 | **56.7** | **56.7** | 0.33 | 0.33 | 1.00 |
| Q1.17 | 3 | **56.7** | **56.7** | 0.33 | 0.33 | 1.00 |
| Q1.21 | 3 | **38.3** | **56.7** | 0.33 | 0.17 | 0.33 |
| Q1.2 | 3 | **34.6** | **34.6** | 0.08 | 0.33 | 0.33 |
| Q1.10 | 3 | **33.3** | **56.7** | 0.33 | 0.00 | 0.33 |
| Q1.15 | 3 | **33.3** | **56.7** | 0.33 | 0.00 | 0.33 |
| Q1.19 | 3 | **27.5** | **50.8** | 0.17 | 0.00 | 0.33 |
| Q1.18 | 3 | **21.7** | **35.0** | 0.00 | 0.00 | 0.33 |

## Interpretation

- **Strict Score**: Uses exact matching for applicability ("oui" vs "oui_sous_conditions") and recommendation ("oui" vs "oui_sous_conditions")
- **Loose Score**: Treats "oui" and "oui_sous_conditions" as equivalent, only distinguishing "non" from positive answers

### Key Findings

1. **Gap of ~20 points** between strict (51.3) and loose (71.1) scores indicates most instability comes from "oui" ↔ "oui_sous_conditions" variations
2. **High performers** (Q1.20, Q1.11, Q1.12, Q1.14, Q1.16) show full stability on loose measure (100.0)
3. **Low performers** (Q1.18, Q1.19) have near-zero approach stability, indicating completely different approaches chosen across runs
4. **Recommendation stability** is generally low (0.33), suggesting the model frequently flips between "oui" and "oui_sous_conditions"
5. **Q1.20** is the only question with high recommendation stability (1.00), indicating consistent final answer across all runs