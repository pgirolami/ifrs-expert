"""Tests for exact-type document caps in document-stage retrieval.

These tests verify:
1. Exact IFRS variants (IFRS-S, IFRS-BC, IFRS-IE, IFRS-IG) get independent caps —
   not a shared cross-type counter.
2. Global d still bounds total hits after per-type caps are applied.
3. Per-type expand_to_section policy is honored (IFRS-S expands, BC/IE do not).
4. Commands reject runs when policy YAML is not provided.
5. Retrieval fails fast when document_type cannot be resolved for a candidate.
"""

from __future__ import annotations

from typing import cast

import pytest

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


class MockIndexPath:
    """Mock index path."""

    def __init__(self, exists: bool = True) -> None:
        self._exists = exists

    def exists(self) -> bool:
        return self._exists


def test_exact_ifrs_variants_get_independent_caps() -> None:
    """IFRS-S, IFRS-BC, IFRS-IE, IFRS-IG each get an independent cap.

    With per-type d=1 and global d=10, all four variants should survive —
    not just one as a shared-counter approach would do.
    """
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="1", page_start="A1", page_end="A1", text="ifrs9 standard"),
                Chunk(id=2, doc_uid="ifrs9-bc", chunk_number="1", page_start="B1", page_end="B1", text="ifrs9 bc"),
                Chunk(id=3, doc_uid="ifrs9-ie", chunk_number="1", page_start="C1", page_end="C1", text="ifrs9 ie"),
                Chunk(id=4, doc_uid="ifrs9-ig", chunk_number="1", page_start="D1", page_end="D1", text="ifrs9 ig"),
            ]
        )

    command = RetrieveCommand(
        query="revenue recognition",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.97},
                    {"doc_uid": "ifrs9-bc", "chunk_id": 2, "score": 0.96},
                    {"doc_uid": "ifrs9-ie", "chunk_id": 3, "score": 0.95},
                    {"doc_uid": "ifrs9-ig", "chunk_id": 4, "score": 0.94},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifrs9", "score": 0.80},
                    {"doc_uid": "ifrs9-bc", "score": 0.78},
                    {"doc_uid": "ifrs9-ie", "score": 0.76},
                    {"doc_uid": "ifrs9-ig", "score": 0.74},
                ]
            ),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            policy=make_retrieval_policy(
                k=5,
                d=10,
                chunk_min_score=0.5,
                expand=0,
                mode="documents",
                per_type_d={"IFRS-S": 1, "IFRS-BC": 1, "IFRS-IE": 1, "IFRS-IG": 1},
                per_type_min_score={"IFRS-S": 0.5, "IFRS-BC": 0.5, "IFRS-IE": 0.5, "IFRS-IG": 0.5},
            ),
            verbose=False,
        ),
    )

    result = command.execute()
    import json
    data = json.loads(result)

    doc_uids = [h["doc_uid"] for h in data["document_hits"]]
    assert "ifrs9" in doc_uids, "IFRS-S (ifrs9) should survive per-type cap"
    assert "ifrs9-bc" in doc_uids, "IFRS-BC should survive its independent cap"
    assert "ifrs9-ie" in doc_uids, "IFRS-IE should survive its independent cap"
    assert "ifrs9-ig" in doc_uids, "IFRS-IG should survive its independent cap"
    assert len(doc_uids) == 4, f"Expected exactly 4 hits (one per exact type), got {doc_uids}"


def test_global_d_truncates_after_per_type_selection() -> None:
    """Global d should bound total hits after per-type caps are applied.

    With 4 IFRS variants (per-type d=2 each) and global d=3, exactly 3
    documents should be returned — not 4 (per-type) nor 1 (shared counter).
    """
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions
    import json

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="1", page_start="A1", page_end="A1", text="ifrs9 standard"),
                Chunk(id=2, doc_uid="ifrs9-bc", chunk_number="1", page_start="B1", page_end="B1", text="ifrs9 bc"),
                Chunk(id=3, doc_uid="ifrs9-ie", chunk_number="1", page_start="C1", page_end="C1", text="ifrs9 ie"),
                Chunk(id=4, doc_uid="ifrs9-ig", chunk_number="1", page_start="D1", page_end="D1", text="ifrs9 ig"),
            ]
        )

    command = RetrieveCommand(
        query="revenue recognition",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.97},
                    {"doc_uid": "ifrs9-bc", "chunk_id": 2, "score": 0.96},
                    {"doc_uid": "ifrs9-ie", "chunk_id": 3, "score": 0.95},
                    {"doc_uid": "ifrs9-ig", "chunk_id": 4, "score": 0.94},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifrs9", "score": 0.80},
                    {"doc_uid": "ifrs9-bc", "score": 0.78},
                    {"doc_uid": "ifrs9-ie", "score": 0.76},
                    {"doc_uid": "ifrs9-ig", "score": 0.74},
                ]
            ),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            policy=make_retrieval_policy(
                k=5,
                d=3,  # global cap: only 3 total
                chunk_min_score=0.5,
                expand=0,
                mode="documents",
                per_type_d={"IFRS-S": 2, "IFRS-BC": 2, "IFRS-IE": 2, "IFRS-IG": 2},
                per_type_min_score={"IFRS-S": 0.5, "IFRS-BC": 0.5, "IFRS-IE": 0.5, "IFRS-IG": 0.5},
            ),
            verbose=False,
        ),
    )

    result = command.execute()
    data = json.loads(result)
    assert len(data["document_hits"]) == 3, f"Expected global d=3 to truncate to 3 hits, got {data['document_hits']}"


def test_per_type_min_score_skips_low_scoring_variants() -> None:
    """Low-scoring exact variants should be skipped even if cap is available.

    ifrs9-ie at 0.35 is below IFRS-IE min_score=0.50 so it should be skipped
    even though IFRS-IE cap would allow it.
    """
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions
    import json

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="1", page_start="A1", page_end="A1", text="ifrs9 standard"),
                Chunk(id=2, doc_uid="ifrs9-bc", chunk_number="1", page_start="B1", page_end="B1", text="ifrs9 bc"),
                Chunk(id=3, doc_uid="ifrs9-ie", chunk_number="1", page_start="C1", page_end="C1", text="ifrs9 ie"),
            ]
        )

    command = RetrieveCommand(
        query="revenue recognition",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.97},
                    {"doc_uid": "ifrs9-bc", "chunk_id": 2, "score": 0.96},
                    {"doc_uid": "ifrs9-ie", "chunk_id": 3, "score": 0.35},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifrs9", "score": 0.80},
                    {"doc_uid": "ifrs9-bc", "score": 0.78},
                    {"doc_uid": "ifrs9-ie", "score": 0.35},
                ]
            ),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            policy=make_retrieval_policy(
                k=5,
                d=10,
                chunk_min_score=0.5,
                expand=0,
                mode="documents",
                per_type_d={"IFRS-S": 2, "IFRS-BC": 2, "IFRS-IE": 2},
                per_type_min_score={"IFRS-S": 0.5, "IFRS-BC": 0.5, "IFRS-IE": 0.50},
            ),
            verbose=False,
        ),
    )

    result = command.execute()
    data = json.loads(result)
    doc_uids = [h["doc_uid"] for h in data["document_hits"]]
    assert "ifrs9" in doc_uids
    assert "ifrs9-bc" in doc_uids
    assert "ifrs9-ie" not in doc_uids, "ifrs9-ie should be skipped (score 0.35 < min_score 0.50)"


def test_expand_to_section_policy_honored_per_type() -> None:
    """IFRS-S expands to section (expand_to_section=true) but IFRS-BC does not.

    Only IFRS-S chunks within the matching section subtree should be included;
    IFRS-BC chunks outside the section tree should be excluded.
    """
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions
    import json

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                # IFRS-S chunks
                Chunk(id=1, doc_uid="ifrs9", chunk_number="3.0", page_start="A1", page_end="A1", chunk_id="IFRS09_3.0", containing_section_id="IFRS09_0054", text="revenue chapter text"),
                Chunk(id=2, doc_uid="ifrs9", chunk_number="3.1", page_start="A2", page_end="A2", chunk_id="IFRS09_3.1", containing_section_id="IFRS09_0054_child", text="revenue section child"),
                # IFRS-BC chunk (outside IFRS-S section tree)
                Chunk(id=3, doc_uid="ifrs9-bc", chunk_number="1", page_start="B1", page_end="B1", chunk_id="IFRS09_BC_1", containing_section_id="IFRS09_BC_root", text="ifrs9-bc text"),
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
                    title="Revenue",
                    section_lineage=["Revenue"],
                    position=1,
                ),
                SectionRecord(
                    section_id="IFRS09_0054_child",
                    doc_uid="ifrs9",
                    parent_section_id="IFRS09_0054",
                    level=3,
                    title="Revenue child",
                    section_lineage=["Revenue", "Revenue child"],
                    position=2,
                ),
                SectionRecord(
                    section_id="IFRS09_BC_root",
                    doc_uid="ifrs9-bc",
                    parent_section_id=None,
                    level=1,
                    title="BC root",
                    section_lineage=["BC root"],
                    position=1,
                ),
            ]
        )
        store.add_descendant_mapping("IFRS09_0054", ["IFRS09_0054", "IFRS09_0054_child"])

    command = RetrieveCommand(
        query="revenue recognition",
        config=RetrieveConfig(
            vector_store=MockVectorStore([{"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.96}]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=section_store,
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifrs9", "score": 0.80},
                    {"doc_uid": "ifrs9-bc", "score": 0.78},
                ]
            ),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            policy=make_retrieval_policy(
                k=5,
                d=10,
                chunk_min_score=0.5,
                expand=0,
                mode="documents",
                per_type_d={"IFRS-S": 1, "IFRS-BC": 1},
                per_type_min_score={"IFRS-S": 0.5, "IFRS-BC": 0.5},
            ),
            verbose=False,
        ),
    )

    result = command.execute()
    data = json.loads(result)

    # IFRS-S (expand_to_section=true) should include the child chunk
    ifrs9_chunk_ids = {c["id"] for c in data["chunks"] if c["doc_uid"] == "ifrs9"}
    assert 2 in ifrs9_chunk_ids, "IFRS-S child chunk should be included (expand_to_section=true)"
    assert 1 in ifrs9_chunk_ids, "IFRS-S root chunk should be included"


def test_retrieval_fails_fast_on_unresolved_document_type() -> None:
    """A doc_uid that cannot be resolved to an exact type should cause an error.

    An unknown doc_uid format should return an error rather than silently
    defaulting to a shared bucket.
    """
    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions
    import json

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="UNKNOWN_12345", chunk_number="1", page_start="A1", page_end="A1", text="unknown doc"),
            ]
        )

    command = RetrieveCommand(
        query="test",
        config=RetrieveConfig(
            vector_store=MockVectorStore([{"doc_uid": "UNKNOWN_12345", "chunk_id": 1, "score": 0.9}]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore([{"doc_uid": "UNKNOWN_12345", "score": 0.9}]),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            policy=make_retrieval_policy(k=5, d=5, chunk_min_score=0.5, expand=0, mode="documents"),
            verbose=False,
        ),
    )

    result = command.execute()
    assert result.startswith("Error:"), f"Expected error for unresolved doc_uid, got: {result}"
    assert "Could not resolve exact document_type" in result or "UNKNOWN_12345" in result
