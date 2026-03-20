"""Retrieval regression tests for IFRS Expert.

These tests verify that the retrieval behavior is consistent across changes.
They ingest the IFRS 16 leases document and query it to ensure expected results.
"""

import json

import pytest
from pathlib import Path

# PDF path for testing
IFRS16_LEASES_PDF = Path("examples/ifrs-16-leases_38-39.pdf")
DOC_UID = "ifrs-16-leases_38-39"


@pytest.fixture(scope="module")
def ingested_ifrs16():
    """Ingest the IFRS 16 leases PDF for testing.

    This fixture runs once per test module and cleans up after all tests.
    """
    if not IFRS16_LEASES_PDF.exists():
        pytest.skip(f"PDF not found: {IFRS16_LEASES_PDF}")

    # Import here to ensure app is configured
    from src.commands import StoreCommand
    from src.db import init_db
    from src.vector import VectorStore
    from src.db import ChunkStore

    # Initialize database
    init_db()

    # Ingest the PDF
    command = StoreCommand(pdf_path=IFRS16_LEASES_PDF, doc_uid=DOC_UID)
    result = command.execute()
    assert not result.startswith("Error:"), f"Failed to ingest PDF: {result}"

    yield  # Tests run here

    # Cleanup: delete the document from DB and vector store
    with ChunkStore() as store:
        store.delete_chunks_by_doc(DOC_UID)

    with VectorStore() as vector_store:
        vector_store.delete_by_doc(DOC_UID)


def run_query(query: str, k: int = 5, min_score: float | None = None) -> list[dict]:
    """Run a query and return results.

    Args:
        query: Query text
        k: Number of results
        min_score: Minimum score threshold

    Returns:
        List of result dictionaries
    """
    from src.commands import QueryCommand

    command = QueryCommand(query=query, k=k, min_score=min_score, verbose=False)
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
        results = run_query("lease definition", k=3)

        assert len(results) > 0, "Expected at least one result"

        # Check top result
        top = results[0]

        # Score should be high (> 0.5) for a direct term match
        assert top["score"] > 0.5, f"Expected high score for 'lease definition', got {top['score']}"

        # Should be in the B43-B50 range (the leases paragraphs)
        section = top["section_path"]
        assert section in ["B43", "B44", "B45", "B46", "B47", "B48", "B49", "B50"], (
            f"Expected section B43-B50, got {section}"
        )

    def test_query_variable_lease_payments(self, ingested_ifrs16):
        """Test query for 'variable lease payments' returns relevant results."""
        results = run_query("variable lease payments", k=3)

        assert len(results) > 0

        top = results[0]

        # Should find B48 or B49 which discuss variable payments
        section = top["section_path"]
        assert section in ["B48", "B49", "B50"], (
            f"Expected section about variable payments (B48-B50), got {section}"
        )

        # Score should be decent
        assert top["score"] > 0.4, f"Expected decent score for 'variable lease payments', got {top['score']}"

    def test_query_termination_options(self, ingested_ifrs16):
        """Test query for 'termination options' returns relevant results."""
        results = run_query("termination options", k=3)

        assert len(results) > 0

        top = results[0]

        # B50 discusses extension and termination options
        section = top["section_path"]
        assert section == "B50", f"Expected B50 for termination options, got {section}"

        # Should have good score
        assert top["score"] > 0.3, f"Expected reasonable score for 'termination options', got {top['score']}"

    def test_query_leaseback_transaction(self, ingested_ifrs16):
        """Test query for 'sale and leaseback' returns relevant results."""
        results = run_query("sale and leaseback transaction", k=3)

        assert len(results) > 0

        top = results[0]

        # B46 discusses sale and leaseback
        section = top["section_path"]
        assert section == "B46", f"Expected B46 for sale and leaseback, got {section}"

    def test_page_numbers_correct(self, ingested_ifrs16):
        """Test that retrieved chunks have correct page numbers."""
        results = run_query("lease", k=1)

        assert len(results) > 0

        top = results[0]

        # Should have page info
        assert top["page_start"] is not None
        assert top["page_end"] is not None


# Example of how to add more tests:
# Just add another method to TestIFRS16Retrieval class following the pattern above.
# Each test should:
# 1. Call run_query() with your query
# 2. Assert on top["section_path"], top["page_start"], and/or top["score"]
