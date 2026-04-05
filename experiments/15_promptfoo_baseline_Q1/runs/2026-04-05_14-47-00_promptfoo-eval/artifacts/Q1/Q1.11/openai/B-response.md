# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>L’exposition au change générée par des dividendes intragroupe, une fois la créance correspondante enregistrée, peut-elle être couverte et documentée en hedge accounting dans les comptes consolidés ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise les comptes consolidés IFRS et une créance de dividende intragroupe déjà comptabilisée.
   - La créance de dividende est analysée comme un élément monétaire intragroupe exposé au risque de change.
   - L’enjeu est la couverture du risque de change de cette créance, et non la couverture d’un investissement net dans une activité à l’étranger.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, si la créance de dividende intragroupe constitue un élément monétaire entre entités de devises fonctionnelles différentes et que les écarts de change ne sont pas entièrement éliminés en consolidation. En revanche, ce n’est pas une couverture d’investissement net ; la documentation et les critères IFRS 9 doivent être respectés.

## Points Opérationnels

   - Le point clé en consolidation est l’exception de l’élément monétaire intragroupe : sans elle, les éléments intragroupe ne sont pas des hedged items.
   - Il faut vérifier concrètement que les deux entités concernées ont des devises fonctionnelles différentes ; sinon, pas d’exposition de change consolidée éligible.
   - La relation de couverture doit être formellement désignée et documentée dès l’origine, avec identification de l’instrument, de l’élément couvert, du risque de change et du hedge ratio.
   - Si l’exposition de change sur la créance est entièrement éliminée en consolidation, la couverture n’est pas éligible dans les comptes consolidés.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance est libellée dans une devise différente de la devise fonctionnelle de l’entité qui la porte.<br>- Les écarts de change sur cet élément monétaire intragroupe ne sont pas entièrement éliminés en consolidation.<br>- Le risque couvert est documenté à l’origine et affecte le résultat consolidé. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La variabilité des flux en devise fonctionnelle provient du risque de change sur la créance reconnue.<br>- La créance intragroupe remplit l’exception de l’élément monétaire intragroupe en consolidation.<br>- Le risque de change couvert affecte le résultat consolidé. |
| 3. Couverture d’investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance est libellée dans une devise différente de la devise fonctionnelle de l’entité qui la porte.
   - Les écarts de change sur cet élément monétaire intragroupe ne sont pas entièrement éliminés en consolidation.
   - Le risque couvert est documenté à l’origine et affecte le résultat consolidé.

**Raisonnment**:
La créance de dividende déjà comptabilisée est un actif reconnu, donc elle entre dans le périmètre des éléments pouvant relever d’une couverture de juste valeur. En consolidation, l’obstacle intragroupe est levé uniquement par l’exception visant le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés.

**Implications pratiques**: Possible en consolidation, mais seulement sur le risque de change résiduel au niveau consolidé et avec documentation IFRS 9 complète.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 6.4.1
    >at the inception ... there is formal designation and documentation

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La variabilité des flux en devise fonctionnelle provient du risque de change sur la créance reconnue.
   - La créance intragroupe remplit l’exception de l’élément monétaire intragroupe en consolidation.
   - Le risque de change couvert affecte le résultat consolidé.

**Raisonnment**:
IFRS 9 permet une couverture de flux de trésorerie pour la variabilité des flux d’un actif reconnu attribuable à un risque particulier. Dans cette situation, cela n’est envisageable en consolidation que si la créance de dividende intragroupe, en tant qu’élément monétaire, génère un risque de change qui affecte le résultat consolidé et n’est pas entièrement éliminé.

**Implications pratiques**: Peut être envisagée si l’entité documente la variabilité des flux liée au change sur la créance reconnue.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.4.1
    >there is an economic relationship between the hedged item and the hedging instrument

### 3. Couverture d’investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur une créance de dividende intragroupe déjà enregistrée, donc sur un élément monétaire intragroupe distinct. Ce n’est pas un montant de net assets d’une activité à l’étranger ; la logique IFRIC 16 sur la couverture d’un investissement net ne vise pas ce type de créance.

**Implications pratiques**: Ne pas documenter cette exposition comme couverture d’investissement net.

**Référence**:
 - ifric-16/2
    >The item being hedged ... may be an amount of net assets
 - 6.5.2
    >hedge of a net investment in a foreign operation