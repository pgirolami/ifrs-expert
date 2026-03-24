"""Answer command - retrieve chunks and embed them into a prompt template."""

import logging
from pathlib import Path

from src.db import ChunkStore, init_db
from src.db.chunks import Chunk as DbChunk
from src.vector import VectorStore
from src.vector.store import get_index_path

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

    def __init__(self, query: str, k: int = 5, min_score: float | None = None) -> None:
        self.query = query
        self.k = k
        self.min_score = min_score

    def execute(self) -> str:
        try:
            # Validate query is not empty
            if not self.query or not self.query.strip():
                return "Error: Query cannot be empty"

            # Check if prompt template exists
            if not _prompt_file_exists(PROMPT_TEMPLATE_PATH):
                return "Error: Prompt template not found. Please create the prompt file first."

            # Check if index exists
            index_path = get_index_path()
            if not index_path.exists():
                return "Error: No index found. Please run 'store' command first."

            # Search for similar chunks (get more results to filter by min_score)
            search_k = self.k * 3 if self.min_score else self.k
            with VectorStore() as vector_store:
                results = vector_store.search(self.query, k=search_k)

            if not results:
                # Return prompt with empty chunks placeholder
                return self._build_prompt([])

            # Filter by minimum score if specified
            if self.min_score is not None:
                results = [r for r in results if r["score"] >= self.min_score]
                if not results:
                    # Return prompt with empty chunks
                    return self._build_prompt([])

            # Get the chunk details from database
            init_db()

            # Group results by doc_uid to minimize DB calls
            doc_uids = list({result["doc_uid"] for result in results})

            with ChunkStore() as store:
                # Fetch all chunks for all relevant docs at once
                doc_chunks: dict[str, list[DbChunk]] = {}
                for doc_uid in doc_uids:
                    doc_chunks[doc_uid] = store.get_chunks_by_doc(doc_uid)

                # Build the formatted chunks
                formatted_chunks = self._format_chunks(results, doc_chunks)

                # Build and return the prompt
                return self._build_prompt(formatted_chunks)

        except Exception as e:
            logger.exception("Error executing answer command")
            return f"Error: {e}"

    def _format_chunks(self, results: list[dict], doc_chunks: dict[str, list[DbChunk]]) -> list[str]:
        """Format chunks using XML format for clear agent readability.

        Uses XML with attributes for metadata to make it unambiguous for LLM agents.
        Each chunk includes: id, doc_uid, section_path, page_start, page_end, score.

        Args:
            results: Search results from vector store
            doc_chunks: Dictionary mapping doc_uid to list of chunks

        Returns:
            List of formatted chunk strings
        """
        formatted = []
        for result in results:
            doc_uid = result["doc_uid"]
            chunk_id = result["chunk_id"]
            score = result["score"]

            # Find matching chunk
            for chunk in doc_chunks.get(doc_uid, []):
                if chunk.chunk_id == chunk_id:
                    # Use XML format with attributes for metadata
                    # This is unambiguous and easy for LLMs to parse
                    chunk_xml = (
                        f'<chunk id="{chunk_id}" doc_uid="{self._escape_xml(doc_uid)}" '
                        f'section_path="{self._escape_xml(chunk.section_path)}" '
                        #    f'page_start="{self._escape_xml(chunk.page_start)}" '
                        #    f'page_end="{self._escape_xml(chunk.page_end)}" score="{score:.4f}"'
                        f">\n"
                        f"{chunk.text}\n"
                        f"</chunk>"
                    )
                    formatted.append(chunk_xml)
                    break
        return formatted

    def _escape_xml(self, text: str) -> str:
        """Escape special XML characters."""
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;")
        )

    def _build_prompt(self, chunks: list[str]) -> str:
        """Build the final prompt by substituting chunks into template.

        Args:
            chunks: List of formatted chunk strings

        Returns:
            Complete prompt string
        """
        # Read the template
        template = _read_prompt_template(PROMPT_TEMPLATE_PATH)

        # Join chunks with a separator
        chunks_text = "\n\n".join(chunks)

        # Replace placeholders and return
        return template.replace("{{CHUNKS}}", chunks_text).replace("{{QUERY}}", self.query)
