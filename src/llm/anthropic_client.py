"""Anthropic LLM client implementation."""

import json
import logging
from typing import Any

import anthropic
from anthropic.types import Message, MessageParam
from anthropic.types.thinking_config_enabled_param import ThinkingConfigEnabledParam

from src.llm.base import LLMClient

logger = logging.getLogger(__name__)

AUTH_FAILED_MESSAGE = "Anthropic API authentication failed. Please check your ANTHROPIC_API_KEY in .env file."
EMPTY_RESPONSE_MESSAGE = "Anthropic returned empty response"
JSON_PARSE_FAILED_MESSAGE = "Failed to parse JSON response"
HIGH_THINKING_BUDGET_TOKENS = 4096
THINKING_MODEL_PREFIXES = ("claude-3-7", "claude-sonnet-4", "claude-opus-4")


def _extract_text_from_blocks(content: list[Any]) -> list[str]:
    """Extract text strings from message content blocks.

    Args:
        content: List of content blocks from Anthropic response

    Returns:
        List of text strings extracted from blocks with text attribute
    """
    result: list[str] = []
    for block in content:
        text_attr = getattr(block, "text", None)
        if text_attr:
            result.append(text_attr)
    return result


class AnthropicClient(LLMClient):
    """Anthropic API client."""

    def __init__(self, api_key: str, model: str) -> None:
        """Initialize the Anthropic client.

        Args:
            api_key: Anthropic API key
            model: Model identifier
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
            response = self._create_message(messages)
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
        json_prompt = f"{prompt}\n\nRespond with valid JSON only, no additional text."

        messages: list[MessageParam] = []
        if system:
            messages.append(MessageParam(role="user", content=system))
        messages.append(MessageParam(role="user", content=json_prompt))

        logger.info(f"Calling Anthropic model {self._model} for JSON")
        response = self._create_message(messages)

        json_parts = _extract_text_from_blocks(response.content)

        if not json_parts:
            raise RuntimeError(EMPTY_RESPONSE_MESSAGE)

        content = "".join(json_parts)
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            logger.exception(JSON_PARSE_FAILED_MESSAGE)
            raise

    def _create_message(self, messages: list[MessageParam]) -> Message:
        """Create an Anthropic message with optional thinking enabled."""
        if self._uses_thinking():
            return self._client.messages.create(
                model=self._model,
                messages=messages,
                temperature=0.0,
                max_tokens=8192,
                thinking=self._thinking_config(),
            )

        return self._client.messages.create(
            model=self._model,
            messages=messages,
            temperature=0.0,
            max_tokens=8192,
        )

    def _uses_thinking(self) -> bool:
        """Return whether the current model supports Anthropic thinking."""
        return self._model.startswith(THINKING_MODEL_PREFIXES)

    def _thinking_config(self) -> ThinkingConfigEnabledParam:
        """Return Anthropic thinking settings for thinking-capable models."""
        logger.info(f"Using Anthropic thinking budget {HIGH_THINKING_BUDGET_TOKENS} for model {self._model}")
        return ThinkingConfigEnabledParam(
            type="enabled",
            budget_tokens=HIGH_THINKING_BUDGET_TOKENS,
        )
