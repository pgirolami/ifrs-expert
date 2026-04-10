# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Documentation consultée**
   - `ias32`
   - `ifrs19`
   - `ifrs18`
   - `ifric17`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ifrs9`
   - `ifrs12`
   - `ias37`
   - `ifric19`
   - `ifric16`

## Hypothèses
   - La question vise les comptes consolidés et la seule composante change d’une créance de dividende intragroupe déjà comptabilisée.
   - La créance de dividende est traitée comme un poste monétaire intragroupe exposé au risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes.
   - L’analyse porte uniquement sur les catégories de documentation de couverture déjà identifiées.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture sur la partie change peut être envisagée principalement via une couverture de juste valeur du poste monétaire intragroupe, si le risque de change génère des écarts non totalement éliminés en consolidation. La couverture de flux de trésorerie n’est pas adaptée ici car la créance est déjà reconnue, et la couverture d’investissement net ne convient que si l’exposition couverte est celle d’un investissement net dans une activité à l’étranger.

## Points Opérationnels

   - Le point décisif en consolidation est de démontrer que le dividende en créance constitue un poste monétaire intragroupe dont les écarts de change affectent le résultat consolidé.
   - La documentation doit être alignée sur le niveau de reporting consolidé, car l’exception IFRS 9 pour les postes intragroupe vise spécifiquement les états financiers consolidés.
   - Si la créance est déjà comptabilisée, la logique de couverture doit viser un poste reconnu ; une documentation de flux de trésorerie serait incohérente avec ce timing.
   - Si l’objectif économique est plutôt de couvrir l’exposition de conversion sur la filiale étrangère dans son ensemble, il faut distinguer cela de la créance de dividende : ce n’est pas le même élément couvert.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit être un poste monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes.<br>- Le risque de change doit affecter le résultat consolidé, c’est-à-dire générer des écarts non totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un poste monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes.
   - Le risque de change doit affecter le résultat consolidé, c’est-à-dire générer des écarts non totalement éliminés en consolidation.

**Raisonnment**:
Ici, l’exposition porte sur une créance de dividende intragroupe déjà comptabilisée, donc sur un poste reconnu et non sur un flux futur. En comptes consolidés, IFRS 9 permet exceptionnellement de désigner le risque de change d’un poste monétaire intragroupe comme élément couvert si les écarts de change ne sont pas totalement éliminés à la consolidation.

**Implications pratiques**: C’est l’approche la plus pertinente pour documenter en consolidation la composante change d’une créance de dividende déjà enregistrée.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette catégorie vise notamment une transaction future hautement probable. Or, dans la situation décrite, le dividende intragroupe a déjà été comptabilisé en créance : l’exposition n’est plus un flux futur attendu mais un poste existant. La logique de cash flow hedge ne correspond donc pas au fait générateur présenté.

**Implications pratiques**: Cette documentation ne convient pas à la partie change d’une créance déjà reconnue.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’un investissement net dans une activité à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise la couverture de change d’une créance de dividende intragroupe, non celle d’un investissement net dans une activité à l’étranger. Le modèle de net investment hedge est une catégorie distincte, applicable à l’exposition de conversion liée à l’investissement net lui-même, pas à un dividende intragroupe comptabilisé en créance.

**Implications pratiques**: À retenir seulement si l’élément couvert est réellement l’investissement net dans l’entité étrangère, ce qui n’est pas le cas décrit.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction or a net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation