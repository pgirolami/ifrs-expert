"""Vector store for IFRS Expert using FAISS and SentenceTransformers."""

import json
import logging
import os
from pathlib import Path
from typing import Self

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Suppress sentence-transformers logging
os.environ["TOKENIZERS_PARALLELISM"] = "false"
logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
logging.getLogger("transformers").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

EMBEDDING_MODEL = "BAAI/bge-m3"
INDEX_PATH = Path(__file__).parent.parent.parent / "data" / "index" / "faiss.index"
ID_MAP_PATH = Path(__file__).parent.parent.parent / "data" / "index" / "id_map.json"


def get_index_path() -> Path:
    """Get the FAISS index path, creating directory if needed."""
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    return INDEX_PATH


def get_id_map_path() -> Path:
    """Get the ID mapping file path."""
    ID_MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
    return ID_MAP_PATH


class VectorStore:
    """Manages vector embeddings using FAISS and SentenceTransformers."""

    def __init__(self) -> None:
        """Initialize the vector store."""
        self._index: faiss.Index | None = None
        self._model: SentenceTransformer | None = None
        self._id_map: dict[int, tuple[str, int]] = {}  # faiss_id -> (doc_uid, chunk_id)

    def __enter__(self) -> Self:
        """Context manager entry - load or create index."""
        self._load_or_create_index()
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Context manager exit - save index."""
        self._save_index()

    def _get_model(self) -> SentenceTransformer:
        """Get or create the embedding model (singleton)."""
        if self._model is None:
            logger.info(f"Loading embedding model: {EMBEDDING_MODEL}")
            self._model = SentenceTransformer(EMBEDDING_MODEL)
        return self._model

    def _load_or_create_index(self) -> None:
        """Load existing index or create a new one."""
        index_path = get_index_path()
        id_map_path = get_id_map_path()

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
            index_path = get_index_path()
            id_map_path = get_id_map_path()

            logger.info(f"Saving FAISS index to {index_path}")
            faiss.write_index(self._index, str(index_path))

            # Save ID map
            with id_map_path.open("w") as f:
                json.dump({str(k): list(v) for k, v in self._id_map.items()}, f)

            logger.info(f"Saved index with {self._index.ntotal} vectors")

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

        # Compute embeddings (locally, no progress bar)
        embeddings = model.encode(texts, show_progress_bar=False)

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

        logger.info(f"Added {len(texts)} embeddings to index")

    def search(self, query: str, k: int = 5) -> list[dict]:
        """Search for similar chunks.

        Args:
            query: Search query text.
            k: Number of results to return.

        Returns:
            List of results with doc_uid, chunk_id, text, and relevance score.
            Score is cosine similarity (0-1, higher is better).
        """
        if self._index is None or self._index.ntotal == 0:
            logger.warning("Index is empty, no results to return")
            return []

        model = self._get_model()
        query_embedding = model.encode([query]).astype("float32")

        # Normalize query embedding for cosine similarity
        query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)

        # Search using inner product (which becomes cosine similarity with normalized vectors)
        scores, indices = self._index.search(query_embedding, k)  # type: ignore[union-attr]

        results: list[dict] = []
        for score, idx in zip(scores[0], indices[0], strict=True):
            if idx >= 0 and idx in self._id_map:
                doc_uid, chunk_id = self._id_map[idx]
                results.append(
                    {
                        "doc_uid": doc_uid,
                        "chunk_id": chunk_id,
                        "score": float(score),
                    }
                )

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
            self._index = faiss.IndexFlatL2(dimension)
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

            # Create new index
            dimension = self._index.d
            self._index = faiss.IndexFlatL2(dimension)
            self._index.add(np.array(new_vectors).astype("float32"))  # type: ignore[union-attr]
            self._id_map = new_id_map

        logger.info(f"Deleted {count} embeddings for doc_uid={doc_uid}")
        return count


def compute_embeddings(texts: list[str]) -> np.ndarray:
    """Compute embeddings for a list of texts.

    Args:
        texts: List of text strings to embed.

    Returns:
        numpy array of embeddings.
    """
    model = SentenceTransformer(EMBEDDING_MODEL)
    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings.astype("float32")
