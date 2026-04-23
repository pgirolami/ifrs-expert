"""Tests for retrieval query embedding modes in the shared pipeline."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from src.retrieval.models import RetrievalRequest
from src.retrieval.pipeline import RetrievalPipelineConfig, execute_retrieval
from tests.fakes import InMemoryChunkStore


class RecordingVectorStore:
    """Vector-store fake that records the query it received."""

    def __init__(self) -> None:
        self.received_queries: list[str] = []

    def __enter__(self) -> "RecordingVectorStore":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str):
        self.received_queries.append(query)
        return [{"doc_uid": "ifric16", "chunk_id": 1, "score": 0.9}]


@dataclass(frozen=True)
class ExistingIndexPath:
    """Fake existing index path for retrieval tests."""

    def exists(self) -> bool:
        """Pretend the backing index exists."""
        return True


def _build_request(query_embedding_mode: str) -> RetrievalRequest:
    return RetrievalRequest(
        query="documentation de couverture",
        query_embedding_mode=query_embedding_mode,
        retrieval_mode="text",
        k=1,
        d=1,
        document_d_by_type={},
        document_min_score_by_type={},
        document_expand_to_section_by_type={},
        document_similarity_representation_by_type={},
        chunk_min_score=0.0,
        expand_to_section=False,
        expand=0,
        full_doc_threshold=0,
    )


def test_execute_retrieval_uses_raw_query_embedding_mode() -> None:
    """Raw mode should send the unmodified query text to vector search."""
    vector_store = RecordingVectorStore()
    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks([])

    execute_retrieval(
        request=_build_request("raw"),
        config=RetrievalPipelineConfig(
            vector_store=vector_store,
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: ExistingIndexPath(),
        ),
    )

    assert vector_store.received_queries == ["documentation de couverture"]


def test_execute_retrieval_uses_enriched_query_embedding_mode() -> None:
    """Enriched mode should append glossary-driven English terms before retrieval."""
    vector_store = RecordingVectorStore()
    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks([])

    execute_retrieval(
        request=_build_request("enriched"),
        config=RetrievalPipelineConfig(
            vector_store=vector_store,
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: ExistingIndexPath(),
        ),
    )

    assert vector_store.received_queries == ["documentation de couverture\nhedge accounting"]
