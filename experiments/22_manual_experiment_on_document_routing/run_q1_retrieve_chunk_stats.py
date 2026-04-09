"""Run sub experiment D for chunk-level retrieval statistics by document.

This script:
1. discovers every `Q1.*.txt` question under `experiments/00_QUESTIONS/Q1`
2. runs `retrieve --retrieval-mode documents` with the Sub experiment C settings
3. groups returned chunks by document for each question
4. builds a markdown matrix with one row per question and one column per document
5. writes markdown and JSON artifacts into this experiment directory

Usage:
    uv run python experiments/22_manual_experiment_on_document_routing/run_q1_retrieve_chunk_stats.py
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

logger = logging.getLogger(__name__)

SUB_EXPERIMENT_D_RETRIEVE_COMMAND: tuple[str, ...] = (
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
    "4",
    "--ias-d",
    "100",
    "--ifric-d",
    "6",
    "--sic-d",
    "100",
    "--ps-d",
    "100",
    "--ifrs-min-score",
    "0.53",
    "--ias-min-score",
    "0",
    "--ifric-min-score",
    "0.48",
    "--sic-min-score",
    "0",
    "--ps-min-score",
    "0",
    "--json",
    "--content-min-score",
    "0",
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

CURRENT_DEFAULT_EXPAND_TO_SECTION_RETRIEVE_COMMAND: tuple[str, ...] = (
    *CURRENT_DEFAULT_RETRIEVE_COMMAND,
    "--expand-to-section",
)


@dataclass(frozen=True)
class RetrievedChunk:
    """One retrieved chunk from the retrieve CLI JSON output."""

    doc_uid: str
    score: float
    text: str


@dataclass(frozen=True)
class ChunkStats:
    """Chunk statistics for one document within one question."""

    doc_uid: str
    chunk_count: int
    score_sum: float
    score_min: float
    score_max: float
    score_avg: float
    score_median: float
    avg_char_count: float


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
    context_size_kb: float
    document_stats: tuple[ChunkStats, ...]


@dataclass(frozen=True)
class DocumentColumn:
    """One markdown table column for a returned document."""

    doc_uid: str
    run_count: int
    average_sum_score_per_question: float


@dataclass(frozen=True)
class ExperimentArtifacts:
    """Output artifact locations for the experiment."""

    markdown_path: Path
    json_path: Path


class RetrieveChunkStatsExperiment:
    """Run sub experiment D and build chunk-stat artifacts."""

    def __init__(
        self,
        repo_root: Path,
        question_dir: Path,
        artifacts: ExperimentArtifacts,
        retrieve_command: tuple[str, ...],
        command_preview: str,
    ) -> None:
        """Initialize the experiment runner."""
        self._repo_root = repo_root
        self._question_dir = question_dir
        self._artifacts = artifacts
        self._retrieve_command = retrieve_command
        self._command_preview = command_preview

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
        """Run retrieve for one question and aggregate chunk stats by document."""
        logger.info(f"Running retrieve for {question.question_id}")
        completed_process = subprocess.run(  # noqa: S603
            self._retrieve_command,
            cwd=self._repo_root,
            input=question.question_text,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed_process.returncode != 0:
            logger.error(
                f"retrieve failed for {question.question_id} with return code "
                f"{completed_process.returncode}: {completed_process.stderr.strip()}"
            )
            error_message = (
                f"retrieve failed for {question.question_id}: "
                f"{completed_process.stderr.strip()}"
            )
            raise RuntimeError(error_message)

        try:
            payload = json.loads(completed_process.stdout)
        except json.JSONDecodeError as error:
            logger.exception(f"Could not parse retrieve JSON for {question.question_id}")
            error_message = f"Invalid JSON output for {question.question_id}"
            raise RuntimeError(error_message) from error

        chunks_payload = payload.get("chunks")
        if not isinstance(chunks_payload, list):
            error_message = f"Expected chunks list for {question.question_id}, got: {payload!r}"
            raise TypeError(error_message)

        chunks = [_parse_retrieved_chunk(item) for item in chunks_payload]
        document_stats = tuple(self._build_document_stats(chunks))
        logger.info(
            f"Received {len(chunks)} chunk(s) across {len(document_stats)} document(s) "
            f"for {question.question_id}"
        )
        return QuestionResult(
            question_id=question.question_id,
            question_text=question.question_text,
            context_size_kb=_calculate_context_size_kb(chunks),
            document_stats=document_stats,
        )

    def _build_document_stats(self, chunks: list[RetrievedChunk]) -> list[ChunkStats]:
        """Aggregate one question's retrieved chunks by document."""
        scores_by_doc_uid: dict[str, list[float]] = {}
        char_counts_by_doc_uid: dict[str, list[int]] = {}
        for chunk in chunks:
            scores_by_doc_uid.setdefault(chunk.doc_uid, []).append(chunk.score)
            char_counts_by_doc_uid.setdefault(chunk.doc_uid, []).append(len(chunk.text))

        document_stats = [
            ChunkStats(
                doc_uid=doc_uid,
                chunk_count=len(scores),
                score_sum=sum(scores),
                score_min=min(scores),
                score_max=max(scores),
                score_avg=mean(scores),
                score_median=median(scores),
                avg_char_count=mean(char_counts_by_doc_uid[doc_uid]),
            )
            for doc_uid, scores in scores_by_doc_uid.items()
        ]
        document_stats.sort(key=lambda item: item.doc_uid)
        return document_stats

    def _build_columns(self, results: list[QuestionResult]) -> list[DocumentColumn]:
        """Build table columns ordered by descending average score sum per question."""
        total_questions = len(results)
        stats_by_doc_uid: dict[str, list[ChunkStats]] = {}
        for result in results:
            for stats in result.document_stats:
                stats_by_doc_uid.setdefault(stats.doc_uid, []).append(stats)

        columns = [
            DocumentColumn(
                doc_uid=doc_uid,
                run_count=len(stats_list),
                average_sum_score_per_question=sum(stats.score_sum for stats in stats_list)
                / total_questions,
            )
            for doc_uid, stats_list in stats_by_doc_uid.items()
        ]
        columns.sort(
            key=lambda column: (
                -column.average_sum_score_per_question,
                -column.run_count,
                column.doc_uid,
            )
        )
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
            self._command_preview,
            "```",
            "",
            f"Generated at: `{generated_at}`",
            "",
        ]

        header_cells = ["Question", "Context size"] + [column.doc_uid for column in columns]
        divider_cells = ["---", "---:"] + ["---:"] * len(columns)
        lines.append("| " + " | ".join(header_cells) + " |")
        lines.append("| " + " | ".join(divider_cells) + " |")

        for result in results:
            stats_by_doc_uid = {stats.doc_uid: stats for stats in result.document_stats}
            row_cells = [result.question_id, _format_context_size_kb(result.context_size_kb)]
            for column in columns:
                stats = stats_by_doc_uid.get(column.doc_uid)
                if stats is None:
                    row_cells.append("")
                    continue
                row_cells.append(_format_chunk_stats_cell(stats))
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
        """Build summary rows for the markdown matrix."""
        stats_by_doc_uid: dict[str, list[ChunkStats]] = {column.doc_uid: [] for column in columns}
        for result in results:
            for stats in result.document_stats:
                if stats.doc_uid in stats_by_doc_uid:
                    stats_by_doc_uid[stats.doc_uid].append(stats)

        summary_rows: list[tuple[str, list[str]]] = [
            ("Runs", [str(len(stats_by_doc_uid[column.doc_uid])) for column in columns]),
            (
                "Avg sum/question",
                [f"{column.average_sum_score_per_question:.4f}" for column in columns],
            ),
        ]
        summary_rows.extend(
            self._build_metric_summary_rows(
                title="**Chunk count**",
                columns=columns,
                stats_by_doc_uid=stats_by_doc_uid,
                accessor=lambda stats: float(stats.chunk_count),
                formatter=_format_float_four,
            )
        )
        summary_rows.extend(
            self._build_metric_summary_rows(
                title="**Score sum**",
                columns=columns,
                stats_by_doc_uid=stats_by_doc_uid,
                accessor=lambda stats: stats.score_sum,
                formatter=_format_float_four,
            )
        )
        summary_rows.extend(
            self._build_metric_summary_rows(
                title="**Score min**",
                columns=columns,
                stats_by_doc_uid=stats_by_doc_uid,
                accessor=lambda stats: stats.score_min,
                formatter=_format_float_four,
            )
        )
        summary_rows.extend(
            self._build_metric_summary_rows(
                title="**Score max**",
                columns=columns,
                stats_by_doc_uid=stats_by_doc_uid,
                accessor=lambda stats: stats.score_max,
                formatter=_format_float_four,
            )
        )
        summary_rows.extend(
            self._build_metric_summary_rows(
                title="**Score avg**",
                columns=columns,
                stats_by_doc_uid=stats_by_doc_uid,
                accessor=lambda stats: stats.score_avg,
                formatter=_format_float_four,
            )
        )
        summary_rows.extend(
            self._build_metric_summary_rows(
                title="**Score median**",
                columns=columns,
                stats_by_doc_uid=stats_by_doc_uid,
                accessor=lambda stats: stats.score_median,
                formatter=_format_float_four,
            )
        )
        summary_rows.extend(
            self._build_metric_summary_rows(
                title="**Avg chars**",
                columns=columns,
                stats_by_doc_uid=stats_by_doc_uid,
                accessor=lambda stats: stats.avg_char_count,
                formatter=_format_float_one,
            )
        )
        return ["| " + " | ".join([label, "", *values]) + " |" for label, values in summary_rows]

    def _build_metric_summary_rows(
        self,
        title: str,
        columns: list[DocumentColumn],
        stats_by_doc_uid: dict[str, list[ChunkStats]],
        accessor: callable,
        formatter: callable,
    ) -> list[tuple[str, list[str]]]:
        """Build one titled summary block for one metric."""
        rows: list[tuple[str, list[str]]] = [(title, [""] * len(columns))]
        reducers = (
            ("Min", min),
            ("Max", max),
            ("Average", mean),
            ("Median", median),
        )
        for label, reducer in reducers:
            values: list[str] = []
            for column in columns:
                series = [accessor(stats) for stats in stats_by_doc_uid[column.doc_uid]]
                if not series:
                    values.append("")
                    continue
                reduced_value = _reduce_float_series(series, reducer)
                values.append(formatter(reduced_value))
            rows.append((label, values))
        return rows

    def _write_artifacts(
        self,
        results: list[QuestionResult],
        columns: list[DocumentColumn],
        markdown: str,
    ) -> None:
        """Write markdown and JSON artifacts."""
        self._artifacts.markdown_path.write_text(markdown, encoding="utf-8")
        payload = {
            "command": list(self._retrieve_command),
            "results": [
                {
                    "question_id": result.question_id,
                    "question_text": result.question_text,
                    "context_size_kb": round(result.context_size_kb, 3),
                    "documents": [
                        {
                            "doc_uid": stats.doc_uid,
                            "chunk_count": stats.chunk_count,
                            "score_sum": round(stats.score_sum, 4),
                            "score_min": round(stats.score_min, 4),
                            "score_max": round(stats.score_max, 4),
                            "score_avg": round(stats.score_avg, 4),
                            "score_median": round(stats.score_median, 4),
                            "avg_char_count": round(stats.avg_char_count, 1),
                        }
                        for stats in result.document_stats
                    ],
                }
                for result in results
            ],
            "columns": [
                {
                    "doc_uid": column.doc_uid,
                    "run_count": column.run_count,
                    "average_sum_score_per_question": round(
                        column.average_sum_score_per_question,
                        4,
                    ),
                }
                for column in columns
            ],
        }
        self._artifacts.json_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        logger.info(
            f"Wrote experiment artifacts to {self._artifacts.markdown_path} and {self._artifacts.json_path}"
        )


def _parse_retrieved_chunk(payload: object) -> RetrievedChunk:
    """Parse one retrieved chunk from CLI JSON output."""
    if not isinstance(payload, dict):
        error_message = f"Expected chunk dict, got: {payload!r}"
        raise TypeError(error_message)
    doc_uid = payload.get("doc_uid")
    score = payload.get("score")
    text = payload.get("text")
    if not isinstance(doc_uid, str):
        error_message = f"Expected doc_uid string, got: {payload!r}"
        raise TypeError(error_message)
    if not isinstance(score, int | float):
        error_message = f"Expected numeric score, got: {payload!r}"
        raise TypeError(error_message)
    if not isinstance(text, str):
        error_message = f"Expected text string, got: {payload!r}"
        raise TypeError(error_message)
    return RetrievedChunk(doc_uid=doc_uid, score=float(score), text=text)



def _format_chunk_stats_cell(stats: ChunkStats) -> str:
    """Format one markdown cell for one document's chunk stats."""
    return "<br>".join(
        [
            str(stats.chunk_count),
            f"{stats.score_sum:.4f}",
            f"{stats.score_min:.4f}",
            f"{stats.score_max:.4f}",
            f"{stats.score_avg:.4f}",
            f"{stats.score_median:.4f}",
            f"{stats.avg_char_count:.1f}",
        ]
    )



def _calculate_context_size_kb(chunks: list[RetrievedChunk]) -> float:
    """Calculate the UTF-8 size in kB of the concatenated retrieved chunk text."""
    total_bytes = sum(len(chunk.text.encode("utf-8")) for chunk in chunks)
    return total_bytes / 1000



def _format_context_size_kb(value: float) -> str:
    """Format one context-size value in kB for markdown output."""
    return f"{value:.3f}"



def _format_float_four(value: float) -> str:
    """Format one float to four decimals."""
    return f"{value:.4f}"



def _format_float_one(value: float) -> str:
    """Format one float to one decimal."""
    return f"{value:.1f}"



def _reduce_float_series(values: list[float], reducer: object) -> float:
    """Reduce a float series with a supported reducer."""
    if not values:
        error_message = "Cannot reduce an empty series"
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



def _question_sort_key(path: Path) -> tuple[int, str]:
    """Sort `Q1.<n>.txt` paths numerically, then lexicographically."""
    suffix = path.stem.removeprefix("Q1.")
    if suffix.isdigit():
        return int(suffix), path.name
    return 10**9, path.name



def _build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser for the chunk-stats experiment runner."""
    parser = argparse.ArgumentParser(description="Run the Q1 retrieve chunk-stats experiment")
    parser.add_argument(
        "--preset",
        choices=("subexperiment-d", "current-defaults", "current-defaults-expand-to-section"),
        default="subexperiment-d",
        help="Retrieve command preset to use.",
    )
    parser.add_argument(
        "--output-stem",
        default=None,
        help="Artifact filename stem without extension. Defaults to a preset-specific name.",
    )
    return parser


def _get_retrieve_command(preset: str) -> tuple[str, ...]:
    """Return the retrieve command for the selected preset."""
    if preset == "current-defaults":
        return CURRENT_DEFAULT_RETRIEVE_COMMAND
    if preset == "current-defaults-expand-to-section":
        return CURRENT_DEFAULT_EXPAND_TO_SECTION_RETRIEVE_COMMAND
    return SUB_EXPERIMENT_D_RETRIEVE_COMMAND


def main() -> None:
    """Run the chunk-stats experiment from the repository root."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()
    script_path = Path(__file__).resolve()
    experiment_dir = script_path.parent
    repo_root = experiment_dir.parent.parent
    question_dir = repo_root / "experiments" / "00_QUESTIONS" / "Q1"
    retrieve_command = _get_retrieve_command(args.preset)
    default_output_stem = "generated_q1_retrieve_chunk_stats"
    if args.preset == "current-defaults":
        default_output_stem = "generated_q1_retrieve_chunk_stats_current_defaults"
    elif args.preset == "current-defaults-expand-to-section":
        default_output_stem = "generated_q1_retrieve_chunk_stats_current_defaults_expand_to_section"
    output_stem = args.output_stem or default_output_stem
    artifacts = ExperimentArtifacts(
        markdown_path=experiment_dir / f"{output_stem}.md",
        json_path=experiment_dir / f"{output_stem}.json",
    )
    experiment = RetrieveChunkStatsExperiment(
        repo_root=repo_root,
        question_dir=question_dir,
        artifacts=artifacts,
        retrieve_command=retrieve_command,
        command_preview=f"printf '<question>' | {' '.join(retrieve_command)}",
    )
    _, _, markdown = experiment.run()
    sys.stdout.write(markdown)


if __name__ == "__main__":
    main()
