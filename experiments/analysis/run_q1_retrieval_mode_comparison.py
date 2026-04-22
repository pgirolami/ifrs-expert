"""Compare raw, enriched, and English-control retrieval on the Q1 family.

This experiment runs three retrieval arms:
- fr_raw: French Q1 questions with query_embedding_mode=raw
- fr_enriched: French Q1 questions with query_embedding_mode=enriched
- en_control: English Q1en questions with query_embedding_mode=raw

It writes:
- one target-matrix markdown file per run
- one merged delta markdown report showing every question/document across runs
- one summary markdown file with aggregate metrics for selected target docs
- JSON companions for the merged report and summary
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULT_OUTPUT_DIRNAME = "40_compare_q1_retrieval_modes"
DEFAULT_FR_QUESTION_DIR = "experiments/00_QUESTIONS/Q1"
DEFAULT_EN_QUESTION_DIR = "experiments/00_QUESTIONS/Q1en"
DEFAULT_PRIORITY_DOC_UIDS: tuple[str, ...] = ("ifric16", "ias39", "ifrs9")
DEFAULT_TARGET_DOC_UIDS: tuple[str, ...] = ("ifric16", "ias39", "ifrs9")
DEFAULT_MERGED_REPORT_FILENAME = "generated_merged_delta_report.md"
DEFAULT_MERGED_REPORT_JSON_FILENAME = "generated_merged_delta_report.json"
DEFAULT_SUMMARY_FILENAME = "generated_summary.md"
DEFAULT_SUMMARY_JSON_FILENAME = "generated_summary.json"
TOP_1_RANK = 1
TOP_3_RANK = 3
TOP_5_RANK = 5
LIGHT_RED_RGB: tuple[int, int, int] = (248, 215, 218)
LIGHT_GREEN_RGB: tuple[int, int, int] = (212, 237, 218)


@dataclass(frozen=True)
class QuestionCase:
    """One Q1-style question variant to run through retrieve."""

    question_id: str
    question_text: str
    source_path: Path


@dataclass(frozen=True)
class RetrievedDocument:
    """One unique document retrieved for a question."""

    doc_uid: str
    display_label: str
    score: float
    rank: int


@dataclass(frozen=True)
class QuestionResult:
    """The retrieval results for one question variant."""

    question_id: str
    hits_by_doc_uid: dict[str, RetrievedDocument]


@dataclass(frozen=True)
class DocumentColumn:
    """One document column in a target matrix."""

    doc_uid: str
    display_label: str
    question_count: int
    score_min: float
    score_max: float


@dataclass(frozen=True)
class ComparisonRunConfig:
    """Configuration for one comparison arm."""

    run_id: str
    label: str
    question_dir: Path
    policy_config_path: Path
    matrix_output_path: Path


@dataclass(frozen=True)
class MergedReportRow:
    """One row in the merged cross-run delta report."""

    question_id: str
    doc_uid: str
    display_label: str
    hits_by_run_id: dict[str, RetrievedDocument | None]


@dataclass(frozen=True)
class SummaryMetric:
    """Aggregate metrics for one target document in one run."""

    run_id: str
    run_label: str
    target_doc_uid: str
    target_display_label: str
    question_count: int
    retrieved_count: int
    top_1_count: int
    top_3_count: int
    top_5_count: int
    mean_rank: float | None
    mean_score: float | None


class Q1RetrievalModeComparisonExperiment:
    """Run and compare several retrieval modes on aligned Q1/Q1en questions."""

    def __init__(
        self,
        repo_root: Path,
        output_dir: Path,
        run_configs: tuple[ComparisonRunConfig, ...],
        priority_doc_uids: tuple[str, ...],
        target_doc_uids: tuple[str, ...],
    ) -> None:
        """Initialize the comparison experiment."""
        self._repo_root = repo_root
        self._output_dir = output_dir
        self._run_configs = run_configs
        self._priority_doc_uids = priority_doc_uids
        self._target_doc_uids = target_doc_uids

    def run(self) -> None:
        """Run all comparison arms and write experiment artifacts."""
        self._output_dir.mkdir(parents=True, exist_ok=True)
        results_by_run_id: dict[str, dict[str, QuestionResult]] = {}

        for run_config in self._run_configs:
            questions = self._load_questions(run_config.question_dir)
            question_results = {question.question_id: self._run_question(question, run_config) for question in questions}
            results_by_run_id[run_config.run_id] = question_results
            matrix_markdown = self._build_target_matrix_markdown(list(question_results.values()))
            run_config.matrix_output_path.write_text(matrix_markdown, encoding="utf-8")
            logger.info(f"Wrote per-run target matrix for {run_config.run_id} to {run_config.matrix_output_path}")

        question_ids = self._build_question_order(results_by_run_id)
        merged_rows = self._build_merged_rows(results_by_run_id=results_by_run_id, question_ids=question_ids)
        merged_report_markdown = self._build_merged_report_markdown(merged_rows)
        merged_report_json = self._build_merged_report_json(merged_rows)
        summary_metrics = self._build_summary_metrics(results_by_run_id=results_by_run_id, question_ids=question_ids)
        summary_markdown = self._build_summary_markdown(summary_metrics)
        summary_json = self._build_summary_json(summary_metrics)

        (self._output_dir / DEFAULT_MERGED_REPORT_FILENAME).write_text(merged_report_markdown, encoding="utf-8")
        (self._output_dir / DEFAULT_MERGED_REPORT_JSON_FILENAME).write_text(
            json.dumps(merged_report_json, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (self._output_dir / DEFAULT_SUMMARY_FILENAME).write_text(summary_markdown, encoding="utf-8")
        (self._output_dir / DEFAULT_SUMMARY_JSON_FILENAME).write_text(
            json.dumps(summary_json, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        logger.info(f"Wrote merged delta report to {self._output_dir / DEFAULT_MERGED_REPORT_FILENAME}")
        logger.info(f"Wrote summary report to {self._output_dir / DEFAULT_SUMMARY_FILENAME}")

    def _load_questions(self, question_dir: Path) -> list[QuestionCase]:
        """Load every `Q1.*.txt` question in numeric order."""
        question_paths = sorted(question_dir.glob("Q1.*.txt"), key=_question_sort_key)
        questions: list[QuestionCase] = []
        for question_path in question_paths:
            question_text = question_path.read_text(encoding="utf-8").strip()
            if not question_text:
                logger.warning(f"Skipping empty question file: {question_path}")
                continue
            questions.append(
                QuestionCase(
                    question_id=question_path.stem,
                    question_text=question_text,
                    source_path=question_path,
                )
            )
        if not questions:
            message = f"No Q1 question files found in {question_dir}"
            raise FileNotFoundError(message)
        logger.info(f"Loaded {len(questions)} question(s) from {question_dir}")
        return questions

    def _run_question(self, question: QuestionCase, run_config: ComparisonRunConfig) -> QuestionResult:
        """Run the retrieve CLI for one question variant in one comparison arm."""
        logger.info(f"Running retrieve for run_id={run_config.run_id}, question_id={question.question_id}, policy_config={run_config.policy_config_path}")
        completed_process = subprocess.run(  # noqa: S603
            (
                "uv",
                "run",
                "python",
                "-m",
                "src.cli",
                "retrieve",
                "--policy-config",
                str(run_config.policy_config_path),
                "--json",
            ),
            cwd=self._repo_root,
            input=question.question_text,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed_process.returncode != 0:
            stderr_text = completed_process.stderr.strip()
            logger.error(f"retrieve failed for run_id={run_config.run_id}, question_id={question.question_id}, returncode={completed_process.returncode}: {stderr_text}")
            message = f"retrieve failed for {run_config.run_id}/{question.question_id}: {stderr_text}"
            raise RuntimeError(message)

        try:
            payload = json.loads(completed_process.stdout)
        except json.JSONDecodeError as error:
            logger.exception(f"Could not parse retrieve JSON for run_id={run_config.run_id}, question_id={question.question_id}")
            message = f"Invalid JSON output for {run_config.run_id}/{question.question_id}"
            raise RuntimeError(message) from error

        hits_payload = payload.get("document_hits")
        if not isinstance(hits_payload, list):
            message = f"Expected document_hits list for run_id={run_config.run_id}, question_id={question.question_id}, got: {payload!r}"
            raise TypeError(message)

        hits_by_doc_uid: dict[str, RetrievedDocument] = {}
        for rank, raw_hit in enumerate(hits_payload, start=1):
            hit = _parse_retrieved_document(raw_hit, rank=rank)
            if hit.doc_uid in hits_by_doc_uid:
                logger.warning(f"Duplicate retrieved document for run_id={run_config.run_id}, question_id={question.question_id}: {hit.doc_uid}; keeping first occurrence")
                continue
            hits_by_doc_uid[hit.doc_uid] = hit

        return QuestionResult(question_id=question.question_id, hits_by_doc_uid=hits_by_doc_uid)

    def _build_target_matrix_markdown(self, results: list[QuestionResult]) -> str:
        """Build one per-run target matrix markdown artifact."""
        columns = self._build_columns(results)
        header_cells = ["Total", "Question", *[column.display_label for column in columns]]
        separator_cells = ["---:", "---", *["---:" for _ in columns]]
        lines = [
            "| " + " | ".join(header_cells) + " |",
            "| " + " | ".join(separator_cells) + " |",
        ]

        for result in sorted(results, key=lambda item: _question_id_sort_key(item.question_id)):
            row_total = len(result.hits_by_doc_uid)
            row_cells = [str(row_total), result.question_id]
            for column in columns:
                hit = result.hits_by_doc_uid.get(column.doc_uid)
                row_cells.append(_format_hit_cell(hit, row_total) if hit is not None else "")
            lines.append("| " + " | ".join(row_cells) + " |")

        total_row = ["Total", ""]
        total_row.extend(_format_total_cell(column) for column in columns)
        lines.append("| " + " | ".join(total_row) + " |")
        return "\n".join(lines) + "\n"

    def _build_columns(self, results: list[QuestionResult]) -> list[DocumentColumn]:
        """Build target-matrix columns ordered by priority then coverage."""
        scores_by_doc_uid: dict[str, list[float]] = {}
        labels_by_doc_uid: dict[str, str] = {}
        for result in results:
            for hit in result.hits_by_doc_uid.values():
                scores_by_doc_uid.setdefault(hit.doc_uid, []).append(hit.score)
                labels_by_doc_uid.setdefault(hit.doc_uid, hit.display_label)

        columns = [
            DocumentColumn(
                doc_uid=doc_uid,
                display_label=labels_by_doc_uid[doc_uid],
                question_count=len(scores),
                score_min=min(scores),
                score_max=max(scores),
            )
            for doc_uid, scores in scores_by_doc_uid.items()
        ]
        priority_columns = [column for column in columns if column.doc_uid in self._priority_doc_uids]
        priority_columns.sort(key=lambda column: self._priority_doc_uids.index(column.doc_uid))
        remaining_columns = [column for column in columns if column.doc_uid not in self._priority_doc_uids]
        remaining_columns.sort(key=lambda column: (-column.question_count, column.display_label, column.doc_uid))
        return [*priority_columns, *remaining_columns]

    def _build_question_order(
        self,
        results_by_run_id: dict[str, dict[str, QuestionResult]],
    ) -> list[str]:
        """Build a stable combined question order across all runs."""
        question_ids = {question_id for run_results in results_by_run_id.values() for question_id in run_results}
        return sorted(question_ids, key=_question_id_sort_key)

    def _build_merged_rows(
        self,
        results_by_run_id: dict[str, dict[str, QuestionResult]],
        question_ids: list[str],
    ) -> list[MergedReportRow]:
        """Build one merged row per question/document across all comparison arms."""
        rows: list[MergedReportRow] = []
        for question_id in question_ids:
            doc_uids = self._collect_question_doc_uids(results_by_run_id=results_by_run_id, question_id=question_id)
            ordered_doc_uids = sorted(doc_uids, key=lambda doc_uid: self._merged_row_sort_key(results_by_run_id, question_id, doc_uid))
            for doc_uid in ordered_doc_uids:
                display_label = humanize_doc_uid(doc_uid)
                hits_by_run_id = {
                    run_config.run_id: results_by_run_id.get(run_config.run_id, {}).get(question_id, QuestionResult(question_id=question_id, hits_by_doc_uid={})).hits_by_doc_uid.get(doc_uid) for run_config in self._run_configs
                }
                rows.append(
                    MergedReportRow(
                        question_id=question_id,
                        doc_uid=doc_uid,
                        display_label=display_label,
                        hits_by_run_id=hits_by_run_id,
                    )
                )
        return rows

    def _collect_question_doc_uids(
        self,
        results_by_run_id: dict[str, dict[str, QuestionResult]],
        question_id: str,
    ) -> set[str]:
        """Collect the union of retrieved document UIDs for one question across runs."""
        doc_uids: set[str] = set()
        for run_results in results_by_run_id.values():
            question_result = run_results.get(question_id)
            if question_result is None:
                continue
            doc_uids.update(question_result.hits_by_doc_uid)
        return doc_uids

    def _merged_row_sort_key(
        self,
        results_by_run_id: dict[str, dict[str, QuestionResult]],
        question_id: str,
        doc_uid: str,
    ) -> tuple[int, int, str, str]:
        """Sort merged rows by target priority, then best rank, then label."""
        priority_rank = self._priority_doc_uids.index(doc_uid) if doc_uid in self._priority_doc_uids else len(self._priority_doc_uids)

        ranks: list[int] = []
        for run_results in results_by_run_id.values():
            question_result = run_results.get(question_id)
            if question_result is None:
                continue
            hit = question_result.hits_by_doc_uid.get(doc_uid)
            if hit is not None:
                ranks.append(hit.rank)
        best_rank = min(ranks) if ranks else 10**9
        display_label = humanize_doc_uid(doc_uid)
        return (priority_rank, best_rank, display_label, doc_uid)

    def _build_merged_report_markdown(self, rows: list[MergedReportRow]) -> str:
        """Build a markdown table that merges every question/document across runs."""
        header_cells = ["Question", "Document", *[run_config.label for run_config in self._run_configs]]
        separator_cells = ["---", "---", *["---:" for _ in self._run_configs]]
        lines = [
            "# Merged delta report",
            "",
            "| " + " | ".join(header_cells) + " |",
            "| " + " | ".join(separator_cells) + " |",
        ]
        for row in rows:
            row_cells = [row.question_id, row.display_label]
            row_cells.extend(_format_optional_hit(row.hits_by_run_id.get(run_config.run_id)) for run_config in self._run_configs)
            lines.append("| " + " | ".join(row_cells) + " |")
        return "\n".join(lines) + "\n"

    def _build_merged_report_json(self, rows: list[MergedReportRow]) -> list[dict[str, object]]:
        """Build the JSON payload for the merged report."""
        return [
            {
                "question_id": row.question_id,
                "doc_uid": row.doc_uid,
                "display_label": row.display_label,
                "runs": {run_config.run_id: _hit_to_json(row.hits_by_run_id.get(run_config.run_id)) for run_config in self._run_configs},
            }
            for row in rows
        ]

    def _build_summary_metrics(
        self,
        results_by_run_id: dict[str, dict[str, QuestionResult]],
        question_ids: list[str],
    ) -> list[SummaryMetric]:
        """Build aggregate metrics for each target document and run."""
        metrics: list[SummaryMetric] = []
        for target_doc_uid in self._target_doc_uids:
            for run_config in self._run_configs:
                run_results = results_by_run_id.get(run_config.run_id, {})
                hits: list[RetrievedDocument] = []
                for question_id in question_ids:
                    question_result = run_results.get(question_id)
                    if question_result is None:
                        continue
                    hit = question_result.hits_by_doc_uid.get(target_doc_uid)
                    if hit is not None:
                        hits.append(hit)
                question_count = len(question_ids)
                retrieved_count = len(hits)
                top_1_count = sum(1 for hit in hits if hit.rank <= TOP_1_RANK)
                top_3_count = sum(1 for hit in hits if hit.rank <= TOP_3_RANK)
                top_5_count = sum(1 for hit in hits if hit.rank <= TOP_5_RANK)
                mean_rank = None if not hits else sum(hit.rank for hit in hits) / len(hits)
                mean_score = None if not hits else sum(hit.score for hit in hits) / len(hits)
                metrics.append(
                    SummaryMetric(
                        run_id=run_config.run_id,
                        run_label=run_config.label,
                        target_doc_uid=target_doc_uid,
                        target_display_label=humanize_doc_uid(target_doc_uid),
                        question_count=question_count,
                        retrieved_count=retrieved_count,
                        top_1_count=top_1_count,
                        top_3_count=top_3_count,
                        top_5_count=top_5_count,
                        mean_rank=mean_rank,
                        mean_score=mean_score,
                    )
                )
        return metrics

    def _build_summary_markdown(self, metrics: list[SummaryMetric]) -> str:
        """Build the markdown summary artifact."""
        lines = ["# Summary", ""]
        for target_doc_uid in self._target_doc_uids:
            lines.append(f"## {humanize_doc_uid(target_doc_uid)}")
            lines.append("")
            lines.append("| Run | Retrieved | Top 1 | Top 3 | Top 5 | Mean rank | Mean score |")
            lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: |")
            lines.extend(
                "| "
                + " | ".join(
                    [
                        metric.run_label,
                        _format_count(metric.retrieved_count, metric.question_count),
                        _format_count(metric.top_1_count, metric.question_count),
                        _format_count(metric.top_3_count, metric.question_count),
                        _format_count(metric.top_5_count, metric.question_count),
                        _format_optional_number(metric.mean_rank),
                        _format_optional_number(metric.mean_score),
                    ]
                )
                + " |"
                for metric in metrics
                if metric.target_doc_uid == target_doc_uid
            )
            lines.append("")
        return "\n".join(lines) + "\n"

    def _build_summary_json(self, metrics: list[SummaryMetric]) -> dict[str, object]:
        """Build the JSON summary artifact."""
        return {
            "targets": [
                {
                    "doc_uid": target_doc_uid,
                    "display_label": humanize_doc_uid(target_doc_uid),
                    "runs": [
                        {
                            "run_id": metric.run_id,
                            "run_label": metric.run_label,
                            "question_count": metric.question_count,
                            "retrieved_count": metric.retrieved_count,
                            "top_1_count": metric.top_1_count,
                            "top_3_count": metric.top_3_count,
                            "top_5_count": metric.top_5_count,
                            "mean_rank": metric.mean_rank,
                            "mean_score": metric.mean_score,
                        }
                        for metric in metrics
                        if metric.target_doc_uid == target_doc_uid
                    ],
                }
                for target_doc_uid in self._target_doc_uids
            ]
        }


def _format_hit_cell(hit: RetrievedDocument, row_total: int) -> str:
    """Format a question-row cell with a rank-based background color."""
    background_color = _rank_to_background_color(hit.rank, row_total)
    return f'<span style="display:block; background-color: {background_color}; padding: 0.1rem 0.35rem; border-radius: 0.25rem; text-align: center;">{hit.score:.2f} / <strong>{hit.rank}</strong></span>'


def _format_total_cell(column: DocumentColumn) -> str:
    """Format the total-row cell with count and score range."""
    return f"{column.question_count} ({column.score_min:.2f}-{column.score_max:.2f})"


def _rank_to_background_color(rank: int, total: int) -> str:
    """Blend from light red at the worst rank to light green at the best rank."""
    if total <= 1:
        return _rgb_to_hex(LIGHT_GREEN_RGB)

    progress = (rank - 1) / (total - 1)
    rgb = tuple(round(green + (red - green) * progress) for green, red in zip(LIGHT_GREEN_RGB, LIGHT_RED_RGB, strict=True))
    return _rgb_to_hex(rgb)


def _rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    """Convert an RGB tuple into a hex color string."""
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


def _parse_retrieved_document(payload: object, *, rank: int) -> RetrievedDocument:
    """Parse one document hit from retrieve JSON output."""
    if not isinstance(payload, dict):
        message = f"Expected document hit dict, got: {payload!r}"
        raise TypeError(message)

    doc_uid = payload.get("doc_uid")
    score = payload.get("score")
    if not isinstance(doc_uid, str):
        message = f"Expected doc_uid string, got: {payload!r}"
        raise TypeError(message)
    if not isinstance(score, int | float):
        message = f"Expected numeric score, got: {payload!r}"
        raise TypeError(message)

    return RetrievedDocument(
        doc_uid=doc_uid,
        display_label=humanize_doc_uid(doc_uid),
        score=float(score),
        rank=rank,
    )


def _format_optional_hit(hit: RetrievedDocument | None) -> str:
    """Format one merged-report cell."""
    if hit is None:
        return ""
    return f"{hit.score:.2f} / {hit.rank}"


def _hit_to_json(hit: RetrievedDocument | None) -> dict[str, object] | None:
    """Convert one optional hit into a JSON-friendly mapping."""
    if hit is None:
        return None
    return {
        "doc_uid": hit.doc_uid,
        "display_label": hit.display_label,
        "score": hit.score,
        "rank": hit.rank,
    }


def _format_count(count: int, total: int) -> str:
    """Format a count with its denominator and percentage."""
    if total == 0:
        return "0/0"
    percentage = 100.0 * count / total
    return f"{count}/{total} ({percentage:.1f}%)"


def _format_optional_number(value: float | None) -> str:
    """Format an optional numeric summary cell."""
    if value is None:
        return "-"
    return f"{value:.2f}"


def humanize_doc_uid(doc_uid: str) -> str:
    """Convert a doc UID like `ifric16` into `IFRIC 16`."""
    normalized_doc_uid = doc_uid.strip()
    if not normalized_doc_uid:
        return normalized_doc_uid

    lower_doc_uid = normalized_doc_uid.lower()
    for prefix in ("ifric", "ifrs", "ias", "sic", "ps", "navis"):
        if not lower_doc_uid.startswith(prefix):
            continue
        suffix = normalized_doc_uid[len(prefix) :]
        suffix = suffix.lstrip("-_ ")
        suffix = suffix.replace("_", " ").replace("-", " ")
        suffix = re.sub(r"(?<=\D)(?=\d)", " ", suffix)
        suffix = re.sub(r"\s+", " ", suffix).strip()
        label = prefix.upper()
        return f"{label} {suffix}" if suffix else label

    return normalized_doc_uid


def _question_sort_key(path: Path) -> tuple[int, str]:
    """Sort `Q1.<n>.txt` paths numerically, then lexicographically."""
    suffix = path.stem.removeprefix("Q1.")
    if suffix.isdigit():
        return (int(suffix), path.name)
    return (10**9, path.name)


def _question_id_sort_key(question_id: str) -> tuple[int, str]:
    """Sort question ids like `Q1.12` numerically, then lexicographically."""
    suffix = question_id.removeprefix("Q1.")
    if suffix.isdigit():
        return (int(suffix), question_id)
    return (10**9, question_id)


def _normalize_doc_uids(raw_value: str) -> tuple[str, ...]:
    """Normalize a comma-separated document UID list into a unique ordered tuple."""
    doc_uids: list[str] = []
    seen_doc_uids: set[str] = set()
    for candidate in raw_value.split(","):
        normalized_candidate = candidate.strip().lower()
        if not normalized_candidate or normalized_candidate in seen_doc_uids:
            continue
        seen_doc_uids.add(normalized_candidate)
        doc_uids.append(normalized_candidate)
    return tuple(doc_uids)


def _build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser for the comparison experiment."""
    parser = argparse.ArgumentParser(description="Compare raw, enriched, and English-control Q1 retrieval modes")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=f"Output directory (default: experiments/{DEFAULT_OUTPUT_DIRNAME})",
    )
    parser.add_argument(
        "--fr-question-dir",
        type=Path,
        default=None,
        help=f"French question directory (default: {DEFAULT_FR_QUESTION_DIR})",
    )
    parser.add_argument(
        "--en-question-dir",
        type=Path,
        default=None,
        help=f"English control question directory (default: {DEFAULT_EN_QUESTION_DIR})",
    )
    parser.add_argument(
        "--fr-raw-policy-config",
        type=Path,
        default=None,
        help="Policy config for the raw French arm",
    )
    parser.add_argument(
        "--fr-enriched-policy-config",
        type=Path,
        default=None,
        help="Policy config for the enriched French arm",
    )
    parser.add_argument(
        "--en-control-policy-config",
        type=Path,
        default=None,
        help="Policy config for the English control arm",
    )
    parser.add_argument(
        "--priority-doc-uids",
        type=str,
        default=",".join(DEFAULT_PRIORITY_DOC_UIDS),
        help="Comma-separated document UIDs to prioritize in reports",
    )
    parser.add_argument(
        "--target-doc-uids",
        type=str,
        default=",".join(DEFAULT_TARGET_DOC_UIDS),
        help="Comma-separated target document UIDs to summarize",
    )
    return parser


def main() -> None:
    """Run the comparison experiment from the repository root."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()

    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent
    output_dir = args.output_dir or (repo_root / "experiments" / DEFAULT_OUTPUT_DIRNAME)
    fr_question_dir = args.fr_question_dir or (repo_root / DEFAULT_FR_QUESTION_DIR)
    en_question_dir = args.en_question_dir or (repo_root / DEFAULT_EN_QUESTION_DIR)
    fr_raw_policy_config = args.fr_raw_policy_config or (output_dir / "policy.raw.yaml")
    fr_enriched_policy_config = args.fr_enriched_policy_config or (output_dir / "policy.enriched.yaml")
    en_control_policy_config = args.en_control_policy_config or (output_dir / "policy.raw.yaml")

    experiment = Q1RetrievalModeComparisonExperiment(
        repo_root=repo_root,
        output_dir=output_dir,
        run_configs=(
            ComparisonRunConfig(
                run_id="fr_raw",
                label="fr_raw",
                question_dir=fr_question_dir,
                policy_config_path=fr_raw_policy_config,
                matrix_output_path=output_dir / "generated_fr_raw_target_matrix.md",
            ),
            ComparisonRunConfig(
                run_id="fr_enriched",
                label="fr_enriched",
                question_dir=fr_question_dir,
                policy_config_path=fr_enriched_policy_config,
                matrix_output_path=output_dir / "generated_fr_enriched_target_matrix.md",
            ),
            ComparisonRunConfig(
                run_id="en_control",
                label="en_control",
                question_dir=en_question_dir,
                policy_config_path=en_control_policy_config,
                matrix_output_path=output_dir / "generated_en_control_target_matrix.md",
            ),
        ),
        priority_doc_uids=_normalize_doc_uids(args.priority_doc_uids),
        target_doc_uids=_normalize_doc_uids(args.target_doc_uids),
    )
    experiment.run()
    sys.stdout.write(f"Wrote comparison artifacts to {output_dir}\n")


if __name__ == "__main__":
    main()
