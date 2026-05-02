# Experiment 57

## Goal

Evaluate stability to wording variants for:

- identified approaches
- target document recall
- target chunk recall
- approach applicability and recommendation applicability

The experiment covers question families `Q5`, `Q6`, `Q9`, `Q12`, and `Q16`.
Answer-level conclusions exclude `Q16.4`, because the last question of the last run was incomplete. Retrieval diagnostics were generated for the saved artifacts, but the `Q16` answer analysis below uses `Q16.0` through `Q16.3`.

## Method

Diagnostics were generated with the shared scripts under `experiments/analysis`:

```bash
uv run python experiments/analysis/document_routing/generate_document_routing_diagnostics.py --experiment experiments/57_answer-evals_on_variants_for_Q5_Q6_Q9_Q12_Q16 --run-id <run-id>
uv run python experiments/analysis/target_chunk_retrieval/generate_target_chunk_retrieval_diagnostics.py --experiment experiments/57_answer-evals_on_variants_for_Q5_Q6_Q9_Q12_Q16 --run-id <run-id>
uv run python experiments/analysis/approach_detection/generate_approach_detection_diagnostics.py --experiment experiments/57_answer-evals_on_variants_for_Q5_Q6_Q9_Q12_Q16 --run-id <run-id>
```

Diagnostic indexes:

- [document routing](./diagnostics/document_routing_index.md)
- [target chunk retrieval](./diagnostics/target_chunk_retrieval_index.md)
- [approach detection](./diagnostics/approach_detection_index.md)

## Cross-family Summary

| Family | Target document recall | Target chunk recall | All target ranges per variant | Mean answer stability | Exact approach stable | Applicability stable | Recommendation stable |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Q5 | 5/5 | 4/5 | 4/5 | 51.7 strict, 58.7 loose | 1/5 | 1/5 | 4/5 strict, 5/5 loose |
| Q6 | 5/5 | 30/30 | 5/5 | 38.0 strict, 48.0 loose | 1/5 | 0/5 | 3/5 strict, 5/5 loose |
| Q9 | 5/5 | 15/15 | 5/5 | 61.0 strict, 61.0 loose | 2/5 | 2/5 | 5/5 strict, 5/5 loose |
| Q12 | 5/5 | 13/15 | 3/5 | 73.7 strict, 73.7 loose | 2/5 | 4/5 | 4/5 strict, 4/5 loose |
| Q16 | 4/4 | 11/12 | 3/4 | 83.8 strict, 83.8 loose | 4/4 | 3/4 | 3/4 strict, 3/4 loose |

Target document recall is strong across all analyzable variants. The main failures are downstream: exact approach labels and applicability values are not stable enough under wording variants.

## Recap per question family

### Q5 - Counterparty Default Risk in Fair Value

Run: `2026-05-02_12-39-53_promptfoo-eval-family-q5`

Target document recall was perfect: `IFRS 13` was retrieved in all 5 variants, always at rank 1.

Target chunk recall was incomplete: expected range `IFRS 13 42-42` was present in 4/5 variants, with mean best rank 35.0 when present. This is the first retrieval weakness in the family: the correct document is always selected, but the exact paragraph can drop out.

Approach identification is unstable. The expected labels are `fair_value_of_a_liability` and `fair_value_of_an_asset`; both were present in 6/10 answer runs. Full expected applicability passed only 4/10 runs because:

- `Q5.0` identifies both expected approaches but assigns `fair_value_of_a_liability` as `non`.
- `Q5.1`, `Q5.3`, and one `Q5.4` run replace the expected labels with paraphrastic or adjacent labels such as `exit_price_for_an_asset`, `stand_alone_asset_fair_value`, or `risk_adjusted_cash_flows`.

Recommendation applicability is mostly stable. Strict recommendation stability is 4/5 variants; loose stability is 5/5 because the only strict difference is `oui` versus `oui_sous_conditions`.

### Q6 - Investor Power Under IFRS 10

Run: `2026-05-02_12-49-24_promptfoo-eval-family-q6`

Target document recall was perfect: `IFRS 10` was retrieved in all 5 variants, always at rank 1.

Target chunk recall was also perfect at the configured range level: all 6 expected ranges were present in all 5 variants (`30/30`). The later ranges are deeper in the prompt, especially `IFRS 10 B36-B36` at mean best rank 53.0 and `IFRS 10 B47-B50` at mean best rank 64.0, but they are present.

Approach identification is the weakest part of this family. There is no expected-label contract in `family.yaml`, so this is a stability finding rather than a pass/fail correctness finding. Across 10 answer runs the model produced 31 unique normalized labels, with repeated decomposition into voting rights, contractual rights, substantive potential voting rights, principal/agent, joint control, and significant influence variants. Exact approach-set stability is 1/5 variants and applicability stability is 0/5.

Recommendation applicability is stable only after loose mapping: strict stability is 3/5, but loose stability is 5/5 because the drift is `oui` versus `oui_sous_conditions`.

### Q9 - IP Licence Revenue Timing

Run: `2026-05-02_12-57-25_promptfoo-eval-family-q9`

Target document recall was perfect: `IFRS 15` was retrieved in all 5 variants, always at rank 1.

Target chunk recall was perfect at the configured range level: `IFRS 15 B56-B56`, `B58-B58`, and `B61-B61` were present in all variants (`15/15`). The expected chunks tend to sit deep in the prompt, with mean best ranks of 57.2, 58.2, and 62.2.

Approach identification is semantically close but label-unstable. The recurring intended pair is right-to-access versus right-to-use intellectual property, but exact labels vary among:

- `right_to_access_intellectual_property`
- `right_to_access`
- `right_to_access_the_entitys_intellectual_property`
- `right_to_use_intellectual_property`
- `right_to_use`
- `right_to_use_the_entitys_intellectual_property`

Exact approach-set stability is 2/5 variants. Applicability stability is also 2/5, even though all observed applicability values are directionally consistent as `oui_sous_conditions`.

Recommendation applicability is fully stable: 5/5 strict and 5/5 loose, always `oui_sous_conditions`.

### Q12 - Short-term Lease Exemption With Renewal

Run: `2026-05-02_13-02-32_promptfoo-eval-family-q12`

Target document recall was perfect: `IFRS 16` was retrieved in all 5 variants, always at rank 1.

Target chunk recall was partial: 13/15 expected range hits. `IFRS 16 5-8` and `IFRS 16 B34-B34` were present in all variants, but `IFRS 16 21-21` was present in only 3/5. All expected ranges were present together in 3/5 variants.

Approach identification is not stable against the expected labels. The expected labels are `right_of_use_model` and `short_term_lease_exemption`; both were present in only 2/10 answer runs. The short-term lease exemption itself is stable, present in 9/10 runs, but the general lessee accounting side is usually emitted as variants such as `right_of_use_asset_and_lease_liability`, `general_lessee_lease_model`, or `general_lessee_accounting`.

Expected applicability passed only 2/10 runs because it depends on the exact expected labels being present. When the expected approaches are present, their applicability is `oui_sous_conditions`, which is correct. Recommendation applicability is stable for 4/5 variants; `Q12.4` has one run with final recommendation `non` instead of `oui_sous_conditions`.

### Q16 - Carbon Neutrality Voluntary Commitment Provision

Run: `2026-05-02_13-12-42_promptfoo-eval-family-q16`

Answer-level analysis excludes `Q16.4`. `Q16.3` is retained, but its repeat answer has missing applicability and recommendation values, which affects stability.

Target document recall was perfect on the analyzable variants: `IAS 37` was retrieved in all 4 analyzed variants, at rank 1.

Target chunk recall was mostly good: 11/12 expected range hits. `IAS 37 10-10` and `IAS 37 17-20` were present in all analyzed variants; `IAS 37 14-14` was present in 3/4. All expected ranges were present together in 3/4 variants.

Approach identification is stable: the expected labels `provision` and `contingent_liability` were present in all 8 analyzed answer runs.

Applicability is the main correctness failure. The expected applicability is `provision = non` and `contingent_liability = oui_sous_conditions`, but all completed runs assign `provision = oui_sous_conditions`. Expected applicability therefore passes 0/8 analyzed answer runs. Recommendation applicability passes 7/8 only because `Q16.3` repeat has a missing recommendation; however, the substantive issue is that the final recommendation follows the same conditional-provision framing instead of the expected no-provision conclusion.

## Analysis

### Missing Target Chunk Analysis

The missing target chunks are not random failures. They occur where the target paragraph is a bridge paragraph whose exact wording is less dominant than neighboring or cross-referenced material. At the time experiment 57 was run, the answer-run wrapper resolved `documents2_through_chunks__enriched` with `min_score=0.53`, `per_document_k=10`, `expand_to_section=true`, and same-standard reference expansion at depth 1. The answer Promptfoo wrapper now requires an explicit `retrieval-policy`, matching the retrieve suite, so future answer runs fail fast instead of silently resolving a catalog default.

Strictly, `documents2_through_chunks__enriched` is the effective policy resolved by this experiment's answer runs: `promptfooconfig.yaml` passes only `policy-config` to `scripts/run_answer.py`, and `load_policy_config()` selects the catalog default. The standalone retrieve Promptfoo suite currently passes `retrieval-policy: standards_only_through_chunks__enriched`, but that explicit retrieve-suite policy was not the one resolved by the saved answer artifacts analyzed here.

| Case | Missing target | Current raw score and rank | Main failure mode | Depth-2 reference expansion | Hypothetical glossary result |
| --- | --- | --- | --- | --- | --- |
| `Q5.2` | `IFRS 13.42` | score 0.6887, global rank 67, IFRS 13 rank 30 | Cut by `per_document_k=10`; score is high enough, but many generic fair-value paragraphs rank ahead | Would retrieve it | Adding `non-performance risk` / `counterparty default risk` makes it rank IFRS 13 #2 |
| `Q12.1` | `IFRS 16.21` | score 0.5621, global rank 165, IFRS 16 rank 15 | Cut by `per_document_k=10`; score clears threshold but is below other short-term lease / agenda-decision hits | Would retrieve it | Adding `lease term`, `non-cancellable period`, `renewal option` makes it rank IFRS 16 #1 |
| `Q12.4` | `IFRS 16.21` | score 0.5261, global rank 346, IFRS 16 rank 23 | Both below `min_score=0.53` and cut by `per_document_k=10` | Would not retrieve it | Adding `lease term` / `renewal option` makes it rank IFRS 16 #6 |
| `Q16.3` | `IAS 37.14` | score 0.5268, global rank 67, IAS 37 rank 6 | Below `min_score=0.53`; it would be within top-k if it cleared the threshold | Would not retrieve it | Adding `present obligation` / `recognise a provision` makes it rank IAS 37 #2 |

#### Similarities in the Dropped Cases

The dropped paragraphs are all necessary legal tests or bridge paragraphs, but they are not always the most lexically distinctive paragraph for the user wording:

- `IFRS 13.42` is the specific non-performance-risk paragraph for liabilities. `Q5.2` uses broad fair-value language: “perspective de marché”, “instrument”, “actif comme passif”. That wording strongly pulls IFRS 13.2, 13.24, valuation-technique material, and market-participant risk material ahead of paragraph 42.
- `IFRS 16.21` is about revising the lease term when the non-cancellable period changes. `Q12.1` and `Q12.4` ask primarily about short-term lease exemption, tacit renewal, automatic continuation, and indefinite term. Those terms pull IFRS 16.5-8, B34-B41, and related agenda-decision material ahead of paragraph 21.
- `IAS 37.14` is the generic three-condition provision recognition test. `Q16.3` says “obligation actuelle” and “crédits carbone à utiliser ultérieurement”, which pulls IAS 37.10 definitions and IAS 37.17-20 future-action / past-event paragraphs ahead of the generic recognition paragraph.

#### Why Q6 and Q9 Did Not Drop Target Chunks

`Q6` and `Q9` have narrower and denser target clusters.

For `Q6`, the expected IFRS 10 ranges all sit inside the same control/power conceptual cluster: power, relevant activities, substantive rights, decision-making, voting rights, and principal/agent analysis. Some target ranges are deep in the final prompt, but the seed chunks and reference expansion keep reaching the cluster.

For `Q9`, the wording is highly distinctive: licence, intellectual property, recognition over time, recognition at a point in time, right to access, right to use. IFRS 15 B56, B58, and B61 use the same conceptual vocabulary. Even though their mean ranks are deep, all three target ranges stay present across variants.

#### Glossary Hypothesis

The local diagnostic strongly suggests that targeted glossary additions would have made target chunk recall 100% for this experiment. A proposed, inactive glossary delta is captured in [config/en-fr-glossary--experiment57-target-recall.yaml](../../config/en-fr-glossary--experiment57-target-recall.yaml):

- Q5: map `non-exécution` and `défaut de la contrepartie` to `non-performance risk` / `counterparty default risk`.
- Q12: map `durée`, `durée indéterminée`, `durée initiale`, `renouvelable tacitement`, and `se poursuivre automatiquement` to `lease term`, `non-cancellable period`, and/or `renewal option`.
- Q16: map `obligation actuelle` and `comptabilisation d’une provision` to `present obligation` and `recognise a provision`.

The main caveat is that these terms improve recall by moving the target paragraph into the top-10 seed set; they may also shift other rankings and should be checked against Q1-Q3 non-regression before being promoted into the active glossary.

**Human**: ❌ the glossary terms generated by the LLM are optimized for retrieval and not representative of what would have been generated while translating French terms. This hypothesis does not hold at the moment. Examples:
```
  - fr: "durée indéterminée"
    en:
      - "lease term"
      - "non-cancellable period"
  - fr: "durée initiale"
    en:
      - "lease term"
```

#### Other Hypotheses

Reference expansion depth 2 helps when the missing paragraph is reachable through the document's internal reference graph. It recovers `IFRS 13.42` and `IFRS 16.21` for `Q12.1`, but not `Q12.4` or `IAS 37.14`. That suggests depth 2 is not a complete fix and may add a lot of context.

`per_document_k=10` is a real ceiling for Q5 and Q12. The target scores are not terrible: `IFRS 13.42` and `IFRS 16.21` in `Q12.1` clear the threshold but lose to many adjacent sections. Raising `per_document_k` might recover them, but likely increases prompt size and noise. Glossary enrichment is more targeted.

The active glossary is still Q1-shaped. It already handles `juste valeur`, which is why Q5 retrieves IFRS 13 reliably, but it does not include later-family canonical terms from IFRS 16 and IAS 37 definitions. That explains why document recall is strong while paragraph recall is uneven.

### Labels for identified approaches are generally not stable

#### Q6 exposes the limits of the current "peer accounting approaches" framing of answers

The Q6 variant runs exposed an important limitation of the current Prompt A → Prompt B architecture.

The system is currently strongest on questions where the task is to identify and evaluate **peer accounting models or treatments**, for example:

- hedge-accounting models
- IFRS 9 measurement categories
- licence revenue-recognition models
- exemptions or recognition treatments where the standard provides a small set of comparable alternatives

In those cases, the current architecture works well because Prompt A is explicitly designed to:

1. identify the primary accounting issue;
2. classify authority;
3. identify treatment families;
4. map those families to peer top-level accounting approaches;
5. pass those approaches to Prompt B for applicability analysis.

Q6 is different because the question “Comment déterminer si un investisseur détient le pouvoir sur une entité ?” is not primarily an approach-selection question. IFRS 10 does not provide a menu of peer accounting models for this issue. It provides a **single control assessment framework** with criteria, indicators, and application-guidance paths, including:

- power over relevant activities;
- substantive rights;
- protective rights;
- voting rights;
- potential voting rights;
- contractual rights;
- delegated decision-making / principal-agent analysis;
- de facto power;
- deemed separate entities;
- exposure to variable returns;
- linkage between power and returns.

Across Q6 runs, Prompt A therefore tried to force a “peer approach” structure onto material that is better understood as assessment criteria and application guidance. The result was unstable approach labels such as:

- `contractual_power`
- `contractual_rights`
- `de_facto_power`
- `power_through_voting_rights`
- `principal_agent_assessment`
- `protective_rights`
- `voting_rights_power`
- `control`
- `joint_control`
- `significant_influence`

Some of these are synonyms or near-synonyms. More importantly, many are not peer accounting approaches at all. They are factors, indicators, fact-pattern paths, or neighbouring accounting conclusions used within the broader control assessment.

This indicates that the remaining issue is not merely label normalization. It is a deeper abstraction mismatch:

> **The current pipeline assumes that the first stage should always identify peer accounting approaches, but some IFRS questions require applying a single assessment framework rather than choosing between peer accounting models.**

A more general system would likely need Prompt A to first classify the question type, for example:

- peer approach selection;
- single-framework assessment;
- recognition-timing assessment;
- measurement assessment;
- presentation or disclosure assessment.

This list would need to be provided or reviewed by the SME.

For single-framework questions, the output should probably contain one governing framework, such as `control_assessment`, plus structured criteria or assessment factors, rather than multiple peer approaches.

That would be a meaningful architecture extension, but it is outside the current scope. It would require changes to the intermediate schema, Prompt A, Prompt B, diagnostics, and eval expectations.

For the purposes of this project checkpoint, the conclusion is therefore:

- the current system will soon generalize well to IFRS questions where the answer depends on identifying and evaluating peer accounting models or treatments;
- it is not yet designed to handle all IFRS question types;
- Q6 identifies a clear next architecture boundary: single-framework assessment questions;
- addressing that boundary would be a separate engineering phase, not a small prompt tweak.

This is an acceptable limitation for the current demonstrator. The project has already shown the core architecture working across several model-selection / treatment-selection question families, while Q6 gives a useful, concrete example of where the next level of generality would need to begin.

#### Q5 also exposes the limits of the current system

The question asks whether counterparty default / non-performance risk is reflected in fair value measurement. IFRS 13 does not provide a set of peer accounting approaches for this issue. It provides a single fair value measurement framework, with different measurement cases and mechanics depending on whether the item is an asset, a liability, a portfolio exposure, or a valuation technique input.

Across runs, Prompt A emitted labels such as `fair_value_of_an_asset`, `fair_value_of_a_liability`, `exit_price_for_an_asset`, `transfer_price_for_a_liability`, `portfolio_exception`, `risk_adjusted_cash_flows`, and `risk_adjusted_discount_rate`.

These are not peer accounting approaches. They mix several abstraction levels:

- measured object: asset / liability
- fair value definition: exit price / transfer price
- measurement mechanics: risk-adjusted cash flows / discount rate
- overlays or exceptions: portfolio exception / net exposure
- surface variants of the same fair value measurement concept

This suggests that Q5 should be classified as a measurement-assessment question, not as a peer-approach-selection question.

The current Prompt A schema can be made to pass by forcing labels such as `fair_value_of_an_asset` and `fair_value_of_a_liability`, but that would be a workaround rather than a clean generalization. A more general architecture would need to classify the question type first and use a different intermediate structure for measurement-assessment questions.

For the current project checkpoint, Q5 should therefore be treated as evidence of a clear architecture boundary rather than as a failed retrieval or simple label-normalization problem.


#### Q9 works because it is consistent with the current system

The Q9 variants are a good fit for the current approach-identification architecture.

Unlike Q5 and Q6, this question family does ask for a choice between peer IFRS accounting models. The issue is whether revenue from a licence of intellectual property is recognized over time or at a point in time. IFRS 15 expresses this through two peer licence models:

- right to access intellectual property
- right to use intellectual property

Across the 10 runs, the answer shape was stable:

- all runs returned exactly 2 approaches
- no run emitted spurious approaches
- no run missed the expected conceptual approaches
- all runs returned `oui_sous_conditions`
- retrieval covered the expected IFRS 15 licence guidance paragraphs: `B56`, `B58`, and `B61`

The remaining issue is not conceptual approach detection but label normalization. The same two approaches appeared under different surface labels:

- `right_to_access`
- `right_to_access_intellectual_property`
- `right_to_access_the_entitys_intellectual_property`

and:

- `right_to_use`
- `right_to_use_intellectual_property`
- `right_to_use_the_entitys_intellectual_property`

These should be canonicalized as:

- `right_to_access_intellectual_property`
- `right_to_use_intellectual_property`

The shorter labels are too generic outside this family, while the longer labels include source-specific IFRS drafting language (`the entity’s`) that does not change the model identity.

**Conclusion**: Q9 supports the current architecture. It is a successful generalization case for approach-based IFRS questions, with a residual code-side canonicalization need for approach labels.

#### Q12 is a qualified success for the current architecture.

The family asks whether a lease with no purchase option, an initial term of one year or less, and tacit renewal or indefinite duration can qualify for the IFRS 16 short-term lease exemption.

This is not as cleanly “approach-based” as Q9. It is partly an eligibility question: determine the lease term, then decide whether the optional short-term lease exemption can apply. Still, IFRS 16 gives a workable two-treatment structure:

- short-term lease exemption
- general right-of-use model

Retrieval appears strong. The expected IFRS 16 evidence was recovered, including:

- IFRS 16 `5`–`8`
- IFRS 16 `21`
- IFRS 16 `B34`

The remaining issues are downstream:

1. **Approach-label normalization**
   The same conceptual approaches appeared under several labels:

   - `short_term_lease_exemption`
   - `expense_recognition_for_short_term_leases`
   - `right_of_use_model`
   - `right_of_use_asset_and_lease_liability`
   - `recognition_of_a_right_of_use_asset_and_lease_liability`

   These should be canonicalized as:

   - `short_term_lease_exemption`
   - `right_of_use_model`

   `expense_recognition_for_short_term_leases` is an accounting consequence of the exemption, not the canonical approach name.  
   `right_of_use_asset_and_lease_liability` describes the mechanics of the general lessee model, but `right_of_use_model` is the better stable evaluation label.

2. **Question polarity**
   Some variants ask whether the exemption can apply; another asks whether the renewal feature prevents short-term lease classification. Because of that, `oui_sous_conditions` and `non` may express the same directional answer depending on the question wording.

**Conclusion**: Q12 supports the system’s ability to handle another approach-like IFRS question, but it also shows that the evaluation layer needs stronger canonicalization of approach labels and semantic handling of question polarity. It is a good generalization case, but less clean than Q9.

#### Q16 is the cleanest generalization result in this batch.

The family asks whether a voluntary commitment to contribute to carbon neutrality at a defined horizon creates an obligation requiring recognition of a provision, including for future carbon credits intended to offset excess emissions.

The expected answer structure is stable under IAS 37:

- `provision`
- `contingent_liability`

Retrieval appears strong. The expected IAS 37 evidence was recovered, including:

- IAS 37 `10`
- IAS 37 `14`
- IAS 37 `17`–`20`

The answer pipeline also behaved well across variants and repeat runs:

- no missing expected labels
- no spurious labels
- stable approach labels
- consistent `oui_sous_conditions` recommendation
- IAS 37 treated as the authoritative document
- unrelated documents, when retrieved, classified as peripheral rather than driving the answer

This is not exactly the same type of question as Q1, Q2, or Q9. It is less about choosing between peer accounting models and more about applying an IAS 37 recognition framework. However, IAS 37 itself provides clear output categories, so the current approach-identification structure still works: `provision` and `contingent_liability` are acceptable canonical answer paths for evaluation purposes.

Conclusion: Q16 is a strong positive generalization case. It shows that the system can handle at least some recognition-threshold questions outside the original IFRS 9 / hedge-accounting area, provided the governing standard exposes clear, stable categories for the answer.

## Conclusion

Experiment 57 shows that document-level retrieval is robust to wording variants. Every analyzable family retrieved the target authoritative document for every analyzed variant, usually at rank 1. The main retrieval weakness is not document routing but target paragraph recall in bridge or generic test paragraphs: `IFRS 13.42`, `IFRS 16.21`, and `IAS 37.14`.

Target chunk recall is good but not fully robust. `Q6` and `Q9` had perfect expected-range recall because their target paragraphs sit in dense, distinctive conceptual clusters. `Q5`, `Q12`, and `Q16` had dropouts where the expected paragraph was either cut by `per_document_k`, fell just below `min_score`, or was less lexically distinctive than nearby material. Depth-2 reference expansion would recover only some cases, and the glossary hypothesis is not currently reliable because the tested additions were optimized for retrieval rather than representative French-to-English accounting-term translations.

The answer-layer result is mixed but informative. `Q9` is the cleanest success for the current peer-approach architecture: the same two licence models are identified consistently, with only canonical label normalization left. `Q12` is a qualified success: the short-term lease exemption and general right-of-use model are recoverable, but evaluation needs label canonicalization and question-polarity handling. `Q16` is also a strong generalization case for recognition-threshold questions where the standard exposes stable answer categories, although the expected applicability contract for `provision` may need SME review against the intended interpretation.

The important architecture finding is that `Q5` and especially `Q6` are not naturally peer-approach-selection questions. `Q5` is better viewed as a fair-value measurement assessment, and `Q6` as a single IFRS 10 control-assessment framework. Forcing those questions into a list of peer accounting approaches creates unstable labels and mixed abstraction levels. The next architecture boundary is therefore question-type classification before Prompt A chooses its intermediate structure.

Overall, the current system generalizes best to IFRS questions that genuinely require selecting or comparing accounting treatments. It is not yet a fully general IFRS reasoning architecture for single-framework assessment questions.

## Next Steps

1. Add an explicit question-type classification step before approach identification. At minimum, distinguish peer-approach selection, single-framework assessment, measurement assessment, recognition-threshold assessment, and eligibility / exemption assessment.
2. Keep the current peer-approach architecture for question families like `Q9`, and add code-side canonicalization for stable labels:
   - Q9: map `right_to_access` and `right_to_access_the_entitys_intellectual_property` to `right_to_access_intellectual_property`; same for right-to-use.
   - Q12: canonicalize the general lessee model to `right_of_use_model` and the exemption to `short_term_lease_exemption`.
3. Extend the evaluation layer so it can handle question polarity. `Q12` shows that `oui_sous_conditions` and `non` can express the same accounting conclusion when variants ask opposite forms of the same question.
4. Treat `Q5` and `Q6` as architecture-boundary cases, not simple label failures. Design separate intermediate structures for:
   - Q5: fair-value measurement assessment, with measured object and measurement mechanics as structured fields rather than peer approaches.
   - Q6: IFRS 10 control assessment, with one governing framework and structured criteria / indicators.
5. Revisit the `Q16` expected applicability contract with SME input. The labels are stable, but the expected `provision = non` conflicts with the model's repeated `oui_sous_conditions` framing.
6. Improve target paragraph recall with retrieval-specific experiments rather than promoting the current glossary proposal. Test `per_document_k`, `min_score`, and reference-expansion depth on Q1-Q3 plus Q5/Q12/Q16 non-regression sets. Only add glossary terms that are representative French-to-English accounting translations, not terms optimized to force target paragraphs into the top-k.
7. Rerun `Q16.4` after the incomplete run issue is resolved.
