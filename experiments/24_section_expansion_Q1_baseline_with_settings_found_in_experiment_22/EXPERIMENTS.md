# 2026-04-09

# Goal

Test whether expanding retrieved chunks to their whole section improves the Q1 baseline from experiment 23 while keeping the document-first retrieval settings found in experiment 22.

Concretely:
- rerun Q1 with `openai-codex`
- keep document-mode retrieval
- switch to `expand-to-section=true` with `expand=0`
- compare the resulting behavior to experiment 23

> Note: the recorded Promptfoo run is incomplete. The available artifacts only cover `Q1.0` through `Q1.7`, so the analysis below is limited to those 8 questions.

## Generated analysis artifacts

- [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md) — automated stability summary for experiment 24
- [`generated_promptfoo_analysis_experiment_23_reference.md`](./generated_promptfoo_analysis_experiment_23_reference.md) — automated reference summary for experiment 23
- [`spurious_approaches_vs_sections_matrix.html`](./spurious_approaches_vs_sections_matrix.html) — emitted-approach vs retrieved-section matrix

## Method

Commands run:

```bash
uv run python experiments/analysis/run_promptfoo_analysis.py \
  'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents' \
  --experiment 24_section_expansion_Q1_baseline_with_settings_found_in_experiment_22 \
  > experiments/24_section_expansion_Q1_baseline_with_settings_found_in_experiment_22/generated_promptfoo_analysis.md

uv run python experiments/analysis/run_promptfoo_analysis.py \
  'content-min-score=0.53__d=25__ias-d=4__ias-min-score=0.4__ifric-d=6__ifric-min-score=0.48__ifrs-d=4__ifrs-min-score=0.53__llm_provider=openai-codex__ps-d=1__ps-min-score=0.4__retrieval-mode=documents__sic-d=6__sic-min-score=0.4' \
  --experiment 23_Q1_baseline_with_settings_found_in_experiment_22 \
  > experiments/24_section_expansion_Q1_baseline_with_settings_found_in_experiment_22/generated_promptfoo_analysis_experiment_23_reference.md

uv run python experiments/analysis/generate_spurious_approaches_sections_matrix.py \
  --experiment 24_section_expansion_Q1_baseline_with_settings_found_in_experiment_22 \
  --provider 'content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents'
```

## Automated analysis of Experiment 24

From [`generated_promptfoo_analysis.md`](./generated_promptfoo_analysis.md):

### Aggregate metrics

| Component | Strict | Loose |
|-----------|:------:|:-----:|
| **Score** | **82.2** | **83.6** |
| Approach stability | 0.5681 | 0.5681 |
| Applicability consistency | 0.9097 | 0.9583 |
| Recommendation consistency | 1.0000 | 1.0000 |
| Total questions | 8 | |
| Total runs | 24 | |

### Top and low performers

- **Top performers:** `Q1.2`, `Q1.4`
- **Low performers:** `Q1.0`, `Q1.3`, `Q1.6`, `Q1.7`

That headline is useful, but it must be interpreted carefully: this script measures **stability**, not **correctness**.

## My analysis

### 1. Section expansion is not a clear win on the overlapping subset

On the shared `Q1.0`–`Q1.7` subset, experiment 24 is slightly worse than experiment 23 overall.

| Metric | Experiment 23 subset | Experiment 24 | Delta |
|--------|----------------------|---------------|-------|
| Loose stability score | 87.2 | 83.6 | **-3.6** |
| Strict stability score | 86.9 | 82.2 | **-4.7** |
| Approach stability | 0.7910 | 0.5681 | **-0.2229** |
| Loose applicability consistency | 0.8160 | 0.9583 | **+0.1423** |
| Loose recommendation consistency | 1.0000 | 1.0000 | 0.0000 |

So section expansion improved answer consistency on applicability wording, but it **materially hurt approach-set stability**, which is the more important issue for this question family.

### 2. The per-question story is mixed

| Question | Exp. 23 loose | Exp. 24 loose | Delta |
|----------|---------------|---------------|-------|
| Q1.0 | 89.5 | 75.5 | **-14.0** |
| Q1.1 | 93.3 | 94.2 | +0.8 |
| Q1.2 | 100.0 | 100.0 | 0.0 |
| Q1.3 | 90.0 | 76.7 | **-13.3** |
| Q1.4 | 83.4 | 100.0 | **+16.6** |
| Q1.5 | 84.8 | 81.3 | -3.5 |
| Q1.6 | 61.2 | 76.7 | **+15.4** |
| Q1.7 | 95.0 | 64.7 | **-30.3** |

At face value this looks balanced: two strong improvements (`Q1.4`, `Q1.6`), three clear regressions (`Q1.0`, `Q1.3`, `Q1.7`), and the rest roughly flat.

But again, some of the “improvements” are stability-only improvements, not necessarily semantic improvements.

### 3. Q1.4 is the clearest example of why stability alone is misleading

`Q1.4` reaches a loose score of `100.0`, but all three runs emit the same wrong framing:
- `hedge_accounting`
- `consolidation_accounting`
- `separate_financials`

The model is extremely stable here, but it is stably answering in a **consolidation / separate-financial-statements taxonomy** instead of the expected three hedge approaches.

The retrieved context for `Q1.4` is consistent with that failure mode. The prompt is dominated by sections from:
- `ifrs10`
- `ias24`
- `ias27`
- plus only a thin slice of `ifrs9`

So section expansion seems to make a routing mistake more “coherent”: once the run lands in the wrong document cluster, the model receives a fuller, internally consistent section context and doubles down on the wrong abstraction.

### 4. The weakest regressions point to the same pattern

The low performers are not random.

#### Q1.3
The runs drift toward:
- `hedge_accounting`
- `foreign_currency_accounting`
- `foreign_currency_translation`

The retrieved context includes `IAS 21` and generic FX sections, which seems to push the model toward “IAS 21 accounting for FX effects” instead of “which hedge-accounting route applies?”

#### Q1.7
This is the biggest regression.

Two of the three runs collapse into:
- `hedge_accounting`
- `foreign_currency_translation`

with only one run recovering the full hedge taxonomy. Here again the prompt consistently includes `IAS 21::45` and nearby translation material, which appears to compete with the intended hedge-accounting framing.

#### Q1.0
`Q1.0` splits between:
- one correct run with the three expected hedge labels
- two runs using `hedge_accounting` plus other generic labels such as `ordinary_accounting` or `undesignated_derivative`

So the section-expanded context does not reliably anchor the taxonomy even on the baseline question.

### 5. Recommendation consistency is perfect, but that is not enough

Experiment 24 has perfect recommendation consistency (`1.0000`). That sounds great, but it hides the more important problem:
- the model consistently says **yes / yes under conditions**
- while often failing to organize the answer into the expected hedge taxonomy

In other words, section expansion seems to help the model converge on the broad high-level conclusion, but not on the specific structured approach decomposition we actually want.

### 6. Section expansion reduced prompt size, but the smaller prompt did not improve the taxonomy

Compared on the overlapping `Q1.0`–`Q1.7` subset:
- average `A-prompt.txt` size fell from about **194,594 chars** in experiment 23 to about **111,648 chars** in experiment 24
- average retrieved chunk count fell from about **295.5** to **173.1**

So experiment 24 is not failing because the prompt became too large. In fact, it became substantially smaller.

That suggests the main issue is not “too much context”, but rather **which sections are being expanded once document routing picks the wrong frame**.

### 7. Overall interpretation

My read is:

- **Section expansion helps when the selected section is already the right one.**
  - `Q1.2` remains perfect.
  - `Q1.6` improves materially.

- **Section expansion hurts when retrieval lands on a nearby but conceptually wrong section family.**
  - `Q1.4` becomes stably wrong in a consolidation taxonomy.
  - `Q1.3` and `Q1.7` drift toward IAS 21 / FX-accounting labels.
  - `Q1.0` still shows taxonomy fracture.

So the technique is promising as a **second-stage context builder**, but only if the **document/section selection stage is already reliable**.

Right now, whole-section expansion appears to magnify both:
- the right framing when routing is good
- the wrong framing when routing is bad

## Conclusion

Experiment 24 does **not** clearly beat experiment 23.

For the available `Q1.0`–`Q1.7` runs:
- overall stability is slightly worse
- approach stability is materially worse
- recommendation consistency stays perfect
- some apparent gains are misleading because they reflect **stable wrong taxonomies**, not better answers

The matrix and prompt review both point to the same root cause: section expansion is only beneficial if retrieval first identifies the right conceptual section family. When the run drifts into consolidation or general FX-accounting sections, expanding the full section gives the model a cleaner but still wrong basis for answer generation.

## Next steps

1. Keep section expansion as a candidate, but only behind stronger routing.
2. Improve document/section selection so IFRS 9 / IFRIC 16 hedge sections win more reliably over IAS 21 / IFRS 10 / IAS 27 framing.
3. Add evaluation checks for **taxonomy correctness**, not only run-to-run stability.
4. Rerun the full Q1 family once the experiment completes beyond `Q1.7`, otherwise the current result remains only a partial signal.

## Human analysis

As in the previous experiments, it seems to me that the model is having trouble when given multiple documents touching on the same topic: it doesn't treat them as complementary. Instead, it is reporting them as competing answers.
- IAS 21 gives the baseline accounting consequence
- IFRS 9 gives a possible hedge-accounting overlay / exception

instead of: baseline treatment + possible overlay if conditions are met

So we may need to address now how multiple documents need to be reconciled before trying to narrow further the documents retrieved. After all, retrieving IAS 21 makes perfect sense !

Suggestion for Prompt A update
```
Identify distinct accounting treatments.
Do not treat:
- the baseline accounting consequence
- an optional overlay such as hedge accounting
- an exception to a general rule
as separate approaches unless they are truly alternative accounting treatments.
```

Suggestion for Prompt B update
```
For each approach, state whether it is:
- a baseline accounting treatment
- an optional overlay
- an exception-driven treatment
- or a true alternative treatment

Do not present a baseline treatment and the absence of an optional overlay as two separate approaches.
```