"""Mistral LLM client implementation."""

import json
import logging

from mistralai.client.models.chatcompletionresponse import ChatCompletionResponse

from src.llm.base import LLMClient

logger = logging.getLogger(__name__)

# Try to use the official Mistral client, fall back to HTTP
try:
    from mistralai.client import Mistral

    MISTRAL_SDK_AVAILABLE = True
except ImportError:
    MISTRAL_SDK_AVAILABLE = False

SDK_NOT_INSTALLED_MESSAGE = "mistralai package is not installed. Install it with: uv add mistralai"
AUTH_FAILED_MESSAGE = "Mistral API authentication failed. Please check your MISTRAL_API_KEY in .env file."
EMPTY_RESPONSE_MESSAGE = "Mistral returned empty response"
JSON_PARSE_FAILED_MESSAGE = "Failed to parse JSON response"
HIGH_REASONING_EFFORT = "high"
REASONING_PROMPT_MODE = "reasoning"
REASONING_MODEL_PREFIXES = ("magistral",)


class MistralClient(LLMClient):
    """Mistral API client."""

    def __init__(self, api_key: str, model: str = "mistral-small-latest") -> None:
        """Initialize the Mistral client.

        Args:
            api_key: Mistral API key
            model: Model identifier (default: mistral-small-latest)
        """
        if not MISTRAL_SDK_AVAILABLE:
            raise ImportError(SDK_NOT_INSTALLED_MESSAGE)
        self._client = Mistral(api_key=api_key)
        self._model = model

    def generate_text(self, prompt: str, system: str | None = None) -> str:
        """Generate text from a prompt using Mistral API.

        Args:
            prompt: The user prompt
            system: Optional system message

        Returns:
            Raw text response from the LLM

        Raises:
            RuntimeError: If the API key is invalid or missing
        """
        messages: list[dict[str, str]] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        logger.info(f"Calling Mistral model {self._model}")
        try:
            response = self._complete_text(messages)
        except Exception as e:
            error_str = str(e)
            if "401" in error_str or "Unauthorized" in error_str:
                raise RuntimeError(AUTH_FAILED_MESSAGE) from e
            raise

        content = self._extract_text_content(response.choices[0].message.content)
        return self._strip_code_fences(content)

    def generate_json(self, prompt: str, system: str | None = None) -> dict[str, object]:
        """Generate and parse JSON from a prompt.

        Args:
            prompt: The user prompt
            system: Optional system message

        Returns:
            Parsed JSON response from the LLM
        """
        json_prompt = f"{prompt}\n\nRespond with valid JSON only, no additional text."

        messages: list[dict[str, str]] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": json_prompt})

        logger.info(f"Calling Mistral model {self._model} for JSON")
        response = self._complete_json(messages)

        content = self._extract_text_content(response.choices[0].message.content)
        return self._parse_json_response(content)

    def _complete_text(self, messages: list[dict[str, str]]) -> ChatCompletionResponse:
        """Call Mistral text completion with optional reasoning enabled."""
        if self._uses_reasoning():
            logger.info(f"Using Mistral reasoning_effort={HIGH_REASONING_EFFORT} for model {self._model}")
            return self._client.chat.complete(
                model=self._model,
                messages=messages,
                temperature=0.0,
                reasoning_effort=HIGH_REASONING_EFFORT,
                prompt_mode=REASONING_PROMPT_MODE,
            )

        return self._client.chat.complete(
            model=self._model,
            messages=messages,
            temperature=0.0,
        )

    def _complete_json(self, messages: list[dict[str, str]]) -> ChatCompletionResponse:
        """Call Mistral JSON completion with optional reasoning enabled."""
        if self._uses_reasoning():
            logger.info(f"Using Mistral reasoning_effort={HIGH_REASONING_EFFORT} for model {self._model}")
            return self._client.chat.complete(
                model=self._model,
                messages=messages,
                temperature=0.0,
                response_format={"type": "json_object"},
                reasoning_effort=HIGH_REASONING_EFFORT,
                prompt_mode=REASONING_PROMPT_MODE,
            )

        return self._client.chat.complete(
            model=self._model,
            messages=messages,
            temperature=0.0,
            response_format={"type": "json_object"},
        )

    def _uses_reasoning(self) -> bool:
        """Return whether the current model supports Mistral reasoning."""
        return self._model.startswith(REASONING_MODEL_PREFIXES)

    def _extract_text_content(self, content: object) -> str:
        """Normalize Mistral message content to plain text."""
        if isinstance(content, str):
            return content

        if isinstance(content, list):
            text_parts: list[str] = []
            for chunk in content:
                text_attr = getattr(chunk, "text", None)
                if isinstance(text_attr, str):
                    text_parts.append(text_attr)
            if text_parts:
                return "".join(text_parts)

        raise RuntimeError(EMPTY_RESPONSE_MESSAGE)

    def _strip_code_fences(self, content: str) -> str:
        """Strip markdown code fences from a text response."""
        cleaned = content.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        elif cleaned.startswith("```"):
            cleaned = cleaned[3:]
        cleaned = cleaned.removesuffix("```")
        return cleaned.strip()

    def _parse_json_response(self, content: str) -> dict[str, object]:
        """Parse JSON from the response content, stripping markdown code fences if present."""
        cleaned = self._strip_code_fences(content)

        try:
            parsed = json.loads(cleaned)
        except json.JSONDecodeError:
            logger.exception(JSON_PARSE_FAILED_MESSAGE)
            raise

        if not isinstance(parsed, dict):
            raise TypeError(JSON_PARSE_FAILED_MESSAGE)
        return parsed
