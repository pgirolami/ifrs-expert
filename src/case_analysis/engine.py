"""Case-analysis answer engine and rendering helpers."""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Protocol

from src.b_response_utils import MarkdownOptions, convert_json_to_faq_markdown, convert_json_to_markdown_full
from src.case_analysis.graph import CaseAnalysisGraphRunner
from src.case_analysis.models import RetrievedSourcePackage, ValidationFailure
from src.case_analysis.stages import AuthoritySufficiencyStage, ClassifyAuthorityStage, EvaluateApplicabilityStage, ExecuteRetrievalFn, VerifyCitationsStage
from src.commands.document_output import build_output_document_sections
from src.models.answer_command_result import AnswerCommandResult, JSONValue, RetrievedChunkHit, RetrievedDocumentHit
from src.models.document import infer_document_kind, infer_exact_document_type
from src.models.provenance import Provenance
from src.retrieval.pipeline import RetrievalPipelineConfig, execute_retrieval

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.interfaces import (
        ReadChunkStoreProtocol,
        ReadSectionStoreProtocol,
        ReferenceStoreProtocol,
        SearchDocumentVectorStoreProtocol,
        SearchResult,
        SearchTitleVectorStoreProtocol,
        SearchVectorStoreProtocol,
    )
    from src.models.chunk import Chunk
    from src.policy import RetrievalPolicy

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).parent.parent.parent
PROMPT_A_PATH = PROJECT_ROOT / "prompts" / "answer_prompt_A.txt"
PROMPT_B_PATH = PROJECT_ROOT / "prompts" / "answer_prompt_B.txt"


class AnswerEngineConfigProtocol(Protocol):
    """Runtime dependency shape consumed by AnswerEngine."""

    vector_store: SearchVectorStoreProtocol
    chunk_store: ReadChunkStoreProtocol
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[], Path]
    send_to_llm_fn: Callable[[str], str]
    section_store: ReadSectionStoreProtocol | None
    reference_store: ReferenceStoreProtocol | None
    title_vector_store: SearchTitleVectorStoreProtocol | None
    title_index_path_fn: Callable[[], Path] | None
    document_vector_store: SearchDocumentVectorStoreProtocol | None
    document_vector_store_factory: Callable[[str], SearchDocumentVectorStoreProtocol] | None
    document_index_path_fn: Callable[[str], Path] | None


def _read_prompt_template(path: Path) -> str:
    """Read the prompt template from file."""
    lines = path.read_text(encoding="utf-8").split("\n")
    return "\n".join(line for line in lines if not line.lstrip().startswith("#"))


def _prompt_file_exists(path: Path) -> bool:
    """Check if prompt template file exists."""
    return path.exists()


@dataclass(frozen=True)
class AnswerEngineHooks:
    """Patchable callables used by the answer engine."""

    execute_retrieval_fn: ExecuteRetrievalFn = execute_retrieval
    prompt_file_exists_fn: Callable[[Path], bool] = _prompt_file_exists
    read_prompt_template_fn: Callable[[Path], str] = _read_prompt_template


def _coerce_json_value(value: object) -> JSONValue:
    """Coerce a Python value into the JSONValue type."""
    if value is None or isinstance(value, str | int | float | bool):
        return value
    if isinstance(value, list):
        return [_coerce_json_value(item) for item in value]
    if isinstance(value, dict):
        coerced: dict[str, JSONValue] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                msg = f"JSON object keys must be strings, got {type(key).__name__}"
                raise TypeError(msg)
            coerced[key] = _coerce_json_value(item)
        return coerced

    msg = f"Unsupported JSON value type: {type(value).__name__}"
    raise TypeError(msg)


def _parse_json_value(raw_text: str) -> JSONValue:
    """Parse raw JSON text into a typed JSON value."""
    parsed: object = json.loads(raw_text)
    return _coerce_json_value(parsed)


def _build_retrieved_chunk_hits(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
) -> list[RetrievedChunkHit]:
    """Build serializable chunk hits from the retrieval result."""
    chunk_hits: list[RetrievedChunkHit] = []
    for result in results:
        doc_uid = str(result["doc_uid"])
        chunk_db_id = int(result["chunk_id"])
        score = float(result["score"])
        document_type = infer_exact_document_type(doc_uid)
        document_kind = infer_document_kind(doc_uid)
        for chunk in doc_chunks.get(doc_uid, []):
            if chunk.id != chunk_db_id:
                continue
            provenance_value = result.get("provenance")
            provenance = Provenance(provenance_value) if provenance_value is not None else None
            chunk_hits.append(
                RetrievedChunkHit(
                    doc_uid=doc_uid,
                    chunk_number=chunk.chunk_number,
                    chunk_id=chunk.chunk_id,
                    score=round(score, 4),
                    document_type=document_type,
                    document_kind=document_kind,
                    containing_section_id=chunk.containing_section_id,
                    containing_section_db_id=chunk.containing_section_db_id,
                    page_start=chunk.page_start,
                    page_end=chunk.page_end,
                    text=chunk.text,
                    provenance=provenance,
                )
            )
            break
    return chunk_hits


def _extract_prompt_content(full_output: str) -> str:
    """Extract only the prompt content, skipping the chunk summary at the top."""
    lines = full_output.split("\n")
    start_idx = 0
    for index, line in enumerate(lines):
        if line.startswith("You are an IFRS expert"):
            start_idx = index
            break
    return "\n".join(lines[start_idx:])


class AnswerEngine:
    """Own answer workflow orchestration, prompt execution, and artifacts."""

    def __init__(
        self,
        query: str,
        policy: RetrievalPolicy,
        config: AnswerEngineConfigProtocol,
        hooks: AnswerEngineHooks | None = None,
    ) -> None:
        """Initialize the engine with workflow dependencies."""
        self.query = query
        self._policy = policy
        self._config = config
        self._hooks = hooks or AnswerEngineHooks()
        self._retrieved_doc_uids: list[str] = []

    def run(self) -> AnswerCommandResult:
        """Run prerequisite checks and the deterministic case-analysis graph."""
        prerequisite_error = self.get_prerequisite_error()
        if prerequisite_error is not None:
            return AnswerCommandResult.failure(query=self.query, error=prerequisite_error, error_stage="prerequisite")

        runner = CaseAnalysisGraphRunner(
            policy=self._policy,
            pipeline_config=self._build_retrieval_pipeline_config(),
            execute_retrieval_fn=self._hooks.execute_retrieval_fn,
            build_answer_result_fn=self._build_answer_result_from_source_package,
            process_prompts_fn=self._process_source_package_prompts,
        )
        return runner.run(self.query)

    def get_prerequisite_error(self) -> str | None:
        """Return a CLI/runtime prerequisite error, if any."""
        prompt_error = self._get_prompt_template_error()
        if prompt_error is not None:
            return prompt_error

        if self._policy.document_routing.source == "all_documents" and self._policy.chunk_retrieval.mode == "title_similarity":
            return self._get_title_prerequisite_error()
        if self._policy.document_routing.source == "document_representation":
            document_prerequisite_error = self._get_document_prerequisite_error()
            if document_prerequisite_error is not None:
                return document_prerequisite_error

        index_path = self._config.index_path_fn()
        if not index_path.exists():
            logger.error(f"Missing vector index at {index_path}; corpus must be built before running the answer pipeline")
            return "Error: No index found. Please run 'store' command first."
        return None

    def _get_prompt_template_error(self) -> str | None:
        if not self._hooks.prompt_file_exists_fn(PROMPT_A_PATH):
            logger.error(f"Missing Prompt A template at {PROMPT_A_PATH}")
            return "Error: Prompt A template not found."
        if not self._hooks.prompt_file_exists_fn(PROMPT_B_PATH):
            logger.error(f"Missing Prompt B template at {PROMPT_B_PATH}")
            return "Error: Prompt B template not found."
        return None

    def _get_title_prerequisite_error(self) -> str | None:
        if self._config.title_index_path_fn is None:
            return "Error: Title retrieval is not configured."
        title_index_path = self._config.title_index_path_fn()
        if not title_index_path.exists():
            logger.error(f"Missing title vector index at {title_index_path}; corpus must be built before running the answer pipeline")
            return "Error: No title index found. Please run 'store' command first."
        return None

    def _get_document_prerequisite_error(self) -> str | None:
        if self._config.document_index_path_fn is None:
            return "Error: Document retrieval is not configured."
        required_representations = sorted({document_policy.similarity_representation for document_policy in self._policy.documents.by_document_type.values()})
        for representation in required_representations:
            try:
                document_index_path = self._config.document_index_path_fn(representation)
            except TypeError:
                document_index_path = self._config.document_index_path_fn()  # type: ignore[call-arg]
            if document_index_path.exists():
                continue
            logger.error(f"Missing document vector index at {document_index_path} for representation={representation}; corpus must be built before running the answer pipeline")
            return "Error: No document index found. Please run 'store' command first."
        return None

    def _build_retrieval_pipeline_config(self) -> RetrievalPipelineConfig:
        return RetrievalPipelineConfig(
            vector_store=self._config.vector_store,
            chunk_store=self._config.chunk_store,
            init_db_fn=self._config.init_db_fn,
            index_path_fn=self._config.index_path_fn,
            section_store=self._config.section_store,
            reference_store=self._config.reference_store,
            title_vector_store=self._config.title_vector_store,
            title_index_path_fn=self._config.title_index_path_fn,
            document_vector_store=self._config.document_vector_store,
            document_vector_store_factory=self._config.document_vector_store_factory,
            document_index_path_fn=self._config.document_index_path_fn,
        )

    def _build_answer_result_from_source_package(self, source_package: RetrievedSourcePackage) -> AnswerCommandResult:
        self._retrieved_doc_uids = source_package.retrieved_doc_uids
        search_results = source_package.to_search_results()
        doc_chunks = source_package.to_doc_chunks()
        return AnswerCommandResult(
            query=self.query,
            retrieved_doc_uids=list(self._retrieved_doc_uids),
            document_hits=[
                RetrievedDocumentHit(
                    doc_uid=hit.doc_uid,
                    score=hit.score,
                    document_type=hit.document_type,
                    document_kind=infer_document_kind(hit.doc_uid),
                )
                for hit in source_package.document_hits
            ],
            chunk_hits=_build_retrieved_chunk_hits(search_results, doc_chunks),
        )

    def _process_source_package_prompts(
        self,
        result: AnswerCommandResult,
        source_package: RetrievedSourcePackage,
    ) -> AnswerCommandResult:
        return self._process_prompts(result, source_package.to_search_results(), source_package.to_doc_chunks())

    def _process_prompts(
        self,
        result: AnswerCommandResult,
        results: list[SearchResult],
        doc_chunks: dict[str, list[Chunk]],
    ) -> AnswerCommandResult:
        chunk_summary = _build_chunk_summary(results, doc_chunks)
        formatted_chunks = self._format_chunks(results, doc_chunks)

        prompt_a_full = self._build_prompt_from_template(PROMPT_A_PATH, formatted_chunks, chunk_summary)
        result.prompt_a_text = _extract_prompt_content(prompt_a_full)

        authority_classification_result = ClassifyAuthorityStage(send_to_llm_fn=self._config.send_to_llm_fn).execute(result.prompt_a_text)
        if isinstance(authority_classification_result, ValidationFailure):
            result.error = authority_classification_result.message
            result.error_stage = authority_classification_result.error_stage
            return result

        result.prompt_a_raw_response = authority_classification_result.raw_response
        result.prompt_a_json = authority_classification_result.payload

        authority_sufficiency_result = AuthoritySufficiencyStage().execute(authority_classification_result.payload)
        result.authority_sufficiency_json = authority_sufficiency_result.model_dump(mode="json")
        if not authority_sufficiency_result.should_continue:
            result.error = f"Error: Authority classification requires controlled stop: {authority_sufficiency_result.reason}"
            result.error_stage = "authority_sufficiency"
            return result

        prompt_b_context = _build_prompt_b_context(formatted_chunks, result.prompt_a_json)
        result.prompt_b_text = self._build_prompt_b(prompt_b_context, json.dumps(result.prompt_a_json, indent=2, ensure_ascii=False))

        applicability_analysis_result = EvaluateApplicabilityStage(send_to_llm_fn=self._config.send_to_llm_fn).execute(result.prompt_b_text)
        if isinstance(applicability_analysis_result, ValidationFailure):
            result.error = applicability_analysis_result.message
            result.error_stage = applicability_analysis_result.error_stage
            return result

        result.prompt_b_raw_response = applicability_analysis_result.raw_response
        result.prompt_b_json = applicability_analysis_result.payload
        logger.info("Step 2 complete: Received final answer from LLM")

        chunk_data = _build_chunk_data_for_markdown(prompt_b_context)
        citation_verification_result = VerifyCitationsStage().execute(applicability_analysis_result.payload, chunk_data)
        result.citation_verification_json = citation_verification_result.model_dump(mode="json")

        prompt_b_doc_uids = _extract_doc_uids_from_context(prompt_b_context)
        primary_accounting_issue = result.prompt_a_json.get("primary_accounting_issue") if isinstance(result.prompt_a_json, dict) else None
        primary_accounting_issue_text = primary_accounting_issue if isinstance(primary_accounting_issue, str) else None
        options = MarkdownOptions(
            question=self.query,
            doc_uids=self._retrieved_doc_uids,
            authority_doc_uids=prompt_b_doc_uids,
            primary_accounting_issue=primary_accounting_issue_text,
            chunk_data=chunk_data,
        )
        result.prompt_b_memo_markdown = convert_json_to_markdown_full(result.prompt_b_json, options)
        result.prompt_b_faq_markdown = convert_json_to_faq_markdown(
            result.prompt_b_json,
            primary_accounting_issue=options.primary_accounting_issue,
        )
        result.mark_success()
        return result

    def _build_prompt_from_template(self, template_path: Path, chunks: list[str], chunk_summary: str) -> str:
        template = self._hooks.read_prompt_template_fn(template_path)
        chunks_text = "\n\n".join(chunks)
        prompt = template.replace("{{CHUNKS}}", chunks_text).replace("{{QUERY}}", self.query)
        return f"{chunk_summary}\n\n{prompt}"

    def _build_prompt_b(self, context: str, approaches_json: str) -> str:
        template = self._hooks.read_prompt_template_fn(PROMPT_B_PATH)
        return template.replace("{{CHUNKS}}", context).replace("{{QUERY}}", self.query).replace("{{APPROACHES_JSON}}", approaches_json)

    def _format_chunks(self, results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> list[str]:
        doc_order: list[str] = []
        chunk_ids_by_doc: dict[str, set[int]] = {}
        score_by_chunk: dict[tuple[str, int], float] = {}

        for result in results:
            doc_uid = result["doc_uid"]
            chunk_id = result["chunk_id"]
            score = result["score"]
            if doc_uid not in chunk_ids_by_doc:
                chunk_ids_by_doc[doc_uid] = set()
                doc_order.append(doc_uid)
            chunk_ids_by_doc[doc_uid].add(chunk_id)
            score_by_chunk[(doc_uid, chunk_id)] = score

        formatted_documents: list[str] = []
        for doc_uid in doc_order:
            formatted_chunks: list[str] = []
            for chunk in doc_chunks.get(doc_uid, []):
                chunk_id = chunk.id
                if chunk_id is None or chunk_id not in chunk_ids_by_doc.get(doc_uid, set()):
                    continue
                score = score_by_chunk.get((doc_uid, chunk_id), 0.0)
                chunk_xml = f'<chunk id="{chunk_id}" doc_uid="{_escape_xml(doc_uid)}" paragraph="{_escape_xml(chunk.chunk_number)}" score="{score:.4f}">\n{chunk.text}\n</chunk>'
                formatted_chunks.append(chunk_xml)

            joined_chunks = "\n\n".join(formatted_chunks)
            document_type = infer_exact_document_type(doc_uid)
            document_kind = infer_document_kind(doc_uid)
            document_type_attr = _escape_xml(document_type or "")
            document_kind_attr = _escape_xml(document_kind or "")
            document_xml = f'<Document name="{_escape_xml(doc_uid)}" document_type="{document_type_attr}" document_kind="{document_kind_attr}">\n{joined_chunks}\n</Document>'
            formatted_documents.append(document_xml)

        return formatted_documents


def _build_prompt_b_context(formatted_chunks: list[str], prompt_a_json: JSONValue) -> str:
    authority_refs = _extract_authority_references(prompt_a_json)
    if authority_refs is None:
        return "\n\n".join(formatted_chunks)
    return _filter_chunks_by_authority(formatted_chunks, authority_refs)


def _extract_authority_references(prompt_a_json: JSONValue) -> set[tuple[str, str]] | None:
    if not isinstance(prompt_a_json, dict):
        logger.error("Prompt A JSON is not a dict; using all chunks for Prompt B (authority filtering skipped)")
        return None

    authority_classification = prompt_a_json.get("authority_classification")
    if not isinstance(authority_classification, dict):
        logger.error("No authority_classification in Prompt A response; using all chunks for Prompt B (authority filtering skipped)")
        return None

    primary_authority = authority_classification.get("primary_authority", [])
    supporting_authority = authority_classification.get("supporting_authority", [])
    if not primary_authority and not supporting_authority:
        logger.warning("No primary or supporting authority identified; using all chunks for Prompt B (authority filtering skipped)")
        return None

    allowed_chunks: set[tuple[str, str]] = set()
    for authority_item in (*primary_authority, *supporting_authority):
        if not isinstance(authority_item, dict):
            continue
        document = authority_item.get("document")
        references = authority_item.get("references", [])
        if not isinstance(document, str) or not isinstance(references, list):
            continue
        for ref in references:
            if isinstance(ref, str):
                allowed_chunks.add((document, ref))

    if not allowed_chunks:
        logger.error("Could not extract authority references; using all chunks for Prompt B (authority filtering skipped)")
        return None

    logger.info(f"Filtering Prompt B context to {len(allowed_chunks)} authority references")
    return allowed_chunks


def _filter_chunks_by_authority(formatted_chunks: list[str], authority_refs: set[tuple[str, str]]) -> str:
    chunk_pattern = re.compile(
        r'<chunk id="(\d+)" doc_uid="[^"]*" paragraph="([^"]*)"[^>]*>\n(.*?)\n</chunk>',
        re.DOTALL,
    )

    filtered_documents: list[str] = []
    for doc_xml in formatted_chunks:
        doc_match = re.search(r'<Document\s+[^>]*name="([^"]+)"[^>]*>', doc_xml)
        if not doc_match:
            continue
        doc_uid = doc_match.group(1)
        document_type_match = re.search(r'document_type="([^"]*)"', doc_xml)
        document_kind_match = re.search(r'document_kind="([^"]*)"', doc_xml)
        document_type = document_type_match.group(1) if document_type_match else ""
        document_kind = document_kind_match.group(1) if document_kind_match else ""
        filtered_chunk_xmls = [match.group(0) for match in chunk_pattern.finditer(doc_xml) if (doc_uid, match.group(2)) in authority_refs]
        if filtered_chunk_xmls:
            joined_chunks = "\n\n".join(filtered_chunk_xmls)
            document_xml = f'<Document name="{_escape_xml(doc_uid)}" document_type="{_escape_xml(document_type)}" document_kind="{_escape_xml(document_kind)}">\n{joined_chunks}\n</Document>'
            filtered_documents.append(document_xml)

    if not filtered_documents:
        logger.error("No chunks matched authority references; falling back to all chunks (authority filtering failed)")
        return "\n\n".join(formatted_chunks)
    return "\n\n".join(filtered_documents)


def _escape_xml(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")


def _extract_doc_uids_from_context(context: str) -> list[str]:
    doc_uids: list[str] = []
    for match in re.finditer(r'<Document\s+[^>]*name="([^"]+)"[^>]*>', context):
        doc_uid = match.group(1)
        if doc_uid not in doc_uids:
            doc_uids.append(doc_uid)
    return doc_uids


def _build_chunk_data_for_markdown(context: str) -> dict[str, str]:
    chunk_data: dict[str, str] = {}
    chunk_pattern = re.compile(
        r'<chunk id="\d+" doc_uid="([^"]*)" paragraph="([^"]*)"[^>]*>\n(.*?)\n</chunk>',
        re.DOTALL,
    )
    for match in chunk_pattern.finditer(context):
        key = f"{match.group(1)}/{match.group(2)}"
        chunk_data[key] = match.group(3)
    return chunk_data


def _build_chunk_summary(results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> str:
    if not results:
        return "Retrieved chunks:\n- none"
    summaries = build_output_document_sections(results=results, doc_chunks=doc_chunks, logger=logger)
    lines: list[str] = ["Retrieved chunks:"]
    for summary in summaries:
        sections_text = ", ".join(summary.section_labels) if summary.section_labels else "(no sections)"
        lines.append(f"- {summary.doc_uid}: {sections_text}")
    return "\n".join(lines)
