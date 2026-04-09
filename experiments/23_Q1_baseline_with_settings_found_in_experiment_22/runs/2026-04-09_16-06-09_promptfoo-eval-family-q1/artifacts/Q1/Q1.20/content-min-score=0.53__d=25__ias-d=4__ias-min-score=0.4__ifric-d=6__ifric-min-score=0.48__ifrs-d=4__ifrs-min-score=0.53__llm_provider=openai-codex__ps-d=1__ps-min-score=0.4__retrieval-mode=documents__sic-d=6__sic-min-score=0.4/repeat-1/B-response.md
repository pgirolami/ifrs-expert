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
   - L’exposition visée est un risque de change sur une créance intragroupe monétaire reconnue dans les états financiers consolidés.
   - L’entité envisage de documenter une relation de couverture selon IFRS 9 ou, si permis, selon IAS 39.
   - La créance relative à des dividendes est supposée être libellée dans une devise autre que la devise fonctionnelle de l’entité qui la comptabilise.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si, dans les comptes consolidés, cette créance intragroupe peut être désignée comme élément couvert parce que son risque de change n’est pas entièrement éliminé à la consolidation, ou parce qu’elle reste présentée en consolidation. À défaut, une transaction intragroupe ne peut pas être couverte en hedge accounting au niveau consolidé.

## Points Opérationnels

   - Vérifier d’abord pourquoi la créance intragroupe figure encore en consolidation : exception de non-élimination du risque de change sur élément monétaire intragroupe, ou cas d’investissement entity.
   - La documentation de couverture doit identifier précisément l’instrument de couverture, la créance couverte, le risque de change couvert et la méthode d’évaluation de l’efficacité dès l’origine.
   - Si la créance est éliminée en consolidation sans exposition résiduelle au résultat consolidé, elle ne peut pas être désignée comme élément couvert au niveau consolidé.
   - En l’absence de qualification en hedge accounting, appliquer IAS 21 et comptabiliser les écarts de change selon le traitement normal.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - Le risque de change sur la créance intragroupe affecte le résultat consolidé et n’est pas entièrement éliminé à la consolidation, ou la créance reste présentée en consolidation.<br>- La relation satisfait aux critères de qualification et de documentation du hedge accounting. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - Le risque de change sur la créance intragroupe peut être désigné comme élément couvert en consolidation selon l’exception applicable aux éléments monétaires intragroupe, ou parce que l’élément reste reconnu en consolidation.<br>- La relation remplit les critères de documentation, de mesurabilité et d’efficacité requis. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Comptabilisation du change selon IAS 21 | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le risque de change sur la créance intragroupe affecte le résultat consolidé et n’est pas entièrement éliminé à la consolidation, ou la créance reste présentée en consolidation.
   - La relation satisfait aux critères de qualification et de documentation du hedge accounting.

**Raisonnment**:
Dans cette situation, la créance est un actif reconnu exposé au risque de change, ce qui peut correspondre à une exposition aux variations de juste valeur attribuables à un risque particulier. Toutefois, au niveau consolidé, un élément intragroupe n’est éligible que s’il entre dans l’exception visant le risque de change d’un élément monétaire intragroupe non totalement éliminé, ou s’il reste présenté en consolidation.

**Implications pratiques**: Possible en consolidation seulement si l’éligibilité spécifique de l’élément intragroupe est démontrée et documentée dès l’origine.

**Référence**:
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le risque de change sur la créance intragroupe peut être désigné comme élément couvert en consolidation selon l’exception applicable aux éléments monétaires intragroupe, ou parce que l’élément reste reconnu en consolidation.
   - La relation remplit les critères de documentation, de mesurabilité et d’efficacité requis.

**Raisonnment**:
Le modèle de cash flow hedge peut viser une exposition à la variabilité des flux de trésorerie d’un actif reconnu attribuable à un risque particulier. Pour cette créance intragroupe, cela n’est envisageable en consolidation que si le risque de change sur l’élément reste économiquement présent dans le résultat consolidé ou si l’élément n’est pas éliminé en consolidation.

**Implications pratiques**: Alternative possible, mais la justification de l’éligibilité en consolidation doit être explicite dans la documentation.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividendes intragroupe reconnue, non un investissement net dans une activité étrangère. Le modèle de net investment hedge concerne le risque de change attaché à l’investissement net dans une opération étrangère; une créance de dividende ne correspond pas, dans ce schéma de faits, à cet objet de couverture.

**Implications pratiques**: Ce modèle n’est pas le bon véhicule de couverture pour la créance de dividendes décrite.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 2
    >The item being hedged ... may be an amount of net assets
 - 15
    >settlement is neither planned nor likely to occur in the foreseeable future

### 4. Comptabilisation du change selon IAS 21
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Indépendamment du hedge accounting, une créance en devise est un élément monétaire et ses écarts de change sont comptabilisés selon IAS 21. C’est donc le traitement de base certain dans cette situation; le hedge accounting ne s’y ajoute que si les conditions d’éligibilité de l’élément intragroupe sont remplies en consolidation.

**Implications pratiques**: À défaut de qualification en couverture, les écarts de change restent comptabilisés selon IAS 21.

**Référence**:
 - 23
    >foreign currency monetary items shall be translated using the closing rate
 - 28
    >Exchange differences ... shall be recognised in profit or loss
 - 5
    >This Standard does not apply to hedge accounting for foreign currency items