"""Integration tests for end-to-end ingestion."""

from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from src.commands.ingest import IngestCommand
from src.commands.store import StoreDependencies, create_store_command
from tests.fakes import InMemoryChunkStore, InMemoryDocumentStore, InMemorySectionStore, RecordingTitleVectorStore, RecordingVectorStore


@pytest.fixture
def temp_db_path() -> Path:
    """Patch the global DB path to an isolated temporary database."""
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        import src.db.connection as connection_module

        original_path = connection_module.DB_PATH
        connection_module.DB_PATH = db_path
        yield db_path
        connection_module.DB_PATH = original_path


@pytest.fixture
def capture_root(tmp_path: Path) -> Path:
    """Create the ingest directory layout."""
    root = tmp_path / "ifrs-expert"
    root.mkdir(parents=True)
    (root / "processed").mkdir()
    (root / "failed").mkdir()
    (root / "skipped").mkdir()
    return root


def _example_file(name: str) -> Path:
    examples_dir = Path(__file__).parent.parent.parent / "examples"
    return examples_dir / name


def _write_html_sidecar(sidecar_path: Path, canonical_url: str, title: str, source_domain: str = "www.ifrs.org") -> None:
    sidecar_path.write_text(
        json.dumps(
            {
                "url": canonical_url,
                "title": title,
                "captured_at": "2026-04-04T14:23:10Z",
                "source_domain": source_domain,
                "canonical_url": canonical_url,
            }
        ),
        encoding="utf-8",
    )


def _extract_canonical_url(html_path: Path) -> str:
    html_text = html_path.read_text(encoding="utf-8")
    canonical_prefix = '<link rel="canonical"\n    href="'
    start = html_text.index(canonical_prefix) + len(canonical_prefix)
    end = html_text.index('">', start)
    return html_text[start:end]


def _store_factory(source_path: Path, extractor: object, explicit_doc_uid: str | None, scope: str):
    global chunk_store, document_store
    _stores.setdefault("chunk_store", InMemoryChunkStore())
    _stores.setdefault("document_store", InMemoryDocumentStore())
    _stores.setdefault("section_store", InMemorySectionStore())
    chunk_store = _stores["chunk_store"]
    document_store = _stores["document_store"]
    vector_store = RecordingVectorStore()
    title_vector_store = RecordingTitleVectorStore()
    dependencies = StoreDependencies(
        chunk_store=_stores["chunk_store"],
        document_store=_stores["document_store"],
        section_store=_stores["section_store"],
        vector_store=vector_store,
        title_vector_store=title_vector_store,
        init_db_fn=lambda: None,
    )
    return create_store_command(
        source_path=source_path,
        extractor=extractor,
        doc_uid=explicit_doc_uid,
        dependencies=dependencies,
        scope=scope,
    )


# Module-level mutable container for in-memory stores set by _store_factory
_stores: dict[str, InMemoryChunkStore | InMemoryDocumentStore | InMemorySectionStore] = {}
chunk_store: InMemoryChunkStore | None = None
document_store: InMemoryDocumentStore | None = None


def test_ingest_command_imports_pdf_from_capture_root(temp_db_path: Path, capture_root: Path) -> None:
    """PDF files in the capture root should be imported and archived to processed/."""
    del temp_db_path
    inbox_pdf = capture_root / "ifrs-16-leases_38-39.pdf"
    shutil.copy(_example_file("ifrs-16-leases_38-39.pdf"), inbox_pdf)

    command = IngestCommand(capture_root=capture_root, store_command_factory=_store_factory)

    output = command.execute()

    assert "1 imported" in output
    assert (capture_root / "processed" / inbox_pdf.name).exists()
    with document_store as ds:
        document = ds.get_document("ifrs-16-leases_38-39")
    assert document is not None, "Expected PDF ingestion to upsert a document record"
    assert document.source_type == "pdf"
    with chunk_store as cs:
        chunks = cs.get_chunks_by_doc("ifrs-16-leases_38-39")
    assert chunks, "Expected stored PDF chunks after ingestion"


def test_ingest_command_imports_html_capture_pair(temp_db_path: Path, capture_root: Path) -> None:
    """Representative IFRS HTML captures should ingest into the database and processed/."""
    del temp_db_path
    html_source = _example_file("www.ifrs.org__issued-standards__list-of-standards__ifrs-9-financial-instruments.html__content__dam__ifrs__publications__html-standards__english__2026__issued__ifrs9.html")
    inbox_html = capture_root / "20260404T142310Z--ifrs9.html"
    inbox_json = capture_root / "20260404T142310Z--ifrs9.json"
    shutil.copy(html_source, inbox_html)
    canonical_url = _extract_canonical_url(inbox_html)
    _write_html_sidecar(inbox_json, canonical_url=canonical_url, title="IFRS 9")

    command = IngestCommand(capture_root=capture_root, store_command_factory=_store_factory)

    output = command.execute()

    assert "1 imported" in output
    assert (capture_root / "processed" / inbox_html.name).exists()
    assert (capture_root / "processed" / inbox_json.name).exists()
    with document_store as ds:
        document = ds.get_document("ifrs9")
    assert document is not None, "Expected HTML ingestion to upsert a document record"
    assert document.source_type == "html"
    assert document.canonical_url == canonical_url
    with chunk_store as cs:
        chunks = cs.get_chunks_by_doc("ifrs9")
    assert any(chunk.section_path == "2.4" for chunk in chunks)
    assert any(chunk.source_anchor == "IFRS09_2.4" for chunk in chunks)


def test_ingest_command_imports_navis_html_capture_pair(temp_db_path: Path, capture_root: Path) -> None:
    """Representative Navis HTML captures should ingest into the database and processed/."""
    del temp_db_path
    html_source = _example_file("Lefebvre-Navis/20260412T190029Z--document.html")
    json_source = _example_file("Lefebvre-Navis/20260412T190029Z--document.json")
    inbox_html = capture_root / "20260412T190029Z--document.html"
    inbox_json = capture_root / "20260412T190029Z--document.json"
    shutil.copy(html_source, inbox_html)
    shutil.copy(json_source, inbox_json)

    command = IngestCommand(capture_root=capture_root, store_command_factory=_store_factory)

    output = command.execute()

    assert "1 imported" in output
    assert (capture_root / "processed" / inbox_html.name).exists()
    assert (capture_root / "processed" / inbox_json.name).exists()
    with document_store as ds:
        document = ds.get_document("navis-QRIFRS-C2A8E6F292F99E-EFL")
    assert document is not None, "Expected Navis ingestion to upsert a document record"
    assert document.source_type == "html"
    assert document.source_domain == "abonnes.efl.fr"
    assert document.document_type == "NAVIS"
    with chunk_store as cs:
        chunks = cs.get_chunks_by_doc("navis-QRIFRS-C2A8E6F292F99E-EFL")
    assert any(chunk.section_path == "12501" for chunk in chunks)
    assert any(chunk.source_anchor == "P8A8E6F292F99E-EFL" for chunk in chunks)


def test_ingest_command_imports_navis_chapter_bundle_capture_pair(temp_db_path: Path, capture_root: Path) -> None:
    """Synthetic Navis chapter bundles should ingest as one chapter-level document."""
    del temp_db_path
    html_source = _example_file("Lefebvre-Navis/20260412T190029Z--document.html")
    soup = BeautifulSoup(html_source.read_text(encoding="utf-8"), "html.parser")
    content_root = soup.select_one("#documentContent .question.question-export")
    assert content_root is not None, "Expected Navis example to contain the content root"

    inbox_html = capture_root / "20260413T120000Z--navis-QRIFRS-C2A8E6F292F99E-EFL--CHAPITRE_4.html"
    inbox_json = capture_root / "20260413T120000Z--navis-QRIFRS-C2A8E6F292F99E-EFL--CHAPITRE_4.json"
    manifest_payload = {
        "chapter_ref_id": "C2A8E6F292F99E-EFL",
        "chapter_title": "CHAPITRE 4 Cadre conceptuel de l'information financière (Cadre conceptuel de l'IASB)",
        "product_key": "QRIFRS",
        "page_ref_ids": ["P8A8E6F292F99E-EFL"],
        "page_titles": ["Généralités"],
    }
    manifest_json = json.dumps(manifest_payload)
    inbox_html.write_text(
        """
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8">
            <title>CHAPITRE 4 Cadre conceptuel de l'information financière (Cadre conceptuel de l'IASB)</title>
          </head>
          <body>
            <script id="ifrs-expert-navis-manifest" type="application/json">"""
        + manifest_json
        + """</script>
            <div id="ifrs-expert-navis-bundle" data-chapter-ref-id="C2A8E6F292F99E-EFL">
              <section class="ifrs-expert-navis-page" data-page-ref-id="P8A8E6F292F99E-EFL" data-page-title="Généralités">
                """
        + str(content_root)
        + """
              </section>
            </div>
          </body>
        </html>
        """,
        encoding="utf-8",
    )
    inbox_json.write_text(
        json.dumps(
            {
                "url": "https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&uaId=000K&refId=C2A8E6F292F99E-EFL",
                "title": "CHAPITRE 4 Cadre conceptuel de l'information financière (Cadre conceptuel de l'IASB)",
                "captured_at": "2026-04-13T12:00:00Z",
                "source_domain": "abonnes.efl.fr",
                "canonical_url": "https://abonnes.efl.fr/EFL2/document/?key=QRIFRS&uaId=000K&refId=C2A8E6F292F99E-EFL",
                "capture_format": "navis-chapter-bundle/v1",
                "capture_mode": "chapter",
                "product_key": "QRIFRS",
                "root_ref_id": "N24F9F491387ED-EFL",
                "chapter_ref_id": "C2A8E6F292F99E-EFL",
                "chapter_title": "CHAPITRE 4 Cadre conceptuel de l'information financière (Cadre conceptuel de l'IASB)",
                "page_ref_ids": ["P8A8E6F292F99E-EFL"],
                "page_titles": ["Généralités"],
            }
        ),
        encoding="utf-8",
    )

    command = IngestCommand(capture_root=capture_root, store_command_factory=_store_factory)

    output = command.execute()

    assert "1 imported" in output
    with document_store as ds:
        document = ds.get_document("navis-QRIFRS-C2A8E6F292F99E-EFL")
    assert document is not None, "Expected chapter bundle ingestion to upsert a document record"
    with chunk_store as cs:
        chunks = cs.get_chunks_by_doc("navis-QRIFRS-C2A8E6F292F99E-EFL")
    assert any(chunk.section_path == "12501" for chunk in chunks)
    assert any(chunk.source_anchor == "P8A8E6F292F99E-EFL" for chunk in chunks)


def test_ingest_command_skips_unchanged_html_and_replaces_changed_html(temp_db_path: Path, capture_root: Path) -> None:
    """HTML captures should skip when unchanged and replace existing chunks when changed."""
    del temp_db_path
    html_source = _example_file("www.ifrs.org__issued-standards__list-of-standards__ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html__content__dam__ifrs__publications__html-standards__english__2026__issued__ifric16.html")

    first_html = capture_root / "20260404T142310Z--ifric16.html"
    first_json = capture_root / "20260404T142310Z--ifric16.json"
    shutil.copy(html_source, first_html)
    canonical_url = _extract_canonical_url(first_html)
    _write_html_sidecar(first_json, canonical_url=canonical_url, title="IFRIC 16")

    command = IngestCommand(capture_root=capture_root, store_command_factory=_store_factory)
    first_output = command.execute()
    assert "1 imported" in first_output

    second_html = capture_root / "20260405T142310Z--ifric16.html"
    second_json = capture_root / "20260405T142310Z--ifric16.json"
    shutil.copy(html_source, second_html)
    _write_html_sidecar(second_json, canonical_url=canonical_url, title="IFRIC 16")

    skip_output = command.execute()

    assert "1 skipped" in skip_output
    assert (capture_root / "skipped" / second_html.name).exists()
    assert (capture_root / "skipped" / second_json.name).exists()

    third_html = capture_root / "20260406T142310Z--ifric16.html"
    third_json = capture_root / "20260406T142310Z--ifric16.json"
    soup = BeautifulSoup(html_source.read_text(encoding="utf-8"), "html.parser")
    paragraph = soup.select_one("div.topic.paragraph#IFRIC16_1 td.paragraph_col2 > .body > p")
    assert paragraph is not None, "Expected to locate the first IFRIC 16 paragraph"
    paragraph.append(" Additional integration test sentence.")
    third_html.write_text(str(soup), encoding="utf-8")
    _write_html_sidecar(third_json, canonical_url=canonical_url, title="IFRIC 16")

    replace_output = command.execute()

    assert "1 imported" in replace_output
    with chunk_store as cs:
        chunks = cs.get_chunks_by_doc("ifric16")
    first_chunk = next(chunk for chunk in chunks if chunk.section_path == "1")
    assert "Additional integration test sentence." in first_chunk.text


def test_ingest_command_moves_invalid_html_to_failed(temp_db_path: Path, capture_root: Path) -> None:
    """Invalid HTML sidecars should be archived under failed/."""
    del temp_db_path
    bad_html = capture_root / "20260404T142310Z--broken.html"
    bad_json = capture_root / "20260404T142310Z--broken.json"
    bad_html.write_text("<html></html>", encoding="utf-8")
    bad_json.write_text("{not valid json}", encoding="utf-8")

    command = IngestCommand(capture_root=capture_root, store_command_factory=_store_factory)

    output = command.execute()

    assert "1 failed" in output
    assert "invalid sidecar JSON" in output
    assert (capture_root / "failed" / bad_html.name).exists()
    assert (capture_root / "failed" / bad_json.name).exists()
