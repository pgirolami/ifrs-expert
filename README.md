# IFRS Expert

Financial reporting guidance is complex, highly structured, and frequently ambiguous. Experts answering questions in this domain must:
- locate authoritative references
- interpret standards and agenda decisions
- reason about incomplete facts
- document conclusions with clear citations

This project explores how to assist IFRS standards experts working in large companies with those workflows.

A key principle identified from the start was:
> Answers must be grounded in retrieved sources approved by Subject-Matter Experts and supported with citations.

# Inputs & Outputs

The assistant operates on a corpus of approved documents provided by the expert and ingested & indexed by the assistant. This need only be done once per document. Documents currently supported:
- IFRS standards
- IFRIC agenda decisions

IFRS experts ask questions to the assistant in any language via a web chat interface and the assistant answers in French with a structured output that surfaces assumpations, recommendation and the reasoning behind the applicability for each approach considered. 

# Methodology
See [METHODOLOGY.md](docs/METHODOLOGY.md)

# Running the assistant
TODO at Delivery

# Repository Structure

 ``` 
 AGENTSmd  
 LEARNINGS.md 
 PLAN.md 
 Makefile  

 docs/
  ARCHITECTURE.md
  ARCHITECTURE-evolution.md
  EVALUATION.md
  LIMITATIONS.md
  METHODOLOGY.md

 evals/  
 
 examples/  
 
 experiments/ 
    01_min_context_size/ 
    02_proper_context_hierarchical_retrieval/  
    03_proper_context_hierarchical_retrieval/  
    04_2_stage_processing/ 
    05_tighter_2_stage_processing_json_only/ 
    06_better_2_stage_processing_json_output/  
    07_betterbetter_2_stage_processing_json_output/  
  
 prompts/ 
  
 prototype/ 

 src/ 
    commands/  
    db/  
    migrations/  
    models/  
    pdf/ 
    vector/  
  
 tests/ 
    unit/  
    integration/ 
 ```  

# Limitations and Next steps
- asking clarifying questions
- handle standards transitions periods & conflicting positions in general
- handle more document types (doctrine, blogs,...)
- more evals
- don't know how well the current FAISS/local-file approach scales both in terms of disk/memory usage but also with the LLM. It is possble that we overload the LLM with context once we ingest all standards.

# Safety

This project is intended as **an expert assistant**, not a decision authority.

Generated outputs should always be treated as:

- **draft analysis**
- **starting points for expert review**

Professional judgment remains essential when interpreting accounting standards.