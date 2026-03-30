# IFRS Expert

IFRS Expert is a local AI assistant designed to answer real IFRS accounting questions with traceable reasoning.

The project was developed with an IFRS subject-matter expert, starting from actual questions encountered in practice. The goal was not just to retrieve relevant standards, but to produce answers that match how experts reason: identifying possible accounting approaches grounded in standards & interpretations, evaluating their applicability, and providing structured, reusable outputs.

This repository focuses on the core technical problem: how to combine retrieval, prompting, and evaluation to make answers both grounded and stable across variations of the same question.

## Design philosophy

This project prioritizes:
- **traceability**: answers are grounded in explicit source material
- **iterative improvement**: behavior is refined through experiments and expert feedback

It does not aim to be a general-purpose chatbot, but a focused assistant for a constrained domain.

## 1. Example output
**Question**
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ? 

*Source: [Q1.0.txt](experiments/00_QUESTIONS/Q1/Q1.0.txt)*

**Output**
>(...)
>### 2. Couverture de juste valeur
>**Applicabilité**: OUI SOUS CONDITIONS
>
>**Conditions**:
>   - La créance intragroupe est un poste monétaire reconnu.
>   - Le risque de change génère des écarts de change non totalement éliminés en consolidation.
>   - La relation de couverture satisfait aux critères de documentation et d'efficacité d'IFRS 9.
>
>**Raisonnment**:
>La créance à recevoir comptabilisée est, selon l'hypothèse, un poste monétaire intragroupe reconnu. IFRS 9 permet en consolidation, par exception, de désigner le risque de change d'un poste monétaire intragroupe comme élément couvert si les gains/pertes de change ne sont pas totalement éliminés selon IAS 21, notamment entre entités ayant des monnaies fonctionnelles différentes.
>
>**Implications pratiques**: Une documentation de fair value hedge peut être envisagée seulement si la créance de dividende crée un vrai risque de change résiduel au niveau consolidé.
>
>**Référence**:
> - 6.3.1
>    >A hedged item can be a recognised asset or liability
> - 6.3.5
>    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
> - 6.3.6
>    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
> - 6.4.1
>    >at the inception of the hedging relationship there is formal designation and documentation
>
>
>(...)

*Source: [B-response.md](experiments/11_remove_extraneous_approaches_while_reserving_nih/Q1.0_k=5_e=5_min-score=0.5__run1/B-response.md)*


## 2. Demo

Requirements:
- Python 3.11+
- [`uv`](https://github.com/astral-sh/uv)
- Download 
  - [IFRS 9](https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2021/issued/part-a/ifrs-9-financial-instruments.pdf)
  - [IFRIC 16](https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2021/issued/part-a/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.pdf)


### Ingest the IFRS 9 & IFRIC 16 PDFs
This only needs to be done once.

```bash
uv sync --all-groups

uv run python -m src.cli store "~/Downloads/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation" --doc-uid ifric-16
uv run python -m src.cli store "~/Downloads/ifrs-9-financial-instruments.pdf" --doc-uid ifrs-9
```
What to expect:
- the command parses the PDF into section-based chunks
- it inserts those chunks into SQLite
- it computes embeddings and appends them to the FAISS index
- a log of the run is available in `./logs/app.log`

Notes:
- on first run, `sentence-transformers` will download the `BAAI/bge-m3` embedding model

```bash
uv run python -m src.cli list
```

What to expect:
- `list` prints the document IDs currently loaded in SQLite, you should see `ifrs-9` and `ifric-16`


### Run the retrieval process

```bash
echo 'Can a derivative be designated as a hedging instrument in a hedge of a net investment in a foreign operation?\n' \
  | uv run python -m src.cli query -k 2 --json --min-score 0.6 --json
```

What to expect:
- `query` returns a JSON array of retrieved chunks
- each result includes `doc_uid`, `section_path`, page range, full chunk text, and a similarity score
- with the corpus ingested above, the top hits should come from IFRIC 16 and IFRS 9 sections about net investment hedges and hedging instruments

Notes:
- `-k` is applied per document, not globally
- `-e` determines how the size of the chunk expansion around the l chunks that best matched the query
- `-min-score` determines a threshold for including chunks, this is used to eliminate non-sensical questions
- `-f` is the size threshold under which a single chunk in a document expands to all the chunks in the document (used to handle the large variation in document size)
- `--json` returns the full result as JSON rather than a plain text sumary

### Run the full answer pipeline

The `answer` command uses direct API calls to OpenAI, Anthropic, or Mistral. Set the provider and its API key via an environment variable or in the `.env` file (see `.env.example`).

```bash
export LLM_PROVIDER=anthropic
export ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here
```

Then run the pipeline, note that the question could be in any language:
```bash
mkdir -p runs/demo

echo 'Can a derivative be designated as a hedging instrument in a hedge of a net investment in a foreign operation?\n' \
  | uv run python -m src.cli answer -k 2 --min-score 0.6 --output-dir runs/demo --save-all
```

What to expect:
- A few console logs while the pipeline is running and the LLMs crunch the answers
- intermediate artifacts are written under `runs/demo/`:
    - A-prompt.txt derived from [answer_prompt_A.txt](./prompts/answer_prompt_A.txt)
    - A-reponse.json
    - B-prompt.txt  derived from [answer_prompt_B.txt](./prompts/answer_prompt_B.txt)
    - B-reponse.json and B-response.md
- if there is an error at any stage, an `A-error.txt` or `B-error.txt` file will be written
- a more detailed log of the run in [logs/app.log](./logs/app.log) 

### What this system demonstrates

Given a question such as:

> “Can a derivative be designated as a hedging instrument in a hedge of a net investment in a foreign operation?”

The system:
- retrieves relevant IFRS 9 and IFRIC 16 sections
- identifies candidate accounting approaches (e.g. net investment hedge)
- evaluates their applicability to the question
- produces a structured answer with reasoning and references

Furthermore, the focus is not just correctness, but consistency across different phrasings of the same question.

## 3. How it works

### Ingestion and chunking
- PDFs are parsed with PyMuPDF in `src/pdf/extraction.py`
- the extractor uses page coordinates and text heuristics to detect section numbers, skip headers/footers, and build chunks aligned to IFRS sections rather than fixed token windows
- each chunk keeps `doc_uid`, `section_path`, `page_start`, `page_end`, and text

### Storage and retrieval
- chunks, including their full text, are stored in SQLite (`data/db/ifrs.db`)
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

## 4. Key design decisions

- **Section-aware chunking**: IFRS guidance is organized by paragraphs and appendices, so retrieval is more useful when chunks line up with section boundaries and citation targets.
- **Two-stage prompting**: separating “which accounting approaches are in play?” from “which one applies here?” reduces premature narrowing and made experiments easier to analyze.
- **CLI-first interface**: the project was built as an experimentation loop first; CLI commands are easy to script, benchmark, diff, and run in batches.
- **Local and grounded retrieval**: the indexed corpus is explicit and inspectable, which makes it easier to trace why an answer was produced and where retrieval failed.

## 5. Evaluation approach

The repository includes a sequence of experiments under `experiments/` rather than a single benchmark. The experiments were used to guide design decisions rather than to benchmark a fixed system.

What was evaluated:
- retrieval settings such as `k`, minimum score thresholds, and chunk expansion
- answer stability across many paraphrases of the same question and repeated runs
- transfer from the initial core question to additional IFRS 9 questions sourced later in the process

Key outcomes:

- Retrieval completeness directly impacts reasoning quality  
  → Missing IFRIC 16 sections prevented the system from surfacing net investment hedges

- Context construction matters as much as retrieval  
  → “Top-k per document” and chunk expansion produced more stable answers than global top-k

- Single-pass prompting was unstable  
  → Splitting reasoning into two stages (identify approaches → assess applicability) significantly improved consistency across question variants

- Answer stability is a core problem  
  → The same question phrased differently could lead to different approaches being identified without careful prompt design

## 6. Limitations

- The tests & evaluations were done on a small corpus so far which includes IFRS 9 and IFRIC 16.
- PDF extraction is heuristic and layout-dependent; section detection is based on coordinates and formatting rules, not a robust parser.
- The project is CLI-first today. There is no finished UI layer in the repository.
- Code quality is uneven in places because the repository grew through experiments; some analysis scripts are brittle .

## 7. Future work

- Continue to improve prompts as new failures are discovered
  - start by addressing the issue uncovered in Experiment 14 regarding answers being too confident & closed when uncertainty still remains

- Extend the corpus beyond the current IFRS 9 / IFRIC 16 focus, including overlapping guidance such as IFRS 13, doctrine, Big 4 materials, blog posts and forums.

- Make ingestion more robust, especially section boundary detection and expansion to better structural units.
  - Consider ingesting straight from the IFRS website because it will simplify aligning section path & text
  - Consider allowing the user to tag parts of PDF to handle all formats beyond IFRS (Big 4, blog posts...)
  - Handle the case

- Experiment & iterate on ways to make chunk expansion smarter 
  - expand to all chunks of sections that contain retrieved chunks
  - run query similarity on section titles only and include all chunks of retrieved titles

- Turn the current experiment scripts into a cleaner regression and evaluation harness.
  - Questions can be reused
  - Review answers with SME & create evals

- Add a lightweight UI on top of the existing CLI workflow.

