"""OpenAI LLM client implementation."""

import json
import logging
from typing import Any

from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam

from src.llm.base import LLMClient

logger = logging.getLogger(__name__)

EMPTY_RESPONSE_MESSAGE = "OpenAI returned empty response"
JSON_PARSE_FAILED_MESSAGE = "Failed to parse JSON response"
DEFAULT_REASONING_EFFORT = "low"

ReasoningLevel = str | None


class OpenAIClient(LLMClient):
    """OpenAI API client."""

    def __init__(
        self,
        api_key: str,
        model: str,
        reasoning_effort: ReasoningLevel = DEFAULT_REASONING_EFFORT,
        base_url: str | None = None,
    ) -> None:
        """Initialize the OpenAI client.

        Args:
            api_key: OpenAI API key
            model: Model identifier
            reasoning_effort: Optional reasoning effort ("low", "medium", "high"). Defaults to "low".
            base_url: Optional base URL for the API. If None, uses OpenAI's default.
        """
        self._client = OpenAI(api_key=api_key, base_url=base_url)
        self._model = model
        self._reasoning_effort = reasoning_effort

    def generate_text(self, prompt: str, system: str | None = None) -> str:
        """Generate text from a prompt using OpenAI API.

        Args:
            prompt: The user prompt
            system: Optional system message

        Returns:
            Raw text response from the LLM
        """
        messages: list[ChatCompletionMessageParam] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        logger.info(f"Calling OpenAI model {self._model}")
        try:
            response = self._create_text_completion(messages)
        except Exception as e:
            error_str = str(e)
            if "401" in error_str or "api_key" in error_str.lower() or "Unauthorized" in error_str:
                auth_failed_message = f"{type(self).__name__} API authentication failed. Please check your API key configuration."
                raise RuntimeError(auth_failed_message) from e
            raise

        content = response.choices[0].message.content
        if content is None:
            raise RuntimeError(EMPTY_RESPONSE_MESSAGE)
        return self._clean_response(content)

    def generate_json(self, prompt: str, system: str | None = None) -> dict[str, Any]:
        """Generate and parse JSON from a prompt.

        Args:
            prompt: The user prompt
            system: Optional system message

        Returns:
            Parsed JSON response from the LLM
        """
        messages: list[ChatCompletionMessageParam] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        logger.info(f"Calling OpenAI model {self._model} with JSON mode")
        response = self._create_json_completion(messages)

        content = response.choices[0].message.content
        if content is None:
            raise RuntimeError(EMPTY_RESPONSE_MESSAGE)
        clean_response = self._clean_response(content)
        return self._parse_json_response(clean_response)

    def _create_text_completion(self, messages: list[ChatCompletionMessageParam]) -> ChatCompletion:
        """Create a text completion with model-specific settings."""
        logger.info(f"Using OpenAI reasoning_effort={self._reasoning_effort} for model {self._model}")
        kwargs: dict[str, object] = {
            "model": self._model,
            "messages": messages,
        }
        if self._reasoning_effort is not None:
            kwargs["reasoning_effort"] = self._reasoning_effort
        return self._client.chat.completions.create(**kwargs)  # type: ignore[arg-type]

    def _create_json_completion(self, messages: list[ChatCompletionMessageParam]) -> ChatCompletion:
        """Create a JSON completion with model-specific settings."""
        logger.info(f"Using OpenAI reasoning_effort={self._reasoning_effort} for model {self._model}")
        kwargs: dict[str, object] = {
            "model": self._model,
            "messages": messages,
            "response_format": {"type": "json_object"},
        }
        if self._reasoning_effort is not None:
            kwargs["reasoning_effort"] = self._reasoning_effort
        return self._client.chat.completions.create(**kwargs)  # type: ignore[arg-type]

    def _parse_json_response(self, content: str) -> dict[str, Any]:
        """Parse JSON from the response content."""
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            logger.exception(JSON_PARSE_FAILED_MESSAGE)
            raise

    def _clean_response(self, content: str) -> str:
        """Clean the response content. Override in subclasses if needed."""
        return content
