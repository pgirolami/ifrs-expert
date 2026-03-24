"""Answer command - retrieve chunks and embed them into a prompt template."""

import logging
from pathlib import Path

from src.db import ChunkStore, init_db
from src.db.chunks import Chunk as DbChunk
from src.vector import VectorStore
from src.vector.store import get_index_path

RELEVANCE_SCORE_THRESHOLD = 0.3

logger = logging.getLogger(__name__)

# Path to the prompt template file
PROMPT_TEMPLATE_PATH = Path(__file__).parent.parent.parent / "prompts" / "answer_prompt.txt"


def _read_prompt_template(path: Path) -> str:
    """Read the prompt template from file.

    Args:
        path: Path to the template file

    Returns:
        Template content as string with # comment lines removed
    """
    lines = path.read_text(encoding="utf-8").split("\n")
    lines = [line for line in lines if not line.lstrip().startswith("#")]
    return "\n".join(lines)


def _prompt_file_exists(path: Path) -> bool:
    """Check if prompt template file exists.

    Args:
        path: Path to check

    Returns:
        True if file exists, False otherwise
    """
    return path.exists()


class AnswerCommand:
    """Retrieve chunks and embed them into a prompt template."""

    def __init__(
        self,
        query: str,
        k: int = 5,
        min_score: float | None = None,
        expand: int = 0,
        full_doc_threshold: int = 0,
    ) -> None:
        self.query = query
        self.k = k
        self.min_score = min_score
        self.expand = expand
        self.full_doc_threshold = full_doc_threshold

    def execute(self) -> str:
        try:
            logger.info(
                f"AnswerCommand(query='{self.query[:50]}', k={self.k}, expand={self.expand}, "
                f"full_doc_threshold={self.full_doc_threshold}, min_score={self.min_score})"
            )

            # Validate query is not empty
            if not self.query or not self.query.strip():
                return "Error: Query cannot be empty"

            if self.expand < 0:
                return "Error: expand must be >= 0"

            if self.full_doc_threshold < 0:
                return "Error: full_doc_threshold must be >= 0"

            # Check if prompt template exists
            if not _prompt_file_exists(PROMPT_TEMPLATE_PATH):
                return "Error: Prompt template not found. Please create the prompt file first."
            logger.info(f"Prompt template found at {PROMPT_TEMPLATE_PATH}")

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

            counts_by_doc: dict[str, int] = {}
            for result in selected_results:
                counts_by_doc[result["doc_uid"]] = counts_by_doc.get(result["doc_uid"], 0) + 1
            doc_summary = ", ".join(f"{doc}({count})" for doc, count in counts_by_doc.items())
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
                for result in selected_results:
                    final_counts_by_doc[result["doc_uid"]] = (
                        final_counts_by_doc.get(result["doc_uid"], 0) + 1
                    )
                final_doc_summary = ", ".join(
                    f"{doc}({count})" for doc, count in final_counts_by_doc.items()
                )
                logger.info(
                    f"Final retrieval: {len(selected_results)} chunks from "
                    f"{len(final_counts_by_doc)} doc(s) - {final_doc_summary}"
                )

                chunk_summary = self._build_chunk_summary(selected_results, doc_chunks)

                # Build the formatted chunks
                formatted_chunks = self._format_chunks(selected_results, doc_chunks)
                logger.info(
                    f"Prompt assembly: {len(formatted_chunks)} document block(s) included"
                )

                # Build and return the prompt
                return self._build_prompt(formatted_chunks, chunk_summary)

        except Exception as e:
            logger.exception("Error executing answer command")
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

    def _format_chunks(self, results: list[dict], doc_chunks: dict[str, list[DbChunk]]) -> list[str]:
        """Format chunks grouped by document for clearer prompt structure.

        Args:
            results: Search results from vector store
            doc_chunks: Dictionary mapping doc_uid to list of chunks

        Returns:
            List of formatted document strings
        """
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
                chunk_xml = (
                    f'<chunk id="{chunk_id}" doc_uid="{self._escape_xml(doc_uid)}" '
                    f'section_path="{self._escape_xml(chunk.section_path)}" '
                    f'score="{score:.4f}"'
                    f">\n"
                    f"{chunk.text}\n"
                    f"</chunk>"
                )
                formatted_chunks.append(chunk_xml)

            joined_chunks = "\n\n".join(formatted_chunks)
            document_xml = f'<Document name="{self._escape_xml(doc_uid)}">\n{joined_chunks}\n</Document>'
            formatted_documents.append(document_xml)

        return formatted_documents

    def _escape_xml(self, text: str) -> str:
        """Escape special XML characters."""
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;")
        )

    def _build_prompt(self, chunks: list[str], chunk_summary: str) -> str:
        """Build the final prompt by substituting chunks into template.

        Args:
            chunks: List of formatted chunk strings
            chunk_summary: Human-readable summary of retrieved chunks

        Returns:
            Complete prompt string
        """
        template = _read_prompt_template(PROMPT_TEMPLATE_PATH)
        chunks_text = "\n\n".join(chunks)
        prompt = template.replace("{{CHUNKS}}", chunks_text).replace("{{QUERY}}", self.query)
        return f"{chunk_summary}\n\n{prompt}"

    def _empty_chunk_summary(self) -> str:
        """Build the summary shown when no chunks were retrieved."""
        return "Retrieved chunks:\n- none"

    def _build_chunk_summary(self, results: list[dict], doc_chunks: dict[str, list[DbChunk]]) -> str:
        """Build a one-line-per-document summary of retrieved chunk sections."""
        if not results:
            return self._empty_chunk_summary()

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
                section_label = chunk.section_path if chunk.section_path else f"chunk {chunk_id}"
                if section_label in seen_sections:
                    continue
                seen_sections.add(section_label)
                ordered_sections.append(section_label)

            sections_text = ", ".join(ordered_sections) if ordered_sections else "(no sections)"
            lines.append(f"- {doc_uid}: {sections_text}")

        return "\n".join(lines)

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
                    for surrounding_chunk in chunks[start_idx:end_idx]:
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
                doc_size = sum(len(chunk.text) for chunk in doc_chunks.get(doc_uid, []))
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
