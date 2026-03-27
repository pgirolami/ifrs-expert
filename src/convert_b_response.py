"""B-response converter - convert B-response.md (JSON) to formatted French markdown."""

import argparse
import json
import logging
import re
import sys
from pathlib import Path

from src.b_response_utils import convert_json_to_markdown
from src.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


def extract_question_from_prompt(prompt_path: Path) -> str | None:
    """Extract the question from an A-prompt.txt file.

    Args:
        prompt_path: Path to A-prompt.txt

    Returns:
        The extracted question or None if not found
    """
    if not prompt_path.exists():
        return None

    content = prompt_path.read_text(encoding="utf-8")

    # Find the question after "Question:" in the content
    match = re.search(r"Question:\s*(.+?)(?:\n\n|\n<|\Z)", content, re.DOTALL)
    if match:
        # Clean up the question - decode HTML entities and normalize
        question = match.group(1).strip()
        question = question.replace("&#39;", "'").replace("&amp;", "&")
        return question

    return None


def extract_doc_uids_from_prompt(prompt_path: Path) -> list[str]:
    """Extract document UIDs from an A-prompt.txt file.

    Args:
        prompt_path: Path to A-prompt.txt

    Returns:
        List of document UIDs
    """
    if not prompt_path.exists():
        return []

    content = prompt_path.read_text(encoding="utf-8")

    # Find all <Document name="..."> tags
    matches = re.findall(r'<Document name="([^"]+)">', content)
    return list(dict.fromkeys(matches))  # Preserve order, remove duplicates


def convert_file(input_path: Path, output_dir: Path | None = None) -> None:
    """Convert a B-response.md file to JSON + French markdown.

    Args:
        input_path: Path to the B-response.md file (contains JSON)
        output_dir: Optional output directory (default: same as input)
    """
    if not input_path.exists():
        msg = f"Input file not found: {input_path}"
        raise FileNotFoundError(msg)

    # Determine the run directory (parent of B-response.md)
    run_dir = input_path.parent

    # Try to extract question and doc UIDs from A-prompt.txt in the same directory
    prompt_a_path = run_dir / "A-prompt.txt"
    question = extract_question_from_prompt(prompt_a_path)
    doc_uids = extract_doc_uids_from_prompt(prompt_a_path)

    if question:
        logger.info(f"Extracted question from A-prompt.txt: {question[:50]}...")
    if doc_uids:
        logger.info(f"Extracted {len(doc_uids)} document UIDs from A-prompt.txt")

    # Read the JSON content from the file
    content = input_path.read_text(encoding="utf-8").strip()

    # Parse JSON
    try:
        b_json = json.loads(content)
    except json.JSONDecodeError as e:
        msg = f"Invalid JSON in {input_path}: {e}"
        raise ValueError(msg) from e

    # Determine output directory
    if output_dir is None:
        output_dir = run_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write formatted JSON to B-response.json
    json_path = output_dir / "B-response.json"
    json_path.write_text(json.dumps(b_json, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info(f"Wrote: {json_path}")

    # Convert to French markdown and write to B-response.md
    markdown_content = convert_json_to_markdown(b_json, question=question, doc_uids=doc_uids)
    md_path = output_dir / "B-response.md"
    md_path.write_text(markdown_content, encoding="utf-8")
    logger.info(f"Wrote: {md_path}")


def convert_directory(dir_path: Path) -> None:
    """Convert all B-response.md files in a directory.

    Args:
        dir_path: Path to directory containing B-response.md files
    """
    if not dir_path.is_dir():
        msg = f"Not a directory: {dir_path}"
        raise ValueError(msg)

    # Find all B-response.md files
    b_response_files = list(dir_path.glob("**/B-response.md"))

    if not b_response_files:
        logger.warning(f"No B-response.md files found in {dir_path}")
        return

    logger.info(f"Found {len(b_response_files)} B-response.md file(s)")

    for b_response_file in b_response_files:
        # Each file goes in its own directory
        output_dir = b_response_file.parent
        logger.info(f"Processing: {b_response_file}")
        try:
            convert_file(b_response_file, output_dir)
        except Exception as e:
            logger.error(f"Error processing {b_response_file}: {e}")


def main() -> int:
    """Entry point for B-response converter."""
    parser = argparse.ArgumentParser(
        description="Convert B-response.md (JSON) to formatted French markdown + JSON"
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Path to B-response.md file or directory containing such files",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory (default: same as input file)",
    )

    args = parser.parse_args()

    try:
        if args.input.is_dir():
            convert_directory(args.input)
        else:
            convert_file(args.input, args.output_dir)
        return 0
    except Exception as e:
        logger.error(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())