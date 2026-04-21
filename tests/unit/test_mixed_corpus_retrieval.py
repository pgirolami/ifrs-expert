"""Integration tests for mixed-corpus retrieval with diverse document types and kinds.

These tests validate:
1. Stored rows have both document_type and document_kind (or derive it correctly).
2. Document-stage retrieval applies exact-type limits across a mixed corpus.
3. Exact-type expand_to_section policy is honored in mixed corpus.
4. Prompt A context contains document_type and document_kind metadata.
5. Legacy documents without explicit extractor metadata get a kind via fallback derivation.
"""

from __future__ import annotations

from typing import cast

from src.interfaces import DocumentSearchResult, SearchDocumentVectorStoreProtocol, SearchResult, SearchVectorStoreProtocol
from src.models.chunk import Chunk
from src.models.document import infer_document_kind, infer_exact_document_type, resolve_document_kind_from_document_type, resolve_document_type_from_doc_uid
from tests.fakes import InMemoryChunkStore, InMemoryDocumentStore, InMemorySectionStore
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


class MockInitDb:
    """No-op init_db for testing."""

    def __call__(self) -> None:
        return None


# ---------------------------------------------------------------------------
# Kind-resolver tests (pure unit — no command needed)
# ---------------------------------------------------------------------------


def test_infer_document_kind_maps_all_supported_types() -> None:
    """Every supported exact document_type should map to a known document_kind."""
    type_kind_pairs = [
        ("IFRS-S", "standard"),
        ("IAS-S", "standard"),
        ("PS", "standard"),
        ("IFRIC", "interpretation"),
        ("SIC", "interpretation"),
        ("NAVIS", "interpretation"),
        ("IFRS-IG", "implementation_guidance"),
        ("IFRS-IE", "illustrative_examples"),
        ("IFRS-BC", "basis_for_conclusions"),
        ("IAS-BCIASC", "basis_for_conclusions"),
        ("IAS-SM", "supporting_materials"),
    ]
    for doc_type, expected_kind in type_kind_pairs:
        kind = resolve_document_kind_from_document_type(doc_type)
        assert kind == expected_kind, f"{doc_type} → expected {expected_kind}, got {kind}"


def test_infer_document_kind_returns_none_for_unsupported_type() -> None:
    """Unsupported types should return None (not a default kind)."""
    assert resolve_document_kind_from_document_type("UNKNOWN") is None
    assert resolve_document_kind_from_document_type("BOGUS") is None


def test_infer_exact_document_type_from_doc_uid() -> None:
    """doc_uid patterns should resolve to exact document_type."""
    cases = [
        ("ifrs9", "IFRS-S"),
        ("ifrs15", "IFRS-S"),
        ("ifrs16", "IFRS-S"),
        ("ifrs9-bc", "IFRS-BC"),
        ("ifrs9-ie", "IFRS-IE"),
        ("ifrs9-ig", "IFRS-IG"),
        ("ias21", "IAS-S"),
        ("ias28-bc", "IAS-BC"),
        ("ias28-bciasc", "IAS-BCIASC"),
        ("ifric16", "IFRIC"),
        ("sic25", "SIC"),
        ("ps1", "PS"),
    ]
    for doc_uid, expected_type in cases:
        actual = infer_exact_document_type(doc_uid)
        assert actual == expected_type, f"{doc_uid} → expected {expected_type}, got {actual}"


def test_resolve_document_type_from_doc_uid_supports_ias_variant_labels() -> None:
    """The pure doc_uid resolver should handle IAS supporting-material and IASC BC variants."""
    cases = [
        ("ias28-sm", "IAS-SM"),
        ("ias28-bciasc", "IAS-BCIASC"),
    ]
    for doc_uid, expected_type in cases:
        actual = resolve_document_type_from_doc_uid(doc_uid)
        assert actual == expected_type, f"{doc_uid} → expected {expected_type}, got {actual}"


# ---------------------------------------------------------------------------
# InMemoryDocumentStore — kind persistence via upsert
# ---------------------------------------------------------------------------


def test_document_store_derives_kind_on_upsert() -> None:
    """Upserting a document without explicit document_kind should derive it."""
    store = InMemoryDocumentStore()

    from src.models.document import DocumentRecord

    store.upsert_document(DocumentRecord(doc_uid="ifrs9", source_type="", source_title="", source_url=None, canonical_url=None, captured_at=None))
    doc = store.get_document("ifrs9")
    assert doc is not None
    assert doc.document_type == "IFRS-S"
    assert doc.document_kind == "standard"

    store.upsert_document(DocumentRecord(doc_uid="ifrs9-bc", source_type="", source_title="", source_url=None, canonical_url=None, captured_at=None))
    doc = store.get_document("ifrs9-bc")
    assert doc is not None
    assert doc.document_type == "IFRS-BC"
    assert doc.document_kind == "basis_for_conclusions"

    store.upsert_document(DocumentRecord(doc_uid="ifric16", source_type="", source_title="", source_url=None, canonical_url=None, captured_at=None))
    doc = store.get_document("ifric16")
    assert doc is not None
    assert doc.document_type == "IFRIC"
    assert doc.document_kind == "interpretation"


def test_document_store_preserves_explicit_kind_on_upsert() -> None:
    """Upserting with an explicit document_kind should preserve it (not overwrite)."""
    store = InMemoryDocumentStore()

    from src.models.document import DocumentRecord

    store.upsert_document(
        DocumentRecord(doc_uid="my-custom-doc", source_type="", source_title="", source_url=None, canonical_url=None, captured_at=None, document_type="IFRIC", document_kind="interpretation"),
    )
    doc = store.get_document("my-custom-doc")
    assert doc is not None
    assert doc.document_kind == "interpretation"


# ---------------------------------------------------------------------------
# Mixed-corpus document-stage retrieval
# ---------------------------------------------------------------------------


def test_mixed_corpus_applies_per_type_limits() -> None:
    """Mixed corpus (IFRS-S, IFRS-BC, IFRS-IE, IFRS-IG, IAS, IFRIC, SIC) respects per-type caps."""
    import json

    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="1", page_start="A1", page_end="A1", text="ifrs9 standard"),
                Chunk(id=2, doc_uid="ifrs9-bc", chunk_number="1", page_start="B1", page_end="B1", text="ifrs9 bc"),
                Chunk(id=3, doc_uid="ifrs9-ie", chunk_number="1", page_start="C1", page_end="C1", text="ifrs9 ie"),
                Chunk(id=4, doc_uid="ifrs9-ig", chunk_number="1", page_start="D1", page_end="D1", text="ifrs9 ig"),
                Chunk(id=5, doc_uid="ias21", chunk_number="1", page_start="E1", page_end="E1", text="ias21"),
                Chunk(id=6, doc_uid="ifric16", chunk_number="1", page_start="F1", page_end="F1", text="ifric16"),
                Chunk(id=7, doc_uid="sic25", chunk_number="1", page_start="G1", page_end="G1", text="sic25"),
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
                    {"doc_uid": "ias21", "chunk_id": 5, "score": 0.93},
                    {"doc_uid": "ifric16", "chunk_id": 6, "score": 0.92},
                    {"doc_uid": "sic25", "chunk_id": 7, "score": 0.91},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=MockInitDb(),
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifrs9", "score": 0.80},
                    {"doc_uid": "ifrs9-bc", "score": 0.78},
                    {"doc_uid": "ifrs9-ie", "score": 0.76},
                    {"doc_uid": "ifrs9-ig", "score": 0.74},
                    {"doc_uid": "ias21", "score": 0.72},
                    {"doc_uid": "ifric16", "score": 0.70},
                    {"doc_uid": "sic25", "score": 0.68},
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
                per_type_d={"IFRS-S": 1, "IFRS-BC": 1, "IFRS-IE": 1, "IFRS-IG": 1, "IAS-S": 1, "IFRIC": 1, "SIC": 1},
                per_type_min_score={"IFRS-S": 0.5, "IFRS-BC": 0.5, "IFRS-IE": 0.5, "IFRS-IG": 0.5, "IAS-S": 0.5, "IFRIC": 0.5, "SIC": 0.5},
            ),
            verbose=False,
        ),
    )

    result = command.execute()
    data = json.loads(result)

    hits = data["document_hits"]
    doc_uids = [h["doc_uid"] for h in hits]
    # Each exact type with d=1 should appear at most once
    assert "ifrs9" in doc_uids
    assert "ifrs9-bc" in doc_uids
    assert "ifrs9-ie" in doc_uids
    assert "ifrs9-ig" in doc_uids
    assert "ias21" in doc_uids
    assert "ifric16" in doc_uids
    assert "sic25" in doc_uids
    assert len(hits) == 7


def test_mixed_corpus_global_d_truncates_total() -> None:
    """Global d=3 should truncate to 3 even when per-type caps allow more."""
    import json

    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="1", page_start="A1", page_end="A1", text="ifrs9"),
                Chunk(id=2, doc_uid="ifrs9-bc", chunk_number="1", page_start="B1", page_end="B1", text="ifrs9-bc"),
                Chunk(id=3, doc_uid="ifrs9-ie", chunk_number="1", page_start="C1", page_end="C1", text="ifrs9-ie"),
                Chunk(id=4, doc_uid="ias21", chunk_number="1", page_start="D1", page_end="D1", text="ias21"),
                Chunk(id=5, doc_uid="ifric16", chunk_number="1", page_start="E1", page_end="E1", text="ifric16"),
            ]
        )

    command = RetrieveCommand(
        query="test",
        config=RetrieveConfig(
            vector_store=MockVectorStore(
                [
                    {"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.97},
                    {"doc_uid": "ifrs9-bc", "chunk_id": 2, "score": 0.96},
                    {"doc_uid": "ifrs9-ie", "chunk_id": 3, "score": 0.95},
                    {"doc_uid": "ias21", "chunk_id": 4, "score": 0.94},
                    {"doc_uid": "ifric16", "chunk_id": 5, "score": 0.93},
                ]
            ),
            chunk_store=chunk_store,
            init_db_fn=MockInitDb(),
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifrs9", "score": 0.80},
                    {"doc_uid": "ifrs9-bc", "score": 0.78},
                    {"doc_uid": "ifrs9-ie", "score": 0.76},
                    {"doc_uid": "ias21", "score": 0.74},
                    {"doc_uid": "ifric16", "score": 0.72},
                ]
            ),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            policy=make_retrieval_policy(
                k=5,
                d=3,  # global cap
                chunk_min_score=0.5,
                expand=0,
                mode="documents",
                per_type_d={"IFRS-S": 5, "IFRS-BC": 5, "IFRS-IE": 5, "IAS-S": 5, "IFRIC": 5},
                per_type_min_score={"IFRS-S": 0.5, "IFRS-BC": 0.5, "IFRS-IE": 0.5, "IAS-S": 0.5, "IFRIC": 0.5},
            ),
            verbose=False,
        ),
    )

    result = command.execute()
    data = json.loads(result)
    assert len(data["document_hits"]) == 3, f"Expected global d=3 to truncate, got {data['document_hits']}"


def test_document_hits_include_document_kind() -> None:
    """Each document_hit should include document_kind for authority surfacing."""
    import json

    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9", chunk_number="1", page_start="A1", page_end="A1", text="standard"),
                Chunk(id=2, doc_uid="ifrs9-bc", chunk_number="1", page_start="B1", page_end="B1", text="bc"),
            ]
        )

    command = RetrieveCommand(
        query="test",
        config=RetrieveConfig(
            vector_store=MockVectorStore([{"doc_uid": "ifrs9", "chunk_id": 1, "score": 0.9}, {"doc_uid": "ifrs9-bc", "chunk_id": 2, "score": 0.9}]),
            chunk_store=chunk_store,
            init_db_fn=MockInitDb(),
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore([{"doc_uid": "ifrs9", "score": 0.8}, {"doc_uid": "ifrs9-bc", "score": 0.8}]),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            policy=make_retrieval_policy(k=5, d=10, chunk_min_score=0.5, expand=0, mode="documents"),
            verbose=False,
        ),
    )

    result = command.execute()
    data = json.loads(result)

    hits_by_uid = {h["doc_uid"]: h for h in data["document_hits"]}
    assert hits_by_uid["ifrs9"]["document_kind"] == "standard", "IFRS-S → standard"
    assert hits_by_uid["ifrs9-bc"]["document_kind"] == "basis_for_conclusions", "IFRS-BC → basis_for_conclusions"


# ---------------------------------------------------------------------------
# Prompt context — XML attributes present
# ---------------------------------------------------------------------------


def test_retrieve_command_context_xml_includes_type_and_kind() -> None:
    """Retrieve command JSON output should include document_type and document_kind on each chunk."""
    import json

    from src.commands.retrieve import RetrieveCommand, RetrieveConfig, RetrieveOptions

    chunk_store = InMemoryChunkStore()
    with chunk_store as store:
        store.insert_chunks(
            [
                Chunk(id=1, doc_uid="ifrs9-ig", chunk_number="1", page_start="A1", page_end="A1", text="ig chunk"),
                Chunk(id=2, doc_uid="ifric16", chunk_number="1", page_start="B1", page_end="B1", text="ifric chunk"),
            ]
        )

    command = RetrieveCommand(
        query="test",
        config=RetrieveConfig(
            vector_store=MockVectorStore([{"doc_uid": "ifrs9-ig", "chunk_id": 1, "score": 0.9}, {"doc_uid": "ifric16", "chunk_id": 2, "score": 0.9}]),
            chunk_store=chunk_store,
            init_db_fn=MockInitDb(),
            index_path_fn=lambda: MockIndexPath(exists=True),
            section_store=InMemorySectionStore(),
            document_vector_store=MockDocumentVectorStore([{"doc_uid": "ifrs9-ig", "score": 0.8}, {"doc_uid": "ifric16", "score": 0.8}]),
            document_index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=RetrieveOptions(
            policy=make_retrieval_policy(k=5, d=10, chunk_min_score=0.5, expand=0, mode="documents"),
            verbose=False,
        ),
    )

    result = command.execute()
    data = json.loads(result)

    chunks_by_uid = {c["doc_uid"]: c for c in data["chunks"]}
    assert chunks_by_uid["ifrs9-ig"]["document_type"] == "IFRS-IG"
    assert chunks_by_uid["ifrs9-ig"]["document_kind"] == "implementation_guidance"
    assert chunks_by_uid["ifric16"]["document_type"] == "IFRIC"
    assert chunks_by_uid["ifric16"]["document_kind"] == "interpretation"
