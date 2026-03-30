# IFRS Expert

IFRS Expert is a local AI assistant designed to answer real IFRS accounting questions with **grounded, structured, and reproducible reasoning**.

This project explores a practical question:

> How do you make LLM-based systems reliable in a constrained expert domain?

It was **developed in collaboration with an IFRS subject-matter expert**, starting from real questions encountered in practice. The goal was not just to retrieve relevant standards, but to produce answers that match how experts reason: identifying possible accounting approaches, evaluating their applicability, and providing structured, auditable outputs.

---

## What this project demonstrates

Building LLM systems in practice quickly surfaces non-obvious challenges:

- **Retrieval completeness directly impacts reasoning correctness**  
  Missing IFRIC 16 sections caused the system to miss *net investment hedge* entirely.

- **Answers are unstable across question phrasing**  
  The same question expressed differently led to different approaches being identified.

- **Single-pass prompting is unreliable**  
  Asking the model to both identify and evaluate approaches in one step produced inconsistent results.

- **Correctness is not enough**  
  Expert users require **traceability**: answers must cite and justify their reasoning from source material.

This project addresses these issues through:
- structured retrieval over IFRS standards
- a two-stage reasoning pipeline
- structured JSON outputs
- a lightweight evaluation loop to detect regressions

---

## Example output

**Question**

> Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Output (excerpt)**

```
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
```

The full structured output [(example)](./experiments/11_remove_extraneous_approaches_while_reserving_nih/Q1.0_k=5_e=5_min-score=0.5__run1/B-response.md) includes:
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
  - IFRS PDFs are parsed into section-aligned chunks (not arbitrary text windows)

- **Semantic retrieval**
  - embeddings (`BAAI/bge-m3`) + FAISS
  - top-k per document + chunk expansion

- **Two-stage reasoning**
  - Prompt A: identify candidate accounting approaches
  - Prompt B: evaluate applicability and produce structured output

- **Structured outputs**
  - JSON schema with:
    - assumptions
    - approaches
    - recommendation
    - references
    - operational points

- **Evaluation loop**
  - Promptfoo-based regression tests
  - checks schema, approach coverage, recommendation consistency

---

## Key design decisions

### Two-stage reasoning
Separating:
1. *What are the possible approaches?*
2. *Which one applies here?*

→ significantly improved stability across question variants.

---

### Section-aware chunking
IFRS is highly structured.

Aligning chunks with sections:
- improves retrieval relevance
- enables precise citations
- reduces hallucination risk

---

### Retrieval strategy matters as much as prompting
- top-k per document > global top-k
- chunk expansion improves recall
- missing documents = missing reasoning paths

---

### Structured outputs enable evaluation
Moving from free text → JSON made it possible to:
- validate outputs programmatically
- assert presence of key approaches
- detect regressions

---

## Evaluation

The project includes two complementary evaluation approaches:

### 1. Experimental analysis

This is an ad-hoc implementation built incrementally from inception
- multiple question variants
- repeated runs
- qualitative analysis of failure modes

With PromptFoo setup, it is no longer going to be used going forward.

### 2. Promptfoo regression suite

```bash
npx promptfoo eval
```

Checks include:
- valid JSON schema
- presence of expected approaches
- consistency of recommendation
- basic reasoning quality (LLM-graded rubric)

This transforms evaluation from:
```
“looks good”
```
to:
```
“behavior is stable and testable”
```

---

## Demo

### Set up
The assistant uses direct API calls to OpenAI, Anthropic, or Mistral. Set the provider and its API key via an environment variable or in the `.env` file (see `.env.example`).

```bash
export LLM_PROVIDER=mistral
export MISTRAL_API_KEY=xxx
```

After cloning the repo, set up its dependencies
```bash
uv sync --all-groups
```

### Ingest documents

```bash

curl https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2021/issued/part-a/ifrs-9-financial-instruments.pdf --output /tmp/ifrs-9-financial-instruments.pdf

curl https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2021/issued/part-a/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.pdf --output /tmp/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.pdf 

uv run python -m src.cli store /tmp/ifrs-9-financial-instruments.pdf --doc-uid ifrs-9
uv run python -m src.cli store /tmp/ifric-16-hedges-of-a-net-investment-in-a-foreign-operation.pdf  --doc-uid ifric-16
```

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
  | uv run python -m src.cli answer -k 5 -e 5 --min-score 0.55
```

---

## Limitations

- Limited corpus (IFRS 9 + IFRIC 16)
- PDF parsing is heuristic
- retrieval errors still affect reasoning completeness
- eval suite is minimal (focused on regression, not full benchmarking)

---

## Future work

- expand corpus (IFRS + Big 4 doctrine + expert materials)
- improve retrieval completeness and chunk expansion
- refine prompts for uncertainty handling
- extend evaluation coverage and automation

---

## Summary

This project is more than a PDF chatbot: it is an exploration of how to build **reliable LLM systems** by:
- grounding *reasoning* in explicit sources
- structuring outputs for inspection
- iterating with real users
- and making behavior testable

The core insight:

> LLM performance is not just a prompting problem —  
> it is a **system design problem**.