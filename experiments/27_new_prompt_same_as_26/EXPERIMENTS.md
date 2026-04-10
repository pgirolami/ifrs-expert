# 2026-04-10

# Goal

Sanity check after restructuring Prompt A to explicitly teach the LLM to break down the approach-identification task into explicit steps. This is a limited run (2 questions) to quickly validate whether the structured approach improves results.

## What Changed from Experiment 26

**Replaced the "approach-identification rules" section with a structured multi-step workflow:**

```
Your task to:

1. Identify the primary accounting issue raised by the question.

2. Classify the provided context into:
   - primary authority: directly governs that accounting issue
   - supporting authority: constrains, modifies, or provides a distinct alternative model relevant to that issue
   - peripheral authority: topically related but not relevant for identifying peer approaches

3. Using only primary and supporting authority, identify the relevant top-level accounting treatment families.

4. Map those treatment families to peer top-level accounting approaches.

Approach-identification rules:
- Output only approaches that are peers at the same level of abstraction.
- ...
- If a treatment family differs from another only because it adds a timing, scope, reporting-level, or fact-pattern qualifier, prefer the broader top-level accounting treatment unless the qualifier changes the accounting model itself.
```

**Key instruction:**
> "Use treatment families only as intermediate reasoning to determine the correct peer approach. Do not output both layers."
> "When treatment families and peer top-level accounting approaches are both identified, output only the peer top-level accounting approaches as the final approaches."

This explicitly teaches the LLM to:
1. First classify the context (primary vs supporting vs peripheral)
2. Then identify treatment families as intermediate reasoning
3. Finally map to peer approaches as the output

All other settings remain identical to experiment 26 (same retrieval settings, same section expansion, same model).

## Generated analysis artifacts

- [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md) — automated stability summary for experiment 27
- [`spurious_approaches_vs_sections_matrix.html`](./spurious_approaches_vs_sections_matrix.html) — emitted-approach vs retrieved-section matrix

## Automated analysis of Experiment 27

From [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md):

### Aggregate metrics

| Component | Strict | Loose |
|-----------|:------:|:-----:|
| **Score** | **90.0** | **100.0** |
| Approach stability | 1.0000 | 1.0000 |
| Applicability consistency | 0.8889 | 1.0000 |
| Recommendation consistency | 0.6667 | 1.0000 |
| Total questions | 2 | |
| Total runs | 6 | |

### Per-question results

| Question | Runs | Score | Score (loose) |
|----------|------|-------|---------------|
| Q1.0 | 3 | 100.0 | 100.0 |
| Q1.2 | 3 | 80.0 | 100.0 |
| **AVERAGE** |  | **90.0** | **100.0** |

### Label frequency

| Label | Q1.0 | Q1.2 | Total |
|-------|------|------|-------|
| cash_flow_hedge | 3 | 3 | 6 |
| fair_value_hedge | 3 | 3 | 6 |
| net_investment_hedge | 3 | 3 | 6 |

## My analysis

### 1. Dramatic improvement on both questions

Both questions achieved perfect loose scores (100.0). More importantly, the approach stability is perfect — all 6 runs emit exactly the same three labels: `cash_flow_hedge`, `fair_value_hedge`, `net_investment_hedge`.

### 2. Q1.0: perfect across all dimensions

Q1.0 achieved a perfect 100.0 strict score. This is a massive improvement from:
- Experiment 25: 59.3 loose
- Experiment 26: 100.0 loose (already improved)

The structured approach appears to have eliminated the taxonomy fracture that was causing variation in earlier experiments.

### 3. Q1.2: perfect loose score, but recommendation consistency issue

Q1.2 achieved a perfect 100.0 loose score, matching experiment 26. However, the strict score is 80.0 because recommendation consistency is only 0.3333 (strict). This means one of the three runs gave a different recommendation answer than the other two.

Looking at the breakdown:
- Approach stability: 1.0000 (perfect)
- Applicability strict: 0.7778 (some variation in applicability values)
- Recommendation strict: 0.3333 (one run differs on recommendation)

This suggests the structured approach fixed the approach identification problem, but there's still some variation in how the model assesses applicability or recommendation for these approaches.

### 4. Label cleanliness

The label frequency table shows only the three core hedge types, with zero spurious labels. This is the cleanest taxonomy yet:
- No `hedge_accounting` (generic)
- No `foreign_currency_accounting` (baseline treatment)
- No qualified labels like `forecast_transaction_hedge`

The intermediate step of classifying context appears to help the model avoid emitting wrong labels.

### 5. Comparison on the sanity check subset

| Question | Exp. 25 | Exp. 26 | Exp. 27 | Best Previous |
|----------|---------|---------|---------|--------------|
| Q1.0 | 59.3 | 100.0 | **100.0** | Exp. 26 |
| Q1.2 | 100.0 | 59.2 | **100.0** | Exp. 25/27 |

Experiment 27 achieved the best loose score on both questions:
- Q1.0: matches Exp. 26's perfect score
- Q1.2: recovers from Exp. 26's collapse back to perfect

### 6. Approach is stable, but recommendation/applicability still varies

The perfect approach stability (1.0) shows the structured approach is highly consistent at identifying the correct taxonomy. However:
- Applicability strict: 0.8889
- Recommendation strict: 0.6667

This suggests the next improvement opportunity is in how the model assesses individual approaches, not just which approaches it identifies.

## Conclusion

The structured approach to prompt design produced **dramatic improvement**:

- Perfect approach stability on both questions
- Both questions achieved 100.0 loose score
- Zero spurious labels — only the correct three hedge types
- Recovered Q1.2 from Exp. 26's collapse

The key insight is that explicitly teaching the LLM to classify context first (primary vs supporting vs peripheral authority) before identifying treatment families produces more consistent results than relying on the model to do this implicitly.

**The structured approach is a clear win for approach identification.**

## Next steps

1. **Run the full Q1 set** with this prompt to see if the improvement generalizes.

2. **Investigate the recommendation/applicability variation** in Q1.2 — the structured approach may need similar explicit steps for the applicability assessment phase.

3. **Consider extending the structure to Prompt B** (applicability assessment) with similar explicit steps.

## Human analysis

The structured approach worked better than expected. By making the intermediate reasoning steps explicit:

1. **Context classification** (primary vs supporting vs peripheral) forces the model to distinguish between authoritative sources and noise before attempting approach identification.

2. **Treatment family identification** as a separate step gives the model a chance to group similar approaches before deciding which are "peers."

3. **The explicit "do not output both layers" instruction** prevents the model from emitting both intermediate and final labels.

A potential refinement for future experiments:
```
5. For each final approach, assess:
   - Is the approach applicable given the specific fact pattern?
   - What is the recommended accounting treatment?
   - Are there any conditions or qualifications that affect applicability?
```

This would extend the structured approach to the applicability assessment phase.
