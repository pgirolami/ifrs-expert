"""Canonical target chunk retrieval diagnostics contract and renderers."""

from __future__ import annotations

import hashlib
import html
import json
import logging
import os
import re
import sqlite3
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

import yaml

from experiments.analysis.approach_detection.approach_detection_contract import (
    ChunkAuthorityRecord,
    ChunkLookupRecord,
    SectionCell,
    SectionColumn,
    SectionDisplayRecord,
    _canonical_doc_key,
    _collect_section_ids,
    _display_doc_uid,
    _display_section_header,
    _doc_order_from_columns,
    _default_db_path,
    _format_score_range,
    _format_section_cell_summary,
    _load_chunk_lookup,
    _load_chunk_lookup_by_reference,
    _load_expected_section_display_records,
    _load_section_lookup,
    _section_background_color,
    _section_column_is_expected,
    _section_column_key,
    _section_id_overlaps_expected_range,
    _section_sort_key,
)
from experiments.analysis.document_routing.document_routing_contract import humanize_doc_uid, resolve_experiment_dir
from src.retrieval.query_embedding import build_query_embedding_text

logger = logging.getLogger(__name__)

DEFAULT_RUNS_DIRNAME = "runs"
DEFAULT_DIAGNOSTICS_DIRNAME = "diagnostics"
DEFAULT_LAYER_DIRNAME = "target_chunk_retrieval"
DEFAULT_RUN_HTML_FILENAME = "target_chunk_retrieval_diagnostics.html"
DEFAULT_RUN_MD_FILENAME = "target_chunk_retrieval_diagnostics.md"
DEFAULT_RUN_JSON_FILENAME = "target_chunk_retrieval_diagnostics.json"
DEFAULT_INDEX_MD_FILENAME = "target_chunk_retrieval_index.md"
DEFAULT_INDEX_JSON_FILENAME = "target_chunk_retrieval_index.json"
DEFAULT_COMPARE_MD_FILENAME = "target_chunk_retrieval_comparison.md"
DEFAULT_COMPARE_JSON_FILENAME = "target_chunk_retrieval_comparison.json"
DEFAULT_RAW_DIRNAME = "raw"
DEFAULT_PROMPTFOO_DB_FILENAME = "promptfoo.db"
DEFAULT_PROMPTFOO_CONFIG_FILENAME = "promptfooconfig.yaml"
DEFAULT_RUN_METADATA_FILENAME = "run.json"
DEFAULT_ANSWER_SOURCE_FILENAME = "target_chunk_retrieval.json"
DEFAULT_SECTION_TITLE = "Target Chunk Retrieval Diagnostics"


@dataclass(frozen=True)
class PromptfooTestCase:
    """One test case from promptfooconfig.yaml."""

    family_id: str
    question_path: Path
    description: str

    @property
    def question_id(self) -> str:
        return self.question_path.stem


@dataclass(frozen=True)
class ExpectedSectionRange:
    """One expected target section range from family.yaml."""

    document: str
    start: str
    end: str

    @property
    def key(self) -> str:
        return f"{self.document}:{self.start}-{self.end}"

    @property
    def display_label(self) -> str:
        return f"{humanize_doc_uid(self.document)} {self.start}-{self.end}"


@dataclass(frozen=True)
class RetrievedChunk:
    """One retrieved or expanded chunk."""

    doc_uid: str
    chunk_number: str
    chunk_id: str
    score: float
    rank: int
    document_type: str | None
    document_kind: str | None
    containing_section_id: str | None
    text_sha256: str | None
    provenance: str | None = None


@dataclass(frozen=True)
class RangeCoverage:
    """Coverage details for one expected section range."""

    key: str
    document: str
    start: str
    end: str
    display_label: str
    present: bool
    chunk_count: int
    best_rank: int | None
    best_score: float | None
    chunk_numbers: tuple[str, ...]


@dataclass(frozen=True)
class QuestionDiagnostics:
    """Target chunk diagnostics for one question."""

    question_id: str
    run_id: str
    question_path: Path
    question_text: str
    embedded_question_text: str
    question_text_sha256: str
    chunks: tuple[RetrievedChunk, ...]
    target_documents: tuple[str, ...]
    expected_ranges: tuple[RangeCoverage, ...]

    @property
    def target_chunk_count(self) -> int:
        target_documents = set(self.target_documents)
        return sum(1 for chunk in self.chunks if chunk.doc_uid in target_documents)

    @property
    def expected_ranges_present_count(self) -> int:
        return sum(1 for coverage in self.expected_ranges if coverage.present)


@dataclass(frozen=True)
class RangeSummary:
    """Aggregate expected range coverage."""

    key: str
    document: str
    start: str
    end: str
    display_label: str
    question_count: int
    present_count: int
    mean_best_rank: float | None
    score_min: float | None
    score_max: float | None


@dataclass(frozen=True)
class SectionHeaderMetadata:
    """Display metadata for one section column header."""

    display_label: str
    observed_range: str
    provenance_marker: str
    provenance_summary: str
    marker_leading_break: bool = False


@dataclass(frozen=True)
class ChunkSectionEntry:
    """One retrieved chunk with its actual containing section."""

    chunk: RetrievedChunk
    canonical_doc_key: str
    actual_section_id: str


@dataclass(frozen=True)
class RunDiagnostics:
    """One run-level target chunk retrieval diagnostics artifact."""

    experiment_name: str
    provider_name: str
    run_id: str
    generated_at: str
    promptfoo_db_path: str
    eval_id: str
    question_families: tuple[str, ...]
    question_sources: tuple[PromptfooTestCase, ...]
    question_ids: tuple[str, ...]
    policy_name: str
    target_documents: tuple[str, ...]
    expected_section_ranges: tuple[ExpectedSectionRange, ...]
    rows: tuple[QuestionDiagnostics, ...]
    range_summaries: tuple[RangeSummary, ...]

    def to_json(self) -> dict[str, object]:
        return {
            "experiment_name": self.experiment_name,
            "provider_name": self.provider_name,
            "run_id": self.run_id,
            "generated_at": self.generated_at,
            "promptfoo_db_path": self.promptfoo_db_path,
            "eval_id": self.eval_id,
            "question_families": list(self.question_families),
            "question_sources": [
                {
                    "family_id": source.family_id,
                    "question_path": str(source.question_path),
                    "description": source.description,
                    "question_id": source.question_id,
                }
                for source in self.question_sources
            ],
            "question_ids": list(self.question_ids),
            "policy_name": self.policy_name,
            "target_documents": list(self.target_documents),
            "expected_section_ranges": [
                {
                    "document": expected.document,
                    "start": expected.start,
                    "end": expected.end,
                    "key": expected.key,
                    "display_label": expected.display_label,
                }
                for expected in self.expected_section_ranges
            ],
            "rows": [self._row_to_json(row) for row in self.rows],
            "range_summaries": [self._summary_to_json(summary) for summary in self.range_summaries],
        }

    @staticmethod
    def _row_to_json(row: QuestionDiagnostics) -> dict[str, object]:
        return {
            "question_id": row.question_id,
            "run_id": row.run_id,
            "question_path": str(row.question_path),
            "question_text": row.question_text,
            "embedded_question_text": row.embedded_question_text,
            "question_text_sha256": row.question_text_sha256,
            "target_chunk_count": row.target_chunk_count,
            "expected_ranges_present_count": row.expected_ranges_present_count,
            "chunks": [
                {
                    "doc_uid": chunk.doc_uid,
                    "chunk_number": chunk.chunk_number,
                    "chunk_id": chunk.chunk_id,
                    "score": chunk.score,
                    "rank": chunk.rank,
                    "document_type": chunk.document_type,
                    "document_kind": chunk.document_kind,
                    "containing_section_id": chunk.containing_section_id,
                    "text_sha256": chunk.text_sha256,
                    "provenance": chunk.provenance,
                }
                for chunk in row.chunks
            ],
            "expected_ranges": [
                {
                    "key": coverage.key,
                    "document": coverage.document,
                    "start": coverage.start,
                    "end": coverage.end,
                    "display_label": coverage.display_label,
                    "present": coverage.present,
                    "chunk_count": coverage.chunk_count,
                    "best_rank": coverage.best_rank,
                    "best_score": coverage.best_score,
                    "chunk_numbers": list(coverage.chunk_numbers),
                }
                for coverage in row.expected_ranges
            ],
        }

    @staticmethod
    def _summary_to_json(summary: RangeSummary) -> dict[str, object]:
        return {
            "key": summary.key,
            "document": summary.document,
            "start": summary.start,
            "end": summary.end,
            "display_label": summary.display_label,
            "question_count": summary.question_count,
            "present_count": summary.present_count,
            "mean_best_rank": summary.mean_best_rank,
            "score_min": summary.score_min,
            "score_max": summary.score_max,
        }


@dataclass(frozen=True)
class ComparisonRow:
    """One comparison row for one question and expected range."""

    question_id: str
    range_key: str
    display_label: str
    values_by_label: dict[str, dict[str, float | int | bool | None]]


@dataclass(frozen=True)
class ComparisonDiagnostics:
    """Comparison artifact."""

    comparison_name: str
    generated_at: str
    input_labels: tuple[str, ...]
    rows: tuple[ComparisonRow, ...]

    def to_json(self) -> dict[str, object]:
        return {
            "comparison_name": self.comparison_name,
            "generated_at": self.generated_at,
            "input_labels": list(self.input_labels),
            "rows": [
                {
                    "question_id": row.question_id,
                    "range_key": row.range_key,
                    "display_label": row.display_label,
                    "values_by_label": row.values_by_label,
                }
                for row in self.rows
            ],
        }


class TargetChunkRetrievalDiagnosticsGenerator:
    """Generate run-level target chunk retrieval diagnostics."""

    def __init__(self, repo_root: Path) -> None:
        self._repo_root = repo_root

    def generate(self, experiment_dir: Path, run_id: str | None) -> RunDiagnostics:
        run_dir = self._select_run_dir(experiment_dir, run_id)
        run_metadata_path = run_dir / DEFAULT_RUN_METADATA_FILENAME
        promptfooconfig_path = run_dir / DEFAULT_PROMPTFOO_CONFIG_FILENAME
        promptfoo_db_path = experiment_dir / ".promptfoo" / DEFAULT_PROMPTFOO_DB_FILENAME
        if not run_metadata_path.exists():
            raise FileNotFoundError(f"Missing run metadata: {run_metadata_path}")
        if not promptfooconfig_path.exists():
            raise FileNotFoundError(f"Missing promptfooconfig.yaml: {promptfooconfig_path}")
        if not promptfoo_db_path.exists():
            raise FileNotFoundError(f"Missing Promptfoo database: {promptfoo_db_path}")

        run_metadata = _load_json_object(run_metadata_path)
        promptfoo_config = _load_yaml_object(promptfooconfig_path)
        eval_id = self._select_eval_id(promptfoo_db_path, run_metadata)
        active_family_ids = self._active_family_ids_from_run_metadata(run_metadata)
        question_sources = self._load_question_sources(promptfoo_config, active_family_ids=active_family_ids)
        target_documents, expected_ranges = self._load_family_expectations(question_sources)
        result_rows = self._load_eval_results_by_question_id(promptfoo_db_path, eval_id)
        rows = [
            self._build_question_row(
                run_dir=run_dir,
                run_id=run_dir.name,
                source=source,
                result_row=result_rows.get(source.question_id),
                target_documents=target_documents,
                expected_ranges=expected_ranges,
            )
            for source in question_sources
        ]
        summaries = self._build_range_summaries(rows, expected_ranges)
        return RunDiagnostics(
            experiment_name=experiment_dir.name,
            provider_name=self._load_provider_name(promptfoo_config),
            run_id=run_dir.name,
            generated_at=datetime.now(tz=UTC).isoformat(),
            promptfoo_db_path=_path_text(promptfoo_db_path, self._repo_root),
            eval_id=eval_id,
            question_families=_collect_question_families(question_sources),
            question_sources=tuple(question_sources),
            question_ids=tuple(source.question_id for source in question_sources),
            policy_name=self._load_policy_name(promptfoo_config),
            target_documents=tuple(target_documents),
            expected_section_ranges=tuple(expected_ranges),
            rows=tuple(rows),
            range_summaries=tuple(summaries),
        )

    def write_run_artifacts(self, diagnostics: RunDiagnostics, output_dir: Path) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)
        raw_dir = output_dir / DEFAULT_RAW_DIRNAME
        raw_dir.mkdir(parents=True, exist_ok=True)
        for row in diagnostics.rows:
            raw_payload = {"chunks": [chunk for chunk in RunDiagnostics._row_to_json(row)["chunks"]]}
            (raw_dir / f"{row.question_id}.chunks.json").write_text(
                json.dumps(raw_payload, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
        (output_dir / DEFAULT_RUN_JSON_FILENAME).write_text(
            json.dumps(diagnostics.to_json(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (output_dir / DEFAULT_RUN_HTML_FILENAME).write_text(self.render_html(diagnostics), encoding="utf-8")
        (output_dir / DEFAULT_RUN_MD_FILENAME).write_text(self.render_run_markdown(diagnostics), encoding="utf-8")

    def refresh_experiment_index(self, experiment_dir: Path) -> tuple[Path, Path]:
        index_root = experiment_dir / DEFAULT_DIAGNOSTICS_DIRNAME
        index_root.mkdir(parents=True, exist_ok=True)
        runs_dir = experiment_dir / DEFAULT_RUNS_DIRNAME
        if not runs_dir.exists():
            raise FileNotFoundError(f"Missing runs directory: {runs_dir}")
        run_outputs: list[tuple[Path, RunDiagnostics]] = []
        run_entries: list[dict[str, object]] = []
        for run_dir in sorted(runs_dir.iterdir(), key=lambda path: path.name):
            json_path = run_dir / DEFAULT_DIAGNOSTICS_DIRNAME / DEFAULT_LAYER_DIRNAME / DEFAULT_RUN_JSON_FILENAME
            if not json_path.exists():
                continue
            payload = _load_json_object(json_path)
            diagnostics = _run_diagnostics_from_json(payload)
            output_dir = json_path.parent
            run_entries.append(
                {
                    "run_id": diagnostics.run_id,
                    "provider_name": diagnostics.provider_name,
                    "policy_name": diagnostics.policy_name,
                    "output_dir": _path_text(output_dir, self._repo_root),
                    "html_path": _path_text(output_dir / DEFAULT_RUN_HTML_FILENAME, self._repo_root),
                    "markdown_path": _path_text(output_dir / DEFAULT_RUN_MD_FILENAME, self._repo_root),
                    "json_path": _path_text(json_path, self._repo_root),
                }
            )
            run_outputs.append((output_dir, diagnostics))
        index_json = {
            "experiment_name": experiment_dir.name,
            "generated_at": datetime.now(tz=UTC).isoformat(),
            "runs": run_entries,
        }
        index_json_path = index_root / DEFAULT_INDEX_JSON_FILENAME
        index_md_path = index_root / DEFAULT_INDEX_MD_FILENAME
        index_json_path.write_text(json.dumps(index_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        index_md_path.write_text(self.render_index_markdown(experiment_dir.name, index_root, run_outputs), encoding="utf-8")
        return index_md_path, index_json_path

    def render_html(self, diagnostics: RunDiagnostics) -> str:
        """Render target chunk diagnostics as an approach-detection-style HTML matrix."""
        section_columns = self._section_columns(diagnostics.rows, diagnostics.expected_section_ranges)
        header_metadata_by_column = self._section_header_metadata_by_column(diagnostics.rows, section_columns, diagnostics.expected_section_ranges)
        rows_html = "\n".join(
            self._render_html_row(index, row, section_columns)
            for index, row in enumerate(sorted(diagnostics.rows, key=lambda item: _question_sort_key(item.question_id)))
        )
        group_header_html = self._render_group_header(section_columns)
        column_header_html = self._render_column_header(section_columns, header_metadata_by_column)
        controls_html = self._render_controls(section_columns)
        script_html = self._render_script(section_columns)
        style_html = self._render_style()
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Target Chunk Retrieval Diagnostics</title>
  {style_html}
</head>
<body>
  <main>
    <h1>Target Chunk Retrieval Diagnostics</h1>
    <p><strong>Experiment:</strong> {html.escape(diagnostics.experiment_name)}<br>
       <strong>Provider:</strong> {html.escape(diagnostics.provider_name)}<br>
       <strong>Policy:</strong> {html.escape(diagnostics.policy_name)}<br>
       <strong>Generated:</strong> {html.escape(diagnostics.generated_at)}</p>
        <p><strong>Legend:</strong> 🎯 exact target range, ↳ nested subrange of the previous discovered range, 🧭 no retrieved chunks</p>

    {controls_html}

    <div class="table-wrap">
      <table id="matrix-table">
        <thead>
          <tr>
            {group_header_html}
          </tr>
          <tr>
            {column_header_html}
          </tr>
        </thead>
        <tbody>
          {rows_html}
        </tbody>
      </table>
    </div>
  </main>
  {script_html}
</body>
</html>
"""

    def render_run_markdown(self, diagnostics: RunDiagnostics) -> str:
        lines = [
            "This table checks whether the expected target paragraph ranges from the question family were retrieved for each question.",
            "Headers use 🎯 for exact target ranges, ↳ for nested subranges of the previous discovered range, and 🧭 when no retrieved chunks are present.",
            "",
            "| Question | Target chunks | Expected ranges present | " + " | ".join(summary.display_label for summary in diagnostics.range_summaries) + " |",
            "| --- | ---: | ---: | " + " | ".join("---:" for _ in diagnostics.range_summaries) + " |",
        ]
        for row in sorted(diagnostics.rows, key=lambda item: _question_sort_key(item.question_id)):
            coverage_by_key = {coverage.key: coverage for coverage in row.expected_ranges}
            cells = [
                row.question_id,
                str(row.target_chunk_count),
                f"{row.expected_ranges_present_count}/{len(row.expected_ranges)}",
            ]
            for summary in diagnostics.range_summaries:
                coverage = coverage_by_key[summary.key]
                cells.append(_format_coverage_cell(coverage))
            lines.append("| " + " | ".join(cells) + " |")
        total_cells = ["", "Total", ""]
        total_cells.extend(f"{summary.present_count}/{summary.question_count}" for summary in diagnostics.range_summaries)
        lines.append("| " + " | ".join(total_cells) + " |")
        return "\n".join(lines) + "\n"

    def render_index_markdown(
        self,
        experiment_name: str,
        index_root: Path,
        run_outputs: list[tuple[Path, RunDiagnostics]],
    ) -> str:
        lines = [
            f"# {experiment_name} target chunk retrieval diagnostics index",
            "",
            "| Run | Provider | Policy | HTML | Markdown | JSON |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for output_dir, diagnostics in run_outputs:
            html_path = output_dir / DEFAULT_RUN_HTML_FILENAME
            markdown_path = output_dir / DEFAULT_RUN_MD_FILENAME
            json_path = output_dir / DEFAULT_RUN_JSON_FILENAME
            lines.append(
                "| "
                + " | ".join(
                    [
                        diagnostics.run_id,
                        diagnostics.provider_name,
                        diagnostics.policy_name,
                        f"[link]({os.path.relpath(html_path, start=index_root)})",
                        f"[link]({os.path.relpath(markdown_path, start=index_root)})",
                        f"[link]({os.path.relpath(json_path, start=index_root)})",
                    ]
                )
                + " |"
            )
        return "\n".join(lines) + "\n"

    def _render_group_header(self, section_columns: tuple[SectionColumn, ...]) -> str:
        doc_order = _doc_order_from_columns(section_columns)
        counts = dict.fromkeys(doc_order, 0)
        display_names = {column.canonical_doc_key: column.doc_display_name for column in section_columns}
        for section_column in section_columns:
            counts[section_column.canonical_doc_key] += 1
        section_group_headers = "".join(
            f'<th class="group-header section-group" id="group-header-{html.escape(doc_key)}" '
            f'data-doc-key="{html.escape(doc_key)}" colspan="{counts[doc_key]}" '
            f'title="{html.escape(display_names[doc_key])}">{html.escape(display_names[doc_key])}</th>'
            for doc_key in doc_order
        )
        return '<th class="group-header sticky-group" colspan="2" title="Question metadata">Run metadata</th>' + section_group_headers

    def _render_column_header(
        self,
        section_columns: tuple[SectionColumn, ...],
        header_metadata_by_column: dict[str, SectionHeaderMetadata],
    ) -> str:
        metadata_headers = (
            '<th class="sticky-1 metadata-col" title="Question id. Hover question cells for raw and embedded query text.">Q</th>',
            '<th class="sticky-2 metadata-col" title="Number of retrieved chunks from target documents.">🎯 chunks</th>',
        )
        section_headers = tuple(self._render_section_header(section_column, header_metadata_by_column) for section_column in section_columns)
        return "".join((*metadata_headers, *section_headers))

    def _render_section_header(
        self,
        section_column: SectionColumn,
        header_metadata_by_column: dict[str, SectionHeaderMetadata],
    ) -> str:
        metadata = header_metadata_by_column[section_column.column_key]
        lineage_text = " > ".join(section_column.section_lineage)
        tooltip = (
            f"{section_column.doc_display_name}\n"
            f"section_id: {section_column.section_id}\n"
            f"title: {section_column.title}\n"
            f"lineage: {lineage_text}\n"
            f"position: {section_column.position}\n"
            f"display label: {metadata.display_label}\n"
            f"observed range: {metadata.observed_range}\n"
            f"provenance: {metadata.provenance_summary}"
        )
        header_text = html.escape(metadata.provenance_marker)
        if metadata.marker_leading_break:
            header_text = f"<br>{header_text}"
        return (
            f'<th class="section-col {section_column.canonical_doc_key}" '
            f'data-section-key="{html.escape(section_column.column_key)}" '
            f'data-doc-key="{html.escape(section_column.canonical_doc_key)}" '
            f'data-is-target="{"1" if section_column.is_target else "0"}" '
            f'title="{html.escape(tooltip)}">{header_text}{html.escape(metadata.display_label)}</th>'
        )

    def _render_controls(self, section_columns: tuple[SectionColumn, ...]) -> str:
        display_names = {column.canonical_doc_key: column.doc_display_name for column in section_columns}
        doc_toggles = "\n      ".join(
            f'<label><input type="checkbox" class="doc-toggle" data-doc-key="{html.escape(doc_key)}" checked> {html.escape(display_names[doc_key])}</label>'
            for doc_key in _doc_order_from_columns(section_columns)
        )
        return f"""
    <section class="controls">
      <button type="button" data-sort-mode="question">Question order</button>
      <button type="button" data-sort-mode="missing">Missing-first</button>
      <label><input type="checkbox" id="missing-only"> Show only rows with missing targets</label>
      <label><input type="checkbox" id="hide-empty-columns" checked> Hide empty target columns</label>
      {doc_toggles}
    </section>
"""

    def _render_html_row(
        self,
        index: int,
        row: QuestionDiagnostics,
        section_columns: tuple[SectionColumn, ...],
    ) -> str:
        section_cells_by_key = self._section_cells(row)
        section_cells = tuple(self._render_section_cell(section_column, section_cells_by_key.get(section_column.column_key)) for section_column in section_columns)
        missing_count = len(row.expected_ranges) - row.expected_ranges_present_count
        question_tooltip = (
            f"question_id: {row.question_id}\n\n"
            f"question:\n{row.question_text}\n\n"
            f"embedded question:\n{row.embedded_question_text}"
        )
        target_chunk_tooltip = (
            f"target document chunks: {row.target_chunk_count}\n"
            f"expected ranges present: {row.expected_ranges_present_count}/{len(row.expected_ranges)}\n"
            f"target documents: {', '.join(humanize_doc_uid(doc_uid) for doc_uid in row.target_documents)}"
        )
        missing_order = f"{0 if missing_count else 1}:{missing_count:03d}:{row.question_id}:{index:04d}"
        return (
            f'<tr data-order-question="{index}" '
            f'data-order-missing="{html.escape(missing_order)}" '
            f'data-has-missing="{"1" if missing_count else "0"}" '
            f'data-question-id="{html.escape(row.question_id)}">'
            f'<td class="sticky-1 metadata-col metadata-q" title="{html.escape(question_tooltip)}">{html.escape(row.question_id)}</td>'
            f'<td class="sticky-2 metadata-col metadata-rec" title="{html.escape(target_chunk_tooltip)}">{row.target_chunk_count}</td>'
            f'{"".join(section_cells)}'
            '</tr>'
        )

    def _render_section_cell(self, section_column: SectionColumn, section_cell: SectionCell | None) -> str:
        if section_cell is None:
            return (
                f'<td class="section-cell {section_column.canonical_doc_key}" '
                f'data-section-key="{html.escape(section_column.column_key)}" '
                f'data-doc-key="{html.escape(section_column.canonical_doc_key)}" '
                f'data-has-retrieved="0" '
                f'data-has-visible="0"></td>'
            )
        lineage_text = " > ".join(section_column.section_lineage)
        retrieved_summary = _format_section_cell_summary(section_cell.retrieved_display_text, section_cell.retrieved_chunks, include_dropped=True, dropped_chunks=section_cell.dropped_chunks)
        visible_summary = _format_section_cell_summary(section_cell.visible_display_text, section_cell.visible_chunks, include_dropped=True, dropped_chunks=section_cell.dropped_chunks)
        tooltip = (
            f"{section_column.doc_display_name}\n"
            f"section_id: {section_column.section_id}\n"
            f"title: {section_column.title}\n"
            f"lineage: {lineage_text}\n\n"
            f"retrieved chunks:\n{_chunk_authority_lines(section_cell.retrieved_chunks)}\n\n"
            f"visible context chunks:\n{_chunk_authority_lines(section_cell.visible_chunks)}\n\n"
            f"dropped chunks:\n{_chunk_authority_lines(section_cell.dropped_chunks)}\n\n"
            f"retrieved summary: {retrieved_summary.replace('<br>', ' | ')}\n"
            f"visible summary: {visible_summary.replace('<br>', ' | ')}"
        )
        retrieved_color = _section_background_color(section_column.canonical_doc_key, section_cell.retrieved_max_score)
        visible_color = _section_background_color(section_column.canonical_doc_key, section_cell.visible_max_score)
        has_retrieved = "1" if section_cell.retrieved_scores else "0"
        has_visible = "1" if section_cell.visible_scores else "0"
        return (
            f'<td class="section-cell {section_column.canonical_doc_key}" '
            f'data-section-key="{html.escape(section_column.column_key)}" '
            f'data-doc-key="{html.escape(section_column.canonical_doc_key)}" '
            f'data-has-retrieved="{has_retrieved}" '
            f'data-has-visible="{has_visible}" '
            f'data-retrieved-text="{html.escape(retrieved_summary)}" '
            f'data-visible-text="{html.escape(visible_summary)}" '
            f'data-retrieved-bg="{html.escape(retrieved_color)}" '
            f'data-visible-bg="{html.escape(visible_color)}" '
            f'title="{html.escape(tooltip)}" '
            f'style="background-color: {retrieved_color};">{retrieved_summary}</td>'
        )

    def _render_style(self) -> str:
        return """
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 0; color: #1f2937; background: #f8fafc; }
  main { padding: 1rem; }
  h1 { margin-top: 0; }
  .controls { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 1rem; align-items: center; }
  .table-wrap { overflow: auto; border: 1px solid #d1d5db; background: #ffffff; }
  table { border-collapse: collapse; font-size: 12px; width: max-content; min-width: 100%; }
  th, td { border: 1px solid #d1d5db; padding: 0.35rem 0.5rem; text-align: center; white-space: nowrap; }
  thead th { position: sticky; top: 0; z-index: 3; background: #f3f4f6; }
  .group-header { background: #e5e7eb; font-weight: 700; }
  .metadata-col { text-align: left; background: #ffffff; }
  .metadata-q, .metadata-rec { text-align: center; }
  .sticky-1, .sticky-2 { position: sticky; z-index: 2; background: #ffffff; }
  .sticky-1 { left: 0; min-width: 56px; }
  .sticky-2 { left: 56px; min-width: 74px; }
  thead .sticky-1, thead .sticky-2 { z-index: 4; background: #f3f4f6; }
  .section-cell { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; line-height: 1.3; }
  .section-cell-score { display: block; font-weight: 600; }
  .section-cell-authority { display: block; font-size: 11px; color: #374151; }
  button { cursor: pointer; }
</style>
"""

    def _render_script(self, section_columns: tuple[SectionColumn, ...]) -> str:
        section_keys = [section_column.column_key for section_column in section_columns]
        doc_keys = _doc_order_from_columns(section_columns)
        return f"""
<script>
  const tableBody = document.querySelector('#matrix-table tbody');
  const sortButtons = document.querySelectorAll('button[data-sort-mode]');
  const missingOnlyCheckbox = document.getElementById('missing-only');
  const hideEmptyCheckbox = document.getElementById('hide-empty-columns');
  const docToggles = document.querySelectorAll('.doc-toggle');
  const sectionKeys = {json.dumps(section_keys)};
  let currentSortMode = 'question';

  function visibleRows() {{
    return Array.from(tableBody.querySelectorAll('tr')).filter((row) => row.style.display !== 'none');
  }}
  function sortRows(mode) {{
    currentSortMode = mode;
    const rows = Array.from(tableBody.querySelectorAll('tr'));
    rows.sort((left, right) => {{
      const leftValue = left.dataset[mode === 'question' ? 'orderQuestion' : 'orderMissing'];
      const rightValue = right.dataset[mode === 'question' ? 'orderQuestion' : 'orderMissing'];
      if (mode === 'question') {{ return Number(leftValue) - Number(rightValue); }}
      return leftValue.localeCompare(rightValue);
    }});
    rows.forEach((row) => tableBody.appendChild(row));
  }}
  function applyRowVisibility() {{
    const missingOnly = missingOnlyCheckbox.checked;
    Array.from(tableBody.querySelectorAll('tr')).forEach((row) => {{
      const hasMissing = row.dataset.hasMissing === '1';
      row.style.display = (!missingOnly || hasMissing) ? '' : 'none';
    }});
  }}
  function updateSectionVisibility() {{
    const enabledDocs = new Set(Array.from(docToggles).filter((checkbox) => checkbox.checked).map((checkbox) => checkbox.dataset.docKey));
    const rows = visibleRows();
    const hideEmpty = hideEmptyCheckbox.checked;
    const docKeys = {json.dumps(doc_keys)};
    const visibleCounts = Object.fromEntries(docKeys.map((docKey) => [docKey, 0]));
    sectionKeys.forEach((sectionKey) => {{
      const header = document.querySelector(`th[data-section-key="${{sectionKey}}"]`);
      if (!header) {{ return; }}
      const docKey = header.dataset.docKey;
      let visible = enabledDocs.has(docKey);
      if (visible && hideEmpty) {{
        visible = header.dataset.isTarget === '1' || rows.some((row) => {{
          const cell = row.querySelector(`td[data-section-key="${{sectionKey}}"]`);
          return cell && cell.dataset.hasRetrieved === '1';
        }});
      }}
      header.style.display = visible ? '' : 'none';
      document.querySelectorAll(`td[data-section-key="${{sectionKey}}"]`).forEach((cell) => {{ cell.style.display = visible ? '' : 'none'; }});
      if (visible) {{ visibleCounts[docKey] += 1; }}
    }});
    docKeys.forEach((docKey) => {{
      const groupHeader = document.getElementById(`group-header-${{docKey}}`);
      if (!groupHeader) {{ return; }}
      const visibleCount = visibleCounts[docKey];
      groupHeader.style.display = visibleCount > 0 ? '' : 'none';
      groupHeader.colSpan = Math.max(visibleCount, 1);
    }});
  }}
  function applyAll() {{
    applyRowVisibility();
    sortRows(currentSortMode);
    updateSectionVisibility();
  }}
  sortButtons.forEach((button) => button.addEventListener('click', () => {{ sortRows(button.dataset.sortMode); updateSectionVisibility(); }}));
  missingOnlyCheckbox.addEventListener('change', applyAll);
  hideEmptyCheckbox.addEventListener('change', updateSectionVisibility);
  docToggles.forEach((checkbox) => checkbox.addEventListener('change', updateSectionVisibility));
  applyAll();
</script>
"""

    def _section_columns(
        self,
        rows: tuple[QuestionDiagnostics, ...],
        expected_section_ranges: tuple[ExpectedSectionRange, ...],
    ) -> tuple[SectionColumn, ...]:
        chunk_lookup = _load_chunk_lookup(_collect_chunk_db_ids(rows))
        chunk_lookup_by_reference = _load_chunk_lookup_by_reference(_collect_chunk_references(rows))
        expected_display_records = _load_expected_section_display_records(expected_section_ranges)
        section_lookup = _load_section_lookup(
            _collect_section_ids(chunk_lookup)
            | _collect_section_ids(chunk_lookup_by_reference)
            | _collect_direct_section_ids(rows)
        )
        observed_section_ids_by_doc: dict[str, set[str]] = {}
        retrieved_doc_counts: dict[str, int] = {}
        doc_display_names: dict[str, str] = {}
        for row in rows:
            entries = self._chunk_section_entries(row, chunk_lookup, chunk_lookup_by_reference)
            display_section_ids = _display_section_ids_for_entries(entries, row.expected_ranges)
            for index, entry in enumerate(entries):
                chunk = entry.chunk
                canonical_doc_key = _canonical_doc_key(chunk.doc_uid)
                if chunk.score > 0.0:
                    retrieved_doc_counts[canonical_doc_key] = retrieved_doc_counts.get(canonical_doc_key, 0) + 1
                doc_display_names.setdefault(canonical_doc_key, _display_doc_uid(chunk.doc_uid))
                section_id = display_section_ids[index]
                observed_section_ids_by_doc.setdefault(canonical_doc_key, set()).add(section_id)

        for canonical_doc_key, records in expected_display_records.items():
            doc_display_names.setdefault(canonical_doc_key, _display_doc_uid(canonical_doc_key))
            observed_section_ids_by_doc.setdefault(canonical_doc_key, set()).update(record.section_id for record in records)
            for record in records:
                section_lookup.setdefault(record.section_id, record)

        columns: list[SectionColumn] = []
        target_doc_keys = list(dict.fromkeys(_canonical_doc_key(expected_range.document) for expected_range in expected_section_ranges))
        non_target_doc_keys = sorted(
            set(observed_section_ids_by_doc) - set(target_doc_keys),
            key=lambda doc_key: (-retrieved_doc_counts.get(doc_key, 0), doc_display_names[doc_key], doc_key),
        )
        doc_keys = [*target_doc_keys, *non_target_doc_keys]
        for canonical_doc_key in doc_keys:
            if canonical_doc_key not in observed_section_ids_by_doc:
                continue
            display_records = [
                self._section_display_record(canonical_doc_key, section_id, section_lookup)
                for section_id in observed_section_ids_by_doc[canonical_doc_key]
            ]
            display_records.sort(key=lambda record: _section_header_sort_key(record.section_id))
            columns.extend(
                SectionColumn(
                    column_key=_section_column_key(canonical_doc_key, record.section_id),
                    canonical_doc_key=canonical_doc_key,
                    doc_display_name=doc_display_names[canonical_doc_key],
                    section_id=record.section_id,
                    title=record.title,
                    section_lineage=record.section_lineage,
                    position=record.position,
                    is_target=_section_column_is_expected(
                        SectionColumn(
                            column_key=_section_column_key(canonical_doc_key, record.section_id),
                            canonical_doc_key=canonical_doc_key,
                            doc_display_name=doc_display_names[canonical_doc_key],
                            section_id=record.section_id,
                            title=record.title,
                            section_lineage=record.section_lineage,
                            position=record.position,
                        ),
                        expected_section_ranges,
                    ),
                )
                for record in display_records
            )
        exact_target_ranges_by_doc = {
            (_canonical_doc_key(expected_range.document), f"{expected_range.start}-{expected_range.end}")
            for expected_range in expected_section_ranges
        }
        return tuple(
            column
            for column in columns
            if (
                column.section_id.startswith(f"{column.canonical_doc_key}_")
                or (_canonical_doc_key(column.canonical_doc_key), _strip_corpus_prefix(_display_section_header(column.section_id)))
                not in exact_target_ranges_by_doc
            )
        )

    def _section_cells(self, row: QuestionDiagnostics) -> dict[str, SectionCell]:
        chunk_lookup = _load_chunk_lookup(_collect_chunk_db_ids((row,)))
        chunk_lookup_by_reference = _load_chunk_lookup_by_reference(_collect_chunk_references((row,)))
        entries_by_section: dict[str, list[RetrievedChunk]] = {}
        entries = self._chunk_section_entries(row, chunk_lookup, chunk_lookup_by_reference)
        display_section_ids = _display_section_ids_for_entries(entries, row.expected_ranges)
        for index, entry in enumerate(entries):
            section_id = display_section_ids[index]
            display_chunk = self._chunk_with_corpus_chunk_number(entry.chunk, chunk_lookup, chunk_lookup_by_reference)
            entries_by_section.setdefault(_section_column_key(entry.canonical_doc_key, section_id), []).append(display_chunk)
        cells_by_key: dict[str, SectionCell] = {}
        for column_key, chunks in entries_by_section.items():
            section_id = column_key.split("::", maxsplit=1)[1]
            observed_range = _display_observed_chunk_range(section_id, [chunk.chunk_number for chunk in chunks])
            is_target_column = any(
                _canonical_doc_key(expected_range.document) == _canonical_doc_key(chunks[0].doc_uid)
                and observed_range == f"{expected_range.start}-{expected_range.end}"
                for expected_range in row.expected_ranges
            )
            cells_by_key[column_key] = _build_section_cell(chunks, row=row, is_target_column=is_target_column)
        return cells_by_key

    def _chunk_section_entries(
        self,
        row: QuestionDiagnostics,
        chunk_lookup: dict[int, ChunkLookupRecord],
        chunk_lookup_by_reference: dict[tuple[str, str], ChunkLookupRecord],
    ) -> list[ChunkSectionEntry]:
        entries: list[ChunkSectionEntry] = []
        for chunk in row.chunks:
            canonical_doc_key = _canonical_doc_key(chunk.doc_uid)
            entries.append(
                ChunkSectionEntry(
                    chunk=chunk,
                    canonical_doc_key=canonical_doc_key,
                    actual_section_id=self._section_id_for_chunk(chunk, chunk_lookup, chunk_lookup_by_reference),
                )
            )
        return entries

    def _section_header_metadata_by_column(
        self,
        rows: tuple[QuestionDiagnostics, ...],
        section_columns: tuple[SectionColumn, ...],
        expected_section_ranges: tuple[ExpectedSectionRange, ...],
    ) -> dict[str, SectionHeaderMetadata]:
        chunk_numbers_by_column: dict[str, list[str]] = {section_column.column_key: [] for section_column in section_columns}
        provenance_by_column: dict[str, list[str]] = {section_column.column_key: [] for section_column in section_columns}
        score_by_column: dict[str, list[float]] = {section_column.column_key: [] for section_column in section_columns}
        for row in rows:
            section_cells = self._section_cells(row)
            for section_column in section_columns:
                section_cell = section_cells.get(section_column.column_key)
                if section_cell is None:
                    continue
                chunk_numbers_by_column[section_column.column_key].extend(section_cell.retrieved_chunk_numbers)
                score_by_column[section_column.column_key].extend(section_cell.retrieved_scores)
                for chunk in section_cell.retrieved_chunks:
                    if chunk.provenance is None:
                        continue
                    if chunk.provenance not in provenance_by_column[section_column.column_key]:
                        provenance_by_column[section_column.column_key].append(chunk.provenance)

        target_column_keys = self._target_column_keys(section_columns, expected_section_ranges, chunk_numbers_by_column)

        metadata_by_column: dict[str, SectionHeaderMetadata] = {}
        last_non_arrow_range_by_doc: dict[str, str] = {}
        for section_column in section_columns:
            observed_range = _display_observed_chunk_range(section_column.section_id, chunk_numbers_by_column[section_column.column_key])
            expected_section_id = None
            for expected_range in expected_section_ranges:
                if _canonical_doc_key(expected_range.document) != section_column.canonical_doc_key:
                    continue
                if f"{expected_range.start}-{expected_range.end}" == observed_range:
                    expected_section_id = f"{section_column.canonical_doc_key}_{expected_range.start}-{expected_range.end}"
                    break
            exact_target_labels = tuple(
                expected_range.display_label.removeprefix(f"{section_column.doc_display_name} ").strip()
                for expected_range in expected_section_ranges
                if _canonical_doc_key(expected_range.document) == section_column.canonical_doc_key
                and observed_range == f"{expected_range.start}-{expected_range.end}"
            )
            is_target_header = section_column.column_key in target_column_keys and section_column.section_id == expected_section_id
            marker_leading_break = False
            if is_target_header:
                display_label = " / ".join(dict.fromkeys(exact_target_labels))
                provenance_marker = "🎯 "
                last_non_arrow_range_by_doc[section_column.canonical_doc_key] = observed_range
            else:
                display_label = _strip_corpus_prefix(_display_section_header(section_column.section_id))
                previous_non_arrow_range = last_non_arrow_range_by_doc.get(section_column.canonical_doc_key)
                if previous_non_arrow_range is not None and _is_strict_subrange(observed_range, previous_non_arrow_range):
                    provenance_marker = "↳ "
                    marker_leading_break = True
                else:
                    provenance_marker = ""
                    last_non_arrow_range_by_doc[section_column.canonical_doc_key] = observed_range
            metadata_by_column[section_column.column_key] = SectionHeaderMetadata(
                display_label=display_label,
                observed_range=observed_range,
                provenance_marker=provenance_marker,
                provenance_summary=_header_provenance_summary(
                    provenances=provenance_by_column[section_column.column_key],
                    scores=score_by_column[section_column.column_key],
                ),
                marker_leading_break=marker_leading_break,
            )
        return metadata_by_column

    def _target_column_keys(
        self,
        section_columns: tuple[SectionColumn, ...],
        expected_section_ranges: tuple[ExpectedSectionRange, ...],
        chunk_numbers_by_column: dict[str, list[str]],
    ) -> set[str]:
        target_column_keys: set[str] = set()
        for expected_range in expected_section_ranges:
            expected_section_id = f"{_canonical_doc_key(expected_range.document)}_{expected_range.start}-{expected_range.end}"
            matching_columns = [
                section_column
                for section_column in section_columns
                if _canonical_doc_key(expected_range.document) == section_column.canonical_doc_key
                and _section_id_overlaps_expected_range(section_column.section_id, expected_range)
            ]
            exact_matching_columns = [
                section_column
                for section_column in matching_columns
                if _display_observed_chunk_range(section_column.section_id, chunk_numbers_by_column[section_column.column_key])
                == f"{expected_range.start}-{expected_range.end}"
            ]
            if not exact_matching_columns:
                continue
            exact_matching_columns.sort(
                key=lambda section_column: (
                    0 if section_column.section_id == expected_section_id else 1,
                    section_column.position,
                    _section_header_sort_key(section_column.section_id),
                )
            )
            target_column_keys.add(exact_matching_columns[0].column_key)
        return target_column_keys

    def _section_id_for_chunk(
        self,
        chunk: RetrievedChunk,
        chunk_lookup: dict[int, ChunkLookupRecord],
        chunk_lookup_by_reference: dict[tuple[str, str], ChunkLookupRecord],
    ) -> str:
        chunk_record = self._chunk_record_for_chunk(chunk, chunk_lookup, chunk_lookup_by_reference)
        if chunk_record is not None and chunk_record.containing_section_id is not None:
            return chunk_record.containing_section_id
        if chunk.containing_section_id is not None:
            return chunk.containing_section_id
        return f"{_canonical_doc_key(chunk.doc_uid)}_{chunk.chunk_number}"

    def _chunk_record_for_chunk(
        self,
        chunk: RetrievedChunk,
        chunk_lookup: dict[int, ChunkLookupRecord],
        chunk_lookup_by_reference: dict[tuple[str, str], ChunkLookupRecord],
    ) -> ChunkLookupRecord | None:
        chunk_db_id = _chunk_db_id(chunk)
        if chunk_db_id is not None:
            chunk_record = chunk_lookup.get(chunk_db_id)
            if chunk_record is not None:
                return chunk_record
        return chunk_lookup_by_reference.get((_canonical_doc_key(chunk.doc_uid), chunk.chunk_number))

    def _chunk_with_corpus_chunk_number(
        self,
        chunk: RetrievedChunk,
        chunk_lookup: dict[int, ChunkLookupRecord],
        chunk_lookup_by_reference: dict[tuple[str, str], ChunkLookupRecord],
    ) -> RetrievedChunk:
        chunk_record = self._chunk_record_for_chunk(chunk, chunk_lookup, chunk_lookup_by_reference)
        if chunk_record is None:
            return chunk
        return RetrievedChunk(
            doc_uid=chunk.doc_uid,
            chunk_number=chunk_record.chunk_number,
            chunk_id=chunk.chunk_id,
            score=chunk.score,
            rank=chunk.rank,
            document_type=chunk.document_type,
            document_kind=chunk.document_kind,
            containing_section_id=chunk.containing_section_id,
            text_sha256=chunk.text_sha256,
            provenance=chunk.provenance,
        )

    def _section_display_record(
        self,
        canonical_doc_key: str,
        section_id: str,
        section_lookup: dict[str, SectionDisplayRecord],
    ) -> SectionDisplayRecord:
        record = section_lookup.get(section_id)
        if record is not None:
            return record
        return SectionDisplayRecord(
            doc_uid=canonical_doc_key,
            section_id=section_id,
            title=section_id,
            section_lineage=(section_id,),
            position=999_999,
        )

    def _select_run_dir(self, experiment_dir: Path, run_id: str | None) -> Path:
        runs_dir = experiment_dir / DEFAULT_RUNS_DIRNAME
        if not runs_dir.exists():
            raise FileNotFoundError(f"Missing runs directory: {runs_dir}")
        run_dirs = sorted(
            [path for path in runs_dir.iterdir() if path.is_dir() and (path / DEFAULT_RUN_METADATA_FILENAME).exists()],
            key=lambda path: path.name,
        )
        if not run_dirs:
            raise FileNotFoundError(f"No runs found in {runs_dir}")
        if run_id is None:
            if len(run_dirs) != 1:
                raise ValueError(f"{experiment_dir} has {len(run_dirs)} runs; pass --run-id")
            return run_dirs[0]
        matching = [path for path in run_dirs if path.name == run_id or path.name.endswith(run_id)]
        if not matching:
            raise FileNotFoundError(f"Could not find run-id {run_id!r} under {runs_dir}")
        if len(matching) > 1:
            raise ValueError(f"Run id {run_id!r} is ambiguous under {runs_dir}")
        return matching[0]

    def _select_eval_id(self, promptfoo_db_path: Path, run_metadata: dict[str, object]) -> str:
        description = _require_str(run_metadata.get("description"), context="run.json.description")
        created_at = _parse_datetime(_require_str(run_metadata.get("created_at_utc"), context="run.json.created_at_utc"))
        with sqlite3.connect(promptfoo_db_path) as conn:
            conn.row_factory = sqlite3.Row
            eval_rows = conn.execute(
                "SELECT id, created_at FROM evals WHERE description = ?",
                (description,),
            ).fetchall()
        if not eval_rows:
            raise LookupError(f"Could not find any evals for description {description!r}")
        chosen = min(eval_rows, key=lambda row: abs(_eval_created_at(row["created_at"]) - created_at))
        return _require_str(chosen["id"], context="evals.id")

    def _load_question_sources(
        self,
        promptfoo_config: dict[str, object],
        *,
        active_family_ids: set[str] | None,
    ) -> list[PromptfooTestCase]:
        tests = _require_list(promptfoo_config.get("tests"), context="promptfooconfig.yaml: tests")
        question_sources: list[PromptfooTestCase] = []
        for index, test in enumerate(tests):
            test_mapping = _require_mapping(test, context=f"promptfooconfig.yaml: tests[{index}]")
            metadata = _require_mapping(test_mapping.get("metadata"), context=f"promptfooconfig.yaml: tests[{index}].metadata")
            family_id = _require_str(metadata.get("family"), context=f"promptfooconfig.yaml: tests[{index}].metadata.family")
            if active_family_ids is not None and family_id not in active_family_ids:
                continue
            question_path = self._repo_root / _require_str(metadata.get("question_path"), context=f"promptfooconfig.yaml: tests[{index}].metadata.question_path")
            if not question_path.exists():
                raise FileNotFoundError(f"Question file not found: {question_path}")
            description = _require_str(test_mapping.get("description"), context=f"promptfooconfig.yaml: tests[{index}].description")
            question_sources.append(PromptfooTestCase(family_id=family_id, question_path=question_path, description=description))
        if not question_sources:
            raise LookupError("promptfooconfig.yaml did not define any matching tests")
        return question_sources

    def _active_family_ids_from_run_metadata(self, run_metadata: dict[str, object]) -> set[str] | None:
        promptfoo_args = run_metadata.get("promptfoo_args")
        if not isinstance(promptfoo_args, list):
            return None
        family_ids: set[str] = set()
        for index, item in enumerate(promptfoo_args):
            if item != "--filter-metadata" or index + 1 >= len(promptfoo_args):
                continue
            filter_value = promptfoo_args[index + 1]
            if isinstance(filter_value, str) and filter_value.startswith("family="):
                family_ids.add(filter_value.removeprefix("family=").strip())
        return family_ids or None

    def _load_family_expectations(self, question_sources: list[PromptfooTestCase]) -> tuple[list[str], list[ExpectedSectionRange]]:
        target_documents: list[str] = []
        expected_ranges: list[ExpectedSectionRange] = []
        seen_documents: set[str] = set()
        seen_ranges: set[str] = set()
        for source in question_sources:
            family_path = source.question_path.parent / "family.yaml"
            family_data = _load_yaml_object(family_path)
            assert_retrieve = _require_mapping(family_data.get("assert_retrieve"), context=f"{family_path}: assert_retrieve")
            for item in _require_list(assert_retrieve.get("required_documents"), context=f"{family_path}: assert_retrieve.required_documents"):
                doc_uid = _require_str(item, context=f"{family_path}: required_documents[]").lower()
                if doc_uid not in seen_documents:
                    seen_documents.add(doc_uid)
                    target_documents.append(doc_uid)
            for item in _require_list(assert_retrieve.get("required_section_ranges"), context=f"{family_path}: assert_retrieve.required_section_ranges"):
                raw_range = _require_mapping(item, context=f"{family_path}: required_section_ranges[]")
                expected_range = ExpectedSectionRange(
                    document=_require_str(raw_range.get("document"), context=f"{family_path}: range.document").lower(),
                    start=_require_str(raw_range.get("start"), context=f"{family_path}: range.start"),
                    end=_require_str(raw_range.get("end"), context=f"{family_path}: range.end"),
                )
                if expected_range.key in seen_ranges:
                    continue
                seen_ranges.add(expected_range.key)
                expected_ranges.append(expected_range)
        if not expected_ranges:
            raise LookupError("Could not load expected section ranges from family.yaml")
        return target_documents, expected_ranges

    def _load_provider_name(self, promptfoo_config: dict[str, object]) -> str:
        providers = _require_list(promptfoo_config.get("providers"), context="promptfooconfig.yaml: providers")
        provider = _require_mapping(providers[0], context="promptfooconfig.yaml: providers[0]")
        return _require_str(provider.get("label"), context="promptfooconfig.yaml: providers[0].label")

    def _load_policy_name(self, promptfoo_config: dict[str, object]) -> str:
        providers = _require_list(promptfoo_config.get("providers"), context="promptfooconfig.yaml: providers")
        provider = _require_mapping(providers[0], context="promptfooconfig.yaml: providers[0]")
        config = _require_mapping(provider.get("config"), context="promptfooconfig.yaml: providers[0].config")
        retrieval_policy = config.get("retrieval-policy")
        if isinstance(retrieval_policy, str) and retrieval_policy.strip():
            return retrieval_policy.strip()
        llm_provider = config.get("llm_provider")
        if isinstance(llm_provider, str) and llm_provider.strip():
            return llm_provider.strip()
        policy_config = _require_str(config.get("policy-config"), context="promptfooconfig.yaml: providers[0].config.policy-config")
        return Path(policy_config).stem

    def _load_eval_results_by_question_id(self, promptfoo_db_path: Path, eval_id: str) -> dict[str, sqlite3.Row]:
        with sqlite3.connect(promptfoo_db_path) as conn:
            conn.row_factory = sqlite3.Row
            result_rows = conn.execute(
                "SELECT test_idx, response, metadata FROM eval_results WHERE eval_id = ? ORDER BY test_idx, prompt_idx",
                (eval_id,),
            ).fetchall()
        rows_by_question_id: dict[str, sqlite3.Row] = {}
        for row in result_rows:
            metadata = _load_json_text(_require_str(row["metadata"], context="eval_results.metadata"))
            variant = metadata.get("variant")
            if not isinstance(variant, str) or not variant.strip():
                continue
            rows_by_question_id[variant.rstrip("¤")] = row
        return rows_by_question_id

    def _build_question_row(
        self,
        *,
        run_dir: Path,
        run_id: str,
        source: PromptfooTestCase,
        result_row: sqlite3.Row | None,
        target_documents: list[str],
        expected_ranges: list[ExpectedSectionRange],
    ) -> QuestionDiagnostics:
        if result_row is None:
            raise LookupError(f"Missing Promptfoo result for question_id={source.question_id}")
        payload = self._load_chunk_payload(
            promptfoo_response=result_row["response"],
            run_artifacts_dir=run_dir / "artifacts",
            question_source=source,
        )
        question_text = source.question_path.read_text(encoding="utf-8").strip()
        chunks = _parse_chunks(payload)
        return QuestionDiagnostics(
            question_id=source.question_id,
            run_id=run_id,
            question_path=source.question_path,
            question_text=question_text,
            embedded_question_text=build_query_embedding_text(question_text).embedding_text.strip(),
            question_text_sha256=_sha256_text(question_text),
            chunks=chunks,
            target_documents=tuple(target_documents),
            expected_ranges=tuple(_coverage_for_range(expected_range, chunks) for expected_range in expected_ranges),
        )

    def _load_chunk_payload(
        self,
        *,
        promptfoo_response: object,
        run_artifacts_dir: Path,
        question_source: PromptfooTestCase,
    ) -> dict[str, object]:
        try:
            payload = _parse_promptfoo_response(promptfoo_response)
        except (TypeError, json.JSONDecodeError):
            payload = {}
        if _payload_has_chunk_provenance(payload):
            return payload

        fallback_payload = self._load_answer_chunk_artifact(run_artifacts_dir=run_artifacts_dir, question_source=question_source)
        if _payload_has_chunk_provenance(fallback_payload):
            return fallback_payload

        provenance_payload = self._load_document_routing_chunk_artifact(run_artifacts_dir=run_artifacts_dir, question_source=question_source)
        if provenance_payload is not None:
            return provenance_payload

        if fallback_payload is not None:
            return fallback_payload
        return payload

    def _load_answer_chunk_artifact(
        self,
        *,
        run_artifacts_dir: Path,
        question_source: PromptfooTestCase,
    ) -> dict[str, object] | None:
        question_root = run_artifacts_dir / question_source.family_id.strip("¤") / question_source.question_id
        if not question_root.exists():
            return None
        candidates = sorted(question_root.rglob(DEFAULT_ANSWER_SOURCE_FILENAME))
        if not candidates:
            return None
        return _load_json_object(candidates[-1])

    def _load_document_routing_chunk_artifact(
        self,
        *,
        run_artifacts_dir: Path,
        question_source: PromptfooTestCase,
    ) -> dict[str, object] | None:
        run_dir = run_artifacts_dir.parent
        raw_path = run_dir / DEFAULT_DIAGNOSTICS_DIRNAME / "document_routing" / DEFAULT_RAW_DIRNAME / f"{question_source.question_id}.retrieve.json"
        if not raw_path.exists():
            return None
        return _load_json_object(raw_path)

    def _build_range_summaries(
        self,
        rows: list[QuestionDiagnostics],
        expected_ranges: list[ExpectedSectionRange],
    ) -> list[RangeSummary]:
        summaries: list[RangeSummary] = []
        for expected_range in expected_ranges:
            coverages = [coverage for row in rows for coverage in row.expected_ranges if coverage.key == expected_range.key]
            ranks = [coverage.best_rank for coverage in coverages if coverage.best_rank is not None]
            scores = [coverage.best_score for coverage in coverages if coverage.best_score is not None]
            summaries.append(
                RangeSummary(
                    key=expected_range.key,
                    document=expected_range.document,
                    start=expected_range.start,
                    end=expected_range.end,
                    display_label=expected_range.display_label,
                    question_count=len(rows),
                    present_count=sum(1 for coverage in coverages if coverage.present),
                    mean_best_rank=None if not ranks else sum(ranks) / len(ranks),
                    score_min=None if not scores else min(scores),
                    score_max=None if not scores else max(scores),
                )
            )
        return summaries


class TargetChunkRetrievalDiagnosticsComparer:
    """Compare one or more target chunk retrieval diagnostics JSON files."""

    def __init__(self, repo_root: Path) -> None:
        self._repo_root = repo_root

    def compare(self, inputs: list[tuple[str, Path]], output_dir: Path) -> ComparisonDiagnostics:
        run_inputs = self._expand_inputs(inputs)
        if len(run_inputs) < 2:
            raise ValueError("Comparison requires at least two inputs")
        loaded_runs = [(label, _load_json_object(path)) for label, path in run_inputs]
        rows = self._build_rows(loaded_runs)
        diagnostics = ComparisonDiagnostics(
            comparison_name=f"{run_inputs[0][1].stem}__comparison",
            generated_at=datetime.now(tz=UTC).isoformat(),
            input_labels=tuple(label for label, _ in run_inputs),
            rows=tuple(rows),
        )
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / DEFAULT_COMPARE_JSON_FILENAME).write_text(
            json.dumps(diagnostics.to_json(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (output_dir / DEFAULT_COMPARE_MD_FILENAME).write_text(self.render_markdown(diagnostics), encoding="utf-8")
        return diagnostics

    def render_markdown(self, diagnostics: ComparisonDiagnostics) -> str:
        max_delta = self._max_delta(diagnostics)
        lines = [
            f"# {diagnostics.comparison_name}",
            "",
            f"Comparing {', '.join(diagnostics.input_labels)}.",
            "",
            "Each cell shows expected-range chunk count, best rank, and best score. Cells are color-scaled by chunk-count change relative to the first input.",
            "",
            "| Question | Expected range | " + " | ".join(diagnostics.input_labels) + " |",
            "| --- | --- | " + " | ".join("---:" for _ in diagnostics.input_labels) + " |",
        ]
        for row in diagnostics.rows:
            baseline = row.values_by_label[diagnostics.input_labels[0]]
            baseline_count = int(baseline.get("chunk_count") or 0)
            cells = [row.question_id, row.display_label]
            for label in diagnostics.input_labels:
                values = row.values_by_label[label]
                count = int(values.get("chunk_count") or 0)
                rank = values.get("best_rank")
                score = values.get("best_score")
                cells.append(_format_comparison_cell(count, None if rank is None else int(rank), None if score is None else float(score), count - baseline_count, max_delta))
            lines.append("| " + " | ".join(cells) + " |")
        return "\n".join(lines) + "\n"

    def _expand_inputs(self, inputs: list[tuple[str, Path]]) -> list[tuple[str, Path]]:
        expanded: list[tuple[str, Path]] = []
        for label, input_path in inputs:
            payload = _load_json_object(input_path)
            if "runs" in payload:
                for run in _require_list(payload.get("runs"), context=f"{input_path}: runs"):
                    run_mapping = _require_mapping(run, context=f"{input_path}: runs[]")
                    raw_json_path = Path(_require_str(run_mapping.get("json_path"), context=f"{input_path}: runs[].json_path"))
                    json_path = raw_json_path if raw_json_path.is_absolute() else self._repo_root / raw_json_path
                    expanded.append((label, json_path))
            else:
                expanded.append((label, input_path))
        return expanded

    def _build_rows(self, loaded_runs: list[tuple[str, dict[str, object]]]) -> list[ComparisonRow]:
        question_ids = sorted(
            {_require_str(row.get("question_id"), context="rows[].question_id") for _, payload in loaded_runs for row in (_require_mapping(item, context="rows[]") for item in _require_list(payload.get("rows"), context="rows"))},
            key=_question_sort_key,
        )
        range_keys = [
            _require_str(item.get("key"), context="expected_section_ranges[].key")
            for item in (_require_mapping(raw, context="expected_section_ranges[]") for raw in _require_list(loaded_runs[0][1].get("expected_section_ranges"), context="expected_section_ranges"))
        ]
        range_labels = {
            _require_str(item.get("key"), context="expected_section_ranges[].key"): _require_str(item.get("display_label"), context="expected_section_ranges[].display_label")
            for item in (_require_mapping(raw, context="expected_section_ranges[]") for raw in _require_list(loaded_runs[0][1].get("expected_section_ranges"), context="expected_section_ranges"))
        }
        rows: list[ComparisonRow] = []
        for question_id in question_ids:
            for range_key in range_keys:
                values_by_label: dict[str, dict[str, float | int | bool | None]] = {}
                for label, payload in loaded_runs:
                    coverage = _find_coverage(payload, question_id, range_key)
                    values_by_label[label] = {"present": False, "chunk_count": 0, "best_rank": None, "best_score": None} if coverage is None else coverage
                rows.append(
                    ComparisonRow(
                        question_id=question_id,
                        range_key=range_key,
                        display_label=range_labels[range_key],
                        values_by_label=values_by_label,
                    )
                )
        return rows

    def _max_delta(self, diagnostics: ComparisonDiagnostics) -> int:
        baseline_label = diagnostics.input_labels[0]
        max_delta = 0
        for row in diagnostics.rows:
            baseline_count = int(row.values_by_label[baseline_label].get("chunk_count") or 0)
            for label in diagnostics.input_labels[1:]:
                count = int(row.values_by_label[label].get("chunk_count") or 0)
                max_delta = max(max_delta, abs(count - baseline_count))
        return max_delta


class TargetChunkRetrievalDiagnosticsAnalyzer:
    """Summarize diagnostics for EXPERIMENTS.md."""

    def __init__(self, repo_root: Path) -> None:
        self._repo_root = repo_root

    def analyze(self, experiment_dir: Path, input_path: Path | None, section_title: str | None = None) -> str:
        payload, markdown_path = self._load_payload(experiment_dir, input_path)
        if "input_labels" in payload:
            lines = self._analyze_comparison(payload)
        elif "range_summaries" in payload:
            lines = self._analyze_run(payload)
        else:
            raise TypeError("Unsupported target chunk retrieval diagnostics input")
        lines.insert(0, f"- Diagnostics: {_markdown_link(markdown_path, experiment_dir)}")
        rendered = self._render_section(section_title or DEFAULT_SECTION_TITLE, lines)
        experiments_md = experiment_dir / "EXPERIMENTS.md"
        existing = experiments_md.read_text(encoding="utf-8") if experiments_md.exists() else ""
        if existing and not existing.endswith("\n"):
            existing += "\n"
        experiments_md.write_text(existing + "\n" + rendered, encoding="utf-8")
        return rendered

    def _load_payload(self, experiment_dir: Path, input_path: Path | None) -> tuple[dict[str, object], Path]:
        if input_path is None:
            index_path = experiment_dir / DEFAULT_DIAGNOSTICS_DIRNAME / DEFAULT_INDEX_JSON_FILENAME
            if not index_path.exists():
                raise FileNotFoundError(f"Missing diagnostics index: {index_path}")
            index_payload = _load_json_object(index_path)
            runs = _require_list(index_payload.get("runs"), context="index.json: runs")
            if len(runs) != 1:
                raise ValueError(f"{experiment_dir} has {len(runs)} generated runs; pass --input")
            run_entry = _require_mapping(runs[0], context="index.json: runs[0]")
            raw_json_path = Path(_require_str(run_entry.get("json_path"), context="index.json: runs[0].json_path"))
            input_path = raw_json_path if raw_json_path.is_absolute() else self._repo_root / raw_json_path
            raw_markdown_path = Path(_require_str(run_entry.get("markdown_path"), context="index.json: runs[0].markdown_path"))
            markdown_path = raw_markdown_path if raw_markdown_path.is_absolute() else self._repo_root / raw_markdown_path
            return _load_json_object(input_path), markdown_path

        payload = _load_json_object(input_path)
        if "runs" in payload and "experiment_name" in payload:
            runs = _require_list(payload.get("runs"), context="index.json: runs")
            if len(runs) != 1:
                raise ValueError(f"{input_path} has {len(runs)} generated runs; pass a run JSON or comparison JSON")
            run_entry = _require_mapping(runs[0], context="index.json: runs[0]")
            raw_json_path = Path(_require_str(run_entry.get("json_path"), context="index.json: runs[0].json_path"))
            run_json_path = raw_json_path if raw_json_path.is_absolute() else self._repo_root / raw_json_path
            raw_markdown_path = Path(_require_str(run_entry.get("markdown_path"), context="index.json: runs[0].markdown_path"))
            markdown_path = raw_markdown_path if raw_markdown_path.is_absolute() else self._repo_root / raw_markdown_path
            return _load_json_object(run_json_path), markdown_path
        return payload, _markdown_path_for_json(input_path)

    def _analyze_run(self, payload: dict[str, object]) -> list[str]:
        rows = _require_list(payload.get("rows"), context="rows")
        summaries = _require_list(payload.get("range_summaries"), context="range_summaries")
        lines = [
            f"- Run `{_require_str(payload.get('run_id'), context='run_id')}` covered {len(rows)} question(s).",
            f"- Provider: `{_require_str(payload.get('provider_name'), context='provider_name')}`",
        ]
        for item in summaries:
            summary = _require_mapping(item, context="range_summaries[]")
            lines.append(
                f"- {_require_str(summary.get('display_label'), context='range_summaries[].display_label')}: "
                f"{int(_require_num(summary.get('present_count'), context='range_summaries[].present_count'))}/{int(_require_num(summary.get('question_count'), context='range_summaries[].question_count'))} present"
            )
        return lines

    def _analyze_comparison(self, payload: dict[str, object]) -> list[str]:
        input_labels = _require_list(payload.get("input_labels"), context="input_labels")
        rows = _require_list(payload.get("rows"), context="rows")
        return [
            f"- Compared {len(input_labels)} runs across {len(rows)} expected-range row(s).",
            f"- Inputs: {', '.join(str(item) for item in input_labels)}",
        ]

    def _render_section(self, section_title: str, lines: list[str]) -> str:
        return "\n".join([f"## {section_title}", "", *lines, ""])


def _parse_promptfoo_response(response_text: object) -> dict[str, object]:
    if not isinstance(response_text, str):
        raise TypeError("Expected Promptfoo response to be a string")
    outer = json.loads(response_text)
    if not isinstance(outer, dict):
        raise TypeError("Promptfoo response must be a JSON object")
    output = outer.get("output")
    if not isinstance(output, str):
        raise TypeError("Promptfoo response missing output")
    inner = json.loads(output)
    if not isinstance(inner, dict):
        raise TypeError("Promptfoo output must be a JSON object")
    return inner


def _parse_chunks(payload: dict[str, object]) -> tuple[RetrievedChunk, ...]:
    chunks = _require_list(payload.get("chunks"), context="retrieval payload: chunks")
    parsed: list[RetrievedChunk] = []
    for index, raw_chunk in enumerate(chunks, start=1):
        chunk = _require_mapping(raw_chunk, context=f"retrieval payload: chunks[{index}]")
        doc_uid = _require_str(chunk.get("doc_uid"), context=f"retrieval payload: chunks[{index}].doc_uid").lower()
        text = _optional_str(chunk.get("text"))
        parsed.append(
            RetrievedChunk(
                doc_uid=doc_uid,
                chunk_number=_require_str(chunk.get("chunk_number"), context=f"retrieval payload: chunks[{index}].chunk_number"),
                chunk_id=_require_str(chunk.get("chunk_id"), context=f"retrieval payload: chunks[{index}].chunk_id"),
                score=_require_num(chunk.get("score"), context=f"retrieval payload: chunks[{index}].score"),
                rank=index,
                document_type=_optional_str(chunk.get("document_type")),
                document_kind=_optional_str(chunk.get("document_kind")),
                containing_section_id=_optional_str(chunk.get("containing_section_id")),
                text_sha256=None if text is None else _sha256_text(text),
            )
        )
    return tuple(parsed)


def _payload_has_chunk_provenance(payload: dict[str, object] | None) -> bool:
    if payload is None:
        return False
    chunks = payload.get("chunks")
    if not isinstance(chunks, list) or not chunks:
        return False
    for raw_chunk in chunks:
        if not isinstance(raw_chunk, dict):
            continue
        provenance = raw_chunk.get("provenance")
        if isinstance(provenance, str) and provenance:
            return True
    return False


def _coverage_for_range(expected_range: ExpectedSectionRange, chunks: tuple[RetrievedChunk, ...]) -> RangeCoverage:
    matching = [chunk for chunk in chunks if chunk.doc_uid == expected_range.document and _chunk_number_in_range(chunk.chunk_number, expected_range.start, expected_range.end)]
    non_expansion = [chunk for chunk in matching if chunk.score > 0]
    ranked_source = non_expansion or matching
    best_chunk = min(ranked_source, key=lambda chunk: chunk.rank) if ranked_source else None
    scores = [chunk.score for chunk in matching]
    return RangeCoverage(
        key=expected_range.key,
        document=expected_range.document,
        start=expected_range.start,
        end=expected_range.end,
        display_label=expected_range.display_label,
        present=bool(matching),
        chunk_count=len(matching),
        best_rank=None if best_chunk is None else best_chunk.rank,
        best_score=None if not scores else max(scores),
        chunk_numbers=tuple(chunk.chunk_number for chunk in matching),
    )


def _chunk_number_in_range(chunk_number: str, start: str, end: str) -> bool:
    return _section_sort_key(start) <= _section_sort_key(chunk_number) <= _section_sort_key(end)


def _format_coverage_cell(coverage: RangeCoverage) -> str:
    if not coverage.present:
        return '<span style="display:block; background-color:#f8d7da; padding:2px 4px;">missing</span>'
    score_text = "-" if coverage.best_score is None else f"{coverage.best_score:.2f}"
    rank_text = "-" if coverage.best_rank is None else str(coverage.best_rank)
    return f'<span style="display:block; background-color:#d4edda; padding:2px 4px;">{coverage.chunk_count} chunk(s)<br>rank {rank_text}<br>score {score_text}</span>'


def _collect_chunk_db_ids(rows: tuple[QuestionDiagnostics, ...]) -> set[int]:
    chunk_ids: set[int] = set()
    for row in rows:
        for chunk in row.chunks:
            chunk_db_id = _chunk_db_id(chunk)
            if chunk_db_id is not None:
                chunk_ids.add(chunk_db_id)
    return chunk_ids


def _collect_chunk_references(rows: tuple[QuestionDiagnostics, ...]) -> set[tuple[str, str]]:
    references: set[tuple[str, str]] = set()
    for row in rows:
        for chunk in row.chunks:
            canonical_doc_key = _canonical_doc_key(chunk.doc_uid)
            references.add((canonical_doc_key, chunk.chunk_number))
    return references


def _collect_direct_section_ids(rows: tuple[QuestionDiagnostics, ...]) -> set[str]:
    return {
        chunk.containing_section_id
        for row in rows
        for chunk in row.chunks
        if chunk.containing_section_id is not None
    }


def _chunk_db_id(chunk: RetrievedChunk) -> int | None:
    if not chunk.chunk_id.isdigit():
        return None
    return int(chunk.chunk_id)


def _display_section_ids_for_entries(entries: list[ChunkSectionEntry], expected_ranges: tuple[RangeCoverage, ...]) -> dict[int, str]:
    exact_target_section_ids = {
        index: _exact_target_section_id(entry.chunk, expected_ranges)
        for index, entry in enumerate(entries)
        if _exact_target_section_id(entry.chunk, expected_ranges) is not None
    }
    scored_section_ids = {
        entry.actual_section_id
        for entry in entries
        if entry.chunk.score > 0.0
    }
    expanded_section_ids = {
        entry.actual_section_id
        for entry in entries
        if entry.chunk.score <= 0.0
    }
    ancestor_section_ids = _nearest_scored_ancestor_section_ids(
        descendant_section_ids=expanded_section_ids,
        ancestor_section_ids=scored_section_ids,
    )
    return {
        index: exact_target_section_ids.get(index, ancestor_section_ids.get(entry.actual_section_id, entry.actual_section_id))
        for index, entry in enumerate(entries)
    }


def _exact_target_section_id(chunk: RetrievedChunk, expected_ranges: tuple[RangeCoverage, ...]) -> str | None:
    for expected_range in expected_ranges:
        if _canonical_doc_key(expected_range.document) != _canonical_doc_key(chunk.doc_uid):
            continue
        if _chunk_number_in_range(chunk.chunk_number, expected_range.start, expected_range.end):
            return f"{_canonical_doc_key(expected_range.document)}_{expected_range.start}-{expected_range.end}"
    return None


def _nearest_scored_ancestor_section_ids(
    *,
    descendant_section_ids: set[str],
    ancestor_section_ids: set[str],
) -> dict[str, str]:
    if not descendant_section_ids or not ancestor_section_ids:
        return {}
    db_path = _default_db_path()
    if not db_path.exists():
        return {}
    with sqlite3.connect(f"file:{db_path}?mode=ro", uri=True) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT
                descendant.section_id AS descendant_section_id,
                ancestor.section_id AS ancestor_section_id,
                closure.depth AS depth
            FROM section_closure closure
            JOIN sections descendant ON descendant.db_id = closure.descendant_section_db_id
            JOIN sections ancestor ON ancestor.db_id = closure.ancestor_section_db_id
            WHERE descendant.section_id IN (SELECT value FROM json_each(?))
              AND ancestor.section_id IN (SELECT value FROM json_each(?))
              AND closure.depth > 0
            ORDER BY descendant.section_id, closure.depth
            """,
            (json.dumps(sorted(descendant_section_ids)), json.dumps(sorted(ancestor_section_ids))),
        ).fetchall()
    nearest_by_descendant: dict[str, str] = {}
    for row in rows:
        descendant_section_id = str(row["descendant_section_id"])
        if descendant_section_id in nearest_by_descendant:
            continue
        nearest_by_descendant[descendant_section_id] = str(row["ancestor_section_id"])
    return nearest_by_descendant


def _build_section_cell(
    chunks: list[RetrievedChunk],
    *,
    row: QuestionDiagnostics,
    is_target_column: bool = True,
) -> SectionCell:
    sorted_chunks = sorted(chunks, key=lambda chunk: (_section_sort_key(chunk.chunk_number), chunk.score))
    retrieved_chunks = sorted_chunks
    scored_retrieved_scores = tuple(chunk.score for chunk in retrieved_chunks if chunk.score > 0.0)
    retrieved_scores = scored_retrieved_scores or tuple(chunk.score for chunk in retrieved_chunks)
    retrieved_chunk_numbers = tuple(chunk.chunk_number for chunk in retrieved_chunks)
    retrieved_chunk_records = tuple(_chunk_authority_record(chunk, row=row, is_target_column=is_target_column) for chunk in retrieved_chunks)
    return SectionCell(
        retrieved_scores=retrieved_scores,
        retrieved_display_text=_format_score_range(retrieved_scores),
        retrieved_max_score=max(retrieved_scores) if retrieved_scores else None,
        retrieved_chunk_numbers=retrieved_chunk_numbers,
        visible_scores=retrieved_scores,
        visible_display_text=_format_score_range(retrieved_scores),
        visible_max_score=max(retrieved_scores) if retrieved_scores else None,
        visible_chunk_numbers=retrieved_chunk_numbers,
        retrieved_chunks=retrieved_chunk_records,
        visible_chunks=retrieved_chunk_records,
        dropped_chunks=tuple(),
    )


def _chunk_authority_record(chunk: RetrievedChunk, *, row: QuestionDiagnostics, is_target_column: bool = True) -> ChunkAuthorityRecord:
    authority_category = "authoritative" if is_target_column and _is_expected_chunk(chunk.doc_uid, chunk.chunk_number, row.expected_ranges) else "secondary"
    return ChunkAuthorityRecord(
        chunk_number=chunk.chunk_number,
        score=chunk.score,
        authority_category=authority_category,
        dropped=False,
        provenance=chunk.provenance,
    )


def _is_expected_chunk(doc_uid: str, chunk_number: str, expected_ranges: tuple[RangeCoverage, ...]) -> bool:
    canonical_doc_key = _canonical_doc_key(doc_uid)
    for expected_range in expected_ranges:
        if _canonical_doc_key(expected_range.document) != canonical_doc_key:
            continue
        if _chunk_number_in_range(chunk_number, expected_range.start, expected_range.end):
            return True
    return False


def _chunk_authority_lines(chunks: tuple[ChunkAuthorityRecord, ...]) -> str:
    lines = [
        f"- {chunk.chunk_number} ({chunk.score:.2f}) [{chunk.authority_category}] provenance={_chunk_provenance_text(chunk)}"
        for chunk in chunks
    ]
    return "\n".join(lines) if lines else "(none)"


def _chunk_provenance_text(chunk: ChunkAuthorityRecord) -> str:
    if chunk.provenance is not None:
        return chunk.provenance
    return "(missing)"


def _header_provenance_summary(*, provenances: list[str], scores: list[float]) -> str:
    if provenances:
        unique_provenances = list(dict.fromkeys(provenances))
        return ", ".join(unique_provenances)
    if scores:
        return "no provenance recorded"
    return "(missing)"


def _is_strict_subrange(candidate_range: str, container_range: str) -> bool:
    candidate_start, candidate_end = _range_bounds(candidate_range)
    container_start, container_end = _range_bounds(container_range)
    candidate_bounds = (_section_sort_key(candidate_start), _section_sort_key(candidate_end))
    container_bounds = (_section_sort_key(container_start), _section_sort_key(container_end))
    return candidate_bounds != container_bounds and container_bounds[0] <= candidate_bounds[0] <= candidate_bounds[1] <= container_bounds[1]


def _range_bounds(range_text: str) -> tuple[str, str]:
    if "-" not in range_text:
        return range_text, range_text
    start, end = range_text.split("-", maxsplit=1)
    return start, end


def _display_observed_chunk_range(section_id: str, chunk_numbers: list[str]) -> str:
    if not chunk_numbers:
        return _strip_corpus_prefix(_display_section_header(section_id))
    display_header = _display_section_header(section_id)
    range_candidates = [chunk_number for chunk_number in chunk_numbers if _is_paragraph_chunk_number(chunk_number)]
    sorted_chunk_numbers = sorted(set(range_candidates or chunk_numbers), key=_section_sort_key)
    first_chunk = sorted_chunk_numbers[0]
    last_chunk = sorted_chunk_numbers[-1]
    range_text = first_chunk if first_chunk == last_chunk else f"{first_chunk}-{last_chunk}"
    return _strip_corpus_prefix(range_text)


def _strip_corpus_prefix(range_text: str) -> str:
    return range_text.removeprefix("sg").removeprefix("g")


def _section_header_sort_key(section_id: str) -> tuple[str, ...]:
    display_header = _strip_corpus_prefix(_display_section_header(section_id))
    return _section_sort_key(display_header)


def _is_paragraph_chunk_number(chunk_number: str) -> bool:
    return re.fullmatch(r"B?\d+(?:\.\d+)*(?:[A-Z])?", chunk_number) is not None


def _format_comparison_cell(
    count: int,
    rank: int | None,
    score: float | None,
    delta: int,
    max_delta: int,
) -> str:
    color = _comparison_color(delta, max_delta)
    delta_text = f"{delta:+d}"
    rank_text = "-" if rank is None else str(rank)
    score_text = "-" if score is None else f"{score:.2f}"
    return f'<span style="display:block; background-color:{color}; padding:2px 4px;">{count} ({delta_text})<br>rank {rank_text}<br>score {score_text}</span>'


def _comparison_color(delta: int, max_delta: int) -> str:
    if delta == 0 or max_delta <= 0:
        return "#ffffff"
    intensity = min(abs(delta) / max_delta, 1.0)
    if delta > 0:
        red = round(255 - ((255 - 212) * intensity))
        green = round(255 - ((255 - 237) * intensity))
        blue = round(255 - ((255 - 218) * intensity))
    else:
        red = round(255 - ((255 - 248) * intensity))
        green = round(255 - ((255 - 215) * intensity))
        blue = round(255 - ((255 - 218) * intensity))
    return f"#{red:02x}{green:02x}{blue:02x}"


def _find_coverage(payload: dict[str, object], question_id: str, range_key: str) -> dict[str, float | int | bool | None] | None:
    for row in _require_list(payload.get("rows"), context="rows"):
        row_mapping = _require_mapping(row, context="rows[]")
        if _require_str(row_mapping.get("question_id"), context="rows[].question_id") != question_id:
            continue
        for coverage in _require_list(row_mapping.get("expected_ranges"), context="rows[].expected_ranges"):
            coverage_mapping = _require_mapping(coverage, context="rows[].expected_ranges[]")
            if _require_str(coverage_mapping.get("key"), context="rows[].expected_ranges[].key") != range_key:
                continue
            return {
                "present": coverage_mapping.get("present") if isinstance(coverage_mapping.get("present"), bool) else False,
                "chunk_count": int(_require_num(coverage_mapping.get("chunk_count"), context="coverage.chunk_count")),
                "best_rank": None if coverage_mapping.get("best_rank") is None else int(_require_num(coverage_mapping.get("best_rank"), context="coverage.best_rank")),
                "best_score": None if coverage_mapping.get("best_score") is None else _require_num(coverage_mapping.get("best_score"), context="coverage.best_score"),
            }
    return None


def _run_diagnostics_from_json(payload: dict[str, object]) -> RunDiagnostics:
    question_sources = [
        PromptfooTestCase(
            family_id=_require_str(source.get("family_id"), context="question_sources[].family_id"),
            question_path=Path(_require_str(source.get("question_path"), context="question_sources[].question_path")),
            description=_require_str(source.get("description"), context="question_sources[].description"),
        )
        for source in (_require_mapping(item, context="question_sources[]") for item in _require_list(payload.get("question_sources"), context="question_sources"))
    ]
    expected_ranges = [
        ExpectedSectionRange(
            document=_require_str(item.get("document"), context="expected_section_ranges[].document"),
            start=_require_str(item.get("start"), context="expected_section_ranges[].start"),
            end=_require_str(item.get("end"), context="expected_section_ranges[].end"),
        )
        for item in (_require_mapping(raw, context="expected_section_ranges[]") for raw in _require_list(payload.get("expected_section_ranges"), context="expected_section_ranges"))
    ]
    rows = []
    for raw_row in _require_list(payload.get("rows"), context="rows"):
        row = _require_mapping(raw_row, context="rows[]")
        chunks = [
            RetrievedChunk(
                doc_uid=_require_str(chunk.get("doc_uid"), context="rows[].chunks[].doc_uid"),
                chunk_number=_require_str(chunk.get("chunk_number"), context="rows[].chunks[].chunk_number"),
                chunk_id=_require_str(chunk.get("chunk_id"), context="rows[].chunks[].chunk_id"),
                score=_require_num(chunk.get("score"), context="rows[].chunks[].score"),
                rank=int(_require_num(chunk.get("rank"), context="rows[].chunks[].rank")),
                document_type=_optional_str(chunk.get("document_type")),
                document_kind=_optional_str(chunk.get("document_kind")),
                containing_section_id=_optional_str(chunk.get("containing_section_id")),
                text_sha256=_optional_str(chunk.get("text_sha256")),
                provenance=_optional_str(chunk.get("provenance")),
            )
            for chunk in (_require_mapping(item, context="rows[].chunks[]") for item in _require_list(row.get("chunks"), context="rows[].chunks"))
        ]
        ranges = [
            RangeCoverage(
                key=_require_str(coverage.get("key"), context="rows[].expected_ranges[].key"),
                document=_require_str(coverage.get("document"), context="rows[].expected_ranges[].document"),
                start=_require_str(coverage.get("start"), context="rows[].expected_ranges[].start"),
                end=_require_str(coverage.get("end"), context="rows[].expected_ranges[].end"),
                display_label=_require_str(coverage.get("display_label"), context="rows[].expected_ranges[].display_label"),
                present=bool(coverage.get("present")),
                chunk_count=int(_require_num(coverage.get("chunk_count"), context="rows[].expected_ranges[].chunk_count")),
                best_rank=None if coverage.get("best_rank") is None else int(_require_num(coverage.get("best_rank"), context="rows[].expected_ranges[].best_rank")),
                best_score=None if coverage.get("best_score") is None else _require_num(coverage.get("best_score"), context="rows[].expected_ranges[].best_score"),
                chunk_numbers=tuple(_require_str(item, context="rows[].expected_ranges[].chunk_numbers[]") for item in _require_list(coverage.get("chunk_numbers"), context="rows[].expected_ranges[].chunk_numbers")),
            )
            for coverage in (_require_mapping(item, context="rows[].expected_ranges[]") for item in _require_list(row.get("expected_ranges"), context="rows[].expected_ranges"))
        ]
        rows.append(
            QuestionDiagnostics(
                question_id=_require_str(row.get("question_id"), context="rows[].question_id"),
                run_id=_require_str(row.get("run_id"), context="rows[].run_id"),
                question_path=Path(_require_str(row.get("question_path"), context="rows[].question_path")),
                question_text=_optional_str(row.get("question_text")) or "",
                embedded_question_text=_optional_str(row.get("embedded_question_text")) or "",
                question_text_sha256=_require_str(row.get("question_text_sha256"), context="rows[].question_text_sha256"),
                chunks=tuple(chunks),
                target_documents=tuple(_require_str(item, context="target_documents[]") for item in _require_list(payload.get("target_documents"), context="target_documents")),
                expected_ranges=tuple(ranges),
            )
        )
    summaries = [
        RangeSummary(
            key=_require_str(summary.get("key"), context="range_summaries[].key"),
            document=_require_str(summary.get("document"), context="range_summaries[].document"),
            start=_require_str(summary.get("start"), context="range_summaries[].start"),
            end=_require_str(summary.get("end"), context="range_summaries[].end"),
            display_label=_require_str(summary.get("display_label"), context="range_summaries[].display_label"),
            question_count=int(_require_num(summary.get("question_count"), context="range_summaries[].question_count")),
            present_count=int(_require_num(summary.get("present_count"), context="range_summaries[].present_count")),
            mean_best_rank=None if summary.get("mean_best_rank") is None else _require_num(summary.get("mean_best_rank"), context="range_summaries[].mean_best_rank"),
            score_min=None if summary.get("score_min") is None else _require_num(summary.get("score_min"), context="range_summaries[].score_min"),
            score_max=None if summary.get("score_max") is None else _require_num(summary.get("score_max"), context="range_summaries[].score_max"),
        )
        for summary in (_require_mapping(item, context="range_summaries[]") for item in _require_list(payload.get("range_summaries"), context="range_summaries"))
    ]
    return RunDiagnostics(
        experiment_name=_require_str(payload.get("experiment_name"), context="experiment_name"),
        provider_name=_require_str(payload.get("provider_name"), context="provider_name"),
        run_id=_require_str(payload.get("run_id"), context="run_id"),
        generated_at=_require_str(payload.get("generated_at"), context="generated_at"),
        promptfoo_db_path=_require_str(payload.get("promptfoo_db_path"), context="promptfoo_db_path"),
        eval_id=_require_str(payload.get("eval_id"), context="eval_id"),
        question_families=tuple(_require_str(item, context="question_families[]") for item in _require_list(payload.get("question_families"), context="question_families")),
        question_sources=tuple(question_sources),
        question_ids=tuple(_require_str(item, context="question_ids[]") for item in _require_list(payload.get("question_ids"), context="question_ids")),
        policy_name=_require_str(payload.get("policy_name"), context="policy_name"),
        target_documents=tuple(_require_str(item, context="target_documents[]") for item in _require_list(payload.get("target_documents"), context="target_documents")),
        expected_section_ranges=tuple(expected_ranges),
        rows=tuple(rows),
        range_summaries=tuple(summaries),
    )


def _load_json_object(path: Path) -> dict[str, object]:
    return _load_json_text(path.read_text(encoding="utf-8"))


def _load_json_text(text: str) -> dict[str, object]:
    payload = json.loads(text)
    if not isinstance(payload, dict):
        raise TypeError("expected a JSON object")
    return payload


def _load_yaml_object(path: Path) -> dict[str, object]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError(f"{path}: expected a mapping")
    return payload


def _require_mapping(value: object, *, context: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise TypeError(f"{context}: expected a mapping")
    return value


def _require_list(value: object, *, context: str) -> list[object]:
    if not isinstance(value, list):
        raise TypeError(f"{context}: expected a list")
    return value


def _require_str(value: object, *, context: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{context}: expected a string")
    stripped = value.strip()
    if not stripped:
        raise ValueError(f"{context}: empty string")
    return stripped


def _require_num(value: object, *, context: str) -> float:
    if not isinstance(value, int | float):
        raise TypeError(f"{context}: expected a number")
    return float(value)


def _optional_str(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    stripped = value.strip()
    return None if not stripped else stripped


def _parse_datetime(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC)


def _eval_created_at(value: object) -> datetime:
    if not isinstance(value, int):
        raise TypeError(f"Expected integer created_at value, got {value!r}")
    return datetime.fromtimestamp(value / 1000, tz=UTC)


def _question_sort_key(question_id: str) -> tuple[int, str]:
    match = re.search(r"\.(\d+)$", question_id)
    if match is not None:
        return int(match.group(1)), question_id
    return 10**9, question_id


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _path_text(path: Path, base: Path) -> str:
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def _markdown_path_for_json(json_path: Path) -> Path:
    if json_path.name == DEFAULT_COMPARE_JSON_FILENAME:
        return json_path.with_name(DEFAULT_COMPARE_MD_FILENAME)
    if json_path.name == DEFAULT_INDEX_JSON_FILENAME:
        return json_path.with_name(DEFAULT_INDEX_MD_FILENAME)
    return json_path.with_name(DEFAULT_RUN_MD_FILENAME)


def _markdown_link(markdown_path: Path, experiment_dir: Path) -> str:
    relative_path = os.path.relpath(markdown_path, start=experiment_dir)
    return f"[diagnostics markdown]({relative_path})"


def _collect_question_families(question_sources: list[PromptfooTestCase]) -> tuple[str, ...]:
    families: list[str] = []
    seen: set[str] = set()
    for source in question_sources:
        if source.family_id in seen:
            continue
        seen.add(source.family_id)
        families.append(source.family_id)
    return tuple(families)
