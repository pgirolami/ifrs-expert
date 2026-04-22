"""Tests for the retrieve command."""

from __future__ import annotations

import json
from typing import cast

from src.interfaces import DocumentSearchResult, SearchDocumentVectorStoreProtocol, SearchResult, SearchVectorStoreProtocol
from src.models.chunk import Chunk
from src.models.section import SectionRecord
from tests.fakes import InMemoryChunkStore, InMemorySectionStore
from tests.policy import make_retrieval_policy


class MockVectorStore(SearchVectorStoreProtocol):
    """Minimal mock for chunk vector store context manager."""

    def __init__(self, search_results: list[dict[str, str | int | float]]) -> None:
        self._search_results = cast(list[SearchResult], search_results)

    def __enter__(self) -> "MockVectorStore":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[SearchResult]:
        del query
        return self._search_results


class MockDocumentVectorStore(SearchDocumentVectorStoreProtocol):
    """Minimal mock for document vector store context manager."""

    def __init__(self, search_results: list[dict[str, str | float]]) -> None:
        self._search_results = cast(list[DocumentSearchResult], search_results)

    def __enter__(self) -> "MockDocumentVectorStore":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[DocumentSearchResult]:
        del query
        return self._search_results


class RepresentationAwareDocumentVectorStoreFactory:
    """Factory returning per-representation mock stores and recording calls."""

    def __init__(self, results_by_representation: dict[str, list[dict[str, str | float]]]) -> None:
        self._results_by_representation = results_by_representation
        self.called_representations: list[str] = []

    def __call__(self, representation: str) -> MockDocumentVectorStore:
        self.called_representations.append(representation)
        return MockDocumentVectorStore(self._results_by_representation.get(representation, []))


class MockIndexPath:
    """Mock index path."""

    def __init__(self, exists: bool = True) -> None:
        self._exists = exists

    def exists(self) -> bool:
        return self._exists


def test_retrieve_documents_mode_applies_per_type_thresholds_and_overall_cap() -> None:
    """Documents mode should apply per-type thresholds before the overall document cap."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifric16", chunk_number="1.1", page_start="A1", page_end="A1", text="ifric chunk"),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="2.1", page_start="B1", page_end="B1", text="ifrs chunk"),
                Chunk(id=3, doc_uid="ias21", chunk_number="3.1", page_start="C1", page_end="C1", text="ias chunk"),
                Chunk(id=4, doc_uid="sic25", chunk_number="4.1", page_start="D1", page_end="D1", text="sic chunk"),
                Chunk(id=5, doc_uid="ps1", chunk_number="5.1", page_start="E1", page_end="E1", text="ps chunk"),
            ]
        )

    command = RetrieveCommand(
        query="foreign currency",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifric16", "chunk_id": 1, "score": 0.96},
                    {"doc_uid": "ifrs9", "chunk_id": 2, "score": 0.95},
                    {"doc_uid": "ias21", "chunk_id": 3, "score": 0.94},
                    {"doc_uid": "sic25", "chunk_id": 4, "score": 0.93},
                    {"doc_uid": "ps1", "chunk_id": 5, "score": 0.92},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifric16", "score": 0.60},
                    {"doc_uid": "ifrs9", "score": 0.595},
                    {"doc_uid": "ias21", "score": 0.56},
                    {"doc_uid": "sic25", "score": 0.52},
                    {"doc_uid": "ps1", "score": 0.49},
                ]
            ),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(policy=make_retrieval_policy(k=5, d=3, chunk_min_score=0.5, expand=0, mode="documents"), verbose=False,
        ),
    )

    result = command.execute()

    data = json.loads(result)
    assert data["retrieval_mode"] == "documents"
    assert data["document_hits"] == [
        {"doc_uid": "ifric16", "score": 0.6, "document_type": "IFRIC", "document_kind": "interpretation"},
        {"doc_uid": "ifrs9", "score": 0.595, "document_type": "IFRS-S", "document_kind": "standard"},
        {"doc_uid": "ias21", "score": 0.56, "document_type": "IAS-S", "document_kind": "standard"},
    ]
    assert [chunk["doc_uid"] for chunk in data["chunks"]] == ["ifric16", "ifrs9", "ias21"]
    assert [chunk["text"] for chunk in data["chunks"]] == ["ifric chunk", "ifrs chunk", "ias chunk"]


def test_retrieve_documents_mode_respects_per_type_document_caps() -> None:
    """Documents mode should respect per-type document caps before chunk retrieval."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifric16", chunk_number="1.1", page_start="A1", page_end="A1", text="ifric 16 chunk"),
                Chunk(id=2, doc_uid="ifric17", chunk_number="1.2", page_start="A2", page_end="A2", text="ifric 17 chunk"),
                Chunk(id=3, doc_uid="ifrs9", chunk_number="2.1", page_start="B1", page_end="B1", text="ifrs chunk"),
            ]
        )

    command = RetrieveCommand(
        query="foreign currency",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifric16", "chunk_id": 1, "score": 0.96},
                    {"doc_uid": "ifric17", "chunk_id": 2, "score": 0.95},
                    {"doc_uid": "ifrs9", "chunk_id": 3, "score": 0.94},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifric16", "score": 0.60},
                    {"doc_uid": "ifric17", "score": 0.59},
                    {"doc_uid": "ifrs9", "score": 0.595},
                ]
            ),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            policy=make_retrieval_policy(k=5, d=5, chunk_min_score=0.5, expand=0, per_type_d={"IFRIC": 1}, mode="documents"),
            verbose=False,
        ),
    )

    result = command.execute()

    data = json.loads(result)
    assert data["document_hits"] == [
        {"doc_uid": "ifric16", "score": 0.6, "document_type": "IFRIC", "document_kind": "interpretation"},
        {"doc_uid": "ifrs9", "score": 0.595, "document_type": "IFRS-S", "document_kind": "standard"},
    ]
    assert [chunk["doc_uid"] for chunk in data["chunks"]] == ["ifric16", "ifrs9"]


def test_retrieve_expand_to_section_includes_descendant_section_chunks() -> None:
    """Section expansion should include all chunks in the matched section subtree."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="3.0", page_start="A1", page_end="A1", chunk_id="IFRS09_3.0", containing_section_id="IFRS09_0054", text="chapter text"),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="3.1.1", page_start="A2", page_end="A2", chunk_id="IFRS09_3.1.1", containing_section_id="IFRS09_g3.1.1-3.1.2", text="initial recognition text"),
            ]
        )

    section_store = InMemorySectionStore()
    with section_store as store:
        store.insert_sections(
            [
                SectionRecord(
                    section_id="IFRS09_0054",
                    doc_uid="ifrs9",
                    parent_section_id=None,
                    level=2,
                    title="Recognition and derecognition",
                    section_lineage=["Recognition and derecognition"],
                    position=1,
                ),
                SectionRecord(
                    section_id="IFRS09_g3.1.1-3.1.2",
                    doc_uid="ifrs9",
                    parent_section_id="IFRS09_0054",
                    level=3,
                    title="Initial recognition",
                    section_lineage=["Recognition and derecognition", "Initial recognition"],
                    position=2,
                ),
            ]
        )
        store.add_descendant_mapping("IFRS09_0054", ["IFRS09_0054", "IFRS09_g3.1.1-3.1.2"])

    command = RetrieveCommand(
        query="recognition",
        config=RetrieveConfig(
            vector_store=MockVectorStore([{"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.96}]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=section_store,
        ),
        options=RetrieveOptions(policy=make_retrieval_policy(k=5, chunk_min_score=0.5, expand_to_section=True, expand=0, mode="text"), verbose=False),
    )

    result = command.execute()

    data = json.loads(result)
    assert [chunk["id"] for chunk in data["chunks"]] == [1, 2]
    assert data["chunks"][0]["score"] == 0.96
    assert data["chunks"][1]["score"] == 0.0


def test_retrieve_documents_mode_routes_document_search_by_similarity_representation() -> None:
    """Documents mode should search each configured similarity representation index."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="1.1", page_start="A1", page_end="A1", text="ifrs chunk"),
                Chunk(id=2, doc_uid="ifric16", chunk_number="2.1", page_start="B1", page_end="B1", text="ifric chunk"),
            ]
        )

    factory = RepresentationAwareDocumentVectorStoreFactory(
        {
            "background_and_issue": [{"doc_uid": "ifrs9", "score": 0.91}],
            "scope": [{"doc_uid": "ifric16", "score": 0.9}],
            "full": [],
        }
    )

    command = RetrieveCommand(
        query="hedges",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.95},
                    {"doc_uid": "ifric16", "chunk_id": 2, "score": 0.94},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            document_vector_store_factory=factory,
            document_index_path_fn=lambda _representation: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            policy=_build_policy_with_similarity_representation_overrides(
                {
                    "IFRS-S": "background_and_issue",
                    "IFRIC": "scope",
                }
            ),
            verbose=False,
        ),
    )

    result = command.execute()
    data = json.loads(result)

    assert [document_hit["doc_uid"] for document_hit in data["document_hits"]] == ["ifrs9", "ifric16"]
    assert sorted(factory.called_representations) == ["background_and_issue", "full", "scope"]


def test_retrieve_documents2_mode_consolidates_variants_to_standard_doc_uid() -> None:
    """Documents2 mode should collapse variant matches onto the standard doc_uid."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="1.1", page_start="A1", page_end="A1", text="ifrs standard chunk"),
            ]
        )

    command = RetrieveCommand(
        query="hedges",
        config=RetrieveConfig(
            vector_store=MockVectorStore([{"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.95}]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifrs9-bc", "score": 0.81},
                    {"doc_uid": "ifrs9-ie", "score": 0.93},
                    {"doc_uid": "ifrs9", "score": 0.89},
                ]
            ),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            policy=make_retrieval_policy(k=5, d=5, chunk_min_score=0.5, expand=0, mode="documents2", per_type_d={"IFRS-S": 1}, per_type_min_score={"IFRS-S": 0.5}),
            verbose=False,
        ),
    )

    result = command.execute()
    data = json.loads(result)

    assert data["retrieval_mode"] == "documents2"
    assert data["document_hits"] == [
        {"doc_uid": "ifrs9", "score": 0.93, "document_type": "IFRS-S", "document_kind": "standard"},
    ]
    assert [chunk["doc_uid"] for chunk in data["chunks"]] == ["ifrs9"]


def _build_policy_with_similarity_representation_overrides(overrides: dict[str, str]):
    from src.policy import DocumentStageRetrievalPolicy, DocumentTypeRetrievalPolicy, RetrievalPolicy

    base_policy = make_retrieval_policy(mode="documents")
    by_document_type: dict[str, DocumentTypeRetrievalPolicy] = dict(base_policy.documents.by_document_type)
    for document_type, representation in overrides.items():
        existing_policy = by_document_type[document_type]
        by_document_type[document_type] = DocumentTypeRetrievalPolicy(
            d=existing_policy.d,
            min_score=existing_policy.min_score,
            expand_to_section=existing_policy.expand_to_section,
            similarity_representation=representation,
        )
    return RetrievalPolicy(
        mode=base_policy.mode,
        k=base_policy.k,
        expand=base_policy.expand,
        full_doc_threshold=base_policy.full_doc_threshold,
        expand_to_section=base_policy.expand_to_section,
        text=base_policy.text,
        titles=base_policy.titles,
        documents=DocumentStageRetrievalPolicy(
            global_d=base_policy.documents.global_d,
            by_document_type=by_document_type,
        ),
    )


def test_retrieve_verbose_output_starts_with_options() -> None:
    """Verbose retrieve output should start with the options object."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="1.1", page_start="A1", page_end="A1", text="ifrs chunk"),
            ]
        )

    command = RetrieveCommand(
        query="leases",
        config=RetrieveConfig(
            vector_store=MockVectorStore([{"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.96}]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(policy=make_retrieval_policy(k=5, expand=0, mode="text"), verbose=True),
    )

    result = command.execute()

    assert result.startswith("RetrieveOptions(policy=")
    assert "Retrieved chunks:" in result
    assert "Document: ifrs9" in result
