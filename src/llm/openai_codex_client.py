"""OpenAI Codex Responses client implementation."""

from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING, Literal, Protocol, TypedDict, cast

import httpx

from src.llm.base import LLMClient

if TYPE_CHECKING:
    from src.llm.codex_auth import CodexAuthContext

logger = logging.getLogger(__name__)

AUTH_FAILED_MESSAGE = "OpenAI Codex authentication failed. Please run 'codex login' and verify your Codex auth.json file."
EMPTY_RESPONSE_MESSAGE = "OpenAI Codex returned empty response"
JSON_PARSE_FAILED_MESSAGE = "Failed to parse JSON response"
DEFAULT_INSTRUCTIONS = "You are a helpful assistant."
REASONING_EFFORT = "low"
REASONING_SUMMARY = "auto"
TEXT_VERBOSITY: Literal["medium"] = "medium"
CODEX_BASE_URL = "https://chatgpt.com/backend-api"
CODEX_RESPONSES_PATH = "/codex/responses"
CODEX_BETA_HEADER_VALUE = "responses=experimental"
CODEX_ORIGINATOR = "pi"
UNAUTHORIZED_STATUS_CODE = 401
HTTP_ERROR_STATUS_MIN = 400


class ResponseFormatConfig(TypedDict):
    """Responses API output format configuration."""

    type: Literal["json_object"]


class ResponseTextConfig(TypedDict, total=False):
    """Responses API text output configuration."""

    verbosity: Literal["medium"]
    format: ResponseFormatConfig


class ReasoningConfig(TypedDict):
    """Responses API reasoning configuration."""

    effort: str
    summary: str


class InputMessage(TypedDict):
    """Minimal Responses API input message."""

    role: Literal["user"]
    content: str


class RequestBody(TypedDict):
    """Minimal Codex Responses request body."""

    model: str
    store: bool
    stream: bool
    instructions: str
    input: list[InputMessage]
    reasoning: ReasoningConfig
    text: ResponseTextConfig
    include: list[str]


class HTTPResponseProtocol(Protocol):
    """Minimal protocol for HTTP responses returned by the transport."""

    status_code: int
    text: str


class HTTPClientProtocol(Protocol):
    """Minimal protocol for the HTTP client used by the Codex transport."""

    def post(
        self,
        url: str,
        *,
        headers: dict[str, str],
        json: RequestBody,
    ) -> HTTPResponseProtocol:
        """Post a JSON request to the Codex backend."""


class OpenAICodexClient(LLMClient):
    """OpenAI Codex client backed by the Codex SSE Responses endpoint."""

    def __init__(
        self,
        model: str,
        auth_context: CodexAuthContext,
        http_client: HTTPClientProtocol | None = None,
    ) -> None:
        """Initialize the OpenAI Codex client."""
        self._model = model
        self._auth_context = auth_context
        self._http_client = http_client or self._create_http_client()

    def generate_text(self, prompt: str, system: str | None = None) -> str:
        """Generate text from a prompt using the Codex Responses API."""
        request_body = self._build_request_body(prompt=prompt, system=system, text_config=self._text_config())

        logger.info(f"Calling OpenAI Codex model {self._model}")
        response = self._post_response(request_body)
        return self._extract_output_text(response)

    def generate_json(self, prompt: str, system: str | None = None) -> dict[str, object]:
        """Generate and parse JSON from a prompt using the Codex Responses API."""
        request_body = self._build_request_body(prompt=prompt, system=system, text_config=self._json_text_config())

        logger.info(f"Calling OpenAI Codex model {self._model} with JSON mode")
        response = self._post_response(request_body)
        content = self._extract_output_text(response)
        return self._parse_json_response(content)

    def _create_http_client(self) -> HTTPClientProtocol:
        return cast("HTTPClientProtocol", httpx.Client(base_url=CODEX_BASE_URL, follow_redirects=True, timeout=60.0))

    def _post_response(self, request_body: RequestBody) -> HTTPResponseProtocol:
        response = self._http_client.post(
            CODEX_RESPONSES_PATH,
            headers=self._build_headers(),
            json=request_body,
        )
        self._raise_for_http_error(response)
        return response

    def _build_headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._auth_context.access_token}",
            "chatgpt-account-id": self._auth_context.account_id,
            "originator": CODEX_ORIGINATOR,
            "OpenAI-Beta": CODEX_BETA_HEADER_VALUE,
            "Accept": "text/event-stream",
            "Content-Type": "application/json",
        }

    def _raise_for_http_error(self, response: HTTPResponseProtocol) -> None:
        if response.status_code == UNAUTHORIZED_STATUS_CODE:
            raise RuntimeError(AUTH_FAILED_MESSAGE)
        if response.status_code >= HTTP_ERROR_STATUS_MIN:
            error_message = self._extract_error_message(response.text)
            raise RuntimeError(error_message)

    def _extract_error_message(self, response_text: str) -> str:
        try:
            payload = json.loads(response_text)
        except json.JSONDecodeError:
            return response_text

        payload_dict = _as_str_object_dict(payload)
        if payload_dict is not None:
            detail = payload_dict.get("detail")
            if isinstance(detail, str) and detail:
                return detail
            error_value = _as_str_object_dict(payload_dict.get("error"))
            if error_value is not None:
                message = error_value.get("message")
                if isinstance(message, str) and message:
                    return message
        return response_text

    def _build_request_body(
        self,
        prompt: str,
        system: str | None,
        text_config: ResponseTextConfig,
    ) -> RequestBody:
        instructions = system or DEFAULT_INSTRUCTIONS
        return {
            "model": self._model,
            "store": False,
            "stream": True,
            "instructions": instructions,
            "input": self._build_input_messages(prompt),
            "reasoning": self._reasoning_config(),
            "text": text_config,
            "include": ["reasoning.encrypted_content"],
        }

    def _build_input_messages(self, prompt: str) -> list[InputMessage]:
        return [{"role": "user", "content": prompt}]

    def _reasoning_config(self) -> ReasoningConfig:
        logger.info(f"Using OpenAI Codex reasoning_effort={REASONING_EFFORT} for model {self._model}")
        return {"effort": REASONING_EFFORT, "summary": REASONING_SUMMARY}

    def _text_config(self) -> ResponseTextConfig:
        return {"verbosity": TEXT_VERBOSITY}

    def _json_text_config(self) -> ResponseTextConfig:
        return {
            "verbosity": TEXT_VERBOSITY,
            "format": {"type": "json_object"},
        }

    def _extract_output_text(self, response: HTTPResponseProtocol) -> str:
        events = self._parse_sse_events(response.text)
        text_fragments: list[str] = []
        fallback_message_text: str | None = None

        for event in events:
            event_type = event.get("type")
            if not isinstance(event_type, str):
                continue

            if event_type == "error":
                error_message = self._extract_event_error_message(event)
                raise RuntimeError(error_message)

            if event_type == "response.failed":
                failed_message = self._extract_failed_response_message(event)
                raise RuntimeError(failed_message)

            if event_type in {"response.output_text.delta", "response.refusal.delta"}:
                delta = event.get("delta")
                if isinstance(delta, str):
                    text_fragments.append(delta)

            if event_type == "response.output_item.done" and not text_fragments:
                fallback_message_text = self._extract_output_item_text(event)

        content = "".join(text_fragments).strip()
        if not content and fallback_message_text:
            content = fallback_message_text.strip()
        if not content:
            raise RuntimeError(EMPTY_RESPONSE_MESSAGE)
        return content

    def _parse_sse_events(self, response_text: str) -> list[dict[str, object]]:
        events: list[dict[str, object]] = []
        for chunk in response_text.split("\n\n"):
            data_lines = [line[5:].strip() for line in chunk.splitlines() if line.startswith("data:")]
            if not data_lines:
                continue

            data = "\n".join(data_lines).strip()
            if not data or data == "[DONE]":
                continue

            try:
                parsed = json.loads(data)
            except json.JSONDecodeError:
                logger.warning(f"Failed to parse Codex SSE event chunk: {data[:200]}")
                continue

            if isinstance(parsed, dict):
                events.append(parsed)
        return events

    def _extract_event_error_message(self, event: dict[str, object]) -> str:
        message = event.get("message")
        if isinstance(message, str) and message:
            return message
        code = event.get("code")
        if isinstance(code, str) and code:
            return code
        return json.dumps(event)

    def _extract_failed_response_message(self, event: dict[str, object]) -> str:
        response_value = _as_str_object_dict(event.get("response"))
        if response_value is None:
            return "Codex response failed"
        error_value = _as_str_object_dict(response_value.get("error"))
        if error_value is None:
            return "Codex response failed"
        message = error_value.get("message")
        if isinstance(message, str) and message:
            return message
        return "Codex response failed"

    def _extract_output_item_text(self, event: dict[str, object]) -> str | None:
        item = _as_str_object_dict(event.get("item"))
        if item is None:
            return None
        item_type = item.get("type")
        if item_type != "message":
            return None
        content_items = _as_object_list(item.get("content"))
        if content_items is None:
            return None

        text_parts = [text_part for content_item in content_items if (text_part := _extract_content_text(content_item))]
        if not text_parts:
            return None
        return "".join(text_parts)

    def _parse_json_response(self, content: str) -> dict[str, object]:
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError:
            logger.exception(JSON_PARSE_FAILED_MESSAGE)
            raise

        parsed_dict = _as_str_object_dict(parsed)
        if parsed_dict is None:
            raise TypeError(JSON_PARSE_FAILED_MESSAGE)
        return parsed_dict


def _as_str_object_dict(value: object) -> dict[str, object] | None:
    if not isinstance(value, dict):
        return None
    return {str(key): item for key, item in value.items()}


def _as_object_list(value: object) -> list[object] | None:
    if not isinstance(value, list):
        return None
    return list(value)


def _extract_content_text(value: object) -> str | None:
    content_dict = _as_str_object_dict(value)
    if content_dict is None:
        return None

    content_type = content_dict.get("type")
    if content_type == "output_text":
        text_value = content_dict.get("text")
        if isinstance(text_value, str):
            return text_value
    if content_type == "refusal":
        refusal_value = content_dict.get("refusal")
        if isinstance(refusal_value, str):
            return refusal_value
    return None
