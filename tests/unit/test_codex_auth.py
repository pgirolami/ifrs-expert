"""Tests for Codex OAuth auth loading."""

from __future__ import annotations

import base64
import json
from pathlib import Path

import pytest

from src.llm.codex_auth import CodexAuthContext, CodexAuthLoader


def _create_access_token(account_id: str) -> str:
    header = base64.urlsafe_b64encode(json.dumps({"alg": "none"}).encode("utf-8")).decode("utf-8").rstrip("=")
    payload = base64.urlsafe_b64encode(
        json.dumps({"https://api.openai.com/auth": {"chatgpt_account_id": account_id}}).encode("utf-8")
    ).decode("utf-8").rstrip("=")
    return f"{header}.{payload}.signature"


def _write_auth_file(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload))


def test_codex_auth_loader_reads_access_token_and_account_id_from_tokens_block(tmp_path: Path) -> None:
    auth_path = tmp_path / "auth.json"
    _write_auth_file(
        auth_path,
        {
            "tokens": {
                "access_token": "test-access-token",
                "account_id": "account-123",
            }
        },
    )

    context = CodexAuthLoader(auth_path=auth_path).load()

    assert context == CodexAuthContext(access_token="test-access-token", account_id="account-123")


def test_codex_auth_loader_decodes_account_id_from_access_token_when_missing_in_file(tmp_path: Path) -> None:
    auth_path = tmp_path / "auth.json"
    access_token = _create_access_token("decoded-account-id")
    _write_auth_file(
        auth_path,
        {
            "tokens": {
                "access_token": access_token,
            }
        },
    )

    context = CodexAuthLoader(auth_path=auth_path).load()

    assert context.account_id == "decoded-account-id"
    assert context.access_token == access_token


def test_codex_auth_loader_raises_clear_error_when_file_is_missing(tmp_path: Path) -> None:
    auth_path = tmp_path / "missing-auth.json"

    with pytest.raises(ValueError, match="codex login"):
        CodexAuthLoader(auth_path=auth_path).load()


def test_codex_auth_loader_raises_clear_error_for_invalid_json(tmp_path: Path) -> None:
    auth_path = tmp_path / "auth.json"
    auth_path.write_text("{not-valid-json")

    with pytest.raises(ValueError, match="Failed to parse"):
        CodexAuthLoader(auth_path=auth_path).load()


def test_codex_auth_loader_raises_clear_error_when_access_token_is_missing(tmp_path: Path) -> None:
    auth_path = tmp_path / "auth.json"
    _write_auth_file(auth_path, {"tokens": {"account_id": "account-123"}})

    with pytest.raises(ValueError, match="access token"):
        CodexAuthLoader(auth_path=auth_path).load()
