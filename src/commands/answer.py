"""Answer command - retrieve chunks and run the two-step answer pipeline."""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

from src.b_response_utils import MarkdownOptions, convert_json_to_faq_markdown, convert_json_to_markdown_full
from src.commands.constants import DEFAULT_VERBOSE
from src.commands.document_output import build_output_document_sections
from src.commands.retrieval_request_builder import build_retrieval_request
from src.db import ChunkStore, ContentReferenceStore, SectionStore, init_db
from src.llm import get_client
from src.models.answer_command_result import AnswerCommandResult, JSONValue, RetrievedChunkHit, RetrievedDocumentHit
from src.models.document import infer_document_kind, infer_exact_document_type
from src.models.provenance import Provenance
from src.retrieval.pipeline import RetrievalPipelineConfig, execute_retrieval
from src.vector.document_store import DocumentVectorStore, get_document_id_map_path, get_document_index_path
from src.vector.store import VectorStore, get_index_path
from src.vector.title_store import TitleVectorStore, get_title_index_path

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


@dataclass
class AnswerConfig:
    """Configuration for AnswerCommand - consolidates dependencies."""

    vector_store: SearchVectorStoreProtocol
    chunk_store: ReadChunkStoreProtocol
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[], Path]
    send_to_llm_fn: Callable[[str], str]
    section_store: ReadSectionStoreProtocol | None = None
    reference_store: ReferenceStoreProtocol | None = None
    title_vector_store: SearchTitleVectorStoreProtocol | None = None
    title_index_path_fn: Callable[[], Path] | None = None
    document_vector_store: SearchDocumentVectorStoreProtocol | None = None
    document_vector_store_factory: Callable[[str], SearchDocumentVectorStoreProtocol] | None = None
    document_index_path_fn: Callable[[str], Path] | None = None


@dataclass
class AnswerOptions:
    """Options for answer command."""

    policy: RetrievalPolicy
    verbose: bool = DEFAULT_VERBOSE
    output_dir: Path | None = None


# Helper functions for chunk expansion (extracted to reduce complexity)
def _init_expansion_data(
    results: list[SearchResult],
) -> tuple[dict[tuple[str, int], float], list[str], dict[str, set[int]]]:
    """Initialize expansion data structures."""
    result_score_by_chunk: dict[tuple[str, int], float] = {}
    doc_order: list[str] = []
    selected_ids_by_doc: dict[str, set[int]] = {}

    for result in results:
        doc_uid = result["doc_uid"]
        chunk_id = result["chunk_id"]
        score = result["score"]

        if doc_uid not in selected_ids_by_doc:
            selected_ids_by_doc[doc_uid] = set()
            doc_order.append(doc_uid)

        result_score_by_chunk[(doc_uid, chunk_id)] = score

    return result_score_by_chunk, doc_order, selected_ids_by_doc


def _include_full_document(
    doc_chunks: dict[str, list[Chunk]],
    selected_ids_by_doc: dict[str, set[int]],
    full_doc_threshold: int,
) -> set[str]:
    """Process full document threshold inclusion."""
    full_doc_docs: set[str] = set()

    for doc_uid, chunks in doc_chunks.items():
        doc_text_size = sum(len(chunk.text) for chunk in chunks)
        if full_doc_threshold > 0 and doc_text_size < full_doc_threshold:
            full_doc_docs.add(doc_uid)
            for document_chunk in chunks:
                if document_chunk.id is not None:
                    selected_ids_by_doc[doc_uid].add(document_chunk.id)

    return full_doc_docs


def _expand_with_neighbour_chunks(
    results: list[SearchResult],
    doc_chunks: dict[str, list[Chunk]],
    selected_ids_by_doc: dict[str, set[int]],
    expand: int,
) -> set[tuple[str, int]]:
    """Expand results by including surrounding chunks."""
    expanded_via_neighbours: set[tuple[str, int]] = set()

    for result in results:
        doc_uid = result["doc_uid"]
        chunk_id = result["chunk_id"]
        chunks = doc_chunks.get(doc_uid, [])

        for idx, chunk in enumerate(chunks):
            if chunk.id == chunk_id:
                start_idx = max(0, idx - expand)
                end_idx = min(len(chunks), idx + expand + 1)
                for surrounding_chunk in chunks[start_idx:end_idx]:
                    if surrounding_chunk.id is not None:
                        selected_ids_by_doc[doc_uid].add(surrounding_chunk.id)
                        if surrounding_chunk.id != chunk_id:
                            expanded_via_neighbours.add((doc_uid, surrounding_chunk.id))
                break

    return expanded_via_neighbours


def _build_expanded_results(
    doc_order: list[str],
    doc_chunks: dict[str, list[Chunk]],
    selected_ids_by_doc: dict[str, set[int]],
    result_score_by_chunk: dict[tuple[str, int], float],
) -> list[SearchResult]:
    """Build the final expanded results list."""
    expanded_results: list[SearchResult] = []
    for doc_uid in doc_order:
        for chunk in doc_chunks.get(doc_uid, []):
            chunk_id = chunk.id
            if chunk_id is None:
                continue
            if chunk_id not in selected_ids_by_doc.get(doc_uid, set()):
                continue
            expanded_results.append(
                {
                    "doc_uid": doc_uid,
                    "chunk_id": chunk_id,
                    "score": result_score_by_chunk.get((doc_uid, chunk_id), 0.0),
                },
            )
    return expanded_results


def _read_prompt_template(path: Path) -> str:
    """Read the prompt template from file."""
    lines = path.read_text(encoding="utf-8").split("\n")
    return "\n".join(line for line in lines if not line.lstrip().startswith("#"))


def _prompt_file_exists(path: Path) -> bool:
    """Check if prompt template file exists."""
    return path.exists()


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
                    provenance=Provenance(result["provenance"]),
                )
            )
            break
    return chunk_hits


class AnswerCommand:
    """Retrieve chunks and run the two-step answer pipeline."""

    def __init__(
        self,
        query: str,
        config: AnswerConfig,
        options: AnswerOptions | None = None,
    ) -> None:
        """Initialize the answer command."""
        if options is None:
            message = "AnswerCommand requires options with a loaded policy"
            raise ValueError(message)
        self.query = query
        self._config = config
        self._options = options
        self.output_dir = options.output_dir
        self.verbose = options.verbose
        self._retrieved_doc_uids: list[str] = []

    def execute(self) -> AnswerCommandResult:
        """Execute the answer command and return the run artifacts."""
        policy = self._options.policy
        logger.info(f"AnswerCommand(query='{self.query[:50]}', k={policy.k}, expand={policy.expand}, f={policy.full_doc_threshold}, min-score={policy.text.min_score})")

        validation_error = self._get_validation_error()
        if validation_error:
            return AnswerCommandResult.failure(query=self.query, error=validation_error, error_stage="validation")

        prerequisite_error = self._get_prerequisite_error()
        if prerequisite_error:
            return AnswerCommandResult.failure(query=self.query, error=prerequisite_error, error_stage="prerequisite")

        return self._execute_workflow()

    def _get_validation_error(self) -> str | None:
        """Validate query and policy; return the first error or None."""
        validators = (
            self._get_query_validation_error,
            self._get_positive_policy_validation_error,
            self._get_document_cap_validation_error,
            self._get_policy_shape_validation_error,
        )
        for validator in validators:
            error = validator()
            if error is not None:
                return error
        return None

    def _get_query_validation_error(self) -> str | None:
        if self.query and self.query.strip():
            return None
        return "Error: Query cannot be empty"

    def _get_positive_policy_validation_error(self) -> str | None:
        policy = self._options.policy
        if policy.expand < 0:
            return "Error: expand must be >= 0"
        if policy.full_doc_threshold < 0:
            return "Error: full_doc_threshold must be >= 0"
        if policy.k <= 0:
            return "Error: retrieval.k in policy must be > 0"
        if policy.documents.global_d <= 0:
            return "Error: retrieval.documents.global_d in policy must be > 0"
        return None

    def _get_document_cap_validation_error(self) -> str | None:
        for document_type, cap in self._options.policy.documents.by_document_type.items():
            if cap.d <= 0:
                return f"Error: per-type document cap for {document_type} must be > 0"
        return None

    def _get_policy_shape_validation_error(self) -> str | None:
        policy = self._options.policy
        if policy.document_routing.source not in {"all_documents", "top_chunk_results", "document_representation"}:
            return "Error: document_routing.source in policy must be 'all_documents', 'top_chunk_results', or 'document_representation'"
        if policy.chunk_retrieval.mode not in {"chunk_similarity", "title_similarity"}:
            return "Error: chunk_retrieval.mode in policy must be 'chunk_similarity' or 'title_similarity'"
        return None

    def _get_prerequisite_error(self) -> str | None:
        """Get prerequisite error or None."""
        policy = self._options.policy
        prompt_error = self._get_prompt_template_error()
        if prompt_error is not None:
            return prompt_error

        if policy.document_routing.source == "all_documents" and policy.chunk_retrieval.mode == "title_similarity":
            return self._get_title_prerequisite_error()
        if policy.document_routing.source == "document_representation":
            document_prerequisite_error = self._get_document_prerequisite_error()
            if document_prerequisite_error is not None:
                return document_prerequisite_error

        index_path = self._config.index_path_fn()
        if not index_path.exists():
            logger.error(f"Missing vector index at {index_path}; corpus must be built before running the answer pipeline")
            return "Error: No index found. Please run 'store' command first."
        return None

    def _get_prompt_template_error(self) -> str | None:
        """Validate that both prompt templates are available."""
        if not _prompt_file_exists(PROMPT_A_PATH):
            logger.error(f"Missing Prompt A template at {PROMPT_A_PATH}")
            return "Error: Prompt A template not found."
        if not _prompt_file_exists(PROMPT_B_PATH):
            logger.error(f"Missing Prompt B template at {PROMPT_B_PATH}")
            return "Error: Prompt B template not found."
        return None

    def _get_title_prerequisite_error(self) -> str | None:
        """Validate the prerequisites for title retrieval mode."""
        if self._config.title_index_path_fn is None:
            return "Error: Title retrieval is not configured."
        title_index_path = self._config.title_index_path_fn()
        if not title_index_path.exists():
            logger.error(f"Missing title vector index at {title_index_path}; corpus must be built before running the answer pipeline")
            return "Error: No title index found. Please run 'store' command first."
        return None

    def _get_document_prerequisite_error(self) -> str | None:
        """Validate the prerequisites for document-first retrieval mode."""
        if self._config.document_index_path_fn is None:
            return "Error: Document retrieval is not configured."
        required_representations = sorted({document_policy.similarity_representation for document_policy in self._options.policy.documents.by_document_type.values()})
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

    def _execute_workflow(self) -> AnswerCommandResult:
        """Execute the main workflow."""
        policy = self._options.policy
        error, retrieval_result = execute_retrieval(
            request=build_retrieval_request(
                query=self.query,
                policy=policy,
                chunk_min_score=policy.titles.min_score if policy.chunk_retrieval.mode == "title_similarity" else policy.text.min_score,
                expand_to_section=policy.expand_to_section if policy.document_routing.source == "all_documents" else True,
            ),
            config=RetrievalPipelineConfig(
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
            ),
        )
        if error is not None:
            return AnswerCommandResult.failure(query=self.query, error=error, error_stage="retrieval")
        if retrieval_result is None:
            return AnswerCommandResult.failure(
                query=self.query,
                error="Error: Retrieval did not return a result",
                error_stage="retrieval",
            )

        self._retrieved_doc_uids = retrieval_result.retrieved_doc_uids
        result = AnswerCommandResult(
            query=self.query,
            retrieved_doc_uids=list(self._retrieved_doc_uids),
            document_hits=[
                RetrievedDocumentHit(
                    doc_uid=hit.doc_uid,
                    score=hit.score,
                    document_type=hit.document_type,
                    document_kind=infer_document_kind(hit.doc_uid),
                )
                for hit in retrieval_result.document_hits
            ],
            chunk_hits=_build_retrieved_chunk_hits(retrieval_result.chunk_results, retrieval_result.doc_chunks),
        )
        return self._process_prompts(result, retrieval_result.chunk_results, retrieval_result.doc_chunks)

    def _process_prompts(
        self,
        result: AnswerCommandResult,
        results: list[SearchResult],
        doc_chunks: dict[str, list[Chunk]],
    ) -> AnswerCommandResult:
        """Build prompts, send to LLM, and collect artifacts."""
        chunk_summary = self._build_chunk_summary(results, doc_chunks)
        formatted_chunks = self._format_chunks(results, doc_chunks)

        prompt_a_full = self._build_prompt_from_template(PROMPT_A_PATH, formatted_chunks, chunk_summary)
        result.prompt_a_text = _extract_prompt_content(prompt_a_full)

        try:
            result.prompt_a_raw_response = self._config.send_to_llm_fn(result.prompt_a_text)
        except RuntimeError as e:
            logger.exception("Prompt A LLM call failed")
            result.error = f"Error: LLM call failed: {e}"
            result.error_stage = "prompt_a"
            return result

        try:
            result.prompt_a_json = _parse_json_value(result.prompt_a_raw_response)
        except (json.JSONDecodeError, TypeError) as e:
            logger.exception("Could not parse JSON response from Prompt A")
            result.error = f"Error: LLM returned invalid JSON: {e}\n\nResponse was:\n{result.prompt_a_raw_response}"
            result.error_stage = "prompt_a_parse"
            return result

        # Build Prompt B context: use only chunks from primary and supporting authority
        prompt_b_context = self._build_prompt_b_context(formatted_chunks, result.prompt_a_json)
        result.prompt_b_text = self._build_prompt_b(prompt_b_context, json.dumps(result.prompt_a_json, indent=2, ensure_ascii=False))

        try:
            result.prompt_b_raw_response = self._config.send_to_llm_fn(result.prompt_b_text)
        except RuntimeError as e:
            logger.exception("Prompt B LLM call failed")
            result.error = f"Error: LLM call failed: {e}"
            result.error_stage = "prompt_b"
            return result

        logger.info("Step 2 complete: Received final answer from LLM")

        if result.prompt_b_raw_response is not None:
            try:
                result.prompt_b_json = _parse_json_value(result.prompt_b_raw_response)
            except (json.JSONDecodeError, TypeError) as e:
                logger.warning(f"Prompt B response could not be parsed as JSON: {e}")
            else:
                if isinstance(result.prompt_b_json, dict):
                    # Build chunk_data for citation formatting
                    chunk_data = self._build_chunk_data_for_markdown(prompt_b_context)

                    # Extract Prompt B context doc_uids from the filtered context
                    prompt_b_doc_uids = self._extract_doc_uids_from_context(prompt_b_context)

                    # Create options and generate markdown
                    options = MarkdownOptions(
                        question=self.query,
                        doc_uids=self._retrieved_doc_uids,
                        authority_doc_uids=prompt_b_doc_uids,
                        primary_accounting_issue=result.prompt_a_json.get("primary_accounting_issue") if isinstance(result.prompt_a_json, dict) else None,
                        chunk_data=chunk_data,
                    )
                    result.prompt_b_memo_markdown = convert_json_to_markdown_full(result.prompt_b_json, options)

                    # Generate FAQ-style markdown from the same JSON
                    result.prompt_b_faq_markdown = convert_json_to_faq_markdown(
                        result.prompt_b_json,
                        primary_accounting_issue=options.primary_accounting_issue,
                    )
                else:
                    logger.warning("Prompt B response parsed as JSON but is not an object; markdown conversion skipped")

        result.mark_success()
        return result

    def _build_prompt_from_template(
        self,
        template_path: Path,
        chunks: list[str],
        chunk_summary: str,
    ) -> str:
        """Build a prompt by substituting chunks into a template."""
        template = _read_prompt_template(template_path)
        chunks_text = "\n\n".join(chunks)
        prompt = template.replace("{{CHUNKS}}", chunks_text).replace("{{QUERY}}", self.query)
        return f"{chunk_summary}\n\n{prompt}"

    def _build_prompt_b(self, context: str, approaches_json: str) -> str:
        """Build Prompt B by substituting placeholders."""
        template = _read_prompt_template(PROMPT_B_PATH)
        return template.replace("{{CHUNKS}}", context).replace("{{QUERY}}", self.query).replace("{{APPROACHES_JSON}}", approaches_json)

    def _format_chunks(self, results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> list[str]:
        """Format chunks grouped by document for clearer prompt structure."""
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
                if chunk_id is None:
                    continue
                if chunk_id not in chunk_ids_by_doc.get(doc_uid, set()):
                    continue

                score = score_by_chunk.get((doc_uid, chunk_id), 0.0)
                chunk_xml = f'<chunk id="{chunk_id}" doc_uid="{self._escape_xml(doc_uid)}" paragraph="{self._escape_xml(chunk.chunk_number)}" score="{score:.4f}">\n{chunk.text}\n</chunk>'
                formatted_chunks.append(chunk_xml)

            joined_chunks = "\n\n".join(formatted_chunks)
            document_type = infer_exact_document_type(doc_uid)
            document_kind = infer_document_kind(doc_uid)
            document_type_attr = self._escape_xml(document_type or "")
            document_kind_attr = self._escape_xml(document_kind or "")
            document_xml = f'<Document name="{self._escape_xml(doc_uid)}" document_type="{document_type_attr}" document_kind="{document_kind_attr}">\n{joined_chunks}\n</Document>'
            formatted_documents.append(document_xml)

        return formatted_documents

    def _build_prompt_b_context(
        self,
        formatted_chunks: list[str],
        prompt_a_json: JSONValue,
    ) -> str:
        """Build Prompt B context using only chunks from primary and supporting authority.

        Parses authority_classification from Prompt A response and filters chunks to only
        include those explicitly identified as primary or supporting authority.
        """
        authority_refs = self._extract_authority_references(prompt_a_json)
        if authority_refs is None:
            return "\n\n".join(formatted_chunks)

        return self._filter_chunks_by_authority(formatted_chunks, authority_refs)

    def _extract_authority_references(self, prompt_a_json: JSONValue) -> set[tuple[str, str]] | None:
        """Extract (doc_uid, chunk_number) references from primary and supporting authority.

        Returns None if no valid references can be extracted (falls back to all chunks).
        """
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
            if not document or not references:
                continue
            for ref in references:
                if isinstance(ref, str):
                    allowed_chunks.add((document, ref))

        if not allowed_chunks:
            logger.error("Could not extract authority references; using all chunks for Prompt B (authority filtering skipped)")
            return None

        logger.info(f"Filtering Prompt B context to {len(allowed_chunks)} authority references")
        return allowed_chunks

    def _filter_chunks_by_authority(
        self,
        formatted_chunks: list[str],
        authority_refs: set[tuple[str, str]],
    ) -> str:
        """Filter formatted chunks to only include those matching authority references."""
        chunk_pattern = re.compile(
            r'<chunk id="(\d+)" doc_uid="[^"]*" paragraph="([^"]*)"[^>]*>\n(.*?)\n</chunk>',
            re.DOTALL,
        )

        filtered_documents: list[str] = []
        for doc_xml in formatted_chunks:
            if not isinstance(doc_xml, str):
                continue

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
                document_xml = f'<Document name="{self._escape_xml(doc_uid)}" document_type="{self._escape_xml(document_type)}" document_kind="{self._escape_xml(document_kind)}">\n{joined_chunks}\n</Document>'
                filtered_documents.append(document_xml)

        if not filtered_documents:
            logger.error("No chunks matched authority references; falling back to all chunks (authority filtering failed)")
            return "\n\n".join(formatted_chunks)

        return "\n\n".join(filtered_documents)

    def _escape_xml(self, text: str) -> str:
        """Escape special XML characters."""
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

    def _extract_doc_uids_from_context(self, context: str) -> list[str]:
        """Extract document UIDs from the Prompt B context XML.

        Parses the <Document name="..."> tags to get the list of documents
        actually used in Prompt B (after authority filtering).
        """
        doc_uids: list[str] = []
        for match in re.finditer(r'<Document\s+[^>]*name="([^"]+)"[^>]*>', context):
            doc_uid = match.group(1)
            if doc_uid not in doc_uids:
                doc_uids.append(doc_uid)
        return doc_uids

    def _build_chunk_data_for_markdown(self, context: str) -> dict[str, str]:
        """Build chunk data dict from Prompt B context for citation formatting.

        Returns a dict mapping "doc_uid/section" -> chunk text, where section
        is the chunk_number extracted from the chunk XML tags.

        Args:
            context: The formatted Prompt B context XML string

        Returns:
            Dict mapping "doc_uid/section" -> full chunk text
        """
        chunk_data: dict[str, str] = {}

        # Pattern to match <chunk ... paragraph="...">text</chunk>
        chunk_pattern = re.compile(
            r'<chunk id="\d+" doc_uid="([^"]*)" paragraph="([^"]*)"[^>]*>\n(.*?)\n</chunk>',
            re.DOTALL,
        )

        for match in chunk_pattern.finditer(context):
            doc_uid = match.group(1)
            chunk_number = match.group(2)
            chunk_text = match.group(3)

            key = f"{doc_uid}/{chunk_number}"
            chunk_data[key] = chunk_text

        return chunk_data

    def _build_chunk_summary(self, results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> str:
        """Build a one-line-per-document summary of retrieved chunk sections."""
        if not results:
            return "Retrieved chunks:\n- none"

        summaries = build_output_document_sections(results=results, doc_chunks=doc_chunks, logger=logger)
        lines: list[str] = ["Retrieved chunks:"]
        for summary in summaries:
            sections_text = ", ".join(summary.section_labels) if summary.section_labels else "(no sections)"
            lines.append(f"- {summary.doc_uid}: {sections_text}")

        return "\n".join(lines)


def _extract_prompt_content(full_output: str) -> str:
    """Extract only the prompt content, skipping the chunk summary at the top."""
    lines = full_output.split("\n")

    start_idx = 0
    for i, line in enumerate(lines):
        if line.startswith("You are an IFRS expert"):
            start_idx = i
            break

    return "\n".join(lines[start_idx:])


def _default_send_to_llm(prompt: str) -> str:
    """Send prompt to LLM and return the response."""
    try:
        client = get_client()
        logger.info(f"Using LLM provider: {type(client).__name__}")
        return client.generate_text(prompt)
    except ValueError as e:
        error_msg = f"LLM not configured: {e}"
        raise RuntimeError(error_msg) from e


def create_answer_command(
    query: str,
    options: AnswerOptions,
) -> AnswerCommand:
    """Create AnswerCommand with real dependencies."""
    config = AnswerConfig(
        vector_store=VectorStore(),
        chunk_store=ChunkStore(),
        init_db_fn=init_db,
        index_path_fn=get_index_path,
        send_to_llm_fn=_default_send_to_llm,
        reference_store=ContentReferenceStore(),
        section_store=SectionStore(),
        title_vector_store=TitleVectorStore(),
        title_index_path_fn=get_title_index_path,
        document_vector_store=DocumentVectorStore(),
        document_vector_store_factory=lambda representation: DocumentVectorStore(
            index_path=get_document_index_path(representation),
            id_map_path=get_document_id_map_path(representation),
        ),
        document_index_path_fn=get_document_index_path,
    )
    return AnswerCommand(query=query, config=config, options=options)
