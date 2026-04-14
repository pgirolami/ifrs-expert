"""Shared embedding-model cache for vector stores."""

from __future__ import annotations

import logging
from collections.abc import Callable
from dataclasses import dataclass
from threading import Lock
from typing import TYPE_CHECKING, Protocol, cast

from sentence_transformers import SentenceTransformer

if TYPE_CHECKING:
    import numpy as np

logger = logging.getLogger(__name__)

EMBEDDING_MODEL = "BAAI/bge-m3"
BATCH_SIZE = 1


class EmbeddingModelProtocol(Protocol):
    """Minimal protocol shared by vector-store embedding models."""

    def encode(
        self,
        inputs: str | list[str],
        *,
        batch_size: int | None = None,
        show_progress_bar: bool = False,
    ) -> np.ndarray:
        """Encode one or more texts into embedding vectors."""


EmbeddingModelFactory = Callable[[str], EmbeddingModelProtocol]


@dataclass
class _ModelCacheState:
    """Mutable process-wide state for the shared embedding-model cache."""

    factory: EmbeddingModelFactory | None = None


_MODEL_CACHE: dict[str, EmbeddingModelProtocol] = {}
_MODEL_CACHE_LOCK = Lock()
_MODEL_CACHE_STATE = _ModelCacheState()


def _default_embedding_model_factory(model_name: str) -> EmbeddingModelProtocol:
    """Create a sentence-transformer model for the requested name."""
    return cast("EmbeddingModelProtocol", SentenceTransformer(model_name))


def get_embedding_model(model_name: str) -> EmbeddingModelProtocol:
    """Return a cached embedding model, creating it on first use."""
    with _MODEL_CACHE_LOCK:
        cached_model = _MODEL_CACHE.get(model_name)
        if cached_model is not None:
            return cached_model

        logger.info(f"Loading embedding model: {model_name}")
        model_factory = _MODEL_CACHE_STATE.factory or _default_embedding_model_factory
        model = model_factory(model_name)
        _MODEL_CACHE[model_name] = model
        return model


def clear_embedding_model_cache() -> None:
    """Clear the process-wide embedding-model cache."""
    with _MODEL_CACHE_LOCK:
        _MODEL_CACHE.clear()


def set_embedding_model_factory(factory: EmbeddingModelFactory | None) -> None:
    """Override the embedding-model factory used by the shared cache."""
    with _MODEL_CACHE_LOCK:
        _MODEL_CACHE_STATE.factory = factory
