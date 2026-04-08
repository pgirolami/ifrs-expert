# Analyse d'une question comptable

**Date**: 2026-04-07

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Documentation consultée**
   - `ps1`
   - `ias8`
   - `ias23`
   - `ifrs19`
   - `ifric17`
   - `ias20`
   - `ias41`
   - `ias19`
   - `ifrs10`
   - `ias34`
   - `ias38`
   - `ifric12`
   - `ifrs2`
   - `sic25`
   - `ias39`
   - `ifric16`
   - `ifric6`
   - `ias26`
   - `ifrs3`
   - `ifrs12`
   - `ps2`
   - `ias28`
   - `ifric21`
   - `ias16`
   - `ifrs16`
   - `ias37`
   - `ifrs11`
   - `ifric23`
   - `ias36`
   - `ifrs6`
   - `ifrs7`
   - `ifrs13`
   - `ifric14`
   - `ias10`
   - `ias27`
   - `ifrs17`
   - `ifrs18`
   - `ifric19`
   - `ifrs1`
   - `ifric2`
   - `sic7`
   - `ifrs14`
   - `ias12`
   - `ias40`
   - `ifrs8`
   - `ias21`
   - `ifrs15`
   - `ias33`
   - `ias29`
   - `ifric22`
   - `ifric1`
   - `sic29`
   - `ifrs5`
   - `ifric7`
   - `ifric5`
   - `ias7`
   - `ias32`
   - `ias2`
   - `ias24`
   - `ifrs9`

## Hypothèses
   - La créance de dividende intragroupe est libellée en devise étrangère.
   - La créance est portée entre des entités du groupe ayant des monnaies fonctionnelles différentes.
   - La partie change sur cette créance génère, en consolidation, des écarts de change qui ne sont pas totalement éliminés.
   - La question porte sur l'application de la comptabilité de couverture IFRS dans les comptes consolidés.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, une documentation de couverture sur la partie change peut être mise en place en consolidation sur une base de fair value hedge ou, sous réserve de la désignation retenue, de cash flow hedge. En revanche, une net investment hedge ne s'applique pas à une simple créance de dividende, sauf si le poste faisait en substance partie d'un investissement net, ce qui n'est pas décrit ici.

## Points Opérationnels

   - En comptes consolidés, il faut démontrer que l'écart de change sur la créance intragroupe n'est pas totalement éliminé ; sinon il n'y a pas de risque couvert au niveau groupe.
   - La qualification de la créance comme poste monétaire intragroupe est centrale pour utiliser l'exception IFRS en consolidation.
   - Le choix entre fair value hedge et cash flow hedge doit être aligné avec le risque effectivement documenté et la manière dont il affecte le résultat consolidé.
   - Le net investment hedge ne doit pas être utilisé pour contourner le traitement d'une créance de dividende ; il faut un véritable investissement net au sens IAS 21.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance doit être un poste monétaire intragroupe<br>- les entités concernées doivent avoir des monnaies fonctionnelles différentes<br>- l'instrument de couverture doit être éligible et la relation documentée conformément à IFRS 9 |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - la documentation doit viser la variabilité des flux due au change sur la créance reconnue<br>- la créance doit être un poste monétaire intragroupe dont le risque de change affecte le résultat consolidé<br>- les critères de désignation et d'efficacité d'IFRS 9 doivent être satisfaits |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance doit être un poste monétaire intragroupe
   - les entités concernées doivent avoir des monnaies fonctionnelles différentes
   - l'instrument de couverture doit être éligible et la relation documentée conformément à IFRS 9

**Raisonnment**:
La créance de dividende est un actif reconnu ; IFRS 9 permet un fair value hedge d'une exposition à des variations de juste valeur d'un actif reconnu attribuables à un risque particulier. En consolidation, l'exception pour le risque de change sur un poste monétaire intragroupe entre entités à monnaies fonctionnelles différentes permet d'envisager la désignation si l'écart de change n'est pas entièrement éliminé.

**Implications pratiques**: La variation de change couverte sur la créance et celle de l'instrument de couverture seraient reconnues en résultat selon la mécanique du fair value hedge.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la documentation doit viser la variabilité des flux due au change sur la créance reconnue
   - la créance doit être un poste monétaire intragroupe dont le risque de change affecte le résultat consolidé
   - les critères de désignation et d'efficacité d'IFRS 9 doivent être satisfaits

**Raisonnment**:
IFRS 9 vise aussi la variabilité des flux de trésorerie d'un actif reconnu. Pour une créance de dividende en devise, les encaissements en monnaie fonctionnelle varient avec le change ; en consolidation, l'exception relative au risque de change sur un poste monétaire intragroupe peut donc permettre une désignation, si c'est bien ce risque qui affecte le résultat consolidé.

**Implications pratiques**: La part efficace irait en autres éléments du résultat global puis serait reclassée lorsque le risque de change affecte le résultat consolidé.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with ... a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le modèle de net investment hedge vise le risque de change sur un investissement net dans une activité étrangère, c'est-à-dire l'intérêt dans les actifs nets de cette activité. Une créance de dividende intragroupe comptabilisée en créance ne correspond pas, sur les faits décrits, à un investissement net ; elle matérialise au contraire un montant à recevoir.

**Implications pratiques**: Cette voie ne devrait pas être retenue pour une créance de dividende intragroupe telle que décrite.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation as defined in IAS 21
 - 8
    >Net investment in a foreign operation is the amount of the reporting entity’s interest in the net assets of that operation.
 - 2
    >The item being hedged ... may be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation.