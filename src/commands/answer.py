"""Answer command - retrieve chunks and embed them into a prompt template."""

import json
import logging
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from src.b_response_utils import convert_json_to_markdown
from src.db import ChunkStore, init_db
from src.llm import get_client
from src.models.chunk import Chunk
from src.vector.store import VectorStore, get_index_path

RELEVANCE_SCORE_THRESHOLD = 0.3

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).parent.parent.parent
PROMPT_A_PATH = PROJECT_ROOT / "prompts" / "answer_prompt_A.txt"
PROMPT_B_PATH = PROJECT_ROOT / "prompts" / "answer_prompt_B.txt"


@dataclass
class AnswerConfig:
    """Configuration for AnswerCommand - consolidates dependencies."""

    vector_store: VectorStore
    chunk_store: ChunkStore
    init_db_fn: Callable[[], None]
    index_path_fn: Callable[[], Path]
    send_to_llm_fn: Callable[[str], str]


@dataclass
class AnswerOptions:
    """Options for answer command."""

    k: int = 5
    min_score: float | None = None
    expand: int = 0
    full_doc_threshold: int = 0
    output_dir: Path | None = None
    save_all: bool = False


class AnswerResult:
    """Result of answer command execution."""

    def __init__(
        self,
        status: str,
        data: str | None = None,
        error: str | None = None,
    ) -> None:
        """Initialize answer result.

        Args:
            status: Status of the result ("ok" or "error").
            data: The result data if successful.
            error: The error message if failed.
        """
        self.success = status == "ok"
        self.data = data
        self.error = error

    @staticmethod
    def ok(data: str) -> "AnswerResult":
        """Create a successful result."""
        return AnswerResult(status="ok", data=data)

    @staticmethod
    def err(message: str) -> "AnswerResult":
        """Create an error result."""
        return AnswerResult(status="error", error=message)


def _read_prompt_template(path: Path) -> str:
    """Read the prompt template from file."""
    lines = path.read_text(encoding="utf-8").split("\n")
    return "\n".join(line for line in lines if not line.lstrip().startswith("#"))


def _prompt_file_exists(path: Path) -> bool:
    """Check if prompt template file exists."""
    return path.exists()


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


class AnswerCommand:
    """Retrieve chunks and embed them into a prompt template."""

    def __init__(
        self,
        query: str,
        config: AnswerConfig,
        options: AnswerOptions | None = None,
    ) -> None:
        """Initialize the answer command."""
        self.query = query
        self.k = options.k if options else 5
        self.min_score = options.min_score if options else None
        self.expand = options.expand if options else 0
        self.full_doc_threshold = options.full_doc_threshold if options else 0
        self.output_dir = options.output_dir if options else None
        self.save_all = options.save_all if options else False

        self._retrieved_doc_uids: list[str] = []
        self._config = config

    def execute(self) -> str:
        """Execute the answer command and return the LLM response."""
        logger.info(f"AnswerCommand(query='{self.query[:50]}', k={self.k})")

        # Run validation and get error early
        error = self._check_input_validation()
        if error:
            return error

        error = self._check_file_prerequisites()
        if error:
            return error

        # Execute workflow
        result = self._execute_workflow()
        if result.error:
            return result.error

        return result.data or ""

    def _check_input_validation(self) -> str | None:
        """Validate input parameters - returns error message or None."""
        errors: list[str] = []

        if not self.query or not self.query.strip():
            errors.append("Query cannot be empty")
        if self.expand < 0:
            errors.append("expand must be >= 0")
        if self.full_doc_threshold < 0:
            errors.append("full_doc_threshold must be >= 0")
        if self.save_all and not self.output_dir:
            errors.append("--save-all requires --output-dir to be specified")
        if self.output_dir and not self.output_dir.exists():
            errors.append(f"Output directory does not exist: {self.output_dir}")

        if errors:
            return "Error: " + ", ".join(errors)
        return None

    def _check_file_prerequisites(self) -> str | None:
        """Check file prerequisites - returns error message or None."""
        if not _prompt_file_exists(PROMPT_A_PATH):
            return "Error: Prompt A template not found."
        if not _prompt_file_exists(PROMPT_B_PATH):
            return "Error: Prompt B template not found."

        index_path = self._config.index_path_fn()
        if not index_path.exists():
            return "Error: No index found. Please run 'store' command first."

        return None

    def _execute_workflow(self) -> AnswerResult:
        """Execute the main workflow."""
        try:
            ranked_results = self._search_chunks()
            if not ranked_results:
                return AnswerResult.err("Error: No chunks retrieved")

            selected_results = self._select_results(ranked_results)
            if not selected_results:
                return AnswerResult.err(f"Error: No chunks found with score >= {RELEVANCE_SCORE_THRESHOLD}")

            doc_chunks = self._fetch_chunks(selected_results)

            if self.expand > 0 or self.full_doc_threshold > 0:
                selected_results = self._expand_chunks(selected_results, doc_chunks)

            if not selected_results:
                return AnswerResult.err("Error: No chunks retrieved")

            response = self._process_prompts(selected_results, doc_chunks)
            if isinstance(response, AnswerResult):
                return response

            return AnswerResult.ok(response)

        except Exception as e:
            logger.exception("Error executing answer command")
            return AnswerResult.err(f"Error: {e}")

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
        self._retrieved_doc_uids = doc_uids

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

    def _process_prompts(self, results: list[dict], doc_chunks: dict[str, list[Chunk]]) -> str | AnswerResult:
        """Build prompts, send to LLM, and process responses."""
        chunk_summary = self._build_chunk_summary(results, doc_chunks)
        formatted_chunks = self._format_chunks(results, doc_chunks)

        # Step 1: Send Prompt A
        response_a = self._send_prompt_a(formatted_chunks, chunk_summary)
        if isinstance(response_a, AnswerResult):
            return response_a

        # response_a is guaranteed to be list[dict] after the check above
        return self._send_prompt_b(response_a)  # type: ignore[arg-type]

    def _send_prompt_a(self, formatted_chunks: list[str], chunk_summary: str) -> str | AnswerResult:
        """Send Prompt A to LLM and return parsed JSON."""
        prompt_a = self._build_prompt_from_template(PROMPT_A_PATH, formatted_chunks, chunk_summary)
        prompt_content = _extract_prompt_content(prompt_a)

        if self.save_all and self.output_dir:
            self._save_file("A-prompt.txt", prompt_content)

        try:
            response_a = self._config.send_to_llm_fn(prompt_content)
        except RuntimeError as e:
            logger.exception("LLM call failed")
            if self.save_all and self.output_dir:
                self._save_file("A-error.txt", str(e))
            return AnswerResult.err(f"Error: LLM call failed: {e}")

        if self.save_all and self.output_dir:
            self._save_file("A-response.json", response_a)

        try:
            return json.loads(response_a)
        except json.JSONDecodeError as e:
            logger.exception("Could not parse JSON response from LLM")
            return AnswerResult.err(f"Error: LLM returned invalid JSON: {e}\n\nResponse was:\n{response_a}")

    def _send_prompt_b(self, approaches_json: list[dict]) -> AnswerResult:
        """Send Prompt B to LLM and return the final response."""
        prompt_b = self._build_prompt_b("", json.dumps(approaches_json, indent=2))

        if self.save_all and self.output_dir:
            self._save_file("B-prompt.txt", prompt_b)

        try:
            response_b = self._config.send_to_llm_fn(prompt_b)
        except RuntimeError as e:
            logger.exception("LLM call failed")
            if self.save_all and self.output_dir:
                self._save_file("B-error.txt", str(e))
            return AnswerResult.err(f"Error: LLM call failed: {e}")

        logger.info("Step 2 complete: Received final answer from LLM")

        if self.save_all and self.output_dir:
            self._save_response_b(response_b)

        return AnswerResult.ok(response_b)

    def _save_response_b(self, response_b: str) -> None:
        """Save response B to files."""
        # Guard against output_dir being None (shouldn't happen due to validation)
        if not self.output_dir:
            return
        try:
            b_json = json.loads(response_b)
            json_path = self.output_dir / "B-response.json"
            json_path.write_text(json.dumps(b_json, indent=2, ensure_ascii=False), encoding="utf-8")
            logger.info(f"Saved B-response.json to {self.output_dir}")
        except json.JSONDecodeError:
            self._save_file("B-response.json", response_b)
            logger.warning("B-response is not valid JSON, saved as-is to B-response.json")

        try:
            b_json = json.loads(response_b)
            markdown_content = self._convert_json_to_markdown(b_json)
            self._save_file("B-response.md", markdown_content)
            logger.info("Converted B-response.json to French markdown B-response.md")
        except (json.JSONDecodeError, KeyError) as e:
            logger.warning(f"Could not convert B-response to markdown: {e}")

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

    def _format_chunks(self, results: list[dict], doc_chunks: dict[str, list[Chunk]]) -> list[str]:
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

    def _build_chunk_summary(self, results: list[dict], doc_chunks: dict[str, list[Chunk]]) -> str:
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

    def _save_file(self, filename: str, content: str) -> None:
        """Save content to a file in the output directory."""
        if not self.output_dir:
            return
        file_path = self.output_dir / filename
        file_path.write_text(content, encoding="utf-8")
        logger.info(f"Saved {filename} to {self.output_dir}")

    def _convert_json_to_markdown(self, b_json: dict) -> str:
        """Convert B-response JSON to French markdown format."""
        return convert_json_to_markdown(b_json, question=self.query, doc_uids=self._retrieved_doc_uids)


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
