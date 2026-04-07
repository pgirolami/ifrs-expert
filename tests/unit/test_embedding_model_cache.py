"""Tests for shared embedding-model caching across vector stores."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from src.vector.model_cache import clear_embedding_model_cache, get_embedding_model, set_embedding_model_factory
from src.vector.store import VectorStore
from src.vector.title_store import TitleVectorStore


@dataclass
class RecordingModel:
    """Simple fake embedding model instance."""

    model_name: str

    def encode(
        self,
        inputs: str | list[str],
        batch_size: int | None = None,
        show_progress_bar: bool = False,
    ) -> np.ndarray:
        """Return a trivial embedding so the fake satisfies the shared protocol."""
        del batch_size, show_progress_bar
        if isinstance(inputs, str):
            return np.array([1.0], dtype="float32")
        return np.array([[1.0] for _ in inputs], dtype="float32")


class RecordingModelFactory:
    """Factory that records how many model instances are created."""

    def __init__(self) -> None:
        self.calls: list[str] = []

    def __call__(self, model_name: str) -> RecordingModel:
        self.calls.append(model_name)
        return RecordingModel(model_name=model_name)


class TestEmbeddingModelCache:
    """Tests for the shared sentence-transformer cache."""

    def setup_method(self) -> None:
        """Reset the process-wide cache before each test."""
        clear_embedding_model_cache()
        set_embedding_model_factory(None)

    def teardown_method(self) -> None:
        """Reset the process-wide cache after each test."""
        clear_embedding_model_cache()
        set_embedding_model_factory(None)

    def test_get_embedding_model_reuses_cached_instance_for_same_name(self) -> None:
        """Repeated lookups of the same model name should return the same instance."""
        factory = RecordingModelFactory()
        set_embedding_model_factory(factory)

        first_model = get_embedding_model("BAAI/bge-m3")
        second_model = get_embedding_model("BAAI/bge-m3")

        assert first_model is second_model
        assert factory.calls == ["BAAI/bge-m3"]

    def test_vector_store_and_title_store_share_one_cached_model_instance(self) -> None:
        """Chunk and title vector stores should share the same cached embedding model."""
        factory = RecordingModelFactory()
        set_embedding_model_factory(factory)

        vector_store = VectorStore()
        title_store = TitleVectorStore()

        first_model = vector_store._get_model()
        second_model = title_store._get_model()

        assert first_model is second_model
        assert factory.calls == ["BAAI/bge-m3"]
