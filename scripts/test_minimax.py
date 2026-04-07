#!/usr/bin/env python3
"""Test script for Minimax LLM client."""

import os

from src.llm.minimax_client import MinimaxClient


def main() -> None:
    api_key = os.environ.get("MINIMAX_API_KEY")
    model = os.environ.get("MINIMAX_MODEL")

    if not api_key or not model:
        print("Error: Set MINIMAX_API_KEY and MINIMAX_MODEL environment variables")
        raise SystemExit(1)

    client = MinimaxClient(api_key=api_key, model=model)
    response = client.generate_text("What is your name?")
    print(f"Model response: {response}")


if __name__ == "__main__":
    main()
