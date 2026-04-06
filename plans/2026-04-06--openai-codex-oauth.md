# Plan: Add OpenAI Codex provider

- Date: 2026-04-06
- Branch: `feature/openai-codex-oauth`
- Worktree: `.worktrees/openai-codex-oauth`

## Goal

Add a new LLM provider, `openai-codex`, that authenticates with the OAuth token from OpenAI Codex, while preserving the existing `openai` provider for OpenAI platform API keys.

Implementation direction agreed after investigation:

- keep `src/llm/openai_client.py` for the existing `openai` platform API-key path
- add a new `src/llm/openai_codex_client.py` for the `openai-codex` path
- keep the public `LLMClient` interface unchanged

## Constraints and context

- Keep the existing `LLM_PROVIDER=openai` path intact for current users.
- Add `LLM_PROVIDER=openai-codex` as a separate provider rather than an auth-mode switch.
- Preserve the existing app-facing `LLMClient` interface:
  - `generate_text(prompt, system=None)`
  - `generate_json(prompt, system=None)`
- Follow project guidance:
  - strict typing
  - no bare exceptions
  - f-string logging
  - prefer small typed seams and dependency injection over brittle patching
- Write tests first.

## Findings from initial investigation

1. Current OpenAI integration is in:
   - `src/llm/openai_client.py`
   - `src/llm/client.py`
2. Current factory behavior requires:
   - `OPENAI_API_KEY`
   - `OPENAI_MODEL`
3. New provider target behavior should require:
   - `LLM_PROVIDER=openai-codex`
   - `OPENAI_CODEX_MODEL`
   - readable Codex auth data from `~/.codex/auth.json` or `CODEX_AUTH_FILE`
4. The reference implementation uses Codex auth from `~/.codex/auth.json` and injects custom headers, including:
   - `Authorization: Bearer <oauth token>`
   - `chatgpt-account-id`
   - `OpenAI-Beta: responses=experimental`
   - `originator: codex_cli_rs`
5. The local Codex auth file appears to use a `tokens` object with:
   - `access_token`
   - `account_id`
   - `refresh_token`
6. Main technical finding:
   - our current client uses `chat.completions.create(...)` and parses `response.choices[0].message.content`
   - the pi-mono Codex implementation sends requests to the Codex `/codex/responses` backend using a Responses-style payload and parses response events/output differently
   - conclusion: we should not force Codex OAuth through the existing chat-completions parsing path

## Implementation plan

### 1. Add configuration for a new provider

Introduce the new provider code and related environment variables:

- `LLM_PROVIDER=openai-codex`
- `OPENAI_CODEX_MODEL`
- `CODEX_AUTH_FILE` optional override for `~/.codex/auth.json`

Behavior:

- `LLM_PROVIDER=openai` keeps current requirements:
  - `OPENAI_API_KEY`
  - `OPENAI_MODEL`
- `LLM_PROVIDER=openai-codex` requires:
  - `OPENAI_CODEX_MODEL`
  - readable Codex auth data

### 2. Add a typed Codex auth module

Create a small module dedicated to Codex auth loading/parsing.

Proposed responsibilities:

- resolve auth file path
- load JSON from the auth file
- extract OAuth access token
- extract account ID
- expose a typed dataclass, e.g. `CodexAuthContext`

Error handling:

- missing auth file -> clear runtime/value error telling the user to run `codex login`
- malformed JSON -> clear parse error
- missing token/account fields -> clear validation error

### 3. Refactor LLM client construction

Update `src/llm/client.py` so it supports both:

- `LLM_PROVIDER=openai` -> existing `OpenAIClient`
- `LLM_PROVIDER=openai-codex` -> new `OpenAICodexClient`

Desired outcome:

- `get_client()` remains unchanged for callers
- provider selection is localized to the LLM factory
- the new provider has its own model env var and auth expectations

### 4. Add a dedicated Codex provider client

Create `src/llm/openai_codex_client.py` as a separate implementation of `LLMClient` for `LLM_PROVIDER=openai-codex`.

Planned approach:

- use the OpenAI Python SDK `responses.create(...)` API rather than `chat.completions.create(...)`
- configure the client with:
  - bearer token from Codex auth
  - account ID header
  - required beta/originator headers
  - Codex base URL (`https://chatgpt.com/backend-api`)
- convert our current prompt model into Responses-style fields:
  - `system` -> `instructions`
  - user prompt -> `input`
- extract generated text from the Responses object, likely via `response.output_text`
- keep the rest of the application unaware of auth/protocol differences

### 5. Parsing strategy

Codex OAuth will use a different internal parsing path from the existing OpenAI client.

Concretely:

- existing `openai_client.py` continues to parse chat completions via:
  - `response.choices[0].message.content`
- new `openai_codex_client.py` will parse Responses API output via:
  - `response.output_text` or equivalent structured Responses output handling
- `generate_json()` in the Codex client will still parse the returned text with `json.loads(...)`

### 6. Non-goal for first implementation

Do not implement streaming/SSE/WebSocket handling in this first pass.

Rationale:

- the app currently uses synchronous request/response flows
- the OpenAI Python SDK can likely handle non-streaming Codex Responses requests directly
- this keeps the first implementation smaller and lower-risk

## Test-first plan

### Unit tests to add/update first

1. `tests/unit/test_llm_client.py`
   - verify `LLM_PROVIDER=openai` still requires `OPENAI_API_KEY` and `OPENAI_MODEL`
   - verify `LLM_PROVIDER=openai-codex` requires `OPENAI_CODEX_MODEL`
   - verify `LLM_PROVIDER=openai-codex` does not require `OPENAI_API_KEY`
   - verify unknown provider values still fail clearly

2. New tests for Codex auth parsing
   - valid auth file returns token + account ID
   - missing file raises clear error
   - invalid JSON raises clear error
   - missing expected fields raises clear error

3. New or expanded OpenAI client tests
   - API-key mode builds the standard OpenAI client path
   - Codex mode builds the Codex-aware path
   - Codex headers/base URL behavior is correct

### Testing style

- prefer temp files and small fakes over broad monkey-patching
- monkeypatch environment variables only where appropriate
- assert outcomes and configuration behavior rather than incidental implementation details

## Documentation updates

Update:

- `.env.example`
- `README.md`

Document:

- `LLM_PROVIDER=openai-codex`
- `OPENAI_CODEX_MODEL`
- `CODEX_AUTH_FILE`
- `codex login` prerequisite
- how to switch between `openai` and `openai-codex`

## Validation plan

Run, at minimum:

- targeted unit tests for changed modules
- broader pytest run if impacted tests remain fast
- repo formatting/linting/type checks for touched files

Likely commands:

```bash
uv run pytest tests/unit/test_llm_client.py -v
uv run pytest tests/unit -v
uv run ruff check .
uv run ruff format --check .
uv run ty
```

## Deliverables

- typed Codex auth loader
- LLM factory support for the new `openai-codex` provider
- Codex OAuth-backed OpenAI client path
- unit tests for selection + parsing + error cases
- updated `.env.example` and README usage docs

## Resolved decisions

1. Provider shape
   - use a separate provider code: `LLM_PROVIDER=openai-codex`
   - keep `LLM_PROVIDER=openai` unchanged for the existing platform API-key path

2. Client structure
   - split into two client classes behind the factory:
     - `src/llm/openai_client.py` for `openai`
     - `src/llm/openai_codex_client.py` for `openai-codex`

3. Request/response protocol
   - keep the existing `openai` client on `chat.completions.create(...)`
   - implement `openai-codex` using the OpenAI Python SDK `responses.create(...)`
   - parse Codex output via the Responses API output path rather than chat completion choices
