"""Backfill document-similarity FAISS indices from persisted document rows."""

from __future__ import annotations

import argparse
import json
import logging
import sqlite3
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable
    from pathlib import Path

try:
    from tqdm import tqdm
except ModuleNotFoundError:
    tqdm = None

from src.db.connection import get_connection, init_db
from src.models.document import DocumentRecord
from src.retrieval.document_profile_builder import (
    DOCUMENT_SIMILARITY_REPRESENTATIONS,
    build_document_similarity_text,
)
from src.vector.constants import MAX_EMBEDDING_TEXT_CHARS
from src.vector.document_store import DocumentVectorStore, get_document_id_map_path, get_document_index_path

logger = logging.getLogger(__name__)

SPECIALIZED_REPRESENTATIONS: tuple[str, ...] = tuple(
    representation for representation in DOCUMENT_SIMILARITY_REPRESENTATIONS if representation != "full"
)


@dataclass(frozen=True)
class BackfillStats:
    """Summary statistics for one representation backfill."""

    representation: str
    indexed_documents: int
    skipped_documents: int
    truncated_documents: int


@dataclass(frozen=True)
class EmbeddingBatch:
    """One embedding batch payload."""

    doc_uids: list[str]
    texts: list[str]


class DocumentSimilarityIndexBackfill:
    """Backfill missing specialized document similarity indices."""

    def __init__(
        self,
        *,
        force: bool = False,
        embedding_batch_size: int = 8,
        max_embedding_chars: int = MAX_EMBEDDING_TEXT_CHARS,
    ) -> None:
        """Initialize the backfill runner."""
        if embedding_batch_size <= 0:
            message = f"embedding_batch_size must be > 0, got {embedding_batch_size}"
            raise ValueError(message)
        if max_embedding_chars <= 0:
            message = f"max_embedding_chars must be > 0, got {max_embedding_chars}"
            raise ValueError(message)
        self._force = force
        self._embedding_batch_size = embedding_batch_size
        self._max_embedding_chars = max_embedding_chars

    def run(self) -> list[BackfillStats]:
        """Execute the backfill process."""
        init_db()
        documents = self._load_documents()
        logger.info(f"Loaded {len(documents)} persisted documents for similarity-index backfill")

        stats: list[BackfillStats] = []
        for representation in self._with_optional_progress(
            items=list(SPECIALIZED_REPRESENTATIONS),
            description="Representations",
            unit="representation",
        ):
            if not self._force and self._index_artifacts_are_complete(
                representation=representation,
                documents=documents,
            ):
                logger.info(f"Skipping representation={representation} because index artifacts are complete")
                continue
            representation_stats = self._backfill_representation(
                representation=representation,
                documents=documents,
            )
            stats.append(representation_stats)
        return stats

    def _index_artifacts_are_complete(
        self,
        *,
        representation: str,
        documents: list[DocumentRecord],
    ) -> bool:
        index_path = get_document_index_path(representation)
        id_map_path = get_document_id_map_path(representation)
        if not (index_path.exists() and id_map_path.exists()):
            return False
        try:
            id_map = id_map_path.read_text(encoding="utf-8")
        except OSError as error:
            logger.warning(f"Could not read id map for representation={representation}: {error}")
            return False

        try:
            parsed_id_map = json.loads(id_map)
        except json.JSONDecodeError as error:
            logger.warning(f"Could not parse id map for representation={representation}: {error}")
            return False

        if not isinstance(parsed_id_map, dict):
            logger.warning(f"Ignoring non-dict id map for representation={representation}")
            return False

        expected_indexed_documents = sum(
            1
            for document in documents
            if build_document_similarity_text(document, representation).strip()
        )
        actual_indexed_documents = len(parsed_id_map)
        if actual_indexed_documents < expected_indexed_documents:
            logger.info(
                f"Rebuilding representation={representation} because index appears incomplete; "
                f"actual_indexed_documents={actual_indexed_documents}, expected_indexed_documents={expected_indexed_documents}"
            )
            return False
        return True

    def _backfill_representation(
        self,
        *,
        representation: str,
        documents: list[DocumentRecord],
    ) -> BackfillStats:
        index_path = get_document_index_path(representation)
        id_map_path = get_document_id_map_path(representation)

        if self._force:
            self._unlink_if_exists(index_path)
            self._unlink_if_exists(id_map_path)

        doc_uids: list[str] = []
        texts: list[str] = []
        skipped_documents = 0
        truncated_documents = 0
        for document in self._with_optional_progress(
            items=documents,
            description=f"{representation}: building texts",
            unit="doc",
        ):
            representation_text = build_document_similarity_text(document, representation)
            if not representation_text.strip():
                skipped_documents += 1
                continue
            if len(representation_text) > self._max_embedding_chars:
                truncated_documents += 1
                representation_text = representation_text[: self._max_embedding_chars]
            doc_uids.append(document.doc_uid)
            texts.append(representation_text)

        with DocumentVectorStore(index_path=index_path, id_map_path=id_map_path) as document_vector_store:
            embedding_batches = self._build_embedding_batches(doc_uids=doc_uids, texts=texts)
            for embedding_batch in self._with_optional_progress(
                items=embedding_batches,
                description=f"{representation}: embedding batches",
                unit="batch",
            ):
                document_vector_store.add_embeddings(embedding_batch.doc_uids, embedding_batch.texts)

        logger.info(
            f"Backfilled representation={representation}; indexed_documents={len(doc_uids)}, "
            f"skipped_documents={skipped_documents}, truncated_documents={truncated_documents}, "
            f"index_path={index_path}, id_map_path={id_map_path}"
        )
        return BackfillStats(
            representation=representation,
            indexed_documents=len(doc_uids),
            skipped_documents=skipped_documents,
            truncated_documents=truncated_documents,
        )

    def _load_documents(self) -> list[DocumentRecord]:
        query = (
            "SELECT doc_uid, source_type, source_title, source_url, canonical_url, captured_at, source_domain, "
            "document_type, document_kind, background_text, issue_text, objective_text, scope_text, intro_text, toc_text "
            "FROM documents ORDER BY doc_uid"
        )
        with get_connection(read_only=True) as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(query).fetchall()
        return [self._row_to_document(row) for row in rows]

    def _row_to_document(self, row: sqlite3.Row) -> DocumentRecord:
        return DocumentRecord(
            doc_uid=str(row["doc_uid"]),
            source_type=str(row["source_type"]),
            source_title=str(row["source_title"]),
            source_url=row["source_url"],
            canonical_url=row["canonical_url"],
            captured_at=row["captured_at"],
            source_domain=row["source_domain"],
            document_type=row["document_type"],
            document_kind=row["document_kind"],
            background_text=row["background_text"],
            issue_text=row["issue_text"],
            objective_text=row["objective_text"],
            scope_text=row["scope_text"],
            intro_text=row["intro_text"],
            toc_text=row["toc_text"],
        )

    def _unlink_if_exists(self, path: Path) -> None:
        if path.exists():
            path.unlink()

    def _build_embedding_batches(
        self,
        *,
        doc_uids: list[str],
        texts: list[str],
    ) -> list[EmbeddingBatch]:
        embedding_batches: list[EmbeddingBatch] = []
        for start in range(0, len(doc_uids), self._embedding_batch_size):
            end = start + self._embedding_batch_size
            embedding_batches.append(
                EmbeddingBatch(
                    doc_uids=doc_uids[start:end],
                    texts=texts[start:end],
                )
            )
        return embedding_batches

    def _with_optional_progress(
        self,
        *,
        items: list[str] | list[DocumentRecord] | list[EmbeddingBatch],
        description: str,
        unit: str,
    ) -> Iterable[str] | Iterable[DocumentRecord] | Iterable[EmbeddingBatch]:
        if tqdm is None:
            return items
        return tqdm(items, total=len(items), desc=description, unit=unit)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Backfill specialized document similarity indices")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Rebuild specialized indices even when they already exist",
    )
    parser.add_argument(
        "--embedding-batch-size",
        type=int,
        default=8,
        help="Number of documents per embedding call (default: 8)",
    )
    parser.add_argument(
        "--max-embedding-chars",
        type=int,
        default=MAX_EMBEDDING_TEXT_CHARS,
        help=f"Maximum chars per document text before truncation (default: {MAX_EMBEDDING_TEXT_CHARS})",
    )
    return parser


def main() -> int:
    """Run the document-similarity index backfill CLI."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")
    args = _build_parser().parse_args()
    backfill = DocumentSimilarityIndexBackfill(
        force=args.force,
        embedding_batch_size=args.embedding_batch_size,
        max_embedding_chars=args.max_embedding_chars,
    )
    stats = backfill.run()
    if not stats:
        logger.info("No specialized similarity indices required backfilling")
        return 0
    for stat in stats:
        logger.info(
            f"Completed backfill for representation={stat.representation}; indexed_documents={stat.indexed_documents}; "
            f"skipped_documents={stat.skipped_documents}; truncated_documents={stat.truncated_documents}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
