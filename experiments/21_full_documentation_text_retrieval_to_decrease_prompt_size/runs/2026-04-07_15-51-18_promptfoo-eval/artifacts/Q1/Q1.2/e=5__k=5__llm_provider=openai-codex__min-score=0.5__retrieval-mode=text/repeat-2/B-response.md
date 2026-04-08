# Analyse d'une question comptable

**Date**: 2026-04-07

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ias34`
   - `ifrs16`
   - `ias7`
   - `ifric12`
   - `ias19`
   - `ias40`
   - `sic29`
   - `ifrs19`
   - `ias33`
   - `ias38`
   - `ifrs13`
   - `ifric14`
   - `ifric7`
   - `ps1`
   - `ias2`
   - `ifrs5`
   - `ifrs14`
   - `ifric23`
   - `ifrs9`
   - `ifrs7`
   - `ias32`
   - `ifrs18`
   - `ias41`
   - `ias24`
   - `sic25`
   - `ifrs11`
   - `ias37`
   - `ps2`
   - `ifric16`
   - `ifrs15`
   - `ias8`
   - `ias26`
   - `ias20`
   - `ias21`
   - `ias23`
   - `ifric17`
   - `ias29`
   - `ias27`
   - `ifric5`
   - `ias10`
   - `ias28`
   - `ifrs1`
   - `ifric19`
   - `ifrs2`
   - `ias16`
   - `ifrs8`
   - `ias12`
   - `ifrs10`
   - `ifrs12`
   - `ifric1`
   - `ifric21`
   - `ifrs6`
   - `ifrs3`
   - `ifric2`
   - `ias36`
   - `ifrs17`
   - `ias39`

## Hypothèses
   - Le dividende intragroupe a déjà été comptabilisé en créance, donc il s’agit d’un poste monétaire intragroupe existant et non d’une transaction future seulement prévue.
   - La question vise les comptes consolidés et la couverture de la seule composante de change liée à cette créance/dividende intragroupe.
   - On suppose qu’il existe un instrument de couverture avec une contrepartie externe au groupe, condition générale du hedge accounting en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie IFRS pertinente est principalement la couverture de juste valeur du risque de change sur la créance intragroupe, sous réserve que le risque de change affecte bien le résultat consolidé. La couverture de flux de trésorerie ne convient pas à une créance déjà reconnue, et la couverture d’investissement net n’est envisageable que si la créance constitue en substance une partie de l’investissement net, ce qui est atypique pour un dividende.

## Points Opérationnels

   - En consolidation, vérifier d’abord si la créance de dividende intragroupe crée bien un écart de change non totalement éliminé ; sans cela, il n’y a pas de base utile pour documenter une couverture.
   - Si la créance est déjà comptabilisée, la piste opérationnelle à analyser en priorité est la couverture de juste valeur du risque de change, avec un instrument externe au groupe.
   - La couverture d’investissement net exige une analyse de substance très stricte ; pour une créance de dividende, la condition de non-règlement planifié est généralement difficile à soutenir.
   - La documentation devra être alignée sur la monnaie fonctionnelle pertinente en consolidation pour mesurer correctement le risque couvert et l’efficacité.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance/dividende intragroupe doit être un poste monétaire exposé à un risque de change<br>- les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation<br>- l’instrument de couverture doit être conclu avec une partie externe au groupe |
| 3. Couverture d’investissement net | OUI SOUS CONDITIONS | - la créance doit former en substance une partie de l’investissement net dans une opération étrangère<br>- son règlement ne doit être ni planifié ni probable dans un avenir prévisible<br>- la documentation doit viser le risque de change de l’investissement net et non un simple flux de dividende à encaisser |

### 1. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le contexte décrit un dividende déjà comptabilisé en créance. On n’est donc plus face à une transaction intragroupe future hautement probable, mais à un poste monétaire existant.
La base IFRS fournie pour les transactions intragroupe en cash flow hedge vise les transactions prévues ; elle ne correspond pas à la situation d’une créance déjà reconnue.

**Implications pratiques**: Cette documentation n’est pas adaptée à la couverture du change d’une créance de dividende déjà enregistrée.

**Référence**:
 - 80
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item
 - AG99A
    >the foreign currency risk of a forecast intragroup transaction may qualify as a hedged item

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance/dividende intragroupe doit être un poste monétaire exposé à un risque de change
   - les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation
   - l’instrument de couverture doit être conclu avec une partie externe au groupe

**Raisonnment**:
La créance de dividende intragroupe est, sur les faits décrits, un poste monétaire existant. En comptes consolidés, le risque de change d’un poste monétaire intragroupe peut être désigné comme élément couvert s’il génère des écarts de change non totalement éliminés en consolidation.
Cette approche est donc la manière IFRS la plus naturelle dans ce cas, à condition que la créance soit bien exposée à un risque de change qui affecte le résultat consolidé.

**Implications pratiques**: Si ces conditions sont remplies, la documentation de couverture peut être structurée comme une couverture de juste valeur du risque de change de la créance intragroupe.

**Référence**:
 - 73
    >only instruments that involve a party external to the reporting entity ... can be designated as hedging instruments
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 3. Couverture d’investissement net
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance doit former en substance une partie de l’investissement net dans une opération étrangère
   - son règlement ne doit être ni planifié ni probable dans un avenir prévisible
   - la documentation doit viser le risque de change de l’investissement net et non un simple flux de dividende à encaisser

**Raisonnment**:
Cette approche n’est possible que si la créance intragroupe liée au dividende forme en substance une partie de l’investissement net dans une opération étrangère. Les textes visent des postes monétaires dont le règlement n’est ni planifié ni probable dans un avenir prévisible.
Pour un dividende comptabilisé en créance, cela paraît en pratique peu compatible, car un dividende est normalement destiné à être réglé. L’approche n’est donc envisageable que dans un cas très spécifique et inhabituel.

**Implications pratiques**: À défaut de démontrer que la créance de dividende est assimilable à un investissement net, cette voie ne devrait pas être retenue.

**Référence**:
 - 32
    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation
 - 38
    >settlement is neither planned nor likely to occur in the foreseeable future
 - 14
    >A derivative or a non-derivative instrument ... may be designated as a hedging instrument in a hedge of a net investment in a foreign operation