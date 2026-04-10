# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Le risque de change attaché à des dividendes intragroupe comptabilisés en créance à recevoir peut-il faire l’objet d’une relation de couverture formellement documentée au niveau des états financiers consolidés ?

**Reformulation**:
>Whether foreign currency risk arising from an intragroup dividend receivable can be designated as a hedged item in a formally documented hedge relationship in consolidated financial statements under IFRS 9 hedge accounting.

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
   - Le dividende intragroupe a déjà été déclaré et comptabilisé en créance à recevoir dans les comptes individuels, de sorte qu'il s'agit d'un poste monétaire intragroupe reconnu.
   - La question vise les états financiers consolidés du groupe, et non les états financiers individuels ou séparés.
   - La créance de dividende est libellée dans une devise pouvant créer un risque de change entre entités du groupe.

## Recommandation

**OUI SOUS CONDITIONS**

Au niveau consolidé, un dividende intragroupe comptabilisé en créance n'est éligible à la couverture que via l'exception IFRS 9 applicable aux postes monétaires intragroupe. Cela suppose que le risque de change ne soit pas totalement éliminé en consolidation, typiquement entre entités de monnaies fonctionnelles différentes.

## Points Opérationnels

   - Vérifier d'abord si la créance de dividende est bien un poste monétaire intragroupe au sens d'IAS 21 dans les faits retenus.
   - Confirmer au niveau consolidé que les entités porteuse et débitrice ont des monnaies fonctionnelles différentes et que l'écart de change affecte le résultat consolidé.
   - La documentation de couverture doit être établie au niveau des états financiers consolidés visés par la question.
   - Si le dividende était seulement prévu mais non encore comptabilisé, l'analyse relèverait potentiellement de la transaction intragroupe hautement probable, ce qui n'est pas le cas ici.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende constitue un poste monétaire intragroupe.<br>- Les entités concernées ont des monnaies fonctionnelles différentes.<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende constitue un poste monétaire intragroupe.
   - Les entités concernées ont des monnaies fonctionnelles différentes.
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.

**Raisonnement**:
La créance de dividende est, dans la situation décrite, un actif reconnu. En consolidé, IFRS 9 exclut en principe les éléments intragroupe, mais admet une exception pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. IAS 21 précise que cela se produit pour un poste monétaire intragroupe entre entités de monnaies fonctionnelles différentes.

**Implications pratiques**: Une relation de couverture formellement documentée est envisageable au niveau consolidé seulement si l'exposition de change subsiste réellement après consolidation.

**Référence**:
 - ifrs9 6.3.5

    >For hedge accounting purposes, **only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity** can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.
 - ias21 45

    >The incorporation of the results and financial position of a foreign operation with those of the reporting entity follows normal consolidation procedures, such as the elimination of intragroup balances and intragroup transactions of a subsidiary (see IFRS 10 Consolidated Financial Statements). However, an intragroup monetary asset (or liability), whether short‑term or long‑term, cannot be eliminated against the corresponding intragroup liability (or asset) without showing the results of currency fluctuations in the consolidated financial statements. This is because the monetary item represents a commitment to convert one currency into another and exposes the reporting entity to a gain or loss through currency fluctuations. Accordingly, in the consolidated financial statements of the reporting entity, such an exchange difference is recognised in profit or loss or, if it arises from the circumstances described in paragraph 32, it is recognised in other comprehensive income and accumulated in a separate component of equity until the disposal of the foreign operation.

### 2. Couverture de flux de trésorerie

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
La question porte sur des dividendes intragroupe déjà comptabilisés en créance à recevoir. Il ne s'agit donc pas d'une transaction future hautement probable, mais d'un actif reconnu. Le modèle de couverture de flux de trésorerie vise les transactions prévues, non une créance déjà constatée.

**Implications pratiques**: Ce modèle n'est pas adapté si le dividende est déjà enregistré en créance au moment de la désignation.

**Référence**:
 - ifrs9 6.3.1

    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, **the foreign currency risk of a highly probable forecast intragroup transaction may qualify** as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d'un investissement net à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le risque visé ici porte sur une créance de dividende intragroupe, non sur l'exposition de change attachée à un investissement net dans une activité étrangère. IFRIC 16 réserve ce modèle aux différences de change entre la monnaie fonctionnelle de l'activité étrangère et celle de l'entité mère concernée. La créance de dividende ne correspond pas à cet objet de couverture.

**Implications pratiques**: La désignation doit être analysée comme couverture d'un poste monétaire intragroupe, pas comme couverture d'investissement net.

**Référence**:
 - ifric16 10

    >Hedge accounting may be applied **only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency**.
 - ifric16 7

    >This Interpretation applies to an entity that **hedges the foreign currency risk arising from its net investments in foreign operations** and wishes to qualify for hedge accounting in accordance with IFRS 9. For convenience this Interpretation refers to such an entity as a parent entity and to the financial statements in which the net assets of foreign operations are included as consolidated financial statements. All references to a parent entity apply equally to an entity that has a net investment in a foreign operation that is a joint venture, an associate or a branch.