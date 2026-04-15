"""Run a manual Q1 retrieve-documents routing experiment.

This script:
1. discovers every `Q1.*.txt` question under `experiments/00_QUESTIONS/Q1`
2. runs `retrieve --retrieval-mode documents` for each question
3. reads the returned `document_hits`
4. builds a markdown matrix with one row per question and one column per returned document
5. writes markdown and JSON artifacts into this experiment directory

Usage:
    uv run python experiments/22_manual_experiment_on_document_routing/run_q1_retrieve_document_routing.py
"""

from __future__ import annotations

import argparse
import json
import logging
import subprocess
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from statistics import mean, median

from src.models.document import infer_exact_document_type

logger = logging.getLogger(__name__)

DEFAULT_RETRIEVE_COMMAND: tuple[str, ...] = (
    "uv",
    "run",
    "python",
    "-m",
    "src.cli",
    "retrieve",
    "--retrieval-mode",
    "documents",
    "-d",
    "10",
    "--json",
    "--content-min-score",
    "0.5",
)

CURRENT_DEFAULT_RETRIEVE_COMMAND: tuple[str, ...] = (
    "uv",
    "run",
    "python",
    "-m",
    "src.cli",
    "retrieve",
    "--retrieval-mode",
    "documents",
    "-d",
    "25",
    "--ifrs-d",
    "4",
    "--ias-d",
    "4",
    "--ifric-d",
    "6",
    "--sic-d",
    "6",
    "--ps-d",
    "1",
    "--ifrs-min-score",
    "0.53",
    "--ias-min-score",
    "0.4",
    "--ifric-min-score",
    "0.48",
    "--sic-min-score",
    "0.4",
    "--ps-min-score",
    "0.4",
    "--json",
    "--content-min-score",
    "0.53",
)

LOOSE_DOCUMENT_RETRIEVE_COMMAND: tuple[str, ...] = (
    "uv",
    "run",
    "python",
    "-m",
    "src.cli",
    "retrieve",
    "--retrieval-mode",
    "documents",
    "-d",
    "100",
    "--ifrs-d",
    "100",
    "--ias-d",
    "100",
    "--ifric-d",
    "100",
    "--sic-d",
    "100",
    "--ps-d",
    "100",
    "--ifrs-min-score",
    "0",
    "--ias-min-score",
    "0",
    "--ifric-min-score",
    "0",
    "--sic-min-score",
    "0",
    "--ps-min-score",
    "0",
    "--json",
    "--content-min-score",
    "0",
)


@dataclass(frozen=True)
class DocumentHit:
    """One document returned by `retrieve --retrieval-mode documents`."""

    doc_uid: str
    score: float


@dataclass(frozen=True)
class QuestionCase:
    """One Q1 question to evaluate."""

    question_id: str
    question_text: str
    source_path: Path


@dataclass(frozen=True)
class QuestionResult:
    """One experiment result row for a question."""

    question_id: str
    question_text: str
    hits: tuple[DocumentHit, ...]


@dataclass(frozen=True)
class DocumentColumn:
    """One markdown table column for a returned document."""

    doc_uid: str
    run_count: int
    average_score: float


@dataclass(frozen=True)
class HitPlacement:
    """One hit placement in both the global and per-type ranking."""

    doc_uid: str
    document_type: str | None
    global_rank: int
    global_total: int
    type_rank: int
    type_total: int
    score: float


@dataclass(frozen=True)
class ExperimentArtifacts:
    """Output artifact locations for the experiment."""

    markdown_path: Path
    json_path: Path


@dataclass(frozen=True)
class ExperimentConfig:
    """Runtime configuration for the experiment."""

    retrieve_command: tuple[str, ...]
    command_preview: str


class RetrieveDocumentRoutingExperiment:
    """Run the Q1 retrieve-documents routing experiment and build artifacts."""

    def __init__(
        self,
        repo_root: Path,
        question_dir: Path,
        artifacts: ExperimentArtifacts,
        config: ExperimentConfig,
    ) -> None:
        """Initialize the experiment runner."""
        self._repo_root = repo_root
        self._question_dir = question_dir
        self._artifacts = artifacts
        self._config = config

    def run(self) -> tuple[list[QuestionResult], list[DocumentColumn], str]:
        """Run the experiment and return structured results plus markdown."""
        questions = self._load_questions()
        results = [self._run_question(question) for question in questions]
        columns = self._build_columns(results)
        markdown = self._build_markdown(results, columns)
        self._write_artifacts(results, columns, markdown)
        return results, columns, markdown

    def _load_questions(self) -> list[QuestionCase]:
        """Load every Q1 question file in natural order."""
        question_paths = sorted(self._question_dir.glob("Q1.*.txt"), key=_question_sort_key)
        questions: list[QuestionCase] = []
        for question_path in question_paths:
            question_id = question_path.stem
            question_text = question_path.read_text(encoding="utf-8").strip()
            if not question_text:
                logger.warning(f"Skipping empty question file: {question_path}")
                continue
            questions.append(
                QuestionCase(
                    question_id=question_id,
                    question_text=question_text,
                    source_path=question_path,
                )
            )
        logger.info(f"Loaded {len(questions)} Q1 question(s) from {self._question_dir}")
        return questions

    def _run_question(self, question: QuestionCase) -> QuestionResult:
        """Run `retrieve --retrieval-mode documents` for one question."""
        logger.info(f"Running retrieve for {question.question_id}")
        completed_process = subprocess.run(  # noqa: S603
            self._config.retrieve_command,
            cwd=self._repo_root,
            input=question.question_text,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed_process.returncode != 0:
            logger.error(f"retrieve failed for {question.question_id} with return code {completed_process.returncode}: {completed_process.stderr.strip()}")
            error_message = f"retrieve failed for {question.question_id}: {completed_process.stderr.strip()}"
            raise RuntimeError(error_message)

        try:
            payload = json.loads(completed_process.stdout)
        except json.JSONDecodeError as error:
            logger.exception(f"Could not parse retrieve JSON for {question.question_id}")
            error_message = f"Invalid JSON output for {question.question_id}"
            raise RuntimeError(error_message) from error

        hits_payload = payload.get("document_hits")
        if not isinstance(hits_payload, list):
            error_message = f"Expected document_hits list for {question.question_id}, got: {payload!r}"
            raise TypeError(error_message)

        hits = tuple(_parse_document_hit(item) for item in hits_payload)
        logger.info(f"Received {len(hits)} document hit(s) for {question.question_id}")
        return QuestionResult(
            question_id=question.question_id,
            question_text=question.question_text,
            hits=hits,
        )

    def _build_columns(self, results: list[QuestionResult]) -> list[DocumentColumn]:
        """Build table columns ordered by descending run frequency."""
        scores_by_doc_uid: dict[str, list[float]] = {}
        for result in results:
            unique_hits_by_doc_uid = {hit.doc_uid: hit.score for hit in result.hits}
            for doc_uid, score in unique_hits_by_doc_uid.items():
                scores_by_doc_uid.setdefault(doc_uid, []).append(score)

        columns = [
            DocumentColumn(
                doc_uid=doc_uid,
                run_count=len(scores),
                average_score=mean(scores),
            )
            for doc_uid, scores in scores_by_doc_uid.items()
        ]
        columns.sort(key=lambda column: (-column.run_count, -column.average_score, column.doc_uid))
        logger.info(f"Built {len(columns)} document column(s) for the markdown matrix")
        return columns

    def _build_markdown(
        self,
        results: list[QuestionResult],
        columns: list[DocumentColumn],
    ) -> str:
        """Build the markdown report body for the experiment."""
        generated_at = datetime.now(tz=UTC).replace(microsecond=0).isoformat()
        lines: list[str] = [
            "Command:",
            "```bash",
            self._config.command_preview,
            "```",
            "",
            f"Generated at: `{generated_at}`",
            "",
        ]

        header_cells = ["Question"] + [column.doc_uid for column in columns]
        divider_cells = ["---"] + ["---:"] * len(columns)
        lines.append("| " + " | ".join(header_cells) + " |")
        lines.append("| " + " | ".join(divider_cells) + " |")

        for result in results:
            hit_placements_by_doc_uid = self._build_hit_placements(result)
            row_cells = [result.question_id]
            for column in columns:
                hit_placement = hit_placements_by_doc_uid.get(column.doc_uid)
                if hit_placement is None:
                    row_cells.append("")
                    continue
                row_cells.append(_format_hit_cell(hit_placement))
            lines.append("| " + " | ".join(row_cells) + " |")

        lines.extend(self._build_summary_rows(results, columns))
        lines.extend(["", "### Question text", ""])
        lines.extend(f"- **{result.question_id}** — {result.question_text}" for result in results)
        return "\n".join(lines) + "\n"

    def _build_summary_rows(
        self,
        results: list[QuestionResult],
        columns: list[DocumentColumn],
    ) -> list[str]:
        """Build summary statistic rows for the markdown matrix."""
        scores_by_doc_uid: dict[str, list[float]] = {column.doc_uid: [] for column in columns}
        ranks_by_doc_uid: dict[str, list[int]] = {column.doc_uid: [] for column in columns}
        type_ranks_by_doc_uid: dict[str, list[int]] = {column.doc_uid: [] for column in columns}
        type_totals_by_doc_uid: dict[str, list[int]] = {column.doc_uid: [] for column in columns}
        for result in results:
            for placement in self._build_hit_placements(result).values():
                if placement.doc_uid not in scores_by_doc_uid:
                    continue
                scores_by_doc_uid[placement.doc_uid].append(placement.score)
                ranks_by_doc_uid[placement.doc_uid].append(placement.global_rank)
                type_ranks_by_doc_uid[placement.doc_uid].append(placement.type_rank)
                type_totals_by_doc_uid[placement.doc_uid].append(placement.type_total)

        summary_rows: list[tuple[str, list[str]]] = [
            ("Runs", [str(len(scores_by_doc_uid[column.doc_uid])) for column in columns]),
            ("**Scores**", [""] * len(columns)),
            ("Min", [_format_stat(scores_by_doc_uid[column.doc_uid], min) for column in columns]),
            ("Max", [_format_stat(scores_by_doc_uid[column.doc_uid], max) for column in columns]),
            ("Average", [_format_stat(scores_by_doc_uid[column.doc_uid], mean) for column in columns]),
            ("Median", [_format_stat(scores_by_doc_uid[column.doc_uid], median) for column in columns]),
            ("**Rank**", [""] * len(columns)),
            ("Min", [_format_stat(ranks_by_doc_uid[column.doc_uid], min) for column in columns]),
            ("Max", [_format_stat(ranks_by_doc_uid[column.doc_uid], max) for column in columns]),
            ("Average", [_format_stat(ranks_by_doc_uid[column.doc_uid], mean) for column in columns]),
            ("Median", [_format_stat(ranks_by_doc_uid[column.doc_uid], median) for column in columns]),
            ("**Type rank**", [""] * len(columns)),
            (
                "Min",
                [
                    _format_ratio_stat(
                        type_ranks_by_doc_uid[column.doc_uid],
                        type_totals_by_doc_uid[column.doc_uid],
                        min,
                    )
                    for column in columns
                ],
            ),
            (
                "Max",
                [
                    _format_ratio_stat(
                        type_ranks_by_doc_uid[column.doc_uid],
                        type_totals_by_doc_uid[column.doc_uid],
                        max,
                    )
                    for column in columns
                ],
            ),
            (
                "Average",
                [
                    _format_ratio_stat(
                        type_ranks_by_doc_uid[column.doc_uid],
                        type_totals_by_doc_uid[column.doc_uid],
                        mean,
                    )
                    for column in columns
                ],
            ),
            (
                "Median",
                [
                    _format_ratio_stat(
                        type_ranks_by_doc_uid[column.doc_uid],
                        type_totals_by_doc_uid[column.doc_uid],
                        median,
                    )
                    for column in columns
                ],
            ),
        ]
        return ["| " + " | ".join([label, *values]) + " |" for label, values in summary_rows]

    def _write_artifacts(
        self,
        results: list[QuestionResult],
        columns: list[DocumentColumn],
        markdown: str,
    ) -> None:
        """Write markdown and JSON artifacts."""
        self._artifacts.markdown_path.write_text(markdown, encoding="utf-8")
        payload = {
            "command": list(self._config.retrieve_command),
            "results": [
                {
                    "question_id": result.question_id,
                    "question_text": result.question_text,
                    "hits": [
                        {
                            "doc_uid": placement.doc_uid,
                            "document_type": placement.document_type,
                            "score": placement.score,
                            "global_rank": placement.global_rank,
                            "global_total": placement.global_total,
                            "type_rank": placement.type_rank,
                            "type_total": placement.type_total,
                        }
                        for placement in self._build_hit_placements(result).values()
                    ],
                }
                for result in results
            ],
            "columns": [
                {
                    "doc_uid": column.doc_uid,
                    "run_count": column.run_count,
                    "average_score": column.average_score,
                }
                for column in columns
            ],
        }
        self._artifacts.json_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        logger.info(f"Wrote experiment artifacts to {self._artifacts.markdown_path} and {self._artifacts.json_path}")

    def _build_hit_placements(self, result: QuestionResult) -> dict[str, HitPlacement]:
        """Build global and per-type rank metadata for one question result."""
        type_totals_by_key: dict[str, int] = {}
        for hit in result.hits:
            type_key = _infer_document_type(hit.doc_uid) or "UNKNOWN"
            type_totals_by_key[type_key] = type_totals_by_key.get(type_key, 0) + 1

        type_rank_by_key: dict[str, int] = {}
        placements: dict[str, HitPlacement] = {}
        global_total = len(result.hits)
        for global_rank, hit in enumerate(result.hits, start=1):
            document_type = _infer_document_type(hit.doc_uid)
            type_key = document_type or "UNKNOWN"
            type_rank = type_rank_by_key.get(type_key, 0) + 1
            type_rank_by_key[type_key] = type_rank
            placements[hit.doc_uid] = HitPlacement(
                doc_uid=hit.doc_uid,
                document_type=document_type,
                global_rank=global_rank,
                global_total=global_total,
                type_rank=type_rank,
                type_total=type_totals_by_key[type_key],
                score=hit.score,
            )
        return placements


def _infer_document_type(doc_uid: str) -> str | None:
    """Infer the exact document type from persisted metadata or UID fallback."""
    return infer_exact_document_type(doc_uid)


def _reduce_stat(values: list[float] | list[int], reducer: object) -> float:
    """Reduce one numeric series with the requested summary function."""
    if not values:
        error_message = "Cannot reduce an empty value list"
        raise ValueError(error_message)
    if reducer is min:
        return float(min(values))
    if reducer is max:
        return float(max(values))
    if reducer is mean:
        return float(mean(values))
    if reducer is median:
        return float(median(values))
    error_message = f"Unsupported reducer: {reducer!r}"
    raise ValueError(error_message)


def _format_stat(values: list[float] | list[int], reducer: object) -> str:
    """Format one numeric statistic for markdown output."""
    if not values:
        return ""
    return f"{_reduce_stat(values, reducer):.4f}"


def _format_ratio_stat(
    left_values: list[int],
    right_values: list[int],
    reducer: object,
) -> str:
    """Format one pair of ratio-style statistics for markdown output."""
    if not left_values or not right_values:
        return ""
    left_value = _reduce_stat(left_values, reducer)
    right_value = _reduce_stat(right_values, reducer)
    return f"{left_value:.4f}/{right_value:.4f}"


def _format_hit_cell(placement: HitPlacement) -> str:
    """Format one markdown cell for a returned document hit."""
    document_type = placement.document_type or "UNKNOWN"
    return f"{placement.global_rank}/{placement.global_total}<br>{document_type} {placement.type_rank}/{placement.type_total}<br>{placement.score:.4f}"


def _parse_document_hit(payload: object) -> DocumentHit:
    """Parse one document hit from CLI JSON output."""
    if not isinstance(payload, dict):
        error_message = f"Expected document hit dict, got: {payload!r}"
        raise TypeError(error_message)
    doc_uid = payload.get("doc_uid")
    score = payload.get("score")
    if not isinstance(doc_uid, str):
        error_message = f"Expected doc_uid string, got: {payload!r}"
        raise TypeError(error_message)
    if not isinstance(score, int | float):
        error_message = f"Expected numeric score, got: {payload!r}"
        raise TypeError(error_message)
    return DocumentHit(doc_uid=doc_uid, score=float(score))


def _question_sort_key(path: Path) -> tuple[int, str]:
    """Sort `Q1.<n>.txt` paths numerically, then lexicographically."""
    suffix = path.stem.removeprefix("Q1.")
    if suffix.isdigit():
        return int(suffix), path.name
    return 10**9, path.name


def _build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser for the experiment runner."""
    parser = argparse.ArgumentParser(description="Run the Q1 retrieve document routing experiment")
    parser.add_argument(
        "--preset",
        choices=("standard", "current-defaults", "loose-docs"),
        default="standard",
        help="Retrieve command preset to use.",
    )
    parser.add_argument(
        "--output-stem",
        default=None,
        help="Artifact filename stem without extension. Defaults to a preset-specific name.",
    )
    return parser


def _build_experiment_config(preset: str) -> ExperimentConfig:
    """Build the experiment config for the selected preset."""
    if preset == "loose-docs":
        retrieve_command = LOOSE_DOCUMENT_RETRIEVE_COMMAND
    elif preset == "current-defaults":
        retrieve_command = CURRENT_DEFAULT_RETRIEVE_COMMAND
    else:
        retrieve_command = DEFAULT_RETRIEVE_COMMAND
    return ExperimentConfig(
        retrieve_command=retrieve_command,
        command_preview=f"printf '<question>' | {' '.join(retrieve_command)}",
    )


def main() -> None:
    """Run the experiment from the repository root."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()
    script_path = Path(__file__).resolve()
    experiment_dir = script_path.parent
    repo_root = experiment_dir.parent.parent
    question_dir = repo_root / "experiments" / "00_QUESTIONS" / "Q1"
    config = _build_experiment_config(args.preset)
    default_output_stem = "generated_q1_retrieve_document_routing"
    if args.preset == "current-defaults":
        default_output_stem = "generated_q1_retrieve_document_routing_current_defaults"
    elif args.preset == "loose-docs":
        default_output_stem = "generated_q1_retrieve_document_routing_loose_docs"
    output_stem = args.output_stem or default_output_stem
    artifacts = ExperimentArtifacts(
        markdown_path=experiment_dir / f"{output_stem}.md",
        json_path=experiment_dir / f"{output_stem}.json",
    )
    experiment = RetrieveDocumentRoutingExperiment(
        repo_root=repo_root,
        question_dir=question_dir,
        artifacts=artifacts,
        config=config,
    )
    _, _, markdown = experiment.run()
    sys.stdout.write(markdown)


if __name__ == "__main__":
    main()
