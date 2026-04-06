"""Tests for the OpenAI Codex client."""

from __future__ import annotations

from dataclasses import dataclass

import pytest

from src.llm.codex_auth import CodexAuthContext
from src.llm.openai_codex_client import DEFAULT_INSTRUCTIONS, EMPTY_RESPONSE_MESSAGE, OpenAICodexClient, RequestBody


@dataclass(frozen=True)
class FakeHTTPResponse:
    """Minimal fake HTTP response."""

    status_code: int
    text: str


class RecordingHTTPClient:
    """Fake HTTP client that records request payloads."""

    def __init__(self, response: FakeHTTPResponse) -> None:
        self._response = response
        self.calls: list[dict[str, object]] = []

    def post(self, url: str, *, headers: dict[str, str], json: RequestBody) -> FakeHTTPResponse:
        self.calls.append({"url": url, "headers": headers, "json": json})
        return self._response


AUTH_CONTEXT = CodexAuthContext(access_token="test-codex-token", account_id="account-123")


def test_generate_text_posts_streaming_request_and_parses_sse_output() -> None:
    fake_client = RecordingHTTPClient(
        FakeHTTPResponse(
            status_code=200,
            text=(
                'data: {"type":"response.output_text.delta","delta":"Codex"}\n\n'
                'data: {"type":"response.output_text.delta","delta":" answer"}\n\n'
                'data: {"type":"response.completed","response":{"status":"completed"}}\n\n'
            ),
        )
    )
    client = OpenAICodexClient(model="gpt-5.1", auth_context=AUTH_CONTEXT, http_client=fake_client)

    result = client.generate_text("What is IFRS 9?", system="Answer precisely")

    assert result == "Codex answer"
    assert len(fake_client.calls) == 1
    call = fake_client.calls[0]
    assert call["url"] == "/codex/responses"
    assert call["json"] == {
        "model": "gpt-5.1",
        "store": False,
        "stream": True,
        "instructions": "Answer precisely",
        "input": [{"role": "user", "content": "What is IFRS 9?"}],
        "reasoning": {"effort": "low", "summary": "auto"},
        "text": {"verbosity": "medium"},
        "include": ["reasoning.encrypted_content"],
    }


def test_generate_json_requests_json_object_output_and_parses_response() -> None:
    fake_client = RecordingHTTPClient(
        FakeHTTPResponse(
            status_code=200,
            text=(
                'data: {"type":"response.output_text.delta","delta":"{\\"answer\\": \\\"yes\\\"}"}\n\n'
                'data: {"type":"response.completed","response":{"status":"completed"}}\n\n'
            ),
        )
    )
    client = OpenAICodexClient(model="gpt-5.1", auth_context=AUTH_CONTEXT, http_client=fake_client)

    result = client.generate_json("Return JSON")

    assert result == {"answer": "yes"}
    assert len(fake_client.calls) == 1
    call = fake_client.calls[0]
    assert call["json"]["instructions"] == DEFAULT_INSTRUCTIONS
    assert call["json"]["text"] == {"verbosity": "medium", "format": {"type": "json_object"}}


def test_generate_text_uses_default_instructions_when_system_is_missing() -> None:
    fake_client = RecordingHTTPClient(
        FakeHTTPResponse(
            status_code=200,
            text='data: {"type":"response.output_text.delta","delta":"Codex answer"}\n\n',
        )
    )
    client = OpenAICodexClient(model="gpt-5.1", auth_context=AUTH_CONTEXT, http_client=fake_client)

    client.generate_text("Return something")

    assert fake_client.calls[0]["json"]["instructions"] == DEFAULT_INSTRUCTIONS


def test_generate_text_falls_back_to_output_item_done_when_no_delta_events_exist() -> None:
    fake_client = RecordingHTTPClient(
        FakeHTTPResponse(
            status_code=200,
            text=(
                'data: {"type":"response.output_item.done","item":{"type":"message","content":[{"type":"output_text","text":"Codex answer"}]}}\n\n'
                'data: {"type":"response.completed","response":{"status":"completed"}}\n\n'
            ),
        )
    )
    client = OpenAICodexClient(model="gpt-5.1", auth_context=AUTH_CONTEXT, http_client=fake_client)

    result = client.generate_text("Return something")

    assert result == "Codex answer"


def test_generate_text_raises_when_output_text_is_empty() -> None:
    fake_client = RecordingHTTPClient(
        FakeHTTPResponse(
            status_code=200,
            text='data: {"type":"response.completed","response":{"status":"completed"}}\n\n',
        )
    )
    client = OpenAICodexClient(model="gpt-5.1", auth_context=AUTH_CONTEXT, http_client=fake_client)

    with pytest.raises(RuntimeError, match=EMPTY_RESPONSE_MESSAGE):
        client.generate_text("Return something")
