"""Answer command - retrieve chunks and run the two-step answer pipeline."""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

from src.b_response_utils import convert_json_to_markdown
from src.commands.constants import (
    DEFAULT_EXPAND,
    DEFAULT_FULL_DOC_THRESHOLD,
    DEFAULT_MIN_SCORE,
    DEFAULT_RETRIEVAL_K,
)
from src.db import ChunkStore, init_db
from src.llm import get_client
from src.models.answer_command_result import AnswerCommandResult, JSONValue
from src.vector.store import VectorStore, get_index_path

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.interfaces import ReadChunkStoreProtocol, SearchResult, SearchVectorStoreProtocol
    from src.models.chunk import Chunk

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


@dataclass
class AnswerOptions:
    """Options for answer command."""

    k: int = DEFAULT_RETRIEVAL_K
    min_score: float | None = DEFAULT_MIN_SCORE
    expand: int = DEFAULT_EXPAND
    full_doc_threshold: int = DEFAULT_FULL_DOC_THRESHOLD
    output_dir: Path | None = None
    save_all: bool = False


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
                if document_chunk.chunk_id is not None:
                    selected_ids_by_doc[doc_uid].add(document_chunk.chunk_id)

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
            if chunk.chunk_id == chunk_id:
                start_idx = max(0, idx - expand)
                end_idx = min(len(chunks), idx + expand + 1)
                for surrounding_chunk in chunks[start_idx:end_idx]:
                    if surrounding_chunk.chunk_id is not None:
                        selected_ids_by_doc[doc_uid].add(surrounding_chunk.chunk_id)
                        if surrounding_chunk.chunk_id != chunk_id:
                            expanded_via_neighbours.add((doc_uid, surrounding_chunk.chunk_id))
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
            chunk_id = chunk.chunk_id
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


class AnswerCommand:
    """Retrieve chunks and run the two-step answer pipeline."""

    def __init__(
        self,
        query: str,
        config: AnswerConfig,
        options: AnswerOptions | None = None,
    ) -> None:
        """Initialize the answer command."""
        self.query = query
        self.k = options.k if options else DEFAULT_RETRIEVAL_K
        self.min_score = options.min_score if options and options.min_score is not None else DEFAULT_MIN_SCORE
        self.expand = options.expand if options else DEFAULT_EXPAND
        self.full_doc_threshold = options.full_doc_threshold if options else DEFAULT_FULL_DOC_THRESHOLD

        self._retrieved_doc_uids: list[str] = []
        self._config = config

    def execute(self) -> AnswerCommandResult:
        """Execute the answer command and return the run artifacts."""
        logger.info(f"AnswerCommand(query='{self.query[:50]}', k={self.k}, expand={self.expand}, f={self.full_doc_threshold}, min-score={self.min_score})")

        validation_error = self._get_validation_error()
        if validation_error:
            return AnswerCommandResult.failure(query=self.query, error=validation_error, error_stage="validation")

        prerequisite_error = self._get_prerequisite_error()
        if prerequisite_error:
            return AnswerCommandResult.failure(query=self.query, error=prerequisite_error, error_stage="prerequisite")

        try:
            return self._execute_workflow()
        except Exception as e:
            logger.exception("Error executing answer command")
            return AnswerCommandResult.failure(query=self.query, error=f"Error: {e}", error_stage="workflow")

    def _get_validation_error(self) -> str | None:
        """Get validation error or None."""
        if not self.query or not self.query.strip():
            return "Error: Query cannot be empty"
        if self.expand < 0:
            return "Error: expand must be >= 0"
        if self.full_doc_threshold < 0:
            return "Error: full_doc_threshold must be >= 0"
        return None

    def _get_prerequisite_error(self) -> str | None:
        """Get prerequisite error or None."""
        if not _prompt_file_exists(PROMPT_A_PATH):
            logger.error(f"Missing Prompt A template at {PROMPT_A_PATH}")
            return "Error: Prompt A template not found."
        if not _prompt_file_exists(PROMPT_B_PATH):
            logger.error(f"Missing Prompt B template at {PROMPT_B_PATH}")
            return "Error: Prompt B template not found."

        index_path = self._config.index_path_fn()
        if not index_path.exists():
            logger.error(f"Missing vector index at {index_path}; corpus must be built before running the answer pipeline")
            return "Error: No index found. Please run 'store' command first."
        return None

    def _execute_workflow(self) -> AnswerCommandResult:
        """Execute the main workflow."""
        ranked_results = self._search_chunks()
        if not ranked_results:
            return AnswerCommandResult.failure(query=self.query, error="Error: No chunks retrieved", error_stage="retrieval")

        selected_results = self._select_results(ranked_results)
        if not selected_results:
            return AnswerCommandResult.failure(
                query=self.query,
                error=f"Error: No chunks found with score >= {self.min_score}",
                error_stage="retrieval",
            )

        doc_chunks = self._fetch_chunks(selected_results)

        if self.expand > 0 or self.full_doc_threshold > 0:
            selected_results = self._expand_chunks(selected_results, doc_chunks)

        result = AnswerCommandResult(query=self.query, retrieved_doc_uids=list(self._retrieved_doc_uids))
        return self._process_prompts(result, selected_results, doc_chunks)

    def _search_chunks(self) -> list[SearchResult]:
        """Search for relevant chunks."""
        with self._config.vector_store as vector_store:
            ranked_results = vector_store.search_all(self.query)

        logger.info(f"Search returned {len(ranked_results)} raw results")
        if ranked_results:
            top_result = ranked_results[0]
            logger.info(f"Top retrieved chunk: doc_uid={top_result['doc_uid']}, chunk_id={top_result['chunk_id']}, score={top_result['score']:.4f}")
        else:
            logger.warning(f"What ?? {ranked_results}")

        return ranked_results

    def _select_results(self, ranked_results: list[SearchResult]) -> list[SearchResult]:
        """Select top-k results per document."""
        selected_results = self._select_top_k_per_document(ranked_results, self.k, self.min_score)
        logger.info(f"{len(selected_results)} chunks with score≥{self.min_score} out of the original {len(ranked_results)}")

        return selected_results

    def _select_top_k_per_document(
        self,
        ranked_results: list[SearchResult],
        k: int,
        min_score: float,
    ) -> list[SearchResult]:
        """Select up to k chunks per document above the score threshold."""
        selected_results: list[SearchResult] = []
        counts_by_doc: dict[str, int] = {}

        for result in ranked_results:
            if result["score"] < min_score:
                continue

            doc_uid = result["doc_uid"]
            if counts_by_doc.get(doc_uid, 0) >= k:
                continue

            selected_results.append(result)
            counts_by_doc[doc_uid] = counts_by_doc.get(doc_uid, 0) + 1

        return selected_results

    def _fetch_chunks(self, selected_results: list[SearchResult]) -> dict[str, list[Chunk]]:
        """Fetch chunk details from database."""
        self._config.init_db_fn()

        doc_uids = list({result["doc_uid"] for result in selected_results})
        self._retrieved_doc_uids = doc_uids

        doc_chunks: dict[str, list[Chunk]] = {}
        with self._config.chunk_store as store:
            for doc_uid in doc_uids:
                doc_chunks[doc_uid] = store.get_chunks_by_doc(doc_uid)

        return doc_chunks

    def _expand_chunks(
        self,
        results: list[SearchResult],
        doc_chunks: dict[str, list[Chunk]],
    ) -> list[SearchResult]:
        """Expand results by including surrounding chunks from each document."""
        result_score_by_chunk, doc_order, selected_ids_by_doc = _init_expansion_data(results)

        full_doc_docs = _include_full_document(doc_chunks, selected_ids_by_doc, self.full_doc_threshold)

        if self.expand > 0:
            _expand_with_neighbour_chunks(results, doc_chunks, selected_ids_by_doc, self.expand)

        expanded_results = _build_expanded_results(doc_order, doc_chunks, selected_ids_by_doc, result_score_by_chunk)

        if self.full_doc_threshold > 0:
            for doc_uid in full_doc_docs:
                doc_size = sum(len(chunk.text) for chunk in doc_chunks.get(doc_uid, []))
                logger.info(f"Full doc inclusion: {doc_uid} (size={doc_size} < threshold={self.full_doc_threshold})")

        return expanded_results

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

        result.prompt_b_text = self._build_prompt_b(
            "\n\n".join(formatted_chunks), json.dumps(result.prompt_a_json, indent=2, ensure_ascii=False)
        )

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
                    result.prompt_b_markdown = convert_json_to_markdown(
                        result.prompt_b_json,
                        question=self.query,
                        doc_uids=self._retrieved_doc_uids,
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
                chunk_id = chunk.chunk_id
                if chunk_id is None:
                    continue
                if chunk_id not in chunk_ids_by_doc.get(doc_uid, set()):
                    continue

                score = score_by_chunk.get((doc_uid, chunk_id), 0.0)
                chunk_xml = f'<chunk id="{chunk_id}" doc_uid="{self._escape_xml(doc_uid)}" section_path="{self._escape_xml(chunk.section_path)}" score="{score:.4f}">\n{chunk.text}\n</chunk>'
                formatted_chunks.append(chunk_xml)

            joined_chunks = "\n\n".join(formatted_chunks)
            document_xml = f'<Document name="{self._escape_xml(doc_uid)}">\n{joined_chunks}\n</Document>'
            formatted_documents.append(document_xml)

        return formatted_documents

    def _escape_xml(self, text: str) -> str:
        """Escape special XML characters."""
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

    def _build_chunk_summary(self, results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> str:
        """Build a one-line-per-document summary of retrieved chunk sections."""
        if not results:
            return "Retrieved chunks:\n- none"

        doc_order: list[str] = []
        chunk_ids_by_doc: dict[str, set[int]] = {}
        for result in results:
            doc_uid = result["doc_uid"]
            chunk_id = result["chunk_id"]
            if doc_uid not in chunk_ids_by_doc:
                chunk_ids_by_doc[doc_uid] = set()
                doc_order.append(doc_uid)
            chunk_ids_by_doc[doc_uid].add(chunk_id)

        lines: list[str] = ["Retrieved chunks:"]
        for doc_uid in doc_order:
            seen_sections: set[str] = set()
            ordered_sections: list[str] = []
            for chunk in doc_chunks.get(doc_uid, []):
                chunk_id = chunk.chunk_id
                if chunk_id is None:
                    continue
                if chunk_id not in chunk_ids_by_doc.get(doc_uid, set()):
                    continue
                section_label = chunk.section_path or f"chunk {chunk_id}"
                if section_label in seen_sections:
                    continue
                seen_sections.add(section_label)
                ordered_sections.append(section_label)

            sections_text = ", ".join(ordered_sections) if ordered_sections else "(no sections)"
            lines.append(f"- {doc_uid}: {sections_text}")

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
    options: AnswerOptions | None = None,
) -> AnswerCommand:
    """Create AnswerCommand with real dependencies."""
    config = AnswerConfig(
        vector_store=VectorStore(),
        chunk_store=ChunkStore(),
        init_db_fn=init_db,
        index_path_fn=get_index_path,
        send_to_llm_fn=_default_send_to_llm,
    )
    return AnswerCommand(query=query, config=config, options=options)
