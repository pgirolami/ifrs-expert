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
   - La créance de dividende intragroupe comptabilisée est un élément monétaire libellé en devise étrangère dans les comptes consolidés.
   - La question vise uniquement la désignation de l’exposition de change correspondante comme élément couvert au titre de la comptabilité de couverture selon IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, le risque de change d’une créance intragroupe monétaire peut être désigné comme élément couvert grâce à l’exception d’IFRS 9 pour les éléments monétaires intragroupe. Cela suppose que les écarts de change ne soient pas totalement éliminés en consolidation ; en revanche, la voie de la couverture d’un investissement net n’est pas adaptée à une créance de dividende à régler.

## Points Opérationnels

   - Le point décisif en consolidation est l’application de l’exception IFRS 9 relative au risque de change d’un élément monétaire intragroupe.
   - Il faut démontrer que les deux entités concernées ont des monnaies fonctionnelles différentes et que les écarts de change ne sont pas totalement éliminés en consolidation.
   - La désignation retenue doit être formellement documentée dès l’origine de la relation de couverture avec l’objectif de gestion du risque et les tests d’efficacité IFRS 9.
   - La piste de couverture d’investissement net doit être écartée pour un dividende intragroupe à régler ; elle ne vise pas une créance de dividende ordinaire.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance et la dette intragroupe correspondante sont entre entités du groupe ayant des monnaies fonctionnelles différentes.<br>- Le risque de change sur cet élément monétaire génère des gains ou pertes non totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - L’exposition couverte est bien la variabilité des flux en monnaie fonctionnelle liée au risque de change de la créance reconnue.<br>- Les écarts de change correspondants affectent le résultat consolidé car ils ne sont pas totalement éliminés en consolidation. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance et la dette intragroupe correspondante sont entre entités du groupe ayant des monnaies fonctionnelles différentes.
   - Le risque de change sur cet élément monétaire génère des gains ou pertes non totalement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, la créance de dividende est un actif reconnu et l’exposition visée est le risque de change. IFRS 9 admet par exception qu’un élément monétaire intragroupe soit un élément couvert en consolidation si les gains/pertes de change ne sont pas totalement éliminés ; IAS 21 confirme que ces écarts subsistent en consolidation pour des entités de monnaies fonctionnelles différentes.

**Implications pratiques**: Une désignation en juste valeur est envisageable pour le risque de change de la créance intragroupe dans les comptes consolidés, sous réserve de la documentation et des critères généraux d’efficacité.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’exposition couverte est bien la variabilité des flux en monnaie fonctionnelle liée au risque de change de la créance reconnue.
   - Les écarts de change correspondants affectent le résultat consolidé car ils ne sont pas totalement éliminés en consolidation.

**Raisonnment**:
La créance intragroupe reconnue expose le groupe à une variabilité en monnaie fonctionnelle des encaissements futurs du fait du change. L’exception d’IFRS 9 sur les éléments monétaires intragroupe permet aussi cette désignation en consolidation, dès lors que l’exposition de change affecte le résultat consolidé et n’est pas totalement éliminée.

**Implications pratiques**: Une couverture de flux de trésorerie peut être retenue si la relation de couverture est documentée comme visant la variabilité des encaissements futurs en monnaie fonctionnelle.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 45
    >such an exchange difference is recognised in profit or loss
 - 6.4.1
    >the hedging relationship meets all of the following hedge effectiveness requirements

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise le risque de change d’un investissement net dans une activité à l’étranger. Or une créance de dividende intragroupe correspond normalement à un montant dont le règlement est attendu ; elle ne correspond donc pas, dans les faits décrits, à un élément dont le règlement n’est ni prévu ni probable dans un avenir prévisible, condition caractéristique d’un investissement net.

**Implications pratiques**: La créance de dividende ne devrait pas être traitée comme élément couvert d’une couverture d’investissement net dans ce cas.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 15
    >settlement is neither planned nor likely to occur in the foreseeable future
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.