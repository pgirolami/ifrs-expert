"""Tests for the generalized store command."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest

from src.commands.store import MAX_CHUNK_CHARS, StoreCommand
from src.models.chunk import Chunk
from src.models.document import DocumentRecord
from src.models.extraction import ExtractedDocument
from tests.fakes import InMemoryChunkStore, InMemoryDocumentStore, RecordingVectorStore


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
                        section_path="1.1",
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
        command = StoreCommand(
            source_path=source_path,
            extractor=extractor,
            chunk_store=chunk_store,
            document_store=document_store,
            vector_store=vector_store,
            init_db_fn=lambda: None,
            explicit_doc_uid=None,
        )

        result = command.execute_result()

        assert result.status == "stored"
        assert result.doc_uid == "ifrs9"
        assert result.chunk_count == 1
        stored_document = document_store.get_document("ifrs9")
        assert stored_document is not None, "Expected document metadata to be stored"
        assert stored_document.source_type == "pdf"
        assert chunk_store.get_chunks_by_doc("ifrs9")[0].text == "test content"
        assert vector_store.added_embeddings == [("ifrs9", [1], ["test content"])]
        assert command.execute().startswith("Stored 1 chunks")

    def test_store_command_skips_unchanged_html_chunks(self, tmp_path: Path) -> None:
        """HTML imports should be skipped when the extracted payload is unchanged."""
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        vector_store = RecordingVectorStore()

        existing_chunk = Chunk(
            doc_uid="ifrs9",
            section_path="2.4",
            page_start="",
            page_end="",
            source_anchor="IFRS09_2.4",
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
                        section_path="2.4",
                        page_start="",
                        page_end="",
                        source_anchor="IFRS09_2.4",
                        text="existing content",
                    )
                ],
            ),
            skip_if_unchanged=True,
        )

        command = StoreCommand(
            source_path=source_path,
            extractor=extractor,
            chunk_store=chunk_store,
            document_store=document_store,
            vector_store=vector_store,
            init_db_fn=lambda: None,
            explicit_doc_uid=None,
        )

        result = command.execute_result()

        assert result.status == "skipped"
        assert result.chunk_count == 1
        assert vector_store.added_embeddings == []
        assert chunk_store.get_chunks_by_doc("ifrs9")[0].text == "existing content"
        assert command.execute().startswith("Skipped: doc_uid=ifrs9")

    def test_store_command_truncates_oversized_chunks(self, tmp_path: Path) -> None:
        """Oversized chunks should be truncated before persistence."""
        source_path = tmp_path / "test.pdf"
        source_path.write_text("dummy", encoding="utf-8")
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        vector_store = RecordingVectorStore()
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
                        section_path="B43",
                        page_start="A856",
                        page_end="A856",
                        text="x" * (MAX_CHUNK_CHARS + 20),
                    )
                ],
            )
        )

        command = StoreCommand(
            source_path=source_path,
            extractor=extractor,
            chunk_store=chunk_store,
            document_store=document_store,
            vector_store=vector_store,
            init_db_fn=lambda: None,
            explicit_doc_uid=None,
        )

        result = command.execute_result()
        stored_chunk = chunk_store.get_chunks_by_doc("ifrs16")[0]

        assert result.status == "stored"
        assert len(stored_chunk.text) == MAX_CHUNK_CHARS

    def test_store_command_file_not_found(self) -> None:
        """Missing source files should return an error result."""
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
            chunk_store=InMemoryChunkStore(),
            document_store=InMemoryDocumentStore(),
            vector_store=RecordingVectorStore(),
            init_db_fn=lambda: None,
            explicit_doc_uid=None,
        )

        result = command.execute()

        assert result.startswith("Error:")
        assert "not found" in result

    def test_store_command_requires_dependencies(self, tmp_path: Path) -> None:
        """The constructor should keep dependency injection explicit."""
        source_path = tmp_path / "test.pdf"
        source_path.write_text("dummy", encoding="utf-8")

        with pytest.raises(TypeError):
            StoreCommand(source_path=source_path)  # type: ignore[call-arg]
