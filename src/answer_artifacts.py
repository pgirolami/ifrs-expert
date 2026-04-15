"""Persistence helpers for answer command artifacts."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path

    from src.models.answer_command_result import AnswerCommandResult


def save_answer_command_result(result: AnswerCommandResult, output_dir: Path) -> None:
    """Persist answer artifacts using the historical CLI file layout."""
    output_dir.mkdir(parents=True, exist_ok=True)

    if result.prompt_a_text is not None:
        _write_text_file(output_dir / "A-prompt.txt", result.prompt_a_text)

    if result.prompt_a_raw_response is not None:
        _write_text_file(output_dir / "A-response.json", result.prompt_a_raw_response)

    if result.prompt_b_text is not None:
        _write_text_file(output_dir / "B-prompt.txt", result.prompt_b_text)

    if result.prompt_b_raw_response is not None:
        _write_b_response_json(output_dir / "B-response.json", result)

    if result.prompt_b_memo_markdown is not None:
        _write_text_file(output_dir / "B-response_memo.md", result.prompt_b_memo_markdown)

    if result.prompt_b_faq_markdown is not None:
        _write_text_file(output_dir / "B-response_faq.md", result.prompt_b_faq_markdown)

    if result.error is not None and result.error_stage == "prompt_a":
        _write_text_file(output_dir / "A-error.txt", result.error)

    if result.error is not None and result.error_stage == "prompt_b":
        _write_text_file(output_dir / "B-error.txt", result.error)


def _write_b_response_json(path: Path, result: AnswerCommandResult) -> None:
    """Write the historical B-response.json artifact."""
    if result.prompt_b_json is not None:
        path.write_text(json.dumps(result.prompt_b_json, indent=2, ensure_ascii=False), encoding="utf-8")
        return

    if result.prompt_b_raw_response is not None:
        path.write_text(result.prompt_b_raw_response, encoding="utf-8")


def _write_text_file(path: Path, content: str) -> None:
    """Write UTF-8 text content to a file."""
    path.write_text(content, encoding="utf-8")
