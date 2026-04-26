"""Canonical document-routing diagnostics contract and renderers."""

from __future__ import annotations

import hashlib
import json
import logging
import os
import sqlite3
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)

DEFAULT_RUNS_DIRNAME = "runs"
DEFAULT_DIAGNOSTICS_DIRNAME = "diagnostics"
DEFAULT_LAYER_DIRNAME = "document_routing"
DEFAULT_RUN_MD_FILENAME = "document_routing_diagnostics.md"
DEFAULT_RUN_JSON_FILENAME = "document_routing_diagnostics.json"
DEFAULT_INDEX_MD_FILENAME = "document_routing_index.md"
DEFAULT_INDEX_JSON_FILENAME = "document_routing_index.json"
DEFAULT_COMPARE_MD_FILENAME = "document_routing_comparison.md"
DEFAULT_COMPARE_JSON_FILENAME = "document_routing_comparison.json"
DEFAULT_RAW_DIRNAME = "raw"
DEFAULT_PROMPTFOO_DB_FILENAME = "promptfoo.db"
DEFAULT_PROMPTFOO_CONFIG_FILENAME = "promptfooconfig.yaml"
DEFAULT_RUN_METADATA_FILENAME = "run.json"
DEFAULT_SECTION_TITLE = "Document Routing Diagnostics"
LIGHT_RED_RGB: tuple[int, int, int] = (248, 215, 218)
LIGHT_GREEN_RGB: tuple[int, int, int] = (212, 237, 218)


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
class DocumentHit:
    """One retrieved document."""

    doc_uid: str
    display_label: str
    rank: int
    score: float
    document_type: str | None
    document_kind: str | None


@dataclass(frozen=True)
class QuestionDiagnostics:
    """Diagnostics for one question."""

    question_id: str
    run_id: str
    question_path: Path
    question_text_sha256: str
    document_hits: tuple[DocumentHit, ...]
    selected_document: str | None
    selected_rank: int | None
    selected_score: float | None
    in_candidate_set: bool | None
    candidate_count: int
    target_documents_present: dict[str, bool]
    target_document_ranks: dict[str, int | None]
    target_document_scores: dict[str, float | None]


@dataclass(frozen=True)
class DocumentSummary:
    """Aggregate document coverage."""

    doc_uid: str
    display_label: str
    question_count: int
    present_count: int
    score_min: float | None
    score_max: float | None
    rank_min: int | None
    rank_max: int | None


@dataclass(frozen=True)
class RunDiagnostics:
    """One run-level diagnostics artifact."""

    experiment_name: str
    provider_name: str
    run_id: str
    generated_at: str
    promptfoo_db_path: str
    eval_id: str
    question_families: tuple[str, ...]
    question_sources: tuple[PromptfooTestCase, ...]
    question_ids: tuple[str, ...]
    policy_file: str
    effective_policy_file: str
    policy_name: str
    policy: dict[str, object]
    glossary_file: str | None
    effective_glossary_file: str | None
    target_documents: tuple[str, ...]
    rows: tuple[QuestionDiagnostics, ...]
    document_summaries: tuple[DocumentSummary, ...]

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
            "policy_file": self.policy_file,
            "effective_policy_file": self.effective_policy_file,
            "policy_name": self.policy_name,
            "policy": self.policy,
            "glossary_file": self.glossary_file,
            "effective_glossary_file": self.effective_glossary_file,
            "target_documents": list(self.target_documents),
            "rows": [self._row_to_json(row) for row in self.rows],
            "document_summaries": [self._summary_to_json(summary) for summary in self.document_summaries],
        }

    @staticmethod
    def _row_to_json(row: QuestionDiagnostics) -> dict[str, object]:
        return {
            "question_id": row.question_id,
            "run_id": row.run_id,
            "question_path": str(row.question_path),
            "question_text_sha256": row.question_text_sha256,
            "document_hits": [
                {
                    "doc_uid": hit.doc_uid,
                    "display_label": hit.display_label,
                    "rank": hit.rank,
                    "score": hit.score,
                    "document_type": hit.document_type,
                    "document_kind": hit.document_kind,
                }
                for hit in row.document_hits
            ],
            "selected_document": row.selected_document,
            "selected_rank": row.selected_rank,
            "selected_score": row.selected_score,
            "in_candidate_set": row.in_candidate_set,
            "candidate_count": row.candidate_count,
            "target_documents_present": row.target_documents_present,
            "target_document_ranks": row.target_document_ranks,
            "target_document_scores": row.target_document_scores,
        }

    @staticmethod
    def _summary_to_json(summary: DocumentSummary) -> dict[str, object]:
        return {
            "doc_uid": summary.doc_uid,
            "display_label": summary.display_label,
            "question_count": summary.question_count,
            "present_count": summary.present_count,
            "score_min": summary.score_min,
            "score_max": summary.score_max,
            "rank_min": summary.rank_min,
            "rank_max": summary.rank_max,
        }


@dataclass(frozen=True)
class ComparisonRow:
    """One comparison row."""

    question_id: str
    doc_uid: str
    display_label: str
    values_by_label: dict[str, dict[str, float | int | None]]


@dataclass(frozen=True)
class ComparisonDiagnostics:
    """Comparison artifact."""

    comparison_name: str
    generated_at: str
    input_labels: tuple[str, ...]
    target_documents: tuple[str, ...]
    rows: tuple[ComparisonRow, ...]

    def to_json(self) -> dict[str, object]:
        return {
            "comparison_name": self.comparison_name,
            "generated_at": self.generated_at,
            "input_labels": list(self.input_labels),
            "target_documents": list(self.target_documents),
            "rows": [
                {
                    "question_id": row.question_id,
                    "doc_uid": row.doc_uid,
                    "display_label": row.display_label,
                    "values_by_label": row.values_by_label,
                }
                for row in self.rows
            ],
        }


class DocumentRoutingDiagnosticsGenerator:
    """Generate run-level document-routing diagnostics."""

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
        question_sources = self._load_question_sources(promptfoo_config)
        target_documents = self._load_target_documents(question_sources)
        provider_name = self._load_provider_name(promptfoo_config)
        policy_name = self._load_policy_name(promptfoo_config)
        policy_file, effective_policy_file, policy = self._load_policy(promptfooconfig_path, promptfoo_config)
        glossary_file, effective_glossary_file = self._load_glossary(run_dir, run_metadata)
        rows = self._load_rows(
            promptfoo_db_path=promptfoo_db_path,
            eval_id=eval_id,
            run_id=run_dir.name,
            question_sources=question_sources,
            target_documents=target_documents,
        )
        summaries = self._build_columns(rows=rows, question_sources=question_sources)

        return RunDiagnostics(
            experiment_name=experiment_dir.name,
            provider_name=provider_name,
            run_id=run_dir.name,
            generated_at=datetime.now(tz=UTC).isoformat(),
            promptfoo_db_path=_path_text(promptfoo_db_path, self._repo_root),
            eval_id=eval_id,
            question_families=self._collect_question_families(question_sources),
            question_sources=tuple(question_sources),
            question_ids=tuple(source.question_id for source in question_sources),
            policy_file=_path_text(policy_file, self._repo_root),
            effective_policy_file=_path_text(effective_policy_file, self._repo_root),
            policy_name=policy_name,
            policy=policy,
            glossary_file=None if glossary_file is None else _path_text(glossary_file, self._repo_root),
            effective_glossary_file=None if effective_glossary_file is None else _path_text(effective_glossary_file, self._repo_root),
            target_documents=tuple(target_documents),
            rows=tuple(rows),
            document_summaries=tuple(summaries),
        )

    def write_run_artifacts(self, diagnostics: RunDiagnostics, output_dir: Path) -> None:
        output_dir.mkdir(parents=True, exist_ok=True)
        raw_dir = output_dir / DEFAULT_RAW_DIRNAME
        raw_dir.mkdir(parents=True, exist_ok=True)
        promptfoo_db_path = Path(diagnostics.promptfoo_db_path)
        if not promptfoo_db_path.is_absolute():
            promptfoo_db_path = self._repo_root / promptfoo_db_path
        self._write_raw_payloads(
            raw_dir=raw_dir,
            promptfoo_db_path=promptfoo_db_path,
            eval_id=diagnostics.eval_id,
            question_ids=tuple(row.question_id for row in diagnostics.rows),
        )
        (output_dir / DEFAULT_RUN_JSON_FILENAME).write_text(
            json.dumps(diagnostics.to_json(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        (output_dir / DEFAULT_RUN_MD_FILENAME).write_text(self.render_run_markdown(diagnostics), encoding="utf-8")

    def refresh_experiment_index(self, experiment_dir: Path) -> tuple[Path, Path]:
        index_root = experiment_dir / DEFAULT_DIAGNOSTICS_DIRNAME
        index_root.mkdir(parents=True, exist_ok=True)
        run_entries: list[dict[str, object]] = []
        run_outputs: list[tuple[Path, RunDiagnostics]] = []
        runs_dir = experiment_dir / DEFAULT_RUNS_DIRNAME
        if not runs_dir.exists():
            raise FileNotFoundError(f"Missing runs directory: {runs_dir}")
        for run_dir in sorted(runs_dir.iterdir(), key=lambda path: path.name):
            if not run_dir.is_dir():
                continue
            run_output_dir = run_dir / DEFAULT_DIAGNOSTICS_DIRNAME / DEFAULT_LAYER_DIRNAME
            json_path = run_output_dir / DEFAULT_RUN_JSON_FILENAME
            if not json_path.exists():
                continue
            run_data = _load_json_object(json_path)
            diagnostics = _run_diagnostics_from_json(run_data)
            run_entries.append(
                {
                    "run_id": diagnostics.run_id,
                    "provider_name": diagnostics.provider_name,
                    "policy_name": diagnostics.policy_name,
                    "output_dir": _path_text(run_output_dir, self._repo_root),
                    "markdown_path": _path_text(run_output_dir / DEFAULT_RUN_MD_FILENAME, self._repo_root),
                    "json_path": _path_text(json_path, self._repo_root),
                }
            )
            run_outputs.append((run_output_dir, diagnostics))

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

    def render_run_markdown(self, diagnostics: RunDiagnostics) -> str:
        return "\n".join(
            [
                "This table shows every document retrieved for each question. The target documents from the family file appear first after the question and total columns, and the remaining retrieved documents are ordered by how often they were retrieved across questions.",
                "",
                self._render_matrix_markdown(diagnostics),
            ]
        )

    def render_index_markdown(
        self,
        experiment_name: str,
        index_root: Path,
        run_outputs: list[tuple[Path, RunDiagnostics]],
    ) -> str:
        lines = [
            f"# {experiment_name} document routing diagnostics index",
            "",
            "| Run | Provider | Policy | Markdown | JSON |",
            "| --- | --- | --- | --- | --- |",
        ]
        for output_dir, diagnostics in run_outputs:
            markdown_path = output_dir / DEFAULT_RUN_MD_FILENAME
            json_path = output_dir / DEFAULT_RUN_JSON_FILENAME
            lines.append(
                "| "
                + " | ".join(
                    [
                        diagnostics.run_id,
                        diagnostics.provider_name,
                        diagnostics.policy_name,
                        f"[link]({os.path.relpath(markdown_path, start=index_root)})",
                        f"[link]({os.path.relpath(json_path, start=index_root)})",
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

    def _load_question_sources(self, promptfoo_config: dict[str, object]) -> list[PromptfooTestCase]:
        tests = _require_list(promptfoo_config.get("tests"), context="promptfooconfig.yaml: tests")
        question_sources: list[PromptfooTestCase] = []
        for index, test in enumerate(tests):
            test_mapping = _require_mapping(test, context=f"promptfooconfig.yaml: tests[{index}]")
            metadata = _require_mapping(test_mapping.get("metadata"), context=f"promptfooconfig.yaml: tests[{index}].metadata")
            family_id = _require_str(metadata.get("family"), context=f"promptfooconfig.yaml: tests[{index}].metadata.family")
            question_path = self._repo_root / _require_str(metadata.get("question_path"), context=f"promptfooconfig.yaml: tests[{index}].metadata.question_path")
            if not question_path.exists():
                raise FileNotFoundError(f"Question file not found: {question_path}")
            description = _require_str(test_mapping.get("description"), context=f"promptfooconfig.yaml: tests[{index}].description")
            question_sources.append(PromptfooTestCase(family_id=family_id, question_path=question_path, description=description))
        if not question_sources:
            raise LookupError("promptfooconfig.yaml did not define any tests")
        return question_sources

    def _load_target_documents(self, question_sources: list[PromptfooTestCase]) -> list[str]:
        target_documents: list[str] = []
        seen: set[str] = set()
        for source in question_sources:
            family_path = source.question_path.parent / "family.yaml"
            family_data = _load_yaml_object(family_path)
            assert_retrieve = _require_mapping(family_data.get("assert_retrieve"), context=f"{family_path}: assert_retrieve")
            required_documents = _require_list(assert_retrieve.get("required_documents"), context=f"{family_path}: assert_retrieve.required_documents")
            for item in required_documents:
                doc_uid = _require_str(item, context=f"{family_path}: required_documents[]").lower()
                if doc_uid in seen:
                    continue
                seen.add(doc_uid)
                target_documents.append(doc_uid)
        if not target_documents:
            raise LookupError("Could not load target documents from family.yaml")
        return target_documents

    def _load_provider_name(self, promptfoo_config: dict[str, object]) -> str:
        providers = _require_list(promptfoo_config.get("providers"), context="promptfooconfig.yaml: providers")
        provider = _require_mapping(providers[0], context="promptfooconfig.yaml: providers[0]")
        return _require_str(provider.get("label"), context="promptfooconfig.yaml: providers[0].label")

    def _load_policy_name(self, promptfoo_config: dict[str, object]) -> str:
        providers = _require_list(promptfoo_config.get("providers"), context="promptfooconfig.yaml: providers")
        provider = _require_mapping(providers[0], context="promptfooconfig.yaml: providers[0]")
        config = _require_mapping(provider.get("config"), context="promptfooconfig.yaml: providers[0].config")
        return _require_str(config.get("retrieval-policy"), context="promptfooconfig.yaml: providers[0].config.retrieval-policy")

    def _load_policy(self, promptfooconfig_path: Path, promptfoo_config: dict[str, object]) -> tuple[Path, Path, dict[str, object]]:
        providers = _require_list(promptfoo_config.get("providers"), context="promptfooconfig.yaml: providers")
        provider = _require_mapping(providers[0], context="promptfooconfig.yaml: providers[0]")
        config = _require_mapping(provider.get("config"), context="promptfooconfig.yaml: providers[0].config")
        policy_config = _require_str(config.get("policy-config"), context="promptfooconfig.yaml: providers[0].config.policy-config")
        policy_path = (promptfooconfig_path.parent / policy_config).resolve()
        if not policy_path.exists():
            raise FileNotFoundError(f"Policy file not found: {policy_path}")
        return policy_path, policy_path, _load_yaml_object(policy_path)

    def _load_glossary(self, run_dir: Path, run_metadata: dict[str, object]) -> tuple[Path | None, Path | None]:
        archived_artifacts = run_metadata.get("archived_artifacts")
        if isinstance(archived_artifacts, dict):
            glossary = archived_artifacts.get("glossary")
            if isinstance(glossary, dict):
                archived_path = glossary.get("archived_path")
                if isinstance(archived_path, str):
                    glossary_path = self._repo_root / archived_path
                    if glossary_path.exists():
                        return glossary_path, glossary_path
        effective_dir = run_dir / "effective"
        for candidate_name in ("glossary.yaml", "en-fr-glossary.yaml", "en-fr-glossary_issues.yaml"):
            candidate = effective_dir / candidate_name
            if candidate.exists():
                return candidate, candidate
        fallback = self._repo_root / "config" / "en-fr-glossary.yaml"
        if fallback.exists():
            logger.warning(f"Glossary file not archived in {run_dir.name}; falling back to {fallback}")
            return fallback, fallback
        return None, None

    def _load_rows(
        self,
        *,
        promptfoo_db_path: Path,
        eval_id: str,
        run_id: str,
        question_sources: list[PromptfooTestCase],
        target_documents: list[str],
    ) -> list[QuestionDiagnostics]:
        rows: list[QuestionDiagnostics] = []
        results = self._load_eval_results(promptfoo_db_path, eval_id)
        for test_idx, source in enumerate(question_sources):
            result_row = results.get(test_idx)
            if result_row is None:
                raise LookupError(f"Missing Promptfoo result for test_idx={test_idx}")
            raw_payload = _parse_promptfoo_response(result_row["response"])
            document_hits = _parse_document_hits(raw_payload)
            target_present: dict[str, bool] = {}
            target_ranks: dict[str, int | None] = {}
            target_scores: dict[str, float | None] = {}
            for doc_uid in target_documents:
                hit = next((item for item in document_hits if item.doc_uid == doc_uid), None)
                target_present[doc_uid] = hit is not None
                target_ranks[doc_uid] = None if hit is None else hit.rank
                target_scores[doc_uid] = None if hit is None else hit.score
            rows.append(
                QuestionDiagnostics(
                    question_id=source.question_id,
                    run_id=run_id,
                    question_path=source.question_path,
                    question_text_sha256=_sha256_text(source.question_path.read_text(encoding="utf-8")),
                    document_hits=document_hits,
                    selected_document=None,
                    selected_rank=None,
                    selected_score=None,
                    in_candidate_set=None,
                    candidate_count=len(document_hits),
                    target_documents_present=target_present,
                    target_document_ranks=target_ranks,
                    target_document_scores=target_scores,
                )
            )
        return rows

    def _load_eval_results(self, promptfoo_db_path: Path, eval_id: str) -> dict[int, sqlite3.Row]:
        with sqlite3.connect(promptfoo_db_path) as conn:
            conn.row_factory = sqlite3.Row
            result_rows = conn.execute(
                "SELECT test_idx, response FROM eval_results WHERE eval_id = ? ORDER BY test_idx, prompt_idx",
                (eval_id,),
            ).fetchall()
        rows_by_test_idx: dict[int, sqlite3.Row] = {}
        for row in result_rows:
            test_idx = row["test_idx"]
            if not isinstance(test_idx, int):
                raise TypeError("Expected integer test_idx")
            rows_by_test_idx[test_idx] = row
        return rows_by_test_idx

    def _write_raw_payloads(self, raw_dir: Path, promptfoo_db_path: Path, eval_id: str, question_ids: tuple[str, ...]) -> None:
        results = self._load_eval_results(promptfoo_db_path, eval_id)
        for test_idx, question_id in enumerate(question_ids):
            result_row = results.get(test_idx)
            if result_row is None:
                continue
            raw_payload = _parse_promptfoo_response(result_row["response"])
            (raw_dir / f"{question_id}.retrieve.json").write_text(
                json.dumps(raw_payload, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

    def _render_matrix_markdown(self, diagnostics: RunDiagnostics) -> str:
        columns = self._build_columns(rows=diagnostics.rows, question_sources=diagnostics.question_sources)
        header_cells = ["Question", "Total", *[column.display_label for column in columns]]
        separator_cells = ["---", "---:", *["---:" for _ in columns]]
        lines = ["| " + " | ".join(header_cells) + " |", "| " + " | ".join(separator_cells) + " |"]
        for row in sorted(diagnostics.rows, key=lambda item: _question_sort_key(item.question_id)):
            row_cells = [row.question_id, str(row.candidate_count)]
            hits_by_doc_uid = {hit.doc_uid: hit for hit in row.document_hits}
            for column in columns:
                hit = hits_by_doc_uid.get(column.doc_uid)
                rank = None if hit is None else hit.rank
                score = None if hit is None else hit.score
                row_cells.append("" if rank is None or score is None else _format_ranked_score_cell(score, rank, row.candidate_count))
            lines.append("| " + " | ".join(row_cells) + " |")
        total_cells = ["", "Total"]
        for column in columns:
            if column.score_min is None or column.score_max is None:
                total_cells.append("")
                continue
            total_cells.append(f"{column.present_count} ({column.score_min:.2f}-{column.score_max:.2f})")
        lines.append("| " + " | ".join(total_cells) + " |")
        return "\n".join(lines)

    def _build_columns(
        self,
        *,
        rows: tuple[QuestionDiagnostics, ...] | list[QuestionDiagnostics],
        question_sources: tuple[PromptfooTestCase, ...],
    ) -> list[DocumentSummary]:
        scores_by_doc_uid: dict[str, list[float]] = {}
        ranks_by_doc_uid: dict[str, list[int]] = {}
        labels_by_doc_uid: dict[str, str] = {}
        for row in rows:
            for hit in row.document_hits:
                scores_by_doc_uid.setdefault(hit.doc_uid, []).append(hit.score)
                ranks_by_doc_uid.setdefault(hit.doc_uid, []).append(hit.rank)
                labels_by_doc_uid.setdefault(hit.doc_uid, hit.display_label)

        columns_by_doc_uid: dict[str, DocumentSummary] = {}
        for doc_uid, scores in scores_by_doc_uid.items():
            ranks = ranks_by_doc_uid[doc_uid]
            columns_by_doc_uid[doc_uid] = DocumentSummary(
                doc_uid=doc_uid,
                display_label=labels_by_doc_uid[doc_uid],
                question_count=len(rows),
                present_count=len(scores),
                score_min=min(scores),
                score_max=max(scores),
                rank_min=min(ranks),
                rank_max=max(ranks),
            )

        ordered_doc_uids = self._ordered_doc_uids_from_families(question_sources)
        ordered_columns: list[DocumentSummary] = []
        seen_doc_uids: set[str] = set()
        for doc_uid in ordered_doc_uids:
            column = columns_by_doc_uid.get(doc_uid)
            if column is None:
                continue
            ordered_columns.append(column)
            seen_doc_uids.add(doc_uid)

        remaining_columns = [column for doc_uid, column in columns_by_doc_uid.items() if doc_uid not in seen_doc_uids]
        remaining_columns.sort(key=lambda column: (-column.present_count, column.display_label, column.doc_uid))
        ordered_columns.extend(remaining_columns)
        return ordered_columns

    def _ordered_doc_uids_from_families(self, question_sources: tuple[PromptfooTestCase, ...]) -> list[str]:
        ordered_doc_uids: list[str] = []
        seen_doc_uids: set[str] = set()
        seen_family_ids: set[str] = set()
        for source in question_sources:
            if source.family_id in seen_family_ids:
                continue
            seen_family_ids.add(source.family_id)
            family_path = source.question_path.parent / "family.yaml"
            family_data = _load_yaml_object(family_path)
            assert_retrieve = _require_mapping(family_data.get("assert_retrieve"), context=f"{family_path}: assert_retrieve")
            required_documents = _require_list(assert_retrieve.get("required_documents"), context=f"{family_path}: assert_retrieve.required_documents")
            for item in required_documents:
                doc_uid = _require_str(item, context=f"{family_path}: required_documents[]").lower()
                if doc_uid in seen_doc_uids:
                    continue
                seen_doc_uids.add(doc_uid)
                ordered_doc_uids.append(doc_uid)
        return ordered_doc_uids

    def _collect_question_families(self, question_sources: list[PromptfooTestCase]) -> tuple[str, ...]:
        families: list[str] = []
        seen: set[str] = set()
        for source in question_sources:
            if source.family_id in seen:
                continue
            seen.add(source.family_id)
            families.append(source.family_id)
        return tuple(families)


class DocumentRoutingDiagnosticsComparer:
    """Compare one or more run-level document-routing diagnostics JSON files."""

    def __init__(self, repo_root: Path) -> None:
        self._repo_root = repo_root

    def compare(
        self,
        inputs: list[tuple[str, Path]],
        output_dir: Path,
        target_documents: list[str] | None = None,
    ) -> ComparisonDiagnostics:
        run_inputs = self._expand_inputs(inputs)
        if len(run_inputs) < 2:
            raise ValueError("Comparison requires at least two inputs")
        loaded_runs = [(label, _load_json_object(path)) for label, path in run_inputs]
        resolved_target_documents = target_documents or self._target_documents_from_payload(loaded_runs[0][1])
        rows = self._build_rows(loaded_runs, resolved_target_documents)
        diagnostics = ComparisonDiagnostics(
            comparison_name=f"{run_inputs[0][1].stem}__comparison",
            generated_at=datetime.now(tz=UTC).isoformat(),
            input_labels=tuple(label for label, _ in run_inputs),
            target_documents=tuple(resolved_target_documents),
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
        max_rank_delta = self._max_rank_delta(diagnostics)
        lines = [
            f"# {diagnostics.comparison_name}",
            "",
            f"Comparing {', '.join(diagnostics.input_labels)}.",
            "",
            "Each cell shows the retrieved rank for one run. Cells are color-scaled by rank change relative to the first input: improvements are green, regressions are red, and no change is white.",
            "",
        ]
        for doc_uid in diagnostics.target_documents:
            lines.extend(
                [
                    f"## {humanize_doc_uid(doc_uid)}",
                    "",
                    self._render_doc_table(diagnostics, doc_uid, max_rank_delta=max_rank_delta),
                    "",
                ]
            )
        return "\n".join(lines)

    def _render_doc_table(self, diagnostics: ComparisonDiagnostics, doc_uid: str, *, max_rank_delta: int) -> str:
        header_cells = ["Question", *diagnostics.input_labels]
        separator_cells = ["---", *["---:" for _ in diagnostics.input_labels]]
        lines = ["| " + " | ".join(header_cells) + " |", "| " + " | ".join(separator_cells) + " |"]
        for row in diagnostics.rows:
            if row.doc_uid != doc_uid:
                continue
            row_cells = [row.question_id]
            baseline_values = row.values_by_label.get(diagnostics.input_labels[0])
            baseline_rank = None if baseline_values is None else baseline_values.get("rank")
            for label in diagnostics.input_labels:
                values = row.values_by_label[label]
                rank = values.get("rank")
                score = values.get("score")
                if rank is None:
                    row_cells.append("")
                    continue
                delta = None if baseline_rank is None else int(baseline_rank) - int(rank)
                row_cells.append(_format_comparison_rank_cell(int(rank), None if score is None else float(score), delta, max_rank_delta))
            lines.append("| " + " | ".join(row_cells) + " |")
        return "\n".join(lines)

    def _max_rank_delta(self, diagnostics: ComparisonDiagnostics) -> int:
        max_rank_delta = 0
        baseline_label = diagnostics.input_labels[0]
        for row in diagnostics.rows:
            baseline_values = row.values_by_label.get(baseline_label)
            baseline_rank = None if baseline_values is None else baseline_values.get("rank")
            if baseline_rank is None:
                continue
            for label in diagnostics.input_labels[1:]:
                values = row.values_by_label.get(label)
                if values is None:
                    continue
                rank = values.get("rank")
                if rank is None:
                    continue
                delta = abs(int(baseline_rank) - int(rank))
                if delta > max_rank_delta:
                    max_rank_delta = delta
        return max_rank_delta

    def _expand_inputs(self, inputs: list[tuple[str, Path]]) -> list[tuple[str, Path]]:
        expanded: list[tuple[str, Path]] = []
        for label, input_path in inputs:
            payload = _load_json_object(input_path)
            if "runs" in payload:
                runs = _require_list(payload.get("runs"), context=f"{input_path}: runs")
                for run in runs:
                    run_mapping = _require_mapping(run, context=f"{input_path}: runs[]")
                    raw_json_path = Path(_require_str(run_mapping.get("json_path"), context=f"{input_path}: runs[].json_path"))
                    json_path = raw_json_path if raw_json_path.is_absolute() else self._repo_root / raw_json_path
                    expanded.append((label, json_path))
            else:
                expanded.append((label, input_path))
        return expanded

    def _target_documents_from_payload(self, payload: dict[str, object]) -> list[str]:
        target_documents = _require_list(payload.get("target_documents"), context="target_documents")
        resolved: list[str] = []
        for item in target_documents:
            resolved.append(_require_str(item, context="target_documents[]").lower())
        return resolved

    def _build_rows(self, loaded_runs: list[tuple[str, dict[str, object]]], target_documents: list[str]) -> list[ComparisonRow]:
        rows_by_question: dict[str, dict[str, object]] = {}
        for _, payload in loaded_runs:
            for row in _require_list(payload.get("rows"), context="rows"):
                row_mapping = _require_mapping(row, context="rows[]")
                question_id = _require_str(row_mapping.get("question_id"), context="rows[].question_id")
                rows_by_question[question_id] = row_mapping
        question_ids = sorted(rows_by_question, key=_question_sort_key)
        comparison_rows: list[ComparisonRow] = []
        for question_id in question_ids:
            for doc_uid in target_documents:
                values_by_label: dict[str, dict[str, float | int | None]] = {}
                for label, payload in loaded_runs:
                    row = _find_row(payload, question_id)
                    if row is None:
                        values_by_label[label] = {"rank": None, "score": None}
                        continue
                    ranks = _require_mapping(row.get("target_document_ranks"), context="target_document_ranks")
                    scores = _require_mapping(row.get("target_document_scores"), context="target_document_scores")
                    rank_value = ranks.get(doc_uid)
                    score_value = scores.get(doc_uid)
                    values_by_label[label] = {
                        "rank": rank_value if isinstance(rank_value, int) else None,
                        "score": score_value if isinstance(score_value, int | float) else None,
                    }
                comparison_rows.append(
                    ComparisonRow(
                        question_id=question_id,
                        doc_uid=doc_uid,
                        display_label=humanize_doc_uid(doc_uid),
                        values_by_label=values_by_label,
                    )
                )
        return comparison_rows


class DocumentRoutingDiagnosticsAnalyzer:
    """Summarize run-level or comparison-level diagnostics for EXPERIMENTS.md."""

    def __init__(self, repo_root: Path) -> None:
        self._repo_root = repo_root

    def analyze(self, experiment_dir: Path, input_path: Path | None, section_title: str | None = None) -> str:
        payload = self._load_payload(experiment_dir, input_path)
        if "input_labels" in payload and "rows" in payload:
            lines = self._analyze_comparison(payload)
        elif "document_summaries" in payload and "rows" in payload:
            lines = self._analyze_run(payload)
        else:
            raise TypeError("Unsupported document routing diagnostics input")
        rendered = self._render_section(section_title or DEFAULT_SECTION_TITLE, lines)
        experiments_md = experiment_dir / "EXPERIMENTS.md"
        existing = experiments_md.read_text(encoding="utf-8") if experiments_md.exists() else ""
        if existing and not existing.endswith("\n"):
            existing += "\n"
        experiments_md.write_text(existing + "\n" + rendered, encoding="utf-8")
        return rendered

    def _load_payload(self, experiment_dir: Path, input_path: Path | None) -> dict[str, object]:
        if input_path is None:
            index_path = experiment_dir / DEFAULT_DIAGNOSTICS_DIRNAME / DEFAULT_INDEX_JSON_FILENAME
            if not index_path.exists():
                raise FileNotFoundError(f"Missing diagnostics index: {index_path}")
            payload = _load_json_object(index_path)
            runs = _require_list(payload.get("runs"), context="index.json: runs")
            if len(runs) != 1:
                raise ValueError(f"{experiment_dir} has {len(runs)} generated runs; pass --input")
            run_entry = _require_mapping(runs[0], context="index.json: runs[0]")
            raw_json_path = Path(_require_str(run_entry.get("json_path"), context="index.json: runs[0].json_path"))
            input_path = raw_json_path if raw_json_path.is_absolute() else self._repo_root / raw_json_path
        return _load_json_object(input_path)

    def _analyze_run(self, payload: dict[str, object]) -> list[str]:
        rows = _require_list(payload.get("rows"), context="rows")
        target_documents = [
            _require_str(item, context="target_documents[]")
            for item in _require_list(payload.get("target_documents"), context="target_documents")
        ]
        rows_by_target: dict[str, int] = {doc_uid: 0 for doc_uid in target_documents}
        for row in rows:
            row_mapping = _require_mapping(row, context="rows[]")
            target_present = _require_bool_map(row_mapping.get("target_documents_present"), context="rows[].target_documents_present")
            for doc_uid in target_documents:
                if target_present.get(doc_uid, False):
                    rows_by_target[doc_uid] += 1
        lines = [
            f"- Run `{_require_str(payload.get('run_id'), context='run_id')}` covered {len(rows)} question(s).",
            f"- Provider: `{_require_str(payload.get('provider_name'), context='provider_name')}`",
        ]
        for doc_uid in target_documents:
            lines.append(
                f"- {humanize_doc_uid(doc_uid)}: {rows_by_target[doc_uid]}/{len(rows)} present"
            )
        return lines

    def _analyze_comparison(self, payload: dict[str, object]) -> list[str]:
        input_labels = _require_list(payload.get("input_labels"), context="input_labels")
        rows = _require_list(payload.get("rows"), context="rows")
        return [
            f"- Compared {len(input_labels)} runs across {len(rows)} row(s).",
            f"- Inputs: {', '.join(str(item) for item in input_labels)}",
        ]

    def _render_section(self, section_title: str, lines: list[str]) -> str:
        return "\n".join([f"## {section_title}", "", *lines, ""])


def humanize_doc_uid(doc_uid: str) -> str:
    doc_uid = doc_uid.strip()
    if not doc_uid:
        return doc_uid
    lower = doc_uid.lower()
    for prefix in ("ifric", "ifrs", "ias", "sic", "ps", "navis"):
        if not lower.startswith(prefix):
            continue
        suffix = doc_uid[len(prefix) :].lstrip("-_ ")
        suffix = suffix.replace("_", " ").replace("-", " ")
        suffix = _separate_letters_and_digits(suffix)
        suffix = " ".join(suffix.split())
        return f"{prefix.upper()} {suffix}".strip()
    return doc_uid


def _separate_letters_and_digits(value: str) -> str:
    chars: list[str] = []
    previous = ""
    for char in value:
        if char.isdigit() and previous and not previous.isdigit() and not previous.isspace():
            chars.append(" ")
        chars.append(char)
        previous = char
    return "".join(chars)


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
    suffix = question_id.removeprefix("Q1.")
    if suffix.isdigit():
        return (int(suffix), question_id)
    return (10**9, question_id)


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


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
        raise TypeError("Retrieve output must be a JSON object")
    return inner


def _parse_document_hits(payload: dict[str, object]) -> tuple[DocumentHit, ...]:
    hits = _require_list(payload.get("document_hits"), context="retrieve payload: document_hits")
    parsed: list[DocumentHit] = []
    seen: set[str] = set()
    for index, raw_hit in enumerate(hits, start=1):
        hit = _require_mapping(raw_hit, context=f"retrieve payload: document_hits[{index}]")
        doc_uid = _require_str(hit.get("doc_uid"), context=f"retrieve payload: document_hits[{index}].doc_uid").lower()
        if doc_uid in seen:
            continue
        seen.add(doc_uid)
        parsed.append(
            DocumentHit(
                doc_uid=doc_uid,
                display_label=humanize_doc_uid(doc_uid),
                rank=index,
                score=_require_num(hit.get("score"), context=f"retrieve payload: document_hits[{index}].score"),
                document_type=_optional_str(hit.get("document_type")),
                document_kind=_optional_str(hit.get("document_kind")),
            )
        )
    return tuple(parsed)


def _optional_str(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    stripped = value.strip()
    return None if not stripped else stripped


def _find_row(payload: dict[str, object], question_id: str) -> dict[str, object] | None:
    rows = _require_list(payload.get("rows"), context="rows")
    for row in rows:
        row_mapping = _require_mapping(row, context="rows[]")
        if _require_str(row_mapping.get("question_id"), context="rows[].question_id") == question_id:
            return row_mapping
    return None


def _run_diagnostics_from_json(payload: dict[str, object]) -> RunDiagnostics:
    question_sources = []
    for item in _require_list(payload.get("question_sources"), context="question_sources"):
        source = _require_mapping(item, context="question_sources[]")
        question_sources.append(
            PromptfooTestCase(
                family_id=_require_str(source.get("family_id"), context="question_sources[].family_id"),
                question_path=Path(_require_str(source.get("question_path"), context="question_sources[].question_path")),
                description=_require_str(source.get("description"), context="question_sources[].description"),
            )
        )
    rows = []
    for item in _require_list(payload.get("rows"), context="rows"):
        row = _require_mapping(item, context="rows[]")
        document_hits = []
        for hit_item in _require_list(row.get("document_hits"), context="rows[].document_hits"):
            hit = _require_mapping(hit_item, context="rows[].document_hits[]")
            document_hits.append(
                DocumentHit(
                    doc_uid=_require_str(hit.get("doc_uid"), context="rows[].document_hits[].doc_uid"),
                    display_label=_require_str(hit.get("display_label"), context="rows[].document_hits[].display_label"),
                    rank=int(_require_num(hit.get("rank"), context="rows[].document_hits[].rank")),
                    score=_require_num(hit.get("score"), context="rows[].document_hits[].score"),
                    document_type=_optional_str(hit.get("document_type")),
                    document_kind=_optional_str(hit.get("document_kind")),
                )
            )
        rows.append(
            QuestionDiagnostics(
                question_id=_require_str(row.get("question_id"), context="rows[].question_id"),
                run_id=_require_str(row.get("run_id"), context="rows[].run_id"),
                question_path=Path(_require_str(row.get("question_path"), context="rows[].question_path")),
                question_text_sha256=_require_str(row.get("question_text_sha256"), context="rows[].question_text_sha256"),
                document_hits=tuple(document_hits),
                selected_document=_optional_str(row.get("selected_document")),
                selected_rank=None if row.get("selected_rank") is None else int(_require_num(row.get("selected_rank"), context="rows[].selected_rank")),
                selected_score=None if row.get("selected_score") is None else _require_num(row.get("selected_score"), context="rows[].selected_score"),
                in_candidate_set=row.get("in_candidate_set") if isinstance(row.get("in_candidate_set"), bool) or row.get("in_candidate_set") is None else None,
                candidate_count=int(_require_num(row.get("candidate_count"), context="rows[].candidate_count")),
                target_documents_present=_require_bool_map(row.get("target_documents_present"), context="rows[].target_documents_present"),
                target_document_ranks=_require_int_or_none_map(row.get("target_document_ranks"), context="rows[].target_document_ranks"),
                target_document_scores=_require_float_or_none_map(row.get("target_document_scores"), context="rows[].target_document_scores"),
            )
        )
    summaries = []
    for item in _require_list(payload.get("document_summaries"), context="document_summaries"):
        summary = _require_mapping(item, context="document_summaries[]")
        summaries.append(
            DocumentSummary(
                doc_uid=_require_str(summary.get("doc_uid"), context="document_summaries[].doc_uid"),
                display_label=_require_str(summary.get("display_label"), context="document_summaries[].display_label"),
                question_count=int(_require_num(summary.get("question_count"), context="document_summaries[].question_count")),
                present_count=int(_require_num(summary.get("present_count"), context="document_summaries[].present_count")),
                score_min=None if summary.get("score_min") is None else _require_num(summary.get("score_min"), context="document_summaries[].score_min"),
                score_max=None if summary.get("score_max") is None else _require_num(summary.get("score_max"), context="document_summaries[].score_max"),
                rank_min=None if summary.get("rank_min") is None else int(_require_num(summary.get("rank_min"), context="document_summaries[].rank_min")),
                rank_max=None if summary.get("rank_max") is None else int(_require_num(summary.get("rank_max"), context="document_summaries[].rank_max")),
            )
        )
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
        policy_file=_require_str(payload.get("policy_file"), context="policy_file"),
        effective_policy_file=_require_str(payload.get("effective_policy_file"), context="effective_policy_file"),
        policy_name=_require_str(payload.get("policy_name"), context="policy_name"),
        policy=_require_mapping(payload.get("policy"), context="policy"),
        glossary_file=_optional_str(payload.get("glossary_file")),
        effective_glossary_file=_optional_str(payload.get("effective_glossary_file")),
        target_documents=tuple(_require_str(item, context="target_documents[]") for item in _require_list(payload.get("target_documents"), context="target_documents")),
        rows=tuple(rows),
        document_summaries=tuple(summaries),
    )


def _require_bool_map(value: object, *, context: str) -> dict[str, bool]:
    mapping = _require_mapping(value, context=context)
    result: dict[str, bool] = {}
    for key, raw in mapping.items():
        if not isinstance(key, str):
            raise TypeError(f"{context}: keys must be strings")
        if not isinstance(raw, bool):
            raise TypeError(f"{context}[{key!r}]: expected a boolean")
        result[key] = raw
    return result


def _require_int_or_none_map(value: object, *, context: str) -> dict[str, int | None]:
    mapping = _require_mapping(value, context=context)
    result: dict[str, int | None] = {}
    for key, raw in mapping.items():
        if not isinstance(key, str):
            raise TypeError(f"{context}: keys must be strings")
        if raw is None:
            result[key] = None
        elif isinstance(raw, int):
            result[key] = raw
        else:
            raise TypeError(f"{context}[{key!r}]: expected integer or null")
    return result


def _require_float_or_none_map(value: object, *, context: str) -> dict[str, float | None]:
    mapping = _require_mapping(value, context=context)
    result: dict[str, float | None] = {}
    for key, raw in mapping.items():
        if not isinstance(key, str):
            raise TypeError(f"{context}: keys must be strings")
        if raw is None:
            result[key] = None
        elif isinstance(raw, int | float):
            result[key] = float(raw)
        else:
            raise TypeError(f"{context}[{key!r}]: expected number or null")
    return result


def _path_text(path: Path, base: Path) -> str:
    """Return a relative path when possible, otherwise the absolute path."""
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def resolve_experiment_dir(repo_root: Path, experiment: str) -> Path:
    """Resolve an experiment number or path to an experiment directory."""
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


def _format_ranked_score_cell(score: float, rank: int, row_total: int) -> str:
    """Format a ranked score cell using the single-run matrix styling."""
    background_color = _rank_to_background_color(rank, row_total)
    return (
        f'<span style="display:block; background-color: {background_color}; '
        f'padding: 0.1rem 0.35rem; border-radius: 0.25rem; text-align: center;">'
        f"{score:.2f} / <strong>{rank}</strong></span>"
    )


def _format_comparison_rank_cell(rank: int, score: float | None, delta: int | None, max_rank_delta: int) -> str:
    """Format a comparison cell using rank deltas relative to the first input."""
    background_color = _rank_delta_to_background_color(delta, max_rank_delta)
    delta_text = "" if delta is None else f" ({delta:+d})"
    score_text = "" if score is None else f"<br>{score:.2f}"
    return (
        f'<span style="display:block; background-color: {background_color}; '
        f'padding: 0.1rem 0.35rem; border-radius: 0.25rem; text-align: center;">'
        f"{rank}{delta_text}{score_text}</span>"
    )


def _rank_delta_to_background_color(delta: int | None, max_rank_delta: int) -> str:
    """Blend from red through white to green based on rank change."""
    if delta is None or max_rank_delta <= 0 or delta == 0:
        return "#ffffff"
    intensity = min(abs(delta) / max_rank_delta, 1.0)
    if delta > 0:
        rgb = tuple(round(255 + (green - 255) * intensity) for green in LIGHT_GREEN_RGB)
    else:
        rgb = tuple(round(255 + (red - 255) * intensity) for red in LIGHT_RED_RGB)
    return _rgb_to_hex(rgb)


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
