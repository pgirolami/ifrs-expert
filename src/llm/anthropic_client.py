"""Anthropic LLM client implementation."""

import json
import logging
from typing import Any

import anthropic
from anthropic.types import Message, MessageParam

from src.llm.base import LLMClient

logger = logging.getLogger(__name__)

AUTH_FAILED_MESSAGE = "Anthropic API authentication failed. Please check your ANTHROPIC_API_KEY in .env file."
EMPTY_RESPONSE_MESSAGE = "Anthropic returned empty response"
JSON_PARSE_FAILED_MESSAGE = "Failed to parse JSON response"


def _extract_text_from_blocks(content: list[Any]) -> list[str]:
    """Extract text strings from message content blocks.

    Args:
        content: List of content blocks from Anthropic response

    Returns:
        List of text strings extracted from blocks with text attribute
    """
    result: list[str] = []
    for block in content:
        # Use getattr to safely access text attribute from union type
        text_attr = getattr(block, "text", None)
        if text_attr:
            result.append(text_attr)
    return result


class AnthropicClient(LLMClient):
    """Anthropic API client."""

    def __init__(self, api_key: str, model: str = "claude-3-haiku-20240307") -> None:
        """Initialize the Anthropic client.

        Args:
            api_key: Anthropic API key
            model: Model identifier (default: claude-3-haiku-20240307)
        """
        self._client = anthropic.Anthropic(api_key=api_key)
        self._model = model

    def generate_text(self, prompt: str, system: str | None = None) -> str:
        """Generate text from a prompt using Anthropic API.

        Args:
            prompt: The user prompt
            system: Optional system message

        Returns:
            Raw text response from the LLM
        """
        messages: list[MessageParam] = []
        if system:
            messages.append(MessageParam(role="user", content=system))
        messages.append(MessageParam(role="user", content=prompt))

        logger.info(f"Calling Anthropic model {self._model}")
        try:
            response: Message = self._client.messages.create(
                model=self._model,
                messages=messages,
                temperature=0.0,
                max_tokens=8192,
            )
        except Exception as e:
            error_str = str(e)
            if "401" in error_str or "api_key" in error_str.lower() or "Unauthorized" in error_str:
                raise RuntimeError(AUTH_FAILED_MESSAGE) from e
            raise

        text_parts = _extract_text_from_blocks(response.content)

        if not text_parts:
            raise RuntimeError(EMPTY_RESPONSE_MESSAGE)
        return "".join(text_parts)

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

        messages: list[MessageParam] = []
        if system:
            messages.append(MessageParam(role="user", content=system))
        messages.append(MessageParam(role="user", content=json_prompt))

        logger.info(f"Calling Anthropic model {self._model} for JSON")
        response: Message = self._client.messages.create(
            model=self._model,
            messages=messages,
            temperature=0.0,
            max_tokens=8192,
        )

        json_parts = _extract_text_from_blocks(response.content)

        if not json_parts:
            raise RuntimeError(EMPTY_RESPONSE_MESSAGE)

        content = "".join(json_parts)
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            logger.exception(JSON_PARSE_FAILED_MESSAGE)
            raise
