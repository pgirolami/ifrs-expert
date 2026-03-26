# Concrete plan for the next 5 days
## Day 1 — Core loop only

Build only this:

input question
→ retrieve chunks
→ show chunks

No memo
No clarification
No fancy UX

## Day 2 — Add answer
question
→ retrieval
→ grounded answer



## Day 3 — Add clarification
question
→ detect missing info
→ ask question
→ continue

## Day 4 — Add memo
answer
→ structured memo

## Day 5 — Basic eval + demo polish
10 questions
simple checks
working Streamlit app

## TODO & EXPERIMENT
- Fix PDF extraction
- Compare PDF extraction vs website ingestion on one standard
- Use each document’s scope/introduction as a document-level routing signal before chunk retrieval.
- expand until heading boundary
- set temperature to 0 to see if wew get more stability on the responses
- two-pass Prompt A:
    - extract all distinct recognized approaches from the retrieved material
    - keep only those that belong to the accounting issue named by the question