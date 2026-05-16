"""Integration tests for end-to-end ingestion."""

from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from src.commands.ingest import IngestCommand
from src.commands.store import StoreCommandOptions, StoreDependencies, create_store_command
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


def _require_example_file(name: str) -> Path:
    path = _example_file(name)
    if not path.exists():
        pytest.skip(f"Fixture not available in this worktree: {name}")
    return path


def _write_html_sidecar(
    sidecar_path: Path,
    canonical_url: str,
    title: str,
    source_domain: str = "www.ifrs.org",
    document_type: str | None = None,
    url: str | None = None,
) -> None:
    payload: dict[str, str] = {
        "url": url or canonical_url,
        "title": title,
        "captured_at": "2026-04-04T14:23:10Z",
        "source_domain": source_domain,
        "canonical_url": canonical_url,
    }
    if document_type is not None:
        payload["document_type"] = document_type
    sidecar_path.write_text(json.dumps(payload), encoding="utf-8")


def _extract_ifrs_sidecar_payload(html_path: Path) -> dict[str, str]:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    canonical_tag = soup.select_one('link[rel="canonical"]')
    identifier_tag = soup.select_one('meta[name="DC.Identifier"]')
    checked_input = soup.select_one('input[name="documentType"][checked]')
    if canonical_tag is None or identifier_tag is None or checked_input is None:
        raise AssertionError(f"Expected IFRS metadata in {html_path}")

    shell_canonical_url = str(canonical_tag.get("href", "")).strip()
    variant_value = str(checked_input.get("value", "")).strip()
    variant_label_node = checked_input.find_next_sibling("span")
    variant_label = variant_label_node.get_text(" ", strip=True) if variant_label_node is not None else "Standard"
    doc_uid = str(identifier_tag.get("content", "")).strip()
    shell_title = soup.title.get_text(" ", strip=True) if soup.title is not None else doc_uid

    if variant_label == "Standard":
        title = shell_title
    else:
        title = f"{shell_title} - {variant_label}"

    if doc_uid.startswith("ifrs"):
        document_type = {
            "Standard": "IFRS-S",
            "Basis for Conclusions": "IFRS-BC",
            "Illustrative Examples": "IFRS-IE",
            "Implementation Guidance": "IFRS-IG",
        }[variant_label]
    elif doc_uid.startswith("ias"):
        document_type = {
            "Standard": "IAS-S",
            "Basis for Conclusions": "IAS-BC",
            "Basis for Conclusions IASC": "IAS-BCIASC",
            "Supporting Materials": "IAS-SM",
            "Illustrative Examples": "IAS-IE",
            "Implementation Guidance": "IAS-IG",
        }[variant_label]
    elif doc_uid.startswith("ifric"):
        document_type = "IFRIC"
    elif doc_uid.startswith("sic"):
        document_type = "SIC"
    else:
        document_type = "PS"

    return {
        "url": f"https://www.ifrs.org/content/ifrs/home/issued-standards/list-of-standards/{html_path.stem}.html{variant_value.removesuffix('.html')}/",
        "title": title,
        "canonical_url": f"{shell_canonical_url}{variant_value}",
        "document_type": document_type,
    }


def _store_factory(
    source_path: Path,
    extractor: object,
    options: StoreCommandOptions | None = None,
):
    global chunk_store, document_store
    _stores.setdefault("chunk_store", InMemoryChunkStore())
    _stores.setdefault("document_store", InMemoryDocumentStore())
    _stores.setdefault("section_store", InMemorySectionStore())
    _stores.setdefault("vector_store", RecordingVectorStore())
    _stores.setdefault("title_vector_store", RecordingTitleVectorStore())
    chunk_store = _stores["chunk_store"]
    document_store = _stores["document_store"]
    vector_store = _stores["vector_store"]
    title_vector_store = _stores["title_vector_store"]
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
        dependencies=dependencies,
        options=options,
    )


# Module-level mutable container for in-memory stores set by _store_factory
_stores: dict[str, object] = {}
chunk_store: InMemoryChunkStore | None = None
document_store: InMemoryDocumentStore | None = None


def test_ingest_command_imports_html_capture_pair(temp_db_path: Path, capture_root: Path) -> None:
    """Representative IFRS HTML captures should ingest into the database and processed/."""
    del temp_db_path
    html_source = _example_file("IFRS/20260414T094554Z--ifrs-9-financial-instruments.html")
    json_source = _example_file("IFRS/20260414T094554Z--ifrs-9-financial-instruments.json")
    expected_sidecar = json.loads(json_source.read_text(encoding="utf-8"))
    inbox_html = capture_root / "20260414T094554Z--ifrs-9-financial-instruments.html"
    inbox_json = capture_root / "20260414T094554Z--ifrs-9-financial-instruments.json"
    shutil.copy(html_source, inbox_html)
    shutil.copy(json_source, inbox_json)

    command = IngestCommand(capture_root=capture_root, store_command_factory=_store_factory)

    output = command.execute()

    assert "1 imported" in output
    assert (capture_root / "processed" / inbox_html.name).exists()
    assert (capture_root / "processed" / inbox_json.name).exists()
    with document_store as ds:
        document = ds.get_document("ifrs9")
    assert document is not None, "Expected HTML ingestion to upsert a document record"
    assert document.source_type == "html"
    assert document.document_type == "IFRS-S"
    assert document.canonical_url == expected_sidecar["canonical_url"]
    with chunk_store as cs:
        chunks = cs.get_chunks_by_doc("ifrs9")
    assert any(chunk.chunk_number == "2.4" for chunk in chunks)
    assert any(chunk.chunk_number == "E19" for chunk in chunks)
    assert any(chunk.chunk_id == "IFRS09_2.4" for chunk in chunks)


def test_ingest_command_imports_navis_html_capture_pair(temp_db_path: Path, capture_root: Path) -> None:
    """Representative Navis HTML captures should ingest into the database and processed/."""
    del temp_db_path
    html_source = _require_example_file("Lefebvre-Navis/20260412T190029Z--document.html")
    json_source = _require_example_file("Lefebvre-Navis/20260412T190029Z--document.json")
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
    assert any(chunk.chunk_number == "12501" for chunk in chunks)
    assert any(chunk.chunk_id == "P8A8E6F292F99E-EFL" for chunk in chunks)


def test_ingest_command_imports_navis_chapter_bundle_capture_pair(temp_db_path: Path, capture_root: Path) -> None:
    """Synthetic Navis chapter bundles should ingest as one chapter-level document."""
    del temp_db_path
    html_source = _require_example_file("Lefebvre-Navis/20260412T190029Z--document.html")
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
    assert any(chunk.chunk_number == "12501" for chunk in chunks)
    assert any(chunk.chunk_id == "P8A8E6F292F99E-EFL" for chunk in chunks)


def test_ingest_command_skips_unchanged_html_and_replaces_changed_html(temp_db_path: Path, capture_root: Path) -> None:
    """HTML captures should skip when unchanged and replace existing chunks when changed."""
    del temp_db_path
    html_source = _example_file("www.ifrs.org__issued-standards__list-of-standards__ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html__content__dam__ifrs__publications__html-standards__english__2026__issued__ifric16.html")

    first_html = capture_root / "20260404T142310Z--ifric16.html"
    first_json = capture_root / "20260404T142310Z--ifric16.json"
    shutil.copy(html_source, first_html)
    first_sidecar = _extract_ifrs_sidecar_payload(first_html)
    _write_html_sidecar(
        first_json,
        canonical_url=first_sidecar["canonical_url"],
        title=first_sidecar["title"],
        document_type=first_sidecar["document_type"],
        url=first_sidecar["url"],
    )

    command = IngestCommand(capture_root=capture_root, store_command_factory=_store_factory)
    first_output = command.execute()
    assert "1 imported" in first_output

    second_html = capture_root / "20260405T142310Z--ifric16.html"
    second_json = capture_root / "20260405T142310Z--ifric16.json"
    shutil.copy(html_source, second_html)
    _write_html_sidecar(
        second_json,
        canonical_url=first_sidecar["canonical_url"],
        title=first_sidecar["title"],
        document_type=first_sidecar["document_type"],
        url=first_sidecar["url"],
    )

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
    _write_html_sidecar(
        third_json,
        canonical_url=first_sidecar["canonical_url"],
        title=first_sidecar["title"],
        document_type=first_sidecar["document_type"],
        url=first_sidecar["url"],
    )

    replace_output = command.execute()

    assert "1 imported" in replace_output
    with chunk_store as cs:
        chunks = cs.get_chunks_by_doc("ifric16")
    first_chunk = next(chunk for chunk in chunks if chunk.chunk_number == "1")
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
