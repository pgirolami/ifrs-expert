"""Tests for the generalized store command."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

import pytest

from src.commands.store import StoreCommand, StoreDependencies
from src.vector.constants import MAX_EMBEDDING_TEXT_CHARS
from src.models.chunk import Chunk
from src.models.document import DocumentRecord
from src.models.extraction import ExtractedDocument
from src.models.reference import ContentReference
from src.models.section import SectionClosureRow, SectionRecord
from tests.fakes import (
    InMemoryChunkStore,
    InMemoryDocumentStore,
    InMemoryReferenceStore,
    InMemorySectionStore,
    RecordingDocumentVectorStore,
    RecordingTitleVectorStore,
    RecordingVectorStore,
)


@dataclass
class FakeExtractor:
    """Test extractor returning a prepared extraction result."""

    extracted_document: ExtractedDocument
    skip_if_unchanged: bool = False

    def extract(self, source_path: Path, explicit_doc_uid: str | None) -> ExtractedDocument:
        del source_path
        if explicit_doc_uid is not None:
            self.extracted_document.document.doc_uid = explicit_doc_uid
            for chunk in self.extracted_document.chunks:
                chunk.doc_uid = explicit_doc_uid
        return self.extracted_document


@dataclass
class FakeBuggyExtractor:
    """Test extractor simulating an unexpected programmer error."""

    skip_if_unchanged: bool = False

    def extract(self, source_path: Path, explicit_doc_uid: str | None) -> ExtractedDocument:
        del source_path, explicit_doc_uid
        raise NameError("simulated programmer bug")


class TestStoreCommand:
    """Tests for store command using dependency injection."""

    def test_store_command_success(self, tmp_path: Path) -> None:
        """Store command should persist document metadata, chunks, and embeddings."""
        source_path = tmp_path / "test.pdf"
        source_path.write_text("dummy", encoding="utf-8")

        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid="ifrs9",
                    source_type="pdf",
                    source_title="IFRS 9",
                    source_url=None,
                    canonical_url=None,
                    captured_at=None,
                ),
                chunks=[
                    Chunk(
                        doc_uid="ifrs9",
                        chunk_number="1.1",
                        page_start="A1",
                        page_end="A1",
                        text="test content",
                    )
                ],
            )
        )
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        vector_store = RecordingVectorStore()
        document_vector_store = RecordingDocumentVectorStore()
        dependencies = StoreDependencies(
            chunk_store=chunk_store,
            document_store=document_store,
            vector_store=vector_store,
            document_vector_store=document_vector_store,
            init_db_fn=lambda: None,
        )
        command = StoreCommand(
            source_path=source_path,
            extractor=extractor,
            dependencies=dependencies,
            explicit_doc_uid=None,
        )

        result = command.execute_result()

        assert result.status == "stored"
        assert result.doc_uid == "ifrs9"
        assert result.chunk_count == 1
        stored_document = document_store.get_document("ifrs9")
        assert stored_document is not None, "Expected document metadata to be stored"
        assert stored_document.source_type == "pdf"
        assert stored_document.document_type == "IFRS-S"
        assert stored_document.intro_text == "test content"
        assert chunk_store.get_chunks_by_doc("ifrs9")[0].text == "test content"
        assert vector_store.added_embeddings == [("ifrs9", [1], ["test content"])]
        assert document_vector_store.added_embeddings == [(["ifrs9"], ["Title: IFRS 9\nIntroduction: test content"])]
        assert command.execute().startswith("Stored 1 chunks")

    def test_store_command_persists_references(self, tmp_path: Path) -> None:
        """Store command should persist parsed references alongside chunks and sections."""
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")

        section = SectionRecord(
            section_id="IFRS09_0054",
            doc_uid="ifrs9",
            parent_section_id=None,
            level=1,
            title="Recognition and derecognition",
            section_lineage=["Recognition and derecognition"],
            position=1,
        )
        chunk = Chunk(
            doc_uid="ifrs9",
            chunk_number="4.1.1",
            page_start="",
            page_end="",
            chunk_id="IFRS09_4.1.1__IFRS09_P0001",
            text="This paragraph has content.",
            containing_section_id="IFRS09_0054",
        )
        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid="ifrs9",
                    source_type="html",
                    source_title="IFRS 9",
                    source_url="https://www.ifrs.org/ifrs9.html",
                    canonical_url="https://www.ifrs.org/ifrs9.html",
                    captured_at="2026-04-04T14:23:10Z",
                    document_type="IFRS-S",
                ),
                chunks=[chunk],
                sections=[section],
                section_closure_rows=[SectionClosureRow("IFRS09_0054", "IFRS09_0054", 0)],
                references=[
                    ContentReference(
                        source_doc_uid="ifrs9",
                        source_location_type="section",
                        reference_order=1,
                        annotation_raw_text="Refer: paragraphs BC4.1-BC4.45",
                        target_raw_text="paragraphs BC4.1-BC4.45",
                        target_kind="basis_for_conclusions",
                        target_start="BC4.1",
                        target_end="BC4.45",
                        parsed_ok=True,
                        source_section_id="IFRS09_0054",
                    ),
                    ContentReference(
                        source_doc_uid="ifrs9",
                        source_location_type="chunk",
                        reference_order=2,
                        annotation_raw_text="Refer: paragraph 4.1.1(a)",
                        target_raw_text="paragraph 4.1.1(a)",
                        target_kind="same_standard_paragraph",
                        target_start="4.1.1",
                        parsed_ok=True,
                        source_chunk_id="IFRS09_4.1.1__IFRS09_P0001",
                        source_section_id="IFRS09_0054",
                    ),
                ],
            )
        )

        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        section_store = InMemorySectionStore()
        reference_store = InMemoryReferenceStore()
        vector_store = RecordingVectorStore()
        title_vector_store = RecordingTitleVectorStore()
        document_vector_store = RecordingDocumentVectorStore()
        dependencies = StoreDependencies(
            chunk_store=chunk_store,
            document_store=document_store,
            section_store=section_store,
            reference_store=reference_store,
            vector_store=vector_store,
            title_vector_store=title_vector_store,
            document_vector_store=document_vector_store,
            init_db_fn=lambda: None,
        )
        command = StoreCommand(
            source_path=source_path,
            extractor=extractor,
            dependencies=dependencies,
            explicit_doc_uid=None,
        )

        result = command.execute_result()
        stored_references = reference_store.get_references_by_doc("ifrs9")

        assert result.status == "stored"
        assert len(stored_references) == 2
        assert stored_references[0].source_location_type == "section"
        assert stored_references[0].source_section_db_id is not None
        assert stored_references[1].source_location_type == "chunk"
        assert stored_references[1].source_chunk_db_id is not None

    def test_store_command_does_not_skip_when_references_change(self, tmp_path: Path) -> None:
        """Reference payload changes should prevent unchanged-content skipping."""
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")

        section = SectionRecord(
            section_id="IFRS09_0054",
            doc_uid="ifrs9",
            parent_section_id=None,
            level=1,
            title="Recognition and derecognition",
            section_lineage=["Recognition and derecognition"],
            position=1,
        )
        chunk = Chunk(
            doc_uid="ifrs9",
            chunk_number="4.1.1",
            page_start="",
            page_end="",
            chunk_id="IFRS09_4.1.1__IFRS09_P0001",
            text="This paragraph has content.",
            containing_section_id="IFRS09_0054",
        )

        chunk_store = InMemoryChunkStore()
        chunk_store.insert_chunks([chunk])
        document_store = InMemoryDocumentStore()
        document_store.upsert_document(
            DocumentRecord(
                doc_uid="ifrs9",
                source_type="html",
                source_title="IFRS 9",
                source_url="https://www.ifrs.org/ifrs9.html",
                canonical_url="https://www.ifrs.org/ifrs9.html",
                captured_at="2026-04-04T14:23:10Z",
                document_type="IFRS-S",
            ),
        )
        section_store = InMemorySectionStore()
        section_store.insert_sections([section])
        section_store.insert_closure_rows("ifrs9", [SectionClosureRow("IFRS09_0054", "IFRS09_0054", 0)])
        reference_store = InMemoryReferenceStore()
        reference_store.insert_references(
            [
                ContentReference(
                    source_doc_uid="ifrs9",
                    source_location_type="chunk",
                    reference_order=1,
                    annotation_raw_text="Refer: paragraph 4.1.1(a)",
                    target_raw_text="paragraph 4.1.1(a)",
                    target_kind="same_standard_paragraph",
                    target_start="4.1.1",
                    parsed_ok=True,
                    source_chunk_id="IFRS09_4.1.1__IFRS09_P0001",
                    source_section_id="IFRS09_0054",
                ),
            ],
        )

        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid="ifrs9",
                    source_type="html",
                    source_title="IFRS 9",
                    source_url="https://www.ifrs.org/ifrs9.html",
                    canonical_url="https://www.ifrs.org/ifrs9.html",
                    captured_at="2026-04-04T14:23:10Z",
                    document_type="IFRS-S",
                ),
                chunks=[
                    Chunk(
                        doc_uid="ifrs9",
                        chunk_number="4.1.1",
                        page_start="",
                        page_end="",
                        chunk_id="IFRS09_4.1.1__IFRS09_P0001",
                        text="This paragraph has content.",
                        containing_section_id="IFRS09_0054",
                    )
                ],
                sections=[section],
                section_closure_rows=[SectionClosureRow("IFRS09_0054", "IFRS09_0054", 0)],
                references=[
                    ContentReference(
                        source_doc_uid="ifrs9",
                        source_location_type="chunk",
                        reference_order=1,
                        annotation_raw_text="Refer: paragraph 4.1.1(b)",
                        target_raw_text="paragraph 4.1.1(b)",
                        target_kind="same_standard_paragraph",
                        target_start="4.1.1",
                        parsed_ok=True,
                        source_chunk_id="IFRS09_4.1.1__IFRS09_P0001",
                        source_section_id="IFRS09_0054",
                    ),
                ],
            ),
            skip_if_unchanged=True,
        )

        dependencies = StoreDependencies(
            chunk_store=chunk_store,
            document_store=document_store,
            section_store=section_store,
            reference_store=reference_store,
            vector_store=RecordingVectorStore(),
            title_vector_store=RecordingTitleVectorStore(),
            document_vector_store=RecordingDocumentVectorStore(existing_doc_uids={"ifrs9"}),
            init_db_fn=lambda: None,
        )
        command = StoreCommand(
            source_path=source_path,
            extractor=extractor,
            dependencies=dependencies,
            explicit_doc_uid=None,
        )

        result = command.execute_result()
        stored_references = reference_store.get_references_by_doc("ifrs9")

        assert result.status == "stored"
        assert stored_references[0].annotation_raw_text == "Refer: paragraph 4.1.1(b)"

    def test_store_command_skips_unchanged_html_chunks(self, tmp_path: Path) -> None:
        """HTML imports should be skipped when the extracted payload is unchanged."""
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        vector_store = RecordingVectorStore(existing_doc_uids={"ifrs9"})
        document_vector_store = RecordingDocumentVectorStore(existing_doc_uids={"ifrs9"})

        existing_chunk = Chunk(
            doc_uid="ifrs9",
            chunk_number="2.4",
            page_start="",
            page_end="",
            chunk_id="IFRS09_2.4",
            text="existing content",
        )
        chunk_store.insert_chunks([existing_chunk])
        document_store.upsert_document(
            DocumentRecord(
                doc_uid="ifrs9",
                source_type="html",
                source_title="IFRS 9",
                source_url="https://www.ifrs.org/original.html",
                canonical_url="https://www.ifrs.org/original.html",
                captured_at="2026-04-04T14:23:10Z",
            )
        )

        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid="ifrs9",
                    source_type="html",
                    source_title="IFRS 9",
                    source_url="https://www.ifrs.org/original.html",
                    canonical_url="https://www.ifrs.org/original.html",
                    captured_at="2026-04-05T14:23:10Z",
                ),
                chunks=[
                    Chunk(
                        doc_uid="ifrs9",
                        chunk_number="2.4",
                        page_start="",
                        page_end="",
                        chunk_id="IFRS09_2.4",
                        text="existing content",
                    )
                ],
            ),
            skip_if_unchanged=True,
        )

        dependencies = StoreDependencies(
            chunk_store=chunk_store,
            document_store=document_store,
            vector_store=vector_store,
            document_vector_store=document_vector_store,
            init_db_fn=lambda: None,
        )
        command = StoreCommand(
            source_path=source_path,
            extractor=extractor,
            dependencies=dependencies,
            explicit_doc_uid=None,
        )

        result = command.execute_result()

        assert result.status == "skipped"
        assert result.chunk_count == 1
        assert vector_store.added_embeddings == []
        assert document_vector_store.added_embeddings == []
        assert chunk_store.get_chunks_by_doc("ifrs9")[0].text == "existing content"
        assert command.execute().startswith("Skipped: doc_uid=ifrs9")

    def test_store_command_repairs_missing_chunk_vector_for_unchanged_html(self, tmp_path: Path) -> None:
        """Unchanged HTML imports should repair a missing chunk vector instead of skipping forever."""
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        vector_store = RecordingVectorStore()
        document_vector_store = RecordingDocumentVectorStore(existing_doc_uids={"ifrs9"})

        existing_chunk = Chunk(
            doc_uid="ifrs9",
            chunk_number="2.4",
            page_start="",
            page_end="",
            chunk_id="IFRS09_2.4",
            text="existing content",
        )
        chunk_store.insert_chunks([existing_chunk])
        document_store.upsert_document(
            DocumentRecord(
                doc_uid="ifrs9",
                source_type="html",
                source_title="IFRS 9",
                source_url="https://www.ifrs.org/original.html",
                canonical_url="https://www.ifrs.org/original.html",
                captured_at="2026-04-04T14:23:10Z",
            )
        )

        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid="ifrs9",
                    source_type="html",
                    source_title="IFRS 9",
                    source_url="https://www.ifrs.org/original.html",
                    canonical_url="https://www.ifrs.org/original.html",
                    captured_at="2026-04-05T14:23:10Z",
                ),
                chunks=[
                    Chunk(
                        doc_uid="ifrs9",
                        chunk_number="2.4",
                        page_start="",
                        page_end="",
                        chunk_id="IFRS09_2.4",
                        text="existing content",
                    )
                ],
            ),
            skip_if_unchanged=True,
        )

        dependencies = StoreDependencies(
            chunk_store=chunk_store,
            document_store=document_store,
            vector_store=vector_store,
            document_vector_store=document_vector_store,
            init_db_fn=lambda: None,
        )
        command = StoreCommand(
            source_path=source_path,
            extractor=extractor,
            dependencies=dependencies,
            explicit_doc_uid=None,
        )

        result = command.execute_result()

        assert result.status == "stored"
        assert result.reason == "repaired missing chunk embedding"
        assert vector_store.deleted_doc_uids == ["ifrs9"]
        assert vector_store.added_embeddings == [("ifrs9", [1], ["existing content"])]
        assert document_vector_store.added_embeddings == []

    def test_store_command_reembeds_missing_document_vector_for_unchanged_html(self, tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
        """Unchanged HTML imports should retry the document embedding when the vector is missing."""
        caplog.set_level(logging.WARNING)
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        vector_store = RecordingVectorStore(existing_doc_uids={"ifrs9"})
        document_vector_store = RecordingDocumentVectorStore()

        existing_chunk = Chunk(
            doc_uid="ifrs9",
            chunk_number="2.4",
            page_start="",
            page_end="",
            chunk_id="IFRS09_2.4",
            text="existing content",
        )
        chunk_store.insert_chunks([existing_chunk])
        document_store.upsert_document(
            DocumentRecord(
                doc_uid="ifrs9",
                source_type="html",
                source_title="IFRS 9",
                source_url="https://www.ifrs.org/original.html",
                canonical_url="https://www.ifrs.org/original.html",
                captured_at="2026-04-04T14:23:10Z",
            )
        )

        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid="ifrs9",
                    source_type="html",
                    source_title="IFRS 9",
                    source_url="https://www.ifrs.org/original.html",
                    canonical_url="https://www.ifrs.org/original.html",
                    captured_at="2026-04-05T14:23:10Z",
                ),
                chunks=[
                    Chunk(
                        doc_uid="ifrs9",
                        chunk_number="2.4",
                        page_start="",
                        page_end="",
                        chunk_id="IFRS09_2.4",
                        text="existing content",
                    )
                ],
            ),
            skip_if_unchanged=True,
        )

        dependencies = StoreDependencies(
            chunk_store=chunk_store,
            document_store=document_store,
            vector_store=vector_store,
            document_vector_store=document_vector_store,
            init_db_fn=lambda: None,
        )
        command = StoreCommand(
            source_path=source_path,
            extractor=extractor,
            dependencies=dependencies,
            explicit_doc_uid=None,
        )

        result = command.execute_result()

        assert result.status == "stored"
        assert vector_store.added_embeddings == []
        assert document_vector_store.deleted_doc_uids == ["ifrs9"]
        assert document_vector_store.added_embeddings == [(["ifrs9"], ["Title: IFRS 9"])]
        assert chunk_store.get_chunks_by_doc("ifrs9")[0].text == "existing content"
        assert any("repair_count=" in record.message for record in caplog.records)

    def test_store_command_reembeds_missing_document_vector_for_unchanged_html_scope_representation(self, tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
        """Unchanged HTML imports should retry all missing document embeddings, including scope."""
        caplog.set_level(logging.WARNING)
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        vector_store = RecordingVectorStore()

        existing_document = DocumentRecord(
            doc_uid="ifric16",
            source_type="html",
            source_title="IFRIC 16 Hedges of a Net Investment in a Foreign Operation",
            source_url="https://www.ifrs.org/ifric16.html",
            canonical_url="https://www.ifrs.org/ifric16.html",
            captured_at="2026-04-05T10:00:00Z",
            scope_text="This Interpretation applies to IFRS 9 hedges of net investments.",
        )
        document_store.upsert_document(existing_document)

        extracted_document = ExtractedDocument(
            document=DocumentRecord(
                doc_uid="ifric16",
                source_type="html",
                source_title="IFRIC 16 Hedges of a Net Investment in a Foreign Operation",
                source_url="https://www.ifrs.org/ifric16.html",
                canonical_url="https://www.ifrs.org/ifric16.html",
                captured_at="2026-04-06T10:00:00Z",
                scope_text="This Interpretation applies to IFRS 9 hedges of net investments.",
            ),
            chunks=[
                Chunk(
                    doc_uid="ifric16",
                    chunk_number="1",
                    page_start="",
                    page_end="",
                    chunk_id="c1",
                    containing_section_id="sec-scope",
                    text="This Interpretation applies to IFRS 9 hedges of net investments.",
                )
            ],
            sections=[
                SectionRecord(
                    section_id="sec-scope",
                    doc_uid="ifric16",
                    parent_section_id=None,
                    level=2,
                    title="Scope",
                    section_lineage=["Scope"],
                    position=1,
                )
            ],
            section_closure_rows=[
                SectionClosureRow("sec-scope", "sec-scope", 0),
            ],
        )

        full_store = RecordingDocumentVectorStore(existing_doc_uids={"ifric16"})
        background_and_issue_store = RecordingDocumentVectorStore(existing_doc_uids={"ifric16"})
        scope_store = RecordingDocumentVectorStore()
        toc_store = RecordingDocumentVectorStore(existing_doc_uids={"ifric16"})
        stores_by_representation = {
            "full": full_store,
            "background_and_issue": background_and_issue_store,
            "scope": scope_store,
            "toc": toc_store,
        }

        dependencies = StoreDependencies(
            chunk_store=chunk_store,
            document_store=document_store,
            vector_store=vector_store,
            document_vector_store_factory=lambda representation: stores_by_representation[representation],
            init_db_fn=lambda: None,
        )
        command = StoreCommand(
            source_path=source_path,
            extractor=FakeExtractor(extracted_document=extracted_document, skip_if_unchanged=True),
            dependencies=dependencies,
            explicit_doc_uid=None,
            scope="documents",
        )

        result = command.execute_result()

        assert result.status == "stored"
        assert vector_store.added_embeddings == []
        assert full_store.deleted_doc_uids == ["ifric16"]
        assert background_and_issue_store.deleted_doc_uids == ["ifric16"]
        assert scope_store.deleted_doc_uids == ["ifric16"]
        assert toc_store.deleted_doc_uids == ["ifric16"]
        assert scope_store.added_embeddings and scope_store.added_embeddings[0][0] == ["ifric16"]
        assert "Scope: This Interpretation applies to IFRS 9 hedges of net investments." in scope_store.added_embeddings[0][1][0]
        assert any("missing_representations=scope" in record.message for record in caplog.records)

    def test_store_command_truncates_oversized_chunks(self, tmp_path: Path) -> None:
        """Oversized chunks should be truncated before persistence."""
        source_path = tmp_path / "test.pdf"
        source_path.write_text("dummy", encoding="utf-8")
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        vector_store = RecordingVectorStore()
        document_vector_store = RecordingDocumentVectorStore()
        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid="ifrs16",
                    source_type="pdf",
                    source_title="IFRS 16",
                    source_url=None,
                    canonical_url=None,
                    captured_at=None,
                ),
                chunks=[
                    Chunk(
                        doc_uid="ifrs16",
                        chunk_number="B43",
                        page_start="A856",
                        page_end="A856",
                        text="x" * (MAX_EMBEDDING_TEXT_CHARS + 20),
                    )
                ],
            )
        )

        dependencies = StoreDependencies(
            chunk_store=chunk_store,
            document_store=document_store,
            vector_store=vector_store,
            document_vector_store=document_vector_store,
            init_db_fn=lambda: None,
        )
        command = StoreCommand(
            source_path=source_path,
            extractor=extractor,
            dependencies=dependencies,
            explicit_doc_uid=None,
        )

        result = command.execute_result()
        stored_chunk = chunk_store.get_chunks_by_doc("ifrs16")[0]

        assert result.status == "stored"
        assert len(stored_chunk.text) == MAX_EMBEDDING_TEXT_CHARS

    def test_store_command_file_not_found(self) -> None:
        """Missing source files should return an error result."""
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        vector_store = RecordingVectorStore()
        document_vector_store = RecordingDocumentVectorStore()
        dependencies = StoreDependencies(
            chunk_store=chunk_store,
            document_store=document_store,
            vector_store=vector_store,
            document_vector_store=document_vector_store,
            init_db_fn=lambda: None,
        )
        command = StoreCommand(
            source_path=Path("/nonexistent/file.pdf"),
            extractor=FakeExtractor(
                extracted_document=ExtractedDocument(
                    document=DocumentRecord(
                        doc_uid="missing",
                        source_type="pdf",
                        source_title="Missing",
                        source_url=None,
                        canonical_url=None,
                        captured_at=None,
                    ),
                    chunks=[],
                )
            ),
            dependencies=dependencies,
            explicit_doc_uid=None,
        )

        result = command.execute()

        assert result.startswith("Error:")
        assert "not found" in result
