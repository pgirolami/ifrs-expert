# Plan — Simplify and streamline the codebase

## Goal

Reduce code volume and architectural friction after the LangGraph migration while preserving behavior, retrieval outputs, and eval coverage.

This plan optimizes for:

- fewer lines of production and test code;
- shorter high-traffic files;
- fewer shallow modules/classes/functions;
- clearer seams between CLI adapters, workflow orchestration, retrieval, prompt execution, and artifact rendering;
- unchanged SQLite corpus schema and unchanged FAISS vector-store format.

## Success targets

Baseline before implementation:

- `src/commands/answer.py`: 764 LOC
- `src/retrieval/pipeline.py`: 1303 LOC
- `src/retrieval/document_profile_builder.py`: 696 LOC
- `src/commands/store.py`: 926 LOC
- `tests/unit/test_answer_command.py`: 1248 LOC
- `tests/unit/test_store_command.py`: 1547 LOC

Target after implementation:

- `src/commands/answer.py` below 300 LOC.
- No production file above 700 LOC unless it is mostly static data/config.
- Delete or merge shallow pass-through classes/functions only when testability through dependency injection, fakes, or autospecced mocks is preserved; do not force monkey-patching to test behavior.
- Track total LOC across touched production/test files and expect it to decrease, but do not treat LOC reduction as a goal above clarity, locality, or testability.
- Keep or improve existing eval pass rates.

## Non-goals

- Do not change the existing database schema.
- Do not replace FAISS or current vector stores.
- Do not rewrite retrieval behavior for quality changes in this plan.
- Do not introduce generic LangChain RAG abstractions.
- Do not add abstractions unless they remove more surface area than they add.

## Architecture principle

Make modules deeper, not merely smaller.

A module earns its seam only when it hides meaningful implementation complexity behind a smaller interface. If a class or file mostly forwards data to one other function, delete it, inline it, or merge it with the code that owns the behavior.

Use the deletion test for every candidate: if deleting the module makes the system simpler without scattering complexity across callers, delete it.

---

# Milestone 0 — Measure and protect behavior

## Objective

Create a baseline so simplification can be judged by deletion and behavior preservation, not taste.

## Tasks

1. Add a lightweight LOC/report command or script output for the target files.
2. Capture current validation commands:
   - `make lint`
   - targeted unit tests for answer, case analysis, retrieval, store
   - retrieval eval for impacted families as needed
   - answer eval only where explicitly allowed by the user
3. Document the before/after file-size table in the eventual experiment/report commit.

## Stop condition

Do not refactor if current tests/evals are failing for unrelated reasons without documenting them first.

---

# Milestone 1 — Turn `AnswerCommand` into a thin adapter

## Problem

`src/commands/answer.py` still mixes too many responsibilities:

- CLI-level validation;
- prerequisite checks;
- retrieval config construction;
- graph runner construction;
- prompt A/B execution;
- authority filtering;
- citation verification;
- markdown rendering;
- JSON artifact assembly.

Some validation now duplicates `ValidateQuestionStage`, and several helper functions are answer-workflow internals rather than command concerns.

## Target shape

`AnswerCommand` should only:

1. receive CLI/UI options;
2. resolve runtime dependencies;
3. run the case-analysis engine;
4. return `AnswerCommandResult`.

Move the workflow implementation behind one deeper module, for example:

```text
src/case_analysis/engine.py
```

The engine should own graph construction, prompt execution, authority gates, citation verification, and answer rendering.

## Deletions / consolidations

- Delete duplicate policy validation from `AnswerCommand` once `ValidateQuestionStage` is the single owner.
- Move prompt-response parsing out of `AnswerCommand` or reuse existing typed prompt stages directly.
- Move `_build_prompt_b_context`, authority-reference extraction, citation chunk-data construction, and chunk-summary construction into the case-analysis engine or a single answer-rendering helper.
- Keep only prerequisite checks in the command when they are truly CLI/runtime concerns.

## Expected result

- `src/commands/answer.py` below 300 LOC.
- `tests/unit/test_answer_command.py` split by behavior and shortened by testing through the public command plus engine fakes.

## Validation

- `uv run pytest tests/unit/test_answer_command.py tests/unit/test_case_analysis_*.py -q`
- `make lint`
- Q1.0 answer eval only if answer behavior changed.

---

# Milestone 2 — Streamline case-analysis graph without deleting core nodes

## Problem

Some case-analysis workflow code is more ceremonial than it needs to be:

- Graph node methods instantiate stages inline, which creates object churn and spreads workflow wiring across small methods.
- `CaseAnalysisGraphRunner` rebuilds the graph on every run.
- Routing methods repeat the same failure/continue pattern.

`ClassifyAuthorityStage` and `EvaluateApplicabilityStage` are core workflow nodes and should remain explicit in the design, even if their shared implementation can be simplified internally.

## Target shape

Keep LangGraph and keep the core prompt nodes explicit, but reduce ceremony:

- Build and cache the compiled graph once per runner instance.
- Keep `ClassifyAuthorityStage` and `EvaluateApplicabilityStage` as named workflow stages/nodes.
- Consolidate repeated routing/failure conversion code.
- Keep typed result models, but remove aliases/classes that do not add validation or behavior.
- Prefer a small number of named node functions over class-per-node when there is no reusable state.

## Expected result

- Clearer `src/case_analysis/stages.py` with core workflow stages preserved.
- Shorter graph runner with less repetitive routing code.
- No behavior change.

## Validation

- `uv run pytest tests/unit/test_case_analysis_graph.py tests/unit/test_case_analysis_prompt_stages.py tests/unit/test_case_analysis_validation_stages.py -q`
- `make lint`

---

# Milestone 3 — Make retrieval pipeline files shorter without changing retrieval behavior

## Problem

`src/retrieval/pipeline.py` is the largest production file and contains several concerns:

- retrieval strategy selection;
- document routing;
- chunk expansion;
- section-subtree expansion;
- same-family reference expansion;
- result shaping.

This hurts locality: changing reference expansion or document routing requires reading unrelated retrieval paths.

## Target shape

Split by behavior, not by helper-function category:

```text
src/retrieval/pipeline.py              # public execute_retrieval facade and strategy dispatch
src/retrieval/document_routing.py      # document selection/routing behavior
src/retrieval/chunk_expansion.py       # neighbour/full-doc/section expansion
src/retrieval/reference_expansion.py   # same-family reference expansion
```

The public interface remains `execute_retrieval(request, config)`.

## Deletions / consolidations

- Consolidate repeated search/fetch/expand flow across text, title, and document retrieval.
- Replace long parameter lists in expansion helpers with a small internal expansion context object.
- Remove duplicate chunk-expansion helpers from `AnswerCommand` after Milestone 1; they should live in retrieval/case-analysis modules, not in the command adapter.
- Keep private helpers private to the file that owns the behavior.

## Expected result

- `src/retrieval/pipeline.py` below 350 LOC.
- No retrieval file above 700 LOC.
- Retrieval eval output unchanged except for timestamps/artifact paths.

## Validation

- `uv run pytest tests/unit/test_retrieve_command.py tests/unit/test_mixed_corpus_retrieval.py tests/unit/test_target_chunk_retrieval_contract.py -q`
- `make eval-retrieve FAMILY=Q1` or the relevant impacted family/families.
- `make lint`

---

# Milestone 4 — Simplify ingestion/store command surface

## Problem

`src/commands/store.py` is large and tests are larger. The command likely mixes:

- CLI validation;
- PDF extraction;
- chunking;
- document metadata construction;
- persistence;
- vector-index updates;
- status formatting.

## Target shape

Make `StoreCommand` a thin adapter like `AnswerCommand`:

```text
src/ingestion/pipeline.py      # ingest one document end-to-end
src/ingestion/chunking.py      # chunk policy and text splitting
src/ingestion/indexing.py      # vector-index update behavior
```

Only introduce these files if they delete more code from `store.py` and tests than they add.

## Deletions / consolidations

- Centralize repeated test setup for PDF/chunk/vector-store fakes.
- Replace many assertion-heavy tests with table-driven tests around the ingestion pipeline interface.
- Remove compatibility helpers that no longer have multiple callers.

## Expected result

- `src/commands/store.py` below 350 LOC.
- `tests/unit/test_store_command.py` materially shorter and focused on command behavior, not every internal helper.

## Validation

- `uv run pytest tests/unit/test_store_command.py tests/integration/test_ingest_command.py -q`
- `make lint`

---

# Milestone 5 — Consolidate test builders and fakes

## Problem

Large tests repeat setup for policies, chunks, stores, search results, and answer artifacts. That increases LOC and makes refactors expensive.

## Target shape

Create or extend small test builders in `tests/fakes.py` and dedicated fixture modules:

- policy builder;
- chunk builder;
- retrieval-result builder;
- answer-result assertions;
- fake LLM sender with queued responses.

## Deletions / consolidations

- Replace repeated fixture dictionaries with typed builders.
- Remove tests for private helpers that disappear behind deeper modules.
- Keep public behavior tests and eval-backed regression tests.

## Expected result

- Shorter answer/retrieval/store tests.
- Better locality: test failures point to public module behavior, not helper implementation details.

## Validation

- targeted unit tests for changed areas;
- full `make test` after all simplification milestones;
- `make lint`.

---

# Execution order

1. Measure baseline and commit it if needed.
2. Thin `AnswerCommand` first because it is now the main seam into LangGraph.
3. Delete shallow case-analysis wrappers while answer tests are fresh.
4. Shorten retrieval pipeline only after answer behavior is stable.
5. Simplify store/ingestion separately.
6. Consolidate tests continuously, not as a final cleanup dump.

Each milestone should be independently committed with before/after LOC notes in the commit body or PR description.

## Final validation gate

At the end of the plan:

```bash
make lint
make test
make eval-retrieve FAMILY=Q1
```

Run answer evals only under the user's explicit variant restrictions.
