# Project Journal - IFRS Expert Assistant

This journal captures the actual development process of the IFRS Expert assistant.

It documents how the system evolved from a single prompt to a structured, evaluated pipeline, including key failures, experiments, and design decisions.

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

- Preparation for Delivery phase
    - Draft proper [README](README.md) and [METHODOLOGY](METHODOLOGY.md)
    - Fix all linting errors, failing test, formatting errors
    - Overhaul mocking strategy that was too brittle
    - Investigate unstructured.io and langchain

### 2026-03-27 : Extend evaluation to other questions

- Obtained 2 additional questions related to IFRS 9 from SME, sourced from Lefebvre Comptable FAQ. Generated 4 additional wording variants for each to evaluate stability of results quantitatively
    - [Experiment 12](../experiments/12_evaluate_question_2/EXPERIMENTS.md)
- Generated answers for additional questions and evaluated quality of the answers and the stability across 3 runs. Wrote qualitative experiment summary
    - [Experiment 13](../experiments/12_evaluate_question_2/EXPERIMENTS.md): question 4
    - [Experiment 14](../experiments/12_evaluate_question_2/EXPERIMENTS.md): questions 5, 6, 7, 8, 9

### 2026-03-31 : Tighten prototype

- Call LLM APIs rather than use Pi to get LLM responses (OpenAI & Mistral checked, Anthropic implemented)
- Add a POC Streamlit app to ask questions & ask follow-ups
- Add PromptFoo for evals, added a few evals
- Setup automated demo

### 2026-04-04 - 2026-04-06 : Prepare for more improvements & evaluations

- Scale PromptFoo setup & automation to support many questions & experiments
    - persist Promptfoo in the experiment directory so we can add to git
    - persist pipeline artifacts to a "run" directory
    - move promptfooconfig.yaml to the "run" directory so it can be added to git too
    - fix VARIANT selection which wasn't working properly (Q1.2 also include Q1.20, Q1.21 and Q1.22)
    - Support using OpenAI codex as a provider
- Fix regression since move to API which was due to thinking not being set & the wrong model being used because of a default fallback that's not warned about (removed it)
    - [Experiment 15](../experiments/15_promptfoo_baseline_Q1/EXPERIMENTS.md)
- Make ingestion more robust
    - Created Chrome extension to download the DOM when on a standards page
    - Ingest straight from HTML to better parse the structure, see [plan](../plans/2026-04-04--html-import.md).
    - Add an `ingest` command to scan the directory to which the HTML is saved to.
- Address Experiment 15 next steps
    - Evaluate the impact of min_score and k on retrieval for worst-performing question Q1.2
        - [Experiment 16](../experiments/16_impact_of_minscore_on_Q1.2/EXPERIMENTS.md)
        - [Experiment 17](../experiments/17_promptfoo_baseline_codex_k=10_Q1/EXPERIMENTS.md) recomputes the baseline on Q1 and shows k=10 improves the approach stability and the overall results
    - Ingest section titles and section tree. Query on section titles and expand to all chunks in section subtree to see if retrieval is improved to address issue found in experiment 15.
        - [Experiment 18](../experiments/18_test_Q1.2_with_titles_retrieval/EXPERIMENTS.md)

### 2026-04-07
- Fixed bug in Chrome extension for downloading IFRS standards
- Ingested many more files related to the Q1 family of questions and check it doesn't degrade the response (it does)
    - [Experiment 19](../experiments/19_check_results_are_still_good_with_more_documents/EXPERIMENTS.md): a few more documents
    - [Experiment 20](../experiments/20_check_results_are_still_good_with_all_public_ifrs_docs/EXPERIMENTS.md): all documents
- Add Minimax API provider

### 2026-04-08 - 2026-04-09
- Worked on making retrieval much more focused so the tool still works with all public IFRS documents
    - create a representation of the document based on key sections (background, scope, ...) and the table of contents to increase chances of surfacing very abstract documents like IFRS 9.
        - filtered out sections with little information for the task at hand (Board of Approvals, References, Contents...)
    - added a `query-documents` command to test document retrieval based on this & manually fine-tuned parameters so it surfaces IFRS 9 (easy) and IFRIC 16 (not as easy)
    - extracted the retrieval pipeline and added a `retrieve` command that first retrieves documents and then only the chunks within those documents and did a quick test:
        - Q1.0 (one of the best retrieval for IFRS 9 and worst for IFRIC 16) returns the right response
        - Q1.18 (one of the worst retrieval for IFRS 9 and mid-performance for IFRIC 16) 
    - ran some manual experiments to get a sense of the parameters to use to consistently retrieve IFRS 9 and IFRIC 16, as well as the impact on the size of the context generated
        - [Experiment 22](../experiments/22_manual_experiment_on_document_routing/EXPERIMENTS.md) (multiple sub experiments)
    - used those parameters on the Q1 family and analyzed the results. Realize that a lot of the apparent instability and spurious approaches aren't as bad as they look: they usually collapse into hedging vs not hedging and the hedging reasoning is usually correct
        - [Experiment 23](../experiments/23_Q1_baseline_with_settings_found_in_experiment_22/EXPERIMENTS.md)
        - [Experiment 24](../experiments/24_section_expansion_Q1_baseline_with_settings_found_in_experiment_22/EXPERIMENTS.md)

### 2026-04-10

Continued work to identify correct approaches on the full free IFRS corpus, using learnings from Experiments 23 & 24. Also created a new output for experiment analysis that shows the returned approaches per run as well as the sections returned


- Rework the prompt so multiple documents are used together rather than against each other before trying to narrow further the documents retrieved because retrieving IAS 21 makes perfect sense but not a "general accounting" approache
    - [Experiment 25](../experiments/25_new_prompt_same_as_24/EXPERIMENTS.md)
    - [Experiment 26](../experiments/26_new_prompt_same_as_25/EXPERIMENTS.md)
- New preliminary step in Prompt A to force the LLM to perform its analysis by identifying the accounting issue, which documents were authoritative or not, and only then identify the approaches (from the primary or supporting authorities)
    - [Experiment 27](../experiments/27_new_prompt_same_as_26/EXPERIMENTS.md)
    - [Experiment 28](../experiments/28_more_questions_same_as_27/EXPERIMENTS.md) : same as experiment 27 but on 8 questions instead of 2

    Results were better in that the spurious approaches were now limited to the "hedging" universe of possibilities but the core approaches still very unstable: some were regularly missing, even across runs for a given question.
    
    This led us to hypothesis we had good-enough retrieval and the problem was now in the reasoning induced by the prompt.

- We wanted to confirm/invalidate our hypothesis: if we change the prompt to more forcefully constrain the output to the core approaches, are they consistently returned ? This would allow us to know whether the remaining problem was the retrieved context or the prompt
    - [Experiment 29](../experiments/29_same_8_questions_prompt_with_hedging/EXPERIMENTS.md).
    
        Only the core approaches were returned and the applicable approaches was always returned but *the 2 others were not returned on every run !* We hypothesized this indicated that the LLM was choosing what to return based on applicability so we rewrote the prompt to force it even further not to consider applicability when identifying approaches and we removed the "assumptions" field from the output since it wasn't needed. We considered removing the question but that would prevent the LLM from identifying the primary accounting issue.
    - [Experiment 30](../experiments/30_same_as_29_with_more_guardrails/EXPERIMENTS.md)

        This was the first experiment with near perfect result on approaches identified, see the [matrix](../experiments/30_same_as_29_with_more_guardrails/spurious_approaches_vs_sections_matrix.html).
        
        ![Experiment 30 result matrix](./Experiment_30_result_matrix.png)
        
        Consequently, this confirmed the context was good enough and further work should focus on making the prompt generic again to remove any mention of hedging approaches.


- Experiments to generalize the prompt away from hedging-specific language
    - Manual test of a new prompt on question Q1.4 (one of the worst)
        
        The answer was correct and contained additional unsollicited JSON fields that mapped to the thinking we were asking of it: `primary_accounting_issue`, `authority_classification`, `treatment_families` and finally `approaches`.
        
        This sounded like a good idea so we incorporated the idea in a new Prompt A and considered giving Prompt B a context limited to the authoratitive and supporting documents

    - Manual test with

