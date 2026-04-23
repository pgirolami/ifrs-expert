"""Run `retrieve` for each Q1 question variant and build a target matrix.

The script executes the CLI on every `Q1.*.txt` file under a question
folder such as `experiments/00_QUESTIONS/Q1` or `experiments/00_QUESTIONS/Q1en`,
collects the retrieved documents, and emits a markdown table with:

- one row per question variant
- a `Total` column with the number of unique documents retrieved for that
  question
- one column per retrieved document, ordered by how many questions retrieved
  it
- a final `Total` row with per-document coverage counts and score ranges

Usage:
    uv run python experiments/analysis/run_q1_retrieve_target_matrix.py
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

DEFAULT_OUTPUT_FILENAME = "generated_q1_retrieve_target_matrix.md"
DEFAULT_POLICY_CONFIG = "config/policy.default.yaml"


@dataclass(frozen=True)
class QuestionCase:
    """One Q1 question variant to run through retrieve."""

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
    """One document column in the markdown matrix."""

    doc_uid: str
    display_label: str
    question_count: int
    score_min: float
    score_max: float


class Q1RetrieveTargetMatrixExperiment:
    """Run retrieve for every Q1 variant and build a markdown table."""

    def __init__(
        self,
        repo_root: Path,
        question_dir: Path,
        output_path: Path,
        retrieve_command: tuple[str, ...],
        priority_doc_uids: tuple[str, ...] = (),
    ) -> None:
        """Initialize the experiment runner."""
        self._repo_root = repo_root
        self._question_dir = question_dir
        self._output_path = output_path
        self._retrieve_command = retrieve_command
        self._priority_doc_uids = _normalize_priority_doc_uids(list(priority_doc_uids))

    def run(self) -> str:
        """Run all questions, write the markdown artifact, and return it."""
        questions = self._load_questions()
        results = [self._run_question(question) for question in questions]
        columns = self._build_columns(results)
        markdown = self._build_markdown(results, columns)
        self._output_path.parent.mkdir(parents=True, exist_ok=True)
        self._output_path.write_text(markdown, encoding="utf-8")
        logger.info(f"Wrote target matrix to {self._output_path}")
        return markdown

    def _load_questions(self) -> list[QuestionCase]:
        """Load every `Q1.*.txt` question in numeric order."""
        question_paths = sorted(self._question_dir.glob("Q1.*.txt"), key=_question_sort_key)
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
            message = f"No Q1 question files found in {self._question_dir}"
            raise FileNotFoundError(message)
        logger.info(f"Loaded {len(questions)} Q1 question(s) from {self._question_dir}")
        return questions

    def _run_question(self, question: QuestionCase) -> QuestionResult:
        """Run the retrieve CLI for one question variant."""
        logger.info(f"Running retrieve for {question.question_id} from {question.source_path.name}")
        completed_process = subprocess.run(  # noqa: S603
            self._retrieve_command,
            cwd=self._repo_root,
            input=question.question_text,
            text=True,
            capture_output=True,
            check=False,
        )
        if completed_process.returncode != 0:
            stderr_text = completed_process.stderr.strip()
            logger.error(f"retrieve failed for {question.question_id} with return code {completed_process.returncode}: {stderr_text}")
            message = f"retrieve failed for {question.question_id}: {stderr_text}"
            raise RuntimeError(message)

        try:
            payload = json.loads(completed_process.stdout)
        except json.JSONDecodeError as error:
            logger.exception(f"Could not parse retrieve JSON for {question.question_id}")
            message = f"Invalid JSON output for {question.question_id}"
            raise RuntimeError(message) from error

        hits_payload = payload.get("document_hits")
        if not isinstance(hits_payload, list):
            message = f"Expected document_hits list for {question.question_id}, got: {payload!r}"
            raise TypeError(message)

        hits_by_doc_uid: dict[str, RetrievedDocument] = {}
        for rank, raw_hit in enumerate(hits_payload, start=1):
            hit = _parse_retrieved_document(raw_hit, rank=rank)
            if hit.doc_uid in hits_by_doc_uid:
                logger.warning(f"Duplicate retrieved document for {question.question_id}: {hit.doc_uid}; keeping first occurrence")
                continue
            hits_by_doc_uid[hit.doc_uid] = hit

        logger.info(f"Received {len(hits_by_doc_uid)} unique document hit(s) for {question.question_id}")
        return QuestionResult(question_id=question.question_id, hits_by_doc_uid=hits_by_doc_uid)

    def _build_columns(self, results: list[QuestionResult]) -> list[DocumentColumn]:
        """Build document columns ordered by question coverage, then label."""
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
        priority_columns = [column for priority_doc_uid in self._priority_doc_uids for column in columns if column.doc_uid == priority_doc_uid]
        remaining_columns = [column for column in columns if column.doc_uid not in self._priority_doc_uids]
        remaining_columns.sort(key=lambda column: (-column.question_count, column.display_label, column.doc_uid))
        columns = [*priority_columns, *remaining_columns]
        logger.info(f"Built {len(columns)} document column(s) for the target matrix")
        return columns

    def _build_markdown(self, results: list[QuestionResult], columns: list[DocumentColumn]) -> str:
        """Build the markdown table."""
        header_cells = ["Total", "Question", *[column.display_label for column in columns]]
        separator_cells = ["---:", "---", *["---:" for _ in columns]]
        lines = [
            "| " + " | ".join(header_cells) + " |",
            "| " + " | ".join(separator_cells) + " |",
        ]

        for result in results:
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


LIGHT_RED_RGB: tuple[int, int, int] = (248, 215, 218)
LIGHT_GREEN_RGB: tuple[int, int, int] = (212, 237, 218)


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


def _normalize_priority_doc_uids(raw_values: list[str]) -> tuple[str, ...]:
    """Normalize priority doc UID CLI values while preserving input order."""
    doc_uids: list[str] = []
    seen_doc_uids: set[str] = set()
    for raw_value in raw_values:
        for candidate in raw_value.split(","):
            normalized_candidate = candidate.strip()
            if not normalized_candidate or normalized_candidate in seen_doc_uids:
                continue
            seen_doc_uids.add(normalized_candidate)
            doc_uids.append(normalized_candidate)
    return tuple(doc_uids)


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


def _build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser for the analysis script."""
    parser = argparse.ArgumentParser(description="Run retrieve on each Q1 question variant")
    parser.add_argument(
        "--question-dir",
        type=Path,
        default=None,
        help="Directory containing Q1 question variants (default: experiments/00_QUESTIONS/Q1)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help=f"Markdown output path (default: {DEFAULT_OUTPUT_FILENAME} next to this script)",
    )
    parser.add_argument(
        "--policy-config",
        type=Path,
        default=None,
        help=f"Retrieval policy config path (default: {DEFAULT_POLICY_CONFIG})",
    )
    parser.add_argument(
        "--priority-doc-uids",
        nargs="+",
        default=(),
        help="Document UIDs to place first. Accepts space-separated values and comma-separated lists.",
    )
    return parser


def main() -> None:
    """Run the experiment from the repository root."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()

    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent
    question_dir = args.question_dir or (repo_root / "experiments" / "00_QUESTIONS" / "Q1")
    output_path = args.output or (script_dir / DEFAULT_OUTPUT_FILENAME)
    policy_config_path = args.policy_config or (repo_root / DEFAULT_POLICY_CONFIG)
    retrieve_command = (
        "uv",
        "run",
        "python",
        "-m",
        "src.cli",
        "retrieve",
        "--policy-config",
        str(policy_config_path),
        "--json",
    )

    experiment = Q1RetrieveTargetMatrixExperiment(
        repo_root=repo_root,
        question_dir=question_dir,
        output_path=output_path,
        retrieve_command=retrieve_command,
        priority_doc_uids=_normalize_priority_doc_uids(args.priority_doc_uids),
    )
    markdown = experiment.run()
    if args.output is None:
        sys.stdout.write(markdown)


if __name__ == "__main__":
    main()
