# Plan: Add Minimax as an LLM Provider

**Date:** 2026-04-07  
**Branch:** `feat/add-minimax-provider` (worktree: `.worktrees/add-minimax-provider`)  
**Status:** Draft - awaiting review

---

## Context

We need to add Minimax (海螺AI) as a new LLM provider, following the existing patterns established by:
- `src/llm/openai_client.py` - Direct SDK client
- `src/llm/anthropic_client.py` - Direct SDK client
- `src/llm/mistral_client.py` - Direct SDK client

All clients implement `LLMClient` from `src/llm/base.py` and are registered in the factory at `src/llm/client.py`.

---

## Research: Minimax API

### API Characteristics
- **Base URL:** `https://api.minimax.io/v1`
- **Authentication:** Bearer token (API key) - same as OpenAI
- **Models:** Multiple models (e.g., `abab6.5s-chat`, `abab6.5-chat`)
- **Endpoint:** OpenAI-compatible (`/v1/chat/completions`)
- **Response Format:** OpenAI-compatible

### Key Differences from OpenAI

| Aspect | OpenAI | Minimax |
|--------|--------|---------|
| Base URL | `https://api.openai.com/v1` | `https://api.minimax.io/v1` |
| Model param | Same | Same |
| Message format | Same | Same |
| Endpoint | `/v1/chat/completions` | `/v1/chat/completions` ✓ |

**Fully OpenAI-compatible!** Just set `base_url` to Minimax's endpoint and it should work.

---

## Approach: Subclass OpenAIClient

`MinimaxClient` extends `OpenAIClient` and only overrides `__init__` to set the correct base URL:

```python
class MinimaxClient(OpenAIClient):
    def __init__(self, api_key: str, model: str) -> None:
        self._model = model
        self._client = OpenAI(api_key=api_key, base_url=MINIMAX_BASE_URL)
```

All other methods (`generate_text`, `generate_json`, etc.) are inherited from `OpenAIClient` unchanged.

---

## Implementation Steps

### Step 1: Add Error Messages to `src/llm/base.py`

Add Minimax-specific error messages:

```python
AUTH_FAILED_MESSAGES = {
    "openai": "OpenAI API authentication failed. Please check your OPENAI_API_KEY in .env file.",
    "anthropic": "Anthropic API authentication failed. Please check your ANTHROPIC_API_KEY in .env file.",
    "mistral": "Mistral API authentication failed. Please check your MISTRAL_API_KEY in .env file.",
    "minimax": "Minimax API authentication failed. Please check your MINIMAX_API_KEY in .env file.",
}

EMPTY_RESPONSE_MESSAGES = {
    "openai": "OpenAI returned empty response",
    "anthropic": "Anthropic returned empty response",
    "mistral": "Mistral returned empty response",
    "minimax": "Minimax returned empty response",
}
```

### Step 2: Create `src/llm/minimax_client.py`

New file with `MinimaxClient` subclassing `OpenAIClient`:

```python
"""Minimax LLM client implementation."""

from openai import OpenAI

from src.llm.openai_client import OpenAIClient

MINIMAX_BASE_URL = "https://api.minimax.io/v1"


class MinimaxClient(OpenAIClient):
    """Minimax API client, extending OpenAIClient with Minimax-specific base URL."""

    def __init__(self, api_key: str, model: str) -> None:
        """Initialize the Minimax client.

        Args:
            api_key: Minimax API key
            model: Model identifier
        """
        self._model = model
        self._client = OpenAI(api_key=api_key, base_url=MINIMAX_BASE_URL)

Note: Logs will say "OpenAI" but that's acceptable - the actual API calls go to Minimax.
```

### Step 3: Update `src/llm/__init__.py`

Export the new client:
```python
from src.llm.minimax_client import MinimaxClient
__all__ = [..., "MinimaxClient"]
```

### Step 4: Update `src/llm/client.py` Factory

Add Minimax to the `get_client()` factory:

```python
if provider == "minimax":
    api_key = _require_env_var("MINIMAX_API_KEY", MISSING_API_KEY_MESSAGE)
    model = _require_env_var("MINIMAX_MODEL", MISSING_MODEL_MESSAGE)
    return MinimaxClient(api_key=api_key, model=model)
```

Update error messages to include "minimax".

### Step 5: Update Tests

Add Minimax to the parametrized test in `tests/unit/test_llm_client.py`:

```python
@pytest.mark.parametrize(
    ("provider", "api_key_var", "model_var"),
    [
        ("openai", "OPENAI_API_KEY", "OPENAI_MODEL"),
        ("anthropic", "ANTHROPIC_API_KEY", "ANTHROPIC_MODEL"),
        ("mistral", "MISTRAL_API_KEY", "MISTRAL_MODEL"),
        ("minimax", "MINIMAX_API_KEY", "MINIMAX_MODEL"),
    ],
)
```

### Step 6: Update `.env.example`

Add Minimax environment variables:
```
# Minimax LLM (https://www.minimax.io/)
MINIMAX_API_KEY=your_minimax_api_key
MINIMAX_MODEL=abab6.5s-chat
```

---

## File Changes Summary

| File | Action |
|------|--------|
| `src/llm/base.py` | Modify - add Minimax error messages |
| `src/llm/minimax_client.py` | Create - subclass of OpenAIClient |
| `src/llm/__init__.py` | Modify - export MinimaxClient |
| `src/llm/client.py` | Modify - add Minimax to factory |
| `tests/unit/test_llm_client.py` | Modify - add Minimax to parametrized tests |
| `.env.example` | Modify - add Minimax env vars |

---

## Dependencies

No new dependencies required.

---

## Verification Checklist

- [ ] `make format`
- [ ] `make lint`
- [ ] `pytest tests/unit/test_llm_client.py -v` passes
- [ ] Manual test with real Minimax API key

---

## Decisions Made

| Decision | Choice |
|----------|--------|
| SDK approach | Subclass OpenAIClient |
| Model specification | Require `MINIMAX_MODEL` env var |
| Streaming | Not supported |
| JSON mode | Use built-in `response_format={"type": "json_object"}` |
| Auth mechanism | Bearer token (identical to OpenAI) |

---

## Effort Estimate

| Task | Estimated Time |
|------|----------------|
| Step 1: base.py updates | 5 min |
| Step 2: minimax_client.py | 10 min (inheritance only) |
| Step 3-4: Module exports & factory | 10 min |
| Step 5: Tests | 15 min |
| Step 6: .env.example | 5 min |
| **Total** | **~45 min** |
