# Plan — add a Streamlit chat UI for IFRS Expert

## 1. Goal

Add a lightweight Streamlit chat interface on top of the existing answer pipeline.

Target behavior:
- on first load, the page shows only the chat input
- on the **first** submitted question, the app runs `AnswerCommand`
- `AnswerCommand` returns **JSON**, not final Markdown
- the Streamlit app formats that JSON into Markdown and displays it in assistant chat bubbles
- the first-turn Prompt B JSON is saved in session state as conversation context
- on **later** turns, the app does **not** call `AnswerCommand` again; it sends the accumulated chat context directly to the LLM
- every later question and answer is appended to the conversation context and displayed in the transcript

This matches your clarified architecture:
- first turn = retrieval + Prompt A + Prompt B via `AnswerCommand`
- later turns = plain conversational LLM turns over accumulated context

---

## 2. What the codebase already gives us

### Existing assets we can reuse

- `src/commands/answer.py`
  - already performs the full first-turn retrieval + Prompt A + Prompt B pipeline
- `src/b_response_utils.py`
  - already converts Prompt B JSON into displayable Markdown
  - this should be reused by both the CLI and Streamlit UI
- `src/llm/client.py`
  - already centralizes provider selection from `.env`
- `src/llm/base.py`
  - already defines the LLM client abstraction we can reuse for later conversational turns
- `src/logging_config.py`
  - already gives a project logging path and format

### Gaps relative to the desired UI

1. **No Streamlit dependency yet**
   - `pyproject.toml` does not include `streamlit`

2. **No Streamlit entrypoint yet**
   - no `streamlit_app.py`
   - no `src/ui/...` package yet

3. **`AnswerCommand.execute()` currently returns a string**
   - for the clarified design, it should return Prompt B JSON
   - formatting should move out of `AnswerCommand`

4. **The CLI currently mixes pipeline execution and output formatting/persistence**
   - the cleaner split is:
     - `AnswerCommand` => returns structured JSON
     - CLI => converts JSON to Markdown and writes files
     - Streamlit => converts JSON to Markdown and renders it

5. **No reusable `AnswerCommandResult` artifact exists yet**
   - we need a typed dataclass produced by `AnswerCommand` that accumulates all answer artefacts:
     - prompts
     - raw responses
     - parsed JSON where applicable
     - retrieved document IDs
     - derived Markdown when needed
   - the CLI should consume this artifact to preserve current file-writing behavior
   - the Streamlit app should consume this artifact to display the grounded answer and create later-turn context

6. **No chat/session model exists yet**
   - we need a typed way to store:
     - rendered transcript
     - first-turn grounded run artifact
     - later freeform assistant turns

7. **No later-turn LLM chat service exists yet**
   - after the first answer, we need a small service that builds a conversation prompt and calls `get_client().generate_text(...)`

---

## 3. Streamlit package / plugin recommendation

### Recommended choice: use native Streamlit chat components

For this project, the best reusable solution is **built into Streamlit already**:
- `st.chat_input(...)`
- `st.chat_message("user")`
- `st.chat_message("assistant")`

These already provide the standard chat-bubble UX you asked for.

### Recommendation for v1

Do **not** add a third-party chat plugin initially.

Why:
- native components already solve the bubble/chat layout cleanly
- fewer dependencies
- better long-term compatibility with Streamlit
- easier debugging and testing

### Community packages that exist, but are not necessary here

There are community chat-oriented components such as older `streamlit-chat` style packages, but for this use case they add little value over the native API and may create maintenance overhead.

**Plan decision:**
- add only `streamlit`
- rely on native chat primitives
- avoid third-party chat UI packages for v1

---

## 4. Recommended implementation shape

Use a thin Streamlit entrypoint plus a small UI/service layer.

### Proposed files

- `streamlit_app.py`
  - standard Streamlit entrypoint
  - very thin: imports and runs the app
- `src/ui/app.py`
  - main Streamlit page logic
  - initializes session state
  - renders chat history
  - handles first-turn and later-turn branching
- `src/ui/chat_state.py`
  - typed dataclasses for messages and session helpers
- `src/ui/chat_service.py`
  - orchestrates:
    - first turn through `AnswerCommand`
    - later turns through direct LLM chat calls
    - JSON-to-Markdown conversion for first turn
- `tests/unit/test_chat_service.py`
- `tests/unit/test_streamlit_state.py`

### Existing files likely to change

- `pyproject.toml`
  - add `streamlit`
- `src/commands/answer.py`
  - return a structured `AnswerCommandResult` artifact instead of a final display string
  - accumulate all answer artefacts on that object
- `src/cli.py`
  - keep CLI behavior unchanged, but make it consume the new `AnswerCommandResult` artifact
- `README.md`
  - add Streamlit run instructions

### Likely new shared model

- `src/models/answer_command_result.py`
  - dataclasses representing one `AnswerCommand` run
  - shared by the CLI and Streamlit app

### Files that should **not** change

Per your instruction:
- `prompts/answer_prompt_A.txt`
- `prompts/answer_prompt_B.txt`

The plan assumes both prompt files remain unchanged.

---

## 5. UX design

Use native Streamlit chat components for a classic bubble interface.

### First-load screen

Behavior:
- no greeting block
- no results yet
- only the input box is visible

### First submitted question

Flow:
1. user enters a question
2. app appends the user message to session state
3. app calls `AnswerCommand`
4. `AnswerCommand` returns Prompt B JSON
5. app converts JSON to Markdown with `convert_json_to_markdown(...)`
6. app displays the formatted Markdown in an assistant bubble
7. app stores both:
   - the rendered Markdown
   - the underlying Prompt B JSON

### Later submitted questions

Flow:
1. user enters a follow-up question
2. app appends the question to session state
3. app builds a plain LLM context from prior transcript + saved first-turn Prompt B JSON
4. app calls the configured LLM client directly
5. app displays the returned text in an assistant bubble
6. app appends the new assistant text to session state

This is intentionally asymmetric:
- turn 1 is grounded by retrieval
- turns 2+ are conversational follow-ups over accumulated context

---

## 6. Conversation state model

Keep separate structures for display and context.

### A. Display transcript

Used to render the UI.

```python
@dataclass
class ChatMessage:
    role: str
    content: str
    format_type: str  # "markdown" | "text"
```

Notes:
- first-turn assistant output will usually be `markdown`
- later assistant follow-ups will usually be `text` unless we explicitly ask the LLM for Markdown too

### B. First-turn grounding artifact

Used as durable context for later turns.

Rather than inventing a UI-only artifact, reuse the `AnswerCommandResult` dataclass produced by `AnswerCommand` for the first grounded turn.

Suggested shape:

```python
@dataclass
class AnswerCommandResult:
    query: str
    retrieved_doc_uids: list[str]
    prompt_a_text: str | None
    prompt_a_raw_response: str | None
    prompt_a_json: dict | None
    prompt_b_text: str | None
    prompt_b_raw_response: str | None
    prompt_b_json: dict | None
    prompt_b_markdown: str | None
    error: str | None
```

Notes:
- this is the artifact produced by `AnswerCommand`
- it accumulates the important prompts, responses, and derived outputs from `AnswerCommand`
- the CLI can use it to preserve current file-writing behavior
- Streamlit can use it to render the grounded Markdown answer and retain grounded context for every later turn

### C. Later-turn chat memory

Used to build the ongoing conversational context.

```python
@dataclass
class FollowUpTurn:
    user_question: str
    assistant_answer: str
```

### Suggested session keys

- `st.session_state.messages`
- `st.session_state.first_turn_artifact`
- `st.session_state.follow_up_turns`
- `st.session_state.last_error`

---

## 7. How later-turn context should work

Since later turns no longer go through retrieval, the app needs a direct LLM context builder.

### Context sources

Later-turn prompt should include:
- the original first user question
- the first-turn `AnswerCommandResult` artefacts, especially Prompt B JSON / Markdown
- the sequence of later user questions and assistant answers
- the current new user question

### Recommended initial strategy

Build one conversation prompt containing:
1. a short system instruction for follow-up assistance
2. the first-turn grounded answer artifact
3. the subsequent transcript
4. the current user question

Example shape:

```text
You are continuing a discussion about IFRS accounting.
Use the grounded first answer below as the base context.
If the follow-up goes beyond that context, answer cautiously and make the limitation explicit.

Grounded first-turn artifact:
...Prompt B markdown or compact JSON summary...

Conversation so far:
User: ...
Assistant: ...
User: ...
Assistant: ...

Current question:
...
```

### Important note

Because later turns skip retrieval, they are **less grounded** than turn 1.
That is acceptable given your chosen design, but it should be treated as an explicit product tradeoff.

---

## 8. Needed refactor in `AnswerCommand`

### Current issue

`AnswerCommand.execute()` returns a final string and also owns output-file behavior conceptually.

### Planned change

Refactor `AnswerCommand` so that its core responsibility is:
- execute retrieval + Prompt A + Prompt B
- accumulate all artefacts on a `AnswerCommandResult`
- return that `AnswerCommandResult`

### Recommended `execute()` contract

Preferred shape:
- `execute()` returns a `AnswerCommandResult`
- `AnswerCommandResult` is the single artifact produced by `AnswerCommand`
- callers decide how to render or persist it

### Formatting responsibility split

- `AnswerCommand` => returns a populated `AnswerCommandResult`
- CLI => preserves existing behavior by converting run data to Markdown and writing the same files as today
- Streamlit => converts run data to Markdown and renders chat bubbles

### Why this is better

- gives `AnswerCommand` one reusable data artifact with all answer artefacts
- avoids ad hoc passing of prompts and responses between layers
- supports both CLI and UI cleanly
- keeps CLI behavior unchanged while making the same grounded run data available to Streamlit

---

## 9. CLI implications

The CLI should remain usable, but with a cleaner layering.

### CLI behavior

CLI behavior should remain unchanged.

For `src/cli.py` on `answer`:
1. call `AnswerCommand.execute()`
2. receive a `AnswerCommandResult`
3. use the run artifact to preserve the current outputs and file-writing behavior
   - same terminal behavior as today
   - same saved artifacts when `--save-all` / `--output-dir` is used
4. perform formatting and persistence from the run artifact rather than from ad hoc local variables

### Planning recommendation

Treat the CLI as the layer that formats and writes, but do so in a way that preserves the current user-visible behavior exactly.

---

## 10. Streamlit app flow

### Startup

1. load `.env`
2. initialize logging
3. initialize session state at the top of the app
4. create cached service dependencies

### Main render loop

1. render prior messages from `st.session_state.messages`
2. wait for `st.chat_input(...)`
3. if no first-turn artifact exists:
   - handle as a first-turn grounded question
4. else:
   - handle as a later conversational follow-up

### Assistant rendering

- first-turn assistant message:
  - render via `st.markdown(prompt_b_markdown)`
- later-turn assistant message:
  - render via `st.markdown(...)` if we ask the LLM for Markdown
  - otherwise render via `st.write(...)`

---

## 11. Resource and performance plan

Per the Streamlit guidance, cache expensive resources.

### Use `@st.cache_resource` for

- the answer service factory
- the LLM client factory wrapper used by the UI
- any long-lived retrieval dependencies needed for first-turn execution

### Do not cache in session state

- raw Streamlit widgets
- transient spinners / loading state
- mutable service instances unless they are safe to reuse

### Performance note

Only the first turn uses retrieval, so the expensive FAISS path is hit once per conversation rather than every turn.
That simplifies the Streamlit performance profile significantly.

---

## 12. Error and edge-case handling

The Streamlit app should explicitly handle:

1. **missing index on first turn**
   - show a clear message that ingestion must run first

2. **missing LLM credentials**
   - surface the provider configuration error from the existing client layer

3. **invalid Prompt B JSON**
   - show an error bubble
   - log the raw response

4. **later-turn LLM failure**
   - keep the transcript intact
   - show a visible assistant-side error message

5. **empty input**
   - ignore it

6. **very long follow-up conversations**
   - start with full history
   - later add truncation if needed

---

## 13. Testing plan

Follow the project testing policy: dependency injection + fakes, not broad monkey-patching.

### Unit tests

#### `tests/unit/test_chat_service.py`

Cover:
- first turn calls `AnswerCommand`
- first turn converts returned JSON into Markdown
- later turns do **not** call `AnswerCommand`
- later turns call the direct LLM chat path
- later-turn prompt contains the saved first-turn Prompt B artifact
- errors from first-turn and later-turn paths are surfaced cleanly

#### `tests/unit/test_answer_command.py`

Refactor tests to cover:
- `execute()` returns a `AnswerCommandResult`
- prompts and responses are accumulated on the run artifact
- Prompt B JSON is parsed and exposed cleanly
- command no longer owns Markdown conversion concerns

#### `tests/unit/test_cli.py`

Extend tests to cover:
- CLI behavior remains unchanged for users
- CLI writes the same artifacts as before, now sourced from the run artifact

#### `tests/unit/test_streamlit_state.py`

Cover:
- session-state initialization helpers
- first-turn artifact persistence
- transcript append behavior
- follow-up context assembly

### Integration test

Add one integration-style test around the chat service:
- fake `AnswerCommand` result for turn 1
- fake LLM client for turn 2
- assert that turn 2 sees the first-turn Prompt B artifact in its constructed context

### UI testing

For v1, a smoke path is enough:
- app loads
- first question renders user + assistant bubbles
- second question appends a new pair of bubbles

---

## 14. Concrete implementation slices

### Slice 1 — add the shared run artifact and reshape `AnswerCommand`

Goal:
- make `AnswerCommand` a data-returning first-turn pipeline with a reusable `AnswerCommandResult` model

Tasks:
- add a shared `AnswerCommandResult` dataclass
- accumulate prompts and responses on the run artifact as the pipeline executes
- return Prompt B JSON / raw response / retrieved docs via the run artifact
- include derived Markdown on the run artifact if that makes reuse simpler
- keep CLI behavior unchanged by making its output-writing logic consume the run artifact

Exit criteria:
- first-turn pipeline still works
- command returns a `AnswerCommandResult`
- CLI behavior is unchanged

### Slice 2 — add Streamlit skeleton

Goal:
- add a minimal runnable chat app

Tasks:
- add `streamlit` dependency
- add `streamlit_app.py`
- add `src/ui/app.py`
- initialize session state
- render native chat bubbles

Exit criteria:
- app opens with only the input box visible
- message bubbles render correctly

### Slice 3 — wire first turn

Goal:
- make the first question run through the grounded pipeline

Tasks:
- add `src/ui/chat_service.py`
- wire first submit to `AnswerCommand`
- use `AnswerCommandResult` to render the grounded answer in the UI layer
- store the first-turn run artifact in session state

Exit criteria:
- first question returns grounded formatted output in the chat

### Slice 4 — wire later conversational turns

Goal:
- make follow-up questions go directly to the LLM

Tasks:
- add direct LLM follow-up method in `chat_service`
- build prompt context from first-turn artifact + later transcript
- append later answers to session state

Exit criteria:
- second and later questions no longer call `AnswerCommand`
- context accumulates correctly

### Slice 5 — polish and docs

Goal:
- make the UI suitable for local demo use

Tasks:
- add a clear-chat button
- add friendly errors
- optionally show first-turn consulted docs in an expander
- add README instructions

Exit criteria:
- app is easy to run locally
- transcript can be reset cleanly

---

## 15. File-by-file change summary

### New
- `streamlit_app.py`
- `src/ui/app.py`
- `src/ui/chat_state.py`
- `src/ui/chat_service.py`
- `src/models/answer_command_result.py`
- `tests/unit/test_chat_service.py`
- `tests/unit/test_streamlit_state.py`

### Modified
- `pyproject.toml`
- `README.md`
- `src/commands/answer.py`
- `src/cli.py`
- `tests/unit/test_cli.py`
- `tests/unit/test_answer_command.py`

### Explicitly unchanged
- `prompts/answer_prompt_A.txt`
- `prompts/answer_prompt_B.txt`

---

## 16. Main risks / decisions

### Risk 1 — later turns are less grounded

Because follow-up turns skip retrieval, the assistant may overextend beyond the original evidence base.

Mitigation:
- instruct the later-turn prompt to stay anchored to the first-turn grounded answer
- tell the assistant to state limitations clearly when a follow-up goes beyond the original scope

### Risk 2 — first-turn artifact may be too verbose for later prompts

Full Prompt B JSON may be larger than needed.

Mitigation:
- start by storing both JSON and Markdown
- if needed, later compress the artifact into a smaller summary view for follow-up prompts

### Risk 3 — run-artifact refactor could break CLI assumptions

Mitigation:
- keep the command core stable
- move formatting outward carefully
- preserve current CLI outputs exactly
- extend tests before rewiring CLI behavior

### Risk 4 — Streamlit reruns may recreate services too often

Mitigation:
- use `@st.cache_resource`
- keep the app layer thin

---

## 17. Recommended order of work

1. add the shared `AnswerCommandResult` dataclass and refactor `AnswerCommand` to populate it
2. update the CLI internals to consume the run artifact while preserving current behavior exactly
3. add `streamlit_app.py` and `src/ui/app.py`
4. add `chat_service` for first-turn vs later-turn branching
5. wire later turns directly to the LLM with accumulated context
6. add tests for the run artifact and the two-path behavior
7. document how to run the app

---

## 18. Final recommendation

The cleanest v1 is:
- **UI:** native Streamlit chat via `st.chat_input` + `st.chat_message`
- **shared `AnswerCommand` artifact:** introduce a `AnswerCommandResult` dataclass that accumulates all answer artefacts
- **first turn:** call `AnswerCommand`, receive a `AnswerCommandResult`, and use it to display the grounded answer
- **later turns:** skip retrieval and go straight to the LLM with accumulated context
- **CLI:** keep behavior unchanged, but drive output writing from the same run artifact
- **formatting:** centralize JSON-to-Markdown conversion outside `AnswerCommand`, using the existing `convert_json_to_markdown(...)` utility
- **dependencies:** add `streamlit`, but no extra chat plugin/package for v1

This keeps the architecture simple, gives `AnswerCommand` a reusable artifact model, preserves CLI behavior, and avoids unnecessary prompt-file changes.