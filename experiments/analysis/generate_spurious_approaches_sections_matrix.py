"""Generate an HTML matrix of emitted approaches vs retrieved sections."""

from __future__ import annotations

import argparse
import html
import importlib
import json
import logging
import re
import sqlite3
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

if TYPE_CHECKING:
    from collections.abc import Iterable

logger = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).parent
EXPERIMENTS_DIR = SCRIPT_DIR.parent
CORE_LABELS: tuple[str, ...] = (
    "cash_flow_hedge",
    "fair_value_hedge",
    "net_investment_hedge",
)
TARGET_DOCS: dict[str, str] = {
    "ifrs9": "IFRS 9",
    "ias21": "IAS 21",
    "ifric16": "IFRIC 16",
    "ifrs10": "IFRS 10",
    "ias24": "IAS 24",
}
RUN_ORDER_BY_NAME: dict[str, int] = {
    "base": 0,
    "repeat-1": 1,
    "repeat-2": 2,
    "repeat-3": 3,
    "repeat-4": 4,
    "repeat-5": 5,
}


@dataclass(frozen=True)
class PromptChunkReference:
    """One retrieved chunk reference found in A-prompt.txt."""

    chunk_db_id: int
    doc_uid: str
    chunk_number: str
    score: float


@dataclass(frozen=True)
class RunRecord:
    """One promptfoo run with labels and retrieved chunks."""

    question_id: str
    run_id: str
    recommendation: str
    labels: tuple[str, ...]
    prompt_chunks: tuple[PromptChunkReference, ...]


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
class LabelColumn:
    """One emitted-label column in the matrix."""

    label: str
    is_core: bool


@dataclass(frozen=True)
class SectionColumn:
    """One section column in the matrix."""

    column_key: str
    canonical_doc_key: str
    doc_display_name: str
    section_id: str
    title: str
    section_lineage: tuple[str, ...]
    position: int


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


@dataclass(frozen=True)
class MatrixRow:
    """One matrix row for a single run."""

    question_id: str
    run_id: str
    recommendation: str
    labels: tuple[str, ...]
    spurious_labels: tuple[str, ...]
    label_presence: dict[str, bool]
    section_cells: dict[str, SectionCell]


@dataclass(frozen=True)
class MatrixModel:
    """All matrix data needed for HTML rendering."""

    experiment_name: str
    provider_name: str
    generated_at: str
    label_columns: tuple[LabelColumn, ...]
    section_columns: tuple[SectionColumn, ...]
    rows: tuple[MatrixRow, ...]
    doc_section_counts: dict[str, int]


@dataclass(frozen=True)
class _ChunkCellEntry:
    """One visible chunk entry used to build a section cell."""

    chunk_number: str
    score: float


class PromptChunkParser:
    """Parse `<chunk ...>` tags from A-prompt.txt."""

    _chunk_tag_pattern = re.compile(r"<chunk\s+([^>]+)>")
    _attribute_pattern = re.compile(r'(\w+)="([^"]*)"')

    def parse(self, content: str) -> list[PromptChunkReference]:
        """Parse prompt chunk tags from prompt content."""
        parsed_chunks: list[PromptChunkReference] = []

        for match in self._chunk_tag_pattern.finditer(content):
            attributes = self._parse_attributes(match.group(1))
            chunk_id_raw = attributes.get("id")
            doc_uid = attributes.get("doc_uid")
            chunk_number = attributes.get("chunk_number") or attributes.get("section_path")
            score_raw = attributes.get("score")

            if chunk_id_raw is None or doc_uid is None or chunk_number is None or score_raw is None:
                continue

            try:
                chunk_db_id = int(chunk_id_raw)
                score = float(score_raw)
            except ValueError:
                logger.warning(
                    f"Skipping chunk with non-numeric id/score: id={chunk_id_raw!r}, score={score_raw!r}",
                )
                continue

            parsed_chunks.append(
                PromptChunkReference(
                    chunk_db_id=chunk_db_id,
                    doc_uid=doc_uid,
                    chunk_number=chunk_number,
                    score=score,
                ),
            )

        return parsed_chunks

    def _parse_attributes(self, raw_attributes: str) -> dict[str, str]:
        """Parse XML-like key/value attributes from one chunk tag."""
        return {match.group(1): match.group(2) for match in self._attribute_pattern.finditer(raw_attributes)}


class PromptfooExperimentLoader:
    """Load promptfoo run records from one experiment/provider."""

    _prompt_chunk_parser: PromptChunkParser

    def __init__(self) -> None:
        """Initialize the loader."""
        self._prompt_chunk_parser = PromptChunkParser()

    def load_runs(self, experiment_name: str, provider_name: str | None) -> tuple[str, str, list[RunRecord]]:
        """Load all runs for one experiment and provider."""
        experiment_dir = EXPERIMENTS_DIR / experiment_name
        if not experiment_dir.exists():
            error_message = f"Experiment directory not found: {experiment_dir}"
            raise FileNotFoundError(error_message)

        run_dir = self._find_latest_run_dir(experiment_dir)
        if run_dir is None:
            error_message = f"No runs found in {experiment_dir / 'runs'}"
            raise FileNotFoundError(error_message)

        resolved_provider_name = provider_name or self._auto_detect_provider(run_dir)
        provider_dirs = self._get_provider_dirs(run_dir, resolved_provider_name)
        if not provider_dirs:
            error_message = (
                f"No provider directories found for provider={resolved_provider_name!r} in {run_dir}"
            )
            raise FileNotFoundError(error_message)

        loaded_runs: list[RunRecord] = []
        for provider_dir, question_id in provider_dirs:
            repetitions = self._get_repetitions(provider_dir)
            for repetition in repetitions:
                run_record = self._load_single_run(
                    provider_dir=provider_dir,
                    question_id=question_id,
                    repetition=repetition,
                )
                if run_record is not None:
                    loaded_runs.append(run_record)

        loaded_runs.sort(key=lambda row: (self._question_sort_key(row.question_id), self._run_sort_key(row.run_id)))
        logger.info(
            f"Loaded {len(loaded_runs)} runs from experiment={experiment_name}, provider={resolved_provider_name}",
        )
        return experiment_name, resolved_provider_name, loaded_runs

    def _find_latest_run_dir(self, experiment_dir: Path) -> Path | None:
        """Return the latest promptfoo run directory."""
        runs_dir = experiment_dir / "runs"
        if not runs_dir.exists():
            return None

        run_dirs = [directory for directory in runs_dir.iterdir() if directory.is_dir()]
        if not run_dirs:
            return None
        return sorted(run_dirs, key=lambda path: path.name, reverse=True)[0]

    def _auto_detect_provider(self, run_dir: Path) -> str:
        """Auto-detect the provider if there is exactly one unique provider name."""
        provider_names = self._list_provider_names(run_dir)
        if len(provider_names) != 1:
            error_message = (
                "Could not auto-detect a unique provider name. "
                f"Found providers: {provider_names}"
            )
            raise ValueError(error_message)
        return provider_names[0]

    def _list_provider_names(self, run_dir: Path) -> list[str]:
        """List unique provider directory names under the artifacts tree."""
        artifacts_dir = run_dir / "artifacts"
        if not artifacts_dir.exists():
            return []

        provider_names: set[str] = set()
        for family_dir in artifacts_dir.iterdir():
            if not family_dir.is_dir():
                continue
            for question_dir in family_dir.iterdir():
                if not question_dir.is_dir():
                    continue
                for provider_dir in question_dir.iterdir():
                    if provider_dir.is_dir():
                        provider_names.add(provider_dir.name)
        return sorted(provider_names)

    def _get_provider_dirs(self, run_dir: Path, provider_name: str) -> list[tuple[Path, str]]:
        """Return `(provider_dir, question_id)` pairs for one provider."""
        artifacts_dir = run_dir / "artifacts"
        if not artifacts_dir.exists():
            return []

        provider_dirs: list[tuple[Path, str]] = []
        for family_dir in artifacts_dir.iterdir():
            if not family_dir.is_dir():
                continue
            for question_dir in family_dir.iterdir():
                if not question_dir.is_dir():
                    continue
                candidate_dir = question_dir / provider_name
                if candidate_dir.exists() and candidate_dir.is_dir():
                    provider_dirs.append((candidate_dir, question_dir.name))
        provider_dirs.sort(key=lambda item: self._question_sort_key(item[1]))
        return provider_dirs

    def _get_repetitions(self, provider_dir: Path) -> list[str | None]:
        """Return base and repeat-* subdirectories with prompt/response files."""
        repetitions: list[str | None] = []
        if (provider_dir / "A-prompt.txt").exists() and (provider_dir / "B-response.json").exists():
            repetitions.append(None)

        for child in sorted(provider_dir.iterdir(), key=lambda path: path.name):
            if not child.is_dir() or not child.name.startswith("repeat-"):
                continue
            if (child / "A-prompt.txt").exists() and (child / "B-response.json").exists():
                repetitions.append(child.name)

        return repetitions

    def _load_single_run(self, provider_dir: Path, question_id: str, repetition: str | None) -> RunRecord | None:
        """Load one run record from a provider directory."""
        run_dir = provider_dir if repetition is None else provider_dir / repetition
        prompt_path = run_dir / "A-prompt.txt"
        response_path = run_dir / "B-response.json"

        try:
            prompt_content = prompt_path.read_text(encoding="utf-8")
        except FileNotFoundError:
            logger.warning(f"Missing prompt file: {prompt_path}")
            return None

        try:
            response_payload = json.loads(response_path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            logger.warning(f"Missing response file: {response_path}")
            return None
        except json.JSONDecodeError as error:
            logger.warning(f"Skipping invalid JSON response {response_path}: {error}")
            return None

        labels = self._extract_labels(response_payload)
        recommendation = self._extract_recommendation(response_payload)
        parsed_chunks = tuple(self._prompt_chunk_parser.parse(prompt_content))
        run_id = "base" if repetition is None else repetition

        return RunRecord(
            question_id=question_id,
            run_id=run_id,
            recommendation=recommendation,
            labels=labels,
            prompt_chunks=parsed_chunks,
        )

    def _extract_labels(self, payload: dict[str, object]) -> tuple[str, ...]:
        """Extract normalized labels from a B-response payload."""
        approaches = payload.get("approaches")
        if not isinstance(approaches, list):
            return ()

        labels: set[str] = set()
        for approach in approaches:
            if not isinstance(approach, dict):
                continue
            normalized_label = approach.get("normalized_label")
            if isinstance(normalized_label, str) and normalized_label.strip():
                labels.add(normalized_label.strip().lower())
        return tuple(sorted(labels))

    def _extract_recommendation(self, payload: dict[str, object]) -> str:
        """Extract the recommendation answer from a B-response payload."""
        recommendation = payload.get("recommendation")
        if not isinstance(recommendation, dict):
            return ""
        answer = recommendation.get("answer")
        if isinstance(answer, str):
            return answer.strip()
        return ""

    def _question_sort_key(self, question_id: str) -> tuple[int, int]:
        """Sort question ids like Q1.9, Q1.10."""
        match = re.fullmatch(r"Q(\d+)\.(\d+)", question_id)
        if match is not None:
            return int(match.group(1)), int(match.group(2))
        return 999, 999

    def _run_sort_key(self, run_id: str) -> int:
        """Sort base before repeat-* runs."""
        if run_id in RUN_ORDER_BY_NAME:
            return RUN_ORDER_BY_NAME[run_id]
        if run_id.startswith("repeat-"):
            suffix = run_id.removeprefix("repeat-")
            if suffix.isdigit():
                return 100 + int(suffix)
        return 999


class SqliteCorpusLookup:
    """Load chunk and section metadata from the corpus sqlite database."""

    _db_path: Path

    def __init__(self, db_path: Path | None = None) -> None:
        """Initialize the lookup with an optional database path override."""
        self._db_path = db_path or _default_db_path()

    def load_chunk_lookup(self, chunk_db_ids: Iterable[int]) -> dict[int, ChunkLookupRecord]:
        """Load chunk lookup records keyed by chunk database id."""
        chunk_ids = sorted(set(chunk_db_ids))
        if not chunk_ids:
            return {}

        records: dict[int, ChunkLookupRecord] = {}
        with sqlite3.connect(f"file:{self._db_path}?mode=ro", uri=True) as connection:
            connection.row_factory = sqlite3.Row
            for batch in self._batched(chunk_ids, 500):
                rows = connection.execute(
                    """
                    SELECT id, doc_uid, chunk_number, containing_section_id
                    FROM chunks
                    WHERE id IN (SELECT value FROM json_each(?))
                    """,
                    (json.dumps(batch),),
                ).fetchall()
                for row in rows:
                    records[int(row["id"])] = ChunkLookupRecord(
                        chunk_db_id=int(row["id"]),
                        doc_uid=str(row["doc_uid"]),
                        chunk_number=str(row["chunk_number"]),
                        containing_section_id=(
                            str(row["containing_section_id"])
                            if row["containing_section_id"] is not None
                            else None
                        ),
                    )
        logger.info(f"Loaded {len(records)} chunk lookup records from {self._db_path}")
        return records

    def load_section_lookup(self, section_ids: Iterable[str]) -> dict[str, SectionDisplayRecord]:
        """Load section display records keyed by section id."""
        unique_section_ids = sorted(set(section_ids))
        if not unique_section_ids:
            return {}

        records: dict[str, SectionDisplayRecord] = {}
        with sqlite3.connect(f"file:{self._db_path}?mode=ro", uri=True) as connection:
            connection.row_factory = sqlite3.Row
            for batch in self._batched(unique_section_ids, 500):
                rows = connection.execute(
                    """
                    SELECT doc_uid, section_id, title, section_lineage, position
                    FROM sections
                    WHERE section_id IN (SELECT value FROM json_each(?))
                    """,
                    (json.dumps(batch),),
                ).fetchall()
                for row in rows:
                    records[str(row["section_id"])] = SectionDisplayRecord(
                        doc_uid=str(row["doc_uid"]),
                        section_id=str(row["section_id"]),
                        title=str(row["title"]),
                        section_lineage=tuple(self._decode_lineage(str(row["section_lineage"]))),
                        position=int(row["position"]),
                    )
        logger.info(f"Loaded {len(records)} section lookup records from {self._db_path}")
        return records

    def _batched(self, values: list[int] | list[str], batch_size: int) -> Iterable[list[int] | list[str]]:
        """Yield batches from a value list."""
        for index in range(0, len(values), batch_size):
            yield values[index : index + batch_size]

    def _decode_lineage(self, raw_lineage: str) -> list[str]:
        """Decode a JSON section lineage payload."""
        decoded = json.loads(raw_lineage)
        if not isinstance(decoded, list) or not all(isinstance(item, str) for item in decoded):
            error_message = f"Invalid section_lineage payload: {raw_lineage}"
            raise ValueError(error_message)
        return decoded


class MatrixBuilder:
    """Build a matrix model from run records and corpus metadata."""

    def build(
        self,
        runs: Iterable[RunRecord],
        chunk_lookup: dict[int, ChunkLookupRecord],
        section_lookup: dict[str, SectionDisplayRecord],
        *,
        experiment_name: str = "",
        provider_name: str = "",
    ) -> MatrixModel:
        """Build one matrix model."""
        run_list = list(runs)
        all_labels = self._collect_all_labels(run_list)
        label_columns = self._build_label_columns(all_labels)
        section_columns = self._build_section_columns(run_list, chunk_lookup, section_lookup)
        rows = self._build_rows(run_list, label_columns, section_columns, chunk_lookup, section_lookup)
        doc_section_counts = self._build_doc_section_counts(section_columns)

        return MatrixModel(
            experiment_name=experiment_name,
            provider_name=provider_name,
            generated_at=datetime.now(tz=UTC).isoformat(timespec="seconds"),
            label_columns=label_columns,
            section_columns=section_columns,
            rows=rows,
            doc_section_counts=doc_section_counts,
        )

    def _collect_all_labels(self, runs: list[RunRecord]) -> set[str]:
        """Collect all emitted labels across all runs."""
        labels: set[str] = set()
        for run in runs:
            labels.update(run.labels)
        return labels

    def _build_label_columns(self, all_labels: set[str]) -> tuple[LabelColumn, ...]:
        """Build ordered label columns with core labels first."""
        ordered_labels: list[LabelColumn] = []
        remaining_labels = set(all_labels)

        for core_label in CORE_LABELS:
            if core_label in all_labels:
                ordered_labels.append(LabelColumn(label=core_label, is_core=True))
                remaining_labels.remove(core_label)

        ordered_labels.extend(
            LabelColumn(label=label, is_core=False)
            for label in sorted(remaining_labels)
        )

        return tuple(ordered_labels)

    def _build_section_columns(
        self,
        runs: list[RunRecord],
        chunk_lookup: dict[int, ChunkLookupRecord],
        section_lookup: dict[str, SectionDisplayRecord],
    ) -> tuple[SectionColumn, ...]:
        """Build ordered section columns from observed retrieved sections only."""
        observed_section_ids_by_doc: dict[str, set[str]] = {doc_key: set() for doc_key in TARGET_DOCS}

        for run in runs:
            for prompt_chunk in run.prompt_chunks:
                chunk_record = chunk_lookup.get(prompt_chunk.chunk_db_id)
                if chunk_record is None or chunk_record.containing_section_id is None:
                    continue
                canonical_doc_key = _canonical_doc_key(prompt_chunk.doc_uid)
                if canonical_doc_key not in TARGET_DOCS:
                    continue
                observed_section_ids_by_doc[canonical_doc_key].add(chunk_record.containing_section_id)

        ordered_columns: list[SectionColumn] = []
        for canonical_doc_key in ("ifrs9", "ias21", "ifric16", "ifrs10", "ias24"):
            section_ids = observed_section_ids_by_doc[canonical_doc_key]
            display_records = [section_lookup[section_id] for section_id in section_ids if section_id in section_lookup]
            display_records.sort(key=lambda record: (record.position, record.section_id))
            ordered_columns.extend(
                SectionColumn(
                    column_key=_section_column_key(canonical_doc_key, record.section_id),
                    canonical_doc_key=canonical_doc_key,
                    doc_display_name=TARGET_DOCS[canonical_doc_key],
                    section_id=record.section_id,
                    title=record.title,
                    section_lineage=record.section_lineage,
                    position=record.position,
                )
                for record in display_records
            )

        return tuple(ordered_columns)

    def _build_rows(
        self,
        runs: list[RunRecord],
        label_columns: tuple[LabelColumn, ...],
        section_columns: tuple[SectionColumn, ...],
        chunk_lookup: dict[int, ChunkLookupRecord],
        section_lookup: dict[str, SectionDisplayRecord],
    ) -> tuple[MatrixRow, ...]:
        """Build ordered matrix rows."""
        section_column_keys = {column.column_key for column in section_columns}
        rows: list[MatrixRow] = []

        for run in runs:
            per_section_entries: dict[str, list[_ChunkCellEntry]] = {}
            for prompt_chunk in run.prompt_chunks:
                canonical_doc_key = _canonical_doc_key(prompt_chunk.doc_uid)
                if canonical_doc_key not in TARGET_DOCS:
                    continue

                chunk_record = chunk_lookup.get(prompt_chunk.chunk_db_id)
                if chunk_record is None or chunk_record.containing_section_id is None:
                    continue
                if chunk_record.containing_section_id not in section_lookup:
                    continue

                section_column_key = _section_column_key(canonical_doc_key, chunk_record.containing_section_id)
                if section_column_key not in section_column_keys:
                    continue

                per_section_entries.setdefault(section_column_key, []).append(
                    _ChunkCellEntry(
                        chunk_number=chunk_record.chunk_number,
                        score=prompt_chunk.score,
                    ),
                )

            section_cells = {
                column_key: self._build_section_cell(entries)
                for column_key, entries in per_section_entries.items()
            }
            spurious_labels = tuple(sorted(label for label in run.labels if label not in CORE_LABELS))
            label_presence = {column.label: (column.label in run.labels) for column in label_columns}

            rows.append(
                MatrixRow(
                    question_id=run.question_id,
                    run_id=run.run_id,
                    recommendation=run.recommendation,
                    labels=run.labels,
                    spurious_labels=spurious_labels,
                    label_presence=label_presence,
                    section_cells=section_cells,
                ),
            )

        rows.sort(key=lambda row: (_question_sort_key(row.question_id), _run_sort_key(row.run_id)))
        return tuple(rows)

    def _build_section_cell(self, entries: list[_ChunkCellEntry]) -> SectionCell:
        """Build a section cell from visible chunk entries in one section."""
        sorted_entries = sorted(entries, key=lambda entry: (entry.chunk_number, entry.score))
        visible_scores = tuple(entry.score for entry in sorted_entries)
        visible_display_text = _format_score_range(visible_scores)
        visible_max_score = max(visible_scores) if visible_scores else None
        visible_chunk_numbers = tuple(entry.chunk_number for entry in sorted_entries)

        retrieved_entries = [entry for entry in sorted_entries if entry.score > 0.0]
        retrieved_scores = tuple(entry.score for entry in retrieved_entries)
        retrieved_display_text = _format_score_range(retrieved_scores)
        retrieved_max_score = max(retrieved_scores) if retrieved_scores else None
        retrieved_chunk_numbers = tuple(entry.chunk_number for entry in retrieved_entries)

        return SectionCell(
            retrieved_scores=retrieved_scores,
            retrieved_display_text=retrieved_display_text,
            retrieved_max_score=retrieved_max_score,
            retrieved_chunk_numbers=retrieved_chunk_numbers,
            visible_scores=visible_scores,
            visible_display_text=visible_display_text,
            visible_max_score=visible_max_score,
            visible_chunk_numbers=visible_chunk_numbers,
        )

    def _build_doc_section_counts(self, section_columns: tuple[SectionColumn, ...]) -> dict[str, int]:
        """Count visible section columns by target document."""
        counts = dict.fromkeys(TARGET_DOCS, 0)
        for section_column in section_columns:
            counts[section_column.canonical_doc_key] += 1
        return counts


class HtmlMatrixRenderer:
    """Render a matrix model as a standalone HTML page."""

    def render(self, matrix: MatrixModel) -> str:
        """Render the matrix to standalone HTML."""
        group_header_html = self._render_group_header(matrix)
        header_html = self._render_column_header(matrix)
        body_html = self._render_body(matrix)
        style_html = self._render_style()
        script_html = self._render_script(matrix)
        legend_html = self._render_legend(matrix)
        spurious_filter_html = self._render_spurious_filter_controls(matrix)

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Spurious approaches vs retrieved sections matrix</title>
  {style_html}
</head>
<body>
  <main>
    <h1>Spurious approaches vs retrieved sections matrix</h1>
    <p><strong>Experiment:</strong> {html.escape(matrix.experiment_name)}<br>
       <strong>Provider:</strong> {html.escape(matrix.provider_name)}<br>
       <strong>Generated:</strong> {html.escape(matrix.generated_at)}</p>

    <section class="controls">
      <button type="button" data-sort-mode="question">Question order</button>
      <button type="button" data-sort-mode="spurious">Spurious-first</button>
      <label><input type="checkbox" id="spurious-only"> Show only runs with spurious labels</label>
      <label><input type="checkbox" id="show-visible-context"> Show visible-context sections</label>
      <label><input type="checkbox" id="hide-empty-columns" checked> Hide empty section columns</label>
      <label><input type="checkbox" class="doc-toggle" data-doc-key="ifrs9" checked> IFRS 9</label>
      <label><input type="checkbox" class="doc-toggle" data-doc-key="ias21" checked> IAS 21</label>
      <label><input type="checkbox" class="doc-toggle" data-doc-key="ifric16" checked> IFRIC 16</label>
      <label><input type="checkbox" class="doc-toggle" data-doc-key="ifrs10" checked> IFRS 10</label>
      <label><input type="checkbox" class="doc-toggle" data-doc-key="ias24" checked> IAS 24</label>
    </section>

    {spurious_filter_html}
    {legend_html}

    <div class="table-wrap">
      <table id="matrix-table">
        <thead>
          <tr>
            {group_header_html}
          </tr>
          <tr>
            {header_html}
          </tr>
        </thead>
        <tbody>
          {body_html}
        </tbody>
      </table>
    </div>
  </main>
  {script_html}
</body>
</html>
"""

    def _render_spurious_filter_controls(self, matrix: MatrixModel) -> str:
        """Render checkbox controls for spurious-label filtering."""
        spurious_labels = [label_column.label for label_column in matrix.label_columns if not label_column.is_core]
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

    def _render_group_header(self, matrix: MatrixModel) -> str:
        """Render the top grouped header row."""
        return "".join(
            (
                '<th class="group-header sticky-group" colspan="4">Run metadata</th>',
                f'<th class="group-header" colspan="{len(matrix.label_columns)}">Emitted labels</th>',
                f'<th class="group-header section-group" id="group-header-ifrs9" data-doc-key="ifrs9" colspan="{matrix.doc_section_counts.get("ifrs9", 0)}">IFRS 9</th>',
                f'<th class="group-header section-group" id="group-header-ias21" data-doc-key="ias21" colspan="{matrix.doc_section_counts.get("ias21", 0)}">IAS 21</th>',
                f'<th class="group-header section-group" id="group-header-ifric16" data-doc-key="ifric16" colspan="{matrix.doc_section_counts.get("ifric16", 0)}">IFRIC 16</th>',
                f'<th class="group-header section-group" id="group-header-ifrs10" data-doc-key="ifrs10" colspan="{matrix.doc_section_counts.get("ifrs10", 0)}">IFRS 10</th>',
                f'<th class="group-header section-group" id="group-header-ias24" data-doc-key="ias24" colspan="{matrix.doc_section_counts.get("ias24", 0)}">IAS 24</th>',
            ),
        )

    def _render_column_header(self, matrix: MatrixModel) -> str:
        """Render the detailed column header row."""
        metadata_headers = (
            '<th class="sticky-1 metadata-col">Q</th>',
            '<th class="sticky-2 metadata-col">run</th>',
            '<th class="sticky-3 metadata-col">rec</th>',
            '<th class="sticky-4 metadata-col">spur</th>',
        )
        label_headers = tuple(
            f'<th class="label-col" data-label="{html.escape(label_column.label)}">{html.escape(label_column.label)}</th>'
            for label_column in matrix.label_columns
        )
        section_headers = tuple(self._render_section_header(section_column) for section_column in matrix.section_columns)
        return "".join((*metadata_headers, *label_headers, *section_headers))

    def _render_section_header(self, section_column: SectionColumn) -> str:
        """Render one section header cell."""
        lineage_text = " > ".join(section_column.section_lineage)
        tooltip = (
            f"{section_column.doc_display_name}\n"
            f"section_id: {section_column.section_id}\n"
            f"title: {section_column.title}\n"
            f"lineage: {lineage_text}\n"
            f"position: {section_column.position}"
        )
        section_header_text = _display_section_header(section_column.section_id)
        return (
            f'<th class="section-col {section_column.canonical_doc_key}" '
            f'data-section-key="{html.escape(section_column.column_key)}" '
            f'data-doc-key="{html.escape(section_column.canonical_doc_key)}" '
            f'title="{html.escape(tooltip)}">{html.escape(section_header_text)}</th>'
        )

    def _render_body(self, matrix: MatrixModel) -> str:
        """Render the table body rows."""
        row_html: list[str] = []
        for index, row in enumerate(matrix.rows):
            row_html.append(self._render_row(index, row, matrix.label_columns, matrix.section_columns))
        return "\n".join(row_html)

    def _render_row(
        self,
        index: int,
        row: MatrixRow,
        label_columns: tuple[LabelColumn, ...],
        section_columns: tuple[SectionColumn, ...],
    ) -> str:
        """Render one matrix row."""
        spurious_text = "<br>".join(html.escape(label) for label in row.spurious_labels)
        metadata_cells = (
            f'<td class="sticky-1 metadata-col metadata-q">{html.escape(row.question_id)}</td>',
            f'<td class="sticky-2 metadata-col metadata-run">{html.escape(_display_run_id(row.run_id))}</td>',
            f'<td class="sticky-3 metadata-col metadata-rec">{html.escape(_display_recommendation(row.recommendation))}</td>',
            f'<td class="sticky-4 metadata-col metadata-spur">{spurious_text}</td>',
        )
        label_cells = tuple(self._render_label_cell(label_column, row) for label_column in label_columns)
        section_cells = tuple(self._render_section_cell(section_column, row.section_cells.get(section_column.column_key)) for section_column in section_columns)

        order_question = index
        order_spurious = self._spurious_order_value(row, index)
        spurious_labels_attr = "|".join(row.spurious_labels)
        return (
            f'<tr data-order-question="{order_question}" '
            f'data-order-spurious="{order_spurious}" '
            f'data-has-spurious="{"1" if row.spurious_labels else "0"}" '
            f'data-spurious-labels="{html.escape(spurious_labels_attr)}" '
            f'data-question-id="{html.escape(row.question_id)}">'
            f'{"".join((*metadata_cells, *label_cells, *section_cells))}'
            '</tr>'
        )

    def _spurious_order_value(self, row: MatrixRow, fallback_index: int) -> str:
        """Build a stable string sort key for spurious-first ordering."""
        spurious_prefix = "0" if row.spurious_labels else "1"
        spurious_text = "|".join(row.spurious_labels)
        return f"{spurious_prefix}:{spurious_text}:{row.question_id}:{row.run_id}:{fallback_index:04d}"

    def _render_label_cell(self, label_column: LabelColumn, row: MatrixRow) -> str:
        """Render one binary emitted-label cell."""
        is_present = row.label_presence.get(label_column.label, False)
        kind_class = "core" if label_column.is_core else "spurious"
        presence_class = "present" if is_present else "absent"
        symbol = "✅" if label_column.is_core and is_present else ("✓" if is_present else "")
        return (
            f'<td class="label-cell {kind_class} {presence_class}" '
            f'data-label="{html.escape(label_column.label)}">{symbol}</td>'
        )

    def _render_section_cell(self, section_column: SectionColumn, section_cell: SectionCell | None) -> str:
        """Render one section cell."""
        if section_cell is None:
            return (
                f'<td class="section-cell {section_column.canonical_doc_key}" '
                f'data-section-key="{html.escape(section_column.column_key)}" '
                f'data-doc-key="{html.escape(section_column.canonical_doc_key)}" '
                f'data-has-retrieved="0" '
                f'data-has-visible="0"></td>'
            )

        lineage_text = " > ".join(section_column.section_lineage)
        retrieved_chunk_lines = [
            f"- {chunk_number} ({score:.2f})"
            for chunk_number, score in zip(section_cell.retrieved_chunk_numbers, section_cell.retrieved_scores, strict=True)
        ]
        visible_chunk_lines = [
            f"- {chunk_number} ({score:.2f})"
            for chunk_number, score in zip(section_cell.visible_chunk_numbers, section_cell.visible_scores, strict=True)
        ]
        retrieved_chunk_lines_text = "\n".join(retrieved_chunk_lines) if retrieved_chunk_lines else "(none)"
        visible_chunk_lines_text = "\n".join(visible_chunk_lines) if visible_chunk_lines else "(none)"
        tooltip = (
            f"{section_column.doc_display_name}\n"
            f"section_id: {section_column.section_id}\n"
            f"title: {section_column.title}\n"
            f"lineage: {lineage_text}\n\n"
            f"retrieved chunks:\n"
            f"{retrieved_chunk_lines_text}\n\n"
            f"visible context chunks:\n"
            f"{visible_chunk_lines_text}\n\n"
            f"retrieved display: {section_cell.retrieved_display_text or '(blank)'}\n"
            f"visible display: {section_cell.visible_display_text or '(blank)'}"
        )
        retrieved_color = (
            _section_background_color(section_column.canonical_doc_key, section_cell.retrieved_max_score)
            if section_cell.retrieved_max_score is not None
            else "transparent"
        )
        visible_color = (
            _section_background_color(section_column.canonical_doc_key, section_cell.visible_max_score)
            if section_cell.visible_max_score is not None
            else "transparent"
        )
        has_retrieved = "1" if section_cell.retrieved_scores else "0"
        has_visible = "1" if section_cell.visible_scores else "0"
        return (
            f'<td class="section-cell {section_column.canonical_doc_key}" '
            f'data-section-key="{html.escape(section_column.column_key)}" '
            f'data-doc-key="{html.escape(section_column.canonical_doc_key)}" '
            f'data-has-retrieved="{has_retrieved}" '
            f'data-has-visible="{has_visible}" '
            f'data-retrieved-text="{html.escape(section_cell.retrieved_display_text)}" '
            f'data-visible-text="{html.escape(section_cell.visible_display_text)}" '
            f'data-retrieved-bg="{html.escape(retrieved_color)}" '
            f'data-visible-bg="{html.escape(visible_color)}" '
            f'title="{html.escape(tooltip)}" '
            f'style="background-color: {retrieved_color};">{html.escape(section_cell.retrieved_display_text)}</td>'
        )

    def _render_legend(self, matrix: MatrixModel) -> str:
        """Render the legend and summary block."""
        return f"""
<section class="legend">
  <p>
    <strong>Rows:</strong> {len(matrix.rows)} runs.<br>
    <strong>Section columns:</strong> {len(matrix.section_columns)} observed visible-context sections across runs.
  </p>
  <ul>
    <li>Core label columns use ✅ when present; spurious label columns are red when present.</li>
    <li>Section text shows the score range for the active mode: retrieved-only by default, or full visible context when toggled on.</li>
    <li>Blue = IFRS 9, orange = IAS 21, green = IFRIC 16, purple = IFRS 10, pink = IAS 24.</li>
    <li>Darker section cells mean a higher maximum retrieved score in that section.</li>
  </ul>
</section>
"""

    def _render_style(self) -> str:
        """Render embedded CSS."""
        return """
<style>
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    margin: 0;
    color: #1f2937;
    background: #f8fafc;
  }
  main {
    padding: 1rem;
  }
  h1 {
    margin-top: 0;
  }
  .controls {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-bottom: 1rem;
    align-items: center;
  }
  .legend {
    margin-bottom: 1rem;
    padding: 0.75rem 1rem;
    background: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 8px;
  }
  .spurious-filter-panel {
    margin-bottom: 1rem;
    padding: 0.75rem 1rem;
    background: #ffffff;
    border: 1px solid #d1d5db;
    border-radius: 8px;
  }
  .spurious-filter-actions {
    display: flex;
    gap: 0.5rem;
    margin: 0.5rem 0;
  }
  .spurious-filter-options {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem 1rem;
  }
  .spurious-filter-option {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
  }
  .table-wrap {
    overflow: auto;
    border: 1px solid #d1d5db;
    background: #ffffff;
  }
  table {
    border-collapse: collapse;
    font-size: 12px;
    width: max-content;
    min-width: 100%;
  }
  th, td {
    border: 1px solid #d1d5db;
    padding: 0.35rem 0.5rem;
    text-align: center;
    white-space: nowrap;
  }
  thead th {
    position: sticky;
    top: 0;
    z-index: 3;
    background: #f3f4f6;
  }
  .group-header {
    background: #e5e7eb;
    font-weight: 700;
  }
  .metadata-col {
    text-align: left;
    background: #ffffff;
  }
  .metadata-q,
  .metadata-run,
  .metadata-rec {
    text-align: center;
  }
  .metadata-spur {
    white-space: normal;
    line-height: 1.2;
    min-width: 140px;
  }
  .sticky-1, .sticky-2, .sticky-3, .sticky-4 {
    position: sticky;
    z-index: 2;
    background: #ffffff;
  }
  .sticky-1 { left: 0; min-width: 56px; }
  .sticky-2 { left: 56px; min-width: 34px; }
  .sticky-3 { left: 90px; min-width: 54px; }
  .sticky-4 { left: 144px; min-width: 140px; }
  thead .sticky-1, thead .sticky-2, thead .sticky-3, thead .sticky-4 {
    z-index: 4;
    background: #f3f4f6;
  }
  .label-cell.present.core {
    color: #111827;
    font-weight: 700;
  }
  .label-cell.present.spurious {
    background: #b91c1c;
    color: #ffffff;
    font-weight: 700;
  }
  .label-cell.absent {
    color: #d1d5db;
  }
  .label-cell.core.absent {
    background: #ffffff;
  }
  .section-cell {
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  }
  button {
    cursor: pointer;
  }
</style>
"""

    def _render_script(self, matrix: MatrixModel) -> str:
        """Render embedded JS for sorting and filtering."""
        section_keys = [column.column_key for column in matrix.section_columns]
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
      if (mode === 'question') {{
        return Number(leftValue) - Number(rightValue);
      }}
      return leftValue.localeCompare(rightValue);
    }});
    rows.forEach((row) => tableBody.appendChild(row));
  }}

  function selectedSpuriousLabels() {{
    return new Set(
      Array.from(spuriousLabelFilters)
        .filter((checkbox) => checkbox.checked)
        .map((checkbox) => checkbox.dataset.spuriousLabel)
    );
  }}

  function applyRowVisibility() {{
    const spuriousOnly = spuriousOnlyCheckbox.checked;
    const selectedLabels = selectedSpuriousLabels();
    const rows = Array.from(tableBody.querySelectorAll('tr'));
    rows.forEach((row) => {{
      const hasSpurious = row.dataset.hasSpurious === '1';
      const rowSpuriousLabels = row.dataset.spuriousLabels
        ? row.dataset.spuriousLabels.split('|').filter((value) => value.length > 0)
        : [];
      const matchesSelectedLabels =
        selectedLabels.size === 0 || rowSpuriousLabels.some((label) => selectedLabels.has(label));
      const isVisible = (!spuriousOnly || hasSpurious) && matchesSelectedLabels;
      row.style.display = isVisible ? '' : 'none';
    }});
  }}

  function isVisibleContextMode() {{
    return showVisibleContextCheckbox.checked;
  }}

  function updateSectionCellPresentation() {{
    const useVisibleContext = isVisibleContextMode();
    document.querySelectorAll('td.section-cell').forEach((cell) => {{
      const text = useVisibleContext ? cell.dataset.visibleText : cell.dataset.retrievedText;
      const backgroundColor = useVisibleContext ? cell.dataset.visibleBg : cell.dataset.retrievedBg;
      cell.textContent = text || '';
      cell.style.backgroundColor = backgroundColor || 'transparent';
    }});
  }}

  function updateSectionVisibility() {{
    const enabledDocs = new Set(
      Array.from(docToggles)
        .filter((checkbox) => checkbox.checked)
        .map((checkbox) => checkbox.dataset.docKey)
    );
    const rows = visibleRows();
    const hideEmpty = hideEmptyCheckbox.checked;
    const visibleCounts = {{ ifrs9: 0, ias21: 0, ifric16: 0, ifrs10: 0, ias24: 0 }};

    sectionKeys.forEach((sectionKey) => {{
      const header = document.querySelector(`th[data-section-key="${{sectionKey}}"]`);
      if (!header) {{
        return;
      }}
      const docKey = header.dataset.docKey;
      let visible = enabledDocs.has(docKey);
      if (visible && hideEmpty) {{
        visible = rows.some((row) => {{
          const cell = row.querySelector(`td[data-section-key="${{sectionKey}}"]`);
          if (!cell) {{
            return false;
          }}
          return isVisibleContextMode() ? cell.dataset.hasVisible === '1' : cell.dataset.hasRetrieved === '1';
        }});
      }}

      header.style.display = visible ? '' : 'none';
      document.querySelectorAll(`td[data-section-key="${{sectionKey}}"]`).forEach((cell) => {{
        cell.style.display = visible ? '' : 'none';
      }});
      if (visible) {{
        visibleCounts[docKey] += 1;
      }}
    }});

    ['ifrs9', 'ias21', 'ifric16', 'ifrs10', 'ias24'].forEach((docKey) => {{
      const groupHeader = document.getElementById(`group-header-${{docKey}}`);
      if (!groupHeader) {{
        return;
      }}
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

  sortButtons.forEach((button) => {{
    button.addEventListener('click', () => {{
      sortRows(button.dataset.sortMode);
      updateSectionVisibility();
    }});
  }});
  spuriousOnlyCheckbox.addEventListener('change', applyAll);
  showVisibleContextCheckbox.addEventListener('change', applyAll);
  hideEmptyCheckbox.addEventListener('change', updateSectionVisibility);
  docToggles.forEach((checkbox) => checkbox.addEventListener('change', updateSectionVisibility));
  spuriousLabelFilters.forEach((checkbox) => checkbox.addEventListener('change', applyAll));
  if (selectAllSpuriousButton) {{
    selectAllSpuriousButton.addEventListener('click', () => {{
      spuriousLabelFilters.forEach((checkbox) => {{
        checkbox.checked = true;
      }});
      applyAll();
    }});
  }}
  if (clearAllSpuriousButton) {{
    clearAllSpuriousButton.addEventListener('click', () => {{
      spuriousLabelFilters.forEach((checkbox) => {{
        checkbox.checked = false;
      }});
      applyAll();
    }});
  }}
  applyAll();
</script>
"""


def _canonical_doc_key(doc_uid: str) -> str:
    """Canonicalize document uid for matching target standards."""
    return re.sub(r"[^a-z0-9]", "", doc_uid.lower())


def _section_column_key(canonical_doc_key: str, section_id: str) -> str:
    """Build a stable section column key."""
    return f"{canonical_doc_key}::{section_id}"


def _display_run_id(run_id: str) -> str:
    """Return a compact display id for one run."""
    if run_id == "base":
        return "0"
    if run_id.startswith("repeat-"):
        suffix = run_id.removeprefix("repeat-")
        if suffix.isdigit():
            return suffix
    return run_id


def _display_recommendation(recommendation: str) -> str:
    """Return a compact display form for one recommendation."""
    if recommendation == "oui_sous_conditions":
        return "oui_sc"
    return recommendation


def _display_section_header(section_id: str) -> str:
    """Return the visible section header text from a section id."""
    underscore_index = section_id.find("_")
    if underscore_index == -1:
        return section_id
    return section_id[underscore_index + 1 :]


def _format_score_range(scores: tuple[float, ...]) -> str:
    """Format one or more scores as a 2-decimal range string."""
    if not scores:
        return ""
    min_score = min(scores)
    max_score = max(scores)
    if min_score == max_score:
        return f"{min_score:.2f}"
    return f"{min_score:.2f}-{max_score:.2f}"


def _section_background_color(canonical_doc_key: str, max_score: float | None) -> str:
    """Return an HSL background color for one section cell."""
    hue_by_doc = {
        "ifrs9": 214,
        "ias21": 32,
        "ifric16": 140,
        "ifrs10": 268,
        "ias24": 330,
    }
    hue = hue_by_doc.get(canonical_doc_key, 0)
    if max_score is None:
        return "transparent"
    if max_score <= 0.0:
        return f"hsl({hue} 35% 97.5%)"
    clamped_score = min(max(max_score, 0.40), 0.70)
    normalized_score = (clamped_score - 0.40) / 0.30
    lightness = 96.0 - (normalized_score * 34.0)
    return f"hsl({hue} 70% {lightness:.1f}%)"


def _question_sort_key(question_id: str) -> tuple[int, int]:
    """Sort question ids like Q1.9, Q1.10."""
    match = re.fullmatch(r"Q(\d+)\.(\d+)", question_id)
    if match is not None:
        return int(match.group(1)), int(match.group(2))
    return 999, 999


def _run_sort_key(run_id: str) -> int:
    """Sort base before repeat-* runs."""
    if run_id in RUN_ORDER_BY_NAME:
        return RUN_ORDER_BY_NAME[run_id]
    return 999


def _collect_target_chunk_ids(runs: Iterable[RunRecord]) -> set[int]:
    """Collect target-doc chunk ids used by the matrix."""
    chunk_ids: set[int] = set()
    for run in runs:
        for prompt_chunk in run.prompt_chunks:
            if _canonical_doc_key(prompt_chunk.doc_uid) not in TARGET_DOCS:
                continue
            chunk_ids.add(prompt_chunk.chunk_db_id)
    return chunk_ids


def _collect_section_ids(chunk_lookup: dict[int, ChunkLookupRecord]) -> set[str]:
    """Collect referenced section ids from chunk lookup metadata."""
    section_ids: set[str] = set()
    for chunk_record in chunk_lookup.values():
        if chunk_record.containing_section_id is not None:
            section_ids.add(chunk_record.containing_section_id)
    return section_ids


def _default_db_path() -> Path:
    """Return the corpus sqlite database path."""
    connection_module = importlib.import_module("src.db.connection")
    return connection_module.get_db_path()


def _configure_logging(*, verbose: bool) -> None:
    """Configure root logging."""
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(levelname)s %(name)s: %(message)s",
    )


def main() -> None:
    """Generate the HTML matrix."""
    parser = argparse.ArgumentParser(description="Generate spurious approaches vs sections HTML matrix")
    parser.add_argument("--experiment", required=True, help="Experiment directory name under experiments/")
    parser.add_argument("--provider", help="Provider directory name; auto-detect if omitted and unique")
    parser.add_argument("--output", help="Output HTML path; defaults to <experiment>/spurious_approaches_vs_sections_matrix.html")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose logging")
    args = parser.parse_args()

    _configure_logging(verbose=args.verbose)

    loader = PromptfooExperimentLoader()
    experiment_name, provider_name, runs = loader.load_runs(args.experiment, args.provider)

    corpus_lookup = SqliteCorpusLookup()
    chunk_lookup = corpus_lookup.load_chunk_lookup(_collect_target_chunk_ids(runs))
    section_lookup = corpus_lookup.load_section_lookup(_collect_section_ids(chunk_lookup))

    builder = MatrixBuilder()
    matrix = builder.build(
        runs=runs,
        chunk_lookup=chunk_lookup,
        section_lookup=section_lookup,
        experiment_name=experiment_name,
        provider_name=provider_name,
    )

    renderer = HtmlMatrixRenderer()
    rendered_html = renderer.render(matrix)

    output_path = (
        Path(args.output)
        if args.output
        else EXPERIMENTS_DIR / experiment_name / "spurious_approaches_vs_sections_matrix.html"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered_html, encoding="utf-8")
    logger.info(f"Wrote HTML matrix to {output_path}")


if __name__ == "__main__":
    main()
