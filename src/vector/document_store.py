"""Document vector store for document-level retrieval."""

from __future__ import annotations

import hashlib
import json
import logging
import os
import re
from pathlib import Path
from typing import TYPE_CHECKING, Self, cast

import faiss
import numpy as np

from src.policy import SIMILARITY_REPRESENTATIONS, DocumentSimilarityRepresentation
from src.vector.model_cache import (
    BATCH_SIZE,
    EMBEDDING_MODEL,
    EmbeddingModelProtocol,
    get_embedding_model,
)

if TYPE_CHECKING:
    from src.interfaces import DocumentSearchResult

os.environ["TOKENIZERS_PARALLELISM"] = "false"
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("transformers").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

QUERY_EMBEDDING_CACHE_VERSION = "v1"
QUERY_EMBEDDING_NDIM = 2

_document_index_path_by_representation: dict[DocumentSimilarityRepresentation, Path] = {}
_document_id_map_path_by_representation: dict[DocumentSimilarityRepresentation, Path] = {}


def _require_representation(
    representation: str,
) -> DocumentSimilarityRepresentation:
    if representation in SIMILARITY_REPRESENTATIONS:
        return cast("DocumentSimilarityRepresentation", representation)
    supported_representations = ", ".join(SIMILARITY_REPRESENTATIONS)
    message = f"Unsupported document similarity representation: {representation}. Expected one of: {supported_representations}"
    raise ValueError(message)


def _default_document_index_path(representation: DocumentSimilarityRepresentation) -> Path:
    index_dir = Path(__file__).parent.parent.parent / "corpus" / "data" / "index"
    if representation == "full":
        return index_dir / "faiss_documents.index"
    return index_dir / f"faiss_documents_{representation}.index"


def get_document_index_path(representation: str = "full") -> Path:
    """Return the persisted FAISS index path for document embeddings."""
    validated_representation = _require_representation(representation)
    cached_path = _document_index_path_by_representation.get(validated_representation)
    if cached_path is None:
        cached_path = _default_document_index_path(validated_representation)
        _document_index_path_by_representation[validated_representation] = cached_path
    cached_path.parent.mkdir(parents=True, exist_ok=True)
    return cached_path


def get_document_id_map_path(representation: str = "full") -> Path:
    """Return the persisted id-map path for document embeddings."""
    validated_representation = _require_representation(representation)
    cached_path = _document_id_map_path_by_representation.get(validated_representation)
    if cached_path is None:
        index_path = get_document_index_path(validated_representation)
        cached_path = index_path.parent / "id_map_documents.json" if validated_representation == "full" else index_path.parent / f"id_map_documents_{validated_representation}.json"
        _document_id_map_path_by_representation[validated_representation] = cached_path
    cached_path.parent.mkdir(parents=True, exist_ok=True)
    return cached_path


def _default_query_cache_dir() -> Path:
    return Path(__file__).parent.parent.parent / ".cache" / "query_embeddings"


def _normalize_query_for_cache(query: str) -> str:
    return query.strip()


def _slugify_path_component(value: str) -> str:
    lowered = value.lower()
    return re.sub(r"[^a-z0-9._-]+", "_", lowered)


class DocumentVectorStore:
    """Manage document embeddings using FAISS and SentenceTransformers."""

    def __init__(
        self,
        index_path: Path | None = None,
        id_map_path: Path | None = None,
        query_cache_dir: Path | None = None,
    ) -> None:
        """Initialize the document vector store."""
        self._index: faiss.Index | None = None
        self._model: EmbeddingModelProtocol | None = None
        self._id_map: dict[int, str] = {}
        self._index_path = index_path
        self._id_map_path = id_map_path
        self._query_cache_dir = query_cache_dir
        self._added_doc_uids: set[str] = set()
        self._deleted_doc_uids: set[str] = set()

    def _resolve_index_path(self) -> Path:
        return self._index_path or get_document_index_path()

    def _resolve_id_map_path(self) -> Path:
        return self._id_map_path or get_document_id_map_path()

    def __enter__(self) -> Self:
        """Load or create the FAISS index when entering the context manager."""
        self._added_doc_uids.clear()
        self._deleted_doc_uids.clear()
        self._load_or_create_index()
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Persist the FAISS index when changes occurred in the context manager."""
        if not self._has_persisted_changes():
            logger.info("Skipping document FAISS index save because no documents were added or deleted")
            return
        self._save_index()

    def _resolve_query_cache_dir(self) -> Path:
        cache_dir = self._query_cache_dir or _default_query_cache_dir()
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def _get_model(self) -> EmbeddingModelProtocol:
        if self._model is None:
            self._model = get_embedding_model(EMBEDDING_MODEL)
        return self._model

    def _has_persisted_changes(self) -> bool:
        return bool(self._added_doc_uids or self._deleted_doc_uids)

    def _load_or_create_index(self) -> None:
        index_path = self._resolve_index_path()
        id_map_path = self._resolve_id_map_path()

        if index_path.exists() and id_map_path.exists():
            logger.info(f"Loading existing document FAISS index from {index_path}")
            self._index = faiss.read_index(str(index_path))
            with id_map_path.open() as file_handle:
                raw_id_map = json.load(file_handle)
            self._id_map = {int(key): str(value) for key, value in raw_id_map.items()}
            logger.info(f"Loaded document index with {self._index.ntotal} vectors")
            return

        logger.info("Creating new document FAISS index")
        model = self._get_model()
        dummy = model.encode("test")
        self._index = faiss.IndexFlatIP(len(dummy))
        self._id_map = {}

    def _save_index(self) -> None:
        if self._index is None:
            return
        index_path = self._resolve_index_path()
        id_map_path = self._resolve_id_map_path()
        logger.info(f"Saving document FAISS index to {index_path}")
        faiss.write_index(self._index, str(index_path))
        with id_map_path.open("w") as file_handle:
            json.dump({str(key): value for key, value in self._id_map.items()}, file_handle)
        self._added_doc_uids.clear()
        self._deleted_doc_uids.clear()
        logger.info(f"Saved document index with {self._index.ntotal} vectors")

    def _get_query_cache_path(self, query: str) -> Path:
        normalized_query = _normalize_query_for_cache(query)
        cache_key = f"{QUERY_EMBEDDING_CACHE_VERSION}:{EMBEDDING_MODEL}:{normalized_query}"
        cache_key_hash = hashlib.sha256(cache_key.encode("utf-8")).hexdigest()
        model_slug = _slugify_path_component(EMBEDDING_MODEL)
        return self._resolve_query_cache_dir() / f"{model_slug}--{cache_key_hash}.npy"

    def _load_cached_query_embedding(self, query: str) -> np.ndarray | None:
        cache_path = self._get_query_cache_path(query)
        if not cache_path.exists():
            return None
        try:
            cached_embedding = np.load(cache_path, allow_pickle=False)
        except (OSError, ValueError) as error:
            logger.warning(f"Could not load cached query embedding from {cache_path}: {error}")
            return None
        if cached_embedding.ndim != QUERY_EMBEDDING_NDIM:
            logger.warning(f"Ignoring cached query embedding with invalid shape {cached_embedding.shape} at {cache_path}")
            return None
        logger.info(f"Loaded cached query embedding from {cache_path}")
        return cached_embedding.astype("float32")

    def _save_query_embedding(self, query: str, query_embedding: np.ndarray) -> None:
        cache_path = self._get_query_cache_path(query)
        try:
            np.save(cache_path, query_embedding)
        except OSError as error:
            logger.warning(f"Could not save query embedding cache to {cache_path}: {error}")
            return
        logger.info(f"Saved query embedding cache to {cache_path}")

    def _get_query_embedding(self, query: str) -> np.ndarray:
        cached_embedding = self._load_cached_query_embedding(query)
        if cached_embedding is not None:
            return cached_embedding
        model = self._get_model()
        query_embedding = model.encode([query]).astype("float32")
        query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)
        self._save_query_embedding(query, query_embedding)
        return query_embedding

    def add_embeddings(self, doc_uids: list[str], texts: list[str]) -> None:
        """Add document embeddings to the FAISS index."""
        if not texts:
            logger.info("Skipping document embedding insert because no texts were provided")
            return
        if len(doc_uids) != len(texts):
            msg = f"Expected doc_uids and texts to have the same length, got {len(doc_uids)} and {len(texts)}"
            raise ValueError(msg)

        for doc_uid, text in zip(doc_uids, texts, strict=True):
            logger.info(f"Preparing document embedding for doc_uid={doc_uid} with chars={len(text)}")

        model = self._get_model()
        logger.info(f"Computing embeddings for {len(texts)} documents")
        embeddings = model.encode(texts, batch_size=BATCH_SIZE, show_progress_bar=True)
        embeddings = embeddings.astype("float32")
        embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
        start_id = self._index.ntotal  # type: ignore[union-attr]
        self._index.add(embeddings)  # type: ignore[union-attr]
        for index_offset, doc_uid in enumerate(doc_uids):
            self._id_map[start_id + index_offset] = doc_uid
            self._added_doc_uids.add(doc_uid)
        logger.info(f"Added {len(texts)} document embeddings to index")

    def has_embedding_for_doc(self, doc_uid: str) -> bool:
        """Return whether a document embedding already exists for the given doc_uid."""
        return any(existing_doc_uid == doc_uid for existing_doc_uid in self._id_map.values())

    def search_all(self, query: str) -> list[DocumentSearchResult]:
        """Search across the full document index and return ranked results."""
        if self._index is None or self._index.ntotal == 0:
            logger.warning("Document index is empty, no results to return")
            return []
        return self._search_with_k(query, self._index.ntotal)

    def _search_with_k(self, query: str, k: int) -> list[DocumentSearchResult]:
        query_embedding = self._get_query_embedding(query)
        scores, indices = self._index.search(query_embedding, k)  # type: ignore[union-attr]
        results: list[DocumentSearchResult] = []
        for score, idx in zip(scores[0], indices[0], strict=True):
            if idx >= 0 and idx in self._id_map:
                results.append({"doc_uid": self._id_map[idx], "score": float(score)})
        return results

    def delete_by_doc(self, doc_uid: str) -> int:
        """Delete all document embeddings for one document."""
        if self._index is None:
            return 0
        ids_to_delete = [idx for idx, existing_doc_uid in self._id_map.items() if existing_doc_uid == doc_uid]
        if not ids_to_delete:
            logger.info(f"No existing document embeddings found for doc_uid={doc_uid}")
            return 0
        count = len(ids_to_delete)
        if self._index.ntotal == count:
            dimension = self._index.d
            self._index = faiss.IndexFlatIP(dimension)
            self._id_map = {}
        else:
            all_vectors = self._index.reconstruct_n(0, self._index.ntotal)  # type: ignore[union-attr]
            new_vectors = []
            new_id_map: dict[int, str] = {}
            new_idx = 0
            for old_idx in range(self._index.ntotal):
                if old_idx not in ids_to_delete:
                    new_vectors.append(all_vectors[old_idx])
                    new_id_map[new_idx] = self._id_map[old_idx]
                    new_idx += 1
            dimension = self._index.d
            self._index = faiss.IndexFlatIP(dimension)
            self._index.add(np.array(new_vectors).astype("float32"))  # type: ignore[union-attr]
            self._id_map = new_id_map
        self._deleted_doc_uids.add(doc_uid)
        logger.info(f"Deleted {count} document embeddings for doc_uid={doc_uid}")
        return count
