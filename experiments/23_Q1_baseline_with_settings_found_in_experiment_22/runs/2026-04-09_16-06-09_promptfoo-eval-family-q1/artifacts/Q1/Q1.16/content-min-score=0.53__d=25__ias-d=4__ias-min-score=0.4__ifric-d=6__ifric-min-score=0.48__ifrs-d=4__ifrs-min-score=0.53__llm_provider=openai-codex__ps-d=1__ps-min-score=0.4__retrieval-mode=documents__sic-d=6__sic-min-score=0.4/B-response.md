# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Au niveau consolidé, l’entité constate une créance liée à des dividendes intragroupe et supporte, de ce fait, une exposition au risque de change. Cette exposition peut-elle faire l’objet d’une documentation de couverture conforme aux IFRS ?

**Documentation consultée**
   - `ias32`
   - `ifrs19`
   - `ifrs7`
   - `ias21`
   - `ifrs9`
   - `ifrs12`
   - `ias7`
   - `ifric17`
   - `sic25`
   - `ifric16`
   - `ifric19`
   - `ifric21`
   - `ifric23`
   - `ifric1`
   - `ias37`
   - `ps1`
   - `sic29`
   - `sic7`

## Hypothèses
   - La créance de dividende intragroupe est libellée dans une devise différente de la monnaie fonctionnelle de l’entité consolidante ou de l’entité qui porte l’exposition au niveau consolidé.
   - Cette créance constitue, au niveau consolidé, un élément monétaire intragroupe dont les écarts de change ne sont pas entièrement éliminés en consolidation.
   - La question porte sur l’éligibilité de cette exposition au risque de change à la comptabilité de couverture dans les états financiers consolidés IFRS.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, une exposition de change sur un élément monétaire intragroupe peut être documentée en couverture IFRS si elle génère des écarts de change non totalement éliminés. En pratique, la voie la plus cohérente ici est la couverture de juste valeur ; la couverture de flux de trésorerie n’est envisageable que si la relation vise bien une variabilité de flux de trésorerie au sens d’IFRS 9. La couverture d’investissement net ne correspond pas à ce fait générateur.

## Points Opérationnels

   - Vérifier d’abord que la créance de dividende reste un élément monétaire exposé au change en consolidé et que l’écart de change n’est pas entièrement éliminé.
   - La documentation de couverture doit être établie à l’origine de la relation et préciser le risque couvert, l’instrument, l’élément couvert et le test d’efficacité.
   - En pratique, la couverture de juste valeur est généralement le modèle le plus aligné avec une créance de dividende déjà comptabilisée.
   - Si l’exposition correspond en réalité à un dividende futur non encore reconnu, l’analyse pourrait basculer vers une transaction future hautement probable, mais ce n’est pas le fait décrit ici.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un élément monétaire reconnu exposé à un risque de change affectant le résultat consolidé.<br>- Les écarts de change sur cet élément intragroupe ne doivent pas être entièrement éliminés en consolidation.<br>- La relation de couverture doit satisfaire aux critères de désignation, documentation et efficacité d’IFRS 9. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La relation doit viser la variabilité des flux de trésorerie en monnaie fonctionnelle liée au risque de change de la créance reconnue.<br>- Le risque couvert doit pouvoir affecter le résultat consolidé.<br>- Les critères de documentation et d’efficacité d’IFRS 9 doivent être respectés. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un élément monétaire reconnu exposé à un risque de change affectant le résultat consolidé.
   - Les écarts de change sur cet élément intragroupe ne doivent pas être entièrement éliminés en consolidation.
   - La relation de couverture doit satisfaire aux critères de désignation, documentation et efficacité d’IFRS 9.

**Raisonnment**:
La créance de dividende est, dans l’hypothèse retenue, un actif reconnu exposé au risque de change. IFRS 9 permet une couverture de juste valeur d’un actif reconnu pour un risque particulier affectant le résultat, et IAS 21 indique qu’un élément monétaire intragroupe ne peut pas être éliminé sans constater l’effet de change en consolidé. L’approche est donc recevable si l’exposition subsiste réellement au niveau consolidé.

**Implications pratiques**: Documenter la créance de dividende comme élément couvert pour le seul risque de change et comptabiliser la couverture selon le modèle de juste valeur si les critères IFRS 9 sont remplis.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La relation doit viser la variabilité des flux de trésorerie en monnaie fonctionnelle liée au risque de change de la créance reconnue.
   - Le risque couvert doit pouvoir affecter le résultat consolidé.
   - Les critères de documentation et d’efficacité d’IFRS 9 doivent être respectés.

**Raisonnment**:
IFRS 9 admet une couverture de flux de trésorerie pour la variabilité de flux d’un actif reconnu ou d’une transaction hautement probable. Dans cette situation, l’exposition porte sur une créance de dividende déjà reconnue ; ce modèle n’est donc pertinent que si la documentation vise réellement la variabilité des flux en monnaie fonctionnelle liée au change, et non simplement la revalorisation comptable de la créance.

**Implications pratiques**: Possible seulement avec une documentation précise orientée sur la variabilité des flux futurs ; à défaut, ce modèle sera moins naturel que la couverture de juste valeur.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.4.1
    >at the inception ... there is formal designation and documentation
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait générateur décrit est une créance de dividende intragroupe, non un investissement net dans une activité à l’étranger. IFRS 9 et IFRIC 16 réservent ce modèle au risque de change attaché aux net assets d’une activité étrangère inclus dans les états financiers consolidés. Une créance de dividende ne correspond pas à cet objet couvert.

**Implications pratiques**: Ne pas documenter cette exposition comme couverture d’investissement net ; utiliser, si les conditions sont réunies, un modèle de juste valeur ou éventuellement de flux de trésorerie.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation as defined in IAS 21
 - 2
    >The item being hedged ... may be an amount of net assets
 - 10
    >only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency