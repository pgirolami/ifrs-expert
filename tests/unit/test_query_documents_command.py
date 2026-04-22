"""Tests for query-documents command."""

from __future__ import annotations

import json
from typing import cast

from src.interfaces import DocumentSearchResult, SearchDocumentVectorStoreProtocol
from src.models.document import DocumentRecord
from tests.fakes import InMemoryDocumentStore
from tests.policy import load_test_retrieval_policy, make_retrieval_policy


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


def test_query_documents_returns_top_d_documents_for_selected_type_as_json() -> None:
    """The command should return the top matching documents for the selected document type."""
    from src.commands.query_documents import QueryDocumentsCommand, QueryDocumentsConfig, QueryDocumentsOptions

    document_store = InMemoryDocumentStore()
    with document_store as store:
        store.upsert_document(
            DocumentRecord(
                doc_uid="ifric16",
                source_type="html",
                source_title="IFRIC 16",
                source_url="https://www.ifrs.org/ifric16.html",
                canonical_url="https://www.ifrs.org/ifric16.html",
                captured_at="2026-04-05T10:00:00Z",
                document_type="IFRIC",
                background_text="Background text",
                issue_text="Issue text",
                scope_text="Scope text",
                toc_text="Background\nIssue\nScope",
            )
        )
        store.upsert_document(
            DocumentRecord(
                doc_uid="ifric17",
                source_type="html",
                source_title="IFRIC 17",
                source_url="https://www.ifrs.org/ifric17.html",
                canonical_url="https://www.ifrs.org/ifric17.html",
                captured_at="2026-04-05T10:00:00Z",
                document_type="IFRIC",
                objective_text="Objective text",
                scope_text="Scope text",
            )
        )
        store.upsert_document(
            DocumentRecord(
                doc_uid="ifrs9",
                source_type="html",
                source_title="IFRS 9",
                source_url="https://www.ifrs.org/ifrs9.html",
                canonical_url="https://www.ifrs.org/ifrs9.html",
                captured_at="2026-04-05T10:00:00Z",
                document_type="IFRS-S",
                intro_text="IFRS intro",
            )
        )
        store.upsert_document(
            DocumentRecord(
                doc_uid="ias21",
                source_type="html",
                source_title="IAS 21",
                source_url="https://www.ifrs.org/ias21.html",
                canonical_url="https://www.ifrs.org/ias21.html",
                captured_at="2026-04-05T10:00:00Z",
                document_type="IAS-S",
                intro_text="IAS intro",
            )
        )
        store.upsert_document(
            DocumentRecord(
                doc_uid="sic25",
                source_type="html",
                source_title="SIC 25",
                source_url="https://www.ifrs.org/sic25.html",
                canonical_url="https://www.ifrs.org/sic25.html",
                captured_at="2026-04-05T10:00:00Z",
                document_type="SIC",
                intro_text="SIC intro",
            )
        )
        store.upsert_document(
            DocumentRecord(
                doc_uid="ps1",
                source_type="html",
                source_title="PS 1",
                source_url="https://www.ifrs.org/ps1.html",
                canonical_url="https://www.ifrs.org/ps1.html",
                captured_at="2026-04-05T10:00:00Z",
                document_type="PS",
                intro_text="PS intro",
            )
        )

    command = QueryDocumentsCommand(
        query="hedges of a net investment",
        config=QueryDocumentsConfig(
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifric16", "score": 0.97},
                    {"doc_uid": "ifrs9", "score": 0.96},
                    {"doc_uid": "ifric17", "score": 0.95},
                    {"doc_uid": "ias21", "score": 0.94},
                    {"doc_uid": "sic25", "score": 0.93},
                    {"doc_uid": "ps1", "score": 0.92},
                ]
            ),
            document_store=document_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryDocumentsOptions(
            policy=make_retrieval_policy(per_type_d={"IFRIC": 2}),
            document_type="IFRIC",
            verbose=False,
        ),
    )

    result = command.execute()

    data = json.loads(result)
    assert [item["doc_uid"] for item in data] == ["ifric16", "ifric17"]
    assert data[0]["document_type"] == "IFRIC"
    assert data[0]["background_text"] == "Background text"
    assert data[0]["issue_text"] == "Issue text"
    assert data[0]["TOC"] == "Background\nIssue\nScope"
    assert data[0]["score"] == 0.97


def test_query_documents_returns_error_for_unsupported_document_type() -> None:
    """The command should reject document types outside the supported set."""
    from src.commands.query_documents import QueryDocumentsCommand, QueryDocumentsConfig, QueryDocumentsOptions

    command = QueryDocumentsCommand(
        query="scope",
        config=QueryDocumentsConfig(
            document_vector_store=MockDocumentVectorStore([]),
            document_store=InMemoryDocumentStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryDocumentsOptions(policy=load_test_retrieval_policy(), document_type="CUSTOM", verbose=False),
    )

    result = command.execute()

    assert result == (
        "Error: document_type must be one of IFRS-S, IFRS-BC, IFRS-IE, IFRS-IG, "
        "IAS-S, IAS-BC, IAS-BCIASC, IAS-IE, IAS-IG, IAS-SM, IFRIC, IFRIC-BC, IFRIC-IE, IFRIC-IG, "
        "SIC, SIC-BC, SIC-IE, PS, PS-BC, NAVIS"
    )


def test_query_documents_returns_error_when_index_missing() -> None:
    """The command should fail clearly when the document index is missing."""
    from src.commands.query_documents import QueryDocumentsCommand, QueryDocumentsConfig, QueryDocumentsOptions

    command = QueryDocumentsCommand(
        query="scope",
        config=QueryDocumentsConfig(
            document_vector_store=MockDocumentVectorStore([]),
            document_store=InMemoryDocumentStore(),
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=False),
        ),
        options=QueryDocumentsOptions(policy=load_test_retrieval_policy(), document_type="IFRS-S", verbose=False),
    )

    result = command.execute()

    assert result == "Error: No document index found. Please run 'store' command first."


def test_query_documents_returns_ifrs_variant_documents() -> None:
    """The command should support exact IFRS variant document types."""
    from src.commands.query_documents import QueryDocumentsCommand, QueryDocumentsConfig, QueryDocumentsOptions

    document_store = InMemoryDocumentStore()
    with document_store as store:
        store.upsert_document(
            DocumentRecord(
                doc_uid="ifrs9",
                source_type="html",
                source_title="IFRS - IFRS 9 Financial Instruments",
                source_url="https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9/",
                canonical_url="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9.html",
                captured_at="2026-04-14T09:45:54Z",
                source_domain="www.ifrs.org",
                document_type="IFRS-S",
                intro_text="IFRS standard introduction",
            )
        )
        store.upsert_document(
            DocumentRecord(
                doc_uid="ifrs9-bc",
                source_type="html",
                source_title="IFRS - IFRS 9 Financial Instruments - Basis for Conclusions",
                source_url="https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9-bc/",
                canonical_url="https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/ifrs-9-financial-instruments.html/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs9-bc.html",
                captured_at="2026-04-14T09:46:15Z",
                source_domain="www.ifrs.org",
                document_type="IFRS-BC",
                intro_text="Basis introduction",
            )
        )

    command = QueryDocumentsCommand(
        query="financial instruments",
        config=QueryDocumentsConfig(
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "ifrs9-bc", "score": 0.92},
                    {"doc_uid": "ifrs9", "score": 0.91},
                ]
            ),
            document_store=document_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryDocumentsOptions(policy=make_retrieval_policy(per_type_d={"IFRS-BC": 2}), document_type="IFRS-BC", verbose=False),
    )

    result = command.execute()

    data = json.loads(result)
    assert [item["doc_uid"] for item in data] == ["ifrs9-bc"]
    assert data[0]["document_type"] == "IFRS-BC"


def test_query_documents_returns_navis_documents() -> None:
    """The command should include NAVIS as a supported document family."""
    from src.commands.query_documents import QueryDocumentsCommand, QueryDocumentsConfig, QueryDocumentsOptions

    document_store = InMemoryDocumentStore()
    with document_store as store:
        store.upsert_document(
            DocumentRecord(
                doc_uid="navis-QRIFRS-C2A8E6F292F99E-EFL",
                source_type="html",
                source_title="Mémento IFRS 2026",
                source_url="https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&refId=C2A8E6F292F99E-EFL",
                canonical_url="https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&refId=C2A8E6F292F99E-EFL",
                captured_at="2026-04-12T19:00:29Z",
                source_domain="abonnes.efl.fr",
                document_type="NAVIS",
                intro_text="Cadre conceptuel de l'information financière",
            )
        )

    command = QueryDocumentsCommand(
        query="cadre conceptuel",
        config=QueryDocumentsConfig(
            document_vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid": "navis-QRIFRS-C2A8E6F292F99E-EFL", "score": 0.91},
                ]
            ),
            document_store=document_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryDocumentsOptions(policy=make_retrieval_policy(per_type_d={"NAVIS": 2}), document_type="NAVIS", verbose=False),
    )

    result = command.execute()

    data = json.loads(result)
    assert [item["doc_uid"] for item in data] == ["navis-QRIFRS-C2A8E6F292F99E-EFL"]
    assert data[0]["document_type"] == "NAVIS"


def test_query_documents_verbose_output_starts_with_options() -> None:
    """Verbose document-query output should start with options and truncated representation details."""
    from src.commands.query_documents import (
        QueryDocumentsCommand,
        QueryDocumentsConfig,
        QueryDocumentsOptions,
        VERBOSE_TEXT_PREVIEW_CHARS,
    )

    long_background_text = "B" * (VERBOSE_TEXT_PREVIEW_CHARS + 10)
    long_scope_text = "S" * (VERBOSE_TEXT_PREVIEW_CHARS + 15)

    document_store = InMemoryDocumentStore()
    with document_store as store:
        store.upsert_document(
            DocumentRecord(
                doc_uid="ifric16",
                source_type="html",
                source_title="IFRIC 16",
                source_url="https://www.ifrs.org/ifric16.html",
                canonical_url="https://www.ifrs.org/ifric16.html",
                captured_at="2026-04-05T10:00:00Z",
                document_type="IFRIC",
                background_text=long_background_text,
                scope_text=long_scope_text,
                toc_text="Background\nIssue\nScope",
            )
        )

    command = QueryDocumentsCommand(
        query="hedges of a net investment",
        config=QueryDocumentsConfig(
            document_vector_store=MockDocumentVectorStore([{"doc_uid": "ifric16", "score": 0.97}]),
            document_store=document_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
        ),
        options=QueryDocumentsOptions(policy=load_test_retrieval_policy(), document_type="IFRIC", verbose=True),
    )

    result = command.execute()

    expected_background_preview = ("B" * VERBOSE_TEXT_PREVIEW_CHARS) + "..."
    expected_scope_preview = ("S" * VERBOSE_TEXT_PREVIEW_CHARS) + "..."

    assert result.startswith("QueryDocumentsOptions(policy=")
    assert f"Snippet: {expected_background_preview}" in result
    assert "Type: IFRIC" in result
    assert "Document representation:" in result
    assert f"- Background: {expected_background_preview}" in result
    assert f"- Scope: {expected_scope_preview}" in result
    assert "- TOC: Background Issue Scope" in result


def test_query_documents_uses_policy_similarity_representation_for_index_and_store() -> None:
    """Query-documents should route to the index/store selected by per-type similarity representation."""
    from src.commands.query_documents import QueryDocumentsCommand, QueryDocumentsConfig, QueryDocumentsOptions

    captured_representations: list[str] = []

    def _index_path_fn(representation: str) -> MockIndexPath:
        captured_representations.append(f"index:{representation}")
        return MockIndexPath(exists=True)

    def _vector_store_factory(representation: str) -> MockDocumentVectorStore:
        captured_representations.append(f"store:{representation}")
        return MockDocumentVectorStore([{"doc_uid": "ifric16", "score": 0.97}])

    document_store = InMemoryDocumentStore()
    with document_store as store:
        store.upsert_document(
            DocumentRecord(
                doc_uid="ifric16",
                source_type="html",
                source_title="IFRIC 16",
                source_url="https://www.ifrs.org/ifric16.html",
                canonical_url="https://www.ifrs.org/ifric16.html",
                captured_at="2026-04-05T10:00:00Z",
                document_type="IFRIC",
                scope_text="Scope text",
            )
        )

    command = QueryDocumentsCommand(
        query="hedges of a net investment",
        config=QueryDocumentsConfig(
            document_vector_store_factory=_vector_store_factory,
            document_store=document_store,
            init_db_fn=lambda: None,
            index_path_fn=_index_path_fn,
        ),
        options=QueryDocumentsOptions(
            policy=_build_policy_with_similarity_representation_overrides({"IFRIC": "scope"}),
            document_type="IFRIC",
            verbose=False,
        ),
    )

    result = command.execute()

    assert json.loads(result)[0]["doc_uid"] == "ifric16"
    assert captured_representations == ["index:scope", "store:scope"]


def _build_policy_with_similarity_representation_overrides(
    overrides: dict[str, str],
):
    from src.policy import DocumentStageRetrievalPolicy, DocumentTypeRetrievalPolicy, RetrievalPolicy

    base_policy = make_retrieval_policy()
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
        query_embedding_mode=base_policy.query_embedding_mode,
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


