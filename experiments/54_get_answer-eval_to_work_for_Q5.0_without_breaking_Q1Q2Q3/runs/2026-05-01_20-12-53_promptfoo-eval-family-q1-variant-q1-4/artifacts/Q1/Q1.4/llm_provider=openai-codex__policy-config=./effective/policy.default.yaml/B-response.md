# Analyse d'une question comptable

**Date**: 2026-05-01

## Question

**Utilisateur**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Reformulation**:
>Déterminer, en comptes consolidés, quelles familles de relations de couverture IFRS peuvent théoriquement accueillir la composante de risque de change liée à un dividende intragroupe lorsqu’une créance correspondante a été comptabilisée.

## Documentation
**Consultée**
   - IAS-S (standard) (`ias39`, `ias21`)
   - IFRIC (interpretation) (`ifric16`)
   - IFRS-S (standard) (`ifrs9`, `ifrs7`)

**Retenue pour l'analyse**
   - IAS-S (standard) (`ias21`)
   - IFRIC (interpretation) (`ifric16`)
   - IFRS-S (standard) (`ifrs9`)

## Hypothèses
   - La créance de dividende intragroupe a été comptabilisée et constitue un élément monétaire entre deux entités du groupe.
   - La question vise les comptes consolidés et un risque de change qui subsiste en consolidation parce que les entités concernées ont des monnaies fonctionnelles différentes.
   - La créance de dividende est destinée à être réglée dans le cadre normal et ne fait pas partie d'un investissement net dans une activité étrangère.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une désignation est envisageable si la créance de dividende reconnue est un élément monétaire intragroupe dont le risque de change n'est pas totalement éliminé en consolidation. Dans ce cas, la voie la plus cohérente est la couverture de juste valeur ; la couverture d'investissement net ne convient pas au dividende à régler.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes.<br>- Le risque de change sur cette créance n'est pas totalement éliminé en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes.
   - Le risque de change sur cette créance n'est pas totalement éliminé en consolidation.

**Raisonnement**:
Une fois le dividende déclaré, la question porte sur une créance reconnue ; IFRS 9 vise précisément une couverture de juste valeur d'un actif reconnu exposé à un risque particulier (IFRS 9 6.5.2(a)). En consolidation, l'exception d'IFRS 9 permet de désigner un élément monétaire intragroupe comme élément couvert si le risque de change génère des écarts non totalement éliminés, ce qui renvoie aux écarts de conversion conservés en consolidation par IAS 21 (IFRS 9 6.3.6 ; IAS 21 45).

**Implications pratiques**: La documentation peut viser le risque de change de la créance intragroupe reconnue en consolidation, sous réserve que l'exposition subsiste effectivement au niveau consolidé.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs9 6.5.2(a)

    >There are three types of hedging relationships: **(a) fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability or an unrecognised firm commitment, or a component of any such item, that is attributable to a particular risk and could affect profit or loss.**
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le fait déterminant de la question est qu'une créance a déjà été reconnue : l'exposition n'est donc plus formulée comme une transaction intragroupe hautement probable, mais comme un actif monétaire existant. IFRS 9 6.3.6 mentionne bien les transactions intragroupe hautement probables, mais ici ce stade est dépassé ; la référence spécifique à la créance reconnue oriente vers l'exception sur l'élément monétaire intragroupe et non vers une couverture de flux (IFRS 9 6.3.6 ; IFRS 9 6.5.2(b)).

**Implications pratiques**: Pour le fait décrit, la documentation ne devrait pas être fondée sur un modèle de couverture de flux de trésorerie du dividende intragroupe déjà devenu créance.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs9 6.5.2(b)

    >There are three types of hedging relationships: **(b) cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability (such as all or some future interest payments on variable-rate debt) or a highly probable forecast transaction, and could affect profit or loss.**

### 3. Couverture d'investissement net

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La couverture d'investissement net vise le risque de change entre la monnaie fonctionnelle de l'activité étrangère et celle de la société mère sur l'investissement net lui-même, non une créance de dividende destinée à être réglée (IFRS 9 6.5.2(c) ; IFRIC 16 10). IAS 21 réserve le traitement OCI aux éléments monétaires faisant partie de l'investissement net ; une créance de dividende reconnue correspond au contraire à un règlement attendu et ne s'inscrit pas, dans les faits décrits, dans cette catégorie (IAS 21 32 ; IAS 21 45).

**Implications pratiques**: Le dividende intragroupe reconnu comme créance ne doit pas être documenté comme couverture d'investissement net dans la situation décrite.

**Référence**:
 - ifrs9 6.5.2(c)

    >There are three types of hedging relationships: **(c) hedge of a net investment in a foreign operation as defined in IAS 21.**
 - ifric16 10

    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - ias21 32

    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation (see paragraph 15) shall be recognised in profit or loss in the separate financial statements of the reporting entity or the individual financial statements of the foreign operation, as appropriate. In the financial statements that include the foreign operation and the reporting entity (eg consolidated financial statements when the foreign operation is a subsidiary), such exchange differences shall be recognised initially in other comprehensive income and reclassified from equity to profit or loss on disposal of the net investment in accordance with paragraph 48.
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.