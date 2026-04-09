# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Une créance relative à des dividendes intragroupe figure désormais dans les états financiers consolidés, avec une sensibilité corrélative aux fluctuations de change. Peut-on couvrir cette exposition dans le cadre d’une documentation de hedge accounting ?

**Documentation consultée**
   - `ias39`
   - `ifrs9`
   - `ias21`
   - `ifric16`
   - `ifrs19`
   - `ias24`
   - `ifrs18`
   - `ias29`
   - `ifrs12`
   - `ifric17`
   - `ifric21`
   - `sic25`
   - `sic29`

## Hypothèses
   - L’exposition visée est un risque de change porté par une créance de dividendes intragroupe, observée au niveau des états financiers consolidés.
   - La créance est libellée dans une devise différente de la monnaie fonctionnelle de l’entité qui la comptabilise.
   - La question porte sur l’éligibilité de cette exposition comme élément couvert en hedge accounting dans les comptes consolidés.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, seulement si la créance de dividendes intragroupe constitue un item monétaire exposé à des écarts de change non intégralement éliminés en consolidation. Dans ce cas, son risque de change peut être désigné comme élément couvert, sous réserve de la documentation et des tests de hedge accounting.

## Points Opérationnels

   - Vérifier d’abord que la créance de dividendes est bien un item monétaire intragroupe exposé à un risque de change non totalement éliminé en consolidation.
   - Documenter explicitement que le risque couvert est le seul risque de change de cette créance intragroupe au niveau des comptes consolidés.
   - Choisir de manière cohérente entre fair value hedge et cash flow hedge selon la manière dont l’exposition est gérée et démontrée dans la documentation.
   - Si les conditions de hedge accounting ne sont pas remplies, appliquer IAS 21 et comptabiliser les écarts de change selon le traitement de base.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit être un item monétaire intragroupe<br>- Les écarts de change doivent ne pas être totalement éliminés en consolidation<br>- La relation de couverture doit satisfaire aux exigences formelles de documentation et d’efficacité |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance doit créer une variabilité de flux de trésorerie liée au change au niveau consolidé<br>- Les écarts de change doivent affecter le résultat consolidé<br>- La relation de couverture doit être documentée et mesurable de façon fiable |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Comptabilisation du change selon IAS 21 | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un item monétaire intragroupe
   - Les écarts de change doivent ne pas être totalement éliminés en consolidation
   - La relation de couverture doit satisfaire aux exigences formelles de documentation et d’efficacité

**Raisonnment**:
Dans cette situation, la créance de dividendes intragroupe est un actif reconnu et son risque de change peut, en consolidation, être couvert seulement si l’exposition génère des gains/pertes de change non totalement éliminés. Les textes admettent alors, par exception, le risque de change d’un item monétaire intragroupe comme élément couvert.

**Implications pratiques**: Possible en consolidation pour le seul risque de change, avec comptabilisation de fair value hedge si les conditions sont remplies.

**Référence**:
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value
 - 88
    >At the inception of the hedge there is formal designation and documentation

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit créer une variabilité de flux de trésorerie liée au change au niveau consolidé
   - Les écarts de change doivent affecter le résultat consolidé
   - La relation de couverture doit être documentée et mesurable de façon fiable

**Raisonnment**:
Le risque de change sur une créance monétaire en devise peut aussi être analysé comme une variabilité de flux de trésorerie en monnaie fonctionnelle. Pour cette créance intragroupe, cela n’est recevable en consolidation que si les écarts de change subsistent après consolidation; sinon, il n’existe pas d’exposition couverte au niveau groupe.

**Implications pratiques**: Alternative possible au fair value hedge si l’exposition est documentée comme variabilité de flux en monnaie fonctionnelle/consolidée.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 27
    >IFRS 9 applies to hedge accounting for foreign currency items

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Une créance de dividendes intragroupe figurant désormais en consolidation correspond, par nature, à un montant destiné à être réglé. Elle ne correspond donc pas, dans ce schéma de fait, à un investissement net dans une activité à l’étranger, lequel vise la quote-part d’actifs nets et, pour les items monétaires, des soldes dont le règlement n’est ni planifié ni probable à court terme.

**Implications pratiques**: Cette voie ne paraît pas adaptée à une créance de dividendes intragroupe à encaisser.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 15
    >settlement is neither planned nor likely to occur in the foreseeable future
 - 2
    >The item being hedged ... may be an amount of net assets

### 4. Comptabilisation du change selon IAS 21
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut ou en complément d’une relation de couverture qualifiante, la créance en devise suit IAS 21. Les écarts de change sur un item monétaire sont reconnus en résultat, sauf cas particulier de net investment; et en consolidation, un solde monétaire intragroupe entre entités de monnaies fonctionnelles différentes ne disparaît pas économiquement du fait de l’élimination intragroupe.

**Implications pratiques**: C’est le traitement de base si la documentation de hedge accounting n’est pas mise en place ou n’est pas éligible.

**Référence**:
 - 23
    >foreign currency monetary items shall be translated using the closing rate
 - 28
    >Exchange differences ... shall be recognised in profit or loss
 - 45
    >an intragroup monetary asset ... cannot be eliminated ... without showing the results of currency fluctuations