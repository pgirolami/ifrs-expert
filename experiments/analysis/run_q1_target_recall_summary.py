"""Run retrieve for each Q1 variant and summarize target-document recall.

This script evaluates one retrieval policy against the full Q1 variant set and
writes both raw per-question retrieve JSON payloads and a compact summary.

It is meant to be reusable for later tests and evals.

Usage:
    uv run python experiments/analysis/run_q1_target_recall_summary.py \
        --policy-config config/policy.default.yaml
"""

from __future__ import annotations

import argparse
import json
import logging
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)

DEFAULT_QUESTION_DIR = "experiments/00_QUESTIONS/Q1"
DEFAULT_POLICY_CONFIG = "config/policy.default.yaml"
DEFAULT_OUTPUT_DIRNAME = "generated_q1_target_recall_summary"
DEFAULT_TARGET_DOC_UIDS: tuple[str, ...] = ("ias39", "ifrs9", "ifric16")


@dataclass(frozen=True)
class QuestionCase:
    """One Q1 question variant to run through retrieve."""

    question_id: str
    question_text: str
    source_path: Path


@dataclass(frozen=True)
class RetrievedDocument:
    """One unique retrieved document for a question."""

    doc_uid: str
    document_type: str
    score: float
    rank: int


@dataclass(frozen=True)
class QuestionSummary:
    """Summary metrics for one question variant."""

    question_id: str
    document_hit_count: int
    target_ranks: dict[str, int | None]
    target_scores: dict[str, float | None]
    target_present: dict[str, bool]
    document_hits: list[str]


class Q1TargetRecallSummaryExperiment:
    """Run retrieve for every Q1 variant and summarize target recall."""

    def __init__(
        self,
        repo_root: Path,
        question_dir: Path,
        policy_config_path: Path,
        output_dir: Path,
        target_doc_uids: tuple[str, ...],
    ) -> None:
        self._repo_root = repo_root
        self._question_dir = question_dir
        self._policy_config_path = policy_config_path
        self._output_dir = output_dir
        self._target_doc_uids = target_doc_uids
        self._runs_dir = output_dir / "runs"
        self._raw_dir = self._runs_dir / policy_config_path.stem

    def run(self) -> dict[str, object]:
        questions = self._load_questions()
        summaries = [self._run_question(question) for question in questions]
        summary_payload = self._build_summary_payload(summaries)
        self._write_outputs(summary_payload, summaries)
        logger.info(f"Wrote target recall summary to {self._output_dir}")
        return summary_payload

    def _load_questions(self) -> list[QuestionCase]:
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

    def _run_question(self, question: QuestionCase) -> QuestionSummary:
        logger.info(f"Running retrieve for {question.question_id} using policy {self._policy_config_path}")
        completed_process = subprocess.run(  # noqa: S603
            (
                "uv",
                "run",
                "python",
                "-m",
                "src.cli",
                "retrieve",
                "--policy-config",
                str(self._policy_config_path),
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
            logger.error(f"retrieve failed for {question.question_id} with return code {completed_process.returncode}: {stderr_text}")
            message = f"retrieve failed for {question.question_id}: {stderr_text}"
            raise RuntimeError(message)

        raw_output = completed_process.stdout
        self._raw_dir.mkdir(parents=True, exist_ok=True)
        raw_output_path = self._raw_dir / f"{question.question_id}.retrieve.json"
        raw_output_path.write_text(raw_output, encoding="utf-8")

        try:
            payload = json.loads(raw_output)
        except json.JSONDecodeError as error:
            logger.exception(f"Could not parse retrieve JSON for {question.question_id}")
            message = f"Invalid JSON output for {question.question_id}"
            raise RuntimeError(message) from error

        hits_payload = payload.get("document_hits")
        if not isinstance(hits_payload, list):
            message = f"Expected document_hits list for {question.question_id}, got: {payload!r}"
            raise TypeError(message)

        document_hits: list[RetrievedDocument] = []
        hits_by_doc_uid: dict[str, RetrievedDocument] = {}
        for rank, raw_hit in enumerate(hits_payload, start=1):
            hit = _parse_retrieved_document(raw_hit, rank=rank)
            if hit.doc_uid in hits_by_doc_uid:
                logger.warning(f"Duplicate retrieved document for {question.question_id}: {hit.doc_uid}; keeping first occurrence")
                continue
            hits_by_doc_uid[hit.doc_uid] = hit
            document_hits.append(hit)

        target_ranks: dict[str, int | None] = {}
        target_scores: dict[str, float | None] = {}
        target_present: dict[str, bool] = {}
        for target_doc_uid in self._target_doc_uids:
            hit = hits_by_doc_uid.get(target_doc_uid)
            if hit is None:
                target_ranks[target_doc_uid] = None
                target_scores[target_doc_uid] = None
                target_present[target_doc_uid] = False
                continue
            target_ranks[target_doc_uid] = hit.rank
            target_scores[target_doc_uid] = hit.score
            target_present[target_doc_uid] = True

        logger.info(f"Received {len(document_hits)} unique document hit(s) for {question.question_id}")
        return QuestionSummary(
            question_id=question.question_id,
            document_hit_count=len(document_hits),
            target_ranks=target_ranks,
            target_scores=target_scores,
            target_present=target_present,
            document_hits=[hit.doc_uid for hit in document_hits],
        )

    def _build_summary_payload(self, summaries: list[QuestionSummary]) -> dict[str, object]:
        question_count = len(summaries)
        all_targets_present_count = sum(1 for summary in summaries if all(summary.target_present.values()))
        total_document_hits = sum(summary.document_hit_count for summary in summaries)
        average_document_hits = total_document_hits / question_count if question_count else 0.0
        max_document_hits = max((summary.document_hit_count for summary in summaries), default=0)

        target_presence = {
            target_doc_uid: sum(1 for summary in summaries if summary.target_present[target_doc_uid])
            for target_doc_uid in self._target_doc_uids
        }
        target_mean_rank = {
            target_doc_uid: _mean(
                summary.target_ranks[target_doc_uid]
                for summary in summaries
                if summary.target_ranks[target_doc_uid] is not None
            )
            for target_doc_uid in self._target_doc_uids
        }
        target_max_rank = {
            target_doc_uid: max(
                (summary.target_ranks[target_doc_uid] for summary in summaries if summary.target_ranks[target_doc_uid] is not None),
                default=0,
            )
            for target_doc_uid in self._target_doc_uids
        }

        return {
            "policy_config": str(self._policy_config_path),
            "question_count": question_count,
            "all_targets_present_count": all_targets_present_count,
            "target_doc_uids": list(self._target_doc_uids),
            "target_presence": target_presence,
            "average_document_hits": average_document_hits,
            "max_document_hits": max_document_hits,
            "target_mean_rank": target_mean_rank,
            "target_max_rank": target_max_rank,
            "questions": [
                {
                    "question_id": summary.question_id,
                    "document_hit_count": summary.document_hit_count,
                    "target_ranks": summary.target_ranks,
                    "target_scores": summary.target_scores,
                    "target_present": summary.target_present,
                    "document_hits": summary.document_hits,
                }
                for summary in summaries
            ],
        }

    def _write_outputs(self, summary_payload: dict[str, object], summaries: list[QuestionSummary]) -> None:
        self._output_dir.mkdir(parents=True, exist_ok=True)
        self._runs_dir.mkdir(parents=True, exist_ok=True)

        summary_json_path = self._output_dir / "summary.json"
        summary_json_path.write_text(json.dumps(summary_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        summary_markdown = self._build_summary_markdown(summary_payload, summaries)
        summary_md_path = self._output_dir / "summary.md"
        summary_md_path.write_text(summary_markdown, encoding="utf-8")

    def _build_summary_markdown(self, summary_payload: dict[str, object], summaries: list[QuestionSummary]) -> str:
        question_count = int(summary_payload["question_count"])
        all_targets_present_count = int(summary_payload["all_targets_present_count"])
        average_document_hits = float(summary_payload["average_document_hits"])
        max_document_hits = int(summary_payload["max_document_hits"])
        target_presence = summary_payload["target_presence"]
        target_mean_rank = summary_payload["target_mean_rank"]
        target_max_rank = summary_payload["target_max_rank"]

        lines = [
            f"# Q1 target recall summary for `{self._policy_config_path}`",
            "",
            f"- Questions: {question_count}",
            f"- All targets present together: {all_targets_present_count} / {question_count}",
            f"- Average document hits: {average_document_hits:.2f}",
            f"- Max document hits: {max_document_hits}",
            "",
            "## Target coverage",
            "",
            "| Target | Present | Mean rank | Max rank |",
            "| --- | ---: | ---: | ---: |",
        ]

        for target_doc_uid in self._target_doc_uids:
            present_count = int(target_presence[target_doc_uid])
            mean_rank = target_mean_rank[target_doc_uid]
            max_rank = target_max_rank[target_doc_uid]
            mean_rank_text = f"{mean_rank:.2f}" if mean_rank is not None else "-"
            lines.append(f"| {target_doc_uid} | {present_count} | {mean_rank_text} | {max_rank} |")

        lines.extend([
            "",
            "## Per-question summary",
            "",
            "| Question | Hits | Targets present | Target ranks |",
            "| --- | ---: | --- | --- |",
        ])

        for summary in summaries:
            target_present_text = ", ".join(
                target_doc_uid for target_doc_uid in self._target_doc_uids if summary.target_present[target_doc_uid]
            )
            target_ranks_text = ", ".join(
                f"{target_doc_uid}:{summary.target_ranks[target_doc_uid]}"
                for target_doc_uid in self._target_doc_uids
            )
            lines.append(
                f"| {summary.question_id} | {summary.document_hit_count} | {target_present_text} | {target_ranks_text} |"
            )

        return "\n".join(lines) + "\n"


def _parse_retrieved_document(payload: object, *, rank: int) -> RetrievedDocument:
    if not isinstance(payload, dict):
        message = f"Expected document hit dict, got: {payload!r}"
        raise TypeError(message)

    doc_uid = payload.get("doc_uid")
    document_type = payload.get("document_type")
    score = payload.get("score")
    if not isinstance(doc_uid, str):
        message = f"Expected doc_uid string, got: {payload!r}"
        raise TypeError(message)
    if not isinstance(document_type, str):
        message = f"Expected document_type string, got: {payload!r}"
        raise TypeError(message)
    if not isinstance(score, int | float):
        message = f"Expected numeric score, got: {payload!r}"
        raise TypeError(message)

    return RetrievedDocument(doc_uid=doc_uid, document_type=document_type, score=float(score), rank=rank)


def _question_sort_key(path: Path) -> tuple[int, str]:
    suffix = path.stem.removeprefix("Q1.")
    if suffix.isdigit():
        return (int(suffix), path.name)
    return (10**9, path.name)


def _mean(values: object) -> float | None:
    numeric_values = [float(value) for value in values if isinstance(value, int | float)]
    if not numeric_values:
        return None
    return sum(numeric_values) / len(numeric_values)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run retrieve on each Q1 variant and summarize target recall")
    parser.add_argument(
        "--question-dir",
        type=Path,
        default=None,
        help=f"Directory containing Q1 question variants (default: {DEFAULT_QUESTION_DIR})",
    )
    parser.add_argument(
        "--policy-config",
        type=Path,
        default=None,
        help=f"Retrieval policy config path (default: {DEFAULT_POLICY_CONFIG})",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=f"Output directory (default: {DEFAULT_OUTPUT_DIRNAME} next to this script)",
    )
    parser.add_argument(
        "--target-doc-uids",
        nargs="+",
        default=DEFAULT_TARGET_DOC_UIDS,
        help="Document UIDs to track in the summary.",
    )
    return parser


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    args = _build_parser().parse_args()

    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent
    question_dir = args.question_dir or (repo_root / DEFAULT_QUESTION_DIR)
    policy_config_path = args.policy_config or (repo_root / DEFAULT_POLICY_CONFIG)
    output_dir = args.output_dir or (script_dir / DEFAULT_OUTPUT_DIRNAME / policy_config_path.stem)

    experiment = Q1TargetRecallSummaryExperiment(
        repo_root=repo_root,
        question_dir=question_dir,
        policy_config_path=policy_config_path,
        output_dir=output_dir,
        target_doc_uids=tuple(args.target_doc_uids),
    )
    summary_payload = experiment.run()
    sys.stdout.write(json.dumps(summary_payload, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
