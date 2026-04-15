"""Tests for query-titles command."""

from __future__ import annotations

import json
from pathlib import Path
from typing import cast

from src.interfaces import SearchResult, SearchVectorStoreProtocol
from src.models.chunk import Chunk
from src.models.section import SectionRecord
from tests.fakes import InMemoryChunkStore, InMemorySectionStore
from tests.policy import load_test_policy_config, load_test_retrieval_policy


class MockTitleVectorStore(SearchVectorStoreProtocol):
    """Minimal mock for title vector store context manager."""

    def __init__(self, search_results: list[dict[str, str | float]]) -> None:
        self._search_results = cast(list[SearchResult], search_results)

    def __enter__(self) -> "MockTitleVectorStore":
        return self

    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        return None

    def search_all(self, query: str) -> list[SearchResult]:
        del query
        return self._search_results


class MockIndexPath:
    """Mock index path."""

    def __init__(self, exists: bool = True) -> None:
        self._exists = exists

    def exists(self) -> bool:
        return self._exists


def test_query_titles_returns_all_chunks_in_matched_section_subtree() -> None:
    """A matched title should expand to all chunks in descendant sections."""
    from src.commands.query_titles import QueryTitlesCommand, QueryTitlesConfig, QueryTitlesOptions

    search_results = [
        {"doc_uid": "ifrs9", "section_id": "IFRS09_0054", "score": 0.95},
    ]

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="3.0", chunk_id="IFRS09_3.0", containing_section_id="IFRS09_0054", text="chapter text"),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="3.1.1", chunk_id="IFRS09_3.1.1", containing_section_id="IFRS09_g3.1.1-3.1.2", text="initial recognition"),
                Chunk(id=3, doc_uid="ifrs9", chunk_number="3.1.2", chunk_id="IFRS09_3.1.2", containing_section_id="IFRS09_g3.1.1-3.1.2", text="regular way purchase"),
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

    command = QueryTitlesCommand(
        query="initial recognition",
        config=QueryTitlesConfig(
            title_vector_store=MockTitleVectorStore(search_results),
            section_store=section_store,
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryTitlesOptions(policy=load_test_retrieval_policy(), verbose=False),
    )

    result = command.execute()

    data = json.loads(result)
    assert len(data) == 1
    assert data[0]["section_id"] == "IFRS09_0054"
    assert [chunk["id"] for chunk in data[0]["chunks"]] == [1, 2, 3]


def test_query_titles_preserves_chunks_for_overlapping_section_matches() -> None:
    """Overlapping matched sections should each retain their resolved chunks."""
    from src.commands.query_titles import QueryTitlesCommand, QueryTitlesConfig, QueryTitlesOptions

    search_results = [
        {"doc_uid": "ifrs9", "section_id": "IFRS09_0054", "score": 0.95},
        {"doc_uid": "ifrs9", "section_id": "IFRS09_g3.1.1-3.1.2", "score": 0.90},
    ]

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="3.1.1", chunk_id="IFRS09_3.1.1", containing_section_id="IFRS09_g3.1.1-3.1.2", text="initial recognition"),
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
        store.add_descendant_mapping("IFRS09_g3.1.1-3.1.2", ["IFRS09_g3.1.1-3.1.2"])

    command = QueryTitlesCommand(
        query="initial recognition",
        config=QueryTitlesConfig(
            title_vector_store=MockTitleVectorStore(search_results),
            section_store=section_store,
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryTitlesOptions(policy=load_test_retrieval_policy(), verbose=False),
    )

    result = command.execute()

    data = json.loads(result)
    assert len(data) == 2
    assert data[0]["section_id"] == "IFRS09_0054"
    assert [chunk["id"] for chunk in data[0]["chunks"]] == [1]
    assert data[1]["section_id"] == "IFRS09_g3.1.1-3.1.2"
    assert [chunk["id"] for chunk in data[1]["chunks"]] == [1]


def test_query_titles_uses_doc_uid_to_resolve_overlapping_source_section_ids() -> None:
    """Title hits should resolve descendants within the matched document only."""
    from src.commands.query_titles import QueryTitlesCommand, QueryTitlesConfig, QueryTitlesOptions

    search_results = [
        {"doc_uid": "doc-a", "section_id": "shared-section", "score": 0.95},
    ]

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="doc-a", chunk_number="1", chunk_id="DOCA_1", containing_section_id="shared-section", text="doc a root"),
                Chunk(id=2, doc_uid="doc-a", chunk_number="1.1", chunk_id="DOCA_1_1", containing_section_id="child-a", text="doc a child"),
                Chunk(id=3, doc_uid="doc-b", chunk_number="1", chunk_id="DOCB_1", containing_section_id="shared-section", text="doc b root"),
                Chunk(id=4, doc_uid="doc-b", chunk_number="1.1", chunk_id="DOCB_1_1", containing_section_id="child-b", text="doc b child"),
            ]
        )

    section_store = InMemorySectionStore()
    with section_store as store:
        store.insert_sections(
            [
                SectionRecord(
                    section_id="shared-section",
                    doc_uid="doc-a",
                    parent_section_id=None,
                    level=1,
                    title="Shared title A",
                    section_lineage=["Shared title A"],
                    position=1,
                ),
                SectionRecord(
                    section_id="child-a",
                    doc_uid="doc-a",
                    parent_section_id="shared-section",
                    level=2,
                    title="Child A",
                    section_lineage=["Shared title A", "Child A"],
                    position=2,
                ),
                SectionRecord(
                    section_id="shared-section",
                    doc_uid="doc-b",
                    parent_section_id=None,
                    level=1,
                    title="Shared title B",
                    section_lineage=["Shared title B"],
                    position=1,
                ),
                SectionRecord(
                    section_id="child-b",
                    doc_uid="doc-b",
                    parent_section_id="shared-section",
                    level=2,
                    title="Child B",
                    section_lineage=["Shared title B", "Child B"],
                    position=2,
                ),
            ]
        )
        store.add_descendant_mapping("shared-section", ["shared-section", "child-a"], doc_uid="doc-a")
        store.add_descendant_mapping("shared-section", ["shared-section", "child-b"], doc_uid="doc-b")

    command = QueryTitlesCommand(
        query="shared title",
        config=QueryTitlesConfig(
            title_vector_store=MockTitleVectorStore(search_results),
            section_store=section_store,
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryTitlesOptions(policy=load_test_retrieval_policy(), verbose=False),
    )

    result = command.execute()

    data = json.loads(result)
    assert len(data) == 1
    assert data[0]["doc_uid"] == "doc-a"
    assert [chunk["id"] for chunk in data[0]["chunks"]] == [1, 2]


def test_query_titles_verbose_output_starts_with_options() -> None:
    """Verbose title-query output should start with the resolved options."""
    from src.commands.query_titles import QueryTitlesCommand, QueryTitlesConfig, QueryTitlesOptions

    search_results = [
        {"doc_uid": "ifrs9", "section_id": "IFRS09_0054", "score": 0.95},
    ]

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="3.1.1", chunk_id="IFRS09_3.1.1", containing_section_id="IFRS09_0054", text="initial recognition"),
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
            ]
        )
        store.add_descendant_mapping("IFRS09_0054", ["IFRS09_0054"])

    command = QueryTitlesCommand(
        query="recognition",
        config=QueryTitlesConfig(
            title_vector_store=MockTitleVectorStore(search_results),
            section_store=section_store,
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryTitlesOptions(policy=load_test_retrieval_policy(), verbose=True),
    )

    result = command.execute()

    assert result.startswith("QueryTitlesOptions(policy=")
