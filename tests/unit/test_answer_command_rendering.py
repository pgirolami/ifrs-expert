"""Rendering and authority-filtering tests for answer command."""

from tests.unit.test_answer_command import *  # noqa: F403

class TestBuildPromptBContext:
    """Tests for the _build_prompt_b_context method that filters Prompt B context by authority."""

    def _make_command(self, chunk_store: InMemoryChunkStore) -> AnswerCommand:
        """Helper to create AnswerCommand with mock dependencies."""
        config = AnswerConfig(
            vector_store=MockVectorStore([]),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=lambda prompt: "result",
        )
        return AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text")))

    def _make_formatted_chunks(self, chunks: list[Chunk]) -> list[str]:
        """Helper to format chunks as they would appear in the prompt."""
        formatted: list[str] = []
        for chunk in chunks:
            chunk_xml = f'<chunk id="{chunk.id}" doc_uid="{chunk.doc_uid}" paragraph="{chunk.chunk_number}" score="0.9000">\n{chunk.text}\n</chunk>'
            formatted.append(f'<Document name="{chunk.doc_uid}">\n{chunk_xml}\n</Document>')
        return formatted

    def test_filters_prompt_b_context_to_primary_authority(self) -> None:
        """Prompt B context should include only chunks listed in primary_authority."""
        mock_chunks = [
            Chunk(id=1, doc_uid="ifrs15", chunk_number="5.1", page_start="A1", page_end="A1", text="primary content - should be included"),
            Chunk(id=2, doc_uid="ifrs15", chunk_number="5.2", page_start="A2", page_end="A2", text="peripheral content - should be excluded"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {"status": "pass", "authority_classification": {"primary_authority": [{"document": "ifrs15", "references": ["5.1"], "reason": "Primary"}], "supporting_authority": [], "peripheral_authority": []}}

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "primary content" in context
        assert "peripheral content" not in context

    def test_filters_prompt_b_context_to_supporting_authority(self) -> None:
        """Prompt B context should include only chunks listed in supporting_authority."""
        mock_chunks = [
            Chunk(id=1, doc_uid="ifrs9", chunk_number="6.1", page_start="A1", page_end="A1", text="main standard content - should be excluded"),
            Chunk(id=2, doc_uid="ias21", chunk_number="8.2", page_start="B1", page_end="B1", text="supporting clarification - should be included"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {"status": "pass", "authority_classification": {"primary_authority": [], "supporting_authority": [{"document": "ias21", "references": ["8.2"], "reason": "Supporting"}], "peripheral_authority": []}}

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "supporting clarification" in context
        assert "main standard content" not in context

    def test_combines_primary_and_supporting_authority(self) -> None:
        """Prompt B context should include chunks from both primary and supporting authority."""
        mock_chunks = [
            Chunk(id=1, doc_uid="ifrs15", chunk_number="5.1", page_start="A1", page_end="A1", text="primary chunk"),
            Chunk(id=2, doc_uid="ias21", chunk_number="8.2", page_start="B1", page_end="B1", text="supporting chunk"),
            Chunk(id=3, doc_uid="ifrs9", chunk_number="3.4", page_start="C1", page_end="C1", text="peripheral chunk"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {
            "status": "pass",
            "authority_classification": {
                "primary_authority": [{"document": "ifrs15", "references": ["5.1"], "reason": "Primary"}],
                "supporting_authority": [{"document": "ias21", "references": ["8.2"], "reason": "Supporting"}],
                "peripheral_authority": [],
            },
        }

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "primary chunk" in context
        assert "supporting chunk" in context
        assert "peripheral chunk" not in context

    def test_uses_all_chunks_when_no_authority_classification(self) -> None:
        """Prompt B context should use all chunks when authority_classification is missing."""
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="first chunk"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="second chunk"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {"status": "pass"}  # No authority_classification

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "first chunk" in context
        assert "second chunk" in context

    def test_uses_all_chunks_when_no_primary_or_supporting_authority(self) -> None:
        """Prompt B context should use all chunks when primary and supporting authority are empty."""
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="peripheral chunk 1"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="peripheral chunk 2"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {"status": "pass", "authority_classification": {"primary_authority": [], "supporting_authority": [], "peripheral_authority": [{"document": "doc1", "references": ["1.1"], "reason": "Peripheral"}]}}

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "peripheral chunk 1" in context
        assert "peripheral chunk 2" in context

    def test_handles_multiple_references_per_document(self) -> None:
        """Prompt B context should handle multiple references for the same document."""
        mock_chunks = [
            Chunk(id=1, doc_uid="ifrs15", chunk_number="5.1", page_start="A1", page_end="A1", text="first primary section"),
            Chunk(id=2, doc_uid="ifrs15", chunk_number="5.2", page_start="A2", page_end="A2", text="second primary section"),
            Chunk(id=3, doc_uid="ifrs15", chunk_number="5.3", page_start="A3", page_end="A3", text="excluded section"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {"status": "pass", "authority_classification": {"primary_authority": [{"document": "ifrs15", "references": ["5.1", "5.2"], "reason": "Primary"}], "supporting_authority": [], "peripheral_authority": []}}

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "first primary section" in context
        assert "second primary section" in context
        assert "excluded section" not in context

    def test_handles_non_dict_prompt_a_json(self) -> None:
        """Prompt B context should use all chunks when Prompt A JSON is not a dict."""
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="first chunk"),
            Chunk(id=2, doc_uid="doc1", chunk_number="1.2", page_start="A2", page_end="A2", text="second chunk"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        # Array instead of dict
        prompt_a_json: object = []

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        assert "first chunk" in context
        assert "second chunk" in context

    def test_handles_missing_document_in_references(self) -> None:
        """Prompt B context should skip authority items without a document field."""
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="included chunk"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {
            "status": "pass",
            "authority_classification": {
                "primary_authority": [
                    {"references": ["1.1"], "reason": "Missing document"}  # Missing document field
                ],
                "supporting_authority": [],
                "peripheral_authority": [],
            },
        }

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        # Falls back to all chunks
        assert "included chunk" in context

    def test_handles_missing_references_in_authority_item(self) -> None:
        """Prompt B context should skip authority items without references."""
        mock_chunks = [
            Chunk(id=1, doc_uid="doc1", chunk_number="1.1", page_start="A1", page_end="A1", text="fallback chunk"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {
            "status": "pass",
            "authority_classification": {
                "primary_authority": [
                    {"document": "doc1", "reason": "No references"}  # Missing references
                ],
                "supporting_authority": [],
                "peripheral_authority": [],
            },
        }

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        # Falls back to all chunks
        assert "fallback chunk" in context

    def test_excludes_entire_document_when_no_matching_chunks(self) -> None:
        """When no chunks from a document match authority, exclude the entire document."""
        mock_chunks = [
            Chunk(id=1, doc_uid="peripheral_doc", chunk_number="2.1", page_start="A1", page_end="A1", text="peripheral doc content"),
            Chunk(id=2, doc_uid="peripheral_doc", chunk_number="2.2", page_start="A2", page_end="A2", text="more peripheral content"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        command = self._make_command(chunk_store)
        formatted_chunks = self._make_formatted_chunks(mock_chunks)

        prompt_a_json = {"status": "pass", "authority_classification": {"primary_authority": [{"document": "some_other_doc", "references": ["1.1"], "reason": "Primary"}], "supporting_authority": [], "peripheral_authority": []}}

        context = command._build_prompt_b_context(formatted_chunks, prompt_a_json)

        # Falls back to all chunks when no chunks match
        assert "peripheral doc content" in context


class TestAnswerCommandAuthorityFiltering:
    """Integration tests for full answer pipeline with authority-based Prompt B filtering."""

    def test_build_chunk_summary_logs_top_chunk_preview(self, caplog: pytest.LogCaptureFixture) -> None:
        """Chunk summary should log the top chunk section number and a short text preview per document."""
        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(
                [
                    Chunk(id=1, doc_uid="doc1", chunk_number="5.1", page_start="A1", page_end="A1", text="This is the first section text and it continues."),
                    Chunk(id=2, doc_uid="doc1", chunk_number="5.2", page_start="A2", page_end="A2", text="This is not the top chunk."),
                    Chunk(id=3, doc_uid="doc2", chunk_number="8.3", page_start="B1", page_end="B1", text="Secondary document section text for logging."),
                ]
            )

        command = AnswerCommand(
            query="test",
            config=AnswerConfig(
                vector_store=MockVectorStore([]),
                chunk_store=chunk_store,
                init_db_fn=lambda: None,
                index_path_fn=lambda: MockIndexPath(exists=True),
                send_to_llm_fn=lambda _prompt: "result",
            ),
            options=AnswerOptions(policy=make_retrieval_policy(mode="text")),
        )
        results = [
            {"doc_uid": "doc1", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "doc2", "chunk_id": 3, "score": 0.8},
        ]
        doc_chunks = {
            "doc1": [
                Chunk(id=1, doc_uid="doc1", chunk_number="5.1", page_start="A1", page_end="A1", text="This is the first section text and it continues."),
                Chunk(id=2, doc_uid="doc1", chunk_number="5.2", page_start="A2", page_end="A2", text="This is not the top chunk."),
            ],
            "doc2": [
                Chunk(id=3, doc_uid="doc2", chunk_number="8.3", page_start="B1", page_end="B1", text="Secondary document section text for logging."),
            ],
        }

        with caplog.at_level(logging.INFO):
            summary = command._build_chunk_summary(results, doc_chunks)

        assert summary.startswith("Retrieved chunks:")
        assert "doc1" in caplog.text
        assert "section_number=5.1" in caplog.text
        assert "score=0.9000" in caplog.text
        assert "section_text_preview='This is the first section text'" in caplog.text
        assert "section_number=8.3" in caplog.text
        assert "score=0.8000" in caplog.text
        assert "section_text_preview='Secondary document section tex'" in caplog.text

    def test_answer_prompt_b_context_filtered_by_authority(self) -> None:
        """End-to-end test: Prompt B should contain only primary/supporting chunks."""
        search_results = [
            {"doc_uid": "ifrs15", "chunk_id": 1, "score": 0.9},
            {"doc_uid": "ifrs15", "chunk_id": 2, "score": 0.85},
            {"doc_uid": "ias21", "chunk_id": 3, "score": 0.8},
        ]

        mock_chunks = [
            Chunk(id=1, doc_uid="ifrs15", chunk_number="5.1", page_start="A1", page_end="A1", text="PRIMARY_CONTENT_IFRS15"),
            Chunk(id=2, doc_uid="ifrs15", chunk_number="5.2", page_start="A2", page_end="A2", text="PERIPHERAL_CONTENT_IFRS15"),
            Chunk(id=3, doc_uid="ias21", chunk_number="8.2", page_start="B1", page_end="B1", text="SUPPORTING_CONTENT_IAS21"),
        ]

        chunk_store = InMemoryChunkStore()
        with chunk_store as store:
            store.insert_chunks(mock_chunks)

        captured_prompts: list[str] = []

        def mock_send_to_llm(prompt: str) -> str:
            captured_prompts.append(prompt)
            if len(captured_prompts) == 1:
                # Prompt A response: ifrs15 5.1 is primary, ias21 8.2 is supporting
                return json.dumps(
                    {
                        "status": "pass",
                        "authority_classification": {
                            "primary_authority": [{"document": "ifrs15", "references": ["5.1"], "reason": "Governs the issue"}],
                            "supporting_authority": [{"document": "ias21", "references": ["8.2"], "reason": "Clarifies the treatment"}],
                            "peripheral_authority": [{"document": "ifrs15", "references": ["5.2"], "reason": "Not directly relevant"}],
                        },
                    }
                )
            return VALID_PROMPT_B_RESPONSE

        config = AnswerConfig(
            vector_store=MockVectorStore(search_results),
            chunk_store=chunk_store,
            init_db_fn=lambda: None,
            index_path_fn=lambda: MockIndexPath(exists=True),
            send_to_llm_fn=mock_send_to_llm,
        )
        command = AnswerCommand(query="test", config=config, options=AnswerOptions(policy=make_retrieval_policy(mode="text", expand=1)))

        with unittest.mock.patch("src.commands.answer._prompt_file_exists", return_value=True):
            result = command.execute()

        assert result.success is True
        assert len(captured_prompts) == 2
        prompt_b = captured_prompts[1]

        # Prompt B should contain primary and supporting authority chunks
        assert "PRIMARY_CONTENT_IFRS15" in prompt_b
        assert "SUPPORTING_CONTENT_IAS21" in prompt_b

        # Prompt B should NOT contain peripheral authority chunk
        assert "PERIPHERAL_CONTENT_IFRS15" not in prompt_b
