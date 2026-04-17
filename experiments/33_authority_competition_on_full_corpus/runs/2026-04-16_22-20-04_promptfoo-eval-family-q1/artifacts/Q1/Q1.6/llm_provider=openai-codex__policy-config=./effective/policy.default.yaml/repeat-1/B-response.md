# Analyse d'une question comptable

**Date**: 2026-04-17

## Question

**Utilisateur**:
>Dans les comptes consolidés, la variation de change relative à des dividendes intragroupe pour lesquels un receivable a été constaté est-elle éligible à une désignation en comptabilité de couverture ?

**Reformulation**:
>Éligibilité, dans les comptes consolidés, d’un dividende intragroupe constaté en créance comme élément couvert au titre de la comptabilité de couverture du risque de change

## Documentation
**Consultée**
   - IAS-S (standard) (`ias39`, `ias12`, `ias21`, `ias32`, `ias7`, `ias27`, `ias33`, `ias10`, `ias19`, `ias29`, `ias38`, `ias24`, `ias20`, `ias37`, `ias40-bciasc`)
   - IFRIC (interpretation) (`ifric17`, `ifric2`, `ifric16`)
   - IFRS-S (standard) (`ifrs19`, `ifrs3`)
   - SIC (interpretation) (`sic25`)

**Retenue pour l'analyse**
   - IAS-S (standard) (`ias39`, `ias21`)
   - IFRIC (interpretation) (`ifric16`)

## Hypothèses
   - Le dividende intragroupe a déjà été constaté en créance dans les comptes individuels, de sorte que l’exposition visée est celle d’un élément monétaire existant et non celle d’une transaction future.
   - La question porte sur les comptes consolidés du groupe, et non sur les comptes individuels ou séparés.
   - Aucune information n’indique que la créance de dividende fasse partie d’un investissement net dans une activité à l’étranger au sens d’IAS 21.

## Recommandation

**OUI SOUS CONDITIONS**

Dans les comptes consolidés, une créance de dividende intragroupe n’est éligible comme élément couvert que si elle constitue un élément monétaire intragroupe exposé à un risque de change qui n’est pas entièrement éliminé en consolidation. À défaut, l’intragroupe n’est pas désignable en comptabilité de couverture.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un élément monétaire intragroupe.<br>- Les entités concernées doivent avoir des monnaies fonctionnelles différentes.<br>- Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un élément monétaire intragroupe.
   - Les entités concernées doivent avoir des monnaies fonctionnelles différentes.
   - Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation.

**Raisonnement**:
Une créance de dividende déjà comptabilisée est, dans cette situation, un actif reconnu, donc potentiellement un élément couvert au titre d’une couverture de juste valeur selon IAS 39.78 et IAS 39.89. Toutefois, en consolidation, IAS 39.80 exclut en principe les éléments intragroupe, sauf pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés ; IAS 21.45 précise que cela vise les éléments monétaires intragroupe entre entités ayant des monnaies fonctionnelles différentes.

**Implications pratiques**: Si ces conditions sont remplies, la variation de change de la créance peut être désignée comme risque couvert en consolidation dans une relation de couverture de juste valeur.

**Référence**:
 - ias39 78

    >**A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a highly probable forecast transaction or a net investment in a foreign operation. The hedged item can be (a) a single asset, liability, firm commitment, highly probable forecast transaction or net investment in a foreign operation, (b) a group of assets, liabilities, firm commitments, highly probable forecast transactions or net investments in foreign operations with similar risk characteristics [Refer: paragraphs 83 and 84]or (c) in a portfolio hedge of interest rate risk only, a portion of the portfolio of financial assets or financial liabilities that share the risk being hedged.**
 - ias39 80

    >For hedge accounting purposes, only assets, liabilities, firm commitments or highly probable forecast transactions that involve a party external to the entity can be designated as hedged items. It follows that hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements. As an exception, the foreign currency risk of an intragroup monetary item (eg a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ias39 89

    >**If a fair value hedge meets the conditions in paragraph 88 during the period, it shall be accounted for as follows:
(a)the gain or loss from remeasuring the hedging instrument at fair value (for a derivative hedging instrument) or the foreign currency component of its carrying amount measured in accordance with IAS 21 (for a non‑derivative hedging instrument) shall be recognised in profit or loss; and
(b)the gain or loss on the hedged item attributable to the hedged risk shall adjust the carrying amount of the hedged item and be recognised in profit or loss. This applies if the hedged item is otherwise measured at cost. Recognition of the gain or loss attributable to the hedged risk in profit or loss applies if the hedged item is a financial asset measured at fair value through other comprehensive income in accordance with paragraph 4.1.2A of IFRS 9.**
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, [Refer: IFRS 10 paragraph B86]such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question vise la variation de change sur des dividendes intragroupe pour lesquels une créance a déjà été constatée ; il ne s’agit donc pas d’une transaction future hautement probable mais d’un actif déjà reconnu. Or IAS 39.78 réserve ce modèle aux flux variables d’une transaction prévue ou d’un autre élément éligible, et IAS 39.95-100 traite le recyclage des montants de couverture liés à des flux futurs, ce qui ne correspond pas à cette situation.

**Implications pratiques**: La couverture de flux de trésorerie n’est pas le modèle adapté pour une créance de dividende déjà comptabilisée en consolidation.

**Référence**:
 - ias39 78

    >**A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a highly probable forecast transaction or a net investment in a foreign operation. The hedged item can be (a) a single asset, liability, firm commitment, highly probable forecast transaction or net investment in a foreign operation, (b) a group of assets, liabilities, firm commitments, highly probable forecast transactions or net investments in foreign operations with similar risk characteristics [Refer: paragraphs 83 and 84]or (c) in a portfolio hedge of interest rate risk only, a portion of the portfolio of financial assets or financial liabilities that share the risk being hedged.**
 - ias39 95

    >**If a cash flow hedge meets the conditions in paragraph 88 during the period, it shall be accounted for as follows:
(a)the portion of the gain or loss on the hedging instrument that is determined to be an effective hedge (see paragraph 88) shall be recognised in other comprehensive income; and
(b)the ineffective portion of the gain or loss on the hedging instrument shall be recognised in profit or loss.**
 - ias39 97

    >**If a hedge of a forecast transaction subsequently results in the recognition of a financial asset or a financial liability, the associated gains or losses that were recognised in other comprehensive income in accordance with paragraph 95 shall be reclassified from equity to profit or loss as a reclassification adjustment (see IAS 1 (as revised in 2007)) in the same period or periods during which the hedged forecast cash flows affect profit or loss (such as in the periods that interest income or interest expense is recognised). However, if an entity expects that all or a portion of a loss recognised in other comprehensive income will not be recovered in one or more future periods, it shall reclassify into profit or loss as a reclassification adjustment the amount that is not expected to be recovered.**
 - ias39 100

    >**For cash flow hedges other than those covered by paragraphs 97 and 98, amounts that had been recognised in other comprehensive income shall be reclassified from equity to profit or loss as a reclassification adjustment (see IAS 1 (revised 2007)) in the same period or periods during which the hedged forecast cash flows affect profit or loss (for example, when a forecast sale occurs).**

### 3. Couverture d’un investissement net dans une activité à l’étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le fait décrit est une créance de dividende intragroupe constatée, non un investissement net dans une activité à l’étranger. IAS 39.78 identifie la couverture d’investissement net comme un modèle distinct ; IAS 21.32 et IFRIC 16.14-15 le rattachent aux éléments monétaires faisant partie de l’investissement net et aux écarts reconnus en OCI, ce qui n’est pas établi ici.

**Implications pratiques**: Sauf démonstration distincte que la créance fait partie d’un investissement net, ce modèle ne s’applique pas au dividende intragroupe à recevoir.

**Référence**:
 - ias39 78

    >**A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a highly probable forecast transaction or a net investment in a foreign operation. The hedged item can be (a) a single asset, liability, firm commitment, highly probable forecast transaction or net investment in a foreign operation, (b) a group of assets, liabilities, firm commitments, highly probable forecast transactions or net investments in foreign operations with similar risk characteristics [Refer: paragraphs 83 and 84]or (c) in a portfolio hedge of interest rate risk only, a portion of the portfolio of financial assets or financial liabilities that share the risk being hedged.**
 - ias21 32

    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation (see paragraph 15) shall be recognised in profit or loss in the separate financial statements of the reporting entity or the individual financial statements of the foreign operation, as appropriate. In the financial statements that include the foreign operation and the reporting entity (eg consolidated financial statements when the foreign operation is a subsidiary), such exchange differences shall be recognised initially in other comprehensive income and reclassified from equity to profit or loss on disposal of the net investment in accordance with paragraph 48.
 - ifric16 14

    >**A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) may be designated as a hedging instrument in a hedge of a net investment in a foreign operation. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.**
 - ifric16 15

    >**For the purpose of assessing effectiveness, the change in value of the hedging instrument in respect of foreign exchange risk is computed by reference to the functional currency of the parent entity against whose functional currency the hedged risk is measured, in accordance with the hedge accounting documentation. Depending on where the hedging instrument is held, in the absence of hedge accounting the total change in value might be recognised in profit or loss, in other comprehensive income, or both. However, the assessment of effectiveness is not affected by whether the change in value of the hedging instrument is recognised in profit or loss or in other comprehensive income. As part of the application of hedge accounting, the total effective portion of the change is included in other comprehensive income. The assessment of effectiveness is not affected by whether the hedging instrument is a derivative or a non‑derivative instrument or by the method of consolidation.**