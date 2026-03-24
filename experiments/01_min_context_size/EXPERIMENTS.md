# 2026-03-24

## Minimum context to see NIH appear

### IFRS 9 + full IFRIC 16 (manual baseline that worked)
**Answer**
   - Ok to cover forex risk ✅
   - Not ok to for intragroup ✅
   - No to highly probable transaction because already accounted for ✅
   - Mentions NIH ✅

**Summary table**
| Approche                                               | Applicable             | Condition clé                                             |
| ------------------------------------------------------ | ---------------------- | --------------------------------------------------------- |
| Créance de dividende comme poste monétaire intragroupe | Oui sous conditions    | Écarts de change non totalement éliminés en consolidation |
| Dividende intragroupe comme transaction intragroupe    | Non                    | Exclusion des transactions intragroupe en consolidation   |
| Dividende futur comme transaction prévue               | Non dans le cas décrit | La créance est déjà comptabilisée                         |
| Couverture d’investissement net par analogie           | Non                    | IFRIC 16 ne s’applique pas à ce cas                       |

### top-k chunks from IFRS 9 + IFRIC 16
#### k=5
_Retrieved chunks_
   - 6.3.5, B6.3.5, 6.3.6, B2.6, 2.1

**Answer**
   - Ok to cover forex risk ✅
   - Not ok to for intragroup ✅
   - No to highly probable transaction because already accounted for ✅
   - Doesn't mention NIH which is not surprising since retrieval didn't include any IFRIC 16 sections ❌

**Sections mentioned in answer**
TODO

**Summary table**
| Approche                                                                     | Applicable          | Condition clé                                                |
| ---------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------ |
| Créance de dividendes intragroupe déjà comptabilisée comme élément monétaire | Oui sous conditions | Écarts de change non entièrement éliminés en consolidation   |
| Application de la règle générale aux éléments intragroupe                    | Non                 | Les hedged items doivent en principe être externes au groupe |
| Transaction intragroupe future hautement probable                            | Non dans ce cas     | La créance est déjà comptabilisée                            |
| Couverture d’un risque de change sans effet sur le résultat consolidé        | Non                 | Le risque doit affecter le résultat consolidé                |

#### k=20
_Retrieved chunks_
   - ifrs9_6.3.5, ifrs9_B6.3.5, ifrs9_6.3.6, ifrs9_B2.6, ifrs9_2.1
   - ifrs9_5, ifrs9_B6.3.6, ifrs9_4.3.4, ifrs9_B5.7.9, ifrs9_B4.3.4
   - ifrs9_2.3, ifrs9_7.2.26, ifrs9_5.7.1, ifrs9_B4.3.12, ifrs9_6.9.6
   - ifrs9_B2.5, ifrs9_3, ifrs9_6.6.3, ifrs9_13, ifrs9_4.2.2
   - ifrs9_5.2.3, ifrs9_3.3.5, ifric16_14, ifrs9_5.7.1A, ifrs9_5.7.3
   - ifrs9_5.7.7, ifrs9_B3.2.17, ifrs9_B5.7.1, ifrs9_B5.7.2, ifric16_AG6
   - ifrs9_B4.3.11, ifrs9_B4.1.36, ifrs9_6.1.3, ifrs9_B4.1.30, ifrs9_7.2.34
   - ifrs9_5.7.8, ifrs9_B3.2.10, ifric16_17, ifrs9_4.3.5

**Answer**
TODO

**Sections mentioned in answer**
   - 6.3.6
   - 6.3.5
   - B6.3.6


**Summary table**
TODO

#### k=40
-Retrieved chunks-
   - 6.3.5, B6.3.5, 6.3.6, B2.6, 2.1
   - 5, B6.3.6, 4.3.4, B5.7.9, B4.3.4
   - 2.3, 7.2.26, 5.7.1, B4.3.12, 6.9.6
   - B2.5, 3, 6.6.3, 13, 4.2.2

**Summary table**
| Approche                                                                    | Applicable          | Condition clé                                                |
| --------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------ |
| Créance de dividende intragroupe déjà comptabilisée comme élément monétaire | Oui sous conditions | Écarts de change non totalement éliminés en consolidation    |
| Dividende intragroupe comme transaction future                              | Non                 | N’affecte pas le résultat consolidé                          |
| Créance intragroupe mais exposition totalement éliminée                     | Non                 | Absence d’exposition résiduelle en consolidation             |
| Documentation dans les comptes individuels/séparés                          | Oui                 | Documentation au niveau de l’entité, pas au niveau consolidé |

**Review**
   - NIH coverage is still not mentioned even though some IFRIC 16 chunks were reported
   - doesn't mention highly-probable transactions to eliminate it but does mention "couverture de flux" and reject it


### top-k chunks + expand to e nearby chunks
#### k=5
##### e=5
###### f=0

_Retrieved chunks_

**ifrs-9**
- 1.1
- 2.1, 2.2, 2.3, 2.4, 2.5, 2.6
- 6.2.6, 6.3.1, 6.3.2, 6.3.3, 6.3.4, 6.3.5, 6.3.6, 6.3.7, 6.4.1, 6.5.1, 6.5.2, 6.5.3
- B2.1, B2.2, B2.3, B2.4, B2.5, B2.6, B3.1.1, B3.1.2, B3.1.2A, B3.1.3, B3.1.4, B6.2.6, B6.3.1, B6.3.2, B6.3.3, B6.3.4, B6.3.5, B6.3.6, B6.3.7, B6.3.8, B6.3.9, B6.3.10

**Sections mentioned in answer**
   - 6.3.6
   - 6.3.5
   - 6.3.1
   - 6.5.2(a)
   - 6.3.7 & 6.3.7(a)
   - B6.3.6


**Summary table**
| Approche                                                            | Applicable          | Condition clé                                                                      |
| ------------------------------------------------------------------- | ------------------- | ---------------------------------------------------------------------------------- |
| Couverture en consolidation de la créance intragroupe comptabilisée | Oui sous conditions | Élément monétaire intragroupe + écarts de change non entièrement éliminés          |
| Couverture du dividende intragroupe comme transaction intragroupe   | Non                 | En consolidation, les transactions intragroupe sont exclues sauf exception précise |
| Documentation comme couverture de juste valeur de l’actif reconnu   | Oui sous conditions | Créance reconnue + risque de change désigné + impact en résultat                   |
| Documentation sans critères formels IFRS 9                          | Non                 | Documentation initiale et tests de qualification obligatoires                      |

**Review**
   - Ok to cover forex risk ✅
   - Not ok to for intragroup ✅
   - doesn't mention highly-probable transactions to eliminate it but does mention "couverture de flux" and reject it ❌
   - Doesn't mention NIH which is not surprising since retrieval didn't include any IFRIC 16 sections ❌
   - 😱 says "Yes if" to fair-value hedge which is incorrect

###### f=30000

- ifrs-9-financial-instruments 2025 required: 1.1, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 6.2.6, 6.3.1, 6.3.2, 6.3.3, 6.3.4, 6.3.5, 6.3.6, 6.3.7, 6.4.1, 6.5.1, 6.5.2, 6.5.3, B2.1, B2.2, B2.3, B2.4, B2.5, B2.6, B3.1.1, B3.1.2, B3.1.2A, B3.1.3, B3.1.4, B6.2.6, B6.3.1, B6.3.2, B6.3.3, B6.3.4, B6.3.5, B6.3.6, B6.3.7, B6.3.8, B6.3.9, B6.3.10

**Sections mentioned in answer**
   - 6.3.6
   - 6.3.5
   - 6.3.1
   - 6.3.3
   - 6.3.7
   - 6.3.7(a)
   - 6.3.2
   - 6.4.1(b)

**Summary table**
| Approche                                                                              | Applicable          | Condition clé                                                            |
| ------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------ |
| Créance de dividende intragroupe reconnue comme élément monétaire couvert             | Oui sous conditions | Écarts de change non totalement éliminés et impact en résultat consolidé |
| Dividende intragroupe traité comme transaction intragroupe ordinaire en consolidation | Non                 | L’élément couvert doit en principe être avec une partie externe          |
| Transaction future intragroupe hautement probable                                     | Non                 | Ici, la créance est déjà comptabilisée                                   |
| Désignation du seul composant change de la créance                                    | Oui sous conditions | Risque de change séparément identifiable et mesurable                    |

**Review**
   - Ok to cover forex risk ✅
   - Not ok to for intragroup ✅
   - No to highly probable transaction because already accounted for ✅
   - Doesn't mention fair value hedge
   - No mention of NIH because it wasn't retrieved at k=5 ❌

#### k=10
##### e=5

_Retrieved chunks_
**ifrs-9**
- 1.1
- 2.1, 2.2, 2.3, 2.4, 2.5, 2.6
- 4.2.1, 4.2.2, 4.3.1, 4.3.2, 4.3.3, 4.3.4, 4.3.5, 4.3.6, 4.3.7, 4.4.1, 4.4.2
- 6.2.6, 6.3.1, 6.3.2, 6.3.3, 6.3.4, 6.3.5, 6.3.6, 6.3.7, 6.4.1, 6.5.1, 6.5.2, 6.5.3
- B2.1, B2.2, B2.3, B2.4, B2.5, B2.6
- B3.1.1, B3.1.2, B3.1.2A, B3.1.3, B3.1.4
- B4.1.35, B4.1.36, B4.3.1, B4.3.2, B4.3.3, B4.3.4, B4.3.5, B4.3.6, B4.3.7, B4.3.8, B4.3.9
- B5.7.4, B5.7.5, B5.7.6, B5.7.7, B5.7.8, B5.7.9, B5.7.10, B5.7.11, B5.7.12, B5.7.13, B5.7.14
- B6.2.6, B6.3.1, B6.3.2, B6.3.3, B6.3.4, B6.3.5, B6.3.6, B6.3.7, B6.3.8, B6.3.9, B6.3.10, B6.3.11
**ifric-16**
- 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

**Sections mentioned in answer**
   - 6.3.5
   - 6.3.6
   - 6.3.2
   - 6.3.1
   - 6.3.3
   - 6.4.1
   - 6.4.1(b)
   - 6.4.1(c)(i)


**Summary table**
| Approche                                                            | Applicable          | Condition clé                                                                            |
| ------------------------------------------------------------------- | ------------------- | ---------------------------------------------------------------------------------------- |
| Couverture du risque de change sur la créance de dividende reconnue | Oui sous conditions | Créance monétaire intragroupe et écart de change non totalement éliminé en consolidation |
| Refus automatique car flux intragroupe                              | Non                 | L’exception IFRS 9.6.3.6 doit être examinée                                              |
| Traitement comme transaction future intragroupe                     | Non                 | Une créance est déjà reconnue ; ce n’est plus une forecast transaction                   |
| Documentation sans test complet IFRS 9                              | Non                 | Documentation initiale, relation économique et hedge ratio requis                        |

**Review**
   - Ok to cover forex risk ✅
   - Not ok to for intragroup ✅
   - No to highly probable transaction because already accounted for ✅
   - Doesn't mention NIH which is surprising since there was some IFRIC 16 chunks ❌
   - 😱 says "Yes if" to fair-value hedge which is incorrect

#### k=10
##### e=10

_Retrieved chunks_
**ifrs-9**
- 1.1, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1.1, 3.1.2, 3.2.1, 4.1.2, 4.1.2A, 4.1.3, 4.1.4, 4.1.5, 4.2.1, 4.2.2, 4.3.1, 4.3.2, 4.3.3, 4.3.4, 4.3.5, 4.3.6, 4.3.7, 4.4.1, 4.4.2, 4.4.3, 5.1.1, 5.1.1A, 5.1.2, 5.1.3, 6.2.1, 6.2.2, 6.2.3, 6.2.4, 6.2.5, 6.2.6, 6.3.1, 6.3.2, 6.3.3, 6.3.4, 6.3.5, 6.3.6, 6.3.7, 6.4.1, 6.5.1, 6.5.2, 6.5.3, 6.5.4, 6.5.5, 6.5.6, 6.5.7, 6.5.8, 7.2.50, 7.2.53, 7.3.1, 7.3.2, 3, B2.1, B2.2, B2.3, B2.4, B2.5, B2.6, B3.1.1, B3.1.2, B3.1.2A, B3.1.3, B3.1.4, B3.1.5, B3.1.6, B3.2.1, B3.2.2, B3.2.3, B4.1.30, B4.1.31, B4.1.32, B4.1.33, B4.1.34, B4.1.35, B4.1.36, B4.3.1, B4.3.2, B4.3.3, B4.3.4, B4.3.5, B4.3.6, B4.3.7, B4.3.8, B4.3.9, B4.3.10, B4.3.11, B4.3.12, B4.4.1, B4.4.2, B5.7.1, B5.7.1A, B5.7.2, B5.7.2A, B5.7.3, B5.7.4, B5.7.5, B5.7.6, B5.7.7, B5.7.8, B5.7.9, B5.7.10, B5.7.11, B5.7.12, B5.7.13, B5.7.14, B5.7.15, B5.7.16, B5.7.17, B5.7.18, B5.7.19, B6.2.1, B6.2.2, B6.2.3, B6.2.4, B6.2.5, B6.2.6, B6.3.1, B6.3.2, B6.3.3, B6.3.4, B6.3.5, B6.3.6, B6.3.7, B6.3.8, B6.3.9, B6.3.10, B6.3.11, B6.3.12, B6.3.13, B6.3.14, B6.3.15, B6.3.16

**ifric-16**
- 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15


**Sections mentioned in answer**
   - 6.3.6
   - 6.3.5
   - 6.3.1
   - ifric-16 8
   - 6.2.3


**Summary table**
| Approche                                                                  | Applicable          | Condition clé                                                                              |
| ------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------ |
| Créance de dividende intragroupe déjà comptabilisée comme poste monétaire | Oui sous conditions | Écarts de change non entièrement éliminés en consolidation et impact en résultat consolidé |
| Dividende intragroupe comme transaction future                            | Non                 | Le risque de change devrait affecter le résultat consolidé                                 |
| Couverture en comptes individuels / séparés                               | Oui                 | Applicable au niveau social, pas automatiquement en consolidé                              |
| Couverture de net investment                                              | Non                 | Ne vise pas la créance de dividende elle-même                                              |

**Review**
   - Ok to cover forex risk ✅
   - Not ok to for intragroup ✅
   - No to highly probable transaction because already accounted for ✅
   - Doesn't mention fair value hedge
   - Mentions NIH but doesn't analyze it, considers it another track 🟠

#### k=30
##### e=5
###### f=30000

_Retrieved chunks_
- ifrs-9-financial-instruments 2025 required: 1.1, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.2.23, 3.3.1, 3.3.2, 3.3.3, 3.3.4, 3.3.5, 4.1.1, 4.1.2, 4.1.2A, 4.1.3, 4.1.4, 4.1.5, 4.2.1, 4.2.2, 4.3.1, 4.3.2, 4.3.3, 4.3.4, 4.3.5, 4.3.6, 4.3.7, 4.4.1, 4.4.2, 5.1.1A, 5.1.2, 5.1.3, 5.2.1, 5.2.2, 5.2.3, 5.3.1, 5.3.2, 5.4.1, 1, 5.4.2, 5.6.3, 5.6.4, 5.6.5, 5.6.6, 5.6.7, 5.7.1, 5.7.1A, 5.7.2, 5.7.3, 5.7.4, 5.7.5, 5.7.6, 5.7.7, 5.7.8, 5.7.9, 5.7.10, 5.7.11, 6.1.1, 6.2.6, 6.3.1, 6.3.2, 6.3.3, 6.3.4, 6.3.5, 6.3.6, 6.3.7, 6.4.1, 6.5.1, 6.5.2, 6.5.3, 6.5.14, 6.5.15, 6.5.16, 6.6.1, 6.6.2, 6.6.3, 6.6.4, 6.6.5, 6.6.6, 6.7.1, 6.7.2, 6.7.3, 6.7.4, 6.8.1, 6.8.2, 2, 6.8.3, 6.8.4, 6.8.5, 6.8.6, 6.8.7, 6.8.8, 6.9.1, 6.9.2, 6.9.3, 6.9.4, 6.9.5, 6.9.6, 6.9.7, 6.9.8, 6.9.9, 6.9.10, 6.9.11, 7.2.21, 7.2.22, 7.2.23, 7.2.24, 7.2.25, 7.2.26, 7.2.27, 7.2.28, 7.2.29, 7.2.30, 7.2.31, 7.2.49, 7.2.50, 7.2.53, 7.3.1, 7.3.2, 3, B2.1, B2.2, B2.3, B2.4, B2.5, B2.6, B3.1.1, B3.1.2, B3.1.2A, B3.1.3, B3.1.4, B3.2.12, B3.2.13, B3.2.14, B3.2.15, B3.2.16, B3.2.17, B3.3.1, B3.3.2, B3.3.3, B3.3.4, B3.3.5, B4.1.35, B4.1.36, B4.3.1, B4.3.2, B4.3.3, B4.3.4, B4.3.5, B4.3.6, B4.3.7, B4.3.8, B4.3.9, B4.3.10, B4.3.11, B4.3.12, B4.4.1, B4.4.2, 4, B4.4.3, B5.1.1, B5.5.53, B5.5.54, B5.5.55, B5.6.1, B5.6.2, B5.7.1, B5.7.1A, B5.7.2, B5.7.2A, B5.7.3, B5.7.4, B5.7.5, B5.7.6, B5.7.7, B5.7.8, B5.7.9, B5.7.10, B5.7.11, B5.7.12, B5.7.13, B5.7.14, B6.2.6, B6.3.1, B6.3.2, B6.3.3, B6.3.4, B6.3.5, B6.3.6, B6.3.7, B6.3.8, B6.3.9, B6.3.10, B6.3.11
- ifric-16-hedges-of-a-net-investment-in-a-foreign-operation: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18A, 18B, 19, AG1, AG2, AG3, AG4, AG5, AG6, AG7, AG8, AG9, AG10, AG11, AG12, AG13, AG14, AG15


**Sections mentioned in answer**
   - 6.3.1
   - 6.3.5
   - 6.3.6
   - 6.3.3

**Summary table**
| Approche                                                          | Applicable                     | Condition clé                                                                 |
| ----------------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------- |
| Couverture de la créance de dividende intragroupe reconnue        | Oui sous conditions            | Créance monétaire + écarts de change non totalement éliminés en consolidation |
| Couverture du dividende intragroupe comme simple flux intragroupe | Non                            | Les éléments intragroupe sont exclus sauf exception limitée                   |
| Couverture d’un dividende futur avant comptabilisation            | Non, sauf cas très particulier | Transaction hautement probable et impact en résultat consolidé                |
| Documentation incomplète ou tardive                               | Non                            | Documentation formelle à l’origine + critères d’efficacité                    |


**Review**
   - Ok to cover forex risk ✅
   - Not ok to for intragroup ✅
   - No to highly probable transaction because already accounted for ✅
   - Doesn't mention fair value hedge
   - No mention of NIH even though all of IFRIC 16 was in the prompt 😱
