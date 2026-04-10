# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Reformulation**:
>Identification of the hedge accounting model(s) that can apply in consolidated financial statements to foreign exchange risk arising from intragroup dividend-related positions and transactions.

## Documentation
**Consultée**
   - IAS (`ias24`)
   - IFRIC (`ifric16`)
   - IFRS (`ifrs10`, `ifrs9`)

**Retenue pour l'analyse**
   - IAS (`ias24`)
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`, `ifrs10`)

## Hypothèses
   - La question vise les états financiers consolidés d’un groupe qui n’est pas une entité d’investissement.
   - Le dividende intragroupe a donné lieu à la comptabilisation d’une créance et d’une dette intragroupe correspondante.
   - La couverture envisagée porte uniquement sur le risque de change lié à cette position intragroupe, et non sur une couverture d’investissement net dans une activité à l’étranger.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, un dividende intragroupe reconnu en créance/dette est en principe éliminé et ne peut pas, en tant que tel, fonder une relation de couverture. Une documentation n’est possible que si la créance/dette constitue un élément monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.

## Points Opérationnels

   - Au niveau consolidé, la créance et la dette de dividende intragroupe sont éliminées ; l’analyse doit donc porter uniquement sur le reliquat de risque de change non éliminé.
   - Le point de timing est déterminant : après reconnaissance de la créance, l’analyse relève d’un élément monétaire intragroupe, pas d’une transaction future hautement probable.
   - La documentation de couverture doit être calibrée sur la seule composante change affectant encore le résultat consolidé.
   - Si les deux entités ont la même monnaie fonctionnelle, la base IFRS pour une désignation en consolidation disparaît en pratique.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende est un élément monétaire intragroupe.<br>- Les entités concernées ont des monnaies fonctionnelles différentes.<br>- Le risque de change donne lieu à des gains ou pertes non totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende est un élément monétaire intragroupe.
   - Les entités concernées ont des monnaies fonctionnelles différentes.
   - Le risque de change donne lieu à des gains ou pertes non totalement éliminés en consolidation.

**Raisonnement**:
Dans cette situation, la créance de dividende intragroupe est en principe éliminée en consolidation avec la dette correspondante. Elle ne peut donc pas être couverte au niveau consolidé, sauf si elle constitue un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes, générant des écarts de change non totalement éliminés.

**Implications pratiques**: La documentation ne peut viser que la composante de change restant exposée au niveau du groupe, pas le dividende intragroupe éliminé en lui-même.

**Référence**:
 - ifrs9 6.3.5

    >For hedge accounting purposes, **only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items**. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs10 B86

    >Consolidated financial statements:
(a)combine like items of assets, liabilities, equity, income, expenses and cash flows of the parent with those of its subsidiaries.
(b)offset (eliminate) the carrying amount of the parent’s investment in each subsidiary and the parent’s portion of equity of each subsidiary (IFRS 3 explains how to account for any related goodwill).
(c)**eliminate in full intragroup assets and liabilities**, equity, income, expenses and cash flows relating to transactions between entities of the group (profits or losses resulting from intragroup transactions that are recognised in assets, such as inventory and fixed assets, are eliminated in full). Intragroup losses may indicate an impairment that requires recognition in the consolidated financial statements. IAS 12 Income Taxes applies to temporary differences that arise from the elimination of profits and losses resulting from intragroup transactions.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question porte sur un dividende intragroupe pour lequel une créance a déjà été comptabilisée. On n’est donc plus dans le cas d’une transaction intragroupe future hautement probable, mais d’une position reconnue. L’exception IFRS 9 relative aux transactions intragroupe futures ne correspond pas à ce fait générateur.

**Implications pratiques**: Ce modèle n’est pas le bon véhicule comptable une fois la créance de dividende déjà reconnue.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, **the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item** in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs10 B86

    >Consolidated financial statements:
(a)combine like items of assets, liabilities, equity, income, expenses and cash flows of the parent with those of its subsidiaries.
(b)offset (eliminate) the carrying amount of the parent’s investment in each subsidiary and the parent’s portion of equity of each subsidiary (IFRS 3 explains how to account for any related goodwill).
(c)**eliminate in full intragroup assets and liabilities**, equity, income, expenses and cash flows relating to transactions between entities of the group (profits or losses resulting from intragroup transactions that are recognised in assets, such as inventory and fixed assets, are eliminated in full). Intragroup losses may indicate an impairment that requires recognition in the consolidated financial statements. IAS 12 Income Taxes applies to temporary differences that arise from the elimination of profits and losses resulting from intragroup transactions.

### 3. Couverture d’un investissement net dans une activité à l’étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Cette approche vise le risque de change attaché à un investissement net dans une activité à l’étranger, non le risque de change d’un dividende intragroupe reconnu en créance. Le fait décrit est une position intragroupe ponctuelle, distincte d’une couverture d’investissement net au sens d’IFRIC 16.

**Implications pratiques**: Cette documentation ne convient pas pour couvrir une créance de dividende intragroupe en tant que telle.

**Référence**:
 - ifric16 7

    >This Interpretation applies to an entity that **hedges the foreign currency risk arising from its net investments in foreign operations** and wishes to qualify for hedge accounting in accordance with IFRS 9. For convenience this Interpretation refers to such an entity as a parent entity and to the financial statements in which the net assets of foreign operations are included as consolidated financial statements. All references to a parent entity apply equally to an entity that has a net investment in a foreign operation that is a joint venture, an associate or a branch.
 - ifric16 10

    >**Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.**