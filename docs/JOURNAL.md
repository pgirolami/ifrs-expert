# Project Journal - IFRS Expert Assistant

This journal documents the development progress of the IFRS Expert Assistant - a local AI assistant for IFRS accounting guidance.

---

## Discovery

### 2026-03-19 : Validate that a prompt can find the right answer to a real question based on grounding standards excerpts

- Worked from a real question fielded by the Subject-Matter Expert where multiple accounting approaches need to be evaluated (answer in IFRS 9 + IFRIC 16). Manually retrieved relevant sections of IFRS 9
- Built prompt constraining LLM to answer based only on sections provided and cite relevant sections
- Iterated on prompt & sections included until SME confirmed response correctness
- iterated on structure and tone until SME signed off
    - uncovered new uses of the tool ("copy-paste summary recommendation", "widen analysis to evaluate multiple approaches")

### 2026-03-20 : PDF Parsing & Chunking prototype

- Implemented PDF parsing for IFRS 16 and IFRS 9 standards, chunking by document section rather than character count
    - Prepare test document & test fixture
    - Implementation
- Built CLI commands to store and list document chunks, integrating SQLite for text storage and FAISS for vector indexing.

### 2026-03-20 : Similarity-based retrieval prototype

- Implement cosine similarity on normalized vectors, test on various queries including non-sensical
- Switch to BGE-M3 embeddings to better separate scores for relevant and non-relevant queries
- Added JSON output option
- Created a cheap retrieval test harness
- Test "discovery" prompt that worked with SME on the chunks retrieved: works ok

### 2026-03-24 : Tune retrieval and prompt until answer is as good as first acceptable answer

- Added chunk size limits to prevent errors on oversized chunks due to imperfect parsing of PDF
- Added `e`= chunk expansion around a retrieved chunk
- Implement `answer` on the CLI so it generates the prompt automatically
- Add option to expand to all the chunks of a document when document is under threshold size (to include all of IFRIC-16)
- Tune until "Net Investment Hedge" approach is surfaced
    - [Experiment 01](../experiments/01_min_context_size/EXPERIMENTS.md): manual experiment on (k, e, f) to evaluate how much context is necessary to surface "Net Investment Hedge" approach
    - [Experiment 02](../experiments/02_proper_context_hierarchical_retrieval/EXPERIMENTS.md): create 3 variations of the SME's question, experiment on a minimum score threshold to consider a retrieved chunk combined with retriving top-k *per document* and structuring chunks per document in the prompt

### 2026-03-24 - 2026-03-25: Tune until answer is stable across wording variants of the question

- Create 20 variations of the SME's question and quick & dirty automation calling the LLM with Pi to streamline testing
- [Experiment 03](../experiments/03_proper_context_hierarchical_retrieval/EXPERIMENTS.md) : fix (k=5, e=5, min-score=0.5, f= 0) and evaluate stability of answers to each question variant qualitatively

- Address answer variance by introducing **2-stage pipeline**: 
    - Prompt A identifies legitimate accounting approaches
    - Prompt B determines applicability to the context
- Refine prompts through many experiments while developping quantitative analysis
    - [Experiment 04](../experiments/04_2_stage_processing/EXPERIMENTS.md) computes 3 runs of the 2-stage pipeline on the 22 questions, first attempt at quantitative analysis
    - [Experiment 05](../experiments/05_tighter_2_stage_processing_json_only/EXPERIMENTS.md)
    - Weed out non-approaches
        - [Experiment 06](../experiments/06_better_2_stage_processing_json_output/EXPERIMENTS.md)
        - [Experiment 07](../experiments/07_betterbetter_2_stage_processing_json_output/EXPERIMENTS)
    - Improving "net investment hedge" recall
        - [Experiment 08](../experiments/08_treatment_only_approaches/EXPERIMENTS.md)
        - [Experiment 09](../experiments/09_candidate_approaches_vs_applicability/EXPERIMENTS.md) 
        - [Experiment 10](../experiments/10_recall_nih_consistently/EXPERIMENTS.md)
        - [Experiment 11](../experiments/11_remove_extraneous_approaches_while_reserving_nih/EXPERIMENTS.md)

### 2026-03-26 : Preparation for Delivery phase

- Draft proper [README](README.md) and [METHODOLOGY](METHODOLOGY.md)
- Fix all linting errors, failing test, formatting errors
- Overhaul mocking strategy that was too brittle
- Investigate unstructured.io and langchain

## Delivery
