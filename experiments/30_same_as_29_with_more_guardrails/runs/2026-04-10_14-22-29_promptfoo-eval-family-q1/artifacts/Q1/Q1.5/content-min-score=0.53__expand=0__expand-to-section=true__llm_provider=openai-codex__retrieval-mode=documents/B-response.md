# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Le risque de change attaché à des dividendes intragroupe comptabilisés en créance à recevoir peut-il faire l’objet d’une relation de couverture formellement documentée au niveau des états financiers consolidés ?

**Documentation consultée**
   - `ifrs9`
   - `ias21`
   - `ifrs19`
   - `ifrs7`
   - `ifric16`
   - `ias32`
   - `sic25`
   - `ifric17`
   - `ifric2`
   - `ifrs12`
   - `ias7`
   - `ias37`
   - `sic7`

## Hypothèses
   - Le dividende intragroupe a déjà été déclaré et comptabilisé en créance à recevoir dans les comptes individuels de l'entité bénéficiaire.
   - La créance et la dette intragroupe correspondante sont libellées dans une devise créant un risque de change entre deux entités du groupe ayant des monnaies fonctionnelles différentes.
   - Le risque visé est celui qui affecte le résultat consolidé via les écarts de change sur cet élément monétaire intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

Au niveau consolidé, cela peut être documenté en couverture si la créance de dividende constitue un élément monétaire intragroupe dont le risque de change n'est pas entièrement éliminé en consolidation. Dans ce cas, la voie pertinente est la fair value hedge ; les modèles cash flow hedge et net investment hedge ne correspondent pas aux faits décrits.

## Points Opérationnels

   - Le point clé en consolidation est de démontrer que la créance de dividende est bien un élément monétaire intragroupe générant un écart de change non entièrement éliminé.
   - Si la créance est déjà reconnue, l'analyse doit être faite à la date de désignation sur un poste existant, non comme transaction future.
   - La documentation de couverture doit être établie au niveau des états financiers consolidés, puisque l'exception IFRS 9 pour les éléments intragroupe est appréciée à ce niveau.
   - Si les entités concernées ont la même monnaie fonctionnelle, la base IFRS permettant la désignation en consolidation disparaît en pratique.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un élément monétaire intragroupe.<br>- Les deux entités du groupe doivent avoir des monnaies fonctionnelles différentes.<br>- Les écarts de change sur cette créance doivent affecter le résultat consolidé car ils ne sont pas entièrement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un élément monétaire intragroupe.
   - Les deux entités du groupe doivent avoir des monnaies fonctionnelles différentes.
   - Les écarts de change sur cette créance doivent affecter le résultat consolidé car ils ne sont pas entièrement éliminés en consolidation.

**Raisonnment**:
La question vise une créance de dividende déjà comptabilisée : il s'agit donc d'un actif reconnu, ce qui correspond à la famille des fair value hedges. En consolidation, IFRS 9 exclut en principe les éléments intragroupe, mais prévoit une exception pour le risque de change d'un élément monétaire intragroupe s'il génère des écarts de change non totalement éliminés ; IAS 21 confirme que ces écarts subsistent en consolidation entre entités à monnaies fonctionnelles différentes.

**Implications pratiques**: La relation de couverture peut être formellement documentée au niveau consolidé si elle cible ce risque de change résiduel sur la créance intragroupe.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les cash flow hedges visent notamment des transactions prévues hautement probables. Or, dans la situation posée, le dividende intragroupe est déjà comptabilisé en créance à recevoir ; il ne s'agit plus d'une transaction future mais d'un poste reconnu. Le modèle n'est donc pas celui qui correspond au fait générateur décrit.

**Implications pratiques**: La documentation de couverture ne devrait pas être structurée comme une cash flow hedge pour une créance de dividende déjà reconnue.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d'investissement net concerne le risque de change attaché à un investissement net dans une activité à l'étranger, c'est-à-dire des actifs nets de l'entité étrangère. Une créance de dividende intragroupe comptabilisée séparément n'est pas, dans les faits décrits, un investissement net dans une activité étrangère. Ce modèle ne correspond donc pas à l'objet de la question.

**Implications pratiques**: Il ne faut pas documenter ce risque comme une couverture d'investissement net sur la seule base d'une créance de dividende intragroupe.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability ... or a net investment in a foreign operation
 - 7
    >This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation