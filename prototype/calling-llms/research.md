# Research: Calling LLMs Directly in IFRS Expert Project

## Summary

The IFRS Expert project currently uses `pi` (the agent harness) via subprocess to make LLM calls. This can be replaced with direct API calls using provider-specific Python libraries, all of which work on the Code plan (API-based, no GPU required). The recommended approach is to use **LiteLLM** as a unified abstraction layer, which supports OpenAI, Anthropic Claude, Mistral, and via custom endpoints also Minimax—allowing easy swapping between providers with a single, consistent interface.

## Findings

1. **Current Implementation Uses `pi` CLI via Subprocess**
   
   The project calls `pi` as a subprocess in `src/commands/answer.py` (lines 25-82). The command uses `--provider openai-codex --model gpt-5.4` and passes prompts via temporary files. This tightly couples the application to the pi CLI tool.

2. **All Major LLM Providers Support API-Based Access (No GPU Required)**
   
   Every major provider—OpenAI, Anthropic, Mistral, and Minimax—offers API endpoints that work without local GPUs. These are "Code plan compatible" because the heavy computation happens on the provider's infrastructure. This makes them a direct replacement for the current pi-based approach.

3. **Official Python Libraries Exist for Primary Providers**
   
   - **OpenAI**: Official `openai` library provides `OpenAI` client with `chat.completions.create()` API. Supports streaming, function calling, and vision models.
   - **Anthropic Claude**: Official `anthropic` library provides `Anthropic` client with `messages.create()` API. Supports streaming and the latest Claude 3.5/4 models.
   - **Mistral AI**: Official `mistralai` library provides `Mistral` client with chat completion API. Also offers OpenAI-compatible endpoints.
   - **Minimax**: No official Python library. Requires direct HTTP calls or OpenAI-compatible endpoint (availability varies by region).

4. **LiteLLM Provides the Best Unified Abstraction Layer**
   
   LiteLLM is a lightweight library that provides a unified interface across 100+ LLM providers. It follows OpenAI's `chat.completions` interface, so switching providers requires only changing a configuration string. Key advantages:
   - Single API for OpenAI, Anthropic, Mistral, Cohere, and others
   - Embedded retry logic, timeouts, and logging
   - Supports streaming and function calling
   - Can proxy through LiteLLM server for additional features
   - Actively maintained with 10k+ GitHub stars

5. **Alternative: LangChain for Complex Workflows**
   
   LangChain offers an `ChatOpenAI`, `ChatAnthropic`, and `ChatMistralAI` interface, plus higher-level abstractions (chains, agents, RAG). However, it adds significant dependency weight and complexity. For a project like this that just needs straightforward LLM calls, LiteLLM is the lighter choice.

6. **Architecture Recommendation: Provider Abstraction Layer**
   
   Replace the `_send_to_llm()` function in `src/commands/answer.py` with a provider-agnostic interface:

   ```python
   from litellm import completion
   
   def _send_to_llm(prompt: str, model: str = "gpt-4o") -> str:
       response = completion(
           model=model,
           messages=[{"role": "user", "content": prompt}]
       )
       return response.choices[0].message.content
   ```

   This allows swapping models via configuration without changing code. Set `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `MISTRAL_API_KEY` environment variables for authentication.

7. **Minimax Requires Custom Handling**
   
   Minimax does not have an official Python SDK. The recommended approach is to use their REST API directly with `requests`, or check if they offer an OpenAI-compatible endpoint (some regions have this). LiteLLM can wrap custom endpoints if needed.

8. **Dependencies Required**
   
   To support all four providers via LiteLLM, add to `pyproject.toml`:
   ```toml
   dependencies = [
       # ... existing
       "litellm>=1.0.0",
   ]
   ```
   
   LiteLLM will automatically use the official client libraries (`openai`, `anthropic`, `mistralai`) as needed.

## Sources

- **Kept**: OpenAI Python Library Documentation — official source for library usage and API patterns
- **Kept**: Anthropic Python SDK Documentation — official source for Claude API client
- **Kept**: Mistral AI Python Library — official client for Mistral models  
- **Kept**: LiteLLM GitHub and Documentation — best unified abstraction layer with 100+ provider support
- **Kept**: LangChain Documentation — alternative for complex workflows (kept as reference, not primary recommendation)
- **Dropped**: Various blog posts on "how to call OpenAI" — redundant with official docs

## Gaps

- **Minimax**: Could not confirm OpenAI-compatible endpoint availability. This may vary by region/account type. Suggested: Test directly with Minimax API or check LiteLLM's supported models list for Minimax.
- **Rate limiting / cost tracking**: Neither source covered practical operational concerns like budgets or rate limits. These should be addressed in implementation planning.

## Suggested Next Steps

1. Test LiteLLM with a single model (e.g., gpt-4o) to validate the abstraction works
2. Create a `src/llm/client.py` module that wraps LiteLLM and provides a `_send_to_llm(prompt, model)` function
3. Move model configuration to `config.yaml` or environment variables
4. Test multi-provider support with Claude and Mistral
5. For Minimax: verify API endpoint availability in your region, potentially use custom LiteLLM embedding