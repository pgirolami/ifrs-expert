"""Tests for document and title vector stores."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from src.vector.document_store import DocumentVectorStore, get_document_id_map_path, get_document_index_path
from src.vector.model_cache import clear_embedding_model_cache, set_embedding_model_factory
from src.vector.title_store import TitleVectorStore


@dataclass
class RecordingEmbeddingModel:
    """Deterministic fake embedding model used by vector-store tests."""

    encode_calls: list[tuple[str | tuple[str, ...], int | None, bool]]

    def encode(
        self,
        inputs: str | list[str],
        batch_size: int | None = None,
        show_progress_bar: bool = False,
    ) -> np.ndarray:
        """Return deterministic non-zero embeddings."""
        if isinstance(inputs, str):
            self.encode_calls.append((inputs, batch_size, show_progress_bar))
            return np.array([1.0, 0.5, 0.25], dtype="float32")

        self.encode_calls.append((tuple(inputs), batch_size, show_progress_bar))
        vectors: list[list[float]] = []
        for index, text in enumerate(inputs, start=1):
            length_factor = float(len(text) + index)
            vectors.append([length_factor, length_factor / 2.0, length_factor / 3.0])
        return np.array(vectors, dtype="float32")


class RecordingEmbeddingModelFactory:
    """Factory returning one shared recording model instance."""

    def __init__(self) -> None:
        self.model = RecordingEmbeddingModel(encode_calls=[])

    def __call__(self, model_name: str) -> RecordingEmbeddingModel:
        del model_name
        return self.model


def setup_function() -> None:
    """Reset process-wide embedding model cache before each test."""
    clear_embedding_model_cache()
    set_embedding_model_factory(None)


def teardown_function() -> None:
    """Reset process-wide embedding model cache after each test."""
    clear_embedding_model_cache()
    set_embedding_model_factory(None)


def test_document_vector_store_add_search_delete_and_reload(tmp_path: Path) -> None:
    """Document store should persist vectors and support search/delete lifecycle."""
    factory = RecordingEmbeddingModelFactory()
    set_embedding_model_factory(factory)

    index_path = tmp_path / "faiss_documents.index"
    id_map_path = tmp_path / "id_map_documents.json"
    query_cache_dir = tmp_path / "query_cache"

    with DocumentVectorStore(index_path=index_path, id_map_path=id_map_path, query_cache_dir=query_cache_dir) as store:
        store.add_embeddings(["ifrs9", "ias7"], ["IFRS text", "IAS text"])
        results_first = store.search_all("hedge accounting")
        results_second = store.search_all("hedge accounting")

        assert {result["doc_uid"] for result in results_first} == {"ifrs9", "ias7"}
        assert {result["doc_uid"] for result in results_second} == {"ifrs9", "ias7"}
        assert store.has_embedding_for_doc("ifrs9") is True
        assert store.has_embedding_for_doc("missing") is False

        deleted_existing = store.delete_by_doc("ias7")
        deleted_missing = store.delete_by_doc("unknown")
        assert deleted_existing == 1
        assert deleted_missing == 0

    assert index_path.exists() is True
    assert id_map_path.exists() is True
    cache_files = list(query_cache_dir.glob("*.npy"))
    assert cache_files, "Expected query embedding cache file to be created"

    with DocumentVectorStore(index_path=index_path, id_map_path=id_map_path, query_cache_dir=query_cache_dir) as reloaded_store:
        results = reloaded_store.search_all("hedge accounting")
        assert [result["doc_uid"] for result in results] == ["ifrs9"]


def test_document_vector_store_validates_parallel_input_lengths(tmp_path: Path) -> None:
    """Document store should reject mismatched doc_uids/texts lengths."""
    factory = RecordingEmbeddingModelFactory()
    set_embedding_model_factory(factory)

    with DocumentVectorStore(
        index_path=tmp_path / "faiss_documents.index",
        id_map_path=tmp_path / "id_map_documents.json",
        query_cache_dir=tmp_path / "query_cache",
    ) as store:
        try:
            store.add_embeddings(["ifrs9"], ["A", "B"])
        except ValueError as error:
            assert "same length" in str(error)
        else:
            raise AssertionError("Expected ValueError for mismatched add_embeddings inputs")


def test_document_vector_store_representation_paths_are_stable() -> None:
    """Representation-aware helpers should preserve legacy full paths and suffix specialized paths."""
    full_index_path = get_document_index_path("full")
    assert full_index_path.name == "faiss_documents.index"
    assert get_document_id_map_path("full").name == "id_map_documents.json"

    scope_index_path = get_document_index_path("scope")
    assert scope_index_path.name == "faiss_documents_scope.index"
    assert get_document_id_map_path("scope").name == "id_map_documents_scope.json"

    background_and_issue_index_path = get_document_index_path("background_and_issue")
    assert background_and_issue_index_path.name == "faiss_documents_background_and_issue.index"
    assert get_document_id_map_path("background_and_issue").name == "id_map_documents_background_and_issue.json"


def test_title_vector_store_add_search_delete_and_reload(tmp_path: Path) -> None:
    """Title store should persist vectors and support section-level search/delete."""
    factory = RecordingEmbeddingModelFactory()
    set_embedding_model_factory(factory)

    index_path = tmp_path / "faiss_titles.index"
    id_map_path = tmp_path / "id_map_titles.json"
    query_cache_dir = tmp_path / "title_query_cache"

    with TitleVectorStore(index_path=index_path, id_map_path=id_map_path, query_cache_dir=query_cache_dir) as store:
        store.add_embeddings(
            doc_uid="ifrs9",
            section_ids=["IFRS09_1", "IFRS09_2"],
            texts=["Scope", "Recognition"],
        )
        store.add_embeddings(
            doc_uid="ias7",
            section_ids=["IAS07_1"],
            texts=["Presentation"],
        )

        results = store.search_all("recognition")
        assert {result["doc_uid"] for result in results} == {"ifrs9", "ias7"}

        deleted_existing = store.delete_by_doc("ias7")
        deleted_missing = store.delete_by_doc("unknown")
        assert deleted_existing == 1
        assert deleted_missing == 0

    assert index_path.exists() is True
    assert id_map_path.exists() is True

    with TitleVectorStore(index_path=index_path, id_map_path=id_map_path, query_cache_dir=query_cache_dir) as reloaded_store:
        results = reloaded_store.search_all("recognition")
        assert all(result["doc_uid"] == "ifrs9" for result in results)
