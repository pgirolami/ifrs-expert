# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Le groupe a comptabilisé un receivable au titre de dividendes intragroupe, créant ainsi une exposition au risque de change dans les comptes consolidés. Cette exposition peut-elle être désignée comme élément couvert au sens des IFRS ?

**Documentation consultée**
   - `ifrs9`
   - `ias32`
   - `ias21`
   - `ifrs19`
   - `ifrs7`
   - `ifric16`
   - `ifric2`
   - `ifric17`
   - `sic25`
   - `ifrs12`
   - `ps1`
   - `ias37`
   - `ifric23`
   - `sic29`

## Hypothèses
   - La créance de dividende est une créance monétaire libellée en devise étrangère et comptabilisée dans les états financiers consolidés.
   - La question porte sur sa désignation comme élément couvert en comptabilité de couverture IFRS, et non sur la seule comptabilisation des écarts de change selon IAS 21.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais uniquement pour le risque de change et seulement si, en consolidation, les écarts de change sur cette créance intragroupe ne sont pas totalement éliminés. En pratique, la voie la plus robuste ici est la couverture de juste valeur; la couverture de flux de trésorerie est plus conditionnelle, et la couverture d’investissement net ne convient pas.

## Points Opérationnels

   - Vérifier au niveau consolidé que la créance et la dette de dividende sont entre entités de monnaies fonctionnelles différentes et que les écarts de change ne sont pas totalement éliminés.
   - Limiter l’élément couvert au seul risque de change; l’exception IFRS 9 vise l’exposition de change sur un élément monétaire intragroupe.
   - Mettre en place dès l’origine la documentation IFRS 9: instrument de couverture, élément couvert, risque couvert, hedge ratio et méthode d’évaluation de l’efficacité.
   - Si l’objectif est de couvrir une créance déjà reconnue, la couverture de juste valeur sera généralement plus simple à défendre que la couverture de flux de trésorerie.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit être un élément monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.<br>- La relation de couverture doit satisfaire aux critères de désignation, documentation et efficacité d’IFRS 9. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - Le groupe doit documenter que le risque couvert est bien une variabilité de flux de trésorerie en monnaie fonctionnelle liée au change sur cette créance reconnue.<br>- Les écarts de change doivent pouvoir affecter le résultat consolidé et la relation doit satisfaire aux critères d’IFRS 9. |
| 3. Couverture d’un investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un élément monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.
   - La relation de couverture doit satisfaire aux critères de désignation, documentation et efficacité d’IFRS 9.

**Raisonnment**:
Dans cette situation, la créance de dividende est un actif reconnu. IFRS 9 admet, par exception, que le risque de change d’un élément monétaire intragroupe soit un élément couvert en consolidation s’il génère des écarts de change non totalement éliminés. Ce risque peut affecter le résultat consolidé, ce qui cadre avec une couverture de juste valeur.

**Implications pratiques**: Le groupe peut désigner la créance intragroupe comme élément couvert pour son seul risque de change si l’exposition subsiste au niveau consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations
 - 6.4.1
    >A hedging relationship qualifies for hedge accounting only if all of the following criteria are met

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le groupe doit documenter que le risque couvert est bien une variabilité de flux de trésorerie en monnaie fonctionnelle liée au change sur cette créance reconnue.
   - Les écarts de change doivent pouvoir affecter le résultat consolidé et la relation doit satisfaire aux critères d’IFRS 9.

**Raisonnment**:
IFRS 9 vise la variabilité des flux de trésorerie associée à un actif reconnu. Une créance de dividende en devise peut, dans les comptes consolidés, exposer le groupe à une variabilité en monnaie fonctionnelle jusqu’au règlement. Toutefois, cette qualification est plus étroite ici car la créance est déjà reconnue et l’exposition ressemble d’abord à un risque de réévaluation comptable.

**Implications pratiques**: Possible en théorie, mais la documentation devra démontrer de façon précise le caractère 'variabilité de flux de trésorerie' de l’exposition.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.4.1
    >there is an economic relationship between the hedged item and the hedging instrument

### 3. Couverture d’un investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Une créance de dividende intragroupe n’est pas, dans les faits décrits, un investissement net dans une activité à l’étranger. IAS 21 réserve cette notion à des éléments monétaires dont le règlement n’est ni planifié ni probable dans un avenir prévisible; à l’inverse, une créance de dividende est destinée à être réglée.

**Implications pratiques**: Le groupe ne doit pas traiter cette créance de dividende comme élément couvert au titre d’une couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 15
    >An item for which settlement is neither planned nor likely to occur in the foreseeable future is, in substance, a part of the entity’s net investment
 - 15
    >They do not include trade receivables or trade payables
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency