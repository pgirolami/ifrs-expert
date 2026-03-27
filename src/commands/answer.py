"""Answer command - retrieve chunks and embed them into a prompt template."""

import json
import logging
import subprocess
import tempfile
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from src.b_response_utils import convert_json_to_markdown
from src.db import ChunkStore, init_db
from src.models.chunk import Chunk
from src.vector.store import VectorStore, get_index_path

RELEVANCE_SCORE_THRESHOLD = 0.3

logger = logging.getLogger(__name__)


# Path to the prompt template files
PROJECT_ROOT = Path(__file__).parent.parent.parent
PROMPT_A_PATH = PROJECT_ROOT / "prompts" / "answer_prompt_A.txt"
PROMPT_B_PATH = PROJECT_ROOT / "prompts" / "answer_prompt_B.txt"

# Type aliases for dependency injection
AnswerVectorStore = VectorStore
AnswerChunkStore = ChunkStore
AnswerInitDb = Callable[[], None]
AnswerIndexPath = Callable[[], Path]
AnswerLlmFn = Callable[[str], str]


@dataclass
class AnswerOptions:
    """Options for answer command."""

    k: int = 5
    min_score: float | None = None
    expand: int = 0
    full_doc_threshold: int = 0
    output_dir: Path | None = None
    save_all: bool = False


# LLM command (same as in existing shell script)
LLM_CMD = [
    "pi",
    "-p",
    "--provider",
    "openai-codex",
    "--model",
    "gpt-5.4",
    "--thinking",
    "high",
    "--no-skills",
    "--no-tools",
    "--no-extensions",
    "--no-prompt-templates",
    "--no-themes",
    "--system-prompt",
    "",
]


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
    """Retrieve chunks and embed them into a prompt template.

    Dependencies are required - use create_answer_command() factory for production.
    """

    def __init__(
        self,
        query: str,
        vector_store: AnswerVectorStore,
        chunk_store: AnswerChunkStore,
        init_db_fn: AnswerInitDb,
        index_path_fn: AnswerIndexPath,
        send_to_llm_fn: AnswerLlmFn,
        options: AnswerOptions | None = None,
    ) -> None:
        """Initialize the answer command.

        Args:
            query: The question to answer.
            vector_store: Vector store instance (required).
            chunk_store: Chunk store instance (required).
            init_db_fn: DB init function (required).
            index_path_fn: Function returning index path (required).
            send_to_llm_fn: Function to send prompt to LLM (required).
            options: Options for the answer command.

        Note:
            For production use, call create_answer_command() instead.
        """
        self.query = query
        self.k = options.k if options else 5
        self.min_score = options.min_score if options else None
        self.expand = options.expand if options else 0
        self.full_doc_threshold = options.full_doc_threshold if options else 0
        self.output_dir = options.output_dir if options else None
        self.save_all = options.save_all if options else False

        # Track retrieved document UIDs for markdown output
        self._retrieved_doc_uids: list[str] = []

        self._vector_store = vector_store
        self._chunk_store = chunk_store
        self._init_db_fn = init_db_fn
        self._index_path_fn = index_path_fn
        self._send_to_llm_fn = send_to_llm_fn

    def execute(self) -> str:
        """Execute the answer command and return the LLM response."""
        try:
            logger.info(
                f"AnswerCommand(query='{self.query[:50]}', k={self.k}, expand={self.expand}, full_doc_threshold={self.full_doc_threshold}, min_score={self.min_score}, output_dir={self.output_dir}, save_all={self.save_all})"
            )

            # Validate query is not empty
            if not self.query or not self.query.strip():
                return "Error: Query cannot be empty"

            if self.expand < 0:
                return "Error: expand must be >= 0"

            if self.full_doc_threshold < 0:
                return "Error: full_doc_threshold must be >= 0"

            if self.save_all and not self.output_dir:
                return "Error: --save-all requires --output-dir to be specified"

            if self.output_dir and not self.output_dir.exists():
                return f"Error: Output directory does not exist: {self.output_dir}"

            # Check if prompt templates exist
            if not _prompt_file_exists(PROMPT_A_PATH):
                return "Error: Prompt A template not found."
            if not _prompt_file_exists(PROMPT_B_PATH):
                return "Error: Prompt B template not found."
            logger.info(f"Prompt templates found: A={PROMPT_A_PATH.name}, B={PROMPT_B_PATH.name}")

            # Check if index exists
            index_path = self._index_path_fn()
            if not index_path.exists():
                return "Error: No index found. Please run 'store' command first."

            with self._vector_store as vector_store:
                ranked_results = vector_store.search_all(self.query)

            logger.info(f"Search returned {len(ranked_results)} raw results")

            if not ranked_results:
                return "Error: No chunks retrieved"

            effective_min_score = self.min_score if self.min_score is not None else RELEVANCE_SCORE_THRESHOLD
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
                f"Per-document selection: {len(selected_results)} chunks from {len(counts_by_doc)} doc(s) - {doc_summary}"
            )

            # Get the chunk details from database
            self._init_db_fn()

            # Group results by doc_uid to minimize DB calls
            doc_uids = list({result["doc_uid"] for result in selected_results})
            self._retrieved_doc_uids = doc_uids

            with self._chunk_store as store:
                # Fetch all chunks for all relevant docs at once
                doc_chunks: dict[str, list[Chunk]] = {}
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
                    final_counts_by_doc[result["doc_uid"]] = final_counts_by_doc.get(result["doc_uid"], 0) + 1
                final_doc_summary = ", ".join(f"{doc}({count})" for doc, count in final_counts_by_doc.items())
                logger.info(
                    f"Final retrieval: {len(selected_results)} chunks from {len(final_counts_by_doc)} doc(s) - {final_doc_summary}"
                )

                chunk_summary = self._build_chunk_summary(selected_results, doc_chunks)

                # Build the formatted chunks
                formatted_chunks = self._format_chunks(selected_results, doc_chunks)
                logger.info(f"Prompt assembly: {len(formatted_chunks)} document block(s) included")

                # Build Prompt A
                prompt_a = self._build_prompt_from_template(PROMPT_A_PATH, formatted_chunks, chunk_summary)

                # Step 1: Send Prompt A to LLM to get approaches
                logger.info("Step 1: Sending Prompt A to LLM...")
                prompt_a_content = _extract_prompt_content(prompt_a)

                # Save prompt A if requested
                if self.save_all and self.output_dir:
                    self._save_file("A-prompt.txt", prompt_a_content)

                try:
                    response_a = self._send_to_llm_fn(prompt_a_content)
                except RuntimeError as e:
                    logger.exception("LLM call failed")
                    # Save error info and continue to next question
                    if self.save_all and self.output_dir:
                        self._save_file("A-error.txt", str(e))
                    return f"Error: LLM call failed: {e}"

                # Save response A if requested
                if self.save_all and self.output_dir:
                    self._save_file("A-response.json", response_a)

                logger.error("SKIPPING prompt B")

                # Parse the JSON response
                try:
                    approaches_json = json.dumps(json.loads(response_a), indent=2)
                except json.JSONDecodeError as e:
                    logger.exception("Could not parse JSON response from LLM")
                    return f"Error: LLM returned invalid JSON: {e}\n\nResponse was:\n{response_a}"

                # Step 2: Build Prompt B and send to LLM
                logger.info("Step 2: Building and sending Prompt B to LLM...")
                context = _extract_context_from_output(prompt_a)
                prompt_b = self._build_prompt_b(context, approaches_json)

                # Save prompt B if requested
                if self.save_all and self.output_dir:
                    self._save_file("B-prompt.txt", prompt_b)

                try:
                    response_b = self._send_to_llm_fn(prompt_b)
                except RuntimeError as e:
                    logger.exception("LLM call failed")
                    if self.save_all and self.output_dir:
                        self._save_file("B-error.txt", str(e))
                    return f"Error: LLM call failed: {e}"

                logger.info("Step 2 complete: Received final answer from LLM")

                # Save response B as JSON to B-response.json (the LLM returns JSON)
                if self.save_all and self.output_dir:
                    # First, try to parse as JSON and save properly formatted JSON
                    try:
                        b_json = json.loads(response_b)
                        json_path = self.output_dir / "B-response.json"
                        json_path.write_text(json.dumps(b_json, indent=2, ensure_ascii=False), encoding="utf-8")
                        logger.info(f"Saved B-response.json to {self.output_dir}")
                    except json.JSONDecodeError:
                        # If not valid JSON, save as-is to both files
                        self._save_file("B-response.json", response_b)
                        logger.warning("B-response is not valid JSON, saved as-is to B-response.json")

                    # Convert JSON to French markdown and save to B-response.md
                    try:
                        b_json = json.loads(response_b) if not hasattr(b_json, "__iter__") else b_json
                        markdown_content = self._convert_json_to_markdown(b_json)
                        self._save_file("B-response.md", markdown_content)
                        logger.info("Converted B-response.json to French markdown B-response.md")
                    except (json.JSONDecodeError, KeyError) as e:
                        logger.warning(f"Could not convert B-response to markdown: {e}")

                return response_b

        except Exception as e:
            logger.exception("Error executing answer command")
            return f"Error: {e}"

    def _save_file(self, filename: str, content: str) -> None:
        """Save content to a file in the output directory."""
        if not self.output_dir:
            return
        file_path = self.output_dir / filename
        file_path.write_text(content, encoding="utf-8")
        logger.info(f"Saved {filename} to {self.output_dir}")

    def _convert_json_to_markdown(self, b_json: dict) -> str:
        """Convert B-response JSON to French markdown format.

        Args:
            b_json: Parsed JSON response from LLM

        Returns:
            Markdown formatted string in French
        """
        return convert_json_to_markdown(
            b_json,
            question=self.query,
            doc_uids=self._retrieved_doc_uids,
        )

    def _build_prompt_from_template(
        self,
        template_path: Path,
        chunks: list[str],
        chunk_summary: str,
    ) -> str:
        """Build a prompt by substituting chunks into a template.

        Args:
            template_path: Path to the template file
            chunks: List of formatted chunk strings
            chunk_summary: Human-readable summary of retrieved chunks

        Returns:
            Complete prompt string

        """
        template = _read_prompt_template(template_path)
        chunks_text = "\n\n".join(chunks)
        prompt = template.replace("{{CHUNKS}}", chunks_text).replace("{{QUERY}}", self.query)
        return f"{chunk_summary}\n\n{prompt}"

    def _build_prompt_b(self, context: str, approaches_json: str) -> str:
        """Build Prompt B by substituting placeholders."""
        template = _read_prompt_template(PROMPT_B_PATH)
        return (
            template.replace("{{CHUNKS}}", context)
            .replace("{{QUERY}}", self.query)
            .replace("{{APPROACHES_JSON}}", approaches_json)
        )

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
            f"Selection filters: {skipped_low_score} below min_score, {skipped_doc_full} skipped because doc already had {k} chunk(s)"
        )
        return selected_results

    def _format_chunks(self, results: list[dict], doc_chunks: dict[str, list[Chunk]]) -> list[str]:
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
                chunk_xml = f'<chunk id="{chunk_id}" doc_uid="{self._escape_xml(doc_uid)}" section_path="{self._escape_xml(chunk.section_path)}" score="{score:.4f}">\n{chunk.text}\n</chunk>'
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

    def _empty_chunk_summary(self) -> str:
        """Build the summary shown when no chunks were retrieved."""
        return "Retrieved chunks:\n- none"

    def _build_chunk_summary(self, results: list[dict], doc_chunks: dict[str, list[Chunk]]) -> str:
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
                section_label = chunk.section_path or f"chunk {chunk_id}"
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
        doc_chunks: dict[str, list[Chunk]],
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
                    },
                )

        if full_doc_threshold > 0:
            for doc_uid in full_doc_docs:
                doc_size = sum(len(chunk.text) for chunk in doc_chunks.get(doc_uid, []))
                logger.info(f"Full doc inclusion: {doc_uid} (size={doc_size} < threshold={full_doc_threshold})")
        if expand > 0:
            neighbour_summary: dict[str, set[int]] = {}
            for doc_uid, chunk_id in expanded_via_neighbours:
                neighbour_summary.setdefault(doc_uid, set()).add(chunk_id)
            for doc_uid, chunk_ids in neighbour_summary.items():
                logger.info(f"Neighbour expansion: {doc_uid} - added {len(chunk_ids)} surrounding chunk(s)")

        return expanded_results


def _extract_context_from_output(full_output: str) -> str:
    """Extract just the <context>...</context> section from the full output."""
    start_tag = "<context>"
    end_tag = "</context>"

    start_idx = full_output.find(start_tag)
    end_idx = full_output.find(end_tag)

    if start_idx == -1 or end_idx == -1:
        return ""

    return full_output[start_idx + len(start_tag) : end_idx].strip()


def _extract_prompt_content(full_output: str) -> str:
    """Extract only the prompt content, skipping the chunk summary at the top."""
    lines = full_output.split("\n")

    # Find the first line that starts the actual prompt
    start_idx = 0
    for i, line in enumerate(lines):
        if line.startswith("You are an IFRS expert"):
            start_idx = i
            break

    return "\n".join(lines[start_idx:])


def _default_send_to_llm(prompt: str) -> str:
    """Send prompt to LLM and return the response."""
    # Write prompt to temp file - subprocess runs inside context so file stays open
    with tempfile.NamedTemporaryFile(mode="w", delete=True, encoding="utf-8") as temp_prompt:
        temp_prompt.write(prompt)
        temp_prompt_path = temp_prompt.name

        result = subprocess.run(
            [*LLM_CMD, "@" + temp_prompt_path, ""],
            capture_output=True,
            text=True,
            check=False,
        )

    # Check for errors
    if result.returncode != 0:
        error_msg = result.stderr.strip() if result.stderr else f"Exit code {result.returncode}"
        logger.error(f"LLM command failed: {error_msg}")
        raise RuntimeError(error_msg)

    return result.stdout


def create_answer_command(
    query: str,
    options: AnswerOptions | None = None,
) -> AnswerCommand:
    """Create AnswerCommand with real dependencies.

    Args:
        query: The question to answer.
        options: Options for the answer command.

    Returns:
        AnswerCommand configured with production dependencies.
    """
    return AnswerCommand(
        query=query,
        options=options,
        vector_store=VectorStore(),
        chunk_store=ChunkStore(),
        init_db_fn=init_db,
        index_path_fn=get_index_path,
        send_to_llm_fn=_default_send_to_llm,
    )
