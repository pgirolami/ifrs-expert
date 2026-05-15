# Plan — Pydantic AI migration

## Goal

Migrate IFRS Expert's LLM-facing Python code to **Pydantic AI** while preserving the existing corpus database, FAISS vector stores, retrieval policy catalog, and retrieval behavior.

The migration should make the answer pipeline more type-safe, observable, and reliable without turning the existing domain-specific retriever into generic LangChain/LlamaIndex RAG.

## Non-goals

- Do not change the SQLite corpus schema.
- Do not replace FAISS or regenerate vector stores as part of this migration.
- Do not replace `src/retrieval/pipeline.py` behavior in the first pass.
- Do not adopt classic LangChain RAG abstractions for retrieval.
- Do not use Pydantic AI's graph support as the main case-file workflow runtime yet; keep that decision separate from the LLM contract migration.

## Why Pydantic AI here

The current code already has strong custom retrieval. The weaker layer is the LLM contract layer:

- provider wrappers live in `src/llm/*`;
- Prompt A and Prompt B return raw JSON strings;
- `AnswerCommand` parses responses with `json.loads()` and manual coercion;
- invalid LLM outputs become runtime failures instead of schema-guided retries;
- prompt orchestration, artifact assembly, rendering, and LLM calls are mixed in `src/commands/answer.py`.

Pydantic AI directly helps with:

- typed `Agent[Deps, Output]` contracts;
- Pydantic output validation;
- structured-output retries;
- dependency injection for retrieved context and citation maps;
- provider-agnostic model configuration;
- streaming and usage metadata;
- Logfire/OpenTelemetry-compatible instrumentation later.

## Target architecture

Keep the current retrieval stack:

```text
SQLite stores + FAISS stores + retrieval policy catalog + execute_retrieval()
```

Introduce a typed LLM/application layer:

```text
src/ai/
  __init__.py
  models.py              # provider/model resolution for Pydantic AI
  agents/
    authority.py          # Prompt A replacement/wrapper
    applicability.py      # Prompt B replacement/wrapper
    follow_up.py          # grounded follow-up agent
  schemas/
    authority.py          # Prompt A output models
    answer.py             # Prompt B output models
    citations.py          # citation support models
  services/
    context_builder.py    # chunk formatting and citation metadata
    answer_runner.py      # runs typed agents over retrieved material
```

The exact module names may change, but these boundaries should stay stable:

1. retrieval stays separate from LLM generation;
2. LLM outputs are Pydantic models, not generic JSON;
3. markdown rendering receives typed objects or explicit DTOs;
4. provider selection is centralized.

---

# Phase 1 — Add Pydantic schemas around current outputs

## Objective

Define typed models for the existing Prompt A and Prompt B JSON contracts without changing prompts or provider code yet.

## Work

1. Add `pydantic` / `pydantic-ai` dependency via `uv`.
2. Create Pydantic models for current Prompt A output:
   - primary accounting issue;
   - authority classification;
   - excluded/superseded material;
   - treatment families;
   - candidate approaches;
   - clarification payload.
3. Create Pydantic models for current Prompt B output:
   - answer summary;
   - approach applicability results;
   - reasoning;
   - practical implications;
   - citations;
   - limitations / missing facts.
4. Replace `_parse_json_value()` usage in the answer path with `model_validate_json()` behind a compatibility adapter.
5. Keep `AnswerCommandResult.prompt_a_json` and `prompt_b_json` populated for current renderers/tests until downstream code is migrated.

## Acceptance criteria

- Existing answer command behavior remains compatible.
- Invalid Prompt A/B JSON now produces validation errors with field-level detail.
- Unit tests cover valid and invalid Prompt A/B outputs.
- Existing promptfoo/retrieval eval entry points still run.

---

# Phase 2 — Introduce Pydantic AI agents for Prompt A and Prompt B

## Objective

Replace direct `send_to_llm_fn(prompt) -> str` calls with typed Pydantic AI agents, while keeping prompt text and retrieval context stable.

## Work

1. Prefer Pydantic AI's native model/provider configuration where it covers the current providers. Add a thin local compatibility adapter only where needed to keep the existing CLI, retrieval evals, and answer evals runnable during migration.
2. Implement `AuthorityAnalysisAgent`:
   - input deps: question, formatted chunks, chunk summary, retrieval metadata;
   - output: Prompt A Pydantic model;
   - instructions: current `prompts/answer_prompt_A.txt` content adapted with explicit schema expectations.
3. Implement `ApplicabilityAnalysisAgent`:
   - input deps: question, Prompt A typed output, pruned context, citation metadata;
   - output: Prompt B Pydantic model;
   - instructions: current `prompts/answer_prompt_B.txt` content adapted with explicit schema expectations.
4. Configure output retries for schema failures.
5. Preserve raw run messages/artifacts where useful for debugging.
6. Keep a fallback compatibility path to the old LLM clients during initial rollout.

## Acceptance criteria

- Prompt A and Prompt B return typed models from Pydantic AI.
- Existing markdown rendering still produces memo and FAQ output.
- LLM provider selection still supports the currently used providers where practical.
- Tests use fake Pydantic AI agent runners rather than real providers.

---

# Phase 3 — Extract LLM orchestration out of `AnswerCommand`

## Objective

Make `AnswerCommand` a thin command wrapper over retrieval + typed answer services.

## Work

1. Create an `AnswerGenerationService` that accepts:
   - question;
   - resolved retrieval policy;
   - retrieval dependencies;
   - typed agent runners.
2. Move prompt/context building out of `src/commands/answer.py` into service modules.
3. Move Prompt B context pruning into a testable `ContextBuilder`.
4. Move markdown preparation into a rendering adapter.
5. Keep CLI and Streamlit public behavior unchanged.

## Acceptance criteria

- `src/commands/answer.py` is materially smaller and mostly delegates.
- Unit tests can exercise Prompt A/B orchestration without filesystem prompts or live LLMs.
- Existing CLI tests and UI tests pass.

---

# Phase 4 — Citation and authority validation as deterministic gates

## Objective

Use typed outputs to add deterministic checks before final rendering.

## Work

1. Build a citation index from retrieved chunks and Prompt B context.
2. Validate that cited chunk/document IDs exist in the allowed context.
3. Validate that final conclusions do not cite excluded/superseded material unless explicitly labelled.
4. Add warnings or failures to the answer artifact.
5. Add an optional repair loop through Pydantic AI only when validation errors are mechanical and recoverable.

## Acceptance criteria

- Unsupported citation IDs are detected before markdown rendering.
- Superseded/excluded authority cannot silently support final conclusions.
- Validation results are visible in `AnswerCommandResult` artifacts.

---

# Phase 5 — Follow-up chat migration

## Objective

Replace the current follow-up prompt stuffing in `src/ui/chat_service.py` with a typed grounded follow-up agent.

## Work

1. Define a `GroundedFollowUpDeps` model containing:
   - first question;
   - typed first answer;
   - retrieved source/citation summary;
   - prior follow-up turns;
   - current question.
2. Define a `GroundedFollowUpOutput` model or plain markdown output with explicit limitations.
3. Require the follow-up agent to state when the follow-up goes beyond first-turn retrieved evidence.
4. Keep Streamlit UI behavior stable.

## Acceptance criteria

- Follow-up answers use typed first-turn artifacts instead of raw markdown when available.
- Tests cover in-scope and out-of-scope follow-ups.

---

# Phase 6 — Observability and eval integration

## Objective

Make typed agent runs inspectable and comparable against current evals.

## Work

1. Capture Pydantic AI usage metadata where available.
2. Add optional Logfire/OpenTelemetry instrumentation behind configuration.
3. Persist or export agent run artifacts alongside current Prompt A/B artifacts.
4. Add eval comparisons:
   - old JSON parser path vs Pydantic model path;
   - old LLM client path vs Pydantic AI agent path;
   - schema validation failure rate;
   - citation validation failure rate.

## Acceptance criteria

- Evals can compare before/after answer quality.
- Token/request usage is visible for Prompt A and Prompt B runs.
- Observability is optional and does not require a hosted service for local development.

---

# Phase 7 — Prepare for case-file workflows

## Objective

Use the Pydantic AI migration to establish the typed contracts needed for future case-file processing.

## New schemas to introduce later

- `CaseFile`
- `CaseDocument`
- `ExtractedCaseFact`
- `EvidenceReference`
- `AccountingIssueClassification`
- `MissingFactQuestion`
- `CaseAnalysisPlan`
- `CaseMemoDraft`
- `ReviewFinding`

## Design direction

Pydantic AI should own typed LLM stages. A future workflow engine can call those stages:

```text
LangGraph case workflow
  -> document classification agent
  -> fact extraction agent
  -> issue classification agent
  -> existing IFRS retrieval
  -> authority/applicability agents
  -> memo drafting agent
  -> human review gate
```

This keeps the migration compatible with the separate LangGraph case-analysis plan while avoiding premature workflow framework coupling.

---

# Suggested implementation order

1. Add schemas and validation around existing Prompt A/B responses.
2. Add Pydantic AI as an optional LLM path behind a feature flag/config switch.
3. Port Prompt A to Pydantic AI.
4. Port Prompt B to Pydantic AI.
5. Extract `AnswerGenerationService` and shrink `AnswerCommand`.
6. Add citation/authority validation gates.
7. Migrate follow-up chat.
8. Enable observability and eval reporting.

## Pydantic AI direct migration

Do not add a `legacy | pydantic_ai` runner flag. There is no need to preserve the old generation path as a supported runtime mode.

The migration should switch the LLM contract layer directly to Pydantic AI while keeping retrieval and answer eval entry points runnable. If a temporary adapter is needed inside an implementation PR, it should be private to that PR and removed before the phase is considered done.

Configuration that remains useful after the migration can stay in the policy file, for example:

```yaml
pydantic_ai:
  output_retries: 2
  observability: false
```

Top-level workflow orchestration remains reserved for the separate LangGraph case-analysis migration. Pydantic AI is the typed LLM generation layer, not the case workflow engine.

## Testing strategy

- Unit tests for every Pydantic schema with representative Prompt A/B fixtures.
- Unit tests for invalid/missing fields and retry/failure behavior.
- Service tests using fake agent runners.
- Regression tests for `AnswerCommandResult` compatibility.
- Existing retrieval non-regression suite unchanged.
- Promptfoo answer eval before/after comparison before removing the old generation path.

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Pydantic AI provider coverage differs from current clients | Migrate provider by provider, but do not expose a permanent legacy runner mode. |
| Structured output changes answer style | Keep prompts stable first; compare evals before prompt redesign. |
| Existing renderers expect generic dicts | Add typed-to-dict compatibility adapters, then migrate renderers later. |
| Framework churn | Isolate Pydantic AI behind local agent runner interfaces. |
| Retry loops increase cost | Set strict `output_retries` and usage limits; log retry counts. |
| Case-file ambitions cause scope creep | Keep this migration focused on LLM contracts, not full workflow orchestration. |

## Definition of done

The migration is complete when:

- Prompt A and Prompt B use Pydantic AI typed outputs by default;
- legacy LLM clients are either removed or retained only as explicit compatibility adapters;
- `AnswerCommand` no longer manually parses generic JSON;
- schema validation and citation validation are tested;
- CLI and Streamlit behavior remain stable;
- retrieval evals and answer evals show no material regression;
- the codebase has typed agent contracts suitable for future case-file processing.
