"""Query command - search for similar chunks using text query."""

import json

from src.db import ChunkStore, init_db
from src.db.chunks import Chunk as DbChunk
from src.vector import VectorStore
from src.vector.store import get_index_path


class QueryCommand:
    """Search for similar chunks using text query."""

    def __init__(
        self,
        query: str,
        k: int = 5,
        min_score: float | None = None,
        verbose: bool = True,
        expand: int = 0,
    ):
        self.query = query
        self.k = k
        self.min_score = min_score
        self.verbose = verbose
        self.expand = expand

    def execute(self) -> str:
        try:
            # Validate query is not empty
            if not self.query or not self.query.strip():
                return "[]" if not self.verbose else "No matching chunks found"

            if self.expand < 0:
                return "Error: expand must be >= 0"

            # Check if index exists
            index_path = get_index_path()
            if not index_path.exists():
                return "Error: No index found. Please run 'store' command first."

            # Search for similar chunks (get more results to filter by min_score)
            search_k = self.k * 3 if self.min_score else self.k
            with VectorStore() as vector_store:
                results = vector_store.search(self.query, k=search_k)

            if not results:
                return "[]" if not self.verbose else "No matching chunks found"

            # Filter by minimum score if specified
            if self.min_score is not None:
                results = [r for r in results if r["score"] >= self.min_score]
                if not results:
                    return (
                        "[]"
                        if not self.verbose
                        else f"No chunks found with score >= {self.min_score}"
                    )

            # Get the chunk details from database
            init_db()

            # Group results by doc_uid to minimize DB calls
            doc_uids = list({result["doc_uid"] for result in results})

            with ChunkStore() as store:
                # Fetch all chunks for all relevant docs at once
                doc_chunks: dict[str, list[DbChunk]] = {}
                for doc_uid in doc_uids:
                    doc_chunks[doc_uid] = store.get_chunks_by_doc(doc_uid)

                # Expand chunks if requested
                if self.expand > 0:
                    results = self._expand_chunks(results, doc_chunks, self.expand)

                # Build output
                if not self.verbose:
                    chunks_output = self._build_json_output(results, doc_chunks)
                    return json.dumps(chunks_output, indent=2, ensure_ascii=False)
                else:
                    return self._build_verbose_output(results, doc_chunks)

        except Exception as e:
            return f"Error: {e}"

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
    ) -> list[dict]:
        """Expand results by including surrounding chunks from each document.

        For each retrieved chunk, find the expand chunks before and after it
        in the same document, deduplicate them, and return them in document order.

        Args:
            results: Original search results
            doc_chunks: Dictionary mapping doc_uid to list of chunks
            expand: Number of chunks before/after to include

        Returns:
            Expanded results with additional chunks
        """
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

            chunks = doc_chunks.get(doc_uid, [])
            if not chunks:
                continue

            for idx, chunk in enumerate(chunks):
                if chunk.chunk_id == chunk_id:
                    start_idx = max(0, idx - expand)
                    end_idx = min(len(chunks), idx + expand + 1)
                    for surrounding_chunk in chunks[start_idx:end_idx]:
                        if surrounding_chunk.chunk_id is not None:
                            selected_ids_by_doc[doc_uid].add(surrounding_chunk.chunk_id)
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

        return expanded_results
