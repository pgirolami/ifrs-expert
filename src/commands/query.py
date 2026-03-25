"""Query command - search for similar chunks using text query."""

import json
import logging

from src.db import ChunkStore, init_db
from src.db.chunks import Chunk as DbChunk
from src.vector import VectorStore
from src.vector.store import get_index_path

logger = logging.getLogger(__name__)

RELEVANCE_SCORE_THRESHOLD = 0.3


class QueryCommand:
    """Search for similar chunks using text query."""

    def __init__(
        self,
        query: str,
        k: int = 5,
        min_score: float | None = None,
        verbose: bool = True,
        expand: int = 0,
        full_doc_threshold: int = 0,
    ):
        self.query = query
        self.k = k
        self.min_score = min_score
        self.verbose = verbose
        self.expand = expand
        self.full_doc_threshold = full_doc_threshold

    def execute(self) -> str:
        try:
            logger.info(
                f"QueryCommand(query='{self.query[:50]}', k={self.k}, expand={self.expand}, "
                f"full_doc_threshold={self.full_doc_threshold}, min_score={self.min_score})"
            )

            # Validate query is not empty
            if not self.query or not self.query.strip():
                return "Error: Query cannot be empty"

            if self.expand < 0:
                return "Error: expand must be >= 0"

            if self.full_doc_threshold < 0:
                return "Error: full_doc_threshold must be >= 0"

            # Check if index exists
            index_path = get_index_path()
            if not index_path.exists():
                return "Error: No index found. Please run 'store' command first."

            with VectorStore() as vector_store:
                ranked_results = vector_store.search_all(self.query)

            logger.info(f"Search returned {len(ranked_results)} raw results")

            if not ranked_results:
                return "Error: No chunks retrieved"

            effective_min_score = max(
                RELEVANCE_SCORE_THRESHOLD,
                self.min_score if self.min_score is not None else RELEVANCE_SCORE_THRESHOLD,
            )
            logger.info(f"Effective min_score: {effective_min_score}")

            selected_results = self._select_top_k_per_document(
                ranked_results,
                k=self.k,
                min_score=effective_min_score,
            )

            if not selected_results:
                return f"Error: No chunks found with score >= {effective_min_score}"

            # Log per-document selection summary
            counts_by_doc: dict[str, int] = {}
            for r in selected_results:
                counts_by_doc[r["doc_uid"]] = counts_by_doc.get(r["doc_uid"], 0) + 1
            doc_summary = ", ".join(f"{doc}({n})" for doc, n in counts_by_doc.items())
            logger.info(
                f"Per-document selection: {len(selected_results)} chunks from "
                f"{len(counts_by_doc)} doc(s) - {doc_summary}"
            )

            # Get the chunk details from database
            init_db()

            # Group results by doc_uid to minimize DB calls
            doc_uids = list({result["doc_uid"] for result in selected_results})

            with ChunkStore() as store:
                # Fetch all chunks for all relevant docs at once
                doc_chunks: dict[str, list[DbChunk]] = {}
                for doc_uid in doc_uids:
                    doc_chunks[doc_uid] = store.get_chunks_by_doc(doc_uid)

                # Expand chunks if requested
                if self.expand > 0 or self.full_doc_threshold > 0:
                    selected_results = self._expand_chunks(
                        selected_results,
                        doc_chunks,
                        self.expand,
                        self.full_doc_threshold,
                    )

                # Fail if no chunks remain after expansion
                if not selected_results:
                    return "Error: No chunks retrieved"

                final_counts_by_doc: dict[str, int] = {}
                for r in selected_results:
                    final_counts_by_doc[r["doc_uid"]] = final_counts_by_doc.get(r["doc_uid"], 0) + 1
                final_doc_summary = ", ".join(
                    f"{doc}({n})" for doc, n in final_counts_by_doc.items()
                )
                logger.info(
                    f"Final retrieval: {len(selected_results)} chunks from "
                    f"{len(final_counts_by_doc)} doc(s) - {final_doc_summary}"
                )

                # Build output
                if not self.verbose:
                    chunks_output = self._build_json_output(selected_results, doc_chunks)
                    return json.dumps(chunks_output, indent=2, ensure_ascii=False)
                else:
                    return self._build_verbose_output(selected_results, doc_chunks)

        except Exception as e:
            logger.exception("QueryCommand exception")
            return f"Error: {e}"

    def _select_top_k_per_document(
        self,
        ranked_results: list[dict],
        k: int,
        min_score: float,
    ) -> list[dict]:
        """Select up to k chunks per document above the score threshold."""
        selected_results: list[dict] = []
        counts_by_doc: dict[str, int] = {}
        skipped_low_score = 0
        skipped_doc_full = 0

        for result in ranked_results:
            if result["score"] < min_score:
                skipped_low_score += 1
                continue

            doc_uid = result["doc_uid"]
            doc_count = counts_by_doc.get(doc_uid, 0)
            if doc_count >= k:
                skipped_doc_full += 1
                continue

            selected_results.append(result)
            counts_by_doc[doc_uid] = doc_count + 1

        logger.info(
            f"Selection filters: {skipped_low_score} below min_score, "
            f"{skipped_doc_full} skipped because doc already had {k} chunk(s)"
        )
        return selected_results

    def _build_json_output(
        self, results: list[dict], doc_chunks: dict[str, list[DbChunk]]
    ) -> list[dict]:
        """Build JSON output."""
        chunks_output = []
        for result in results:
            doc_uid = result["doc_uid"]
            chunk_id = result["chunk_id"]
            score = result["score"]

            # Find matching chunk
            for chunk in doc_chunks.get(doc_uid, []):
                if chunk.chunk_id == chunk_id:
                    relevance = "High" if score >= 0.3 else "Low"
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
                        }
                    )
                    break
        return chunks_output

    def _build_verbose_output(
        self, results: list[dict], doc_chunks: dict[str, list[DbChunk]]
    ) -> str:
        """Build verbose text output."""
        output_lines = []
        for result in results:
            doc_uid = result["doc_uid"]
            chunk_id = result["chunk_id"]
            score = result["score"]

            # Find matching chunk
            for chunk in doc_chunks.get(doc_uid, []):
                if chunk.chunk_id == chunk_id:
                    relevance = "High" if score >= 0.3 else "Low"
                    output_lines.append(f"\n--- Score: {score:.4f} ({relevance}) ---")
                    output_lines.append(f"Document: {chunk.doc_uid}")
                    output_lines.append(f"Section: {chunk.section_path}")
                    output_lines.append(f"Page: {chunk.page_start}-{chunk.page_end}")
                    # Print snippet (first 200 chars)
                    snippet = chunk.text[:200].replace("\n", " ")
                    output_lines.append(f"Snippet: {snippet}...")
                    break
        return "\n".join(output_lines)

    def _expand_chunks(
        self,
        results: list[dict],
        doc_chunks: dict[str, list[DbChunk]],
        expand: int,
        full_doc_threshold: int,
    ) -> list[dict]:
        """Expand results by including surrounding chunks from each document.

        For each retrieved chunk, find the expand chunks before and after it
        in the same document. If the total text size of a retrieved document is
        below the full_doc_threshold, include the whole document instead.
        Deduplicate results and return them in document order.
        """
        result_score_by_chunk: dict[tuple[str, int], float] = {}
        doc_order: list[str] = []
        selected_ids_by_doc: dict[str, set[int]] = {}
        full_doc_docs: set[str] = set()
        expanded_via_neighbours: set[tuple[str, int]] = set()

        for result in results:
            doc_uid = result["doc_uid"]
            chunk_id = result["chunk_id"]
            score = result["score"]

            if doc_uid not in selected_ids_by_doc:
                selected_ids_by_doc[doc_uid] = set()
                doc_order.append(doc_uid)

            result_score_by_chunk[(doc_uid, chunk_id)] = score

            chunks = doc_chunks.get(doc_uid, [])
            if not chunks:
                continue

            doc_text_size = sum(len(chunk.text) for chunk in chunks)
            if full_doc_threshold > 0 and doc_text_size < full_doc_threshold:
                full_doc_docs.add(doc_uid)
                for document_chunk in chunks:
                    if document_chunk.chunk_id is not None:
                        selected_ids_by_doc[doc_uid].add(document_chunk.chunk_id)
                continue

            for idx, chunk in enumerate(chunks):
                if chunk.chunk_id == chunk_id:
                    start_idx = max(0, idx - expand)
                    end_idx = min(len(chunks), idx + expand + 1)
                    for i, surrounding_chunk in enumerate(chunks[start_idx:end_idx]):
                        if surrounding_chunk.chunk_id is not None:
                            selected_ids_by_doc[doc_uid].add(surrounding_chunk.chunk_id)
                            if surrounding_chunk.chunk_id != chunk_id:
                                expanded_via_neighbours.add((doc_uid, surrounding_chunk.chunk_id))
                    break

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
                    }
                )

        if full_doc_threshold > 0:
            for doc_uid in full_doc_docs:
                doc_size = sum(len(c.text) for c in doc_chunks.get(doc_uid, []))
                logger.info(
                    f"Full doc inclusion: {doc_uid} "
                    f"(size={doc_size} < threshold={full_doc_threshold})"
                )
        if expand > 0:
            neighbour_summary: dict[str, set[int]] = {}
            for doc_uid, chunk_id in expanded_via_neighbours:
                neighbour_summary.setdefault(doc_uid, set()).add(chunk_id)
            for doc_uid, chunk_ids in neighbour_summary.items():
                logger.info(
                    f"Neighbour expansion: {doc_uid} - added {len(chunk_ids)} surrounding chunk(s)"
                )

        return expanded_results
