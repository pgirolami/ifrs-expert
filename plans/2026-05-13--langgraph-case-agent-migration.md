# Plan — LangGraph case-analysis migration

## Goal

Move IFRS Expert from a mostly linear custom RAG answer command toward a case-file analysis engine with three incremental steps:

1. Refactor the current workflow into smaller typed stages that map cleanly to tools and LangGraph nodes.
2. Replace the current hand-rolled workflow orchestration with LangGraph while preserving retrieval behavior.
3. Evolve selected stages into a bounded agent that calls tools instead of receiving all context upfront.

Non-goals for this plan:

- Do not change the SQLite schema for the existing corpus store.
- Do not replace FAISS or the existing vector-store files.
- Do not replace the current retrieval policy catalog or retrieval evals during the first migration.
- Do not adopt generic LangChain RAG abstractions as a replacement for the domain-specific retrieval pipeline.

## Design principle

Use LangGraph as the **workflow/control layer**, not as the domain intelligence layer.

The domain-specific assets remain first-class:

- `src/retrieval/pipeline.py` retrieval behavior;
- `config/policy.default.yaml` retrieval policies;
- prompt A / prompt B reasoning contracts;
- SQLite stores for chunks, sections, references, documents;
- FAISS stores for chunk/title/document vectors;
- promptfoo and retrieval non-regression evals.

The migration should make process rules executable rather than prompt-only:

- source retrieval is mandatory before IFRS analysis;
- retrieved source material must be classified for authority and pass sufficiency checks before it can support an answer;
- missing facts trigger clarification instead of unsupported final answers;
- citation verification runs before rendering;
- agent tool-calling is allowed only inside bounded graph stages.

---

# Step 1 — Refactor current code into node/tool-shaped stages

## Objective

Break the current `AnswerCommand` and retrieval orchestration into composable, typed services without changing runtime behavior.

This is the safety step. It should be possible to complete it before adding LangGraph.

## Current hotspots

- `src/commands/answer.py`
  - mixes validation, retrieval orchestration, prompt construction, LLM calls, JSON parsing, markdown rendering, and artifact assembly.
- `src/retrieval/pipeline.py`
  - contains several retrieval strategies plus expansion logic in one large module.
- Prompt responses are parsed as generic JSON values instead of validated domain models.
- Follow-up handling in `src/ui/chat_service.py` is context-stuffing oriented and not yet case-state oriented.

## Target architecture after Step 1

Introduce an application/service layer, for example:

```text
src/case_analysis/
  __init__.py
  state.py
  models.py
  services.py
  workflow.py          # still custom in Step 1
  nodes/
    validate_question.py
    retrieve_authority.py
    classify_authority.py
    evaluate_applicability.py
    render_answer.py
    verify_citations.py
  tools/
    authority_retrieval.py
    llm_generation.py
```

The exact paths can change, but the boundaries should be stable.

## Proposed stage contracts

### 1. `ValidateQuestionStage`

Input:

- user question;
- selected retrieval policy.

Output:

- valid question text, trimmed of leading/trailing whitespace; or
- validation failure with the exact reason, for example `empty_question` or `invalid_policy`.

Purpose:

- move query/policy validation out of `AnswerCommand`.

### 2. `RetrieveSourceMaterialStage`

Input:

- validated question text;
- resolved retrieval policy;
- the existing retrieval services needed to run retrieval: chunk store, section store, reference store, vector stores, DB initialization function, and index path functions.

Output:

- `RetrievedSourcePackage` containing:
  - document hits;
  - chunk hits;
  - expanded source chunks;
  - retrieval policy name;
  - provenance.

This stage retrieves potentially relevant IFRS/source material. It does **not** decide yet which material is authoritative. That decision happens in `ClassifyAuthorityStage`.

Implementation:

- call existing `execute_retrieval()` initially;
- do not change retrieval ranking or expansion behavior in this step.

### 3. `ClassifyAuthorityStage` / current Prompt A

Input:

- question;
- formatted retrieved-source context;
- chunk summary.

Output:

- typed authority classification result model, for example:
  - primary accounting issue;
  - source classifications: primary authority, supporting authority, peripheral material, excluded material;
  - treatment families;
  - candidate approaches;
  - clarification payload.

Implementation:

- keep existing prompt text initially;
- validate the response with Pydantic models;
- if the model returns invalid JSON or misses required fields, return a structured workflow failure instead of continuing with a broken answer.

### 4. `BuildApplicabilityContextStage`

Input:

- retrieved source package;
- authority classification result.

Output:

- pruned context for Prompt B;
- list of source doc UIDs included in the applicability context;
- citation metadata.

Purpose:

- extract `_build_prompt_b_context()` behavior from `AnswerCommand`.

### 5. `EvaluateApplicabilityStage` / current Prompt B

Input:

- authority classification result;
- pruned applicability context.

Output:

- typed final analysis object;
- raw response artifact.

### 6. `RenderAnswerStage`

Input:

- final analysis object;
- citation metadata;
- question;
- retrieved document list.

Output:

- memo markdown;
- FAQ markdown;
- JSON artifact.

Implementation:

- preserve behavior of `src/b_response_utils.py`.

### 7. `VerifyCitationsStage`

Input:

- final analysis object;
- retrieved chunks/context.

Output:

- pass/warn/fail;
- missing citation references;
- unsupported citation references.

Initial implementation can be deterministic:

- cited chunk/document IDs must exist in context;
- cited quoted text must exactly match, or be a verbatim substring of, the retrieved source chunk;
- citations must not be attached to claims that the cited source text does not actually support;
- no citation to excluded/superseded material in the final conclusion unless explicitly labelled.

## Implementation sequence

1. Add typed Pydantic result models under `src/case_analysis/models.py`.
2. Extract prompt template reading/building into a dedicated prompt service.
3. Extract retrieved source package construction from `AnswerCommand`.
4. Extract Prompt A call/parse into `ClassifyAuthorityStage`.
5. Extract Prompt B call/parse into `EvaluateApplicabilityStage`.
6. Extract markdown rendering into `RenderAnswerStage`.
7. Rebuild `AnswerCommand.execute()` as a thin compatibility wrapper that calls the new custom workflow.
8. Keep CLI and Streamlit entry points unchanged from the user perspective.

## Unit tests for Step 1

Add focused unit tests for each stage:

- validation stage rejects empty question and malformed policy;
- retrieval stage calls fake retriever and returns stable retrieved source package;
- Prompt A stage parses valid JSON into typed authority classification result;
- Prompt A stage returns structured failure for invalid JSON;
- Prompt B context builder includes only material classified as primary/supporting authority;
- Prompt B stage parses valid final analysis;
- render stage preserves existing memo/FAQ output behavior;
- citation verifier catches missing chunk/document citations.

Use dependency injection and small fakes. Avoid broad monkey-patching.

## Regression tests for Step 1

Keep existing tests passing, especially:

- `tests/unit/test_answer_command.py`;
- `tests/unit/test_chat_service.py`;
- `tests/retrieval/test_retrieval.py`;
- retrieval policy tests;
- promptfoo config/script tests.

Add a compatibility test:

- same fake retrieval + same fake LLM responses through old `AnswerCommand` wrapper produce the same `AnswerCommandResult` fields as before.

## Evals for Step 1

Do not change eval targets yet.

Run:

- retrieval non-regression suite;
- existing promptfoo answer evals;
- at least one known Q1/Q2 artifact comparison.

Expected result:

- no meaningful output drift except incidental formatting if explicitly accepted.

Acceptance criteria:

- `AnswerCommand` is mostly orchestration wrapper code;
- new stages are independently testable;
- all existing unit/integration tests pass;
- retrieval and answer eval baselines remain stable.

---

# Step 2 — Replace custom workflow implementation with LangGraph

## Objective

Use LangGraph to encode the deterministic answer/case workflow while preserving the stage implementations from Step 1.

LangGraph should replace custom orchestration, not replace the domain-specific retrieval or prompt logic.

## Dependency decision

Add LangGraph as a direct dependency only when Step 1 is stable.

Likely dependency:

```toml
langgraph = "..."
```

Avoid pulling in broad LangChain abstractions unless needed for specific LangGraph primitives.

## Target architecture after Step 2

```text
src/case_analysis/
  graph.py
  state.py
  checkpoints.py
  nodes/
  tools/
```

`state.py` should define the workflow state, for example:

```python
class CaseAnalysisState(TypedDict):
    case_id: str | None
    question: str
    policy_name: str
    retrieved_source_package: RetrievedSourcePackage | None
    authority_classification_result: AuthorityClassification | None
    applicability_context: ApplicabilityContext | None
    applicability_analysis_result: ApplicabilityAnalysis | None
    citation_verification_result: CitationVerificationResult | None
    memo_markdown: str | None
    faq_markdown: str | None
    errors: list[WorkflowError]
    next_action: str | None
```

Use concrete project types where possible. Avoid untyped catch-all state.

## Graph shape for the current answer workflow

Initial deterministic graph:

```text
start
  → validate_question
  → retrieve_source_material
  → classify_authority
  → route_after_classification
      ├── needs_clarification → clarification_response
      ├── insufficient_authority → cautious_no_answer
      └── sufficient → build_applicability_context
  → evaluate_applicability
  → verify_citations
  → route_after_citation_check
      ├── pass/warn → render_answer
      └── fail → repair_or_cautious_no_answer
  → end
```

This graph should support the existing one-shot answer first. Case-file persistence can come after the one-shot path works.

## Human-in-the-loop preparation

Even if not fully implemented in Step 2, design the graph so clarification can become an interrupt/resume point later.

Clarification output should be structured:

- questions to ask;
- missing facts;
- why the facts matter;
- authority or issue area affected.

## Checkpointing strategy

Initial mode:

- in-memory checkpoints for tests and development.

Later case-file mode:

- checkpoint by `case_id`.
- Use a dedicated workflow-state persistence table only when case-file work begins. This plan does not require changing the current corpus tables.

## Implementation sequence

1. Add LangGraph dependency.
2. Define `CaseAnalysisState`.
3. Wrap each Step 1 stage as a graph node.
4. Implement conditional edge functions:
   - after validation;
   - after authority classification;
   - after citation verification.
5. Create `CaseAnalysisGraphRunner` with a simple `.run(question, policy)` API.
6. Update `AnswerCommand` to call the graph runner instead of the custom Step 1 workflow.
7. Keep output model `AnswerCommandResult` stable for CLI/UI compatibility.
8. Add graph execution logging with node names and case/run IDs.

## Unit tests for Step 2

Add graph-level tests with fake nodes or fake services:

- happy path visits nodes in expected order;
- validation failure stops before retrieval;
- authority classification clarification route does not call applicability evaluation;
- insufficient authority route returns cautious result;
- citation failure route does not render a normal final answer;
- graph runner converts final state to `AnswerCommandResult` correctly.

Node-level tests from Step 1 remain unchanged.

## Integration tests for Step 2

- CLI `answer` still returns expected success/failure fields with fake LLM where possible.
- Streamlit `ChatService` still uses first-turn grounded answer successfully.
- Existing retrieval integration tests remain unchanged.

## Evals for Step 2

Keep evals comparing behavior before/after LangGraph.

Recommended eval gates:

1. **Retrieval parity**
   - same policy and question produce same retrieved doc/chunk IDs as before.
2. **Prompt artifact parity**
   - Prompt A text and Prompt B text should be identical or explainably changed.
3. **Answer quality parity**
   - promptfoo score does not regress beyond agreed tolerance.
4. **Failure path evals**
   - add synthetic cases for invalid Prompt A JSON, missing authority, missing facts, bad citation.

Acceptance criteria:

- old custom workflow can be removed or kept only as temporary fallback;
- LangGraph owns all answer workflow branching;
- user-facing CLI/UI behavior remains stable;
- node-level traces make failures easier to diagnose;
- eval baselines remain stable.

---

# Step 3 — Move toward bounded agent tooling instead of context stuffing

## Objective

Introduce agentic tool use inside controlled graph stages so the system can analyze case files without stuffing every source into one prompt.

The graph remains deterministic at the macro level. The agent is bounded to specific stages and tool sets.

## Core design

Do not build a free-form autonomous IFRS agent.

Use this pattern:

```text
deterministic graph stage
  → bounded agent with allowed tools and budget
  → structured result
  → deterministic validation gate
```

The graph decides required stages. The agent chooses tool calls inside a stage.

## Candidate tools

Wrap existing capabilities as typed tools:

### Source-retrieval tools

These tools retrieve potentially relevant material. They should not be called “authority” tools because the later authority-classification stage may decide that some retrieved material is only background, peripheral, superseded, or irrelevant.

- `retrieve_ifrs_sources(query, policy_name, issue_type)`
- `retrieve_sources_by_document(doc_uid, query)`
- `expand_source_to_section(doc_uid, section_id)`
- `get_referenced_sources(doc_uid, chunk_id)`

These call existing stores/retrieval functions.

### Case-file tools

These likely require new case-file storage later, but can start as in-memory/test tools:

- `list_case_files(case_id)`
- `extract_case_facts(file_id)`
- `retrieve_case_evidence(case_id, query)`
- `quote_case_evidence(file_id, page_or_anchor)`

### Analysis tools

- `classify_issue_type(question, facts)`
- `map_facts_to_ifrs_criteria(issue_type, facts, classified_authority)`
- `detect_missing_facts(issue_type, criteria_map)`
- `verify_citations(answer_json, source_context, case_context)`

### Output tools

- `draft_memo(analysis_json)`
- `export_workpaper(case_id, memo, citations)`

## First bounded-agent stage to implement

Start with a narrow stage, not the whole workflow.

Recommended first target:

**Case evidence gathering agent**

Input:

- issue type;
- known facts;
- case files available;
- required criteria from authority analysis.

Allowed tools:

- list case files;
- extract facts;
- retrieve case evidence;
- quote evidence.

Output:

- structured evidence map:
  - criterion;
  - supporting fact;
  - evidence quote/anchor;
  - confidence;
  - missing facts.

Why this first:

- source retrieval and authority classification remain graph-controlled and protected;
- the agent adds value by deciding which case-file evidence to inspect;
- output can be validated against evidence anchors.

## Later bounded-agent stage

Second target:

**Source exploration agent**

Input:

- issue type;
- initial retrieved source package;
- missing/ambiguous source checklist from the authority-classification or sufficiency gate.

Allowed tools:

- retrieve IFRS sources;
- follow references;
- expand sections.

Graph constraints:

- must call source retrieval at least once;
- cannot answer directly;
- must return a retrieved source package;
- returned sources must still pass later authority classification, sufficiency, and citation validation.

## Avoiding context stuffing

Move from this:

```text
Prompt contains all retrieved chunks + all case facts + all prior turns.
```

to this:

```text
Agent sees task + compact state summary.
Agent calls tools to fetch exact source/evidence excerpts when needed.
Final prompt receives only validated excerpts and structured maps.
```

This reduces prompt size and makes source use auditable.

## Implementation sequence

1. Define typed tool interfaces independent of LangGraph.
2. Implement tool wrappers around existing retrieval and store services.
3. Add tool-call logging and artifacts:
   - tool name;
   - input parameters;
   - output summary;
   - source IDs returned;
   - latency/error.
4. Add a bounded agent node for case evidence gathering with fake tools first.
5. Add deterministic validation of the agent's structured output.
6. Add graph budgets:
   - max tool calls;
   - max retries;
   - allowed tools per node;
   - timeout per tool.
7. Replace selected context-stuffing prompts with tool-backed prompts.
8. Extend UI/CLI only after the graph path and tests are stable.

## Unit tests for Step 3

Tool tests:

- each tool validates inputs;
- tools return typed outputs;
- retrieval tools preserve existing retrieval behavior;
- case-evidence tools return stable anchors.

Agent-node tests with fake LLM/tool caller:

- agent calls only allowed tools;
- max tool-call budget is enforced;
- invalid tool arguments produce structured failure;
- malformed agent output is rejected or repaired;
- missing evidence triggers clarification rather than fabricated facts.

Validation tests:

- evidence map cannot cite unknown file/chunk anchors;
- classified source map cannot cite chunks not returned by retrieval;
- final memo cannot include unsupported citations.

## Evals for Step 3

Add evals in layers.

### Retrieval evals remain unchanged

Existing retrieval non-regression continues to protect source retrieval behavior.

### Tool-use evals

Add cases that assert:

- required tools were called;
- prohibited tools were not called;
- tool-call count stays within budget;
- returned citations are from tool outputs.

### Case-file analysis evals

Create small fixture cases with known expected outputs:

- uploaded evidence snippets;
- issue type;
- required facts;
- expected missing facts;
- expected authority paragraphs;
- expected memo conclusion shape.

Evaluate:

- fact extraction accuracy;
- evidence-to-criterion mapping;
- missing-fact detection;
- citation validity;
- final memo usefulness.

### Promptfoo integration

Keep current answer evals.

Add new promptfoo suites for:

- graph state outputs;
- structured evidence maps;
- final case memo;
- citation verifier outcomes.

Acceptance criteria:

- at least one bounded agent node is in production path behind a feature flag;
- agent tool calls are logged and auditable;
- graph-level gates prevent unsupported final answers;
- evals cover both answer quality and process compliance.

---

# Cross-cutting architecture requirements

## Compatibility

Keep `AnswerCommandResult` stable until CLI/UI callers are migrated.

New graph outputs can be richer internally, but existing public fields should remain available:

- query;
- retrieved document UIDs;
- document hits;
- chunk hits;
- prompt A/B raw responses;
- prompt A/B parsed JSON;
- memo markdown;
- FAQ markdown;
- error stage.

## Observability

Every workflow run should log:

- run ID / case ID;
- selected policy;
- node start/end;
- retrieved document count and chunk count;
- Prompt A/B model/provider;
- tool calls;
- validation failures;
- final route taken.

Prefer structured artifacts for eval/debugging over only log text.

## Type safety

Use Pydantic models for all node inputs/outputs that cross workflow boundaries. Plain dataclasses are acceptable only for small internal helper objects that never cross node/tool boundaries.

Avoid passing raw dicts between stages except at external boundaries.

## Error handling

Each node should return structured failure data rather than throwing generic exceptions through the graph.

Exceptions are still appropriate for programmer errors and unrecoverable infrastructure failures, but expected model/retrieval failures should become workflow state.

## Feature flags

Introduce flags/config for staged rollout:

- `workflow_engine=custom|langgraph` during Step 2;
- `case_agent_enabled=false|true` during Step 3;
- per-node agent enablement if needed.

## Documentation

Update docs as each step lands:

- architecture diagram in `docs/ARCHITECTURE.md`;
- explain deterministic graph vs bounded agent design;
- document eval gates and artifact locations;
- document how to add a new node/tool.

---

# Suggested milestone breakdown

## Milestone A — Stage extraction

- New stage classes/services.
- `AnswerCommand` delegates to custom stage workflow.
- No behavior change.
- Unit tests added.
- Existing evals pass.

## Milestone B — Typed Prompt A/B contracts

- Pydantic models for Prompt A and Prompt B outputs.
- Structured parse/validation failures.
- Markdown rendering uses typed objects or validated JSON.
- Eval artifacts capture validation status.

## Milestone C — LangGraph deterministic workflow

- LangGraph state and nodes added.
- Graph runner behind feature flag.
- `AnswerCommand` can use graph runner.
- Graph route tests added.
- Parity evals pass.

## Milestone D — Citation and sufficiency gates

- Citation verifier node active.
- Authority sufficiency routing active.
- Failure-path evals added.

## Milestone E — First bounded agent node

- Tool interfaces added.
- Case evidence gathering agent implemented with fake/test case-file tools first.
- Tool-use logging and tests added.
- Feature flag controls production path.

## Milestone F — Case-file workflow expansion

- Add persistent case state/checkpoints.
- Add upload/evidence ingestion flow.
- Add clarification interrupt/resume flow.
- Add case memo/workpaper export path.

---

# Main risks and mitigations

## Risk: Framework migration causes output drift

Mitigation:

- Step 1 preserves behavior before LangGraph.
- Step 2 requires prompt artifact parity and retrieval parity.

## Risk: Agent skips mandatory accounting controls

Mitigation:

- Graph owns mandatory stages.
- Agent is bounded by allowed tools, budgets, and validation gates.

## Risk: Tests become too coupled to graph internals

Mitigation:

- Test nodes independently.
- Use a smaller set of graph route tests.
- Keep evals focused on behavior and artifacts.

## Risk: Evals only check final prose, not process

Mitigation:

- Add process-compliance evals:
  - tool calls;
  - authority sufficiency;
  - citation validity;
  - missing-fact detection.

## Risk: LangGraph state becomes an untyped dumping ground

Mitigation:

- Define explicit state fields.
- Keep rich domain objects in models.
- Review every new state field for ownership and lifecycle.

---

# Recommended next action

Start with **Milestone A** only.

Do not install LangGraph yet. First extract the current answer path into typed stage classes and prove with tests/evals that behavior is unchanged. Once those seams exist, LangGraph adoption becomes a low-risk orchestration swap instead of a framework rewrite.
