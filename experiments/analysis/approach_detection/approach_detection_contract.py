"""Canonical approach-detection diagnostics contract and renderers."""

from __future__ import annotations

import html
import importlib
import json
import logging
import os
import re
import shutil
import sqlite3
from dataclasses import dataclass, replace
from datetime import UTC, datetime
from pathlib import Path

import yaml

from experiments.analysis.stability_scorer import compute_stability_score, normalize_label
from src.retrieval.query_embedding import build_query_embedding_text

logger = logging.getLogger(__name__)

DEFAULT_RUNS_DIRNAME = "runs"
DEFAULT_DIAGNOSTICS_DIRNAME = "diagnostics"
DEFAULT_LAYER_DIRNAME = "approach_detection"
DEFAULT_RUN_HTML_FILENAME = "approach_detection_diagnostics.html"
DEFAULT_RUN_MD_FILENAME = "approach_detection_diagnostics.md"
DEFAULT_RUN_JSON_FILENAME = "approach_detection_diagnostics.json"
DEFAULT_INDEX_MD_FILENAME = "approach_detection_index.md"
DEFAULT_INDEX_JSON_FILENAME = "approach_detection_index.json"
DEFAULT_COMPARE_MD_FILENAME = "approach_detection_comparison.md"
DEFAULT_COMPARE_JSON_FILENAME = "approach_detection_comparison.json"
DEFAULT_RAW_DIRNAME = "raw"
DEFAULT_PROMPTFOO_CONFIG_FILENAME = "promptfooconfig.yaml"
DEFAULT_RUN_METADATA_FILENAME = "run.json"
DEFAULT_SECTION_TITLE = "Approach Detection Diagnostics"
DEFAULT_B_RESPONSE_FILENAME = "B-response.json"
DEFAULT_A_RESPONSE_FILENAME = "A-response.json"
DEFAULT_A_PROMPT_FILENAME = "A-prompt.txt"


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


@dataclass(frozen=True)
class PromptChunk:
    """One chunk shown to Prompt B."""

    doc_uid: str
    chunk_number: str
    score: float
    chunk_id: str | None
    expected: bool

    @property
    def chunk_db_id(self) -> int | None:
        if self.chunk_id is None or not self.chunk_id.isdigit():
            return None
        return int(self.chunk_id)


@dataclass(frozen=True)
class ChunkLookupRecord:
    """Chunk metadata loaded from the corpus database."""

    chunk_db_id: int
    doc_uid: str
    chunk_number: str
    containing_section_id: str | None


@dataclass(frozen=True)
class SectionDisplayRecord:
    """Section display metadata loaded from the corpus database."""

    doc_uid: str
    section_id: str
    title: str
    section_lineage: tuple[str, ...]
    position: int


@dataclass(frozen=True)
class SectionColumn:
    """One section column in the HTML matrix."""

    column_key: str
    canonical_doc_key: str
    doc_display_name: str
    section_id: str
    title: str
    section_lineage: tuple[str, ...]
    position: int


@dataclass(frozen=True)
class ChunkAuthorityRecord:
    """One chunk plus its authority categorization status."""

    chunk_number: str
    score: float
    authority_category: str
    dropped: bool


@dataclass(frozen=True)
class SectionCell:
    """One run x section cell with retrieved and visible-context views."""

    retrieved_scores: tuple[float, ...]
    retrieved_display_text: str
    retrieved_max_score: float | None
    retrieved_chunk_numbers: tuple[str, ...]
    visible_scores: tuple[float, ...]
    visible_display_text: str
    visible_max_score: float | None
    visible_chunk_numbers: tuple[str, ...]
    retrieved_chunks: tuple[ChunkAuthorityRecord, ...]
    visible_chunks: tuple[ChunkAuthorityRecord, ...]
    dropped_chunks: tuple[ChunkAuthorityRecord, ...]


@dataclass(frozen=True)
class ApproachRecord:
    """One emitted approach."""

    normalized_label: str
    label: str
    applicability: str | None
    reference_count: int


@dataclass(frozen=True)
class QuestionRunDiagnostics:
    """One Prompt B answer attempt for a question."""

    question_id: str
    question_text: str
    embedded_question_text: str
    family_id: str
    run_label: str
    artifact_dir: Path
    recommendation: str | None
    approaches: tuple[ApproachRecord, ...]
    labels: tuple[str, ...]
    missing_expected_labels: tuple[str, ...]
    spurious_labels: tuple[str, ...]
    prompt_chunks: tuple[PromptChunk, ...]
    authoritative_references: tuple[tuple[str, str], ...]
    secondary_references: tuple[tuple[str, str], ...]
    peripheral_references: tuple[tuple[str, str], ...]
    dropped_documents: tuple[str, ...]


@dataclass(frozen=True)
class LabelSummary:
    """Aggregate frequency for one normalized label."""

    label: str
    expected: bool
    present_count: int
    run_count: int
    question_count: int


@dataclass(frozen=True)
class QuestionStabilitySummary:
    """Stability metrics for one question across repeated outputs."""

    question_id: str
    run_count: int
    stability_score: float
    stability_score_loose: float
    approach_set_stability: float
    applicability_stability: float
    recommendation_stability: float
    missing_expected_count: int
    spurious_count: int


@dataclass(frozen=True)
class RunDiagnostics:
    """One run-level approach-detection diagnostics artifact."""

    experiment_name: str
    provider_name: str
    run_id: str
    generated_at: str
    question_families: tuple[str, ...]
    question_sources: tuple[PromptfooTestCase, ...]
    question_ids: tuple[str, ...]
    expected_labels: tuple[str, ...]
    expected_section_ranges: tuple[ExpectedSectionRange, ...]
    rows: tuple[QuestionRunDiagnostics, ...]
    label_summaries: tuple[LabelSummary, ...]
    question_stability: tuple[QuestionStabilitySummary, ...]

    def to_json(self) -> dict[str, object]:
        return {
            "experiment_name": self.experiment_name,
            "provider_name": self.provider_name,
            "run_id": self.run_id,
            "generated_at": self.generated_at,
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
            "expected_labels": list(self.expected_labels),
            "expected_section_ranges": [{"document": item.document, "start": item.start, "end": item.end} for item in self.expected_section_ranges],
            "rows": [self._row_to_json(row) for row in self.rows],
            "label_summaries": [self._label_summary_to_json(summary) for summary in self.label_summaries],
            "question_stability": [self._stability_to_json(summary) for summary in self.question_stability],
        }

    @staticmethod
    def _row_to_json(row: QuestionRunDiagnostics) -> dict[str, object]:
        return {
            "question_id": row.question_id,
            "question_text": row.question_text,
            "embedded_question_text": row.embedded_question_text,
            "family_id": row.family_id,
            "run_label": row.run_label,
            "artifact_dir": str(row.artifact_dir),
            "recommendation": row.recommendation,
            "approaches": [
                {
                    "normalized_label": approach.normalized_label,
                    "label": approach.label,
                    "applicability": approach.applicability,
                    "reference_count": approach.reference_count,
                }
                for approach in row.approaches
            ],
            "labels": list(row.labels),
            "missing_expected_labels": list(row.missing_expected_labels),
            "spurious_labels": list(row.spurious_labels),
            "prompt_chunks": [
                {
                    "doc_uid": chunk.doc_uid,
                    "chunk_number": chunk.chunk_number,
                    "score": chunk.score,
                    "chunk_id": chunk.chunk_id,
                    "expected": chunk.expected,
                }
                for chunk in row.prompt_chunks
            ],
            "authoritative_references": [list(item) for item in row.authoritative_references],
            "secondary_references": [list(item) for item in row.secondary_references],
            "peripheral_references": [list(item) for item in row.peripheral_references],
            "dropped_documents": list(row.dropped_documents),
        }

    @staticmethod
    def _label_summary_to_json(summary: LabelSummary) -> dict[str, object]:
        return {
            "label": summary.label,
            "expected": summary.expected,
            "present_count": summary.present_count,
            "run_count": summary.run_count,
            "question_count": summary.question_count,
        }

    @staticmethod
    def _stability_to_json(summary: QuestionStabilitySummary) -> dict[str, object]:
        return {
            "question_id": summary.question_id,
            "run_count": summary.run_count,
            "stability_score": summary.stability_score,
            "stability_score_loose": summary.stability_score_loose,
            "approach_set_stability": summary.approach_set_stability,
            "applicability_stability": summary.applicability_stability,
            "recommendation_stability": summary.recommendation_stability,
            "missing_expected_count": summary.missing_expected_count,
            "spurious_count": summary.spurious_count,
        }


@dataclass(frozen=True)
class ComparisonRow:
    """One comparison row for one label."""

    label: str
    expected: bool
    values_by_label: dict[str, dict[str, float | int | bool]]


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
                    "label": row.label,
                    "expected": row.expected,
                    "values_by_label": row.values_by_label,
                }
                for row in self.rows
            ],
        }


class ApproachDetectionDiagnosticsGenerator:
    """Generate run-level approach-detection diagnostics."""

    _chunk_tag_pattern = re.compile(r"<chunk\s+([^>]+)>")
    _attribute_pattern = re.compile(r'(\w+)="([^"]*)"')
    _expected_label_pattern = re.compile(r"labels\.includes\(['\"]([^'\"]+)['\"]\)")

    def __init__(self, repo_root: Path) -> None:
        self._repo_root = repo_root

    def generate(self, experiment_dir: Path, run_id: str | None) -> RunDiagnostics:
        run_dir = self._select_run_dir(experiment_dir, run_id)
        run_metadata_path = run_dir / DEFAULT_RUN_METADATA_FILENAME
        promptfoo_config_path = run_dir / DEFAULT_PROMPTFOO_CONFIG_FILENAME
        if not run_metadata_path.exists():
            raise FileNotFoundError(f"Missing run metadata: {run_metadata_path}")
        if not promptfoo_config_path.exists():
            raise FileNotFoundError(f"Missing promptfooconfig.yaml: {promptfoo_config_path}")

        run_metadata = _load_json_object(run_metadata_path)
        promptfoo_config = _load_yaml_object(promptfoo_config_path)
        active_family_ids = self._active_family_ids_from_run_metadata(run_metadata)
        question_sources = self._load_question_sources(promptfoo_config, active_family_ids=active_family_ids)
        provider_name = self._load_provider_name(promptfoo_config)
        expected_labels = self._load_expected_labels(question_sources)
        expected_ranges = self._load_expected_section_ranges(question_sources)
        rows, raw_payloads = self._load_rows(
            run_dir=run_dir,
            question_sources=question_sources,
            expected_labels=set(expected_labels),
            expected_ranges=expected_ranges,
        )
        diagnostics = RunDiagnostics(
            experiment_name=experiment_dir.name,
            provider_name=provider_name,
            run_id=run_dir.name,
            generated_at=datetime.now(tz=UTC).isoformat(),
            question_families=tuple(_ordered_unique(source.family_id for source in question_sources)),
            question_sources=tuple(question_sources),
            question_ids=tuple(_ordered_unique(source.question_id for source in question_sources)),
            expected_labels=expected_labels,
            expected_section_ranges=expected_ranges,
            rows=tuple(rows),
            label_summaries=self._build_label_summaries(rows, set(expected_labels)),
            question_stability=self._build_question_stability(raw_payloads, set(expected_labels)),
        )
        logger.info(f"Generated approach detection diagnostics rows={len(rows)} run_id={run_dir.name}")
        return diagnostics

    def write_run_artifacts(self, diagnostics: RunDiagnostics, output_dir: Path) -> tuple[Path, Path, Path]:
        output_dir.mkdir(parents=True, exist_ok=True)
        html_path = output_dir / DEFAULT_RUN_HTML_FILENAME
        md_path = output_dir / DEFAULT_RUN_MD_FILENAME
        json_path = output_dir / DEFAULT_RUN_JSON_FILENAME
        html_path.write_text(self.render_html(diagnostics), encoding="utf-8")
        md_path.write_text(self.render_markdown(diagnostics), encoding="utf-8")
        json_path.write_text(json.dumps(diagnostics.to_json(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        self._write_raw_payloads(diagnostics, output_dir / DEFAULT_RAW_DIRNAME)
        return html_path, md_path, json_path

    def refresh_experiment_index(self, experiment_dir: Path) -> tuple[Path, Path]:
        index_root = experiment_dir / DEFAULT_DIAGNOSTICS_DIRNAME
        index_root.mkdir(parents=True, exist_ok=True)
        runs_dir = experiment_dir / DEFAULT_RUNS_DIRNAME
        run_entries: list[dict[str, object]] = []
        run_outputs: list[tuple[Path, RunDiagnostics]] = []
        if runs_dir.exists():
            for run_dir in sorted(runs_dir.iterdir(), key=lambda path: path.name):
                json_path = run_dir / DEFAULT_DIAGNOSTICS_DIRNAME / DEFAULT_LAYER_DIRNAME / DEFAULT_RUN_JSON_FILENAME
                if not json_path.exists():
                    continue
                diagnostics = _run_diagnostics_from_json(_load_json_object(json_path))
                output_dir = json_path.parent
                run_entries.append(
                    {
                        "run_id": diagnostics.run_id,
                        "provider_name": diagnostics.provider_name,
                        "output_dir": _path_text(output_dir, self._repo_root),
                        "html_path": _path_text(output_dir / DEFAULT_RUN_HTML_FILENAME, self._repo_root),
                        "markdown_path": _path_text(output_dir / DEFAULT_RUN_MD_FILENAME, self._repo_root),
                        "json_path": _path_text(json_path, self._repo_root),
                    }
                )
                run_outputs.append((output_dir, diagnostics))
        index_payload = {
            "experiment_name": experiment_dir.name,
            "generated_at": datetime.now(tz=UTC).isoformat(),
            "runs": run_entries,
        }
        index_json_path = index_root / DEFAULT_INDEX_JSON_FILENAME
        index_md_path = index_root / DEFAULT_INDEX_MD_FILENAME
        index_json_path.write_text(json.dumps(index_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        index_md_path.write_text(self.render_index_markdown(experiment_dir.name, index_root, run_outputs), encoding="utf-8")
        return index_md_path, index_json_path

    def render_html(self, diagnostics: RunDiagnostics) -> str:
        label_columns = self._label_columns(diagnostics)
        section_columns = self._section_columns(diagnostics.rows, diagnostics.expected_section_ranges)
        rows_html = "\n".join(self._render_html_row(index, row, label_columns, section_columns) for index, row in enumerate(diagnostics.rows))
        group_header_html = self._render_group_header(label_columns, section_columns)
        column_header_html = self._render_column_header(label_columns, section_columns, diagnostics.expected_section_ranges)
        controls_html = self._render_controls(section_columns)
        spurious_filter_html = self._render_spurious_filter_controls(label_columns, set(diagnostics.expected_labels))
        legend_html = self._render_legend(diagnostics, section_columns)
        script_html = self._render_script(section_columns)
        style_html = self._render_style()
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Approach Identification Diagnostics</title>
  {style_html}
</head>
<body>
  <main>
    <h1>Approach Identification Diagnostics</h1>
    <p><strong>Experiment:</strong> {html.escape(diagnostics.experiment_name)}<br>
       <strong>Provider:</strong> {html.escape(diagnostics.provider_name)}<br>
       <strong>Generated:</strong> {html.escape(diagnostics.generated_at)}</p>

    {controls_html}
    {spurious_filter_html}
    {legend_html}

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

    def render_markdown(self, diagnostics: RunDiagnostics) -> str:
        lines = [
            "# approach_detection_diagnostics",
            "",
            "This report summarizes Prompt B approach labels, missing expected approaches, spurious approaches, repeated-output stability, and authority categorization of visible prompt chunks.",
            "",
            f"- Experiment: `{diagnostics.experiment_name}`",
            f"- Run: `{diagnostics.run_id}`",
            f"- Provider: `{diagnostics.provider_name}`",
            f"- Answer attempts: {len(diagnostics.rows)}",
            "",
            "## Label Frequency",
            "",
            "| Label | Expected | Present | Questions |",
            "| --- | ---: | ---: | ---: |",
        ]
        for summary in diagnostics.label_summaries:
            expected = "yes" if summary.expected else "no"
            lines.append(f"| {summary.label} | {expected} | {summary.present_count}/{summary.run_count} | {summary.question_count} |")
        lines.extend(["", "## Question Stability", "", "| Question | Runs | Strict | Loose | Missing expected | Spurious |", "| --- | ---: | ---: | ---: | ---: | ---: |"])
        for summary in diagnostics.question_stability:
            lines.append(f"| {summary.question_id} | {summary.run_count} | {summary.stability_score:.1f} | {summary.stability_score_loose:.1f} | {summary.missing_expected_count} | {summary.spurious_count} |")

        section_columns = self._section_columns(diagnostics.rows, diagnostics.expected_section_ranges)
        lines.extend(["", "## Authority Categorization by Run", ""])
        for row in diagnostics.rows:
            lines.extend([
                f"### {row.question_id} / {_display_run_id(row.run_label)}",
                "",
                f"- Question: {row.question_text}",
                f"- Embedded question: {row.embedded_question_text}",
                "",
                "| Document | Section range | Category | Retrieved score | Dropped |",
                "| --- | --- | --- | --- | --- |",
            ])
            section_cells_by_key = self._section_cells(row)
            for section_column in section_columns:
                section_cell = section_cells_by_key.get(section_column.column_key)
                if section_cell is None:
                    continue
                range_category = _section_range_category(section_cell)
                lines.append(
                    f"| {section_column.doc_display_name} | {_display_section_header(section_column.section_id)} | "
                    f"{_range_category_emoji(range_category)} {range_category} | "
                    f"{section_cell.retrieved_display_text or '—'} | "
                    f"D:{len(section_cell.dropped_chunks)} |"
                )
            dropped_lines = _markdown_dropped_chunk_lines(section_columns, section_cells_by_key)
            if dropped_lines:
                lines.extend(["", "Dropped chunks:", "", *dropped_lines])
            lines.append("")
        return "\n".join(lines) + "\n"

    def render_index_markdown(
        self,
        experiment_name: str,
        index_root: Path,
        run_outputs: list[tuple[Path, RunDiagnostics]],
    ) -> str:
        lines = [
            f"# {experiment_name} approach detection diagnostics index",
            "",
            "| Run | Provider | HTML | Markdown | JSON |",
            "| --- | --- | --- | --- | --- |",
        ]
        for output_dir, diagnostics in run_outputs:
            lines.append(
                "| "
                + " | ".join(
                    [
                        diagnostics.run_id,
                        diagnostics.provider_name,
                        f"[link]({os.path.relpath(output_dir / DEFAULT_RUN_HTML_FILENAME, start=index_root)})",
                        f"[link]({os.path.relpath(output_dir / DEFAULT_RUN_MD_FILENAME, start=index_root)})",
                        f"[link]({os.path.relpath(output_dir / DEFAULT_RUN_JSON_FILENAME, start=index_root)})",
                    ]
                )
                + " |"
            )
        return "\n".join(lines) + "\n"

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

    def _load_question_sources(
        self,
        promptfoo_config: dict[str, object],
        *,
        active_family_ids: set[str] | None,
    ) -> list[PromptfooTestCase]:
        tests = _require_list(promptfoo_config.get("tests"), context="promptfooconfig.yaml: tests")
        question_sources: list[PromptfooTestCase] = []
        for index, raw_test in enumerate(tests):
            test = _require_mapping(raw_test, context=f"promptfooconfig.yaml: tests[{index}]")
            metadata = _require_mapping(test.get("metadata"), context=f"promptfooconfig.yaml: tests[{index}].metadata")
            family_id = _require_str(metadata.get("family"), context=f"promptfooconfig.yaml: tests[{index}].metadata.family")
            normalized_family_id = _normalize_family_id(family_id)
            if active_family_ids is not None and normalized_family_id not in active_family_ids:
                continue
            question_path = Path(_require_str(metadata.get("question_path"), context=f"promptfooconfig.yaml: tests[{index}].metadata.question_path"))
            resolved_question_path = question_path if question_path.is_absolute() else self._repo_root / question_path
            if not resolved_question_path.exists():
                raise FileNotFoundError(f"Question path not found: {resolved_question_path}")
            question_sources.append(
                PromptfooTestCase(
                    family_id=family_id,
                    question_path=question_path,
                    description=_require_str(test.get("description"), context=f"promptfooconfig.yaml: tests[{index}].description"),
                )
            )
        if not question_sources:
            raise ValueError("No promptfoo tests matched the selected run family filter")
        return question_sources

    def _active_family_ids_from_run_metadata(self, run_metadata: dict[str, object]) -> set[str] | None:
        promptfoo_args = run_metadata.get("promptfoo_args")
        if not isinstance(promptfoo_args, list):
            return None
        active_family_ids: set[str] = set()
        for index, value in enumerate(promptfoo_args):
            if value != "--filter-metadata" or index + 1 >= len(promptfoo_args):
                continue
            next_value = promptfoo_args[index + 1]
            if not isinstance(next_value, str) or not next_value.startswith("family="):
                continue
            active_family_ids.add(_normalize_family_id(next_value.split("=", 1)[1]))
        return active_family_ids or None

    def _load_provider_name(self, promptfoo_config: dict[str, object]) -> str:
        providers = _require_list(promptfoo_config.get("providers"), context="promptfooconfig.yaml: providers")
        provider = _require_mapping(providers[0], context="promptfooconfig.yaml: providers[0]")
        return _require_str(provider.get("label"), context="promptfooconfig.yaml: providers[0].label")

    def _load_expected_labels(self, question_sources: list[PromptfooTestCase]) -> tuple[str, ...]:
        labels: list[str] = []
        for family_path in self._family_paths(question_sources):
            family = _load_yaml_object(family_path)
            assertions = _require_list(family.get("assert"), context=f"{family_path}: assert")
            for assertion in assertions:
                assertion_mapping = _require_mapping(assertion, context=f"{family_path}: assert[]")
                raw_value = assertion_mapping.get("value")
                if not isinstance(raw_value, str):
                    continue
                for match in self._expected_label_pattern.finditer(raw_value):
                    labels.append(normalize_label(match.group(1)))
        return tuple(_ordered_unique(labels))

    def _load_expected_section_ranges(self, question_sources: list[PromptfooTestCase]) -> tuple[ExpectedSectionRange, ...]:
        ranges: list[ExpectedSectionRange] = []
        for family_path in self._family_paths(question_sources):
            family = _load_yaml_object(family_path)
            assert_retrieve = family.get("assert_retrieve")
            if not isinstance(assert_retrieve, dict):
                continue
            raw_ranges = assert_retrieve.get("required_section_ranges")
            if not isinstance(raw_ranges, list):
                continue
            for raw_range in raw_ranges:
                range_mapping = _require_mapping(raw_range, context=f"{family_path}: assert_retrieve.required_section_ranges[]")
                ranges.append(
                    ExpectedSectionRange(
                        document=_require_str(range_mapping.get("document"), context="required_section_ranges[].document"),
                        start=_require_str(range_mapping.get("start"), context="required_section_ranges[].start"),
                        end=_require_str(range_mapping.get("end"), context="required_section_ranges[].end"),
                    )
                )
        return tuple(ranges)

    def _family_paths(self, question_sources: list[PromptfooTestCase]) -> list[Path]:
        family_dirs: list[Path] = []
        seen: set[Path] = set()
        for source in question_sources:
            question_path = source.question_path if source.question_path.is_absolute() else self._repo_root / source.question_path
            family_dir = question_path.parent
            if family_dir in seen:
                continue
            seen.add(family_dir)
            family_dirs.append(family_dir)
        return [family_dir / "family.yaml" for family_dir in family_dirs]

    def _load_rows(
        self,
        *,
        run_dir: Path,
        question_sources: list[PromptfooTestCase],
        expected_labels: set[str],
        expected_ranges: tuple[ExpectedSectionRange, ...],
    ) -> tuple[list[QuestionRunDiagnostics], dict[str, list[dict[str, object]]]]:
        artifacts_dir = run_dir / "artifacts"
        if not artifacts_dir.exists():
            raise FileNotFoundError(f"Missing artifacts directory: {artifacts_dir}")
        rows: list[QuestionRunDiagnostics] = []
        raw_payloads_by_question: dict[str, list[dict[str, object]]] = {}
        for source in question_sources:
            family_dirname = _normalize_family_id(source.family_id)
            resolved_question_path = source.question_path if source.question_path.is_absolute() else self._repo_root / source.question_path
            question_text = resolved_question_path.read_text(encoding="utf-8").strip()
            embedded_question_text = build_query_embedding_text(question_text).embedding_text.strip()
            question_dirs = self._find_question_artifact_dirs(
                artifacts_dir=artifacts_dir,
                family_dirname=family_dirname,
                question_id=source.question_id,
            )
            if not question_dirs:
                logger.warning(f"Skipping missing approach artifact question_id={source.question_id} family={family_dirname}")
                continue
            for question_dir in question_dirs:
                for artifact_dir, run_label in self._iter_answer_artifact_dirs(question_dir):
                    payload = self._load_preferred_response_payload(artifact_dir)
                    raw_payloads_by_question.setdefault(source.question_id, []).append(payload)
                    prompt_chunks = self._load_prompt_chunks(artifact_dir / DEFAULT_A_PROMPT_FILENAME, expected_ranges)
                    approaches = _parse_approaches(payload)
                    labels = tuple(_ordered_unique(approach.normalized_label for approach in approaches if approach.normalized_label))
                    authoritative_references, secondary_references, peripheral_references, dropped_documents = _extract_authority_diagnostics(artifact_dir / DEFAULT_A_RESPONSE_FILENAME)
                    rows.append(
                        QuestionRunDiagnostics(
                            question_id=source.question_id,
                            question_text=question_text,
                            embedded_question_text=embedded_question_text,
                            family_id=source.family_id,
                            run_label=run_label,
                            artifact_dir=artifact_dir,
                            recommendation=_extract_recommendation(payload),
                            approaches=tuple(approaches),
                            labels=labels,
                            missing_expected_labels=tuple(sorted(expected_labels - set(labels))),
                            spurious_labels=tuple(sorted(set(labels) - expected_labels)) if expected_labels else tuple(),
                            prompt_chunks=prompt_chunks,
                            authoritative_references=authoritative_references,
                            secondary_references=secondary_references,
                            peripheral_references=peripheral_references,
                            dropped_documents=dropped_documents,
                        )
                    )
        if not rows:
            raise FileNotFoundError(
                f"No {DEFAULT_B_RESPONSE_FILENAME} or {DEFAULT_A_RESPONSE_FILENAME} artifacts found in {artifacts_dir}"
            )
        return sorted(rows, key=lambda item: (_question_sort_key(item.question_id), _run_label_sort_key(item.run_label))), raw_payloads_by_question

    def _find_question_artifact_dirs(self, *, artifacts_dir: Path, family_dirname: str, question_id: str) -> list[Path]:
        direct = artifacts_dir / family_dirname / question_id
        if direct.exists():
            return [direct]
        return sorted(
            [path for path in artifacts_dir.rglob(question_id) if path.is_dir() and path.name == question_id],
            key=lambda path: str(path),
        )

    def _iter_answer_artifact_dirs(self, question_dir: Path) -> list[tuple[Path, str]]:
        artifact_dirs: list[tuple[Path, str]] = []
        response_paths = sorted(
            {
                *question_dir.rglob(DEFAULT_B_RESPONSE_FILENAME),
                *question_dir.rglob(DEFAULT_A_RESPONSE_FILENAME),
            },
            key=lambda path: str(path),
        )
        seen_dirs: set[Path] = set()
        for response_path in response_paths:
            artifact_dir = response_path.parent
            if artifact_dir in seen_dirs:
                continue
            seen_dirs.add(artifact_dir)
            repeat_parent = next((parent for parent in [artifact_dir, *artifact_dir.parents] if parent.parent != parent and parent.name.startswith("repeat-")), None)
            run_label = repeat_parent.name if repeat_parent is not None and question_dir in repeat_parent.parents else "base"
            artifact_dirs.append((artifact_dir, run_label))
        return artifact_dirs

    def _load_preferred_response_payload(self, artifact_dir: Path) -> dict[str, object]:
        b_response_path = artifact_dir / DEFAULT_B_RESPONSE_FILENAME
        if b_response_path.exists():
            return _load_json_object(b_response_path)
        a_response_path = artifact_dir / DEFAULT_A_RESPONSE_FILENAME
        if a_response_path.exists():
            return _load_json_object(a_response_path)
        raise FileNotFoundError(
            f"Missing both {DEFAULT_B_RESPONSE_FILENAME} and {DEFAULT_A_RESPONSE_FILENAME} in {artifact_dir}"
        )

    def _load_prompt_chunks(self, a_prompt_path: Path, expected_ranges: tuple[ExpectedSectionRange, ...]) -> tuple[PromptChunk, ...]:
        if not a_prompt_path.exists():
            return tuple()
        prompt_text = a_prompt_path.read_text(encoding="utf-8")
        chunks: list[PromptChunk] = []
        for match in self._chunk_tag_pattern.finditer(prompt_text):
            attributes = {item.group(1): item.group(2) for item in self._attribute_pattern.finditer(match.group(1))}
            doc_uid = attributes.get("doc_uid")
            chunk_number = attributes.get("chunk_number") or attributes.get("section_path") or attributes.get("paragraph")
            score_text = attributes.get("score")
            if doc_uid is None or chunk_number is None or score_text is None:
                continue
            try:
                score = float(score_text)
            except ValueError:
                continue
            chunks.append(
                PromptChunk(
                    doc_uid=doc_uid,
                    chunk_number=chunk_number,
                    score=score,
                    chunk_id=attributes.get("id"),
                    expected=_is_expected_chunk(doc_uid, chunk_number, expected_ranges),
                )
            )
        return tuple(chunks)

    def _build_label_summaries(self, rows: list[QuestionRunDiagnostics], expected_labels: set[str]) -> tuple[LabelSummary, ...]:
        run_count = len(rows)
        labels = sorted(set(expected_labels) | {label for row in rows for label in row.labels})
        summaries: list[LabelSummary] = []
        for label in labels:
            present_rows = [row for row in rows if label in row.labels]
            summaries.append(
                LabelSummary(
                    label=label,
                    expected=label in expected_labels,
                    present_count=len(present_rows),
                    run_count=run_count,
                    question_count=len({row.question_id for row in present_rows}),
                )
            )
        return tuple(summaries)

    def _build_question_stability(
        self,
        raw_payloads: dict[str, list[dict[str, object]]],
        expected_labels: set[str],
    ) -> tuple[QuestionStabilitySummary, ...]:
        summaries: list[QuestionStabilitySummary] = []
        for question_id in sorted(raw_payloads, key=_question_sort_key):
            payloads = raw_payloads[question_id]
            result = compute_stability_score(payloads, expected_normalized_labels=expected_labels)
            diagnostics = result.diagnostics
            summaries.append(
                QuestionStabilitySummary(
                    question_id=question_id,
                    run_count=diagnostics.run_count,
                    stability_score=result.stability_score,
                    stability_score_loose=result.stability_score_loose,
                    approach_set_stability=result.approach_set_stability,
                    applicability_stability=result.applicability_stability,
                    recommendation_stability=result.recommendation_stability,
                    missing_expected_count=diagnostics.missing_expected_alternatives_count,
                    spurious_count=diagnostics.weird_alternatives_count,
                )
            )
        return tuple(summaries)

    def _write_raw_payloads(self, diagnostics: RunDiagnostics, raw_dir: Path) -> None:
        if raw_dir.exists():
            shutil.rmtree(raw_dir)
        raw_dir.mkdir(parents=True, exist_ok=True)
        for row in diagnostics.rows:
            artifact_dir = row.artifact_dir
            source_path = artifact_dir / DEFAULT_B_RESPONSE_FILENAME
            if source_path.exists():
                destination = raw_dir / f"{row.question_id}__{row.run_label}.B-response.json"
                shutil.copyfile(source_path, destination)

    def _label_columns(self, diagnostics: RunDiagnostics) -> list[str]:
        expected_labels = list(diagnostics.expected_labels)
        emitted_labels = {label for row in diagnostics.rows for label in row.labels}
        spurious_labels = sorted(emitted_labels - set(expected_labels))
        return [*expected_labels, *spurious_labels]

    def _section_columns(
        self,
        rows: tuple[QuestionRunDiagnostics, ...],
        expected_section_ranges: tuple[ExpectedSectionRange, ...],
    ) -> tuple[SectionColumn, ...]:
        chunk_lookup = _load_chunk_lookup(_collect_chunk_db_ids(rows))
        chunk_lookup_by_reference = _load_chunk_lookup_by_reference(_collect_chunk_references(rows))
        expected_display_records = _load_expected_section_display_records(expected_section_ranges)
        section_lookup = _load_section_lookup(
            _collect_section_ids(chunk_lookup)
            | _collect_section_ids(chunk_lookup_by_reference))
        observed_section_ids_by_doc: dict[str, set[str]] = {}
        retrieved_doc_counts: dict[str, int] = {}
        doc_display_names: dict[str, str] = {}
        for row in rows:
            for chunk in row.prompt_chunks:
                canonical_doc_key = _canonical_doc_key(chunk.doc_uid)
                if chunk.score > 0.0:
                    retrieved_doc_counts[canonical_doc_key] = retrieved_doc_counts.get(canonical_doc_key, 0) + 1
                doc_display_names.setdefault(canonical_doc_key, _display_doc_uid(chunk.doc_uid))
                section_id = self._section_id_for_chunk(chunk, chunk_lookup, chunk_lookup_by_reference)
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
            display_records.sort(key=lambda record: _lexicographic_chunk_key(_display_section_header(record.section_id)))
            columns.extend(
                SectionColumn(
                    column_key=_section_column_key(canonical_doc_key, record.section_id),
                    canonical_doc_key=canonical_doc_key,
                    doc_display_name=doc_display_names[canonical_doc_key],
                    section_id=record.section_id,
                    title=record.title,
                    section_lineage=record.section_lineage,
                    position=record.position,
                )
                for record in display_records
            )
        return tuple(columns)

    def _section_id_for_chunk(
        self,
        chunk: PromptChunk,
        chunk_lookup: dict[int, ChunkLookupRecord],
        chunk_lookup_by_reference: dict[tuple[str, str], ChunkLookupRecord],
    ) -> str:
        chunk_record = self._chunk_record_for_chunk(chunk, chunk_lookup, chunk_lookup_by_reference)
        if chunk_record is not None and chunk_record.containing_section_id is not None:
            return chunk_record.containing_section_id
        return f"{_canonical_doc_key(chunk.doc_uid)}_{chunk.chunk_number}"

    def _chunk_record_for_chunk(
        self,
        chunk: PromptChunk,
        chunk_lookup: dict[int, ChunkLookupRecord],
        chunk_lookup_by_reference: dict[tuple[str, str], ChunkLookupRecord],
    ) -> ChunkLookupRecord | None:
        chunk_db_id = chunk.chunk_db_id
        if chunk_db_id is not None:
            chunk_record = chunk_lookup.get(chunk_db_id)
            if chunk_record is not None:
                return chunk_record
        return chunk_lookup_by_reference.get((_canonical_doc_key(chunk.doc_uid), chunk.chunk_number))

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

    def _render_group_header(self, label_columns: list[str], section_columns: tuple[SectionColumn, ...]) -> str:
        doc_order = _doc_order_from_columns(section_columns)
        counts = dict.fromkeys(doc_order, 0)
        display_names = {column.canonical_doc_key: column.doc_display_name for column in section_columns}
        for section_column in section_columns:
            counts[section_column.canonical_doc_key] += 1
        section_group_headers = "".join(
            f'<th class="group-header section-group" id="group-header-{doc_key}" data-doc-key="{doc_key}" colspan="{counts[doc_key]}">{html.escape(display_names[doc_key])}</th>'
            for doc_key in doc_order
        )
        return (
            '<th class="group-header sticky-group" colspan="3">Run metadata</th>'
            f'<th class="group-header" colspan="{len(label_columns)}">Emitted labels</th>'
            f"{section_group_headers}"
        )

    def _render_column_header(
        self,
        label_columns: list[str],
        section_columns: tuple[SectionColumn, ...],
        expected_section_ranges: tuple[ExpectedSectionRange, ...],
    ) -> str:
        metadata_headers = (
            '<th class="sticky-1 metadata-col">Q</th>',
            '<th class="sticky-2 metadata-col">run</th>',
            '<th class="sticky-3 metadata-col">rec</th>',
        )
        label_headers = tuple(f'<th class="label-col" data-label="{html.escape(label)}">{html.escape(label)}</th>' for label in label_columns)
        section_headers = tuple(self._render_section_header(section_column, expected_section_ranges) for section_column in section_columns)
        return "".join((*metadata_headers, *label_headers, *section_headers))

    def _render_section_header(self, section_column: SectionColumn, expected_section_ranges: tuple[ExpectedSectionRange, ...]) -> str:
        lineage_text = " > ".join(section_column.section_lineage)
        tooltip = (
            f"{section_column.doc_display_name}\n"
            f"section_id: {section_column.section_id}\n"
            f"title: {section_column.title}\n"
            f"lineage: {lineage_text}\n"
            f"position: {section_column.position}"
        )
        target_prefix = "🎯 " if _section_column_is_expected(section_column, expected_section_ranges) else ""
        return (
            f'<th class="section-col {section_column.canonical_doc_key}" '
            f'data-section-key="{html.escape(section_column.column_key)}" '
            f'data-doc-key="{html.escape(section_column.canonical_doc_key)}" '
            f'title="{html.escape(tooltip)}">{target_prefix}{html.escape(_display_section_header(section_column.section_id))}</th>'
        )

    def _render_controls(self, section_columns: tuple[SectionColumn, ...]) -> str:
        display_names = {column.canonical_doc_key: column.doc_display_name for column in section_columns}
        doc_toggles = "\n      ".join(
            f'<label><input type="checkbox" class="doc-toggle" data-doc-key="{doc_key}" checked> {html.escape(display_names[doc_key])}</label>'
            for doc_key in _doc_order_from_columns(section_columns)
        )
        return f"""
    <section class="controls">
      <button type="button" data-sort-mode="question">Question order</button>
      <button type="button" data-sort-mode="spurious">Spurious-first</button>
      <label><input type="checkbox" id="spurious-only"> Show only runs with spurious labels</label>
      <label><input type="checkbox" id="show-visible-context"> Show visible-context sections</label>
      <label><input type="checkbox" id="hide-empty-columns" checked> Hide empty section columns</label>
      {doc_toggles}
    </section>
"""

    def _render_spurious_filter_controls(self, label_columns: list[str], expected_labels: set[str]) -> str:
        spurious_labels = [label for label in label_columns if label not in expected_labels]
        if not spurious_labels:
            return ""
        checkboxes_html = "".join(
            (
                f'<label class="spurious-filter-option">'
                f'<input type="checkbox" class="spurious-label-filter" '
                f'data-spurious-label="{html.escape(label)}"> '
                f'{html.escape(label)}</label>'
            )
            for label in spurious_labels
        )
        return f"""
    <section class="spurious-filter-panel">
      <strong>Spurious approach filter</strong>
      <div class="spurious-filter-actions">
        <button type="button" id="select-all-spurious">Select all</button>
        <button type="button" id="clear-all-spurious">Clear all</button>
      </div>
      <div class="spurious-filter-options">
        {checkboxes_html}
      </div>
    </section>
"""

    def _render_html_row(
        self,
        index: int,
        row: QuestionRunDiagnostics,
        label_columns: list[str],
        section_columns: tuple[SectionColumn, ...],
    ) -> str:
        row_labels = set(row.labels)
        label_cells = tuple(self._render_label_cell(label, label in row_labels, label in row.spurious_labels) for label in label_columns)
        section_cells_by_key = self._section_cells(row)
        section_cells = tuple(self._render_section_cell(section_column, section_cells_by_key.get(section_column.column_key)) for section_column in section_columns)
        order_spurious = self._spurious_order_value(row, index)
        spurious_labels_attr = "|".join(row.spurious_labels)
        question_tooltip = (
            f"question_id: {row.question_id}\n\n"
            f"question:\n{row.question_text}\n\n"
            f"embedded question:\n{row.embedded_question_text}"
        )
        return (
            f'<tr data-order-question="{index}" '
            f'data-order-spurious="{order_spurious}" '
            f'data-has-spurious="{"1" if row.spurious_labels else "0"}" '
            f'data-spurious-labels="{html.escape(spurious_labels_attr)}" '
            f'data-question-id="{html.escape(row.question_id)}">'
            f'<td class="sticky-1 metadata-col metadata-q" title="{html.escape(question_tooltip)}">{html.escape(row.question_id)}</td>'
            f'<td class="sticky-2 metadata-col metadata-run">{html.escape(_display_run_id(row.run_label))}</td>'
            f'<td class="sticky-3 metadata-col metadata-rec">{html.escape(_display_recommendation(row.recommendation or ""))}</td>'
            f'{"".join((*label_cells, *section_cells))}'
            '</tr>'
        )

    def _render_label_cell(self, label: str, is_present: bool, is_spurious: bool) -> str:
        kind_class = "spurious" if is_spurious else "core"
        presence_class = "present" if is_present else "absent"
        symbol = "✅" if is_present and not is_spurious else ("✓" if is_present else "")
        return f'<td class="label-cell {kind_class} {presence_class}" data-label="{html.escape(label)}">{symbol}</td>'

    def _section_cells(self, row: QuestionRunDiagnostics) -> dict[str, SectionCell]:
        chunk_lookup = _load_chunk_lookup(_collect_chunk_db_ids((row,)))
        chunk_lookup_by_reference = _load_chunk_lookup_by_reference(_collect_chunk_references((row,)))
        entries_by_section: dict[str, list[PromptChunk]] = {}
        for chunk in row.prompt_chunks:
            canonical_doc_key = _canonical_doc_key(chunk.doc_uid)
            section_id = self._section_id_for_chunk(chunk, chunk_lookup, chunk_lookup_by_reference)
            display_chunk = self._chunk_with_corpus_chunk_number(chunk, chunk_lookup, chunk_lookup_by_reference)
            entries_by_section.setdefault(_section_column_key(canonical_doc_key, section_id), []).append(display_chunk)
        return {
            column_key: _build_section_cell(chunks, row=row)
            for column_key, chunks in entries_by_section.items()
        }

    def _chunk_with_corpus_chunk_number(
        self,
        chunk: PromptChunk,
        chunk_lookup: dict[int, ChunkLookupRecord],
        chunk_lookup_by_reference: dict[tuple[str, str], ChunkLookupRecord],
    ) -> PromptChunk:
        chunk_record = self._chunk_record_for_chunk(chunk, chunk_lookup, chunk_lookup_by_reference)
        if chunk_record is None:
            return chunk
        return replace(chunk, chunk_number=chunk_record.chunk_number)

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

    def _spurious_order_value(self, row: QuestionRunDiagnostics, fallback_index: int) -> str:
        spurious_prefix = "0" if row.spurious_labels else "1"
        spurious_text = "|".join(row.spurious_labels)
        return f"{spurious_prefix}:{spurious_text}:{row.question_id}:{row.run_label}:{fallback_index:04d}"

    def _render_legend(self, diagnostics: RunDiagnostics, section_columns: tuple[SectionColumn, ...]) -> str:
        return ""

    def _render_style(self) -> str:
        return """
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 0; color: #1f2937; background: #f8fafc; }
  main { padding: 1rem; }
  h1 { margin-top: 0; }
  .controls { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 1rem; align-items: center; }
  .legend, .spurious-filter-panel { margin-bottom: 1rem; padding: 0.75rem 1rem; background: #ffffff; border: 1px solid #d1d5db; border-radius: 8px; }
  .spurious-filter-actions { display: flex; gap: 0.5rem; margin: 0.5rem 0; }
  .spurious-filter-options { display: flex; flex-wrap: wrap; gap: 0.5rem 1rem; }
  .spurious-filter-option { display: inline-flex; align-items: center; gap: 0.25rem; }
  .table-wrap { overflow: auto; border: 1px solid #d1d5db; background: #ffffff; }
  table { border-collapse: collapse; font-size: 12px; width: max-content; min-width: 100%; }
  th, td { border: 1px solid #d1d5db; padding: 0.35rem 0.5rem; text-align: center; white-space: nowrap; }
  thead th { position: sticky; top: 0; z-index: 3; background: #f3f4f6; }
  .group-header { background: #e5e7eb; font-weight: 700; }
  .metadata-col { text-align: left; background: #ffffff; }
  .metadata-q, .metadata-run, .metadata-rec { text-align: center; }
  .sticky-1, .sticky-2, .sticky-3 { position: sticky; z-index: 2; background: #ffffff; }
  .sticky-1 { left: 0; min-width: 56px; }
  .sticky-2 { left: 56px; min-width: 34px; }
  .sticky-3 { left: 90px; min-width: 54px; }
  thead .sticky-1, thead .sticky-2, thead .sticky-3 { z-index: 4; background: #f3f4f6; }
  .label-cell.present.core { color: #111827; font-weight: 700; }
  .label-cell.present.spurious { background: #b91c1c; color: #ffffff; font-weight: 700; }
  .label-cell.absent { color: #d1d5db; }
  .label-cell.core.absent { background: #ffffff; }
  .section-cell { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; line-height: 1.3; }
  .section-cell-score { display: block; font-weight: 600; }
  .section-cell-authority { display: block; font-size: 11px; color: #374151; }
  button { cursor: pointer; }
</style>
"""

    def _render_script(self, section_columns: tuple[SectionColumn, ...]) -> str:
        section_keys = [column.column_key for column in section_columns]
        return f"""
<script>
  const tableBody = document.querySelector('#matrix-table tbody');
  const sortButtons = document.querySelectorAll('button[data-sort-mode]');
  const spuriousOnlyCheckbox = document.getElementById('spurious-only');
  const showVisibleContextCheckbox = document.getElementById('show-visible-context');
  const hideEmptyCheckbox = document.getElementById('hide-empty-columns');
  const docToggles = document.querySelectorAll('.doc-toggle');
  const spuriousLabelFilters = document.querySelectorAll('.spurious-label-filter');
  const selectAllSpuriousButton = document.getElementById('select-all-spurious');
  const clearAllSpuriousButton = document.getElementById('clear-all-spurious');
  const sectionKeys = {json.dumps(section_keys)};
  let currentSortMode = 'question';

  function visibleRows() {{
    return Array.from(tableBody.querySelectorAll('tr')).filter((row) => row.style.display !== 'none');
  }}
  function sortRows(mode) {{
    currentSortMode = mode;
    const rows = Array.from(tableBody.querySelectorAll('tr'));
    rows.sort((left, right) => {{
      const leftValue = left.dataset[mode === 'question' ? 'orderQuestion' : 'orderSpurious'];
      const rightValue = right.dataset[mode === 'question' ? 'orderQuestion' : 'orderSpurious'];
      if (mode === 'question') {{ return Number(leftValue) - Number(rightValue); }}
      return leftValue.localeCompare(rightValue);
    }});
    rows.forEach((row) => tableBody.appendChild(row));
  }}
  function selectedSpuriousLabels() {{
    return new Set(Array.from(spuriousLabelFilters).filter((checkbox) => checkbox.checked).map((checkbox) => checkbox.dataset.spuriousLabel));
  }}
  function applyRowVisibility() {{
    const spuriousOnly = spuriousOnlyCheckbox.checked;
    const selectedLabels = selectedSpuriousLabels();
    Array.from(tableBody.querySelectorAll('tr')).forEach((row) => {{
      const hasSpurious = row.dataset.hasSpurious === '1';
      const rowSpuriousLabels = row.dataset.spuriousLabels ? row.dataset.spuriousLabels.split('|').filter((value) => value.length > 0) : [];
      const matchesSelectedLabels = selectedLabels.size === 0 || rowSpuriousLabels.some((label) => selectedLabels.has(label));
      row.style.display = (!spuriousOnly || hasSpurious) && matchesSelectedLabels ? '' : 'none';
    }});
  }}
  function isVisibleContextMode() {{ return showVisibleContextCheckbox.checked; }}
  function updateSectionCellPresentation() {{
    const useVisibleContext = isVisibleContextMode();
    document.querySelectorAll('td.section-cell').forEach((cell) => {{
      cell.innerHTML = (useVisibleContext ? cell.dataset.visibleText : cell.dataset.retrievedText) || '';
      cell.style.backgroundColor = (useVisibleContext ? cell.dataset.visibleBg : cell.dataset.retrievedBg) || 'transparent';
    }});
  }}
  function updateSectionVisibility() {{
    const enabledDocs = new Set(Array.from(docToggles).filter((checkbox) => checkbox.checked).map((checkbox) => checkbox.dataset.docKey));
    const rows = visibleRows();
    const hideEmpty = hideEmptyCheckbox.checked;
    const docKeys = {json.dumps(_doc_order_from_columns(section_columns))};
    const visibleCounts = Object.fromEntries(docKeys.map((docKey) => [docKey, 0]));
    sectionKeys.forEach((sectionKey) => {{
      const header = document.querySelector(`th[data-section-key="${{sectionKey}}"]`);
      if (!header) {{ return; }}
      const docKey = header.dataset.docKey;
      let visible = enabledDocs.has(docKey);
      if (visible && hideEmpty) {{
        visible = rows.some((row) => {{
          const cell = row.querySelector(`td[data-section-key="${{sectionKey}}"]`);
          if (!cell) {{ return false; }}
          return isVisibleContextMode() ? cell.dataset.hasVisible === '1' : cell.dataset.hasRetrieved === '1';
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
    updateSectionCellPresentation();
    updateSectionVisibility();
  }}
  sortButtons.forEach((button) => button.addEventListener('click', () => {{ sortRows(button.dataset.sortMode); updateSectionVisibility(); }}));
  spuriousOnlyCheckbox.addEventListener('change', applyAll);
  showVisibleContextCheckbox.addEventListener('change', applyAll);
  hideEmptyCheckbox.addEventListener('change', updateSectionVisibility);
  docToggles.forEach((checkbox) => checkbox.addEventListener('change', updateSectionVisibility));
  spuriousLabelFilters.forEach((checkbox) => checkbox.addEventListener('change', applyAll));
  if (selectAllSpuriousButton) {{ selectAllSpuriousButton.addEventListener('click', () => {{ spuriousLabelFilters.forEach((checkbox) => {{ checkbox.checked = true; }}); applyAll(); }}); }}
  if (clearAllSpuriousButton) {{ clearAllSpuriousButton.addEventListener('click', () => {{ spuriousLabelFilters.forEach((checkbox) => {{ checkbox.checked = false; }}); applyAll(); }}); }}
  applyAll();
</script>
"""


def _collect_chunk_db_ids(rows: tuple[QuestionRunDiagnostics, ...]) -> set[int]:
    chunk_ids: set[int] = set()
    for row in rows:
        for chunk in row.prompt_chunks:
            chunk_db_id = chunk.chunk_db_id
            if chunk_db_id is not None:
                chunk_ids.add(chunk_db_id)
    return chunk_ids


def _collect_chunk_references(rows: tuple[QuestionRunDiagnostics, ...]) -> set[tuple[str, str]]:
    references: set[tuple[str, str]] = set()
    for row in rows:
        for chunk in row.prompt_chunks:
            canonical_doc_key = _canonical_doc_key(chunk.doc_uid)
            references.add((canonical_doc_key, chunk.chunk_number))
    return references


def _load_chunk_lookup(chunk_db_ids: set[int]) -> dict[int, ChunkLookupRecord]:
    if not chunk_db_ids:
        return {}
    try:
        db_path = _default_db_path()
    except (AttributeError, ModuleNotFoundError):
        logger.warning("Could not resolve corpus database path for approach detection section lookup")
        return {}
    if not db_path.exists():
        logger.warning(f"Corpus database not found for approach detection section lookup: {db_path}")
        return {}
    records: dict[int, ChunkLookupRecord] = {}
    with sqlite3.connect(f"file:{db_path}?mode=ro", uri=True) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT id, doc_uid, chunk_number, containing_section_id
            FROM chunks
            WHERE id IN (SELECT value FROM json_each(?))
            """,
            (json.dumps(sorted(chunk_db_ids)),),
        ).fetchall()
        for row in rows:
            records[int(row["id"])] = ChunkLookupRecord(
                chunk_db_id=int(row["id"]),
                doc_uid=str(row["doc_uid"]),
                chunk_number=str(row["chunk_number"]),
                containing_section_id=str(row["containing_section_id"]) if row["containing_section_id"] is not None else None,
            )
    return records


def _load_chunk_lookup_by_reference(references: set[tuple[str, str]]) -> dict[tuple[str, str], ChunkLookupRecord]:
    if not references:
        return {}
    try:
        db_path = _default_db_path()
    except (AttributeError, ModuleNotFoundError):
        logger.warning("Could not resolve corpus database path for approach detection chunk reference lookup")
        return {}
    if not db_path.exists():
        logger.warning(f"Corpus database not found for approach detection chunk reference lookup: {db_path}")
        return {}

    doc_keys = sorted({doc_key for doc_key, _chunk_number in references})
    chunk_numbers = sorted({chunk_number for _doc_key, chunk_number in references})
    records: dict[tuple[str, str], ChunkLookupRecord] = {}
    with sqlite3.connect(f"file:{db_path}?mode=ro", uri=True) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT id, doc_uid, chunk_number, containing_section_id
            FROM chunks
            WHERE doc_uid IN (SELECT value FROM json_each(?))
              AND chunk_number IN (SELECT value FROM json_each(?))
            """,
            (json.dumps(doc_keys), json.dumps(chunk_numbers)),
        ).fetchall()
        for row in rows:
            doc_key = _canonical_doc_key(str(row["doc_uid"]))
            chunk_number = str(row["chunk_number"])
            key = (doc_key, chunk_number)
            if key not in references:
                continue
            records[key] = ChunkLookupRecord(
                chunk_db_id=int(row["id"]),
                doc_uid=str(row["doc_uid"]),
                chunk_number=chunk_number,
                containing_section_id=str(row["containing_section_id"]) if row["containing_section_id"] is not None else None,
            )
    return records


def _collect_section_ids(chunk_lookup: dict[int, ChunkLookupRecord]) -> set[str]:
    return {record.containing_section_id for record in chunk_lookup.values() if record.containing_section_id is not None}


def _load_expected_section_display_records(
    expected_section_ranges: tuple[ExpectedSectionRange, ...],
) -> dict[str, tuple[SectionDisplayRecord, ...]]:
    if not expected_section_ranges:
        return {}
    db_path = _default_db_path()
    if not db_path.exists():
        return {}

    doc_keys = sorted({_canonical_doc_key(expected_range.document) for expected_range in expected_section_ranges})
    ranges_by_doc: dict[str, list[ExpectedSectionRange]] = {}
    for expected_range in expected_section_ranges:
        ranges_by_doc.setdefault(_canonical_doc_key(expected_range.document), []).append(expected_range)

    records_by_doc: dict[str, list[SectionDisplayRecord]] = {}
    with sqlite3.connect(f"file:{db_path}?mode=ro", uri=True) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT doc_uid, section_id, title, section_lineage, position
            FROM sections
            WHERE doc_uid IN (SELECT value FROM json_each(?))
            """,
            (json.dumps(doc_keys),),
        ).fetchall()
        for row in rows:
            doc_uid = str(row["doc_uid"])
            doc_key = _canonical_doc_key(doc_uid)
            section_id = str(row["section_id"])
            if not any(_section_id_overlaps_expected_range(section_id, expected_range) for expected_range in ranges_by_doc.get(doc_key, [])):
                continue
            records_by_doc.setdefault(doc_key, []).append(
                SectionDisplayRecord(
                    doc_uid=doc_uid,
                    section_id=section_id,
                    title=str(row["title"]),
                    section_lineage=tuple(_decode_lineage(str(row["section_lineage"]))),
                    position=int(row["position"]),
                )
            )
    return {doc_key: tuple(records) for doc_key, records in records_by_doc.items()}


def _load_section_lookup(section_ids: set[str]) -> dict[str, SectionDisplayRecord]:
    if not section_ids:
        return {}
    db_path = _default_db_path()
    if not db_path.exists():
        return {}
    records: dict[str, SectionDisplayRecord] = {}
    with sqlite3.connect(f"file:{db_path}?mode=ro", uri=True) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT doc_uid, section_id, title, section_lineage, position
            FROM sections
            WHERE section_id IN (SELECT value FROM json_each(?))
            """,
            (json.dumps(sorted(section_ids)),),
        ).fetchall()
        for row in rows:
            records[str(row["section_id"])] = SectionDisplayRecord(
                doc_uid=str(row["doc_uid"]),
                section_id=str(row["section_id"]),
                title=str(row["title"]),
                section_lineage=tuple(_decode_lineage(str(row["section_lineage"]))),
                position=int(row["position"]),
            )
    return records


def _decode_lineage(raw_lineage: str) -> list[str]:
    decoded = json.loads(raw_lineage)
    if not isinstance(decoded, list) or not all(isinstance(item, str) for item in decoded):
        raise ValueError(f"Invalid section_lineage payload: {raw_lineage}")
    return decoded


def _build_section_cell(chunks: list[PromptChunk], *, row: QuestionRunDiagnostics) -> SectionCell:
    sorted_chunks = sorted(chunks, key=lambda chunk: (_section_sort_key(chunk.chunk_number), chunk.score))
    visible_scores = tuple(chunk.score for chunk in sorted_chunks)
    visible_chunk_numbers = tuple(chunk.chunk_number for chunk in sorted_chunks)
    retrieved_chunks = [chunk for chunk in sorted_chunks if chunk.score > 0.0]
    retrieved_scores = tuple(chunk.score for chunk in retrieved_chunks)
    retrieved_chunk_numbers = tuple(chunk.chunk_number for chunk in retrieved_chunks)
    visible_chunk_records = tuple(_chunk_authority_record(chunk, row=row) for chunk in sorted_chunks if not _chunk_is_dropped(chunk, row=row))
    retrieved_chunk_records = tuple(_chunk_authority_record(chunk, row=row) for chunk in retrieved_chunks if not _chunk_is_dropped(chunk, row=row))
    dropped_chunk_records = tuple(_chunk_authority_record(chunk, row=row) for chunk in sorted_chunks if _chunk_is_dropped(chunk, row=row))
    return SectionCell(
        retrieved_scores=retrieved_scores,
        retrieved_display_text=_format_score_range(retrieved_scores),
        retrieved_max_score=max(retrieved_scores) if retrieved_scores else None,
        retrieved_chunk_numbers=retrieved_chunk_numbers,
        visible_scores=visible_scores,
        visible_display_text=_format_score_range(visible_scores),
        visible_max_score=max(visible_scores) if visible_scores else None,
        visible_chunk_numbers=visible_chunk_numbers,
        retrieved_chunks=retrieved_chunk_records,
        visible_chunks=visible_chunk_records,
        dropped_chunks=dropped_chunk_records,
    )


def _chunk_authority_record(chunk: PromptChunk, *, row: QuestionRunDiagnostics) -> ChunkAuthorityRecord:
    canonical_doc_key = _canonical_doc_key(chunk.doc_uid)
    reference_key = (canonical_doc_key, chunk.chunk_number)
    if canonical_doc_key in set(row.dropped_documents):
        authority_category = "dropped"
        dropped = True
    elif reference_key in set(row.authoritative_references):
        authority_category = "authoritative"
        dropped = False
    elif reference_key in set(row.secondary_references):
        authority_category = "secondary"
        dropped = False
    elif reference_key in set(row.peripheral_references):
        authority_category = "peripheral"
        dropped = False
    else:
        authority_category = "dropped"
        dropped = True
    return ChunkAuthorityRecord(
        chunk_number=chunk.chunk_number,
        score=chunk.score,
        authority_category=authority_category,
        dropped=dropped,
    )


def _chunk_is_dropped(chunk: PromptChunk, *, row: QuestionRunDiagnostics) -> bool:
    return _canonical_doc_key(chunk.doc_uid) in set(row.dropped_documents)


def _chunk_authority_lines(chunks: tuple[ChunkAuthorityRecord, ...]) -> str:
    lines = [
        f"- {chunk.chunk_number} ({chunk.score:.2f}) [{chunk.authority_category}]"
        for chunk in chunks
    ]
    return "\n".join(lines) if lines else "(none)"


def _format_score_range(scores: tuple[float, ...]) -> str:
    if not scores:
        return ""
    min_score = min(scores)
    max_score = max(scores)
    if min_score == max_score:
        return f"{min_score:.2f}"
    return f"{min_score:.2f}-{max_score:.2f}"


def _section_range_category(section_cell: SectionCell) -> str:
    return _range_category_from_chunks(section_cell.visible_chunks, section_cell.dropped_chunks)


def _range_category_emoji(category: str) -> str:
    if category == "authoritative":
        return "🎯"
    if category == "secondary":
        return "🔎"
    if category == "peripheral":
        return "🖼️"
    return "🗑️"


def _range_category_from_chunks(
    categorized_chunks: tuple[ChunkAuthorityRecord, ...],
    dropped_chunks: tuple[ChunkAuthorityRecord, ...],
) -> str:
    categories = {chunk.authority_category for chunk in (*categorized_chunks, *dropped_chunks)}
    if "authoritative" in categories:
        return "authoritative"
    if "secondary" in categories:
        return "secondary"
    if "peripheral" in categories:
        return "peripheral"
    return "dropped"


def _format_section_cell_summary(
    score_text: str,
    categorized_chunks: tuple[ChunkAuthorityRecord, ...],
    *,
    include_dropped: bool,
    dropped_chunks: tuple[ChunkAuthorityRecord, ...] = (),
) -> str:
    del include_dropped
    range_category = _range_category_from_chunks(categorized_chunks, dropped_chunks)
    score_line = html.escape(score_text or "—")
    emoji_line = html.escape(_range_category_emoji(range_category))
    return f'<span class="section-cell-score">{score_line}</span><span class="section-cell-authority">{emoji_line}</span>'


def _markdown_dropped_chunk_lines(
    section_columns: tuple[SectionColumn, ...],
    section_cells_by_key: dict[str, SectionCell],
) -> list[str]:
    lines: list[str] = []
    for section_column in section_columns:
        section_cell = section_cells_by_key.get(section_column.column_key)
        if section_cell is None or not section_cell.dropped_chunks:
            continue
        for chunk in section_cell.dropped_chunks:
            lines.append(
                f"- {section_column.doc_display_name} / {_display_section_header(section_column.section_id)} / {chunk.chunk_number} / {chunk.authority_category}"
            )
    return lines


def _section_background_color(canonical_doc_key: str, max_score: float | None) -> str:
    hue = _document_hue(canonical_doc_key)
    if max_score is None:
        return "transparent"
    if max_score <= 0.0:
        return f"hsl({hue} 35% 97.5%)"
    clamped_score = min(max(max_score, 0.40), 0.70)
    normalized_score = (clamped_score - 0.40) / 0.30
    lightness = 96.0 - (normalized_score * 34.0)
    return f"hsl({hue} 70% {lightness:.1f}%)"


def _document_hue(canonical_doc_key: str) -> int:
    accumulator = 0
    for character in canonical_doc_key:
        accumulator = ((accumulator * 131) + ord(character)) % 360
    return (accumulator * 137) % 360


def _section_column_key(canonical_doc_key: str, section_id: str) -> str:
    return f"{canonical_doc_key}::{section_id}"


def _canonical_doc_key(doc_uid: str) -> str:
    return re.sub(r"[^a-z0-9]", "", doc_uid.lower())


def _display_doc_uid(doc_uid: str) -> str:
    without_separators = doc_uid.upper().replace("-", " ")
    return re.sub(r"([A-Z]+)(\d)", r"\1 \2", without_separators)


def _doc_order_from_columns(section_columns: tuple[SectionColumn, ...]) -> list[str]:
    ordered_doc_keys: list[str] = []
    for section_column in section_columns:
        if section_column.canonical_doc_key not in ordered_doc_keys:
            ordered_doc_keys.append(section_column.canonical_doc_key)
    return ordered_doc_keys


def _display_run_id(run_id: str) -> str:
    if run_id == "base":
        return "0"
    if run_id.startswith("repeat-"):
        suffix = run_id.removeprefix("repeat-")
        if suffix.isdigit():
            return suffix
    return run_id


def _display_recommendation(recommendation: str) -> str:
    if recommendation == "oui_sous_conditions":
        return "oui_sc"
    if recommendation == "yes_under_conditions":
        return "yes_uc"
    return recommendation


def _display_section_header(section_id: str) -> str:
    underscore_index = section_id.find("_")
    if underscore_index == -1:
        return section_id
    return section_id[underscore_index + 1 :]


def _lexicographic_chunk_key(value: str) -> tuple[str, ...]:
    return tuple(part.lower() for part in re.split(r"(\d+)", value))


def _section_column_is_expected(section_column: SectionColumn, expected_section_ranges: tuple[ExpectedSectionRange, ...]) -> bool:
    for expected_range in expected_section_ranges:
        if _canonical_doc_key(expected_range.document) != section_column.canonical_doc_key:
            continue
        if _section_id_overlaps_expected_range(section_column.section_id, expected_range):
            return True
    return False


def _section_display_range(section_id: str) -> tuple[str, str]:
    display_header = _display_section_header(section_id)
    range_text = display_header.removeprefix("sg").removeprefix("g")
    if "-" not in range_text:
        return range_text, range_text
    start, end = range_text.split("-", maxsplit=1)
    return start, end


def _section_id_overlaps_expected_range(section_id: str, expected_range: ExpectedSectionRange) -> bool:
    section_start, section_end = _section_display_range(section_id)
    return _section_ranges_overlap(section_start, section_end, expected_range.start, expected_range.end)


def _section_ranges_overlap(left_start: str, left_end: str, right_start: str, right_end: str) -> bool:
    return not (_section_sort_key(left_end) < _section_sort_key(right_start) or _section_sort_key(right_end) < _section_sort_key(left_start))


def _default_db_path() -> Path:
    connection_module = importlib.import_module("src.db.connection")
    return connection_module.get_db_path()


class ApproachDetectionDiagnosticsComparer:
    """Compare generated approach-detection diagnostics."""

    def __init__(self, repo_root: Path) -> None:
        self._repo_root = repo_root

    def compare(self, inputs: list[tuple[str, Path]], output_dir: Path) -> ComparisonDiagnostics:
        if len(inputs) < 2:
            raise ValueError("At least two --input values are required")
        run_inputs = self._expand_inputs(inputs)
        loaded_runs = [(label, _load_json_object(path)) for label, path in run_inputs]
        rows = self._build_rows(loaded_runs)
        diagnostics = ComparisonDiagnostics(
            comparison_name=output_dir.name,
            generated_at=datetime.now(tz=UTC).isoformat(),
            input_labels=tuple(label for label, _ in loaded_runs),
            rows=tuple(rows),
        )
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / DEFAULT_COMPARE_JSON_FILENAME).write_text(json.dumps(diagnostics.to_json(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        (output_dir / DEFAULT_COMPARE_MD_FILENAME).write_text(self.render_markdown(diagnostics), encoding="utf-8")
        return diagnostics

    def render_markdown(self, diagnostics: ComparisonDiagnostics) -> str:
        lines = [
            "# approach_detection_diagnostics__comparison",
            "",
            f"Comparing {', '.join(diagnostics.input_labels)}.",
            "",
            "| Label | Expected | " + " | ".join(diagnostics.input_labels) + " |",
            "| --- | ---: | " + " | ".join("---:" for _ in diagnostics.input_labels) + " |",
        ]
        for row in diagnostics.rows:
            cells = [row.label, "yes" if row.expected else "no"]
            for input_label in diagnostics.input_labels:
                values = row.values_by_label[input_label]
                count = int(values["present_count"])
                total = int(values["run_count"])
                rate = float(values["present_rate"])
                cells.append(f"{count}/{total}<br>{rate:.0%}")
            lines.append("| " + " | ".join(cells) + " |")
        return "\n".join(lines) + "\n"

    def _expand_inputs(self, inputs: list[tuple[str, Path]]) -> list[tuple[str, Path]]:
        expanded: list[tuple[str, Path]] = []
        for label, input_path in inputs:
            payload = _load_json_object(input_path)
            if "runs" in payload:
                runs = _require_list(payload.get("runs"), context=f"{input_path}: runs")
                for run_entry_raw in runs:
                    run_entry = _require_mapping(run_entry_raw, context=f"{input_path}: runs[]")
                    json_path = Path(_require_str(run_entry.get("json_path"), context=f"{input_path}: runs[].json_path"))
                    resolved = json_path if json_path.is_absolute() else self._repo_root / json_path
                    expanded.append((f"{label}:{_require_str(run_entry.get('run_id'), context='runs[].run_id')}", resolved))
            else:
                expanded.append((label, input_path))
        return expanded

    def _build_rows(self, loaded_runs: list[tuple[str, dict[str, object]]]) -> list[ComparisonRow]:
        all_labels: set[str] = set()
        expected_labels: set[str] = set()
        summaries_by_input: dict[str, dict[str, dict[str, object]]] = {}
        for input_label, payload in loaded_runs:
            summaries = _require_list(payload.get("label_summaries"), context="label_summaries")
            summaries_by_input[input_label] = {}
            for raw_summary in summaries:
                summary = _require_mapping(raw_summary, context="label_summaries[]")
                label = _require_str(summary.get("label"), context="label_summaries[].label")
                all_labels.add(label)
                if bool(summary.get("expected")):
                    expected_labels.add(label)
                summaries_by_input[input_label][label] = summary
        rows: list[ComparisonRow] = []
        for label in sorted(all_labels):
            values_by_label: dict[str, dict[str, float | int | bool]] = {}
            for input_label, payload in loaded_runs:
                summary = summaries_by_input[input_label].get(label)
                run_count = len(_require_list(payload.get("rows"), context="rows"))
                present_count = 0 if summary is None else int(_require_num(summary.get("present_count"), context="label_summaries[].present_count"))
                values_by_label[input_label] = {
                    "present_count": present_count,
                    "run_count": run_count,
                    "present_rate": present_count / run_count if run_count else 0.0,
                    "expected": label in expected_labels,
                }
            rows.append(ComparisonRow(label=label, expected=label in expected_labels, values_by_label=values_by_label))
        return rows


class ApproachDetectionDiagnosticsAnalyzer:
    """Summarize diagnostics for EXPERIMENTS.md."""

    def __init__(self, repo_root: Path) -> None:
        self._repo_root = repo_root

    def analyze(self, experiment_dir: Path, input_path: Path | None, section_title: str | None = None) -> str:
        payload, markdown_path = self._load_payload(experiment_dir, input_path)
        if "input_labels" in payload:
            lines = self._analyze_comparison(payload)
        elif "label_summaries" in payload:
            lines = self._analyze_run(payload)
        else:
            raise TypeError("Unsupported approach detection diagnostics input")
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
            json_path = _resolve_index_path(self._repo_root, run_entry, "json_path")
            markdown_path = _resolve_index_path(self._repo_root, run_entry, "markdown_path")
            return _load_json_object(json_path), markdown_path
        payload = _load_json_object(input_path)
        if "runs" in payload and "experiment_name" in payload:
            runs = _require_list(payload.get("runs"), context="index.json: runs")
            if len(runs) != 1:
                raise ValueError(f"{input_path} has {len(runs)} generated runs; pass a run JSON or comparison JSON")
            run_entry = _require_mapping(runs[0], context="index.json: runs[0]")
            json_path = _resolve_index_path(self._repo_root, run_entry, "json_path")
            markdown_path = _resolve_index_path(self._repo_root, run_entry, "markdown_path")
            return _load_json_object(json_path), markdown_path
        return payload, _markdown_path_for_json(input_path)

    def _analyze_run(self, payload: dict[str, object]) -> list[str]:
        rows = _require_list(payload.get("rows"), context="rows")
        summaries = _require_list(payload.get("label_summaries"), context="label_summaries")
        stability = _require_list(payload.get("question_stability"), context="question_stability")
        spurious_rows = [row for row in rows if _require_list(_require_mapping(row, context="rows[]").get("spurious_labels"), context="rows[].spurious_labels")]
        missing_rows = [row for row in rows if _require_list(_require_mapping(row, context="rows[]").get("missing_expected_labels"), context="rows[].missing_expected_labels")]
        lines = [
            f"- Run `{_require_str(payload.get('run_id'), context='run_id')}` covered {len(rows)} answer attempt(s).",
            f"- Provider: `{_require_str(payload.get('provider_name'), context='provider_name')}`",
            f"- Missing expected approach rows: {len(missing_rows)}/{len(rows)}",
            f"- Spurious approach rows: {len(spurious_rows)}/{len(rows)}",
        ]
        for raw_summary in summaries:
            summary = _require_mapping(raw_summary, context="label_summaries[]")
            if not bool(summary.get("expected")):
                continue
            lines.append(
                f"- {_require_str(summary.get('label'), context='label_summaries[].label')}: "
                f"{int(_require_num(summary.get('present_count'), context='label_summaries[].present_count'))}/"
                f"{int(_require_num(summary.get('run_count'), context='label_summaries[].run_count'))} present"
            )
        if stability:
            worst = min(stability, key=lambda item: _require_num(_require_mapping(item, context="question_stability[]").get("stability_score"), context="question_stability[].stability_score"))
            worst_mapping = _require_mapping(worst, context="question_stability[]")
            lines.append(
                f"- Lowest strict stability: {_require_str(worst_mapping.get('question_id'), context='question_stability[].question_id')} "
                f"at {_require_num(worst_mapping.get('stability_score'), context='question_stability[].stability_score'):.1f}"
            )
        return lines

    def _analyze_comparison(self, payload: dict[str, object]) -> list[str]:
        input_labels = _require_list(payload.get("input_labels"), context="input_labels")
        rows = _require_list(payload.get("rows"), context="rows")
        return [
            f"- Compared {len(input_labels)} runs across {len(rows)} approach label row(s).",
            f"- Inputs: {', '.join(str(item) for item in input_labels)}",
        ]

    def _render_section(self, section_title: str, lines: list[str]) -> str:
        return "\n".join([f"## {section_title}", "", *lines, ""])


def _extract_authority_diagnostics(a_response_path: Path) -> tuple[tuple[tuple[str, str], ...], tuple[tuple[str, str], ...], tuple[tuple[str, str], ...], tuple[str, ...]]:
    if not a_response_path.exists():
        return (), (), (), ()
    payload = _load_json_object(a_response_path)
    authority_classification = payload.get("authority_classification")
    if not isinstance(authority_classification, dict):
        return (), (), (), ()
    authority_resolution = payload.get("authority_resolution")
    dropped_documents_raw = authority_resolution.get("discarded_due_to_overlap") if isinstance(authority_resolution, dict) else []
    dropped_documents = tuple(
        sorted(
            {
                _canonical_doc_key(document)
                for document in dropped_documents_raw
                if isinstance(document, str) and document.strip()
            }
        )
    )
    return (
        _extract_authority_references(authority_classification.get("primary_authority")),
        _extract_authority_references(authority_classification.get("supporting_authority")),
        _extract_authority_references(authority_classification.get("peripheral_authority")),
        dropped_documents,
    )


def _extract_authority_references(value: object) -> tuple[tuple[str, str], ...]:
    if not isinstance(value, list):
        return ()
    references: list[tuple[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for item in value:
        if not isinstance(item, dict):
            continue
        document = item.get("document")
        raw_references = item.get("references")
        if not isinstance(document, str) or not isinstance(raw_references, list):
            continue
        canonical_doc_key = _canonical_doc_key(document)
        for raw_reference in raw_references:
            if not isinstance(raw_reference, str) or not raw_reference.strip():
                continue
            reference = (canonical_doc_key, raw_reference.strip())
            if reference in seen:
                continue
            seen.add(reference)
            references.append(reference)
    return tuple(references)


def _parse_approaches(payload: dict[str, object]) -> list[ApproachRecord]:
    raw_approaches = payload.get("approaches")
    if not isinstance(raw_approaches, list):
        return []
    approaches: list[ApproachRecord] = []
    for raw_approach in raw_approaches:
        if not isinstance(raw_approach, dict):
            continue
        label = _optional_str(raw_approach.get("normalized_label"))
        if label is None:
            continue
        references = raw_approach.get("references")
        approaches.append(
            ApproachRecord(
                normalized_label=normalize_label(label),
                label=_optional_str(raw_approach.get("label_fr")) or _optional_str(raw_approach.get("label_en")) or label,
                applicability=_optional_str(raw_approach.get("applicability")),
                reference_count=len(references) if isinstance(references, list) else 0,
            )
        )
    return approaches


def _extract_recommendation(payload: dict[str, object]) -> str | None:
    recommendation = payload.get("recommendation")
    if not isinstance(recommendation, dict):
        return None
    return _optional_str(recommendation.get("answer"))


def _is_expected_chunk(doc_uid: str, chunk_number: str, expected_ranges: tuple[ExpectedSectionRange, ...]) -> bool:
    for expected_range in expected_ranges:
        if doc_uid != expected_range.document:
            continue
        if _section_number_in_range(chunk_number, expected_range.start, expected_range.end):
            return True
    return False


def _section_number_in_range(value: str, start: str, end: str) -> bool:
    parsed_value = _section_sort_key(value)
    return _section_sort_key(start) <= parsed_value <= _section_sort_key(end)


def _section_sort_key(value: str) -> tuple[str, ...]:
    pieces: list[str] = []
    for piece in re.findall(r"[A-Za-z]+|\d+", value):
        pieces.append(f"{int(piece):08d}" if piece.isdigit() else piece.upper())
    return tuple(pieces)


def _question_sort_key(question_id: str) -> tuple[int, str]:
    match = re.search(r"\.(\d+)$", question_id)
    if match is not None:
        return int(match.group(1)), question_id
    return 10**9, question_id


def _run_label_sort_key(run_label: str) -> tuple[int, str]:
    if run_label == "base":
        return 0, run_label
    match = re.search(r"repeat-(\d+)$", run_label)
    if match is not None:
        return int(match.group(1)), run_label
    return 10**9, run_label


def _chunk_label_sort_key(label: str) -> tuple[str, tuple[str, ...]]:
    doc_uid, _, chunk_number = label.partition(" ")
    return doc_uid, _section_sort_key(chunk_number)


def _ordered_unique(values: object) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for raw_value in values:
        value = str(raw_value)
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def _normalize_family_id(family_id: str) -> str:
    return family_id.replace("¤", "").strip()


def _load_json_object(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError(f"{path}: expected a JSON object")
    return payload


def _load_yaml_object(path: Path) -> dict[str, object]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise TypeError(f"{path}: expected a mapping")
    return payload


def _run_diagnostics_from_json(payload: dict[str, object]) -> RunDiagnostics:
    question_sources = [
        PromptfooTestCase(
            family_id=_require_str(_require_mapping(item, context="question_sources[]").get("family_id"), context="question_sources[].family_id"),
            question_path=Path(_require_str(_require_mapping(item, context="question_sources[]").get("question_path"), context="question_sources[].question_path")),
            description=_require_str(_require_mapping(item, context="question_sources[]").get("description"), context="question_sources[].description"),
        )
        for item in _require_list(payload.get("question_sources"), context="question_sources")
    ]
    return RunDiagnostics(
        experiment_name=_require_str(payload.get("experiment_name"), context="experiment_name"),
        provider_name=_require_str(payload.get("provider_name"), context="provider_name"),
        run_id=_require_str(payload.get("run_id"), context="run_id"),
        generated_at=_require_str(payload.get("generated_at"), context="generated_at"),
        question_families=tuple(_require_str(item, context="question_families[]") for item in _require_list(payload.get("question_families"), context="question_families")),
        question_sources=tuple(question_sources),
        question_ids=tuple(_require_str(item, context="question_ids[]") for item in _require_list(payload.get("question_ids"), context="question_ids")),
        expected_labels=tuple(_require_str(item, context="expected_labels[]") for item in _require_list(payload.get("expected_labels"), context="expected_labels")),
        expected_section_ranges=tuple(
            ExpectedSectionRange(
                document=_require_str(_require_mapping(item, context="expected_section_ranges[]").get("document"), context="expected_section_ranges[].document"),
                start=_require_str(_require_mapping(item, context="expected_section_ranges[]").get("start"), context="expected_section_ranges[].start"),
                end=_require_str(_require_mapping(item, context="expected_section_ranges[]").get("end"), context="expected_section_ranges[].end"),
            )
            for item in _require_list(payload.get("expected_section_ranges"), context="expected_section_ranges")
        ),
        rows=tuple(_row_from_json(item) for item in _require_list(payload.get("rows"), context="rows")),
        label_summaries=tuple(_label_summary_from_json(item) for item in _require_list(payload.get("label_summaries"), context="label_summaries")),
        question_stability=tuple(_stability_from_json(item) for item in _require_list(payload.get("question_stability"), context="question_stability")),
    )


def _row_from_json(value: object) -> QuestionRunDiagnostics:
    row = _require_mapping(value, context="rows[]")
    return QuestionRunDiagnostics(
        question_id=_require_str(row.get("question_id"), context="rows[].question_id"),
        question_text=_require_str(row.get("question_text"), context="rows[].question_text") if row.get("question_text") is not None else "",
        embedded_question_text=_require_str(row.get("embedded_question_text"), context="rows[].embedded_question_text") if row.get("embedded_question_text") is not None else "",
        family_id=_require_str(row.get("family_id"), context="rows[].family_id"),
        run_label=_require_str(row.get("run_label"), context="rows[].run_label"),
        artifact_dir=Path(_require_str(row.get("artifact_dir"), context="rows[].artifact_dir")),
        recommendation=_optional_str(row.get("recommendation")),
        approaches=tuple(
            ApproachRecord(
                normalized_label=_require_str(_require_mapping(item, context="rows[].approaches[]").get("normalized_label"), context="rows[].approaches[].normalized_label"),
                label=_require_str(_require_mapping(item, context="rows[].approaches[]").get("label"), context="rows[].approaches[].label"),
                applicability=_optional_str(_require_mapping(item, context="rows[].approaches[]").get("applicability")),
                reference_count=int(_require_num(_require_mapping(item, context="rows[].approaches[]").get("reference_count"), context="rows[].approaches[].reference_count")),
            )
            for item in _require_list(row.get("approaches"), context="rows[].approaches")
        ),
        labels=tuple(_require_str(item, context="rows[].labels[]") for item in _require_list(row.get("labels"), context="rows[].labels")),
        missing_expected_labels=tuple(_require_str(item, context="rows[].missing_expected_labels[]") for item in _require_list(row.get("missing_expected_labels"), context="rows[].missing_expected_labels")),
        spurious_labels=tuple(_require_str(item, context="rows[].spurious_labels[]") for item in _require_list(row.get("spurious_labels"), context="rows[].spurious_labels")),
        prompt_chunks=tuple(_prompt_chunk_from_json(item) for item in _require_list(row.get("prompt_chunks"), context="rows[].prompt_chunks")),
        authoritative_references=tuple(_reference_pair_from_json(item, context="rows[].authoritative_references[]") for item in _require_list(row.get("authoritative_references") or [], context="rows[].authoritative_references")),
        secondary_references=tuple(_reference_pair_from_json(item, context="rows[].secondary_references[]") for item in _require_list(row.get("secondary_references") or [], context="rows[].secondary_references")),
        peripheral_references=tuple(_reference_pair_from_json(item, context="rows[].peripheral_references[]") for item in _require_list(row.get("peripheral_references") or [], context="rows[].peripheral_references")),
        dropped_documents=tuple(_require_str(item, context="rows[].dropped_documents[]") for item in _require_list(row.get("dropped_documents") or [], context="rows[].dropped_documents")),
    )


def _reference_pair_from_json(value: object, *, context: str) -> tuple[str, str]:
    pair = _require_list(value, context=context)
    if len(pair) != 2:
        raise ValueError(f"Expected reference pair of length 2 for {context}, got {pair!r}")
    return (
        _require_str(pair[0], context=f"{context}[0]"),
        _require_str(pair[1], context=f"{context}[1]"),
    )


def _prompt_chunk_from_json(value: object) -> PromptChunk:
    chunk = _require_mapping(value, context="rows[].prompt_chunks[]")
    return PromptChunk(
        doc_uid=_require_str(chunk.get("doc_uid"), context="rows[].prompt_chunks[].doc_uid"),
        chunk_number=_require_str(chunk.get("chunk_number"), context="rows[].prompt_chunks[].chunk_number"),
        score=_require_num(chunk.get("score"), context="rows[].prompt_chunks[].score"),
        chunk_id=_optional_str(chunk.get("chunk_id")),
        expected=bool(chunk.get("expected")),
    )


def _label_summary_from_json(value: object) -> LabelSummary:
    summary = _require_mapping(value, context="label_summaries[]")
    return LabelSummary(
        label=_require_str(summary.get("label"), context="label_summaries[].label"),
        expected=bool(summary.get("expected")),
        present_count=int(_require_num(summary.get("present_count"), context="label_summaries[].present_count")),
        run_count=int(_require_num(summary.get("run_count"), context="label_summaries[].run_count")),
        question_count=int(_require_num(summary.get("question_count"), context="label_summaries[].question_count")),
    )


def _stability_from_json(value: object) -> QuestionStabilitySummary:
    summary = _require_mapping(value, context="question_stability[]")
    return QuestionStabilitySummary(
        question_id=_require_str(summary.get("question_id"), context="question_stability[].question_id"),
        run_count=int(_require_num(summary.get("run_count"), context="question_stability[].run_count")),
        stability_score=_require_num(summary.get("stability_score"), context="question_stability[].stability_score"),
        stability_score_loose=_require_num(summary.get("stability_score_loose"), context="question_stability[].stability_score_loose"),
        approach_set_stability=_require_num(summary.get("approach_set_stability"), context="question_stability[].approach_set_stability"),
        applicability_stability=_require_num(summary.get("applicability_stability"), context="question_stability[].applicability_stability"),
        recommendation_stability=_require_num(summary.get("recommendation_stability"), context="question_stability[].recommendation_stability"),
        missing_expected_count=int(_require_num(summary.get("missing_expected_count"), context="question_stability[].missing_expected_count")),
        spurious_count=int(_require_num(summary.get("spurious_count"), context="question_stability[].spurious_count")),
    )


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
    return stripped or None


def _path_text(path: Path, base: Path) -> str:
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def _resolve_index_path(repo_root: Path, run_entry: dict[str, object], key: str) -> Path:
    raw_path = Path(_require_str(run_entry.get(key), context=f"index.json: runs[].{key}"))
    return raw_path if raw_path.is_absolute() else repo_root / raw_path


def _markdown_path_for_json(json_path: Path) -> Path:
    if json_path.name == DEFAULT_COMPARE_JSON_FILENAME:
        return json_path.with_name(DEFAULT_COMPARE_MD_FILENAME)
    if json_path.name == DEFAULT_INDEX_JSON_FILENAME:
        return json_path.with_name(DEFAULT_INDEX_MD_FILENAME)
    return json_path.with_name(DEFAULT_RUN_MD_FILENAME)


def _markdown_link(markdown_path: Path, experiment_dir: Path) -> str:
    relative_path = os.path.relpath(markdown_path, start=experiment_dir)
    return f"[diagnostics markdown]({relative_path})"


def resolve_experiment_dir(repo_root: Path, experiment: str) -> Path:
    candidate = Path(experiment)
    if candidate.exists():
        return candidate.resolve()
    if experiment.isdigit():
        matches = sorted((repo_root / "experiments").glob(f"{experiment}_*"))
        if len(matches) == 1:
            return matches[0].resolve()
    direct = repo_root / "experiments" / experiment
    if direct.exists():
        return direct.resolve()
    matches = sorted((repo_root / "experiments").glob(f"{experiment}*"))
    if len(matches) == 1:
        return matches[0].resolve()
    raise FileNotFoundError(f"Could not resolve experiment {experiment!r}")
