"""Retrieval regression tests for IFRS Expert.

These tests verify that the retrieval behavior is consistent across changes.
They ingest the IFRS 16 leases document and query it to ensure expected results.
"""

import json
import tempfile
from pathlib import Path

import pytest


from tests.policy import load_test_policy_config, make_retrieval_policy, load_test_retrieval_policy

# HTML path for testing
HTML_INGESTION_PATH = Path("examples/ifrs/20260414T094610Z--ifrs-9-financial-instruments.html")
DOC_UID = "ifrs9"


@pytest.fixture(scope="module")
def temp_index_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    return tmp_path_factory.mktemp("index")


@pytest.fixture(scope="module")
def temp_db_path() -> Path:
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = Path(tmpdir) / "test.db"
        import src.db.connection as connection_module

        original_path = connection_module.DB_PATH
        connection_module.DB_PATH = db_path
        yield db_path
        connection_module.DB_PATH = original_path


@pytest.fixture(scope="module")
def ingested_ifrs16(temp_index_dir: Path, temp_db_path: Path):
    """Ingest the IFRS 9 HTML capture for testing.

    This fixture runs once per test module and cleans up after all tests.
    """
    if not HTML_INGESTION_PATH.exists():
        pytest.skip(f"HTML not found: {HTML_INGESTION_PATH}")

    del temp_db_path

    # Import here to ensure app is configured
    from src.commands.store import create_store_command
    from src.db import ChunkStore
    from src.db import init_db
    from src.vector import VectorStore
    from src.vector.store import set_index_path

    # Set temp index path for this test
    index_path = temp_index_dir / "faiss.index"
    set_index_path(index_path)

    # Initialize database
    init_db()

    # Ingest the HTML capture
    command = create_store_command(source_path=HTML_INGESTION_PATH, doc_uid=DOC_UID, scope="chunks")
    result = command.execute()
    assert not result.startswith("Error:"), f"Failed to ingest HTML: {result}"

    yield

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
        min_score: Minimum score threshold (None uses policy default)
        expand: Number of neighboring chunks to include

    Returns:
        List of result dictionaries
    """
    from src.commands.query import QueryOptions, create_query_command

    policy_kwargs: dict[str, object] = {}
    if k != 5:
        policy_kwargs["k"] = k
    if min_score is not None:
        policy_kwargs["chunk_min_score"] = min_score
    if expand != 0:
        policy_kwargs["expand"] = expand
    policy = make_retrieval_policy(**policy_kwargs) if policy_kwargs else load_test_retrieval_policy()

    command = create_query_command(
        query=query,
        options=QueryOptions(policy=policy, verbose=False),
    )
    result = command.execute()

    # Handle error results
    if result.startswith("Error:"):
        raise RuntimeError(f"Query failed: {result}")

    return json.loads(result)


class TestIFRS16Retrieval:
    """Regression tests for IFRS 16 leases retrieval."""

    def test_query_scope_returns_relevant_results(self, ingested_ifrs16):
        """Test query for the scope paragraph returns relevant results."""
        results = run_query("contracts to buy or sell a non-financial item that can be settled net in cash", k=1)

        assert len(results) > 0, "Expected at least one result"

        # Check top result
        top = results[0]

        # Score should be high (> 0.5) for a direct term match
        assert top["score"] > 0.5, f"Expected high score for the scope query, got {top['score']}"

        # Should be in the 2.6 range for the scope paragraph
        section = top["chunk_number"]
        assert section == "2.6", f"Expected section 2.6, got {section}"

    def test_query_has_low_relevance_when_non_sensical(self, ingested_ifrs16):
        # Use min_score=0 to get all results and verify they're low-scoring
        results = run_query("do cats eat dogs?", k=5, min_score=0)

        assert len(results) > 0, "Expected at least one result"

        top = results[0]

        # Score should be low but not zero
        assert top["score"] < 0.4, f"Expected low score for non-sensical query, got {top['score']}"

    def test_empty_query(self, ingested_ifrs16):
        """Test query returns error for empty query."""
        with pytest.raises(RuntimeError, match="Query failed: Error: Query cannot be empty"):
            run_query("", k=5)

    def test_whitespace_query(self, ingested_ifrs16):
        """Test query returns error for whitespace-only query."""
        with pytest.raises(RuntimeError, match="Query failed: Error: Query cannot be empty"):
            run_query(" \t \n ", k=5)
