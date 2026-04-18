"""Build a TOC-only document index and score all Q1 variants against it.

This throw-away script:
1. loads every document with non-empty ``toc_text`` from the SQLite database
2. builds a fresh FAISS document index using only ``toc_text``
3. scores every ``Q1.*.txt`` question against that TOC-only index
4. writes a markdown report with summary and full ranking tables

Usage:
    uv run python scripts/run_q1_toc_similarity.py
    uv run python scripts/run_q1_toc_similarity.py --output-markdown /tmp/q1_toc_similarity.md
"""

from __future__ import annotations

import argparse
import importlib
import logging
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

get_db_path = importlib.import_module("src.db.connection").get_db_path
DocumentVectorStore = importlib.import_module("src.vector.document_store").DocumentVectorStore

logger = logging.getLogger(__name__)

DEFAULT_QUESTION_DIR = PROJECT_ROOT / "experiments" / "00_QUESTIONS" / "Q1"
DEFAULT_OUTPUT_MARKDOWN = PROJECT_ROOT / "experiments" / "analysis" / "generated_q1_toc_similarity.md"
DEFAULT_INDEX_PATH = PROJECT_ROOT / "experiments" / "analysis" / "faiss_q1_toc_similarity.index"
DEFAULT_ID_MAP_PATH = PROJECT_ROOT / "experiments" / "analysis" / "id_map_q1_toc_similarity.json"
DEFAULT_QUERY_CACHE_DIR = PROJECT_ROOT / ".cache" / "q1_toc_similarity_query_embeddings"
SUMMARY_TOP_K = 5


@dataclass(frozen=True)
class TocDocument:
    """One persisted document with TOC text available for indexing."""

    doc_uid: str
    source_title: str
    document_type: str | None
    toc_text: str


@dataclass(frozen=True)
class QuestionCase:
    """One Q1 question variant to score."""

    question_id: str
    question_text: str
    source_path: Path


@dataclass(frozen=True)
class RankedHit:
    """One ranked document hit for one question."""

    question_id: str
    doc_uid: str
    source_title: str
    document_type: str | None
    rank: int
    score: float


@dataclass(frozen=True)
class ScriptConfig:
    """Filesystem configuration for the TOC-similarity run."""

    question_dir: Path
    output_markdown: Path
    index_path: Path
    id_map_path: Path
    query_cache_dir: Path


class Q1TocSimilarityRunner:
    """Run the TOC-only similarity experiment for all Q1 variants."""

    def __init__(self, config: ScriptConfig) -> None:
        """Initialize the runner."""
        self._config = config

    def run(self) -> Path:
        """Run the experiment and return the markdown output path."""
        documents = self._load_documents()
        questions = self._load_questions()
        ranked_hits = self._score_questions(documents=documents, questions=questions)
        markdown = self._build_markdown(documents=documents, questions=questions, ranked_hits=ranked_hits)
        self._write_markdown(markdown)
        logger.info(
            f"Completed TOC similarity run: questions={len(questions)}, documents={len(documents)}, output={self._config.output_markdown}"
        )
        return self._config.output_markdown

    def _load_documents(self) -> list[TocDocument]:
        """Load every document with non-empty TOC text."""
        db_path = get_db_path()
        logger.info(f"Loading TOC documents from {db_path}")
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(
                """
                SELECT doc_uid, source_title, document_type, toc_text
                FROM documents
                WHERE toc_text IS NOT NULL
                  AND TRIM(toc_text) <> ''
                ORDER BY doc_uid
                """
            ).fetchall()

        documents = [
            TocDocument(
                doc_uid=row["doc_uid"],
                source_title=row["source_title"],
                document_type=row["document_type"],
                toc_text=row["toc_text"],
            )
            for row in rows
        ]
        if not documents:
            message = "No documents with non-empty toc_text were found in the database"
            raise ValueError(message)

        logger.info(f"Loaded {len(documents)} TOC document(s)")
        return documents

    def _load_questions(self) -> list[QuestionCase]:
        """Load all Q1 question files in numeric order."""
        logger.info(f"Loading Q1 variants from {self._config.question_dir}")
        question_paths = sorted(self._config.question_dir.glob("Q1.*.txt"), key=_question_sort_key)
        questions: list[QuestionCase] = []
        for question_path in question_paths:
            question_text = question_path.read_text(encoding="utf-8").strip()
            if not question_text:
                logger.warning(f"Skipping empty question file: {question_path}")
                continue
            questions.append(
                QuestionCase(
                    question_id=question_path.stem,
                    question_text=question_text,
                    source_path=question_path,
                )
            )
        if not questions:
            message = f"No Q1 question files found under {self._config.question_dir}"
            raise ValueError(message)

        logger.info(f"Loaded {len(questions)} question variant(s)")
        return questions

    def _score_questions(
        self,
        *,
        documents: list[TocDocument],
        questions: list[QuestionCase],
    ) -> list[RankedHit]:
        """Build a fresh TOC-only FAISS index and score every question."""
        self._prepare_output_paths()
        self._remove_existing_index_artifacts()

        document_by_uid = {document.doc_uid: document for document in documents}
        doc_uids = [document.doc_uid for document in documents]
        toc_texts = [document.toc_text for document in documents]

        ranked_hits: list[RankedHit] = []
        with DocumentVectorStore(
            index_path=self._config.index_path,
            id_map_path=self._config.id_map_path,
            query_cache_dir=self._config.query_cache_dir,
        ) as vector_store:
            logger.info(f"Building fresh TOC-only FAISS index at {self._config.index_path}")
            vector_store.add_embeddings(doc_uids=doc_uids, texts=toc_texts)

            for question in questions:
                logger.info(f"Scoring {question.question_id} against {len(documents)} TOC document(s)")
                search_results = vector_store.search_all(question.question_text)
                for rank, result in enumerate(search_results, start=1):
                    document = document_by_uid.get(result["doc_uid"])
                    if document is None:
                        message = f"Missing document metadata for doc_uid={result['doc_uid']}"
                        raise KeyError(message)
                    ranked_hits.append(
                        RankedHit(
                            question_id=question.question_id,
                            doc_uid=document.doc_uid,
                            source_title=document.source_title,
                            document_type=document.document_type,
                            rank=rank,
                            score=result["score"],
                        )
                    )

        return ranked_hits

    def _prepare_output_paths(self) -> None:
        """Create parent directories for all generated artifacts."""
        self._config.output_markdown.parent.mkdir(parents=True, exist_ok=True)
        self._config.index_path.parent.mkdir(parents=True, exist_ok=True)
        self._config.id_map_path.parent.mkdir(parents=True, exist_ok=True)
        self._config.query_cache_dir.mkdir(parents=True, exist_ok=True)

    def _remove_existing_index_artifacts(self) -> None:
        """Delete any previous TOC-only index artifacts before rebuilding."""
        if self._config.index_path.exists():
            logger.info(f"Removing previous index artifact at {self._config.index_path}")
            self._config.index_path.unlink()
        if self._config.id_map_path.exists():
            logger.info(f"Removing previous id-map artifact at {self._config.id_map_path}")
            self._config.id_map_path.unlink()

    def _build_markdown(
        self,
        *,
        documents: list[TocDocument],
        questions: list[QuestionCase],
        ranked_hits: list[RankedHit],
    ) -> str:
        """Build the markdown report with summary and full ranking tables."""
        hits_by_question_id: dict[str, list[RankedHit]] = {question.question_id: [] for question in questions}
        for ranked_hit in ranked_hits:
            hits_by_question_id[ranked_hit.question_id].append(ranked_hit)

        lines: list[str] = [
            "# Q1 TOC similarity report",
            "",
            "## Run metadata",
            "",
            f"- Question directory: `{self._config.question_dir}`",
            f"- Documents indexed (non-empty `toc_text`): **{len(documents)}**",
            f"- Q1 variants scored: **{len(questions)}**",
            f"- FAISS index: `{self._config.index_path}`",
            f"- FAISS id map: `{self._config.id_map_path}`",
            f"- Markdown output: `{self._config.output_markdown}`",
            "",
            "## Summary table",
            "",
            f"Top {SUMMARY_TOP_K} TOC matches per Q1 variant.",
            "",
            "| Variant | Top matches |",
            "| --- | --- |",
        ]

        for question in questions:
            top_hits = hits_by_question_id[question.question_id][:SUMMARY_TOP_K]
            summary_text = "<br>".join(
                f"{hit.rank}. `{hit.doc_uid}` ({hit.score:.4f})"
                for hit in top_hits
            )
            lines.append(f"| {question.question_id} | {summary_text} |")

        lines.extend(
            [
                "",
                "## Full score table",
                "",
                "| Variant | Rank | Doc UID | Type | Score | Title |",
                "| --- | ---: | --- | --- | ---: | --- |",
            ]
        )

        for question in questions:
            for hit in hits_by_question_id[question.question_id]:
                document_type = hit.document_type or ""
                escaped_title = _escape_markdown_cell(hit.source_title)
                lines.append(
                    f"| {hit.question_id} | {hit.rank} | `{hit.doc_uid}` | {document_type} | {hit.score:.4f} | {escaped_title} |"
                )

        lines.extend(
            [
                "",
                "## Question text",
                "",
            ]
        )
        lines.extend(
            f"- **{question.question_id}** — {_escape_markdown_text(question.question_text)}"
            for question in questions
        )

        lines.append("")
        return "\n".join(lines)

    def _write_markdown(self, markdown: str) -> None:
        """Write the markdown report to disk."""
        self._config.output_markdown.write_text(markdown, encoding="utf-8")
        logger.info(f"Wrote markdown report to {self._config.output_markdown}")


def _question_sort_key(path: Path) -> tuple[int, str]:
    """Sort `Q1.<n>.txt` paths numerically, then lexicographically."""
    suffix = path.stem.removeprefix("Q1.")
    if suffix.isdigit():
        return int(suffix), path.name
    return 10**9, path.name


def _escape_markdown_cell(value: str) -> str:
    """Escape minimal markdown table characters for one cell."""
    return value.replace("|", "\\|").replace("\n", " ").strip()


def _escape_markdown_text(value: str) -> str:
    """Normalize multi-line markdown text for bullet-list output."""
    return " ".join(value.split())


def parse_args() -> ScriptConfig:
    """Parse CLI arguments into a typed script config."""
    parser = argparse.ArgumentParser(description="Run TOC-only document similarity for all Q1 variants.")
    parser.add_argument(
        "--question-dir",
        type=Path,
        default=DEFAULT_QUESTION_DIR,
        help="Directory containing Q1.*.txt files.",
    )
    parser.add_argument(
        "--output-markdown",
        type=Path,
        default=DEFAULT_OUTPUT_MARKDOWN,
        help="Markdown report output path.",
    )
    parser.add_argument(
        "--index-path",
        type=Path,
        default=DEFAULT_INDEX_PATH,
        help="Output path for the generated TOC-only FAISS index.",
    )
    parser.add_argument(
        "--id-map-path",
        type=Path,
        default=DEFAULT_ID_MAP_PATH,
        help="Output path for the generated TOC-only FAISS id map.",
    )
    parser.add_argument(
        "--query-cache-dir",
        type=Path,
        default=DEFAULT_QUERY_CACHE_DIR,
        help="Cache directory for query embeddings.",
    )
    args = parser.parse_args()
    return ScriptConfig(
        question_dir=args.question_dir,
        output_markdown=args.output_markdown,
        index_path=args.index_path,
        id_map_path=args.id_map_path,
        query_cache_dir=args.query_cache_dir,
    )


def main() -> None:
    """Run the script from the repository root."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    config = parse_args()
    runner = Q1TocSimilarityRunner(config=config)
    runner.run()


if __name__ == "__main__":
    main()
