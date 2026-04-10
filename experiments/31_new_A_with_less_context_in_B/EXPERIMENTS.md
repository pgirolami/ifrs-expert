# 2026-04-10

# Goal

Test a simpler, more generic approach to improve answer quality. Instead of explicit canonical-label guardrails (experiment 30), use a cleaner two-stage prompt design where:
- **Prompt A** identifies the accounting issue and classifies authority before selecting approaches
- **Prompt B** has explicit anti-abduction rules to prevent spurious approach labels

## What Changed from Experiment 30

### Prompt A: Issue-first approach

Added structured identification before approach selection:

```
1. Identify the primary accounting issue raised by the question.

2. Classify the provided context into:
   - primary authority: directly governs that accounting issue
   - supporting authority: constrains, modifies, clarifies, or provides a distinct alternative model relevant to that issue
   - peripheral authority: topically related but not relevant for identifying peer approaches within that issue

3. Using only primary and supporting authority, identify the relevant top-level accounting treatment families.

4. Map those treatment families to peer top-level accounting approaches.
```

This forces the model to first understand the accounting issue and classify authority before jumping to approaches.

### Prompt B: Anti-abduction rules

Replaced explicit label mapping with generic anti-abduction rules:

```
Approach constraints:
- Use exactly the approaches provided in <identified_approaches>
- Do not introduce any new approach
- Do not omit any identified approach
- Do not merge or split approaches
- Preserve the order of approaches
- Keep the scope of each approach unchanged
- Each approach represents a distinct accounting treatment already surfaced upstream

Do NOT introduce:
- sub-approaches
- variants
- components
- intermediate reasoning steps
- new candidate treatments
- new normalized labels
- fallback outcomes such as "absence of designation", "no accounting treatment" as separate approaches
```

And a "Composition rule" that teaches proper relationship reasoning:

```
Composition rule:
- Distinguish carefully between:
  - a baseline accounting treatment
  - an optional overlay or designation
  - an exception-driven treatment
  - a true alternative treatment
- Do NOT present a baseline treatment and the absence of an optional overlay as two separate approaches unless both are explicitly present in <identified_approaches>
- If the context presents a general rule and an exception that can coexist, explain how they relate rather than treating them as competing peer approaches
```

## Generated analysis artifacts

- [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md) — automated stability summary for experiment 31
- [`generated_promptfoo_analysis_experiment_30_reference.md`](./generated_promptfoo_analysis_experiment_30_reference.md) — automated reference summary for experiment 30
- [`spurious_approaches_vs_sections_matrix.html`](./spurious_approaches_vs_sections_matrix.html) — emitted-approach vs retrieved-section matrix

## Method

Commands run:

```bash
uv run python experiments/analysis/run_promptfoo_analysis.py \
  'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents' \
  --experiment 31_new_A_with_less_context_in_B \
  > experiments/31_new_A_with_less_context_in_B/generated_promptfoo_analysis.md

uv run python experiments/analysis/run_promptfoo_analysis.py \
  'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents' \
  --experiment 30_same_as_29_with_more_guardrails \
  > experiments/31_new_A_with_less_context_in_B/generated_promptfoo_analysis_experiment_30_reference.md

uv run python experiments/analysis/generate_spurious_approaches_sections_matrix.py \
  --experiment 31_new_A_with_less_context_in_B \
  --provider 'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents'
```

## Automated analysis of Experiment 31

From [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md) (corrected):

### Per-Question Results

| Question | Runs | Score | Score (loose) | Valid |
|---|---|---|---|---|
| Q1.0 | 3 | 100.0 | 100.0 | True |
| Q1.1 | 3 | 100.0 | 100.0 | True |
| Q1.2 | 3 | 86.7 | 86.7 | True |
| Q1.3 | 3 | 100.0 | 100.0 | True |
| Q1.4 | 3 | 80.0 | 80.0 | True |
| Q1.5 | 3 | 100.0 | 100.0 | True |
| Q1.6 | 3 | 100.0 | 100.0 | True |
| Q1.7 | 3 | 100.0 | 100.0 | True |
| **AVERAGE** |  | **95.8** | **95.8** |  |

### Detailed Breakdown

| Question | Approach (strict) | Approach (mapped) | Applic (strict) | Applic (loose) | Rec (strict) | Rec (loose) |
|----------|------------------:|-----------------:|----------------:|---------------:|-------------:|------------:|
| Q1.0 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.1 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.2 | 1.0000 | 1.0000 | 0.5556 | 0.5556 | 1.0000 | 1.0000 |
| Q1.3 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.4 | 1.0000 | 1.0000 | 0.7778 | 0.7778 | 0.3333 | 0.3333 |
| Q1.5 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.6 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.7 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

### Aggregate Metrics

| Component | Strict | Loose |
|-----------|-------:|------:|
| **Score** | **95.8** | **95.8** |
| Approach (Jaccard, exact labels) | 1.0000 | 1.0000 |
| Applicability (exact values) | 0.9167 | 0.9167 |
| Recommendation (exact values) | 0.9167 | 0.9167 |
| | | |
| Total Questions | 8 | |
| Total Runs | 24 | |

### Label Frequency by Question

All three hedge approaches appear in every run (24/24 = 100%):
- `cash_flow_hedge`: 24/24
- `fair_value_hedge`: 24/24  
- `net_investment_hedge`: 24/24

**Zero spurious labels.**

### Comparison: Top vs Low Performers

- **Top performers** (score >= 95): Q1.0, Q1.1, Q1.3, Q1.5, Q1.6, Q1.7 = **6/8 (75%)**
- **Low performers** (score < 80): none = **0/8 (0%)**

## Minimax 2.7 analysis

### 1. Experiment 30 vs Experiment 31 comparison

| Metric | Exp. 30 | Exp. 31 | Delta |
|--------|---------|---------|-------|
| Average Score | 97.2 | 95.8 | **-1.4** |
| Perfect Questions | 5/8 | 6/8 | +1 |
| Approach Stability | 0.9444 | 1.0000 | **+0.06** |
| Applicability Stability | 0.9722 | 0.9167 | -0.06 |
| Recommendation Stability | 1.0000 | 0.9167 | **-0.08** |

### 2. Key differences

**Experiment 31 (new approach) is better at:**
- Approach identification: 100% stability vs 94.4% in Exp. 30
- Zero spurious labels (Exp. 30 had 2 missing `net_investment_hedge` in Q1.4 and Q1.5)

**Experiment 31 is worse at:**
- Applicability consistency: slight drop on Q1.2 (0.56 vs 1.0)
- Recommendation consistency: major drop on Q1.4 (0.33 vs 1.0) — this is the main regression

### 3. Remaining imperfections

**Q1.2 (86.7):** Applicability instability
- Run 1: all three approaches `oui_sous_conditions`
- Run 2 & 3: `fair_value_hedge=oui_sous_conditions`, others `non`

**Q1.4 (80.0):** Recommendation split — this is the main issue
- Run 1 & 3: recommendation `oui_sous_conditions`
- Run 2: recommendation `non` (stability killer)
- Also has applicability inconsistency (0.78)

## Conclusion

**Experiment 31 achieves excellent approach identification with simpler prompts, but has a regression in recommendation stability on Q1.4.**

- **Pros:**
  - Perfect approach stability (100% vs 94.4%)
  - Zero spurious labels across all 24 runs
  - More top performers (75% vs 62%)
  - Simpler, more generic prompt design

- **Cons:**
  - Lower recommendation stability on Q1.4 (0.33)
  - Slight applicability drop on Q1.2

**Net assessment:** The simpler prompts are viable, with the recommendation instability on Q1.4 being the main area for improvement. The issue-first approach (Prompt A) and anti-abduction rules (Prompt B) are a good foundation.


The key improvement came from forcing the model to first identify the accounting issue, then classify authority, then identify treatment families, then map to peer top-level approaches. Preventing Prompt A from doing applicability reasoning was critical. A richer structured JSON artifact improved stability and created a natural way to filter context for Prompt B.

## Next steps

1. **Investigate Q1.4 recommendation split** — Understand why one run diverges to `non` while others say `oui_sous_conditions`

2. **Investigate Q1.2 applicability** — Understand why one run gives different applicability values

3. **Combine best of both** — Use Exp. 31's approach identification with Exp. 30's recommendation stability

