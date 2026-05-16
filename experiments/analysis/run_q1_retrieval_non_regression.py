"""Run Q1 retrieval non-regression checks and emit deterministic diagnostics.

This script is the retrieval-side companion to the Promptfoo harness. It does
not call any LLM. Instead it executes `src.cli retrieve --json` directly for
the configured Q1 question variants and computes:

- hard-gate style recall@K checks for the required authorities
- all-targets-in-top-K rate
- mean rank per target authority
- average and max returned document counts
- MRR

The fixture file defines the common Q1 authorities and the scenario arms:
- `authority_gate` for the absolute enriched-policy gate
- `glossary_sentinel` for raw vs enriched comparison

Usage:
    uv run python experiments/analysis/run_q1_retrieval_non_regression.py
"""

from __future__ import annotations

import argparse
import json
import logging
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import yaml

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.models.document import resolve_document_type_from_doc_uid
from src.retrieval.retrieval_contract import load_retrieve_contract_from_family_path

DEFAULT_FIXTURE_PATH = PROJECT_ROOT / "tests" / "fixtures" / "retrieval" / "q1_retrieval_non_regression.yaml"
DEFAULT_OUTPUT_DIRNAME = "generated_q1_retrieval_non_regression"
TOP_K_DEFAULT = 5

ScenarioMode = Literal["absolute", "comparison"]


@dataclass(frozen=True)
class AuthoritySpec:
    """One required target authority."""

    doc_uid: str
    label: str
    document_type: str


@dataclass(frozen=True)
class RetrievalArmSpec:
    """One retrieval policy arm inside a scenario."""

    label: str
    policy_config_path: Path
    retrieval_policy: str


@dataclass(frozen=True)
class ScenarioSpec:
    """One non-regression scenario from the fixture."""

    scenario_id: str
    mode: ScenarioMode
    arms: tuple[RetrievalArmSpec, ...]


@dataclass(frozen=True)
class RetrievalFixture:
    """Parsed Q1 retrieval fixture."""

    family_id: str
    question_dir: Path
    authorities: tuple[AuthoritySpec, ...]
    scenarios: tuple[ScenarioSpec, ...]


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
class QuestionResult:
    """The retrieval results for one question variant."""

    question_id: str
    document_hit_count: int
    target_ranks: dict[str, int | None]
    target_present: dict[str, bool]
    best_target_rank: int | None
    reciprocal_rank: float
    document_hits: list[str]


@dataclass(frozen=True)
class ArmSummary:
    """Aggregate metrics for one retrieval arm."""

    label: str
    question_count: int
    top_k: int
    all_targets_in_top_k_count: int
    average_document_hits: float
    max_document_hits: int
    target_recall_at_k: dict[str, float]
    target_mean_rank: dict[str, float | None]
    mrr: float


@dataclass(frozen=True)
class ScenarioReport:
    """Computed metrics and pass/fail state for one scenario."""

    scenario_id: str
    mode: ScenarioMode
    arms: tuple[ArmSummary, ...]
    passed: bool
    failures: tuple[str, ...]


def _load_fixture(path: Path) -> RetrievalFixture:
    """Load the YAML fixture file from disk."""
    raw_data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw_data, dict):
        raise TypeError(f"{path}: expected a mapping")

    family_id = _require_str(raw_data.get("family_id"), context=f"{path}: family_id")
    common = _require_mapping(raw_data.get("common"), context=f"{path}: common")
    scenarios = _require_mapping(raw_data.get("scenarios"), context=f"{path}: scenarios")

    question_dir = _resolve_path(_require_str(common.get("question_dir"), context=f"{path}: common.question_dir"))
    family_contract = load_retrieve_contract_from_family_path(question_dir / "family.yaml")
    authorities = tuple(_parse_authority(doc_uid) for doc_uid in family_contract.required_documents)

    scenario_specs: list[ScenarioSpec] = []
    for scenario_id, scenario_payload in scenarios.items():
        if not isinstance(scenario_id, str):
            raise TypeError(f"{path}: scenario key must be a string")
        scenario_specs.append(_parse_scenario(scenario_id, scenario_payload, path=path))

    return RetrievalFixture(
        family_id=family_id,
        question_dir=question_dir,
        authorities=authorities,
        scenarios=tuple(scenario_specs),
    )


def _parse_authority(doc_uid: str) -> AuthoritySpec:
    document_type = resolve_document_type_from_doc_uid(doc_uid)
    if document_type is None:
        raise ValueError(f"Could not resolve document_type for required document {doc_uid}")
    return AuthoritySpec(
        doc_uid=doc_uid,
        label=_format_authority_label(doc_uid),
        document_type=document_type,
    )


def _parse_scenario(scenario_id: str, payload: object, *, path: Path) -> ScenarioSpec:
    mapping = _require_mapping(payload, context=f"{path}: scenarios.{scenario_id}")
    if scenario_id == "authority_gate":
        arm = RetrievalArmSpec(
            label=_require_str(mapping.get("label", "enriched"), context=f"{path}: scenarios.{scenario_id}.label"),
            policy_config_path=_resolve_path(_require_str(mapping.get("policy_config"), context=f"{path}: scenarios.{scenario_id}.policy_config")),
            retrieval_policy=_require_str(mapping.get("retrieval_policy"), context=f"{path}: scenarios.{scenario_id}.retrieval_policy"),
        )
        return ScenarioSpec(scenario_id=scenario_id, mode="absolute", arms=(arm,))

    if scenario_id == "glossary_sentinel":
        baseline = _require_mapping(mapping.get("baseline"), context=f"{path}: scenarios.{scenario_id}.baseline")
        candidate = _require_mapping(mapping.get("candidate"), context=f"{path}: scenarios.{scenario_id}.candidate")
        return ScenarioSpec(
            scenario_id=scenario_id,
            mode="comparison",
            arms=(
                RetrievalArmSpec(
                    label=_require_str(baseline.get("label"), context=f"{path}: scenarios.{scenario_id}.baseline.label"),
                    policy_config_path=_resolve_path(_require_str(baseline.get("policy_config"), context=f"{path}: scenarios.{scenario_id}.baseline.policy_config")),
                    retrieval_policy=_require_str(baseline.get("retrieval_policy"), context=f"{path}: scenarios.{scenario_id}.baseline.retrieval_policy"),
                ),
                RetrievalArmSpec(
                    label=_require_str(candidate.get("label"), context=f"{path}: scenarios.{scenario_id}.candidate.label"),
                    policy_config_path=_resolve_path(_require_str(candidate.get("policy_config"), context=f"{path}: scenarios.{scenario_id}.candidate.policy_config")),
                    retrieval_policy=_require_str(candidate.get("retrieval_policy"), context=f"{path}: scenarios.{scenario_id}.candidate.retrieval_policy"),
                ),
            ),
        )

    raise ValueError(f"{path}: unsupported scenario: {scenario_id}")


def _load_questions(question_dir: Path) -> list[QuestionCase]:
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
        raise FileNotFoundError(f"No Q1 question files found in {question_dir}")
    logger.info(f"Loaded {len(questions)} question(s) from {question_dir}")
    return questions


def _run_retrieve(question: QuestionCase, arm: RetrievalArmSpec) -> tuple[int, str]:
    """Run the real retrieval pipeline and capture stdout."""
    logger.info(
        "Running retrieve for question_id=%s policy_config=%s retrieval_policy=%s",
        question.question_id,
        arm.policy_config_path,
        arm.retrieval_policy,
    )
    completed_process = subprocess.run(  # noqa: S603
        (
            "uv",
            "run",
            "python",
            "-m",
            "src.cli",
            "retrieve",
            "--policy-config",
            str(arm.policy_config_path),
            "--retrieval-policy",
            arm.retrieval_policy,
            "--json",
        ),
        cwd=PROJECT_ROOT,
        input=question.question_text,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed_process.returncode != 0:
        stderr_text = completed_process.stderr.strip() or completed_process.stdout.strip()
        raise RuntimeError(f"retrieve failed for {question.question_id}: {stderr_text}")
    stdout_text = completed_process.stdout.strip()
    if not stdout_text:
        raise RuntimeError(f"Empty retrieve output for {question.question_id}")
    return completed_process.returncode, stdout_text


def _parse_retrieved_document(payload: object, *, rank: int) -> RetrievedDocument:
    if not isinstance(payload, dict):
        raise TypeError(f"Expected document hit dict, got: {payload!r}")
    doc_uid = payload.get("doc_uid")
    document_type = payload.get("document_type")
    score = payload.get("score")
    if not isinstance(doc_uid, str):
        raise TypeError(f"Expected doc_uid string, got: {payload!r}")
    if not isinstance(document_type, str):
        raise TypeError(f"Expected document_type string, got: {payload!r}")
    if not isinstance(score, int | float):
        raise TypeError(f"Expected numeric score, got: {payload!r}")
    return RetrievedDocument(doc_uid=doc_uid, document_type=document_type, score=float(score), rank=rank)


def _run_question(
    question: QuestionCase,
    arm: RetrievalArmSpec,
    authorities: tuple[AuthoritySpec, ...],
    output_dir: Path,
) -> QuestionResult:
    """Run retrieve for one question/arm pair."""
    returncode, stdout_text = _run_retrieve(question, arm)
    del returncode

    output_dir.mkdir(parents=True, exist_ok=True)

    raw_path = output_dir / f"{question.question_id}.retrieve.json"
    raw_path.write_text(stdout_text, encoding="utf-8")

    payload = json.loads(stdout_text)
    hits_payload = payload.get("document_hits")
    if not isinstance(hits_payload, list):
        raise TypeError(f"Expected document_hits list for {question.question_id}, got: {payload!r}")

    hits_by_doc_uid: dict[str, RetrievedDocument] = {}
    ordered_hits: list[RetrievedDocument] = []
    for rank, raw_hit in enumerate(hits_payload, start=1):
        hit = _parse_retrieved_document(raw_hit, rank=rank)
        if hit.doc_uid in hits_by_doc_uid:
            logger.warning(
                "Duplicate retrieved document for question_id=%s arm=%s: %s; keeping first occurrence",
                question.question_id,
                arm.label,
                hit.doc_uid,
            )
            continue
        hits_by_doc_uid[hit.doc_uid] = hit
        ordered_hits.append(hit)

    target_ranks: dict[str, int | None] = {}
    target_present: dict[str, bool] = {}
    target_ranks_for_mrr: list[int] = []
    for authority in authorities:
        hit = hits_by_doc_uid.get(authority.doc_uid)
        if hit is None:
            target_ranks[authority.doc_uid] = None
            target_present[authority.doc_uid] = False
            continue
        target_ranks[authority.doc_uid] = hit.rank
        target_present[authority.doc_uid] = True
        target_ranks_for_mrr.append(hit.rank)

    best_target_rank = min(target_ranks_for_mrr) if target_ranks_for_mrr else None
    reciprocal_rank = 1.0 / best_target_rank if best_target_rank is not None else 0.0

    return QuestionResult(
        question_id=question.question_id,
        document_hit_count=len(ordered_hits),
        target_ranks=target_ranks,
        target_present=target_present,
        best_target_rank=best_target_rank,
        reciprocal_rank=reciprocal_rank,
        document_hits=[hit.doc_uid for hit in ordered_hits],
    )


def _run_arm(
    questions: list[QuestionCase],
    arm: RetrievalArmSpec,
    authorities: tuple[AuthoritySpec, ...],
    output_dir: Path,
    max_workers: int,
) -> list[QuestionResult]:
    """Run one retrieval arm across all questions."""
    arm_output_dir = output_dir / _slugify(arm.label)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(_run_question, question, arm, authorities, arm_output_dir) for question in questions]
        results = [future.result() for future in futures]

    return results


def _build_arm_summary(
    arm: RetrievalArmSpec,
    results: list[QuestionResult],
    authorities: tuple[AuthoritySpec, ...],
    top_k: int,
) -> ArmSummary:
    """Aggregate one retrieval arm into a deterministic summary."""
    question_count = len(results)
    if question_count == 0:
        raise ValueError(f"Cannot summarize empty result set for arm {arm.label}")

    all_targets_in_top_k_count = sum(1 for result in results if all((rank is not None and rank <= top_k) for rank in result.target_ranks.values()))
    average_document_hits = sum(result.document_hit_count for result in results) / question_count
    max_document_hits = max(result.document_hit_count for result in results)
    target_recall_at_k = {authority.doc_uid: sum(1 for result in results if result.target_ranks[authority.doc_uid] is not None and result.target_ranks[authority.doc_uid] <= top_k) / question_count for authority in authorities}
    target_mean_rank = {authority.doc_uid: _mean(result.target_ranks[authority.doc_uid] for result in results if result.target_ranks[authority.doc_uid] is not None) for authority in authorities}
    mrr = sum(result.reciprocal_rank for result in results) / question_count

    return ArmSummary(
        label=arm.label,
        question_count=question_count,
        top_k=top_k,
        all_targets_in_top_k_count=all_targets_in_top_k_count,
        average_document_hits=average_document_hits,
        max_document_hits=max_document_hits,
        target_recall_at_k=target_recall_at_k,
        target_mean_rank=target_mean_rank,
        mrr=mrr,
    )


def _build_report(
    fixture: RetrievalFixture,
    scenario_reports: list[ScenarioReport],
) -> dict[str, object]:
    """Build the JSON summary payload."""
    return {
        "family_id": fixture.family_id,
        "question_dir": str(fixture.question_dir),
        "top_k": TOP_K_DEFAULT,
        "target_authorities": [
            {
                "doc_uid": authority.doc_uid,
                "label": authority.label,
                "document_type": authority.document_type,
            }
            for authority in fixture.authorities
        ],
        "scenarios": [
            {
                "scenario_id": report.scenario_id,
                "mode": report.mode,
                "passed": report.passed,
                "failures": list(report.failures),
                "arms": [
                    {
                        "label": arm.label,
                        "question_count": arm.question_count,
                        "top_k": arm.top_k,
                        "all_targets_in_top_k_count": arm.all_targets_in_top_k_count,
                        "average_document_hits": arm.average_document_hits,
                        "max_document_hits": arm.max_document_hits,
                        "target_recall_at_k": arm.target_recall_at_k,
                        "target_mean_rank": arm.target_mean_rank,
                        "mrr": arm.mrr,
                    }
                    for arm in report.arms
                ],
            }
            for report in scenario_reports
        ],
    }


def _build_markdown(report: dict[str, object]) -> str:
    """Build a compact markdown summary."""
    lines = [f"# {report['family_id']} retrieval non-regression summary", ""]
    lines.append(f"- Question dir: `{report['question_dir']}`")
    lines.append(f"- Top K: {report['top_k']}")
    lines.append("")

    target_authorities = report["target_authorities"]
    scenarios = report["scenarios"]

    for scenario in scenarios:
        scenario_id = scenario["scenario_id"]
        mode = scenario["mode"]
        passed = "pass" if scenario["passed"] else "fail"
        lines.append(f"## {scenario_id} ({mode}, {passed})")
        lines.append("")
        for arm in scenario["arms"]:
            lines.append(f"### {arm['label']}")
            lines.append("")
            lines.append(
                f"- Questions: {arm['question_count']}, all-targets-in-top-K: {arm['all_targets_in_top_k_count']}/{arm['question_count']}, "
                f"avg docs: {arm['average_document_hits']:.2f}, max docs: {arm['max_document_hits']}, MRR: {arm['mrr']:.3f}"
            )
            lines.append("")
            lines.append("| Authority | Recall@K | Mean rank |")
            lines.append("| --- | ---: | ---: |")
            for authority in target_authorities:
                doc_uid = authority["doc_uid"]
                recall = arm["target_recall_at_k"][doc_uid]
                mean_rank = arm["target_mean_rank"][doc_uid]
                mean_rank_text = f"{mean_rank:.2f}" if mean_rank is not None else "-"
                lines.append(f"| {authority['label']} | {recall:.2%} | {mean_rank_text} |")
            lines.append("")
        if scenario["failures"]:
            lines.append("Failures:")
            for failure in scenario["failures"]:
                lines.append(f"- {failure}")
            lines.append("")

    return "\n".join(lines).strip() + "\n"


def _evaluate_scenario(
    fixture: RetrievalFixture,
    scenario: ScenarioSpec,
    questions: list[QuestionCase],
    output_dir: Path,
    max_workers: int,
) -> ScenarioReport:
    """Run one scenario and evaluate its pass/fail criteria."""
    arm_summaries: list[ArmSummary] = []
    failures: list[str] = []
    for arm in scenario.arms:
        results = _run_arm(
            questions=questions,
            arm=arm,
            authorities=fixture.authorities,
            output_dir=output_dir / scenario.scenario_id,
            max_workers=max_workers,
        )
        arm_summaries.append(_build_arm_summary(arm=arm, results=results, authorities=fixture.authorities, top_k=TOP_K_DEFAULT))

    if scenario.mode == "absolute":
        summary = arm_summaries[0]
        for authority in fixture.authorities:
            recall = summary.target_recall_at_k[authority.doc_uid]
            if recall < 1.0:
                failures.append(f"{authority.doc_uid} recall@{TOP_K_DEFAULT} = {recall:.3f} < 1.000")
        all_targets_rate = summary.all_targets_in_top_k_count / summary.question_count
        if all_targets_rate < 1.0:
            failures.append(f"all-targets-in-top-{TOP_K_DEFAULT} rate = {all_targets_rate:.3f} < 1.000")
    else:
        baseline_summary, candidate_summary = arm_summaries
        for authority in fixture.authorities:
            baseline_recall = baseline_summary.target_recall_at_k[authority.doc_uid]
            candidate_recall = candidate_summary.target_recall_at_k[authority.doc_uid]
            if candidate_recall + 1e-9 < baseline_recall:
                failures.append(f"{authority.doc_uid} recall@{TOP_K_DEFAULT} regressed: {candidate_recall:.3f} < {baseline_recall:.3f}")
        baseline_rate = baseline_summary.all_targets_in_top_k_count / baseline_summary.question_count
        candidate_rate = candidate_summary.all_targets_in_top_k_count / candidate_summary.question_count
        if candidate_rate + 1e-9 < baseline_rate:
            failures.append(f"all-targets-in-top-{TOP_K_DEFAULT} rate regressed: {candidate_rate:.3f} < {baseline_rate:.3f}")
        if candidate_summary.mrr + 1e-9 < baseline_summary.mrr:
            failures.append(f"MRR regressed: {candidate_summary.mrr:.3f} < {baseline_summary.mrr:.3f}")

    return ScenarioReport(
        scenario_id=scenario.scenario_id,
        mode=scenario.mode,
        arms=tuple(arm_summaries),
        passed=not failures,
        failures=tuple(failures),
    )


def _require_mapping(value: object, *, context: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise TypeError(f"{context}: expected a mapping")
    for key in value:
        if not isinstance(key, str):
            raise TypeError(f"{context}: expected string keys")
    return value


def _require_sequence(value: object, *, context: str) -> list[object]:
    if not isinstance(value, list):
        raise TypeError(f"{context}: expected a sequence")
    return value


def _require_str(value: object, *, context: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{context}: expected a string")
    return value


def _resolve_path(value: str) -> Path:
    """Resolve a repo-relative or absolute path."""
    path = Path(value)
    if path.is_absolute():
        return path
    return PROJECT_ROOT / path


def _mean(values: object) -> float | None:
    numeric_values = [float(value) for value in values if isinstance(value, int | float)]
    if not numeric_values:
        return None
    return sum(numeric_values) / len(numeric_values)


def _question_sort_key(path: Path) -> tuple[int, str]:
    suffix = path.stem.removeprefix("Q1.")
    if suffix.isdigit():
        return (int(suffix), path.name)
    return (10**9, path.name)


def _format_authority_label(doc_uid: str) -> str:
    prefix = []
    suffix = []
    for char in doc_uid:
        if char.isdigit():
            suffix.append(char)
        else:
            prefix.append(char.upper())
    if suffix:
        return f"{''.join(prefix)} {''.join(suffix)}"
    return "".join(prefix)


def _slugify(value: str) -> str:
    normalized = "".join(char.lower() if char.isalnum() else "-" for char in value).strip("-")
    while "--" in normalized:
        normalized = normalized.replace("--", "-")
    return normalized or "retrieval-arm"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description="Run Q1 retrieval non-regression checks")
    parser.add_argument(
        "--fixture",
        type=Path,
        default=DEFAULT_FIXTURE_PATH,
        help="Path to the Q1 retrieval fixture YAML file",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help=f"Directory for diagnostic artifacts. Defaults to {DEFAULT_OUTPUT_DIRNAME} under the fixture directory's experiment root.",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=8,
        help="Maximum number of concurrent retrieve subprocesses per arm",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run the retrieval non-regression suite."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    args = parse_args(argv)

    fixture = _load_fixture(args.fixture)

    output_dir = args.output_dir or (PROJECT_ROOT / "experiments" / DEFAULT_OUTPUT_DIRNAME)
    output_dir.mkdir(parents=True, exist_ok=True)

    questions = _load_questions(fixture.question_dir)

    scenario_reports = [_evaluate_scenario(fixture=fixture, scenario=scenario, questions=questions, output_dir=output_dir, max_workers=args.max_workers) for scenario in fixture.scenarios]
    report = _build_report(fixture, scenario_reports)
    (output_dir / "summary.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (output_dir / "summary.md").write_text(_build_markdown(report), encoding="utf-8")

    exit_code = 0 if all(scenario.passed for scenario in scenario_reports) else 1
    if exit_code != 0:
        logger.error("Retrieval non-regression checks failed")
    else:
        logger.info("Retrieval non-regression checks passed")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
