"""Query command - search for similar chunks using text query."""

import json

from src.db import ChunkStore, init_db
from src.db.chunks import Chunk as DbChunk
from src.vector import VectorStore
from src.vector.store import get_index_path


class QueryCommand:
    """Search for similar chunks using text query."""

    def __init__(self, query: str, k: int = 5, min_score: float | None = None, verbose: bool = True):
        self.query = query
        self.k = k
        self.min_score = min_score
        self.verbose = verbose

    def execute(self) -> str:
        try:
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
                    return "[]" if not self.verbose else f"No chunks found with score >= {self.min_score}"

            # Get the chunk details from database
            init_db()

            # Group results by doc_uid to minimize DB calls
            doc_uids = list({result["doc_uid"] for result in results})

            with ChunkStore() as store:
                # Fetch all chunks for all relevant docs at once
                doc_chunks: dict[str, list[DbChunk]] = {}
                for doc_uid in doc_uids:
                    doc_chunks[doc_uid] = store.get_chunks_by_doc(doc_uid)

                # Build output
                if not self.verbose:
                    chunks_output = self._build_json_output(results, doc_chunks)
                    return json.dumps(chunks_output, indent=2, ensure_ascii=False)
                else:
                    return self._build_verbose_output(results, doc_chunks)

        except Exception as e:
            return f"Error: {e}"

    def _build_json_output(self, results: list[dict], doc_chunks: dict[str, list[DbChunk]]) -> list[dict]:
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

    def _build_verbose_output(self, results: list[dict], doc_chunks: dict[str, list[DbChunk]]) -> str:
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
