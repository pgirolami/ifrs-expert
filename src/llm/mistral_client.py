"""Mistral LLM client implementation."""

import json
import logging
from typing import Any

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
            response = self._client.chat.complete(
                model=self._model,
                messages=messages,
                temperature=0.0,
            )
        except Exception as e:
            error_str = str(e)
            if "401" in error_str or "Unauthorized" in error_str:
                raise RuntimeError(AUTH_FAILED_MESSAGE) from e
            raise

        content = response.choices[0].message.content
        if content is None:
            raise RuntimeError(EMPTY_RESPONSE_MESSAGE)

        # Strip markdown code fences if present
        cleaned = content.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        elif cleaned.startswith("```"):
            cleaned = cleaned[3:]
        cleaned = cleaned.removesuffix("```")
        return cleaned.strip()

    def generate_json(self, prompt: str, system: str | None = None) -> dict[str, Any]:
        """Generate and parse JSON from a prompt.

        Args:
            prompt: The user prompt
            system: Optional system message

        Returns:
            Parsed JSON response from the LLM
        """
        # Add JSON instruction to prompt for more reliable JSON output
        json_prompt = f"{prompt}\n\nRespond with valid JSON only, no additional text."

        messages: list[dict[str, str]] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": json_prompt})

        logger.info(f"Calling Mistral model {self._model} for JSON")
        response = self._client.chat.complete(
            model=self._model,
            messages=messages,
            temperature=0.0,
            response_format={"type": "json_object"},
        )

        content = response.choices[0].message.content
        if content is None:
            raise RuntimeError(EMPTY_RESPONSE_MESSAGE)
        return self._parse_json_response(content)

    def _parse_json_response(self, content: str) -> dict[str, Any]:
        """Parse JSON from the response content, stripping markdown code fences if present."""
        cleaned = content.strip()
        if cleaned.startswith("```json"):
            cleaned = cleaned[7:]
        elif cleaned.startswith("```"):
            cleaned = cleaned[3:]
        cleaned = cleaned.removesuffix("```")
        cleaned = cleaned.strip()

        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            logger.exception(JSON_PARSE_FAILED_MESSAGE)
            raise
