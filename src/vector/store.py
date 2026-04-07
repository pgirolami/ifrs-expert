"""Vector store for IFRS Expert using FAISS and SentenceTransformers."""

import hashlib
import json
import logging
import os
import re
from pathlib import Path
from typing import Self

import faiss
import numpy as np

from src.interfaces import SearchResult
from src.vector.model_cache import EmbeddingModelProtocol, get_embedding_model

# Suppress sentence-transformers logging
os.environ["TOKENIZERS_PARALLELISM"] = "false"
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("transformers").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

EMBEDDING_MODEL = "BAAI/bge-m3"
QUERY_EMBEDDING_CACHE_VERSION = "v1"
QUERY_EMBEDDING_NDIM = 2

# Default paths (can be overridden for testing)
_index_path: Path | None = None
_id_map_path: Path | None = None


def set_index_path(path: Path | None) -> None:
    """Set a custom index path (useful for testing)."""
    global _index_path, _id_map_path  # noqa: PLW0603
    _index_path = path
    _id_map_path = path.parent / "id_map.json" if path else None


def _default_index_path() -> Path:
    """Get the default index path."""
    return Path(__file__).parent.parent.parent / "corpus" / "data" / "index" / "faiss.index"


def get_index_path() -> Path:
    """Get the FAISS index path, creating directory if needed."""
    global _index_path  # noqa: PLW0603
    if _index_path is None:
        _index_path = _default_index_path()
    _index_path.parent.mkdir(parents=True, exist_ok=True)
    return _index_path


def get_id_map_path() -> Path:
    """Get the ID mapping file path."""
    global _id_map_path, _index_path  # noqa: PLW0603
    if _id_map_path is None:
        if _index_path is None:
            _index_path = _default_index_path()
        _id_map_path = _index_path.parent / "id_map.json"
    _id_map_path.parent.mkdir(parents=True, exist_ok=True)
    return _id_map_path


def _default_query_cache_dir() -> Path:
    """Get the default directory for cached query embeddings."""
    return Path(__file__).parent.parent.parent / ".cache" / "query_embeddings"


def _normalize_query_for_cache(query: str) -> str:
    """Normalize a query string before generating a cache key."""
    return query.strip()


def _slugify_path_component(value: str) -> str:
    """Convert a string into a filesystem-safe path component."""
    lowered = value.lower()
    return re.sub(r"[^a-z0-9._-]+", "_", lowered)


class VectorStore:
    """Manages vector embeddings using FAISS and SentenceTransformers."""

    def __init__(
        self,
        index_path: Path | None = None,
        id_map_path: Path | None = None,
        query_cache_dir: Path | None = None,
    ) -> None:
        """Initialize the vector store.

        Args:
            index_path: Optional custom path for FAISS index. Defaults to data/index/faiss.index.
            id_map_path: Optional custom path for ID mapping file.
            query_cache_dir: Optional custom directory for cached query embeddings.

        """
        self._index: faiss.Index | None = None
        self._model: EmbeddingModelProtocol | None = None
        self._id_map: dict[int, tuple[str, int]] = {}  # faiss_id -> (doc_uid, chunk_id)
        self._index_path = index_path
        self._id_map_path = id_map_path
        self._query_cache_dir = query_cache_dir
        self._added_doc_uids: set[str] = set()
        self._deleted_doc_uids: set[str] = set()

    def _resolve_index_path(self) -> Path:
        """Resolve the index path, using instance or global default."""
        if self._index_path is None:
            return get_index_path()
        return self._index_path

    def _resolve_id_map_path(self) -> Path:
        """Resolve the ID map path, using instance or global default."""
        if self._id_map_path is None:
            return get_id_map_path()
        return self._id_map_path

    def __enter__(self) -> Self:
        """Context manager entry - load or create index."""
        self._added_doc_uids.clear()
        self._deleted_doc_uids.clear()
        self._load_or_create_index()
        return self

    def _resolve_query_cache_dir(self) -> Path:
        """Resolve the query embedding cache directory."""
        cache_dir = self._query_cache_dir or _default_query_cache_dir()
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Context manager exit - save index when it changed."""
        if not self._has_persisted_changes():
            logger.info("Skipping FAISS index save because no documents were added or deleted")
            return
        self._save_index()

    def _get_model(self) -> EmbeddingModelProtocol:
        """Get or create the embedding model (singleton)."""
        if self._model is None:
            self._model = get_embedding_model(EMBEDDING_MODEL)
        return self._model

    def _has_persisted_changes(self) -> bool:
        """Return whether documents were added to or deleted from the index."""
        return bool(self._added_doc_uids or self._deleted_doc_uids)

    def _load_or_create_index(self) -> None:
        """Load existing index or create a new one."""
        index_path = self._resolve_index_path()
        id_map_path = self._resolve_id_map_path()

        if index_path.exists() and id_map_path.exists():
            logger.info(f"Loading existing FAISS index from {index_path}")
            self._index = faiss.read_index(str(index_path))

            # Load ID map
            with id_map_path.open() as f:
                self._id_map = {int(k): tuple(v) for k, v in json.load(f).items()}

            logger.info(f"Loaded index with {self._index.ntotal} vectors")
        else:
            logger.info("Creating new FAISS index")
            # Get embedding dimension
            model = self._get_model()
            dummy = model.encode("test")
            dimension = len(dummy)
            # Use Inner Product index for cosine similarity with normalized vectors
            self._index = faiss.IndexFlatIP(dimension)
            self._id_map = {}

    def _save_index(self) -> None:
        """Save the index to disk."""
        if self._index is not None:
            index_path = self._resolve_index_path()
            id_map_path = self._resolve_id_map_path()

            logger.info(f"Saving FAISS index to {index_path}")
            faiss.write_index(self._index, str(index_path))

            # Save ID map
            with id_map_path.open("w") as f:
                json.dump({str(k): list(v) for k, v in self._id_map.items()}, f)

            self._added_doc_uids.clear()
            self._deleted_doc_uids.clear()
            logger.info(f"Saved index with {self._index.ntotal} vectors")

    def _get_query_cache_path(self, query: str) -> Path:
        """Build the file path for a cached query embedding."""
        normalized_query = _normalize_query_for_cache(query)
        cache_key = f"{QUERY_EMBEDDING_CACHE_VERSION}:{EMBEDDING_MODEL}:{normalized_query}"
        cache_key_hash = hashlib.sha256(cache_key.encode("utf-8")).hexdigest()
        model_slug = _slugify_path_component(EMBEDDING_MODEL)
        return self._resolve_query_cache_dir() / f"{model_slug}--{cache_key_hash}.npy"

    def _load_cached_query_embedding(self, query: str) -> np.ndarray | None:
        """Load a cached query embedding from disk when available."""
        cache_path = self._get_query_cache_path(query)
        if not cache_path.exists():
            return None

        try:
            cached_embedding = np.load(cache_path, allow_pickle=False)
        except (OSError, ValueError) as e:
            logger.warning(f"Could not load cached query embedding from {cache_path}: {e}")
            return None

        if cached_embedding.ndim != QUERY_EMBEDDING_NDIM:
            logger.warning(f"Ignoring cached query embedding with invalid shape {cached_embedding.shape} at {cache_path}")
            return None

        logger.info(f"Loaded cached query embedding from {cache_path}")
        return cached_embedding.astype("float32")

    def _save_query_embedding(self, query: str, query_embedding: np.ndarray) -> None:
        """Persist a normalized query embedding to disk."""
        cache_path = self._get_query_cache_path(query)

        try:
            np.save(cache_path, query_embedding)
        except OSError as e:
            logger.warning(f"Could not save query embedding cache to {cache_path}: {e}")
            return

        logger.info(f"Saved query embedding cache to {cache_path}")

    def _get_query_embedding(self, query: str) -> np.ndarray:
        """Get a normalized query embedding, using the file cache when possible."""
        cached_embedding = self._load_cached_query_embedding(query)
        if cached_embedding is not None:
            return cached_embedding

        model = self._get_model()
        query_embedding = model.encode([query]).astype("float32")
        query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)
        self._save_query_embedding(query, query_embedding)
        return query_embedding

    def add_embeddings(self, doc_uid: str, chunk_ids: list[int], texts: list[str]) -> None:
        """Add embeddings for chunks to the index.

        Args:
            doc_uid: Document UID.
            chunk_ids: List of chunk database IDs.
            texts: List of text content to embed.

        """
        if not texts:
            return

        model = self._get_model()
        logger.info(f"Computing embeddings for {len(texts)} chunks")

        # Compute embeddings in batches
        embeddings = model.encode(texts, batch_size=4, show_progress_bar=True)

        # Convert to float32 (FAISS requirement)
        embeddings = embeddings.astype("float32")

        # Normalize for cosine similarity
        embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

        # Add to index
        start_id = self._index.ntotal  # type: ignore[union-attr]
        self._index.add(embeddings)  # type: ignore[union-attr]

        # Update ID map
        for i, chunk_id in enumerate(chunk_ids):
            self._id_map[start_id + i] = (doc_uid, chunk_id)

        self._added_doc_uids.add(doc_uid)
        logger.info(f"Added {len(texts)} embeddings to index for doc_uid={doc_uid}")

    def search(self, query: str, k: int = 5) -> list[SearchResult]:
        """Search for similar chunks.

        Args:
            query: Search query text.
            k: Number of results to return.

        Returns:
            List of results with doc_uid, chunk_id, and relevance score.
            Score is cosine similarity (0-1, higher is better).

        """
        if self._index is None or self._index.ntotal == 0:
            logger.warning("Index is empty, no results to return")
            return []

        bounded_k = min(k, self._index.ntotal)
        return self._search_with_k(query, bounded_k)

    def search_all(self, query: str) -> list[SearchResult]:
        """Search across the full index and return all ranked results."""
        if self._index is None or self._index.ntotal == 0:
            logger.warning("Index is empty, no results to return")
            return []

        return self._search_with_k(query, self._index.ntotal)

    def _search_with_k(self, query: str, k: int) -> list[SearchResult]:
        """Run a FAISS search with the specified k."""
        query_embedding = self._get_query_embedding(query)

        # Search using inner product (which becomes cosine similarity with normalized vectors)
        scores, indices = self._index.search(query_embedding, k)  # type: ignore[union-attr]

        results: list[SearchResult] = []
        for score, idx in zip(scores[0], indices[0], strict=True):
            if idx >= 0 and idx in self._id_map:
                doc_uid, chunk_id = self._id_map[idx]
                results.append(
                    {
                        "doc_uid": doc_uid,
                        "chunk_id": chunk_id,
                        "score": float(score),
                    },
                )

        # FAISS IndexFlatIP returns results in descending order by default
        return results

    def delete_by_doc(self, doc_uid: str) -> int:
        """Delete all embeddings for a document.

        Note: FAISS doesn't support efficient deletion, so we rebuild the index.
        This is slow for large indexes but works for now.

        Args:
            doc_uid: Document UID to delete.

        Returns:
            Number of embeddings deleted.

        """
        if self._index is None:
            return 0

        # Find IDs to delete
        ids_to_delete = [idx for idx, (uid, _) in self._id_map.items() if uid == doc_uid]
        if not ids_to_delete:
            return 0

        count = len(ids_to_delete)

        # Rebuild index without deleted items
        if self._index.ntotal == count:
            # Deleting everything
            dimension = self._index.d
            self._index = faiss.IndexFlatIP(dimension)
            self._id_map = {}
        else:
            # Get all vectors and filter
            all_vectors = self._index.reconstruct_n(0, self._index.ntotal)  # type: ignore[union-attr]
            new_vectors = []
            new_id_map: dict[int, tuple[str, int]] = {}
            new_idx = 0

            for old_idx in range(self._index.ntotal):
                if old_idx not in ids_to_delete:
                    new_vectors.append(all_vectors[old_idx])
                    new_id_map[new_idx] = self._id_map[old_idx]
                    new_idx += 1

            # Create new IndexFlatIP (cosine similarity via inner product)
            dimension = self._index.d
            self._index = faiss.IndexFlatIP(dimension)
            self._index.add(np.array(new_vectors).astype("float32"))  # type: ignore[union-attr]
            self._id_map = new_id_map

        self._deleted_doc_uids.add(doc_uid)
        logger.info(f"Deleted {count} embeddings for doc_uid={doc_uid}")
        return count


def compute_embeddings(texts: list[str]) -> np.ndarray:
    """Compute embeddings for a list of texts.

    Args:
        texts: List of text strings to embed.

    Returns:
        numpy array of embeddings.

    """
    model = get_embedding_model(EMBEDDING_MODEL)
    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings.astype("float32")
