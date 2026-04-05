"""Retrieval regression tests for IFRS Expert.

These tests verify that the retrieval behavior is consistent across changes.
They ingest the IFRS 16 leases document and query it to ensure expected results.
"""

import json
import tempfile

import pytest
from pathlib import Path

# PDF path for testing
IFRS16_LEASES_PDF = Path("examples/ifrs-16-leases_38-39.pdf")
DOC_UID = "ifrs-16-leases_38-39"


@pytest.fixture(scope="module")
def temp_index_dir():
    """Create a temporary directory for the FAISS index."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture(scope="module")
def ingested_ifrs16(temp_index_dir):
    """Ingest the IFRS 16 leases PDF for testing.

    This fixture runs once per test module and cleans up after all tests.
    """
    if not IFRS16_LEASES_PDF.exists():
        pytest.skip(f"PDF not found: {IFRS16_LEASES_PDF}")

    # Import here to ensure app is configured
    from src.commands.store import create_store_command
    from src.db import init_db
    from src.vector import VectorStore
    from src.vector.store import set_index_path
    from src.db import ChunkStore

    # Set temp index path for this test
    index_path = temp_index_dir / "faiss.index"
    set_index_path(index_path)

    # Initialize database
    init_db()

    # Ingest the PDF
    command = create_store_command(pdf_path=IFRS16_LEASES_PDF, doc_uid=DOC_UID)
    result = command.execute()
    assert not result.startswith("Error:"), f"Failed to ingest PDF: {result}"

    yield  # Tests run here

    # Cleanup: delete the document from DB and vector store
    with ChunkStore() as store:
        store.delete_chunks_by_doc(DOC_UID)

    with VectorStore() as vector_store:
        vector_store.delete_by_doc(DOC_UID)

    # Reset index path
    set_index_path(None)


def run_query(query: str, k: int = 5, min_score: float | None = None, expand: int = 0) -> list[dict]:
    """Run a query and return results.

    Args:
        query: Query text
        k: Number of results
        min_score: Minimum score threshold
        expand: Number of neighboring chunks to include

    Returns:
        List of result dictionaries
    """
    from src.commands.query import create_query_command
    from src.commands import QueryOptions

    command = create_query_command(
        query=query,
        options=QueryOptions(k=k, min_score=min_score, verbose=False, expand=expand),
    )
    result = command.execute()

    # Handle error results
    if result.startswith("Error:"):
        raise RuntimeError(f"Query failed: {result}")

    return json.loads(result)


class TestIFRS16Retrieval:
    """Regression tests for IFRS 16 leases retrieval."""

    def test_query_lease_definition(self, ingested_ifrs16):
        """Test query for 'lease definition' returns relevant results.

        This test verifies that searching for lease definition returns
        the correct section (likely B43 or nearby) with good score.
        """
        results = run_query("are payments for the right to use an underlying asset part of the cost of constructing the asset", k=1)

        assert len(results) > 0, "Expected at least one result"

        # Check top result
        top = results[0]

        # Score should be high (> 0.5) for a direct term match
        assert top["score"] > 0.5, f"Expected high score for 'lease definition', got {top['score']}"

        # Should be in the B43-B50 range (the leases paragraphs)
        section = top["chunk_number"]
        assert section == "B44", (
            f"Expected section B44, got {section}"
        )

    def test_query_has_low_relevance_when_non_sensical(self, ingested_ifrs16):
        # Use min_score=0 to get all results and verify they're low-scoring
        results = run_query("do cats eat dogs?", k=5, min_score=0)

        assert len(results) > 0, "Expected at least one result"

        top = results[0]

        # Score should be low but not zero
        assert top["score"] < 0.3, f"Expected low score for non-sensical query, got {top['score']}"

    def test_empty_query(self, ingested_ifrs16):
        """Test query returns error for empty query."""
        with pytest.raises(RuntimeError, match="Query failed: Error: Query cannot be empty"):
            run_query("", k=5)

    def test_whitespace_query(self, ingested_ifrs16):
        """Test query returns error for whitespace-only query."""
        with pytest.raises(RuntimeError, match="Query failed: Error: Query cannot be empty"):
            run_query(" \t \n ", k=5)
