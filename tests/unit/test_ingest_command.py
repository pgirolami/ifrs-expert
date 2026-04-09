"""Tests for the ingest command."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from src.commands.ingest import IngestCommand, SharedDependenciesStoreCommandFactory
from src.commands.store import StoreCommandResult, StoreDependencies


@dataclass
class FakeStoreCommand:
    """Fake store command returning a prepared result."""

    result: StoreCommandResult

    def execute_result(self) -> StoreCommandResult:
        return self.result


class RecordingStoreFactory:
    """Factory that records requested source paths and returns prepared results."""

    def __init__(self, results_by_name: dict[str, StoreCommandResult]) -> None:
        self._results_by_name = results_by_name
        self.calls: list[tuple[str, str, str]] = []

    def __call__(self, source_path: Path, extractor: object, explicit_doc_uid: str | None, scope: str) -> FakeStoreCommand:
        del explicit_doc_uid
        self.calls.append((source_path.name, type(extractor).__name__, scope))
        return FakeStoreCommand(result=self._results_by_name[source_path.name])


class FakeCreateStoreCommand:
    """Record the dependencies passed by the shared ingest store factory."""

    def __init__(self) -> None:
        self.dependencies_by_source_name: list[tuple[str, StoreDependencies, str]] = []

    def __call__(
        self,
        source_path: Path | None = None,
        doc_uid: str | None = None,
        extractor: object | None = None,
        dependencies: StoreDependencies | None = None,
        pdf_path: Path | None = None,
        scope: str = "all",
    ) -> FakeStoreCommand:
        del doc_uid, extractor, pdf_path
        assert scope in {"all", "chunks", "sections", "documents"}
        assert source_path is not None, "Expected a source path"
        assert dependencies is not None, "Expected shared dependencies to be provided"
        self.dependencies_by_source_name.append((source_path.name, dependencies, scope))
        return FakeStoreCommand(result=StoreCommandResult(status="stored", doc_uid=source_path.stem, chunk_count=1, embedding_count=1))


class TestIngestCommand:
    """Tests for ingest discovery, validation, and archiving."""

    def test_shared_dependencies_factory_reuses_one_dependency_bundle(self, tmp_path: Path) -> None:
        """The default ingest factory should reuse the same store dependencies across files."""
        source_one = tmp_path / "first.pdf"
        source_two = tmp_path / "second.pdf"
        source_one.write_text("pdf", encoding="utf-8")
        source_two.write_text("pdf", encoding="utf-8")

        dependencies = StoreDependencies(
            chunk_store=object(),
            document_store=object(),
            section_store=None,
            vector_store=object(),
            title_vector_store=None,
            init_db_fn=lambda: None,
        )
        fake_create_store_command = FakeCreateStoreCommand()
        factory = SharedDependenciesStoreCommandFactory(
            dependencies=dependencies,
            create_store_command_fn=fake_create_store_command,
        )

        factory(source_one, extractor=object(), explicit_doc_uid=None, scope="documents")
        factory(source_two, extractor=object(), explicit_doc_uid=None, scope="documents")

        recorded_dependencies = [recorded_dependency for _source_name, recorded_dependency, _scope in fake_create_store_command.dependencies_by_source_name]
        assert recorded_dependencies == [dependencies, dependencies]
        assert recorded_dependencies[0] is recorded_dependencies[1]
        assert [scope for _source_name, _recorded_dependency, scope in fake_create_store_command.dependencies_by_source_name] == [
            "documents",
            "documents",
        ]

    def test_ingest_discovers_html_pairs_and_pdfs_while_ignoring_part_files(self, tmp_path: Path) -> None:
        """Only complete final files should be ingested."""
        capture_root = tmp_path / "ifrs-expert"
        capture_root.mkdir(parents=True)
        (capture_root / "processed").mkdir()
        (capture_root / "failed").mkdir()
        (capture_root / "skipped").mkdir()

        html_path = capture_root / "20260404T142310Z--ifrs-9.html"
        json_path = capture_root / "20260404T142310Z--ifrs-9.json"
        pdf_path = capture_root / "ifrs-16.pdf"
        html_path.write_text(
            '<html><head><link rel="canonical" href="https://www.ifrs.org/ifrs9.html"><meta name="DC.Identifier" content="ifrs9"></head><body><section class="ifrs-cmp-htmlviewer__section"></section></body></html>',
            encoding="utf-8",
        )
        json_path.write_text(
            json.dumps(
                {
                    "url": "https://www.ifrs.org/ifrs9.html",
                    "title": "IFRS 9",
                    "captured_at": "2026-04-04T14:23:10Z",
                    "source_domain": "www.ifrs.org",
                    "canonical_url": "https://www.ifrs.org/ifrs9.html",
                }
            ),
            encoding="utf-8",
        )
        pdf_path.write_text("pdf", encoding="utf-8")
        (capture_root / "ignore-me.html.part").write_text("partial", encoding="utf-8")
        (capture_root / "ignore-me.json.part").write_text("partial", encoding="utf-8")
        (capture_root / "ignore-me.pdf.part").write_text("partial", encoding="utf-8")

        store_factory = RecordingStoreFactory(
            results_by_name={
                html_path.name: StoreCommandResult(status="stored", doc_uid="ifrs9", chunk_count=2, embedding_count=2),
                pdf_path.name: StoreCommandResult(status="stored", doc_uid="ifrs-16", chunk_count=3, embedding_count=3),
            }
        )
        command = IngestCommand(capture_root=capture_root, store_command_factory=store_factory)

        output = command.execute()

        assert "Processed 2 item(s): 2 imported, 0 skipped, 0 failed" in output
        assert store_factory.calls == [
            (html_path.name, "HtmlExtractor", "all"),
            (pdf_path.name, "PdfExtractor", "all"),
        ]
        assert (capture_root / "ignore-me.html.part").exists(), "The command must not move .part files"
        assert (capture_root / "processed" / html_path.name).exists()
        assert (capture_root / "processed" / json_path.name).exists()
        assert (capture_root / "processed" / pdf_path.name).exists()
        assert (capture_root / "ignore-me.html.part").exists()
        assert (capture_root / "ignore-me.json.part").exists()
        assert (capture_root / "ignore-me.pdf.part").exists()

    def test_ingest_moves_invalid_html_capture_to_failed(self, tmp_path: Path) -> None:
        """HTML captures with invalid sidecars should fail before StoreCommand runs."""
        capture_root = tmp_path / "ifrs-expert"
        capture_root.mkdir(parents=True)
        (capture_root / "processed").mkdir()
        (capture_root / "failed").mkdir()
        (capture_root / "skipped").mkdir()

        html_path = capture_root / "20260404T142310Z--broken.html"
        json_path = capture_root / "20260404T142310Z--broken.json"
        html_path.write_text("<html></html>", encoding="utf-8")
        json_path.write_text("{not valid json}", encoding="utf-8")

        store_factory = RecordingStoreFactory(results_by_name={})
        command = IngestCommand(capture_root=capture_root, store_command_factory=store_factory)

        output = command.execute()

        assert "Processed 1 item(s): 0 imported, 0 skipped, 1 failed" in output
        assert "invalid sidecar JSON" in output
        assert store_factory.calls == []
        assert (capture_root / "failed" / html_path.name).exists()
        assert (capture_root / "failed" / json_path.name).exists()

    def test_ingest_moves_unchanged_html_capture_to_skipped(self, tmp_path: Path) -> None:
        """Unchanged HTML captures should be archived under skipped/."""
        capture_root = tmp_path / "ifrs-expert"
        capture_root.mkdir(parents=True)
        (capture_root / "processed").mkdir()
        (capture_root / "failed").mkdir()
        (capture_root / "skipped").mkdir()

        html_path = capture_root / "20260404T142310Z--ifrs-9.html"
        json_path = capture_root / "20260404T142310Z--ifrs-9.json"
        html_path.write_text(
            '<html><head><link rel="canonical" href="https://www.ifrs.org/ifrs9.html"><meta name="DC.Identifier" content="ifrs9"></head><body><section class="ifrs-cmp-htmlviewer__section"></section></body></html>',
            encoding="utf-8",
        )
        json_path.write_text(
            json.dumps(
                {
                    "url": "https://www.ifrs.org/ifrs9.html",
                    "title": "IFRS 9",
                    "captured_at": "2026-04-04T14:23:10Z",
                    "source_domain": "www.ifrs.org",
                    "canonical_url": "https://www.ifrs.org/ifrs9.html",
                }
            ),
            encoding="utf-8",
        )

        store_factory = RecordingStoreFactory(
            results_by_name={
                html_path.name: StoreCommandResult(
                    status="skipped",
                    doc_uid="ifrs9",
                    chunk_count=12,
                    embedding_count=0,
                    reason="unchanged content",
                )
            }
        )
        command = IngestCommand(capture_root=capture_root, store_command_factory=store_factory, scope="documents")

        output = command.execute()

        assert "Processed 1 item(s): 0 imported, 1 skipped, 0 failed" in output
        assert "Skipped: https://www.ifrs.org/ifrs9.html (unchanged content)" in output
        assert store_factory.calls == [(html_path.name, "HtmlExtractor", "documents")]
        assert (capture_root / "skipped" / html_path.name).exists()
        assert (capture_root / "skipped" / json_path.name).exists()
