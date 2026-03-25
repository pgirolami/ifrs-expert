# Methodology
Implementing an AI assistant in 2026 requires an experimental approach rather than diving straight into "best-pratice" implementation because 
   - it might not be possible with today's technology to operate at the level of reliability required by the Subject-Matter Expert for the assistant to be useful
   - the SME cannot know what they want upfront because they have to experience the technology: SMEs will open up and generate ideas when they are shown examples

In this repository, the following approach was applied with the help of an SME working in a large company in France listed on the CAC-40.

1. Discovery: 
   * **Goal**: show feasibility and identify complexity _at a minimum cost_.
   * **Measure of success**: the SME signs-off on answers that were produced in a repeatable way for 3 out-of-sample questions
   * **Mechanics**
      * Get to a good answer on one question
         * start with one question & correct answer provided by SME
         * limit the corpus of ground truth to standards documents that contain the answer (in our case: IFRS-9 and IFRIC-16)
         * manually iterate on prompts & the retrieval data used in the prompt with the SME until the answer is acceptable in content, structure, presentation and tone. This is where the scope of the assistant is really defined.
            * increase/decrease amount of ground-truth included in the prompt
            * tweak prompt to address issues reported by the SME
      * Make the answer correct for many other ways of formulating the same question
         * identify whether the problems are in retrieval or generation and address them. For example:
            * better embeddings
            * retrieval expansion & thresholding strategies
            * retrieval structuring in the prompt (hierarchy of grounding-data rather than a large number of chunks of text flat)
            * additional rules & constrants in the prompt
            * multi-stage prompts to separate planning from reasoning
         * you want something automated at this stage
            * automatic response generation to a corpus of questions
            * automatic analysis of the stability of answers and their constituents
      * Expand evaluation to new questions provided by SME
      * Expand to more standards documents with the same 4 questions to evaluate stability to noise
      * Expand to more questions for other documents to evaluate ability to generalize
      * Expand to more documents that overlap with standards to evaluate LLM's ablity to handle overlapping and conflicting information
2. Delivery of V1
   * **Goal**: assistant is used by SME
   * **Measure of success**: percentage of questions where assistant was used in first intention to find an answer is over XX%
   * **Mechaniscs**
      * Upgrade what code exists to a proper architecture implemented with Python, including
         * UI for ingestion & asking questions
         * Observability (including LLM calls)
         * Error handling around critical paths
         * Evals for non-regression when models change
         * Professionnal implementation
            * typing
            * tests
            * config via config files
            * secrets not hard-coded
            * logging
         * Docker image
         * Docs