# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Peut-on désigner, dans les comptes consolidés, le risque de change afférent à des dividendes intragroupe donnant lieu à la comptabilisation d’une créance à recevoir dans une relation de couverture documentée ?

**Reformulation**:
>Which IFRS hedge accounting model can apply in consolidated financial statements to foreign currency risk on an intragroup dividend-related receivable or forecast intragroup dividend cash flow.

## Documentation
**Consultée**
   - IAS (`ias21`)
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

**Retenue pour l'analyse**
   - IAS (`ias21`)
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`)

## Hypothèses
   - La question vise les comptes consolidés du groupe.
   - Le dividende intragroupe a déjà été décidé de sorte qu'une créance intragroupe à recevoir est comptabilisée à la date d'analyse.
   - La créance est un poste monétaire en devise entre entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que des écarts de change ne sont pas intégralement éliminés en consolidation.
   - La relation de couverture est documentée conformément au modèle de comptabilité de couverture d'IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, dans les comptes consolidés, le risque de change d'une créance intragroupe de dividende peut être désigné si cette créance monétaire génère des écarts de change non totalement éliminés en consolidation. En revanche, la logique pertinente ici est celle d'un poste monétaire reconnu, non celle d'une transaction future ni d'une couverture d'investissement net.

## Points Opérationnels

   - Le point clé est le moment de désignation : une fois la créance de dividende comptabilisée, l'analyse se fait comme pour un poste monétaire reconnu.
   - En consolidation, la désignation n'est admise que si le risque de change de la créance intragroupe affecte encore le résultat consolidé.
   - Il faut vérifier les monnaies fonctionnelles des deux entités ; c'est ce différentiel qui fonde la non-élimination des écarts de change.
   - La documentation doit être rédigée au niveau des comptes consolidés et cibler explicitement le risque de change de la créance intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire intragroupe.<br>- Les entités concernées ont des monnaies fonctionnelles différentes.<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire intragroupe.
   - Les entités concernées ont des monnaies fonctionnelles différentes.
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.

**Raisonnement**:
Ici, il existe une créance intragroupe déjà comptabilisée. IFRS 9 permet en consolidation de désigner un poste intragroupe monétaire uniquement si le risque de change crée des gains ou pertes non entièrement éliminés ; IAS 21 confirme que, dans ce cas, l'effet de change subsiste en comptes consolidés. La désignation est donc possible dans cette situation seulement si cette condition de non-élimination est satisfaite.

**Implications pratiques**: La documentation de couverture doit viser le risque de change de la créance intragroupe reconnue au niveau consolidé.

**Référence**:
 - ifrs9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche vise une transaction future intragroupe hautement probable. Or, dans la situation posée, le dividende a déjà donné lieu à la comptabilisation d'une créance à recevoir ; le sujet n'est donc plus un flux futur non reconnu mais un poste monétaire existant. Cette approche ne correspond pas au fait décrit.

**Implications pratiques**: Ce modèle ne serait pertinent qu'avant la constatation de la créance, au stade d'une transaction intragroupe future hautement probable affectant le résultat consolidé.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.3

    >If a hedged item is a forecast transaction (or a component thereof), **that transaction must be highly probable**.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, **the foreign currency risk of a highly probable forecast intragroup transaction may qualify** as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d'investissement net

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question porte sur une créance de dividende intragroupe, pas sur le risque de change attaché à un investissement net dans une activité à l'étranger. Le régime IAS 21 / IFRIC 16 concerne les différences de change sur l'investissement net et leur comptabilisation en OCI, ce qui est distinct du cas d'une créance de dividende reconnue.

**Implications pratiques**: Le modèle de couverture d'investissement net ne doit pas être utilisé pour une simple créance de dividende intragroupe.

**Référence**:
 - ias21 32

    >Exchange differences arising on a monetary item that **forms part of a reporting entity’s net investment in a foreign operation** (see paragraph 15) shall be recognised in profit or loss in the separate financial statements of the reporting entity or the individual financial statements of the foreign operation, as appropriate. In the financial statements that include the foreign operation and the reporting entity (eg consolidated financial statements when the foreign operation is a subsidiary), such exchange differences shall be recognised initially in other comprehensive income and reclassified from equity to profit or loss on disposal of the net investment in accordance with paragraph 48.
 - ifric16 10

    >Hedge accounting may be applied **only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency**.
 - ifric16 3

    >IFRS 9 requires the designation of an eligible hedged item and eligible hedging instruments in a hedge accounting relationship. If there is a designated hedging relationship, **in the case of a net investment hedge**, the gain or loss on the hedging instrument that is determined to be an effective hedge of the net investment is recognised in other comprehensive income and is included with the foreign exchange differences arising on translation of the results and financial position of the foreign operation.