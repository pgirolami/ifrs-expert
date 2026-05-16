"""Query command - search for similar chunks using text query."""

import json
import logging
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from src.commands.constants import DEFAULT_VERBOSE
from src.commands.retrieval_request_builder import RetrievalRequestOverrides, build_retrieval_request
from src.db import ChunkStore, ContentReferenceStore, init_db
from src.interfaces import ReadChunkStoreProtocol, ReferenceStoreProtocol, SearchResult, SearchVectorStoreProtocol
from src.models.chunk import Chunk
from src.models.document import infer_document_kind, infer_exact_document_type
from src.models.provenance import Provenance
from src.policy import ResolvedRetrievalPolicy
from src.retrieval.pipeline import RetrievalPipelineConfig, execute_retrieval
from src.vector.store import VectorStore, get_index_path

logger = logging.getLogger(__name__)

RELEVANCE_HIGH_THRESHOLD = 0.3


@dataclass
class QueryConfig:
    """Configuration for QueryCommand."""

    vector_store: SearchVectorStoreProtocol
    chunk_store: ReadChunkStoreProtocol
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[], Path]
    reference_store: ReferenceStoreProtocol | None = None


@dataclass
class QueryOptions:
    """Options for query command."""

    policy: ResolvedRetrievalPolicy
    verbose: bool = DEFAULT_VERBOSE


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


class QueryCommand:
    """Search for similar chunks using text query."""

    def __init__(
        self,
        query: str,
        config: QueryConfig,
        options: QueryOptions,
    ) -> None:
        """Initialize the query command."""
        self.query = query
        self._options = options
        self.verbose = options.verbose
        self._config = config

    def execute(self) -> str:
        """Execute the query command and return search results."""
        policy = self._options.policy
        chunk_profile = policy.chunk_retrieval.profile_config
        logger.info(f"QueryCommand(query='{self.query[:50]}', k={chunk_profile.filter.per_document_k})")

        # Validate inputs - collect errors first
        validation_error = self._get_validation_error()
        if validation_error:
            return validation_error

        # Check prerequisites
        prereq_error = self._get_prerequisite_error()
        if prereq_error:
            return prereq_error

        try:
            return self._execute_search()
        except (RuntimeError, ValueError) as error:
            logger.exception(f"Query command failed for query={self.query[:50]}")
            return f"Error: {error}"

    def _get_validation_error(self) -> str | None:
        """Get validation error or None."""
        if not self.query or not self.query.strip():
            return "Error: Query cannot be empty"
        policy = self._options.policy
        chunk_profile = policy.chunk_retrieval.profile_config
        expansion = chunk_profile.expansion
        if policy.chunk_retrieval.mode != "chunk_similarity":
            return "Error: query command requires chunk_similarity retrieval policy"
        if expansion is not None and expansion.expand < 0:
            return "Error: expand must be >= 0"
        if expansion is not None and expansion.full_doc_threshold < 0:
            return "Error: full_doc_threshold must be >= 0"
        return None

    def _get_prerequisite_error(self) -> str | None:
        """Get prerequisite error or None."""
        index_path = self._config.index_path_fn()
        if not index_path.exists():
            logger.error(f"Missing vector index at {index_path}; corpus must be built before running queries")
            return "Error: No index found. Please run 'store' command first."
        return None

    def _execute_search(self) -> str:
        """Execute the search workflow."""
        policy = self._options.policy
        chunk_profile = policy.chunk_retrieval.profile_config
        expansion = chunk_profile.expansion
        error, retrieval_result = execute_retrieval(
            request=build_retrieval_request(
                query=self.query,
                policy=policy,
                chunk_min_score=chunk_profile.filter.min_score,
                expand_to_section=expansion.expand_to_section if expansion is not None else False,
                overrides=RetrievalRequestOverrides(
                    policy_name=policy.policy_name,
                    document_routing_source="all_documents",
                    document_routing_post_processing="none",
                    chunk_retrieval_mode="chunk_similarity",
                ),
            ),
            config=RetrievalPipelineConfig(
                vector_store=self._config.vector_store,
                chunk_store=self._config.chunk_store,
                init_db_fn=self._config.init_db_fn,
                index_path_fn=self._config.index_path_fn,
                reference_store=self._config.reference_store,
            ),
        )
        if error is not None:
            return error
        if retrieval_result is None:
            return "Error: Retrieval did not return a result"
        return self._format_output(retrieval_result.chunk_results, retrieval_result.doc_chunks)

    def _format_output(self, results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> str:
        """Format and return the output."""
        if not self.verbose:
            chunks_output = self._build_json_output(results, doc_chunks)
            return json.dumps(chunks_output, indent=2, ensure_ascii=False)

        verbose_output = self._build_verbose_output(results, doc_chunks)
        return f"{self._options}\n{verbose_output}"

    def _check_prerequisites(self) -> str | None:
        """Check that required indexes exist."""
        index_path = self._config.index_path_fn()
        if not index_path.exists():
            logger.error(f"Missing vector index at {index_path}; corpus must be built before running queries")
            return "Error: No index found. Please run 'store' command first."

        return None

    def _fetch_chunks(self, selected_results: list[SearchResult]) -> dict[str, list[Chunk]]:
        """Fetch chunk details from database."""
        self._config.init_db_fn()

        doc_uids = list({result["doc_uid"] for result in selected_results})

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

        policy = self._options.policy
        chunk_profile = policy.chunk_retrieval.profile_config
        expansion = chunk_profile.expansion
        full_doc_docs = _include_full_document(doc_chunks, selected_ids_by_doc, expansion.full_doc_threshold if expansion is not None else 0)

        if expansion is not None and expansion.expand > 0:
            _expand_with_neighbour_chunks(results, doc_chunks, selected_ids_by_doc, expansion.expand)

        expanded_results = _build_expanded_results(doc_order, doc_chunks, selected_ids_by_doc, result_score_by_chunk)

        if expansion is not None and expansion.full_doc_threshold > 0:
            for doc_uid in full_doc_docs:
                doc_size = sum(len(c.text) for c in doc_chunks.get(doc_uid, []))
                logger.info(f"Full doc inclusion: {doc_uid} (size={doc_size} < threshold={expansion.full_doc_threshold})")

        return expanded_results

    def _build_json_output(self, results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> list[SearchResult]:
        """Build JSON output."""
        chunks_output = []
        for result in results:
            doc_uid = result["doc_uid"]
            chunk_id = result["chunk_id"]
            score = result["score"]

            for chunk in doc_chunks.get(doc_uid, []):
                if chunk.id == chunk_id:
                    document_type = infer_exact_document_type(doc_uid)
                    document_kind = infer_document_kind(doc_uid)
                    relevance = "High" if score >= RELEVANCE_HIGH_THRESHOLD else "Low"
                    chunks_output.append(
                        {
                            "id": chunk.id,
                            "doc_uid": chunk.doc_uid,
                            "document_type": document_type,
                            "document_kind": document_kind,
                            "chunk_number": chunk.chunk_number,
                            "chunk_id": chunk.chunk_id,
                            "containing_section_id": chunk.containing_section_id,
                            "page_start": chunk.page_start,
                            "page_end": chunk.page_end,
                            "text": chunk.text,
                            "score": round(score, 4),
                            "relevance": relevance,
                            "provenance": Provenance(result["provenance"]).value,
                        },
                    )
                    break
        return chunks_output

    def _build_verbose_output(self, results: list[SearchResult], doc_chunks: dict[str, list[Chunk]]) -> str:
        """Build verbose text output."""
        output_lines = []
        for result in results:
            doc_uid = result["doc_uid"]
            chunk_id = result["chunk_id"]
            score = result["score"]

            for chunk in doc_chunks.get(doc_uid, []):
                if chunk.id == chunk_id:
                    document_type = infer_exact_document_type(doc_uid)
                    document_kind = infer_document_kind(doc_uid)
                    relevance = "High" if score >= RELEVANCE_HIGH_THRESHOLD else "Low"
                    output_lines.append(f"\n--- Score: {score:.4f} ({relevance}) ---")
                    output_lines.append(f"Provenance: {Provenance(result['provenance']).value}")
                    output_lines.append(f"Document: {chunk.doc_uid}")
                    output_lines.append(f"Document type: {document_type}")
                    output_lines.append(f"Document kind: {document_kind}")
                    output_lines.append(f"Chunk number: {chunk.chunk_number}")
                    output_lines.append(f"Page: {chunk.page_start}-{chunk.page_end}")
                    snippet = chunk.text[:200].replace("\n", " ")
                    output_lines.append(f"Snippet: {snippet}...")
                    break
        return "\n".join(output_lines)


def create_query_command(
    query: str,
    options: QueryOptions,
) -> QueryCommand:
    """Create QueryCommand with real dependencies."""
    config = QueryConfig(
        vector_store=VectorStore(),
        chunk_store=ChunkStore(),
        init_db_fn=init_db,
        index_path_fn=get_index_path,
        reference_store=ContentReferenceStore(),
    )
    return QueryCommand(query=query, config=config, options=options)
