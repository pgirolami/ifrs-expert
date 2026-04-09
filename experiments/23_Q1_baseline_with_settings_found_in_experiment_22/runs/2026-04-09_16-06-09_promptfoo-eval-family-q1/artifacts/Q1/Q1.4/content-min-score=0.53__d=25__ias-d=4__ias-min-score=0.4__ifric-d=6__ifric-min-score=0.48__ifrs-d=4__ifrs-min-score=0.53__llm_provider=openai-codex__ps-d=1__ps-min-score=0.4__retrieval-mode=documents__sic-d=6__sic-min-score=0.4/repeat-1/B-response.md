# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>En consolidation, est-il possible de mettre en place une documentation de couverture portant sur la composante change de dividendes intragroupe dès lors qu’une créance correspondante a été reconnue ?

**Documentation consultée**
   - `ifrs10`
   - `ifrs12`
   - `ifrs19`
   - `ias24`
   - `ifrs9`
   - `ias7`
   - `ifric17`
   - `ias27`
   - `ifric16`
   - `ias32`
   - `sic25`
   - `ifric2`

## Hypothèses
   - La question vise les états financiers consolidés établis selon les IFRS.
   - Le dividende intragroupe est libellé en devise et, après sa décision/constatation, une créance et une dette intragroupe correspondantes ont été comptabilisées.
   - La créance/dette de dividende constitue un poste monétaire exposé au risque de change.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, ce n’est envisageable que si la créance/dette intragroupe de dividende en devise génère des écarts de change qui ne sont pas totalement éliminés en consolidation. Dans ce cas, une désignation de couverture peut être documentée sur ce poste reconnu; sinon, l’élimination intragroupe prive le poste de base de couverture au niveau consolidé.

## Points Opérationnels

   - Le point décisif n’est pas l’existence juridique du dividende, mais l’existence d’un risque de change résiduel au niveau des comptes consolidés après éliminations.
   - Si la créance/dette de dividende est reconnue, la fenêtre pertinente est celle d’un poste monétaire intragroupe déjà comptabilisé, non celle d’une transaction future couverte en cash flow hedge.
   - La documentation de couverture, si retenue, doit être établie au niveau consolidé et démontrer que l’exception IFRS 9 sur les postes monétaires intragroupe est satisfaite.
   - Si les écarts de change sont totalement éliminés en consolidation, la réponse pratique est non: il n’existe plus d’élément couvert pertinent dans les comptes consolidés.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance/dette de dividende est un poste monétaire intragroupe en devise<br>- les écarts de change correspondants affectent le résultat consolidé et ne sont pas totalement éliminés |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Éliminations de consolidation | OUI SOUS CONDITIONS | - les éliminations de consolidation ne font pas disparaître l’effet de change pertinent en résultat consolidé |
| 5. Comptabilisation du change | OUI SOUS CONDITIONS | - le poste de dividende intragroupe en devise laisse subsister des écarts de change au niveau consolidé |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance/dette de dividende est un poste monétaire intragroupe en devise
   - les écarts de change correspondants affectent le résultat consolidé et ne sont pas totalement éliminés

**Raisonnment**:
La créance de dividende reconnue est un actif reconnu, donc le modèle de couverture de juste valeur peut en principe être pertinent. Mais en consolidation, IFRS 9 n’admet des éléments intragroupe comme éléments couverts que de façon exceptionnelle: il faut que le poste monétaire intragroupe crée des écarts de change non totalement éliminés au niveau consolidé.

**Implications pratiques**: Documenter la relation de couverture au niveau consolidé seulement si le risque de change subsiste après éliminations de consolidation.

**Référence**:
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur un dividende intragroupe pour lequel une créance a déjà été reconnue. On n’est donc plus dans la variabilité de flux d’une transaction future hautement probable, mais face à un poste intragroupe déjà comptabilisé, dont le sujet est le change sur un solde reconnu.

**Implications pratiques**: Ce modèle n’est pas le bon fondement pour couvrir un dividende intragroupe déjà constaté par une créance/dette.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé ici est celui d’un dividende intragroupe déjà déclaré et transformé en créance/dette. Ce n’est pas, dans les faits décrits, une couverture du risque de change sur un investissement net dans une activité à l’étranger, mais sur un poste de règlement intragroupe distinct.

**Implications pratiques**: Ne pas documenter cette situation comme une couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.

### 4. Éliminations de consolidation
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - les éliminations de consolidation ne font pas disparaître l’effet de change pertinent en résultat consolidé

**Raisonnment**:
IFRS 10 impose l’élimination intégrale des actifs, passifs, produits, charges et flux intragroupe. Donc, en règle générale, le dividende intragroupe et la créance correspondante disparaissent en consolidation; cela empêche la désignation d’un élément couvert, sauf si un risque de change sur poste monétaire intragroupe subsiste au résultat consolidé.

**Implications pratiques**: Vérifier d’abord l’effet exact des éliminations; sans risque résiduel au niveau consolidé, pas de couverture possible.

**Référence**:
 - B86
    >eliminate in full intragroup assets and liabilities, equity, income, expenses and cash flows

### 5. Comptabilisation du change
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - le poste de dividende intragroupe en devise laisse subsister des écarts de change au niveau consolidé

**Raisonnment**:
Même sans relation de couverture, le traitement ordinaire du change reste pertinent si le poste monétaire intragroupe de dividende génère des écarts de change non totalement éliminés en consolidation. C’est d’ailleurs la raison précise pour laquelle IFRS 9 prévoit une exception limitée pour les postes monétaires intragroupe.

**Implications pratiques**: À défaut de documentation de couverture admissible, comptabiliser simplement les écarts de change résiduels selon les règles de change applicables.

**Référence**:
 - 6.3.6
    >foreign exchange rate gains and losses on intragroup monetary items are not fully eliminated on consolidation