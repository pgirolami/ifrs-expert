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
from src.models.section import SectionClosureRow, SectionRecord
from tests.fakes import (
    InMemoryChunkStore,
    InMemoryDocumentStore,
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

    def test_store_command_skips_unchanged_html_chunks(self, tmp_path: Path) -> None:
        """HTML imports should be skipped when the extracted payload is unchanged."""
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

        assert result.status == "skipped"
        assert result.chunk_count == 1
        assert vector_store.added_embeddings == []
        assert document_vector_store.added_embeddings == []
        assert chunk_store.get_chunks_by_doc("ifrs9")[0].text == "existing content"
        assert command.execute().startswith("Skipped: doc_uid=ifrs9")

    def test_store_command_reembeds_missing_document_vector_for_unchanged_html(self, tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
        """Unchanged HTML imports should retry the document embedding when the vector is missing."""
        caplog.set_level(logging.WARNING)
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        vector_store = RecordingVectorStore()
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

    def test_store_command_stores_sections_title_embeddings_and_document_representation(self, tmp_path: Path) -> None:
        """Store command should persist sections, title embeddings, and document embeddings."""
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")

        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid="ifrs9",
                    source_type="html",
                    source_title="IFRS 9",
                    source_url="https://www.ifrs.org/ifrs9.html",
                    canonical_url="https://www.ifrs.org/ifrs9.html",
                    captured_at="2026-04-04T14:23:10Z",
                ),
                chunks=[
                    Chunk(
                        doc_uid="ifrs9",
                        chunk_number="3.1.1",
                        page_start="",
                        page_end="",
                        chunk_id="IFRS09_3.1.1",
                        containing_section_id="IFRS09_g3.1.1-3.1.2",
                        text="test content",
                    )
                ],
                sections=[
                    SectionRecord(
                        section_id="IFRS09_0054",
                        doc_uid="ifrs9",
                        parent_section_id=None,
                        level=2,
                        title="Scope",
                        section_lineage=["Scope"],
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
                ],
                section_closure_rows=[
                    SectionClosureRow("IFRS09_0054", "IFRS09_0054", 0),
                    SectionClosureRow("IFRS09_0054", "IFRS09_g3.1.1-3.1.2", 1),
                    SectionClosureRow("IFRS09_g3.1.1-3.1.2", "IFRS09_g3.1.1-3.1.2", 0),
                ],
            )
        )
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        section_store = InMemorySectionStore()
        vector_store = RecordingVectorStore()
        title_vector_store = RecordingTitleVectorStore()
        document_vector_store = RecordingDocumentVectorStore()
        dependencies = StoreDependencies(
            chunk_store=chunk_store,
            document_store=document_store,
            section_store=section_store,
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

        assert result.status == "stored"
        stored_sections = section_store.get_sections_by_doc("ifrs9")
        stored_chunks = chunk_store.get_chunks_by_doc("ifrs9")

        assert [section.section_id for section in stored_sections] == ["IFRS09_0054", "IFRS09_g3.1.1-3.1.2"]
        assert stored_chunks[0].containing_section_db_id == stored_sections[1].db_id
        assert title_vector_store.added_embeddings == [("ifrs9", ["IFRS09_0054", "IFRS09_g3.1.1-3.1.2"], ["Scope", "Initial recognition"])]
        stored_document = document_store.get_document("ifrs9")
        assert stored_document is not None
        assert stored_document.document_type == "IFRS-S"
        assert stored_document.scope_text == "test content"
        assert stored_document.intro_text is None
        assert stored_document.toc_text is None
        assert document_vector_store.added_embeddings == [(["ifrs9"], ["Title: IFRS 9\nScope: test content"])]

    def test_store_command_with_documents_scope_stores_only_document_representation(self, tmp_path: Path) -> None:
        """Document scope should skip chunk and section persistence while updating document embeddings."""
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")

        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid="ifrs9",
                    source_type="html",
                    source_title="IFRS 9",
                    source_url="https://www.ifrs.org/ifrs9.html",
                    canonical_url="https://www.ifrs.org/ifrs9.html",
                    captured_at="2026-04-04T14:23:10Z",
                ),
                chunks=[
                    Chunk(
                        doc_uid="ifrs9",
                        chunk_number="3.1.1",
                        page_start="",
                        page_end="",
                        chunk_id="IFRS09_3.1.1",
                        containing_section_id="IFRS09_scope",
                        text="test content",
                    )
                ],
                sections=[
                    SectionRecord(
                        section_id="IFRS09_scope",
                        doc_uid="ifrs9",
                        parent_section_id=None,
                        level=2,
                        title="Scope",
                        section_lineage=["Scope"],
                        position=1,
                    )
                ],
                section_closure_rows=[
                    SectionClosureRow("IFRS09_scope", "IFRS09_scope", 0),
                ],
            )
        )
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        section_store = InMemorySectionStore()
        vector_store = RecordingVectorStore()
        title_vector_store = RecordingTitleVectorStore()
        document_vector_store = RecordingDocumentVectorStore()
        dependencies = StoreDependencies(
            chunk_store=chunk_store,
            document_store=document_store,
            section_store=section_store,
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
            scope="documents",
        )

        result = command.execute_result()

        assert result.status == "stored"
        assert chunk_store.get_chunks_by_doc("ifrs9") == []
        assert section_store.get_sections_by_doc("ifrs9") == []
        stored_document = document_store.get_document("ifrs9")
        assert stored_document is not None
        assert stored_document.scope_text == "test content"
        assert vector_store.added_embeddings == []
        assert title_vector_store.added_embeddings == []
        assert document_vector_store.added_embeddings == [(["ifrs9"], ["Title: IFRS 9\nScope: test content"])]

    def test_store_command_persists_navis_intro_text_from_essentiel_generalites(self, tmp_path: Path) -> None:
        """Navis documents should persist intro_text from Généralités under L'ESSENTIEL DE LA NORME."""
        source_path = tmp_path / "navis.html"
        source_path.write_text("dummy", encoding="utf-8")

        navis_doc_uid = "navis-QRIFRS-C2A8E6F292F99E-EFL"
        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid=navis_doc_uid,
                    source_type="html",
                    source_title="CHAPITRE 4 Cadre conceptuel de l'information financière",
                    source_url="https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&refId=C2A8E6F292F99E-EFL",
                    canonical_url="https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&refId=C2A8E6F292F99E-EFL",
                    captured_at="2026-04-13T12:00:00Z",
                    source_domain="abonnes.efl.fr",
                    document_type="NAVIS",
                ),
                chunks=[
                    Chunk(
                        doc_uid=navis_doc_uid,
                        chunk_number="12501",
                        page_start="",
                        page_end="",
                        chunk_id="P8A8E6F292F99E-EFL",
                        containing_section_id="generalites",
                        text="Premier paragraphe.",
                    ),
                    Chunk(
                        doc_uid=navis_doc_uid,
                        chunk_number="12502",
                        page_start="",
                        page_end="",
                        chunk_id="P8A8E6F292F99E-EFL-2",
                        containing_section_id="generalites-child",
                        text="Deuxième paragraphe.",
                    ),
                ],
                sections=[
                    SectionRecord(
                        section_id="chapter-1",
                        doc_uid=navis_doc_uid,
                        parent_section_id=None,
                        level=1,
                        title="Cadre conceptuel de l'information financière",
                        section_lineage=["Cadre conceptuel de l'information financière"],
                        position=1,
                    ),
                    SectionRecord(
                        section_id="essential",
                        doc_uid=navis_doc_uid,
                        parent_section_id="chapter-1",
                        level=2,
                        title="L'ESSENTIEL DE LA NORME",
                        section_lineage=["Cadre conceptuel de l'information financière", "L'ESSENTIEL DE LA NORME"],
                        position=2,
                    ),
                    SectionRecord(
                        section_id="generalites",
                        doc_uid=navis_doc_uid,
                        parent_section_id="essential",
                        level=3,
                        title="Généralités",
                        section_lineage=[
                            "Cadre conceptuel de l'information financière",
                            "L'ESSENTIEL DE LA NORME",
                            "Généralités",
                        ],
                        position=3,
                    ),
                    SectionRecord(
                        section_id="generalites-child",
                        doc_uid=navis_doc_uid,
                        parent_section_id="generalites",
                        level=4,
                        title="Définitions clés",
                        section_lineage=[
                            "Cadre conceptuel de l'information financière",
                            "L'ESSENTIEL DE LA NORME",
                            "Généralités",
                            "Définitions clés",
                        ],
                        position=4,
                    ),
                ],
                section_closure_rows=[
                    SectionClosureRow("chapter-1", "chapter-1", 0),
                    SectionClosureRow("chapter-1", "essential", 1),
                    SectionClosureRow("chapter-1", "generalites", 2),
                    SectionClosureRow("chapter-1", "generalites-child", 3),
                    SectionClosureRow("essential", "essential", 0),
                    SectionClosureRow("essential", "generalites", 1),
                    SectionClosureRow("essential", "generalites-child", 2),
                    SectionClosureRow("generalites", "generalites", 0),
                    SectionClosureRow("generalites", "generalites-child", 1),
                    SectionClosureRow("generalites-child", "generalites-child", 0),
                ],
            )
        )
        dependencies = StoreDependencies(
            chunk_store=InMemoryChunkStore(),
            document_store=InMemoryDocumentStore(),
            section_store=InMemorySectionStore(),
            vector_store=RecordingVectorStore(),
            title_vector_store=RecordingTitleVectorStore(),
            document_vector_store=RecordingDocumentVectorStore(),
            init_db_fn=lambda: None,
        )
        command = StoreCommand(
            source_path=source_path,
            extractor=extractor,
            dependencies=dependencies,
            explicit_doc_uid=None,
        )

        result = command.execute_result()
        stored_document = dependencies.document_store.get_document(navis_doc_uid)

        assert result.status == "stored"
        assert stored_document is not None
        assert stored_document.intro_text == "Premier paragraphe.\nDeuxième paragraphe."

    def test_store_command_with_sections_scope_stores_only_sections_and_title_embeddings(self, tmp_path: Path) -> None:
        """Section scope should skip chunk and document persistence while updating section embeddings."""
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")

        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid="ifrs9",
                    source_type="html",
                    source_title="IFRS 9",
                    source_url="https://www.ifrs.org/ifrs9.html",
                    canonical_url="https://www.ifrs.org/ifrs9.html",
                    captured_at="2026-04-04T14:23:10Z",
                ),
                chunks=[
                    Chunk(
                        doc_uid="ifrs9",
                        chunk_number="3.1.1",
                        page_start="",
                        page_end="",
                        chunk_id="IFRS09_3.1.1",
                        containing_section_id="IFRS09_scope",
                        text="test content",
                    )
                ],
                sections=[
                    SectionRecord(
                        section_id="IFRS09_scope",
                        doc_uid="ifrs9",
                        parent_section_id=None,
                        level=2,
                        title="Scope",
                        section_lineage=["Scope"],
                        position=1,
                    )
                ],
                section_closure_rows=[
                    SectionClosureRow("IFRS09_scope", "IFRS09_scope", 0),
                ],
            )
        )
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        section_store = InMemorySectionStore()
        vector_store = RecordingVectorStore()
        title_vector_store = RecordingTitleVectorStore()
        document_vector_store = RecordingDocumentVectorStore()
        dependencies = StoreDependencies(
            chunk_store=chunk_store,
            document_store=document_store,
            section_store=section_store,
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
            scope="sections",
        )

        result = command.execute_result()

        assert result.status == "stored"
        assert chunk_store.get_chunks_by_doc("ifrs9") == []
        assert document_store.get_document("ifrs9") is None
        assert [section.section_id for section in section_store.get_sections_by_doc("ifrs9")] == ["IFRS09_scope"]
        assert vector_store.added_embeddings == []
        assert title_vector_store.added_embeddings == [("ifrs9", ["IFRS09_scope"], ["Scope"])]
        assert document_vector_store.added_embeddings == []

    def test_store_command_excludes_filtered_sections_from_toc(self, tmp_path: Path) -> None:
        """TOC should omit sections excluded by section filtering."""
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")

        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid="ifrs9",
                    source_type="html",
                    source_title="IFRS 9",
                    source_url="https://www.ifrs.org/ifrs9.html",
                    canonical_url="https://www.ifrs.org/ifrs9.html",
                    captured_at="2026-04-04T14:23:10Z",
                ),
                chunks=[
                    Chunk(
                        doc_uid="ifrs9",
                        chunk_number="1",
                        page_start="",
                        page_end="",
                        chunk_id="IFRS09_contents",
                        containing_section_id="sec-contents",
                        text="contents chunk",
                    ),
                    Chunk(
                        doc_uid="ifrs9",
                        chunk_number="2",
                        page_start="",
                        page_end="",
                        chunk_id="IFRS09_scope",
                        containing_section_id="sec-scope",
                        text="scope chunk",
                    ),
                ],
                sections=[
                    SectionRecord(
                        section_id="sec-contents",
                        doc_uid="ifrs9",
                        parent_section_id=None,
                        level=2,
                        title="Contents",
                        section_lineage=["Contents"],
                        position=1,
                    ),
                    SectionRecord(
                        section_id="sec-scope",
                        doc_uid="ifrs9",
                        parent_section_id=None,
                        level=2,
                        title="Scope",
                        section_lineage=["Scope"],
                        position=2,
                    ),
                ],
                section_closure_rows=[
                    SectionClosureRow("sec-contents", "sec-contents", 0),
                    SectionClosureRow("sec-scope", "sec-scope", 0),
                ],
            )
        )
        dependencies = StoreDependencies(
            chunk_store=InMemoryChunkStore(),
            document_store=InMemoryDocumentStore(),
            section_store=InMemorySectionStore(),
            vector_store=RecordingVectorStore(),
            title_vector_store=RecordingTitleVectorStore(),
            document_vector_store=RecordingDocumentVectorStore(),
            init_db_fn=lambda: None,
        )
        command = StoreCommand(
            source_path=source_path,
            extractor=extractor,
            dependencies=dependencies,
            explicit_doc_uid=None,
        )

        result = command.execute_result()
        stored_document = dependencies.document_store.get_document("ifrs9")

        assert result.status == "stored"
        assert stored_document is not None
        assert stored_document.toc_text is None

    def test_store_command_rebuilds_when_document_representation_changes(self, tmp_path: Path) -> None:
        """Changed document-representation fields should force a re-store even if chunks are unchanged."""
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        vector_store = RecordingVectorStore()
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
                source_title="Old IFRS 9 title",
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
        stored_document = document_store.get_document("ifrs9")
        assert stored_document is not None
        assert stored_document.source_title == "IFRS 9"
        assert stored_document.intro_text is None
        assert document_vector_store.added_embeddings == [(["ifrs9"], ["Title: IFRS 9"])]

    def test_store_command_raises_unexpected_programmer_errors(self, tmp_path: Path) -> None:
        """Unexpected programmer errors should not be downgraded into failed results."""
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")
        dependencies = StoreDependencies(
            chunk_store=InMemoryChunkStore(),
            document_store=InMemoryDocumentStore(),
            vector_store=RecordingVectorStore(),
            document_vector_store=RecordingDocumentVectorStore(),
            init_db_fn=lambda: None,
        )
        command = StoreCommand(
            source_path=source_path,
            extractor=FakeBuggyExtractor(),
            dependencies=dependencies,
            explicit_doc_uid=None,
        )

        with pytest.raises(NameError, match="simulated programmer bug"):
            command.execute_result()

    def test_store_command_requires_dependencies(self, tmp_path: Path) -> None:
        """The constructor should keep dependency injection explicit."""
        source_path = tmp_path / "test.pdf"
        source_path.write_text("dummy", encoding="utf-8")

        with pytest.raises(TypeError):
            StoreCommand(source_path=source_path)  # type: ignore[call-arg]
