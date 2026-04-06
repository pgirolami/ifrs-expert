"""Codex OAuth authentication helpers."""

from __future__ import annotations

import base64
import binascii
import json
import logging
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Never

logger = logging.getLogger(__name__)

CODEX_AUTH_FILE_ENV_VAR = "CODEX_AUTH_FILE"
DEFAULT_CODEX_AUTH_FILE = Path.home() / ".codex" / "auth.json"
JWT_ACCOUNT_CLAIM = "https://api.openai.com/auth"
CHATGPT_ACCOUNT_ID_KEY = "chatgpt_account_id"
JWT_SEGMENT_COUNT = 3
INVALID_CREDENTIAL_MESSAGE = "Codex auth data does not contain a valid access token."
INVALID_AUTH_PAYLOAD_TYPE_MESSAGE = "Invalid Codex auth data payload type. Expected a JSON object."
NOT_A_JWT_MESSAGE = "Codex access token is not a JWT."
JWT_PAYLOAD_NOT_OBJECT_MESSAGE = "Codex access token payload is not a JSON object."
ACCOUNT_CLAIMS_MISSING_MESSAGE = "Codex access token does not contain account claims."
CHATGPT_ACCOUNT_ID_MISSING_MESSAGE = "Codex access token does not contain a chatgpt_account_id."


@dataclass(frozen=True)
class CodexAuthContext:
    """Authentication data loaded from Codex CLI auth.json."""

    access_token: str
    account_id: str


class CodexAuthLoader:
    """Load Codex OAuth credentials from the local Codex auth file."""

    def __init__(self, auth_path: Path | None = None) -> None:
        """Initialize the loader with an optional explicit auth file path."""
        self._auth_path = auth_path or self._resolve_auth_path()

    def load(self) -> CodexAuthContext:
        """Load and validate Codex OAuth credentials."""
        auth_payload = self._load_auth_payload()
        token_payload = self._extract_token_payload(auth_payload)
        access_token = self._extract_access_token(token_payload)
        account_id = self._extract_account_id(token_payload, access_token)
        logger.info(f"Loaded Codex auth context from {self._auth_path}")
        return CodexAuthContext(access_token=access_token, account_id=account_id)

    def _resolve_auth_path(self) -> Path:
        configured_path = os.getenv(CODEX_AUTH_FILE_ENV_VAR)
        if configured_path:
            return Path(configured_path)
        return DEFAULT_CODEX_AUTH_FILE

    def _load_auth_payload(self) -> dict[str, object]:
        if not self._auth_path.exists():
            error_message = f"Codex auth file not found at {self._auth_path}. Please run 'codex login' first."
            _raise_value_error(error_message)

        try:
            raw_payload = json.loads(self._auth_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            error_message = f"Failed to parse Codex auth data from {self._auth_path}: {exc}"
            raise ValueError(error_message) from exc
        except OSError as exc:
            error_message = f"Failed to read Codex auth data from {self._auth_path}: {exc}"
            raise ValueError(error_message) from exc

        if not isinstance(raw_payload, dict):
            error_message = f"Invalid Codex auth data in {self._auth_path}: {INVALID_AUTH_PAYLOAD_TYPE_MESSAGE}"
            _raise_type_error(error_message)

        return raw_payload

    def _extract_token_payload(self, auth_payload: dict[str, object]) -> dict[str, object]:
        tokens_value = auth_payload.get("tokens")
        if isinstance(tokens_value, dict):
            return {str(key): value for key, value in tokens_value.items()}

        chatgpt_value = auth_payload.get("chatgpt")
        if isinstance(chatgpt_value, dict):
            return {str(key): value for key, value in chatgpt_value.items()}

        if "access_token" in auth_payload:
            return auth_payload

        error_message = "Unsupported Codex auth.json structure. Expected 'tokens', 'chatgpt', or top-level 'access_token'."
        raise ValueError(error_message)

    def _extract_access_token(self, token_payload: dict[str, object]) -> str:
        access_token = token_payload.get("access_token")
        if not isinstance(access_token, str) or not access_token:
            _raise_value_error(INVALID_CREDENTIAL_MESSAGE)
        return access_token

    def _extract_account_id(self, token_payload: dict[str, object], access_token: str) -> str:
        account_id = token_payload.get("account_id")
        if isinstance(account_id, str) and account_id:
            return account_id
        return self._decode_account_id(access_token)

    def _decode_account_id(self, access_token: str) -> str:
        try:
            token_parts = access_token.split(".")
            if len(token_parts) != JWT_SEGMENT_COUNT:
                _raise_value_error(NOT_A_JWT_MESSAGE)

            payload_segment = token_parts[1]
            padding = "=" * (-len(payload_segment) % 4)
            decoded_payload = base64.urlsafe_b64decode(payload_segment + padding).decode("utf-8")
            jwt_payload = json.loads(decoded_payload)
            if not isinstance(jwt_payload, dict):
                _raise_type_error(JWT_PAYLOAD_NOT_OBJECT_MESSAGE)

            claim_value = jwt_payload.get(JWT_ACCOUNT_CLAIM)
            if not isinstance(claim_value, dict):
                _raise_type_error(ACCOUNT_CLAIMS_MISSING_MESSAGE)

            account_id = claim_value.get(CHATGPT_ACCOUNT_ID_KEY)
            if not isinstance(account_id, str) or not account_id:
                _raise_value_error(CHATGPT_ACCOUNT_ID_MISSING_MESSAGE)
            else:
                return account_id
        except (TypeError, UnicodeDecodeError, binascii.Error, json.JSONDecodeError, ValueError) as exc:
            error_message = f"Failed to extract chatgpt_account_id from Codex access token: {exc}"
            raise ValueError(error_message) from exc


def _raise_type_error(message: str) -> Never:
    raise TypeError(message)


def _raise_value_error(message: str) -> Never:
    raise ValueError(message)
