"""Repair and error-path tests for store command."""

from tests.unit.test_store_command import *  # noqa: F403


class TestStoreCommandRepairs:
    def test_store_command_documents_scope_repairs_plural_issues_document_representation(self, tmp_path: Path) -> None:
        """Document-only reruns should repair stale issue_text, toc_text, and document embeddings."""
        source_path = tmp_path / "ifric16.html"
        source_path.write_text("dummy", encoding="utf-8")
        chunk_store = InMemoryChunkStore()
        document_store = InMemoryDocumentStore()
        section_store = InMemorySectionStore()
        vector_store = RecordingVectorStore()
        title_vector_store = RecordingTitleVectorStore()
        document_vector_store = RecordingDocumentVectorStore(existing_doc_uids={"ifric16"})

        document_store.upsert_document(
            DocumentRecord(
                doc_uid="ifric16",
                source_type="html",
                source_title="IFRIC 16 Hedges of a Net Investment in a Foreign Operation",
                source_url="https://www.ifrs.org/ifric16.html",
                canonical_url="https://www.ifrs.org/ifric16.html",
                captured_at="2026-04-05T10:00:00Z",
                background_text="This Interpretation addresses hedges of net investments.",
                scope_text="This Interpretation applies to IFRS 9 hedges of net investments.",
                toc_text="Issues\nConsensus",
            )
        )

        extractor = FakeExtractor(
            extracted_document=ExtractedDocument(
                document=DocumentRecord(
                    doc_uid="ifric16",
                    source_type="html",
                    source_title="IFRIC 16 Hedges of a Net Investment in a Foreign Operation",
                    source_url="https://www.ifrs.org/ifric16.html",
                    canonical_url="https://www.ifrs.org/ifric16.html",
                    captured_at="2026-04-05T10:00:00Z",
                ),
                chunks=[
                    Chunk(
                        doc_uid="ifric16",
                        chunk_number="1",
                        page_start="",
                        page_end="",
                        chunk_id="c1",
                        containing_section_id="sec-background",
                        text="This Interpretation addresses hedges of net investments.",
                    ),
                    Chunk(
                        doc_uid="ifric16",
                        chunk_number="2",
                        page_start="",
                        page_end="",
                        chunk_id="c2",
                        containing_section_id="sec-scope",
                        text="This Interpretation applies to IFRS 9 hedges of net investments.",
                    ),
                    Chunk(
                        doc_uid="ifric16",
                        chunk_number="3",
                        page_start="",
                        page_end="",
                        chunk_id="c3",
                        containing_section_id="sec-issues",
                        text="The issues are which entity may hold the hedging instrument.",
                    ),
                    Chunk(
                        doc_uid="ifric16",
                        chunk_number="4",
                        page_start="",
                        page_end="",
                        chunk_id="c4",
                        containing_section_id="sec-consensus",
                        text="The consensus sets out the interpretation outcome.",
                    ),
                ],
                sections=[
                    SectionRecord(
                        section_id="sec-background",
                        doc_uid="ifric16",
                        parent_section_id=None,
                        level=2,
                        title="Background",
                        section_lineage=["Background"],
                        position=1,
                    ),
                    SectionRecord(
                        section_id="sec-scope",
                        doc_uid="ifric16",
                        parent_section_id=None,
                        level=2,
                        title="Scope",
                        section_lineage=["Scope"],
                        position=2,
                    ),
                    SectionRecord(
                        section_id="sec-issues",
                        doc_uid="ifric16",
                        parent_section_id=None,
                        level=2,
                        title="Issues",
                        section_lineage=["Issues"],
                        position=3,
                    ),
                    SectionRecord(
                        section_id="sec-consensus",
                        doc_uid="ifric16",
                        parent_section_id=None,
                        level=2,
                        title="Consensus",
                        section_lineage=["Consensus"],
                        position=4,
                    ),
                ],
                section_closure_rows=[
                    SectionClosureRow("sec-background", "sec-background", 0),
                    SectionClosureRow("sec-scope", "sec-scope", 0),
                    SectionClosureRow("sec-issues", "sec-issues", 0),
                    SectionClosureRow("sec-consensus", "sec-consensus", 0),
                ],
            ),
            skip_if_unchanged=True,
        )

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
            options=StoreCommandOptions(scope="documents"),
        )

        result = command.execute_result()
        stored_document = document_store.get_document("ifric16")

        assert result.status == "stored"
        assert stored_document is not None
        assert stored_document.issue_text == "The issues are which entity may hold the hedging instrument."
        assert stored_document.toc_text == "Consensus"
        assert chunk_store.get_chunks_by_doc("ifric16") == []
        assert section_store.get_sections_by_doc("ifric16") == []
        assert vector_store.added_embeddings == []
        assert title_vector_store.added_embeddings == []
        assert document_vector_store.deleted_doc_uids == ["ifric16"]
        assert document_vector_store.added_embeddings == [
            (
                ["ifric16"],
                [
                    "Title: IFRIC 16 Hedges of a Net Investment in a Foreign Operation\n"
                    "Background: This Interpretation addresses hedges of net investments.\n"
                    "Issue: The issues are which entity may hold the hedging instrument.\n"
                    "Scope: This Interpretation applies to IFRS 9 hedges of net investments.\n"
                    "TOC: Consensus"
                ],
            )
        ]

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
            options=StoreCommandOptions(),
        )

        with pytest.raises(NameError, match="simulated programmer bug"):
            command.execute_result()

    def test_store_command_requires_dependencies(self, tmp_path: Path) -> None:
        """The constructor should keep dependency injection explicit."""
        source_path = tmp_path / "test.html"
        source_path.write_text("dummy", encoding="utf-8")

        with pytest.raises(TypeError):
            StoreCommand(source_path=source_path)  # type: ignore[call-arg]
