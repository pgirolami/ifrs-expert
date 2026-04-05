# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Le groupe a comptabilisé un receivable au titre de dividendes intragroupe, créant ainsi une exposition au risque de change dans les comptes consolidés. Cette exposition peut-elle être désignée comme élément couvert au sens des IFRS ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - On suppose que la créance de dividendes est un élément monétaire intragroupe comptabilisé, libellé en devise étrangère.
   - On suppose que la question porte sur une désignation comme élément couvert dans les comptes consolidés selon IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement au titre du risque de change d’un élément monétaire intragroupe si ce risque n’est pas entièrement éliminé en consolidation. Dans ce cas, la désignation est envisageable en couverture de juste valeur ou de flux de trésorerie, pas comme couverture d’un investissement net.

## Points Opérationnels

   - Le point décisif est de vérifier si la créance de dividendes est bien un élément monétaire intragroupe dont le risque de change n’est pas entièrement éliminé en consolidation.
   - En comptes consolidés, la règle générale exclut les éléments intragroupe, sauf cette exception ciblée sur le risque de change des éléments monétaires intragroupe.
   - La relation de couverture devra aussi satisfaire aux critères de documentation et d’efficacité d’IFRS 9 à la date de désignation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance doit être un élément monétaire intragroupe<br>- les écarts de change correspondants ne doivent pas être entièrement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - la créance doit être un élément monétaire intragroupe<br>- le risque de change doit affecter les flux de trésorerie en monnaie fonctionnelle du groupe et ne pas être entièrement éliminé en consolidation |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance doit être un élément monétaire intragroupe
   - les écarts de change correspondants ne doivent pas être entièrement éliminés en consolidation

**Raisonnment**:
La créance de dividendes est, selon les hypothèses, un actif comptabilisé. IFRS 9 permet qu’un actif reconnu soit un élément couvert, et prévoit une exception pour le risque de change d’un élément monétaire intragroupe dans les comptes consolidés lorsqu’il génère des écarts de change non entièrement éliminés. Dans cette situation, le risque de change de la créance peut donc être désigné.

**Implications pratiques**: La documentation de couverture doit viser spécifiquement le risque de change de la créance intragroupe reconnue.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance doit être un élément monétaire intragroupe
   - le risque de change doit affecter les flux de trésorerie en monnaie fonctionnelle du groupe et ne pas être entièrement éliminé en consolidation

**Raisonnment**:
IFRS 9 prévoit qu’une couverture de flux de trésorerie peut porter sur la variabilité des flux de trésorerie d’un actif reconnu attribuable à un risque particulier. Si la créance de dividendes intragroupe expose le groupe à une variabilité des flux en monnaie fonctionnelle du fait du change, et si cette exposition n’est pas entièrement éliminée en consolidation, cette désignation est possible.

**Implications pratiques**: Il faut démontrer que la variabilité des flux liée au change sur la créance reconnue est bien l’exposition couverte.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows ... of ... a recognised asset

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividendes intragroupe comptabilisée, et non un investissement net dans une activité à l’étranger. IFRS 9 et IFRIC 16 réservent ce modèle à la couverture du risque de change attaché aux net assets d’une foreign operation. Le fait générateur décrit ne correspond donc pas à cette catégorie.

**Implications pratiques**: La créance de dividendes ne doit pas être documentée comme couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 2
    >The item being hedged ... may be an amount of net assets
 - 10
    >the hedged item can be an amount of net assets