# IFRS Expert

IFRS Expert is a prototype, local, grounded assistant for IFRS accounting questions. It ingests IFRS PDFs, extracts section-aware chunks, stores them in SQLite and FAISS, retrieves relevant passages for a question, and can run a two-stage reasoning pipeline to produce a structured answer. The repository is intentionally closer to an applied research prototype than a finished product: it shows the retrieval, prompting, and evaluation loops used to make IFRS answers more inspectable and stable.

## 1. Demo

Requirements:
- Python 3.11+
- [`uv`](https://github.com/astral-sh/uv)

The fastest demo uses the small committed corpus already present in `data/db/` and `data/index/`, so you can run retrieval without ingesting anything first.

### Minimal retrieval demo

```bash
uv sync --all-groups

uv run python -m src.cli list

printf 'Can a derivative be designated as a hedging instrument in a hedge of a net investment in a foreign operation?\n' \
  | uv run python -m src.cli query -k 2 --json --min-score 0.6
```

What to expect:
- `list` prints the document IDs currently loaded in SQLite
- `query` returns a JSON array of retrieved chunks
- each result includes `doc_uid`, `section_path`, page range, full chunk text, and a similarity score
- with the committed demo corpus, the top hits should come from IFRIC 16 and IFRS 9 sections about net investment hedges and hedging instruments

Notes:
- on first run, `sentence-transformers` may download the `BAAI/bge-m3` embedding model
- `-k` is applied per document, not globally

### Optional: ingest one of the sample PDFs

```bash
uv run python -m src.cli store "examples/ifrs-16-leases_38-39.pdf" --doc-uid ifrs-16-demo
```

What to expect:
- the command parses the PDF into section-based chunks
- it inserts those chunks into SQLite
- it computes embeddings and appends them to the FAISS index

### Optional: run the full answer pipeline

The `answer` command depends on the local `pi` CLI plus configured model/provider access.

```bash
mkdir -p runs/demo

printf 'Can a derivative be designated as a hedging instrument in a hedge of a net investment in a foreign operation?\n' \
  | uv run python -m src.cli answer -k 2 --min-score 0.6 --output-dir runs/demo --save-all
```

What to expect:
- Prompt A identifies candidate accounting approaches from retrieved context
- Prompt B evaluates applicability and returns a structured French JSON answer
- when `--save-all` succeeds, intermediate artifacts are written under `runs/demo/`

## 2. How it works

### Ingestion and chunking
- PDFs are parsed with PyMuPDF in `src/pdf/extraction.py`
- the extractor uses page coordinates and text heuristics to detect section numbers, skip headers/footers, and build chunks aligned to IFRS sections rather than fixed token windows
- each chunk keeps `doc_uid`, `section_path`, `page_start`, `page_end`, and text

### Storage and retrieval
- chunks are stored in SQLite (`data/db/ifrs.db`)
- embeddings are stored in a FAISS inner-product index plus an `id_map.json`
- embeddings are generated with `sentence-transformers` using `BAAI/bge-m3`

### Retrieval policy
- a query is embedded once and searched against the full FAISS index
- results are filtered by a minimum score threshold
- selection is `top-k per document`, not just global top-k
- retrieval can then expand around each hit by adding neighboring chunks (`--expand`)
- for small documents, the pipeline can include the whole document when total text length is below `--full-doc-threshold`

### Two-stage reasoning pipeline
- **Prompt A**: decides whether the question is answerable from the retrieved context and extracts candidate top-level accounting approaches as JSON
- **Prompt B**: takes the same retrieved context plus Prompt A's output, assesses applicability for the specific facts, and returns structured French JSON with recommendation, per-approach reasoning, conditions, references, and operational points
- both prompts are grounded: they explicitly restrict the model to the retrieved context and forbid web search

## 3. Key design decisions

- **Section-aware chunking**: IFRS guidance is organized by paragraphs and appendices, so retrieval is more useful when chunks line up with section boundaries and citation targets.
- **Two-stage prompting**: separating “which accounting approaches are in play?” from “which one applies here?” reduces premature narrowing and made experiments easier to analyze.
- **CLI-first interface**: the project was built as an experimentation loop first; CLI commands are easy to script, benchmark, diff, and run in batches.
- **Local and grounded retrieval**: the indexed corpus is explicit and inspectable, which makes it easier to trace why an answer was produced and where retrieval failed.

## 4. Evaluation approach

The repository includes a sequence of experiments under `experiments/` rather than a single benchmark.

What was evaluated:
- retrieval settings such as `k`, minimum score thresholds, and chunk expansion
- answer stability across many paraphrases of the same question and repeated runs
- transfer from the initial core question to additional IFRS 9 questions sourced later in the process

What those experiments showed:
- adding neighboring chunks often improved recall materially compared with isolated top hits
- `top-k per document` plus score thresholding gave cleaner context than a flat global top-k
- the two-stage pipeline improved consistency in surfacing candidate approaches, but applicability judgments still varied run to run
- when answers failed, the root cause was often either missing source material in the corpus or prompt/output formats that did not fit the question type

## 5. Limitations

- The current corpus is small and centered on IFRS 9 and IFRIC 16, with a few repo artifacts in the committed demo data.
- PDF extraction is heuristic and layout-dependent; section detection is based on coordinates and formatting rules, not a robust parser.
- The project is CLI-first today. There is no finished UI layer in the repository.
- Answer generation is not fully self-contained: the `answer` command shells out to `pi` and expects local model/provider configuration.
- Code quality is uneven in places because the repository grew through experiments; some analysis scripts are brittle and some workflows are still manual.

## 6. Future work

- Make ingestion more robust, especially section boundary detection and expansion to better structural units.
- Extend the corpus beyond the current IFRS 9 / IFRIC 16 focus, including overlapping guidance such as IFRS 13, doctrine, and Big 4 materials.
- Turn the current experiment scripts into a cleaner regression and evaluation harness.
- Add a lightweight UI on top of the existing CLI workflow.
- Replace the current subprocess-based answer integration with a cleaner model interface.
