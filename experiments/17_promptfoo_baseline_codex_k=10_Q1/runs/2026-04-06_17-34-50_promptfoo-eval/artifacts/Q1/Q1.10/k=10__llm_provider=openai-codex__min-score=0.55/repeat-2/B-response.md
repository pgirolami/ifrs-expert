# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Dans un contexte de consolidation IFRS, une relation de couverture peut-elle être documentée au titre du risque de change sur des dividendes intragroupe comptabilisés à recevoir ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question vise les états financiers consolidés en IFRS.
   - Le dividende intragroupe a déjà été comptabilisé en créance à recevoir dans une entité du groupe, avec un risque de change entre entités du groupe.
   - Aucun fait n’indique qu’il s’agit d’une couverture d’un investissement net dans une activité à l’étranger.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une couverture n’est pas documentable du seul fait qu’il s’agit d’un dividende intragroupe. Elle ne peut l’être que si la créance/dividende constitue un élément monétaire intragroupe exposé à un risque de change dont les écarts ne sont pas totalement éliminés en consolidation ; à défaut, la réponse est non.

## Points Opérationnels

   - Le point décisif est de vérifier si le dividende à recevoir constitue bien un élément monétaire intragroupe en devise dont les écarts de change affectent encore le résultat consolidé.
   - Si les écarts de change sont entièrement éliminés en consolidation, la documentation de couverture n’est pas recevable.
   - La documentation doit être établie dès l’origine de la relation et satisfaire aux critères de désignation et d’efficacité d’IFRS 9.
   - En pratique, les dividendes intragroupe sont souvent éliminés en consolidation ; il faut donc démontrer spécifiquement pourquoi le risque de change subsiste au niveau consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.<br>- Le risque couvert est le risque de change affectant le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |
| 4. Pas de comptabilité de couverture | OUI SOUS CONDITIONS | - La créance de dividende ne remplit pas les critères de l’exception visant le risque de change d’un élément monétaire intragroupe en consolidation. |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.
   - Le risque couvert est le risque de change affectant le résultat consolidé.

**Raisonnment**:
Une créance de dividende déjà comptabilisée est un actif reconnu, ce qui est compatible en principe avec une couverture de juste valeur. Toutefois, en consolidation, seuls des éléments avec une partie externe peuvent être désignés, sauf exception pour le risque de change d’un élément monétaire intragroupe dont les écarts ne sont pas totalement éliminés. Donc cela n’est possible ici que si le dividende à recevoir répond à cette exception.

**Implications pratiques**: Documenter la relation comme couverture du risque de change sur la créance intragroupe seulement si l’exception intragroupe est démontrée en consolidation.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, le dividende est déjà comptabilisé à recevoir : l’exposition porte donc sur une créance reconnue en devise, non sur une transaction future hautement probable. Le contexte fourni ne supporte pas ici une variabilité de flux future du type visé par ce modèle ; le point central est le risque de change sur un poste monétaire déjà reconnu.

**Implications pratiques**: Ne pas documenter la relation comme couverture de flux de trésorerie pour un dividende déjà comptabilisé à recevoir.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items

### 3. Couverture d’un investissement net dans une activité à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur des dividendes intragroupe comptabilisés à recevoir, pas sur la couverture du risque de change d’un investissement net dans une activité à l’étranger. Le modèle IFRS 9/IFRIC 16 vise les net assets d’une activité étrangère inclus dans les états financiers, ce qui ne correspond pas à une créance de dividende intragroupe.

**Implications pratiques**: Écarter ce modèle sauf si la relation vise en réalité un investissement net, ce qui n’est pas le cas décrit.

**Référence**:
 - 6.5.1
    >hedge of a net investment in a foreign operation
 - ifric-16 2
    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation
 - ifric-16 10
    >the hedged item can be an amount of net assets

### 4. Pas de comptabilité de couverture
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende ne remplit pas les critères de l’exception visant le risque de change d’un élément monétaire intragroupe en consolidation.

**Raisonnment**:
Si la créance de dividende intragroupe ne satisfait pas l’exception applicable aux éléments monétaires intragroupe en devise, elle ne peut pas être désignée en couverture en consolidation. Dans ce cas, les variations de l’instrument de couverture et du poste couvert suivent leur traitement IFRS normal, sans comptabilité de couverture.

**Implications pratiques**: À défaut d’éligibilité du poste intragroupe en consolidation, comptabiliser sans hedge accounting.

**Référence**:
 - 6.4.1
    >qualifies for hedge accounting only if all of the following criteria are met
 - 6.3.5
    >not in the consolidated financial statements of the group
 - 6.3.6
    >may qualify as a hedged item ... if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation