# Goal

Improve & tune retrieval to retrieve IFRS 9, IAS 39 & IFRIC 16 on every Q1 variant. IFRIC 17 and IAS 21 would be acceptable too.

# Steps

1. Fixed ingestion bugs affecting multiple documents (IAS 19, IAS 21...) which might make retrieval less efficient, manual review of each standard document ([Verification table](./ingestion_review.md))
2. Evaluated new mechanism for retrieval `documents2`: query each document-type but map each variant back to the standard. The idea is to narrow the corpus of standards to look at by considering that if supporting material matches the semantics of the query then it's likely the standard is relevant. Widening to supporting documents might be done later if we see the quality of the answer is not up to par.

# Results
## Results on the Q1 family

Results of `documents2` retrieval with the policy a little bit tuned in Q1.0 => [Results](./generated_q1_retrieve_target_matrix.md) show that we are still far from being able to retrieve IFRS 9 & IAS 39 consistently
- IFRS 9 is retrieved in 10/23 questions, often time very high
- IFRIC 16 is retrieved in 19/23 questions, at all ranks
- IAS 39 is retrieved in 10/23 questions, often low in the ranking

It doesn't make sense for some documents to be retrieved:
- IFRS 17 "Insurance Contracts"
- IFRIC 23 "Uncertainty over Income Tax Treatments"
- IFRIC 5 "Rights to Interests arising from Decommissioning, Restoration and Environmental Rehabilitation Funds"
- IFRS 2 "Share-based Payment"
- ...

Some documents are not authoritative but it can make sense based on the title
- IFRIC 17 "Distributions of Non‑cash Assets to Owners"
- IFRS 12 "Disclosure of Interests in Other Entities"
- IFRIC 19 "Extinguishing Financial Liabilities with Equity Instruments"
- IFRS 19 "Subsidiaries without Public Accountability: Disclosures"
- IAS 7 "Statement of Cash Flows"
- IFRIC 23 "
- ...

Finally, a lot of questions retrieve more than 15 documents

## Results on the Q1en family

This family contains the same questions but translated to English by ChatGPT. The [results](./generated_q1en_retrieve_target_matrix.md) show **very** different results:
- IFRS 9, IAS 39 and IFRIC 16 are retrieved for every variant and make up the top 3 on almost all of them. The lowest ranking achieved on any of the question is 7th.
- the total number of documents retrieved by question is significantly lower than in French

# Conclusions

This experiment does not yet validate `documents2` retrieval for the real target setting, which is the French Q1 family:
- IFRS 9 is retrieved in only 10/23 questions
- IAS 39 is retrieved in only 10/23 questions
- IFRIC 16 is retrieved in 19/23 questions
- many non-authoritative documents are retrieved
- result sets are often too large for document routing to be considered successful


This would lead us to believe the representation is deficient or that the cosine similarity is not a good measure for retrieval but the results in English paint a completely different picture. On Q1en:
- IFRS 9, IAS 39 and IFRIC 16 are retrieved in 23/23 questions
- they are almost always the top 3 results
- the total number of retrieved documents is significantly lower


This suggests that the new retrieval architecture is viable in principle, but that the current document representations and/or embedding behavior are not robust enough for French query phrasing. The main problem is therefore not downstream prompting, and probably not document routing as a concept, but French semantic matching at document-retrieval time.

# Next steps

Focus on improving document representations for French retrieval, especially for IAS/IFRS standards, before doing further work on prompt behavior or authority-resolution logic.

Ideas to test that do not require extra steps in the retrieval pipeline or during ingestion
1. Look up terms in the French question in a bilingual glossary, deduplicate them and append them after the question when running the similarity query
    The hope is that the words in english will match better with the documents we're interested in
    ```
        Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?
        consolidated financial statements
        hedge accounting
        foreign exchange risk
        intragroup dividend
        receivable
        recognized
    ```
2. Match on chunks & derive the documents from the matching chunks
3. Match the query on section titles or document titles and deduplicate the documents across chunks. This might solve IAS 39/IFRS 9 that are very broad and don't necessarily match perfectly to hedging
4. Add hybrid dense + sparse retrieval on authoritative docs only, especially on title, TOC and scope / objective / issue / background
5. Add weighting by child document class in the `documents2` retrieval mode


