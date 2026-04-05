#!/usr/bin/env python3
"""Analyze promptfoo experiment outputs.

Usage:
    python experiments/analysis/analyze.py openai
    python experiments/analysis/analyze.py openai --experiment 15_promptfoo_baseline_Q1
    python experiments/analysis/analyze.py openai -v
"""

import sys
from pathlib import Path

# Add analysis directory to path
sys.path.insert(0, str(Path(__file__).parent))

from run_promptfoo_analysis import main

if __name__ == "__main__":
    main()
