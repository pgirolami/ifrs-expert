"""Tests for the retrieve command."""

from __future__ import annotations

import json
from typing import cast

from src.interfaces import DocumentSearchResult, SearchDocumentVectorStoreProtocol, SearchResult, SearchVectorStoreProtocol
from src.models.chunk import Chunk
from src.models.reference import ContentReference
from src.models.section import SectionRecord
from src.policy import RetrievalPolicy
from tests.fakes import InMemoryChunkStore, InMemoryReferenceStore, InMemorySectionStore
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
        options=RetrieveOptions(
            policy=make_retrieval_policy(k=5, d=3, chunk_min_score=0.5, expand=0, mode="documents"),
            verbose=False,
        ),
    )

    result = command.execute()

    data = json.loads(result)
    assert data["policy_name"] == "documents"
    assert data["document_routing_source"] == "document_representation"
    assert data["document_routing_post_processing"] == "none"
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


def test_retrieve_expands_same_family_references_before_section_expansion() -> None:
    """Reference expansion should recover the governing paragraph before section fan-out runs."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9-bc", chunk_number="B1", page_start="A1", page_end="A1", chunk_id="IFRS09BC_B1", containing_section_id="IFRS09BC_S1", text="application guidance chunk"),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="5.1", page_start="B1", page_end="B1", chunk_id="IFRS09_5.1", containing_section_id="IFRS09_S5", text="governing paragraph"),
                Chunk(id=3, doc_uid="ifrs9", chunk_number="5.1.1", page_start="B2", page_end="B2", chunk_id="IFRS09_5.1.1", containing_section_id="IFRS09_S5_1", text="section child"),
            ]
        )

    section_store = InMemorySectionStore()
    with section_store as store:
        store.insert_sections(
            [
                SectionRecord(
                    section_id="IFRS09_S5",
                    doc_uid="ifrs9",
                    parent_section_id=None,
                    level=2,
                    title="Recognition",
                    section_lineage=["Recognition"],
                    position=1,
                ),
                SectionRecord(
                    section_id="IFRS09_S5_1",
                    doc_uid="ifrs9",
                    parent_section_id="IFRS09_S5",
                    level=3,
                    title="Initial recognition",
                    section_lineage=["Recognition", "Initial recognition"],
                    position=2,
                ),
            ]
        )
        store.add_descendant_mapping("IFRS09_S5", ["IFRS09_S5", "IFRS09_S5_1"])

    reference_store = InMemoryReferenceStore()
    with reference_store as store:
        store.insert_references(
            [
                ContentReference(
                    source_doc_uid="ifrs9-bc",
                    source_location_type="chunk",
                    source_chunk_id="IFRS09BC_B1",
                    annotation_raw_text="Refer: paragraph 5.1",
                    target_raw_text="paragraph 5.1",
                    target_kind="same_standard_paragraph",
                    target_start="5.1",
                    parsed_ok=True,
                )
            ]
        )

    command = RetrieveCommand(
        query="recognition",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifrs9-bc", "chunk_id": 1, "score": 0.96},
                    {"doc_uid": "ifrs9", "chunk_id": 2, "score": 0.94},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=section_store,
            reference_store=reference_store,
        ),
        options=RetrieveOptions(policy=make_retrieval_policy(k=5, chunk_min_score=0.5, expand_to_section=True, expand=0, mode="text"), verbose=False),
    )

    result = command.execute()
    data = json.loads(result)

    assert [chunk["doc_uid"] for chunk in data["chunks"]] == ["ifrs9-bc", "ifrs9", "ifrs9"]
    assert [chunk["chunk_number"] for chunk in data["chunks"]] == ["B1", "5.1", "5.1.1"]
    assert [chunk["provenance"] for chunk in data["chunks"]] == ["similarity", "similarity", "exp_section_from_seed"]


def test_retrieve_expands_same_family_references_across_two_levels() -> None:
    """Depth-2 reference expansion should follow an intermediate governing paragraph."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9-bc", chunk_number="B1", page_start="A1", page_end="A1", chunk_id="IFRS09BC_B1", containing_section_id="IFRS09BC_S1", text="application guidance chunk"),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="4.1.1", page_start="B1", page_end="B1", chunk_id="IFRS09_4.1.1", containing_section_id="IFRS09_S4", text="governing paragraph"),
                Chunk(id=3, doc_uid="ifrs9", chunk_number="B4.1.7", page_start="B2", page_end="B2", chunk_id="IFRS09_B4.1.7", containing_section_id="IFRS09_S4_1", text="guidance chunk 1"),
                Chunk(id=4, doc_uid="ifrs9", chunk_number="B4.1.8", page_start="B3", page_end="B3", chunk_id="IFRS09_B4.1.8", containing_section_id="IFRS09_S4_1", text="guidance chunk 2"),
                Chunk(id=5, doc_uid="ifrs9", chunk_number="B4.1.9", page_start="B4", page_end="B4", chunk_id="IFRS09_B4.1.9", containing_section_id="IFRS09_S4_1", text="guidance chunk 3"),
            ]
        )

    reference_store = InMemoryReferenceStore()
    with reference_store as store:
        store.insert_references(
            [
                ContentReference(
                    source_doc_uid="ifrs9-bc",
                    source_location_type="chunk",
                    source_chunk_id="IFRS09BC_B1",
                    annotation_raw_text="Refer: paragraph 4.1.1",
                    target_raw_text="paragraph 4.1.1",
                    target_kind="same_standard_paragraph",
                    target_start="4.1.1",
                    parsed_ok=True,
                ),
                ContentReference(
                    source_doc_uid="ifrs9",
                    source_location_type="chunk",
                    source_chunk_id="IFRS09_4.1.1",
                    annotation_raw_text="Refer: paragraphs B4.1.7-B4.1.9",
                    target_raw_text="paragraphs B4.1.7-B4.1.9",
                    target_kind="same_standard_paragraph",
                    target_start="B4.1.7",
                    target_end="B4.1.9",
                    parsed_ok=True,
                ),
            ]
        )

    base_config = RetrieveConfig(
        vector_store=MockVectorStore([{"doc_uid": "ifrs9-bc", "chunk_id": 1, "score": 0.96}]),
        chunk_store=chunk_store,
        init_db_fn=lambda: None,
        index_path_fn=lambda: MockIndexPath(exists=True),
        reference_store=reference_store,
    )

    depth_one_command = RetrieveCommand(
        query="recognition",
        config=base_config,
        options=RetrieveOptions(policy=make_retrieval_policy(k=5, chunk_min_score=0.5, expand=0, expand_to_section=False, reference_expand_depth=1, mode="text"), verbose=False),
    )
    depth_two_command = RetrieveCommand(
        query="recognition",
        config=base_config,
        options=RetrieveOptions(policy=make_retrieval_policy(k=5, chunk_min_score=0.5, expand=0, expand_to_section=False, reference_expand_depth=2, mode="text"), verbose=False),
    )

    depth_one_data = json.loads(depth_one_command.execute())
    depth_two_data = json.loads(depth_two_command.execute())

    assert [chunk["chunk_number"] for chunk in depth_one_data["chunks"]] == ["B1", "4.1.1"]
    assert [chunk["provenance"] for chunk in depth_one_data["chunks"]] == ["similarity", "ref_sf"]
    assert [chunk["chunk_number"] for chunk in depth_two_data["chunks"]] == ["B1", "4.1.1", "B4.1.7", "B4.1.8", "B4.1.9"]
    assert [chunk["provenance"] for chunk in depth_two_data["chunks"]] == ["similarity", "ref_sf", "ref_sf", "ref_sf", "ref_sf"]


def test_retrieve_expands_section_target_references() -> None:
    """Section targets should resolve through same-family reference expansion."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9-bc", chunk_number="B1", page_start="A1", page_end="A1", chunk_id="IFRS09BC_B1", containing_section_id="IFRS09BC_S1", text="source chunk"),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="5.5.1", page_start="B1", page_end="B1", chunk_id="IFRS09_5.5.1", containing_section_id="IFRS09_g5.5.1-5.5.8", text="section target chunk"),
                Chunk(id=3, doc_uid="ifrs9", chunk_number="5.5.2", page_start="B2", page_end="B2", chunk_id="IFRS09_5.5.2", containing_section_id="IFRS09_g5.5.1-5.5.8", text="section child chunk"),
                Chunk(id=4, doc_uid="ifrs9", chunk_number="5.5.15", page_start="B3", page_end="B3", chunk_id="IFRS09_5.5.15", containing_section_id="IFRS09_g5.5.15-5.5.16", text="later subsection chunk"),
                Chunk(id=5, doc_uid="ifrs9", chunk_number="5.5.16", page_start="B4", page_end="B4", chunk_id="IFRS09_5.5.16", containing_section_id="IFRS09_g5.5.15-5.5.16", text="later subsection child"),
            ]
        )

    section_store = InMemorySectionStore()
    with section_store as store:
        store.insert_sections(
            [
                SectionRecord(
                    section_id="IFRS09_g5.5.1-5.5.20",
                    doc_uid="ifrs9",
                    parent_section_id=None,
                    level=2,
                    title="Section 5.5",
                    section_lineage=["Section 5.5"],
                    position=1,
                ),
                SectionRecord(
                    section_id="IFRS09_g5.5.1-5.5.14",
                    doc_uid="ifrs9",
                    parent_section_id="IFRS09_g5.5.1-5.5.20",
                    level=3,
                    title="Section 5.5.1-5.5.14",
                    section_lineage=["Section 5.5", "Section 5.5.1-5.5.14"],
                    position=2,
                ),
                SectionRecord(
                    section_id="IFRS09_g5.5.1-5.5.8",
                    doc_uid="ifrs9",
                    parent_section_id="IFRS09_g5.5.1-5.5.14",
                    level=3,
                    title="Section 5.5.1-5.5.8",
                    section_lineage=["Section 5.5", "Section 5.5.1-5.5.14", "Section 5.5.1-5.5.8"],
                    position=3,
                ),
                SectionRecord(
                    section_id="IFRS09_g5.5.15-5.5.16",
                    doc_uid="ifrs9",
                    parent_section_id="IFRS09_g5.5.1-5.5.20",
                    level=3,
                    title="Section 5.5.15-5.5.16",
                    section_lineage=["Section 5.5", "Section 5.5.15-5.5.16"],
                    position=4,
                ),
            ]
        )
        store.add_descendant_mapping("IFRS09_g5.5.1-5.5.20", ["IFRS09_g5.5.1-5.5.20", "IFRS09_g5.5.1-5.5.14", "IFRS09_g5.5.1-5.5.8", "IFRS09_g5.5.15-5.5.16"])

    reference_store = InMemoryReferenceStore()
    with reference_store as store:
        store.insert_references(
            [
                ContentReference(
                    source_doc_uid="ifrs9-bc",
                    source_location_type="chunk",
                    source_chunk_id="IFRS09BC_B1",
                    annotation_raw_text="Refer: Section 5.5",
                    target_raw_text="Section 5.5",
                    target_kind="same_standard_paragraph",
                    target_unit="section",
                    target_start="5.5",
                    parsed_ok=True,
                )
            ]
        )

    command = RetrieveCommand(
        query="section 5.5",
        config=RetrieveConfig(
            vector_store=MockVectorStore([{"doc_uid": "ifrs9-bc", "chunk_id": 1, "score": 0.96}]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=section_store,
            reference_store=reference_store,
        ),
        options=RetrieveOptions(policy=make_retrieval_policy(k=5, chunk_min_score=0.5, expand=0, expand_to_section=False, reference_expand_depth=1, mode="text"), verbose=False),
    )

    data = json.loads(command.execute())
    assert [chunk["chunk_number"] for chunk in data["chunks"]] == ["B1", "5.5.1", "5.5.2", "5.5.15", "5.5.16"]
    assert [chunk["provenance"] for chunk in data["chunks"]] == ["similarity", "ref_sf", "exp_sect_from_reference", "exp_sect_from_reference", "exp_sect_from_reference"]


def test_retrieve_expands_suffixed_appendix_ranges() -> None:
    """Appendix B ranges like B4.1.2C-B4.1.4 should resolve during reference expansion."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="4.1.2", page_start="B1", page_end="B1", chunk_id="IFRS09_4.1.2", containing_section_id="IFRS09_S4", text="source chunk"),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="B4.1.2C", page_start="B2", page_end="B2", chunk_id="IFRS09_B4.1.2C", containing_section_id="IFRS09_B4", text="appendix target chunk"),
                Chunk(id=3, doc_uid="ifrs9", chunk_number="B4.1.4", page_start="B3", page_end="B3", chunk_id="IFRS09_B4.1.4", containing_section_id="IFRS09_B4", text="appendix end chunk"),
            ]
        )

    reference_store = InMemoryReferenceStore()
    with reference_store as store:
        store.insert_references(
            [
                ContentReference(
                    source_doc_uid="ifrs9",
                    source_location_type="chunk",
                    source_chunk_id="IFRS09_4.1.2",
                    annotation_raw_text="Refer: paragraphs B4.1.2C-B4.1.4",
                    target_raw_text="paragraphs B4.1.2C-B4.1.4",
                    target_kind="same_standard_paragraph",
                    target_start="B4.1.2C",
                    target_end="B4.1.4",
                    parsed_ok=True,
                )
            ]
        )

    command = RetrieveCommand(
        query="business model",
        config=RetrieveConfig(
            vector_store=MockVectorStore([{"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.96}]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            reference_store=reference_store,
        ),
        options=RetrieveOptions(policy=make_retrieval_policy(k=5, chunk_min_score=0.5, expand=0, expand_to_section=False, reference_expand_depth=1, mode="text"), verbose=False),
    )

    data = json.loads(command.execute())
    assert [chunk["chunk_number"] for chunk in data["chunks"]] == ["4.1.2", "B4.1.2C", "B4.1.4"]
    assert [chunk["provenance"] for chunk in data["chunks"]] == ["similarity", "ref_sf", "ref_sf"]


def test_retrieve_ignores_cross_document_and_non_standard_references_in_v1() -> None:
    """Cross-document and BC/IE/IG references should not be auto-followed in v1."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9-bc", chunk_number="B1", page_start="A1", page_end="A1", chunk_id="IFRS09BC_B1", containing_section_id="IFRS09BC_S1", text="supporting chunk"),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="9", page_start="B1", page_end="B1", chunk_id="IFRS09_9", containing_section_id="IFRS09_S9", text="cross doc target"),
            ]
        )

    reference_store = InMemoryReferenceStore()
    with reference_store as store:
        store.insert_references(
            [
                ContentReference(
                    source_doc_uid="ifrs9-bc",
                    source_location_type="chunk",
                    source_chunk_id="IFRS09BC_B1",
                    annotation_raw_text="Refer: IAS 24 paragraph 9",
                    target_raw_text="IAS 24 paragraph 9",
                    target_kind="cross_document",
                    target_doc_hint="IAS 24",
                    target_start="9",
                    parsed_ok=True,
                ),
                ContentReference(
                    source_doc_uid="ifrs9-bc",
                    source_location_type="chunk",
                    source_chunk_id="IFRS09BC_B1",
                    annotation_raw_text="Refer: BC4.1",
                    target_raw_text="BC4.1",
                    target_kind="basis_for_conclusions",
                    target_start="BC4.1",
                    parsed_ok=True,
                ),
            ]
        )

    command = RetrieveCommand(
        query="recognition",
        config=RetrieveConfig(
            vector_store=MockVectorStore([{"doc_uid": "ifrs9-bc", "chunk_id": 1, "score": 0.96}]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            reference_store=reference_store,
        ),
        options=RetrieveOptions(policy=make_retrieval_policy(k=5, chunk_min_score=0.5, expand_to_section=True, expand=0, mode="text"), verbose=False),
    )

    result = command.execute()
    data = json.loads(result)

    assert [chunk["doc_uid"] for chunk in data["chunks"]] == ["ifrs9-bc"]
    assert data["chunks"][0]["provenance"] == "similarity"


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

    assert data["policy_name"] == "documents2"
    assert data["document_routing_source"] == "document_representation"
    assert data["document_routing_post_processing"] == "aggregate_to_main_variant"
    assert data["document_hits"] == [
        {"doc_uid": "ifrs9", "score": 0.93, "document_type": "IFRS-S", "document_kind": "standard"},
    ]
    assert [chunk["doc_uid"] for chunk in data["chunks"]] == ["ifrs9"]


def test_retrieve_documents2_through_chunks_mode_routes_and_scores_by_chunk_similarity() -> None:
    """documents2-through-chunks should route on chunk scores and keep only routed docs."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9-bc", chunk_number="bc.1", page_start="A1", page_end="A1", text="supporting chunk"),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="1.1", page_start="B1", page_end="B1", text="standard chunk"),
                Chunk(id=3, doc_uid="ifric16", chunk_number="1.1", page_start="C1", page_end="C1", text="other standard chunk"),
            ]
        )

    command = RetrieveCommand(
        query="hedges",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifrs9-bc", "chunk_id": 1, "score": 0.98},
                    {"doc_uid": "ifrs9", "chunk_id": 2, "score": 0.94},
                    {"doc_uid": "ifric16", "chunk_id": 3, "score": 0.96},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            policy=make_retrieval_policy(
                k=5,
                d=1,
                chunk_min_score=0.5,
                expand=0,
                mode="documents2-through-chunks",
                per_type_d={"IFRS-S": 1, "IFRIC": 1},
                per_type_min_score={"IFRS-S": 0.5, "IFRIC": 0.5},
            ),
            verbose=False,
        ),
    )

    result = command.execute()
    data = json.loads(result)

    assert data["policy_name"] == "documents2-through-chunks"
    assert data["document_routing_source"] == "top_chunk_results"
    assert data["document_routing_post_processing"] == "aggregate_to_main_variant"
    assert data["document_hits"] == [
        {"doc_uid": "ifrs9", "score": 0.98, "document_type": "IFRS-S", "document_kind": "standard"},
    ]
    assert [chunk["doc_uid"] for chunk in data["chunks"]] == ["ifrs9"]
    assert [chunk["score"] for chunk in data["chunks"]] == [0.94]


def test_retrieve_logs_top_chunk_per_output_document(caplog) -> None:
    """Retrieve should log the top chunk section number and section preview for each output document."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="doc1", chunk_number="5.1", page_start="A1", page_end="A1", text="This is the first section text and it keeps going."),
                Chunk(id=2, doc_uid="doc1", chunk_number="5.2", page_start="A2", page_end="A2", text="Another section."),
            ]
        )

    command = RetrieveCommand(
        query="leases",
        config=RetrieveConfig(
            vector_store=MockVectorStore([{"doc_uid": "doc1", "chunk_id": 1, "score": 0.96}]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(policy=make_retrieval_policy(k=5, expand=0, mode="text"), verbose=False),
    )

    with caplog.at_level("INFO"):
        command.execute()

    assert "section_number=5.1" in caplog.text
    assert "score=0.9600" in caplog.text
    assert "section_text_preview='This is the first section text'" in caplog.text


def test_retrieve_logs_highest_scoring_chunk_for_each_output_document(caplog) -> None:
    """Retrieve should log the highest-scoring selected chunk, not the first chunk in document order."""
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="6.3.1", page_start="A1", page_end="A1", text="A lower-scoring selected chunk."),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="6.3.2", page_start="A2", page_end="A2", text="A higher-scoring selected chunk."),
            ]
        )

    command = RetrieveCommand(
        query="hedges",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifrs9", "chunk_id": 2, "score": 0.6376},
                    {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.0},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(policy=make_retrieval_policy(k=5, expand=0, mode="text"), verbose=False),
    )

    with caplog.at_level("INFO"):
        command.execute()

    assert "section_number=6.3.2" in caplog.text
    assert "score=0.6376" in caplog.text
    assert "section_number=6.3.1" not in caplog.text or "score=0.0000" not in caplog.text


def _build_policy_with_similarity_representation_overrides(overrides: dict[str, str]) -> RetrievalPolicy:
    from src.policy import DocumentStageRetrievalPolicy, DocumentTypeRetrievalPolicy, ResolvedRetrievalPolicy

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
    return ResolvedRetrievalPolicy(
        policy_name=base_policy.policy_name,
        querying=base_policy.querying,
        document_routing=base_policy.document_routing,
        chunk_retrieval=base_policy.chunk_retrieval,
        legacy_document_stage=DocumentStageRetrievalPolicy(
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
