# Analyse d'une question comptable

**Date**: 2026-04-10

## Question

**Utilisateur**:
>Le risque de change attaché à des dividendes intragroupe comptabilisés en créance à recevoir peut-il faire l’objet d’une relation de couverture formellement documentée au niveau des états financiers consolidés ?

**Reformulation**:
>Whether foreign currency risk on an intragroup dividend receivable can qualify as a hedged item in hedge accounting at the consolidated financial statement level.

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
   - Les dividendes intragroupe sont déjà comptabilisés en créance à recevoir, donc la question porte sur un poste monétaire reconnu et non sur une transaction future.
   - La question vise les états financiers consolidés du groupe.
   - La créance de dividende est libellée dans une devise qui peut différer de la monnaie fonctionnelle de l'entité concernée.

## Recommandation

**OUI SOUS CONDITIONS**

Au niveau consolidé, un dividende intragroupe comptabilisé en créance à recevoir ne peut être couvert que via l'exception IFRS 9 applicable aux postes monétaires intragroupe exposés à un risque de change non totalement éliminé en consolidation. En pratique, cela suppose un poste monétaire entre entités de monnaies fonctionnelles différentes, avec un effet de change qui subsiste dans le résultat consolidé.

## Points Opérationnels

   - La première vérification porte sur la nature monétaire de la créance de dividende et sur son existence à la date de désignation.
   - Au niveau consolidé, il faut démontrer que l'écart de change sur la créance intragroupe n'est pas intégralement éliminé et affecte bien le résultat consolidé.
   - Si les deux entités ont la même monnaie fonctionnelle, l'exception IFRS 9 6.3.6 ne joue pas.
   - La relation de couverture doit être documentée formellement au niveau consolidé, en ciblant uniquement le risque de change éligible.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit constituer un poste monétaire intragroupe.<br>- Les entités concernées doivent avoir des monnaies fonctionnelles différentes.<br>- Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation et affecter le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur

**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit constituer un poste monétaire intragroupe.
   - Les entités concernées doivent avoir des monnaies fonctionnelles différentes.
   - Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation et affecter le résultat consolidé.

**Raisonnement**:
Ici, la créance de dividende est un actif reconnu, ce qui correspond en principe à une catégorie de hedged item. Toutefois, en consolidé, un élément intragroupe est en principe exclu, sauf pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Si la créance de dividende est un poste monétaire entre entités à monnaies fonctionnelles différentes, avec un impact résiduel en résultat consolidé, une relation formellement documentée est possible.

**Implications pratiques**: La documentation de couverture au niveau consolidé est envisageable seulement pour le risque de change qui subsiste réellement après consolidation.

**Référence**:
 - ifrs9 6.3.1

    >**A hedged item can be a recognised asset or liability**, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
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
La question décrit des dividendes déjà comptabilisés en créance à recevoir. Il ne s'agit donc pas d'une transaction future hautement probable mais d'un actif reconnu. L'approche cash flow hedge identifiée pour les expositions sur flux futurs ne correspond pas à cette situation précise.

**Implications pratiques**: Cette voie n'est pas adaptée à une créance de dividende déjà enregistrée.

**Référence**:
 - ifrs9 6.3.1

    >**A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction** or a net investment in a foreign operation. The hedged item can be:
(a)a single item; or
(b)a group of items (subject to paragraphs 6.6.1⁠–⁠6.6.6 and B6.6.1⁠–⁠B6.6.16).
A hedged item can also be a component of such an item or group of items (see paragraphs 6.3.7 and B6.3.7⁠–⁠B6.3.25).
 - ifrs9 6.3.5

    >For hedge accounting purposes, only assets, liabilities, **firm commitments or highly probable forecast transactions** with a party external to the reporting entity can be designated as hedged items. Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements of those entities and not in the consolidated financial statements of the group, except for the consolidated financial statements of an investment entity, as defined in IFRS 10, where transactions between an investment entity and its subsidiaries measured at fair value through profit or loss will not be eliminated in the consolidated financial statements.
 - ifrs9 6.3.6

    >However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation in accordance with IAS 21 The Effects of Changes in Foreign Exchange Rates. In accordance with IAS 21, foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation when the intragroup monetary item is transacted between two group entities that have different functional currencies. In addition, **the foreign currency risk of a highly probable forecast intragroup transaction may qualify** as a hedged item in consolidated financial statements provided that the transaction is denominated in a currency other than the functional currency of the entity entering into that transaction and the foreign currency risk will affect consolidated profit or loss.

### 3. Couverture d'un investissement net à l'étranger

**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnement**:
Le risque visé ici porte sur une créance de dividende intragroupe reconnue, non sur l'investissement net dans une activité à l'étranger. IFRIC 16 réserve ce modèle au risque de change entre la monnaie fonctionnelle de l'activité étrangère et celle de la société mère. Ce cadre ne traite pas la couverture d'un dividende intragroupe à recevoir.

**Implications pratiques**: Le modèle de couverture d'investissement net ne doit pas être utilisé pour une créance de dividende intragroupe.

**Référence**:
 - ifric16 7

    >This Interpretation applies to an entity that **hedges the foreign currency risk arising from its net investments in foreign operations** and wishes to qualify for hedge accounting in accordance with IFRS 9. For convenience this Interpretation refers to such an entity as a parent entity and to the financial statements in which the net assets of foreign operations are included as consolidated financial statements. All references to a parent entity apply equally to an entity that has a net investment in a foreign operation that is a joint venture, an associate or a branch.
 - ifric16 10

    >Hedge accounting may be applied **only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency**.
 - ifric16 14

    >A derivative or a non-derivative instrument (or a combination of derivative and non-derivative instruments) **may be designated as a hedging instrument in a hedge of a net investment in a foreign operation**. The hedging instrument(s) may be held by any entity or entities within the group, as long as the designation, documentation and effectiveness requirements of IFRS 9 paragraph 6.4.1 that relate to a net investment hedge are satisfied. In particular, the hedging strategy of the group should be clearly documented because of the possibility of different designations at different levels of the group.