# Experiment 33: Authority Competition on Full Corpus

## Goal

We ran some manual tests on Q1.0 with all data on ifrs.org (including behind paywall) and all Lefebvre Navis and detected that there was a strong regression on approach stability (the answer often fell back to hedge/don't hedge).

The goal of this evaluation is to test the impact of the improvements made to the prompt to force it back to the 3 core approaches and to handle overlapping standards (ex: IFRS 9 vs IAS 39)

Although, we expect some instability in approaches due to the larger corpus diluting the useful information, we expect IAS 39 to be consistently discarded.

## Run Details

**Date:** 2026-04-16
**Provider:** openai-codex with policy.default.yaml
**Questions:** Q1.0 - Q1.7 (8 questions from family Q1)

---

**Provider:** `llm_provider=openai-codex__policy-config=./effective/policy.default.yaml`
**Experiment:** `33_authority_competition_on_full_corpus`
**Run:** `2026-04-16_22-20-04_promptfoo-eval-family-q1`

## Per-Question Results

| Question | Runs | Score | Score (loose) | Valid |
|---|---|---|---|---|
| Q1.0 | 2 | 100.0 | 100.0 | True |
| Q1.1 | 2 | 100.0 | 100.0 | True |
| Q1.2 | 2 | 100.0 | 100.0 | True |
| Q1.3 | 2 | 100.0 | 100.0 | True |
| Q1.4 | 2 | 100.0 | 100.0 | True |
| Q1.5 | 2 | 90.0 | 90.0 | True |
| Q1.6 | 2 | 100.0 | 100.0 | True |
| Q1.7 | 2 | 56.7 | 56.7 | True |
| **AVERAGE** |  | **93.3** | **93.3** |  |

## Detailed Breakdown

| Question | Approach (strict) | Approach (mapped) | Applic (strict) | Applic (loose) | Rec (strict) | Rec (loose) |
|----------|------------------:|-----------------:|----------------:|---------------:|-------------:|------------:|
| Q1.0 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.1 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.2 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.3 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.4 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.5 | 1.0000 | 1.0000 | 0.6667 | 0.6667 | 1.0000 | 1.0000 |
| Q1.6 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Q1.7 | 0.3333 | 0.3333 | 1.0000 | 1.0000 | 0.0000 | 0.0000 |

## Aggregate Metrics

| Component | Strict | Loose |
|-----------|-------:|------:|
| **Score** | **93.3** | **93.3** |
| Approach (Jaccard, exact labels) | 0.9167 | 0.9167 |
| Applicability (exact values) | 0.9583 | 0.9583 |
| Recommendation (exact values) | 0.8750 | 0.8750 |
| | | |
| Total Questions | 8 | |
| Total Runs | 16 | |
| | | |
*Strict*: exact label/value matching | *Loose*: maps `oui` ↔ `oui_sous_conditions`


## Label Frequency by Question

### Core Labels (>= 10% of runs)

| Label | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Total |
|---|---|---|---|---|---|---|---|---|---|
| net_investment_hedge | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 16 |
| cash_flow_hedge | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 14 |
| fair_value_hedge | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 14 |

### Spurious Labels (< 10% of runs)

| Total | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 | Label |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | monetary_item_hedge |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | monetary_item_remeasurement |

## Comparison: Top vs Low Performers

### Top Performers (loose score >= 95.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.2 | 2 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.3 | 2 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.4 | 2 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.1 | 2 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.6 | 2 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |
| Q1.0 | 2 | 100.0 | 100.0 | 1.00 | 1.00 | 1.00 |

**6/8 questions (75%) are top performers**

### Low Performers (loose score < 80.0)

| Question | Runs | Score | Score (loose) | Approach | Applic | Rec |
|----------|------|-------|---------------|----------|--------|-----|
| Q1.7 | 2 | 56.7 | 56.7 | 0.33 | 1.00 | 0.00 |

**1/8 questions (12%) are low performers**

### Key Observations

- **Approach stability (strict)**: Top=1.000, Low=0.333, Delta=+0.667
- **Approach stability (canonical)**: Top=1.000, Low=0.333, Delta=+0.667
- **Applicability consistency (loose)**: Top=1.000, Low=1.000, Delta=+0.000
- **Recommendation consistency (loose)**: Top=1.000, Low=0.000, Delta=+1.000
- **Avg unique labels per run**: Top=3.0, Low=3.0

## Human analysis

These results are quite good quantitatively, there is hardly even a loss compared to experiment 32.

However
1. the size of Prompt A has exploded to 400-500kB from 100-120kB, this negatively impacts the cost
2. although the approaches are stable and correct, the references are often bad because IAS 39 is cited and not IFRS 9. So on this point the evaluation shows a clear regression.

When diving into which citation was used on which question, the picture is far from being so rosy:
1. On half the questions (Q1.3 - Q1.7), IAS 39 is cited instead of IFRS 9 despite the authority competition rule
   - That's because Prompt A doesn't send any IFRS 9 chunks : we have a retrieval problem in that other IFRS standards match the question better and the thresholds eliminate IFRS 9 from the prompt
   - On Q1.0, both IAS39 and IFRS 9 we retrieved and IAS39 was successfully discarded from the output of Prompt A
      ```json
        "authority_resolution": {
        "candidate_governing_documents": ["ifrs9", "ias39", "ias21", "ifric16"],
        "selected_primary_document": "ifrs9",
        "selection_reason": "I applied the strict precedence rule that IFRS supersedes IAS for overlapping hedge accounting eligibility questions, so IFRS 9 governs the identification of hedge accounting models and hedged items, displacing IAS 39 on the same issue.",
        "discarded_due_to_overlap": ["ias39"],
        "residual_uncertainty": "Low: IFRS 9 clearly supersedes IAS 39 for hedge accounting, while IAS 21 and IFRIC 16 remain relevant only to clarify foreign currency effects and net investment hedge constraints rather than replace IFRS 9."
        },
       ```
2. Half of the IFRIC citations are irrelevant
3. The citation coming from IAS 21 is not mandatory to reason but it is relevant

One good thing is that all the IFRS 9 citations are good.



 | Citation | Relevant | Total | Q1.0 | Q1.1 | Q1.2 | Q1.3 | Q1.4 | Q1.5 | Q1.6 | Q1.7 |                                                                                                
 |---|---|---|---|---|---|---|---|---|---|---|
 | ias21:23 | ❌ | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
 | ias21:32 | ✅  | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
 | ias21:45 | ✅ | 16 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
 | ias27:12 | 🤔 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
 | ias39:78 | ❌ | 7 | 0 | 0 | 0 | 2 | 2 | 1 | 2 | 0 |
 | ias39:80 | ❌ | 8 | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 0 |
 | ias39:81 | ❌ | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
 | ias39:86 | ❌ | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
 | ias39:88 | ❌ | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
 | ias39:89 | ❌ | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
 | ias39:95 | ❌ | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
 | ias39:97 | ❌ | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
 | ias39:100 | ❌ | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
 | ias39:102 | ❌ | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
 | ifric16:8 | 🤔 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
 | ifric16:10 | ✅ | 8 | 2 | 0 | 0 | 1 | 1 | 2 | 0 | 2 |
 | ifric16:11 | ✅ | 3 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
 | ifric16:12 | ✅ | 8 | 1 | 0 | 0 | 2 | 1 | 2 | 0 | 2 |
 | ifric16:13 | ❌ | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
 | ifric16:14 | ❌ | 5 | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 1 |
 | ifric16:15 | ❌ | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 |
 | ifric16:2 | ✅ | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 |
 | ifrs9:6.3.1 | ✅ | 6 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
 | ifrs9:6.3.3 | ✅ | 3 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 |
 | ifrs9:6.3.5 |  ✅ | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
 | ifrs9:6.3.6 | ✅ | 6 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
 | ifrs10:B86 | ❌ | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
 
 ### Next steps

 We need to fix retrieval again to ensure IFRS 9 is always surfaced. Ways to do this
 - increase the number of IFRS documents retrieved or lower the min-score but *that's a bad idea* because it will make a huge prompt even bigger
 - investigate why the similarity score is not higher and find better ways of retrieving the right documents