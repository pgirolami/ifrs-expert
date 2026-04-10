# IFRS Expert

IFRS Expert is a local AI assistant designed to answer real IFRS accounting questions with **grounded, structured, and reproducible reasoning**.

This project explores a practical question:

> How do you make LLM-based systems reliable in a constrained expert domain?

It was **developed in collaboration with an IFRS subject-matter expert**, starting from real questions encountered in practice. The goal was not just to retrieve relevant standards, but to produce answers that match how experts reason: identifying possible accounting approaches, evaluating their applicability, and providing structured, auditable outputs.

---

## What this project demonstrates

Building LLM systems in practice quickly surfaces non-obvious challenges:

- **Retrieval completeness directly impacts reasoning correctness**  
  Missing sections caused the system to miss an accounting approach entirely (*net investment hedge*).

- **Answers are unstable across question phrasing**  
  The same question expressed differently led to different accounting approaches being identified.

- **Single-pass prompting is unreliable**  
  Asking the model to both identify and evaluate accounting approaches in one step produced inconsistent results.

- **Correctness is not enough**  
  Expert users require answers to cite and justify their reasoning from source material.

This project addresses these issues through:
- structured retrieval over IFRS standards
- a two-stage reasoning pipeline with explicit intermediate artifacts
- structured JSON outputs
- a systematic Promptfoo-based evaluation loop to detect regressions and confirm improvements

---

## Example output

**Question**

> Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Output (excerpt)**

```
(...)

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe est un poste monétaire reconnu.
   - Le risque de change génère des écarts de change non totalement éliminés en consolidation.
   - La relation de couverture satisfait aux critères de documentation et d'efficacité d'IFRS 9.

**Raisonnment**:
La créance à recevoir comptabilisée est, selon l'hypothèse, un poste monétaire intragroupe reconnu. IFRS 9 permet en consolidation, par exception, de désigner le risque de change d'un poste monétaire intragroupe comme élément couvert si les gains/pertes de change ne sont pas totalement éliminés selon IAS 21, notamment entre entités ayant des monnaies fonctionnelles différentes.

**Implications pratiques**: Une documentation de fair value hedge peut être envisagée seulement si la créance de dividende crée un vrai risque de change résiduel au niveau consolidé.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.4.1
    >at the inception of the hedging relationship there is formal designation and documentation

(...)
```

The full structured output [(example)](./experiments/31_new_A_with_less_context_in_B/runs/2026-04-10_17-44-35_promptfoo-eval-family-q1/artifacts/Q1/Q1.3/content-min-score=0.53__expand=0__expand-to-section=true__llm_provider=openai-codex__retrieval-mode=documents/B-response.md) includes:
- explicit assumptions
- all candidate approaches (cash flow, fair value, net investment, etc.)
- applicability assessment per approach
- references to IFRS sections
- operational guidance

---

## System overview

The system follows a simple but deliberate pipeline:

```
retrieve → structure → reason → evaluate
```

### Key components

- **Structure-aware ingestion**
  - IFRS HTML pages (downloaded via the chrome-extension) are parsed into section-aligned chunks (not arbitrary text windows)
    - Legacy PDF ingestion is also possible but doesn't work well
  - document structure (sections, hierarchy) is preserved and reused at retrieval time

- **Multi-level semantic retrieval**
  - embeddings (`BAAI/bge-m3`) + cosine similarity search using FAISS
    - bge-m3 was chosen because it is multilingual and it maximized the score distance between non-sensical questions and actual accounting questions among the embeddings tested initially
  - retrieval operates at multiple levels:
    - **document-level retrieval** (coarse filtering)
    - **section-title retrieval** (semantic matching on headings) - not used in the current pipeline, but tested
    - **chunk retrieval** (fine-grained passages)
  - section expansion allows retrieving entire logical subsections instead of isolated chunks
    - there is a "neighbooring expansion" method but it was abandonned

- **Document-aware retrieval strategy**
  - document-first retrieval narrows the corpus before chunk search
  - per-document-type routing (IFRS / IAS / IFRIC / SIC / PS) with different thresholds and caps
  - avoids global top-k competition across heterogeneous documents

- **Shared retrieval pipeline**
  - retrieval logic is centralized and reused across commands
  - exposed via a dedicated `retrieve` command for inspection and debugging (without invoking the LLM)

- **Two-stage reasoning**
  - Prompt A: identify candidate accounting approaches using structured analysis:
    - accounting issue identification
    - authority classification (primary / supporting / peripheral)
    - treatment-family identification
    - mapping to peer top-level approaches
  - Prompt B: evaluate applicability and produce the final structured answer
  - Prompt B only receives **primary and supporting authority**, reducing noise and contradictions

- **Structured outputs**
  - JSON schema with:
    - primary accounting issue
    - authority classification
    - treatment families
    - approaches
    - applicability assessment
    - recommendation
    - references
    - operational points

- **Evaluation loop**
  - Promptfoo-based regression tests
  - schema validation
  - approach coverage checks
  - recommendation consistency checks

---

## Key design decisions

### Two-stage reasoning with explicit intermediate artifact
Separating:
1. *What are the possible approaches?*
2. *Which one applies here?*

→ significantly improved stability across question variants

Prompt A produces a **structured analysis artifact** (issue, authority, treatment families, approaches), which:
- stabilizes approach identification
- makes reasoning auditable
- enables context filtering for Prompt B

---

### Retrieval strategy is a first-class problem
Retrieval evolved from simple chunk search to a **multi-stage, document-aware pipeline**:

- document-level filtering reduces noise early
- per-document-type thresholds avoid cross-document interference
- section-title retrieval improves semantic recall
- section expansion improves completeness

→ retrieval quality directly determines which accounting reasoning paths are even available to the model

---

### Authority classification improves reasoning quality
Explicitly separating:
- primary authority (governing)
- supporting authority (clarifying / alternative models)
- peripheral authority (ignored for approach identification)

→ prevents irrelevant context from influencing the set of candidate approaches  
→ enables Prompt B to operate on a much cleaner context

---

### Structured outputs enable evaluation
Moving from free text to JSON made it possible to:
- validate outputs programmatically
- assert presence of key approaches
- detect regressions across experiments
- compare runs systematically

---

## Evaluation with Promptfoo

Promptfoo is the ongoing regression harness for structured-answer quality.

Recent work focused on:
- stabilizing approach identification (ensuring all peer approaches are consistently found)
- eliminating spurious approaches
- improving recommendation consistency

Typical usage:

```bash
make eval EXPERIMENT_DIR=promptfoo_regression
```

All artifacts are preserved and the Promptfoo UI can be launched to view the results of any evaluation.

Promptfoo details, commands, storage layout, and archive conventions are documented in:
- [`docs/PROMPTFOO.md`](./docs/PROMPTFOO.md)

---

## Demo

This sections sets up a quick demo with only 2 documents (IFRS-9 & IFRIC-16).

### Set up
The assistant supports `openai`, `openai-codex`, `anthropic`, and `mistral` as LLM providers. Configure the provider in your environment or in the `.env` file (see `.env.example`).

Example using Mistral:

```bash
export LLM_PROVIDER=mistral
export MISTRAL_API_KEY=xxx
```

Example using OpenAI Codex OAuth:

```bash
codex login
export LLM_PROVIDER=openai-codex
export OPENAI_CODEX_MODEL=gpt-5.4
# optional override if you do not use ~/.codex/auth.json
# export CODEX_AUTH_FILE=/path/to/auth.json
```

Run the full demo flow end-to-end with the following
```bash
make demo
```
or go-through it line by line by following the instructions.

### Ingest documents

#### Ingesting 2 provided documents
This is enough for the demo

```bash
uv sync --all-groups

uv run python -m src.cli store examples/www.ifrs.org__issued-standards__list-of-standards__ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.html__content__dam__ifrs__publications__html-standards__english__2026__issued__ifric16.html --doc-uid ifric16
uv run python -m src.cli store examples/www.ifrs.org__issued-standards__list-of-standards__ifrs-9-financial-instruments.html__content__dam__ifrs__publications__html-standards__english__2026__issued__ifrs9.html  --doc-uid ifrs9
```
#### Ingesting more documents
If you want to look at how all 64 free documents are ingested:
- create an account on https://ifrs.org
- install the [chrome extension](./chrome_extension/ifrs-expert-import/) through developer mode
- navigate to the [list of standards](https://www.ifrs.org/issued-standards/list-of-standards/)
  - click on each standard: the extension's icon becomes red. Click on the icon
- run the ingestion `uv run python -m src.cli ingest --scope all`

### Quick start using the UI

```bash
uv run streamlit run streamlit_app.py
```
Then copy-paste the following and hit enter
```
Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?
```

### Ask a question via the CLI

```bash
echo "Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?" \
  | uv run python -m src.cli answer
```

---

## Development process

This project was developed through an iterative, experiment-driven approach with a subject-matter expert.

- See [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) for the approach used to go from a single question to a prototype assistant
- See [`docs/JOURNAL.md`](docs/JOURNAL.md) for a chronological record of experiments, failures, and improvements

These documents reflect how the system evolved in response to real-world constraints and feedback.

---

## Limitations

- Full IFRS, IAS, IFRIC, SIC corpus ingested limited to Free documents
- PDF parsing is heuristic which is why it was abandonned in favor of HTML parsing
- retrieval errors still affect reasoning completeness
- evaluation coverage is still limited (focused on regression, not full benchmarking)

---

## Future work

- expand corpus (private IFRS + Big 4 doctrine + expert materials)
- evaluate on other questions in IFRS 9
- evaluate to other types of questions: we expect the prompt to need improvement here because it is very approach-centric and not all questions are about an approach 
- further improve retrieval completeness and document routing
- refine uncertainty handling in outputs

---

## Summary

This project is an exploration of how to build **reliable LLM systems** by:
- grounding *reasoning* in explicit sources
- structuring intermediate and final outputs
- separating retrieval, approach identification, and applicability
- iterating with real users
- and making behavior testable

The core insight:

> LLM performance is not just a prompting problem —  
> it is a **system design problem**.