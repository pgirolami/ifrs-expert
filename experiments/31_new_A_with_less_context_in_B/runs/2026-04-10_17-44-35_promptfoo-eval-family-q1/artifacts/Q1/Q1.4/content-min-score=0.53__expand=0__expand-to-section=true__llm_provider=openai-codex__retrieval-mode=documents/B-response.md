# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Reformulation**:
>Which IFRS hedge accounting models are relevant in consolidated financial statements for foreign exchange risk on intragroup dividend-related positions, given the consolidation elimination rules and the IFRS 9 restrictions on intragroup hedged items.

## Documentation
**Consultée**
   - IAS (`ias24`, `ias27`)
   - IFRIC (`ifric16`)
   - IFRS (`ifrs10`, `ifrs9`)

**Retenue pour l'analyse**
   - IAS (`ias27`, `ias24`)
   - IFRIC (`ifric16`)
   - IFRS (`ifrs9`, `ifrs10`)

## Hypothèses
   - La question vise les états financiers consolidés du groupe, et non les états financiers individuels ou séparés.
   - Le dividende intragroupe a été déclaré et une créance intragroupe correspondante a été comptabilisée chez le bénéficiaire.
   - La couverture envisagée porte sur le risque de change attaché à cette créance/dividende intragroupe, et non sur une couverture d'investissement net dans une activité à l'étranger.
   - Aucune exception d'entité d'investissement au sens d'IFRS 10 n'est supposée applicable.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, le dividende intragroupe et la créance correspondante sont en principe éliminés. Une documentation de couverture n'est envisageable que si la créance intragroupe est un élément monétaire exposé à un risque de change dont les écarts ne sont pas intégralement éliminés en consolidation ; sinon, la réponse est non.

## Points Opérationnels

   - Il faut distinguer strictement les comptes consolidés des comptes individuels : en individuel, le dividende peut être reconnu ; en consolidation, il est éliminé.
   - Le point clé n'est pas l'existence de la créance en soi, mais le fait que son risque de change subsiste ou non après éliminations de consolidation.
   - Si la créance de dividende est libellée entre entités à monnaies fonctionnelles différentes, documenter précisément pourquoi les écarts de change ne sont pas totalement éliminés en consolidation.
   - La documentation doit viser la créance monétaire intragroupe et sa composante change résiduelle, et non le produit de dividende intragroupe éliminé.
   - En l'absence d'exposition de change résiduelle au niveau consolidé, aucune désignation de couverture ne peut être soutenue pour ce dividende intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende est un élément monétaire intragroupe<br>- les entités concernées ont des monnaies fonctionnelles différentes<br>- le risque de change génère des gains ou pertes non intégralement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende est un élément monétaire intragroupe
   - les entités concernées ont des monnaies fonctionnelles différentes
   - le risque de change génère des gains ou pertes non intégralement éliminés en consolidation

**Raisonnement**:
Dans cette situation, la créance née du dividende déclaré est un solde intragroupe reconnu, mais ce solde est éliminé en consolidation. Toutefois, IFRS 9 admet une exception pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation, notamment entre entités ayant des monnaies fonctionnelles différentes.

**Implications pratiques**: La documentation ne peut viser que la composante change résiduelle au niveau consolidé, pas le dividende intragroupe en tant que tel.

**Référence**:
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs10 B86

    >Consolidated financial statements:
(a)combine like items of assets, liabilities, equity, income, expenses and cash flows of the parent with those of its subsidiaries.
(b)offset (eliminate) the carrying amount of the parent’s investment in each subsidiary and the parent’s portion of equity of each subsidiary (IFRS 3 explains how to account for any related goodwill).
(c)**eliminate in full intragroup assets and liabilities, equity, income, expenses and cash flows** relating to transactions between entities of the group (profits or losses resulting from intragroup transactions that are recognised in assets, such as inventory and fixed assets, are eliminated in full). Intragroup losses may indicate an impairment that requires recognition in the consolidated financial statements. IAS 12 Income Taxes applies to temporary differences that arise from the elimination of profits and losses resulting from intragroup transactions.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question porte sur un dividende intragroupe déjà déclaré, avec créance reconnue : il ne s'agit donc plus d'une transaction future hautement probable. En outre, en consolidation, les dividendes intragroupe sont éliminés et IFRS 9 ne permet l'exception sur transaction intragroupe future qu'en cas d'effet sur le résultat consolidé, ce qui n'est pas le cas d'un dividende intragroupe éliminé.

**Implications pratiques**: Une désignation en cash flow hedge n'est pas appropriée pour une créance de dividende intragroupe déjà constatée.

**Référence**:
 - ifrs9 6.3.5

    >For hedge accounting purposes, **only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity** can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ifrs10 B86

    >Consolidated financial statements:
(a)combine like items of assets, liabilities, equity, income, expenses and cash flows of the parent with those of its subsidiaries.
(b)offset (eliminate) the carrying amount of the parent’s investment in each subsidiary and the parent’s portion of equity of each subsidiary (IFRS 3 explains how to account for any related goodwill).
(c)**eliminate in full intragroup assets and liabilities, equity, income, expenses and cash flows** relating to transactions between entities of the group (profits or losses resulting from intragroup transactions that are recognised in assets, such as inventory and fixed assets, are eliminated in full). Intragroup losses may indicate an impairment that requires recognition in the consolidated financial statements. IAS 12 Income Taxes applies to temporary differences that arise from the elimination of profits and losses resulting from intragroup transactions.

### 3. Couverture d'un investissement net dans une activité à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le fait générateur décrit est un dividende intragroupe avec créance reconnue, donc un solde intragroupe ponctuel, et non l'exposition de conversion sur un investissement net dans une activité à l'étranger. Le modèle IFRIC 16 vise un risque différent, attaché aux net assets d'une activité étrangère dans les comptes consolidés.

**Implications pratiques**: Ce modèle ne répond pas à la question posée sur la composante change d'un dividende intragroupe déclaré.

**Référence**:
 - ifric16 7

    >This Interpretation applies to an entity that **hedges the foreign currency risk arising from its net investments in foreign operations** and wishes to qualify for hedge accounting in accordance with IFRS 9. For convenience this Interpretation refers to such an entity as a parent entity and to the financial statements in which the net assets of foreign operations are included as consolidated financial statements. All references to a parent entity apply equally to an entity that has a net investment in a foreign operation that is a joint venture, an associate or a branch.
 - ifric16 10

    >Hedge accounting may be applied **only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency**.