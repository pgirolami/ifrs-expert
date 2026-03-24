## 2026-03-20

What worked:
- adding embedding + vector storage
- adding query to vector storage
- asking LLM which embedding model to use

What was surprisingly easy:
- how fast I could add those features when not focused on architecture & choosing THE right solution
- solving the fact that nonsensical and on-point queries had about the same embedding: asked LLM to investigate (in Pi) and it found an embedding that separated better

What was confusing / unclear:
- whether I should create my own eval harness or use a real product

Next step:
- 

## 2026-03-23

What worked
- truncating the ingested text to prevent overflow in FAISS because of chunking bugs so I could simply test a query on the full IFRS 9 + IRIC 16 corpus

What was frustrating:
- I spent all my time trying to fix the ingestion bug to prevent the FAISS memory overflow so I was very frustrated at the end of the day from not having made progress
- I vibe-coded it with Minimax and it kept getting lost. Moving to a frontier model helped fix it
- I tried too many different things too fast (fixing the PF extraction, trying scrapling, playwright...)

Next steps:
- figure out why results from `query` are returned in ascending order
- run the retrieved chunks through the LLM with the prompt *manually*
- consider a Chrome extension to retrieve from website directly. Would also allow user to click on section that identify text & section path

What will I change ?
- Go for quick & dirty first and then refine: I could have done the query test at the beginning of the day if I had gone down the truncation route

## 2026-XX-YY

what worked
- 

What was frustrating:
- 

Next steps:
-

What will I change ?
-