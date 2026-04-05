"""OpenAI LLM client implementation."""

import json
import logging
from typing import Any

from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam

from src.llm.base import LLMClient

logger = logging.getLogger(__name__)

AUTH_FAILED_MESSAGE = "OpenAI API authentication failed. Please check your OPENAI_API_KEY in .env file."
EMPTY_RESPONSE_MESSAGE = "OpenAI returned empty response"
JSON_PARSE_FAILED_MESSAGE = "Failed to parse JSON response"
REASONING_EFFORT = "xhigh"


class OpenAIClient(LLMClient):
    """OpenAI API client."""

    def __init__(self, api_key: str, model: str) -> None:
        """Initialize the OpenAI client.

        Args:
            api_key: OpenAI API key
            model: Model identifier
        """
        self._client = OpenAI(api_key=api_key)
        self._model = model

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
                raise RuntimeError(AUTH_FAILED_MESSAGE) from e
            raise

        content = response.choices[0].message.content
        if content is None:
            raise RuntimeError(EMPTY_RESPONSE_MESSAGE)
        return content

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
        return self._parse_json_response(content)

    def _create_text_completion(self, messages: list[ChatCompletionMessageParam]) -> ChatCompletion:
        """Create a text completion with model-specific settings."""
        logger.info(f"Using OpenAI reasoning_effort={REASONING_EFFORT} for model {self._model}")
        return self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            reasoning_effort=REASONING_EFFORT,
        )

    def _create_json_completion(self, messages: list[ChatCompletionMessageParam]) -> ChatCompletion:
        """Create a JSON completion with model-specific settings."""
        logger.info(f"Using OpenAI reasoning_effort={REASONING_EFFORT} for model {self._model}")
        return self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            response_format={"type": "json_object"},
            reasoning_effort=REASONING_EFFORT,
        )

    def _parse_json_response(self, content: str) -> dict[str, Any]:
        """Parse JSON from the response content."""
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            logger.exception(JSON_PARSE_FAILED_MESSAGE)
            raise
