#!/usr/bin/env python3
"""Test script for Minimax LLM client."""

import os
import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.llm.minimax_client import MinimaxClient


def main() -> None:
    api_key = os.environ.get("MINIMAX_API_KEY")
    model = os.environ.get("MINIMAX_MODEL")

    if not api_key or not model:
        print("Error: Set MINIMAX_API_KEY and MINIMAX_MODEL environment variables")
        raise SystemExit(1)

    client = MinimaxClient(api_key=api_key, model=model)
    response = client.generate_text("What is your name?")
    print(response)


if __name__ == "__main__":
    main()
