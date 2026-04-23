# Plan — retrieval policy configuration cleanup

## Goal

Replace the current retrieval policy YAML with a cleaner configuration model that separates:

- **mechanism**: the retrieval machinery being used
- **tuning profile**: thresholds, caps, and per-document-type tuning scoped to the compatible mechanism
- **assembled policy**: one named runtime policy that references the chosen mechanism pieces and profiles

The resulting file should work both as:

- the default runtime retrieval configuration
- a **catalog of experimental retrieval configurations** that can be assembled at runtime

This plan is implementation-oriented:

- introduce a typed catalog model in `src/policy.py`
- add an explicit resolver from named assembled policy -> resolved runtime policy
- update request building and command code to consume the resolved policy
- preserve current retrieval behavior while making the config structurally easier to evolve

## Why change the model

The current retrieval config mixes together:

- query embedding behavior
- document routing mechanism
- document routing tuning
- chunk retrieval mechanism
- chunk retrieval thresholds and expansion tuning
- per-document-type routing settings

That makes the file hard to reason about and hard to extend when we want to compare experimental retrieval variants.

The new model should let us describe configurations such as:

- enriched querying + route through chunk results + aggregate to main variant + default dense chunk retrieval
- enriched querying + route through document representations + full-representation routing tuning + default dense chunk retrieval
- enriched querying + return all documents + title_similarity chunk retrieval

without copying the entire config tree for each variant.

## Current state

Today the codebase effectively has these retrieval concerns:

- **querying**
  - `query_embedding_mode`
- **document routing**
  - all-documents behavior for `text` and `titles`
  - document-level routing for `documents` and `documents2`
  - chunk-driven routing plus bundle aggregation for `documents2-through-chunks`
- **chunk retrieval**
  - chunk similarity retrieval
  - title similarity retrieval
- **chunk post-processing**
  - `expand`
  - `expand_to_section`
  - `full_doc_threshold`
- **document-type tuning**
  - per-type `d`
  - per-type `min_score`
  - per-type `expand_to_section`
  - per-type `similarity_representation` when document representations are used

The current YAML shape does not make those boundaries clear.

## Fixed design decisions

### 1. Keep assembled retrieval policies as the runtime-facing unit

The runtime should select one named assembled policy from a catalog, resolve it, and run retrieval from that resolved object.

That gives us:

- named experimental configurations
- simpler runtime logging
- easier snapshot testing
- cleaner CLI/app selection semantics

### 2. Keep `querying` as a separate catalog

`querying` is its own named catalog.

Assembled retrieval policies should reference a named querying entry rather than embedding query settings inline.

### 3. Document routing tuning must be scoped to the routing strategy

A separate top-level `document_routing_profiles` section is misleading because routing tuning depends on the strategy:

- `similarity_representation` matters for document-representation routing
- it does not matter for chunk-driven routing
- future routing strategies may have their own compatible tuning fields

So document routing profiles should live **inside each routing strategy definition**.

That keeps the dependency explicit:

- strategy family
- compatible profiles for that strategy

### 4. Keep document routing post-processing separate

Document routing still benefits from a separate post-processing catalog because it cleanly represents optional transformations over routed candidates, such as:

- no post-processing
- aggregate to main variant
- main variant only

That separation is still useful because post-processing is orthogonal to the routing source, while the profile is not.

### 5. Chunk retrieval tuning must also be scoped to the chunk retrieval strategy

Chunk retrieval has the same dependency problem as document routing:

- `chunk_similarity` supports:
  - filtering
  - expansion tuning
- `title_similarity` supports:
  - filtering
  - but not the same expansion tuning block

So a separate top-level `chunk_retrieval_profiles` catalog is also misleading.

Chunk retrieval profiles should live **inside each chunk retrieval strategy definition**.

That keeps the dependency explicit:

- chunk retrieval strategy family
- compatible profiles for that strategy

### 6. `per_document_k` belongs only to chunk retrieval

Once document routing and chunk retrieval are separated cleanly, `per_document_k` belongs only under:

- `chunk_retrieval_strategies.*.profiles.*.filter.per_document_k`

It should not appear under document routing.

### 7. `similarity_representation` belongs only to document-representation routing profiles

Chunk-driven routing does not use document similarity representations.

So `similarity_representation` should only appear in strategy-scoped routing profiles under:

- `document_routing_strategies.through_document_representation.profiles.*`

### 8. `title_similarity` chunk retrieval does not need extra expansion settings

For `title_similarity` retrieval, the retrieval logic already expands a matched title to the full section subtree.

So title-based chunk retrieval profiles should contain filtering only, not extra expansion settings.

## Desired YAML target shape

This is the desired end state for the policy file:

```yaml
querying: # old: retrieval.query_embedding_mode -> named querying catalog
  raw:
    embedding_mode: raw # old: query_embedding_mode -> embedding_mode

  enriched:
    embedding_mode: enriched # old: query_embedding_mode -> embedding_mode


document_routing_strategies: # old: retrieval.documents + retrieval.mode(document routing branches) -> document_routing_strategies
  return_all:
    source: all_documents

  through_chunks:
    source: top_chunk_results
    profiles:
      q1_authority_family:
        global_d: 25
        by_document_type:
          IFRS-S:
            d: 10
            min_score: 0.55
            expand_to_section: true
          IFRIC:
            d: 10
            min_score: 0.53
            expand_to_section: true

  through_document_representation:
    source: document_representation
    profiles:
      q1_authority_family_full_repr:
        global_d: 25
        by_document_type:
          IFRS-S:
            d: 10
            min_score: 0.55
            expand_to_section: true
            similarity_representation: full
          IFRIC:
            d: 10
            min_score: 0.53
            expand_to_section: true
            similarity_representation: full


document_routing_post_processing: # old: inline routing-specific behavior -> document_routing_post_processing catalog
  none: {}
  aggregate_to_main_variant:
    document_post_processing: aggregate_to_main_variant
  main_variant_only:
    filter: main_variant_only # old: search -> filter


chunk_retrieval_strategies: # old: retrieval.text / retrieval.titles / retrieval.k / retrieval.expand* -> chunk_retrieval_strategies
  dense_chunks:
    mode: chunk_similarity # old: mode value chunk-similarity -> chunk_similarity
    profiles:
      default:
        filter: # old: search -> filter
          min_score: 0.53
          per_document_k: 5
        expansion:
          expand: 0
          expand_to_section: true
          full_doc_threshold: 0

  title_chunks:
    mode: title_similarity # old: mode value title-similarity -> title_similarity
    profiles:
      titles_default:
        filter: # old: search -> filter
          min_score: 0.6
          per_document_k: 5


retrieval_policies: # old: retrieval -> retrieval_policies catalog
  documents2_through_chunks__raw:
    querying: raw
    document_routing:
      strategy: through_chunks
      profile: q1_authority_family
      post_processing: aggregate_to_main_variant
    chunk_retrieval:
      strategy: dense_chunks
      profile: default

  documents2_through_chunks__enriched:
    querying: enriched
    document_routing:
      strategy: through_chunks
      profile: q1_authority_family
      post_processing: aggregate_to_main_variant
    chunk_retrieval:
      strategy: dense_chunks
      profile: default

  standards_only_through_chunks__enriched:
    querying: enriched
    document_routing:
      strategy: through_chunks
      profile: q1_authority_family
      post_processing: main_variant_only
    chunk_retrieval:
      strategy: dense_chunks
      profile: default

  full_documents__enriched:
    querying: enriched
    document_routing:
      strategy: through_document_representation
      profile: q1_authority_family_full_repr
      post_processing: none
    chunk_retrieval:
      strategy: dense_chunks
      profile: default

  text__enriched:
    querying: enriched
    document_routing:
      strategy: return_all
      profile: null
      post_processing: none
    chunk_retrieval:
      strategy: dense_chunks
      profile: default

  titles__enriched:
    querying: enriched
    document_routing:
      strategy: return_all
      profile: null
      post_processing: none
    chunk_retrieval:
      strategy: title_chunks
      profile: titles_default
```

## Naming convention for the target shape

Use one convention consistently:

- **snake_case** for YAML keys
- **snake_case** for enum-like field values
- **snake_case** for named catalog entries

Examples:

- `source: top_chunk_results`
- `mode: chunk_similarity`
- `post_processing: aggregate_to_main_variant`
- `strategy: through_document_representation`

This keeps the file visually consistent and avoids mixing styles within the same config model.

## Resolution model

The runtime should not consume `retrieval_policies` directly in raw YAML form.

Instead, add an explicit resolution step:

1. load the YAML catalog
2. select one named entry from `retrieval_policies`
3. resolve all symbolic references into a **fully assembled resolved retrieval policy**
4. pass that resolved policy to retrieval request building and the retrieval pipeline

The resolver must understand that both document routing profiles and chunk retrieval profiles are scoped under their chosen strategies.

Examples:

- if `document_routing.strategy = through_chunks`, then `document_routing.profile = q1_authority_family` is resolved from:
  - `document_routing_strategies.through_chunks.profiles.q1_authority_family`
- if `document_routing.strategy = through_document_representation`, then `document_routing.profile = q1_authority_family_full_repr` is resolved from:
  - `document_routing_strategies.through_document_representation.profiles.q1_authority_family_full_repr`
- if `document_routing.strategy = return_all`, then `document_routing.profile` must be `null`
- if `chunk_retrieval.strategy = dense_chunks`, then `chunk_retrieval.profile = default` is resolved from:
  - `chunk_retrieval_strategies.dense_chunks.profiles.default`
- if `chunk_retrieval.strategy = title_chunks`, then `chunk_retrieval.profile = titles_default` is resolved from:
  - `chunk_retrieval_strategies.title_chunks.profiles.titles_default`

## Proposed typed model changes

Update `src/policy.py` so it represents both:

- the YAML catalog shape
- the resolved assembled runtime policy shape

Recommended dataclass groups:

### Catalog-level dataclasses

- `QueryingConfig`
- `DocumentRoutingStrategyConfig`
- `DocumentRoutingProfileConfig`
- `DocumentRoutingPostProcessingConfig`
- `ChunkRetrievalStrategyConfig`
- `ChunkRetrievalProfileConfig`
- `RetrievalPolicyReferenceConfig`
- `PolicyCatalog`

Recommended structure detail:

- `DocumentRoutingStrategyConfig` should include:
  - `source`
  - optional `profiles: dict[str, DocumentRoutingProfileConfig]`
- `ChunkRetrievalStrategyConfig` should include:
  - `mode`
  - `profiles: dict[str, ChunkRetrievalProfileConfig]`

### Resolved runtime dataclasses

- `ResolvedQueryingPolicy`
- `ResolvedDocumentRoutingPolicy`
- `ResolvedChunkRetrievalPolicy`
- `ResolvedRetrievalPolicy`

### Resolver API

Add a resolver entry point such as:

- `load_policy_catalog(path: Path) -> PolicyCatalog`
- `resolve_retrieval_policy(catalog: PolicyCatalog, policy_name: str) -> ResolvedRetrievalPolicy`

or equivalent.

## Query command design — closer look

The current query-family commands are not all aligned with the shared retrieval pipeline:

- `query` currently runs text chunk retrieval through the shared retrieval path
- `query-titles` currently runs title search directly
- `query-documents` currently runs document search directly and uses a required `--document-type`

To keep the CLI simple, all of these commands should use the same selection model:

- one required `--retrieval-policy <name>` argument
- no separate mechanism/profile arguments on the CLI
- each command reads only the relevant subset of the selected resolved policy

### Recommendation

Use one retrieval-policy selector everywhere.

Specifically:

- `retrieve` and `answer` should read a full assembled retrieval policy via `--retrieval-policy` and the code should be shared
- `query`, `query-titles`, and `query-documents` should also read a full assembled retrieval policy via `--retrieval-policy`
- each query-family command should validate that the selected policy is compatible with that command’s role

This keeps the UX simple while preserving a single policy model across the application.

### Recommended query-family behavior

#### `query`

Define `query` as a **chunk retrieval diagnostic**.

It should read from the selected resolved retrieval policy:

- `querying`
- `chunk_retrieval`

It should not read document routing.

Compatibility rule:

- require `chunk_retrieval.mode = chunk_similarity`
- reject policies that resolve to `title_similarity`

This command should run only dense chunk retrieval plus chunk expansion.

#### `query-titles`

Define `query-titles` as a **title retrieval diagnostic**.

It should read from the selected resolved retrieval policy:

- `querying`
- `chunk_retrieval`

Compatibility rule:

- require `chunk_retrieval.mode = title_similarity`
- reject policies that resolve to `chunk_similarity`

This command should run only title-similarity retrieval and section-subtree expansion.

#### `query-documents`

This command deserves the closest review.

Recommendation: define `query-documents` as a **document-routing-stage diagnostic** that keeps an explicit `--document-type` parameter.

It should read from the selected resolved retrieval policy:

- `querying`
- `document_routing`
- and, when `document_routing.source = top_chunk_results`, also the relevant chunk-retrieval filtering inputs that produce those routing candidates

It should also read from the CLI:

- `--document-type <DOC_TYPE>`

The role of `--document-type` in the new model should be:

- constrain or filter the document-routing diagnostic output to one exact document type
- not replace `--retrieval-policy`
- not act as the primary policy-definition mechanism

Concretely:

- for `document_routing.source = document_representation`
  - read `querying`
  - read `document_routing`
  - apply `--document-type` when selecting/reporting document candidates
  - do not read chunk expansion settings
- for `document_routing.source = top_chunk_results`
  - read `querying`
  - read `document_routing`
  - read `chunk_retrieval.mode` and the `chunk_retrieval.filter` settings needed to generate routing candidates
  - apply `--document-type` when selecting/reporting document candidates
  - do **not** read `chunk_retrieval.expansion`, because routing should be based on raw candidate generation, not post-retrieval chunk expansion
- for `document_routing.source = all_documents`
  - read `querying`
  - read `document_routing`
  - apply `--document-type` to the returned document set

### What parts of the policy each command should read

#### `answer`
Reads the full resolved retrieval policy.

#### `retrieve`
Reads the full resolved retrieval policy.

#### `query`
Reads only:

- `querying`
- `chunk_retrieval`

#### `query-titles`
Reads only:

- `querying`
- `chunk_retrieval`

#### `query-documents`
Reads:

- `querying`
- `document_routing`
- and, for chunk-driven routing only, the chunk-retrieval candidate-generation subset:
  - `chunk_retrieval.mode`
  - `chunk_retrieval.filter`
- plus CLI parameter:
  - `--document-type`

### Command definition implications

This leads to a clean command model:

- all retrieval-related commands accept `--retrieval-policy`
- full execution commands (`retrieve`, `answer`) consume the whole resolved policy
- query-family commands consume only the subset that matches their diagnostic role
- `query-documents` additionally keeps `--document-type`
- compatibility is enforced by command-side validation rather than many mechanism-specific CLI arguments

### `query-documents` and `--document-type`

Under this model, `query-documents` should keep `--document-type` as an explicit command parameter.

However, it should no longer treat `--document-type` as the primary policy-definition mechanism.

Recommended role:

- keep `--document-type`
- use `--retrieval-policy` to select the retrieval configuration
- use `--document-type` to constrain or filter the diagnostic document output within that selected policy

So the command contract becomes:

- retrieval behavior comes from `--retrieval-policy`
- document-type focus comes from `--document-type`

## Implementation plan

### Phase 1 — add the catalog model and resolver

Update `src/policy.py` to:

- parse the new catalog layout
- validate named references
- validate allowed mechanism values
- validate strategy/profile compatibility
- validate per-document-type coverage where profiles require it
- resolve one named assembled policy into a concrete runtime object

Validation to add:

- unknown querying reference fails
- unknown routing strategy fails
- unknown routing post-processing fails
- unknown routing profile for the chosen strategy fails
- routing profile supplied for a strategy that has no profiles fails
- missing routing profile for a strategy that requires profiles fails
- unknown chunk retrieval profile for the chosen strategy fails
- missing chunk retrieval profile for a strategy that requires profiles fails
- invalid `embedding_mode` fails
- invalid `chunk_retrieval.mode` fails
- invalid routing `source` fails
- invalid score/cap values fail

### Phase 2 — require runtime selection of one named retrieval policy

Add an explicit retrieval policy selector.

Recommended behavior:

- the config contains a named catalog under `retrieval_policies`
- the runtime chooses one named policy by name
- there is **no YAML default** and no implicit fallback
- CLI/app callers must pass the desired retrieval policy explicitly

Recommended implementation:

- add a required CLI/app argument such as `--retrieval-policy <name>` for commands that execute an assembled retrieval policy
- resolve that selected name before building a `RetrievalRequest`

This keeps policy choice explicit and makes experiments easier to reason about.

### Phase 3 — adapt retrieval request building to the resolved policy

Update request-building code so it reads from `ResolvedRetrievalPolicy` instead of the current flat `RetrievalPolicy` structure.

Files likely affected:

- `src/commands/retrieval_request_builder.py`
- `src/commands/retrieve.py`
- `src/commands/answer.py`

Concrete changes:

- querying uses resolved `embedding_mode`
- document routing uses resolved `source`, optional post-processing, and optional resolved strategy-scoped profile
- chunk retrieval uses resolved `mode` and resolved strategy-scoped profile content

Note: the query-family commands should be handled separately from full assembled retrieval policy consumers.

### Phase 4 — map assembled policies to existing runtime behavior

Keep runtime behavior the same while changing only the config model.

Expected mapping:

- `text__enriched`
  - all_documents routing
  - `chunk_similarity` retrieval
- `titles__enriched`
  - all_documents routing
  - `title_similarity` retrieval
- `documents2_through_chunks__enriched`
  - `top_chunk_results` routing
  - `aggregate_to_main_variant` post-processing
  - dense chunk retrieval
- `full_documents__enriched`
  - `document_representation` routing
  - no routing post-processing
  - dense chunk retrieval

The resolver should make this mapping explicit and testable.

### Phase 5 — rewrite `config/policy.default.yaml` into the new catalog shape

Replace the old monolithic shape with the catalog structure shown above.

Keep current numeric values unless a value needs to move because of the new split.

The rewritten default config should be usable both as:

- the default runtime configuration
- a catalog of experimental retrieval variants for evaluation scripts

### Phase 6 — update tests around policy loading and retrieval behavior

Add focused tests for:

#### Policy catalog and resolution

- policy catalog loads successfully
- one named retrieval policy resolves correctly
- invalid references fail with clear errors
- resolved policy snapshots match expected assembled objects
- routing profile resolution is strategy-scoped
- chunk retrieval profile resolution is strategy-scoped

#### Retrieval semantics

- `documents2_through_chunks__enriched` uses:
  - chunk-based routing
  - `aggregate_to_main_variant` post-processing
  - `chunk_similarity` retrieval
- `full_documents__enriched` uses:
  - document-representation routing
  - `full` similarity representation from the strategy-scoped profile
- `titles__enriched` uses:
  - `title_similarity` retrieval
  - no extra chunk expansion block
- `per_document_k` is read only from `chunk_retrieval_strategies.*.profiles.*.filter`
- `similarity_representation` is required only where document-representation routing needs it

## Files likely touched

### Policy loading and resolution

- `src/policy.py`
- possibly a small helper module if resolution logic becomes large

### Command / request-building layer

All retrieval-related commands should accept `--retrieval-policy` and then read the relevant subset of the resolved policy.

Files likely affected:

- `src/commands/retrieval_request_builder.py`
- `src/commands/retrieve.py`
- `src/commands/answer.py`
- `src/commands/query.py`
- `src/commands/query_titles.py`
- `src/commands/query_documents.py`
- CLI/app wiring for required `--retrieval-policy`

### Tests

- policy loading tests
- retrieval request builder tests
- retrieve/answer command tests
- query-family command tests using `--retrieval-policy`
- tests that pin resolved assembled policy behavior

## Risks

### 1. Resolver complexity drifts upward

If the resolver becomes too clever, it will be hard to debug.

Mitigation:

- keep catalogs shallow
- produce one explicit resolved object
- log the selected policy name and resolved settings

### 2. The config allows combinations the runtime does not support yet

The catalog model is more flexible than the current code paths.

Mitigation:

- validate supported combinations during resolution
- fail fast with explicit errors for unsupported assembled policies

### 3. Old tests may still assume the monolithic policy shape

Mitigation:

- migrate tests in layers
- add policy-resolution tests first
- then move command tests to resolved policy objects

## Success criteria

This cleanup is successful when:

1. the YAML file cleanly separates mechanism catalogs, strategy-scoped tuning profiles, and assembled retrieval policies
2. one named retrieval policy can be resolved into a concrete runtime policy object
3. the default policy file can act as a catalog of experimental retrieval configurations
4. document routing profiles are visibly scoped to the strategy that uses them
5. chunk retrieval profiles are visibly scoped to the strategy that uses them
6. chunk retrieval and document routing each read only the settings that belong to their stage
7. `similarity_representation` appears only where document-representation routing needs it
8. `title_similarity` retrieval does not carry redundant expansion settings
9. the retrieval pipeline behavior remains unchanged for the current named policies
10. adding a new experimental retrieval policy no longer requires copying the entire config tree
