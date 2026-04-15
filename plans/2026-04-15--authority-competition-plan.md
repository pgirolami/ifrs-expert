# Plan — authority competition, per-variant document caps, and document kind metadata

## Goal

Reduce authority confusion during retrieval and Prompt A authority classification by doing two things together:

1. make document-stage limits apply **per exact document type / variant**, not through one shared cross-type counter
2. persist new `document_kind` field so system can distinguish normative standards from interpretations and secondary materials

This slice now also standardizes policy-config loading across the command surface:

- `query`
- `query-documents`
- `query-titles` where applicable
- `retrieve`
- `answer`

This plan assumes the recent IFRS multi-variant ingestion work is the baseline:

- `IFRS-S`
- `IFRS-BC`
- `IFRS-IE`
- `IFRS-IG`
- `IAS`
- `IFRIC`
- `SIC`
- `NAVIS`
- `PS`

## Problem statement

### 1. Shared cross-type document caps are suppressing useful variant coverage

Today the document-stage pipeline buckets by a shared type bucket via `infer_document_family(doc_uid)`.

That means all IFRS variants currently compete inside one shared `IFRS` counter:

- Standard
- Basis for Conclusions
- Illustrative Examples
- Implementation Guidance

So the old shared-bucket behavior effectively acts like:

- **one shared cap across all IFRS variants**

but the desired behavior is:

- **one independent cap per exact document type / variant**

We do **not** want `--ifrs-d` or any other broader-bucket equivalent anymore.
We want separate exact-type settings in policy, for example:

- `IFRS-S.d`
- `IFRS-BC.d`
- `IFRS-IE.d`
- `IFRS-IG.d`

subject to the overall global document cap `-d/--d`.

### 2. All documents effectively compete with the same authority weight

Even after retrieving the right variants, the downstream prompt context does not currently expose a durable machine-readable notion of document authority class.

That causes predictable confusion between:

- governing standards
- interpretations
- implementation guidance
- illustrative examples
- basis for conclusions

### 3. We need a stable authority taxonomy that is separate from `document_type`

`document_type` should keep identifying the exact source type / variant.

We now also need a separate field, `document_kind`, to express the authority role used in prompting, ranking, and explanation.

## Fixed decisions

### New metadata field

Add a new persisted document field:

- `document_kind`

Supported values:

- `standard`
- `interpretation`
- `implementation_guidance`
- `illustrative_examples`
- `basis_for_conclusions`

### Exact document-type → document-kind mapping

Use this mapping:

- `IFRS` -> `standard`
- `IFRS-S` -> `standard`
- `IAS` -> `standard`
- `IFRIC` -> `interpretation`
- `SIC` -> `interpretation`
- `NAVIS` -> `interpretation`
- `IFRS-IG` -> `implementation_guidance`
- `IFRS-IE` -> `illustrative_examples`
- `IFRS-BC` -> `basis_for_conclusions`
- `PS` -> `standard` unless we explicitly decide otherwise later

If `PS` should receive a different kind later, treat that as a separate follow-up decision rather than blocking this slice.

### Policy YAML semantics

All retrieval-aware commands should move to a **mandatory YAML policy file** instead of growing permanent CLI knobs.

That file should be intentionally broader than retrieval.
This slice requires a `retrieval` section, and the schema / loader should leave room for future sections such as:

- `prompts`
- `output`

The `retrieval` section should define document-stage tuning by exact `document_type`, including:

- `d`
- `min_score`
- `expand_to_section`

for every supported exact type.

Examples:

- `IFRS-S`
- `IFRS-BC`
- `IFRS-IE`
- `IFRS-IG`
- `IAS`
- `IFRIC`
- `SIC`
- `NAVIS`
- `PS`

The overall global `d` cap still remains a hard stop on total selected documents.

Preferred semantics:

- retrieval selection counts by **exact persisted `document_type`**
- policy YAML is required input for all retrieval-aware commands:
  - `query`
  - `query-documents`
  - `query-titles` where applicable
  - `retrieve`
  - `answer`
- CLI should carry a path to policy YAML, not a large matrix of tuning flags
- no broader-bucket policy surface remains

### Alternative rejected — exact per-type CLI parameters

One possible solution would be separate CLI knobs for every exact `document_type`, such as:

- `--ifrs-s-d`
- `--ifrs-s-min-score`
- `--ifrs-s-expand-to-section`
- `--ifrs-bc-d`
- `--ifrs-bc-min-score`
- `--ifrs-bc-expand-to-section`
- `--ifrs-ie-d`
- `--ifrs-ie-min-score`
- `--ifrs-ie-expand-to-section`
- `--ifrs-ig-d`
- `--ifrs-ig-min-score`
- `--ifrs-ig-expand-to-section`
- plus exact-type knobs for `IAS`, `IFRIC`, `SIC`, `NAVIS`, and `PS`

Under that design, retrieval would count by exact `document_type` directly, with no extra expansion step.

#### Pros

- semantics are explicit: each exact document type has its own cap and min score
- retrieval logic becomes simpler because selection uses exact types end to end
- future IFRS.org variant tuning becomes easier because there is no hidden cross-type translation
- easier to experiment with different thresholds for `IFRS-S` vs `IFRS-BC` vs `IFRS-IE` vs `IFRS-IG`

#### Cons

- CLI surface becomes too large and system becomes knob-heavy
- `RetrieveOptions`, `AnswerOptions`, parser help text, and tests get noisier
- adding new document types later means more CLI flags, more docs, and more test churn
- one-off command invocations become harder to read and compare

#### Implementation difficulties

- current options model is not exact-type shaped, so moving to many CLI fields touches commands, defaults, tests, wrappers, and Streamlit defaults
- validation surface grows because every exact type needs defaults, error handling, and logging
- risk of drift rises if exact-type defaults are duplicated across `retrieve`, `answer`, eval scripts, and UI entry points

This is not current preference.

### Preferred design — mandatory policy config file

Exact per-type tuning surface is now large enough that a policy config file makes more sense at system level.

Example direction:

```yaml
retrieval:
  documents:
    global_d: 25
    global_doc_min_score: null
    by_document_type:
      IFRS-S:
        d: 4
        min_score: 0.58
        expand_to_section: true
      IFRS-BC:
        d: 2
        min_score: 0.62
        expand_to_section: false
      IFRS-IE:
        d: 2
        min_score: 0.60
        expand_to_section: false
      IFRS-IG:
        d: 2
        min_score: 0.60
        expand_to_section: false
      IAS:
        d: 4
        min_score: 0.40
        expand_to_section: true
      IFRIC:
        d: 6
        min_score: 0.48
        expand_to_section: true
      SIC:
        d: 6
        min_score: 0.40
        expand_to_section: true
      NAVIS:
        d: 2
        min_score: 0.60
        expand_to_section: true
      PS:
        d: 1
        min_score: 0.40
        expand_to_section: true
```

#### Pros

- scales better than adding many permanent CLI flags
- tuning policy becomes durable, reviewable, and reusable across CLI, Streamlit, and eval runs
- the file can grow beyond retrieval into prompt customization and output controls
- reduces parser bloat and centralizes defaults
- keeps system policy in one place instead of scattering knobs through commands and wrappers

#### Cons

- behavior becomes less obvious at command line unless effective config is logged clearly
- requires stronger validation and better observability to avoid silent bad configs
- adds another artifact that must stay in sync with code and docs
- quick one-off terminal experiments need config editing or config swapping instead of ad hoc flags

#### Implementation difficulties

- need shared config schema and loader with strict validation
- need a typed root config model that can grow beyond retrieval
- need updates across command construction, tests, wrappers, and UI settings
- need Promptfoo defaults and script wrappers to stop encoding retrieval knobs inline

#### Impact on CLI commands and Promptfoo

Mandatory YAML changes both local command usage and eval workflow.

For CLI:

- `query` should require something like `--policy-config <path>` when command uses retrieval policy
- `query-documents` should require same
- `query-titles` should use same pattern if title-stage policy remains configurable
- `retrieve` should require same
- `answer` should require same
- command help gets smaller because tuning knobs move out of parser surface
- reproducibility improves because one named YAML captures retrieval policy and can later carry prompt/output policy too

For Promptfoo:

- `promptfoo_src/base.yaml` should stop carrying large answer-command retrieval knob blocks
- Promptfoo provider config should instead pass only `policy-config` path, which decouples provider wiring from policy content
- `scripts/run_answer.py` should load or forward `policy-config` path rather than rebuild many scalar retrieval options
- `scripts/run_promptfoo_eval.py` should copy the effective policy YAML into the run folder
- `scripts/run_promptfoo_eval.py` should also copy the effective Prompt A template and Prompt B template into the run folder
- eval comparisons become cleaner because policy plus prompt templates become explicit experiment artifacts

No automatic migration of prior experiments or archived eval runs is needed in this slice.
They can remain untouched.
Main affected surfaces are:

- `promptfoo_src/base.yaml`
- `scripts/run_promptfoo_eval.py`
- `scripts/run_answer.py`
- tests that currently assert individual retrieval flags or Promptfoo option extraction

#### Recommendation relative to this plan

This is current preference for this branch:

1. move all retrieval-aware commands to mandatory policy YAML
2. keep the root file broader than retrieval, with `retrieval` required now and room for `prompts` / `output`
3. key retrieval policy by exact `document_type`
4. remove the large CLI knob matrix
5. update Promptfoo and helper scripts to pass `policy-config` path and archive policy / prompt templates in the run folder

### Configs and options architecture

Commands should **not** receive a raw dict parsed from YAML.

Preferred architecture:

`YAML -> strict validation -> typed dataclass config -> commands consume typed objects`

Keep dataclasses.
Do not pass loose dict through the command layer.

Recommended split:

- **root policy dataclass** holds YAML-backed system policy
- **nested retrieval / prompts / output dataclasses** hold validated policy sections
- **small command option dataclasses** hold invocation-specific runtime options

Examples of policy concerns:

- exact-type document `d`
- exact-type document `min_score`
- exact-type `expand_to_section`
- global document cap
- content min score
- retrieval mode defaults
- prompt-specific extra instructions
- output configuration switches

Examples of runtime option concerns:

- query text
- output format
- verbosity
- output directory
- save-all

Important boundary rule:

- command constructors should receive typed policy objects and should not know YAML schema directly
- YAML parsing and validation should happen once in a shared loader layer
- dynamic exact-type entries may still live inside dataclass fields as `dict[str, ...]`
- raw dict should not be the command boundary because it weakens validation, typing, and test clarity

### Authority behavior

This slice should improve authority handling in two layers:

1. **selection layer** — ensure the candidate set contains enough documents from each relevant exact type
2. **prompting layer** — expose `document_type` and `document_kind` so Prompt A can classify authority with less ambiguity

This slice does **not** need to hard-code a fully deterministic authority ranking engine yet.
It only needs to provide the correct metadata and retrieval behavior so the LLM is no longer blind.

## Proposed implementation

### Phase 1 — add tests that reproduce current cap bug and define policy behavior

Add retrieval tests showing that exact IFRS variants currently compete inside one shared cap, then codify desired exact-type behavior driven by policy YAML.

Minimum cases:

1. policy YAML with exact-type entries for:
   - `IFRS-S`
   - `IFRS-BC`
   - `IFRS-IE`
   - `IFRS-IG`

   and ranked document hits for:
   - `ifrs9` (`IFRS-S`)
   - `ifrs9-bc` (`IFRS-BC`)
   - `ifrs9-ie` (`IFRS-IE`)
   - `ifrs9-ig` (`IFRS-IG`)

   Expected: one document from **each exact type** can survive when each exact type has `d: 1`, still bounded by global `d`.

2. verify global `d` still truncates final selection order after per-type caps are applied

3. verify exact-type `expand_to_section` policy is honored, e.g. `IFRS-S` can expand while `IFRS-BC` and `IFRS-IE` do not

4. verify retrieval-aware commands reject runs with no policy YAML:
   - `query`
   - `query-documents`
   - `query-titles` where applicable
   - `retrieve`
   - `answer`

5. verify commands consume typed policy objects rather than raw YAML dicts at the command boundary

6. verify retrieval fails fast when an exact `document_type` cannot be resolved for a candidate document

Prefer unit tests around YAML loading plus `src/retrieval/pipeline.py`, then command-level tests for `QueryCommand`, `QueryDocumentsCommand`, `QueryTitlesCommand` where applicable, `RetrieveCommand`, `AnswerCommand`, Promptfoo wrapper parsing, and script integration.

### Phase 2 — introduce exact-type helpers and policy schema

Add explicit helpers so the retrieval layer stops overloading approximate buckets and add a YAML-backed policy model.

Suggested helpers / models:

- `infer_exact_document_type(doc_uid: str) -> str | None`
- `resolve_document_kind(document_type: str | None) -> str | None`
- root policy dataclass plus nested retrieval / prompts / output config dataclasses
- retrieval policy dataclasses keyed by exact `document_type`
- small command option dataclasses for non-policy runtime args
- YAML loader + strict validator for policy config

Important rules:

- pipeline should select against **exact persisted document type**
- policy YAML should be exact-type keyed
- `expand_to_section` should also be exact-type keyed
- no broader grouping helper remains in the operational policy surface

### Phase 3 — change document-stage selection to count by exact type

Update `src/retrieval/pipeline.py`:

- replace shared cross-type counters with exact-type counters
- resolve exact document type for each document hit and fail fast if it is missing or unsupported
- apply YAML-provided per-exact-type `d` and `min_score` thresholds
- keep global `d` cap unchanged

This should be implemented in a way that is transparent in logs, e.g.:

- policy-config path
- resolved exact type
- effective per-type cap
- effective per-type min score
- effective per-type `expand_to_section`
- selected count by exact type
- whether the hit was skipped due to cap or threshold

### Phase 4 — persist `document_kind` in the database and model layer

Add a migration, likely:

- `011_add_document_kind.sql`

Update:

- `src/migrations/000_schema.sql`
- `src/models/document.py`
- `src/db/documents.py`
- `tests/fakes.py`
- any fixture helpers that construct `DocumentRecord`

`DocumentRecord` should gain:

- `document_kind: str | None = None`

Persistence behavior:

- if `document_kind` is explicitly provided by extraction, store it
- otherwise derive it from resolved `document_type`
- for existing rows in the active corpus, backfill `document_kind` from stored `document_type`

### Phase 5 — assign `document_kind` during extraction and storage

Update extraction / storage paths so every stored document gets both:

- exact `document_type`
- derived `document_kind`

At minimum update:

- IFRS HTML extractor
- Navis HTML extractor
- PDF fallback path
- store finalization logic
- document upsert logic

If extraction cannot determine a supported exact `document_type`, fail fast rather than storing ambiguous metadata.

This should avoid re-deriving authority ad hoc later.

### Phase 6 — require policy YAML on retrieval-aware commands and update CLI + Promptfoo flow

Update command entry points so policy YAML becomes mandatory wherever command behavior depends on retrieval policy.

At minimum update:

- `src/cli.py`
- `src/commands/query.py`
- `src/commands/query_documents.py`
- `src/commands/query_titles.py` where applicable
- `src/commands/retrieve.py`
- `src/commands/answer.py`
- `promptfoo_src/base.yaml`
- `scripts/run_answer.py`
- `scripts/run_promptfoo_eval.py`

Key changes:

- remove the retrieval tuning matrix from the main CLI surface for retrieval-aware commands
- remove `--expand-to-section` from the main CLI surface and move it into exact-type policy entries
- require `--policy-config` instead
- parse YAML once into typed policy dataclasses
- pass typed policy objects into commands
- keep small command option dataclasses only for non-policy runtime args
- ensure Promptfoo provider config carries only `policy-config` path, not embedded retrieval knobs
- copy the effective policy YAML into the Promptfoo run folder
- copy the effective Prompt A and Prompt B templates into the Promptfoo run folder
- record the source paths and content hashes for those artifacts in run metadata
- keep logs explicit about which policy config was used

### Phase 7 — surface `document_type` and `document_kind` in document-first and prompt context

The LLM currently sees mostly `doc_uid` plus chunk text.
That is not enough once several related variants are present.

Update prompt context formatting so each document block exposes structured metadata, for example:

```xml
<Document name="ifrs9-bc" document_type="IFRS-BC" document_kind="basis_for_conclusions">
...
</Document>
```

Do the same wherever document-first retrieval results are shown or serialized and where that extra metadata is helpful.

Prompt A instructions should then explicitly tell the model to treat:

- `standard`
- `interpretation`

as more authoritative than:

- `implementation_guidance`
- `illustrative_examples`
- `basis_for_conclusions`

without forbidding the latter from being used as supporting or peripheral authority.

### Phase 8 — update memo / reporting helpers to group and label correctly

Current reporting should group documents by exact `document_type`.
It should not collapse several variants into one broader bucket.

Update relevant formatting helpers so they can display:

- exact `document_type`
- `document_kind`

At minimum review:

- `src/b_response_utils.py`
- any query / retrieve JSON output that currently emits only `document_type`

### Phase 9 — validate backfill and mixed-corpus behavior

Add integration coverage for a mixed corpus containing:

- IFRS standard + BC + IE + IG
- IAS standard
- IFRIC / SIC
- NAVIS

Validate that:

1. stored rows have both `document_type` and `document_kind`
2. document-stage retrieval applies YAML-specified exact-type limits correctly
3. exact-type `expand_to_section` behavior is honored
4. Prompt A context contains enough metadata to distinguish governing vs supporting materials
5. legacy documents without explicit extractor metadata are still assigned a sensible kind through fallback derivation from stored `document_type`

## Validation checklist

Before implementation is considered done, verify:

- missing policy YAML causes retrieval-aware commands to fail fast with a clear error
- missing or unsupported exact `document_type` causes retrieval to fail fast with a clear error
- YAML keyed by exact `document_type` controls document-stage caps, min scores, and `expand_to_section`
- no shared cross-type cap remains across IFRS variants
- `-d/--d` still limits total documents globally
- `document_kind` is persisted for newly ingested documents
- existing active-corpus documents are backfilled correctly
- Navis, IFRIC, and SIC resolve to `interpretation`
- `IFRS-BC` resolves to `basis_for_conclusions`
- `IFRS-IE` resolves to `illustrative_examples`
- `IFRS-IG` resolves to `implementation_guidance`
- Prompt A context exposes exact type and kind for each document block
- Promptfoo run folders contain the copied policy YAML plus Prompt A / Prompt B templates

## Deliverables

- new migration for `document_kind`
- updated `DocumentRecord` and document persistence
- generic policy YAML schema and loader, with `retrieval` required now and room for `prompts` / `output`
- `query`, `query-documents`, `query-titles` where applicable, `retrieve`, and `answer` moved to mandatory policy YAML
- retrieval-pipeline change from shared cross-type counting to exact-type counting with YAML-provided exact-type policy
- typed policy dataclasses plus small runtime option dataclasses
- exact-type `expand_to_section` policy support
- Promptfoo and helper-script updates to pass `policy-config` path and archive the effective policy YAML plus Prompt A / Prompt B templates in run folders
- prompt/context formatting updates exposing `document_type` and `document_kind`
- unit and integration tests covering cap fix, policy config, `expand_to_section`, and kind mapping

## Suggested branch scope boundaries

This branch should handle:

- data model changes for `document_kind`
- mandatory policy YAML for retrieval-aware commands
- typed config boundary for commands instead of raw dict passing
- exact-type retrieval policy semantics
- exact-type `expand_to_section` policy semantics
- Promptfoo / helper-script updates to pass `policy-config` path and archive run artifacts
- prompt metadata surfacing for authority classification

This branch should **not** also try to redesign the whole authority-classification prompt/output schema beyond the minimum needed to consume the new metadata.
