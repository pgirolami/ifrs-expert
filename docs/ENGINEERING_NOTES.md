# Engineering Notes

These are the engineering lessons that seem reusable outside this project.
The chronological record lives in [`JOURNAL.md`](./JOURNAL.md); this file is the cleaned-up version of what we learned from those experiments.

---

## 1. Check the evidence layer before tuning the reasoning

The biggest process lesson was simple: do not spend too long tuning prompts until retrieval has been measured directly.

Several early failures looked like weak reasoning. Some were but a lot of them were evidence problems:

- the governing document was missing;
- the right document was present, but the needed paragraph was missing;
- English variants retrieved the right paragraph while French variants did not;
- supporting material outranked the standard itself;
- older or overlapping authority appeared instead of the current governing standard.

The work became easier once retrieval had its own diagnostics:

- target document recall;
- target paragraph / chunk recall;
- retrieval-only Promptfoo suites;
- document-routing diagnostics;
- chunk-retrieval diagnostics;
- run-to-run comparison artifacts.

### Better order next time

The order I would use next time:

1. prove the question is answerable in principle;
2. build a small end-to-end demo for SME feedback;
3. instrument retrieval early;
4. stabilize document routing and paragraph evidence;
5. then work on approach identification and applicability reasoning.

The first prototype did the first two steps quickly, which was useful. The mistake was letting retrieval instrumentation arrive late, because that made some prompt work happen on top of an unstable evidence layer.

---

## 2. Clean corpora make prototypes look better than they are

The first version worked against a tiny corpus of hand-picked documents. That was useful for moving fast, but it quietly removed one of the hardest jobs: deciding which authority mattered.

Once the corpus became more realistic, the real problems showed up:

- IFRS vs IAS overlap;
- IFRIC vs SIC overlap;
- standards vs basis material;
- standards vs implementation guidance;
- standards vs illustrative examples;
- standards vs FAQ-style practitioner sources;
- current guidance vs older or superseded guidance;
- explanatory material vs the paragraphs that actually govern the answer.

A RAG system can look good when the corpus is artificially clean. In an expert corpus, document routing is not plumbing. It is part of the reasoning system, because the model can only compare the accounting paths that retrieval puts in front of it.

---

## 3. Retrieval has to be document-aware and paragraph-aware

Plain chunk similarity was not enough.

The retrieval design moved through several stages:

1. chunk similarity;
2. document-level representations;
3. document routing before chunk retrieval;
4. routing from the best local chunk evidence;
5. standards-only routing from strong local evidence;
6. same-family reference expansion;
7. section expansion.

The important shift was away from broad document similarity. If one chunk in a document family strongly matches the question, that can be a better routing signal than an averaged document representation.

That led to a cleaner split between:

- document routing;
- seed evidence retrieval;
- reference expansion;
- section expansion;
- final prompt construction.

Those are separate operations and need separate knobs.

---

## 4. Cross-references are part of the retrieval graph

IFRS standards contain many explicit internal references. They should not be treated as display text only.

Some application-guidance paragraphs are lexically close to the user's question but point back to governing paragraphs that are needed for the answer. If retrieval keeps only the matching explanatory chunk, the prompt may miss the actual test.

The project added support for:

- `Refer:` annotations;
- inline cross-references;
- section-scoped references;
- same-document-family expansion;
- provenance tags showing whether a chunk came from similarity search, reference expansion, or section expansion.

For structured expert corpora, the document's own reference graph is a useful retrieval signal. Embeddings alone leave too much on the table.

---

## 5. Multilingual retrieval needs concepts, not just translation

The user questions are in French, while much of the IFRS material is in English.

A French-to-English glossary helped, but it was brittle:

- one added translation could improve one target and hurt another;
- literal translations were often less useful than accounting concepts;
- expanded entries sometimes competed with better existing entries;
- retrieval-friendly glossary terms were not always good translations.

The glossary is therefore only a retrieval aid in this project. A stronger version would map user wording to controlled accounting concepts, but that is its own product problem rather than a quick dictionary pass.

---

## 6. Two-stage reasoning was more stable

The answers became more stable after separating:

1. approach identification;
2. applicability reasoning.

Prompt A identifies the accounting issue, authority types, candidate treatment families, and peer accounting approaches. Prompt B uses that structured output, plus pruned primary and supporting authority, to decide what applies and write the answer.

This helped because Prompt A could be told not to decide applicability too early. It also made the intermediate reasoning visible. JSON was not just an output format; it became the debugging and evaluation surface.

---

## 7. Authority classification reduces context noise

The model did better when retrieved material was not treated as one flat pile.

The current pipeline classifies context as:

- primary authority;
- supporting authority;
- peripheral authority.

Prompt B then receives a smaller context focused on primary and supporting material.

That matters because a paragraph can be topically relevant and still be the wrong authority. Expert-domain RAG needs authority modelling, not only relevance ranking.

---

## 8. Not every IFRS question is an approach-selection question

This was the most important boundary found near the end of the project.

The current Prompt A schema assumes the main task is to identify peer accounting approaches. That works when the standard provides a small set of comparable treatments or models.

Good fits include:

- hedge-accounting models;
- IFRS 9 measurement categories;
- IP licence revenue timing models;
- short-term lease exemption vs the general lessee model.

It does not fit every IFRS question.

### Single-framework assessment

IFRS 10 control questions are a good example. Determining whether an investor has power over an investee is a control assessment with criteria and indicators, not a menu of peer approaches.

When forced into the current schema, the model produced labels such as:

- voting rights;
- contractual rights;
- protective rights;
- principal-agent assessment;
- de facto power;
- significant influence;
- joint control.

Those are mixed abstraction levels: criteria, indicators, application-guidance paths, and neighbouring conclusions.

### Measurement assessment

IFRS 13 default-risk questions had the same problem. They are better modelled as fair-value measurement assessments, not approach-selection questions.

The model mixed labels for:

- measured objects;
- definition mechanics;
- valuation technique mechanics;
- portfolio exceptions;
- risk-adjustment mechanics.

A more general IFRS system should classify the question type before choosing the intermediate schema. Likely types include peer approach selection, single-framework assessment, measurement assessment, recognition-threshold assessment, eligibility / exemption assessment, and presentation or disclosure assessment.

---

## 9. Evaluation needs to understand polarity

Some variants ask the same issue from opposite directions:

- "Can the exemption apply?"
- "Does this feature prevent the exemption?"

A strict expected recommendation might mark one as `oui_sous_conditions` and the other as `non`, even when the underlying accounting conclusion is consistent.

Answer evaluation needs to separate:

- literal answer polarity;
- underlying accounting conclusion;
- applicability of each treatment;
- recommendation wording.

This matters a lot when variants are positive and negative forms of the same accounting question.

---

## 10. Retrieval recall and answer correctness are separate

The final generalization experiments produced several combinations:

- strong document recall but missing bridge paragraphs;
- perfect chunk recall but unstable approach labels;
- stable recommendation but unstable approach applicability;
- stable labels but disputed expected applicability;
- correct conceptual answer but failed exact eval label.

A useful evaluation system needs layered diagnostics. One score is not enough.

The project therefore separates:

- document-routing diagnostics;
- target-chunk retrieval diagnostics;
- approach-detection diagnostics;
- recommendation checks;
- applicability checks;
- qualitative experiment analysis.