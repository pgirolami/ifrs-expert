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

    if result.approach_identification_text is not None:
        _write_text_file(output_dir / "A-prompt.txt", result.approach_identification_text)

    if result.approach_identification_output is not None:
        _write_text_file(output_dir / "A-response.json", result.approach_identification_output.model_dump_json(indent=2))

    if result.applicability_analysis_text is not None:
        _write_text_file(output_dir / "B-prompt.txt", result.applicability_analysis_text)

    if result.applicability_analysis_output is not None:
        _write_applicability_analysis_json(output_dir / "B-response.json", result)

    if result.applicability_analysis_memo_markdown is not None:
        _write_text_file(output_dir / "B-response.md", result.applicability_analysis_memo_markdown)

    if result.applicability_analysis_faq_markdown is not None:
        _write_text_file(output_dir / "B-response_faq.md", result.applicability_analysis_faq_markdown)

    _write_retrieval_diagnostic_artifacts(result, output_dir)

    if result.error is not None and result.error_stage == "approach_identification":
        _write_text_file(output_dir / "A-error.txt", result.error)

    if result.error is not None and result.error_stage == "applicability_analysis":
        _write_text_file(output_dir / "B-error.txt", result.error)


def _write_applicability_analysis_json(path: Path, result: AnswerCommandResult) -> None:
    """Write the applicability-analysis JSON artifact."""
    if result.applicability_analysis_output is not None:
        path.write_text(result.applicability_analysis_output.model_dump_json(indent=2), encoding="utf-8")


def _write_retrieval_diagnostic_artifacts(result: AnswerCommandResult, output_dir: Path) -> None:
    """Persist retrieval-side diagnostic source artifacts when available."""
    if result.document_hits:
        _write_text_file(
            output_dir / "document_routing.json",
            json.dumps(
                {
                    "document_hits": [
                        {
                            "doc_uid": hit.doc_uid,
                            "score": hit.score,
                            "document_type": hit.document_type,
                            "document_kind": hit.document_kind,
                        }
                        for hit in result.document_hits
                    ]
                },
                indent=2,
                ensure_ascii=False,
            ),
        )

    if result.chunk_hits:
        _write_text_file(
            output_dir / "target_chunk_retrieval.json",
            json.dumps(
                {
                    "chunks": [
                        {
                            "doc_uid": hit.doc_uid,
                            "document_type": hit.document_type,
                            "document_kind": hit.document_kind,
                            "chunk_number": hit.chunk_number,
                            "chunk_id": hit.chunk_id,
                            "containing_section_id": hit.containing_section_id,
                            "containing_section_db_id": hit.containing_section_db_id,
                            "page_start": hit.page_start,
                            "page_end": hit.page_end,
                            "text": hit.text,
                            "provenance": hit.provenance,
                            "score": hit.score,
                        }
                        for hit in result.chunk_hits
                    ]
                },
                indent=2,
                ensure_ascii=False,
            ),
        )


def _write_text_file(path: Path, content: str) -> None:
    """Write UTF-8 text content to a file."""
    path.write_text(content, encoding="utf-8")
