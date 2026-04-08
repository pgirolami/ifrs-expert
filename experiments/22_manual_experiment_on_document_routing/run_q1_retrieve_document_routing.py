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

import json
import logging
import subprocess
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from statistics import mean, median

logger = logging.getLogger(__name__)

RETRIEVE_COMMAND: tuple[str, ...] = (
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
class ExperimentArtifacts:
    """Output artifact locations for the experiment."""

    markdown_path: Path
    json_path: Path


class RetrieveDocumentRoutingExperiment:
    """Run the Q1 retrieve-documents routing experiment and build artifacts."""

    def __init__(
        self,
        repo_root: Path,
        question_dir: Path,
        artifacts: ExperimentArtifacts,
    ) -> None:
        """Initialize the experiment runner."""
        self._repo_root = repo_root
        self._question_dir = question_dir
        self._artifacts = artifacts

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
            RETRIEVE_COMMAND,
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
            "printf '<question>' | uv run python -m src.cli retrieve --retrieval-mode documents -d 10 --json --content-min-score 0.5",
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
            hit_position_by_doc_uid = {
                hit.doc_uid: (index + 1, len(result.hits), hit.score)
                for index, hit in enumerate(result.hits)
            }
            row_cells = [result.question_id]
            for column in columns:
                hit_position = hit_position_by_doc_uid.get(column.doc_uid)
                if hit_position is None:
                    row_cells.append("")
                    continue
                rank, total_hits, score = hit_position
                row_cells.append(f"{rank}/{total_hits}<br>{score:.4f}")
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
        for result in results:
            for index, hit in enumerate(result.hits, start=1):
                if hit.doc_uid not in scores_by_doc_uid:
                    continue
                scores_by_doc_uid[hit.doc_uid].append(hit.score)
                ranks_by_doc_uid[hit.doc_uid].append(index)

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
            "command": list(RETRIEVE_COMMAND),
            "results": [
                {
                    "question_id": result.question_id,
                    "question_text": result.question_text,
                    "hits": [
                        {
                            "doc_uid": hit.doc_uid,
                            "score": hit.score,
                        }
                        for hit in result.hits
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
        logger.info(
            f"Wrote experiment artifacts to {self._artifacts.markdown_path} and {self._artifacts.json_path}"
        )


def _format_stat(values: list[float] | list[int], reducer: object) -> str:
    """Format one numeric statistic for markdown output."""
    if not values:
        return ""
    if reducer is min:
        value = min(values)
    elif reducer is max:
        value = max(values)
    elif reducer is mean:
        value = mean(values)
    elif reducer is median:
        value = median(values)
    else:
        error_message = f"Unsupported reducer: {reducer!r}"
        raise ValueError(error_message)
    return f"{float(value):.4f}"



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



def main() -> None:
    """Run the experiment from the repository root."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    script_path = Path(__file__).resolve()
    experiment_dir = script_path.parent
    repo_root = experiment_dir.parent.parent
    question_dir = repo_root / "experiments" / "00_QUESTIONS" / "Q1"
    artifacts = ExperimentArtifacts(
        markdown_path=experiment_dir / "generated_q1_retrieve_document_routing.md",
        json_path=experiment_dir / "generated_q1_retrieve_document_routing.json",
    )
    experiment = RetrieveDocumentRoutingExperiment(
        repo_root=repo_root,
        question_dir=question_dir,
        artifacts=artifacts,
    )
    _, _, markdown = experiment.run()
    sys.stdout.write(markdown)


if __name__ == "__main__":
    main()
