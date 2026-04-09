# Analyse d'une question comptable

**Date**: 2026-04-09

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
   - Le dividende intragroupe a été déclaré et comptabilisé en créance/dette intragroupe avant élimination en consolidation.
   - La question vise les états financiers consolidés et le risque de change portant sur ce solde intragroupe comptabilisé.
   - La créance et la dette de dividende sont libellées dans une devise créant des écarts de change entre entités du groupe ayant des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, le risque de change d’une créance de dividende intragroupe peut être désigné dans une relation de couverture si le solde est un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. Dans cette situation, le modèle le plus directement aligné est la couverture de juste valeur.

## Points Opérationnels

   - La documentation de couverture doit être établie dès l’origine de la relation, avec identification de l’instrument de couverture, de l’élément couvert, du risque de change et de la méthode d’évaluation de l’efficacité.
   - Le point décisif en consolidation est de démontrer que la créance/dette de dividende est un élément monétaire intragroupe entre entités de monnaies fonctionnelles différentes, générant des écarts de change non totalement éliminés.
   - Si ces conditions ne sont pas réunies, la réponse pratique redevient l’absence de comptabilité de couverture formelle au niveau consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende doit constituer un élément monétaire intragroupe.<br>- Les écarts de change doivent affecter le résultat consolidé et ne pas être totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net | NON | - (non spécifiées) |
| 4. Sans comptabilité de couverture | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende doit constituer un élément monétaire intragroupe.
   - Les écarts de change doivent affecter le résultat consolidé et ne pas être totalement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, la créance de dividende intragroupe reconnue est un actif comptabilisé exposé au risque de change. IFRS 9 permet, en consolidation, de désigner le risque de change d’un élément monétaire intragroupe comme élément couvert si les écarts de change ne sont pas totalement éliminés ; IAS 21 précise justement qu’ils subsistent en consolidation entre entités de monnaies fonctionnelles différentes.

**Implications pratiques**: Une documentation formelle de couverture peut être mise en place au niveau consolidé sur le risque de change de la créance de dividende.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 45
    >cannot be eliminated ... without showing the results of currency fluctuations in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait générateur décrit est une créance de dividende déjà comptabilisée, donc un solde monétaire reconnu, et non une transaction future hautement probable. Au vu des textes fournis, la voie explicitement prévue en consolidation pour un solde intragroupe reconnu est l’exception relative aux éléments monétaires intragroupe, qui s’aligne ici sur une couverture de juste valeur plutôt que sur une couverture de flux.

**Implications pratiques**: Ce modèle n’est pas le traitement à retenir pour la créance de dividende intragroupe déjà reconnue dans les faits décrits.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’un investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé porte sur une créance de dividende intragroupe comptabilisée, non sur l’investissement net dans une activité à l’étranger. IFRIC 16 réserve cette mécanique au risque de change attaché au net investment lui-même ; les faits décrits concernent un poste monétaire intragroupe distinct.

**Implications pratiques**: Il ne faut pas documenter ce dividende intragroupe comme une couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.

### 4. Sans comptabilité de couverture
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut de relation de couverture formellement documentée, les écarts de change sur le poste monétaire intragroupe sont comptabilisés selon IAS 21 et les variations de juste valeur d’un dérivé selon IFRS 9. Cette approche reste toujours possible, mais elle ne répond pas à l’objectif de comptabilité de couverture posé dans la question.

**Implications pratiques**: Les écarts de change et les variations du dérivé suivront leurs règles ordinaires, sans mécanisme de hedge accounting.

**Référence**:
 - 45
    >such an exchange difference is recognised in profit or loss
 - 5.7.1
    >A gain or loss on a financial asset or financial liability that is measured at fair value shall be recognised in profit or loss