"""Query command - search for similar chunks using text query."""

import json
import logging
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from src.db import ChunkStore, init_db
from src.models.chunk import Chunk
from src.vector.store import VectorStore, get_index_path

logger = logging.getLogger(__name__)

RELEVANCE_SCORE_THRESHOLD = 0.3
RELEVANCE_HIGH_THRESHOLD = 0.3


@dataclass
class QueryConfig:
    """Configuration for QueryCommand."""

    vector_store: VectorStore
    chunk_store: ChunkStore
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[], Path]


@dataclass
class QueryOptions:
    """Options for query command."""

    k: int = 5
    min_score: float | None = None
    verbose: bool = True
    expand: int = 0
    full_doc_threshold: int = 0


# Helper functions for chunk expansion (extracted to reduce complexity)
def _init_expansion_data(results: list[dict]) -> tuple[dict[tuple[str, int], float], list[str], dict[str, set[int]]]:
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
    results: list[dict],
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
) -> list[dict]:
    """Build the final expanded results list."""
    expanded_results: list[dict] = []
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


class QueryCommand:
    """Search for similar chunks using text query."""

    def __init__(
        self,
        query: str,
        config: QueryConfig,
        options: QueryOptions | None = None,
    ) -> None:
        """Initialize the query command."""
        self.query = query
        self.k = options.k if options else 5
        self.min_score = options.min_score if options else None
        self.verbose = options.verbose if options else True
        self.expand = options.expand if options else 0
        self.full_doc_threshold = options.full_doc_threshold if options else 0

        self._config = config

    def execute(self) -> str:
        """Execute the query command and return search results."""
        logger.info(f"QueryCommand(query='{self.query[:50]}', k={self.k})")

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
        except Exception as e:
            logger.exception("QueryCommand exception")
            return f"Error: {e}"

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
        index_path = self._config.index_path_fn()
        if not index_path.exists():
            return "Error: No index found. Please run 'store' command first."
        return None

    def _execute_search(self) -> str:
        """Execute the search workflow."""
        ranked_results = self._search_chunks()
        if not ranked_results:
            return "Error: No chunks retrieved"

        selected_results = self._select_results(ranked_results)
        if not selected_results:
            return f"Error: No chunks found with score >= {RELEVANCE_SCORE_THRESHOLD}"

        doc_chunks = self._fetch_chunks(selected_results)

        if self.expand > 0 or self.full_doc_threshold > 0:
            selected_results = self._expand_chunks(selected_results, doc_chunks)

        if not selected_results:
            return "Error: No chunks retrieved"

        return self._format_output(selected_results, doc_chunks)

    def _format_output(self, results: list[dict], doc_chunks: dict[str, list[Chunk]]) -> str:
        """Format and return the output."""
        if not self.verbose:
            chunks_output = self._build_json_output(results, doc_chunks)
            return json.dumps(chunks_output, indent=2, ensure_ascii=False)

        return self._build_verbose_output(results, doc_chunks)

    def _validate_inputs(self) -> str | None:
        """Validate input parameters."""
        if not self.query or not self.query.strip():
            return "Error: Query cannot be empty"

        if self.expand < 0:
            return "Error: expand must be >= 0"

        if self.full_doc_threshold < 0:
            return "Error: full_doc_threshold must be >= 0"

        return None

    def _check_prerequisites(self) -> str | None:
        """Check that required indexes exist."""
        index_path = self._config.index_path_fn()
        if not index_path.exists():
            return "Error: No index found. Please run 'store' command first."

        return None

    def _search_chunks(self) -> list[dict]:
        """Search for relevant chunks."""
        with self._config.vector_store as vector_store:
            ranked_results = vector_store.search_all(self.query)

        logger.info(f"Search returned {len(ranked_results)} raw results")
        return ranked_results

    def _select_results(self, ranked_results: list[dict]) -> list[dict]:
        """Select top-k results per document."""
        effective_min_score = self.min_score if self.min_score is not None else RELEVANCE_SCORE_THRESHOLD
        logger.info(f"Effective min_score: {effective_min_score}")

        selected_results = self._select_top_k_per_document(ranked_results, self.k, effective_min_score)
        logger.info(f"Per-document selection: {len(selected_results)} chunks")

        return selected_results

    def _select_top_k_per_document(
        self,
        ranked_results: list[dict],
        k: int,
        min_score: float,
    ) -> list[dict]:
        """Select up to k chunks per document above the score threshold."""
        selected_results: list[dict] = []
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

    def _fetch_chunks(self, selected_results: list[dict]) -> dict[str, list[Chunk]]:
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
        results: list[dict],
        doc_chunks: dict[str, list[Chunk]],
    ) -> list[dict]:
        """Expand results by including surrounding chunks from each document."""
        result_score_by_chunk, doc_order, selected_ids_by_doc = _init_expansion_data(results)

        full_doc_docs = _include_full_document(doc_chunks, selected_ids_by_doc, self.full_doc_threshold)

        if self.expand > 0:
            _expand_with_neighbour_chunks(results, doc_chunks, selected_ids_by_doc, self.expand)

        expanded_results = _build_expanded_results(doc_order, doc_chunks, selected_ids_by_doc, result_score_by_chunk)

        if self.full_doc_threshold > 0:
            for doc_uid in full_doc_docs:
                doc_size = sum(len(c.text) for c in doc_chunks.get(doc_uid, []))
                logger.info(f"Full doc inclusion: {doc_uid} (size={doc_size} < threshold={self.full_doc_threshold})")

        return expanded_results

    def _build_json_output(self, results: list[dict], doc_chunks: dict[str, list[Chunk]]) -> list[dict]:
        """Build JSON output."""
        chunks_output = []
        for result in results:
            doc_uid = result["doc_uid"]
            chunk_id = result["chunk_id"]
            score = result["score"]

            for chunk in doc_chunks.get(doc_uid, []):
                if chunk.chunk_id == chunk_id:
                    relevance = "High" if score >= RELEVANCE_HIGH_THRESHOLD else "Low"
                    chunks_output.append(
                        {
                            "id": chunk.chunk_id,
                            "doc_uid": chunk.doc_uid,
                            "section_path": chunk.section_path,
                            "page_start": chunk.page_start,
                            "page_end": chunk.page_end,
                            "text": chunk.text,
                            "score": round(score, 4),
                            "relevance": relevance,
                        },
                    )
                    break
        return chunks_output

    def _build_verbose_output(self, results: list[dict], doc_chunks: dict[str, list[Chunk]]) -> str:
        """Build verbose text output."""
        output_lines = []
        for result in results:
            doc_uid = result["doc_uid"]
            chunk_id = result["chunk_id"]
            score = result["score"]

            for chunk in doc_chunks.get(doc_uid, []):
                if chunk.chunk_id == chunk_id:
                    relevance = "High" if score >= RELEVANCE_HIGH_THRESHOLD else "Low"
                    output_lines.append(f"\n--- Score: {score:.4f} ({relevance}) ---")
                    output_lines.append(f"Document: {chunk.doc_uid}")
                    output_lines.append(f"Section: {chunk.section_path}")
                    output_lines.append(f"Page: {chunk.page_start}-{chunk.page_end}")
                    snippet = chunk.text[:200].replace("\n", " ")
                    output_lines.append(f"Snippet: {snippet}...")
                    break
        return "\n".join(output_lines)


def create_query_command(
    query: str,
    options: QueryOptions | None = None,
) -> QueryCommand:
    """Create QueryCommand with real dependencies."""
    config = QueryConfig(
        vector_store=VectorStore(),
        chunk_store=ChunkStore(),
        init_db_fn=init_db,
        index_path_fn=get_index_path,
    )
    return QueryCommand(query=query, config=config, options=options)
