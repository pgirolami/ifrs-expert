# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Peut-on appliquer la comptabilité de couverture en consolidation à l’exposition de change résultant de dividendes intragroupe dès lors que ceux-ci ont été comptabilisés en créance à recevoir ?

**Documentation consultée**
   - `ifrs9`
   - `ifric17`
   - `ias32`
   - `ifrs18`
   - `ias7`
   - `ifric2`
   - `ifrs19`
   - `ifric16`
   - `ifrs7`
   - `ias37`
   - `sic25`

## Hypothèses
   - La question vise les états financiers consolidés.
   - La créance de dividende intragroupe déjà comptabilisée constitue un élément monétaire libellé en devise étrangère.
   - Seule l’exposition de change liée à cette créance intragroupe est analysée au regard des modèles de comptabilité de couverture.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une couverture peut viser le risque de change d’un élément monétaire intragroupe reconnu, y compris une créance de dividende, mais seulement si ce risque génère des écarts de change non entièrement éliminés en consolidation. Dans ce cas, le modèle pertinent est la couverture de juste valeur, pas la couverture de flux de trésorerie ni la couverture d’investissement net.

## Points Opérationnels

   - Le point clé est le traitement en consolidation: l’exception IFRS 9 ne joue que si l’élément monétaire intragroupe crée des écarts de change non entièrement éliminés.
   - Le moment pertinent est postérieur à la comptabilisation de la créance de dividende; avant cela, l’analyse pourrait relever d’une transaction intragroupe hautement probable, ce qui n’est pas le cas posé ici.
   - Si les entités concernées ont la même monnaie fonctionnelle ou si les écarts de change sont entièrement éliminés, la réponse devient non en consolidation.
   - Même si le traitement est possible, il faut documenter formellement la relation de couverture dès l’origine et démontrer les critères d’efficacité d’IFRS 9.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un élément monétaire intragroupe.<br>- Les écarts de change sur cette créance ne sont pas entièrement éliminés en consolidation, notamment entre entités ayant des monnaies fonctionnelles différentes.<br>- La relation de couverture satisfait aux critères de désignation, documentation et efficacité d’IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un élément monétaire intragroupe.
   - Les écarts de change sur cette créance ne sont pas entièrement éliminés en consolidation, notamment entre entités ayant des monnaies fonctionnelles différentes.
   - La relation de couverture satisfait aux critères de désignation, documentation et efficacité d’IFRS 9.

**Raisonnment**:
La créance de dividende déjà reconnue est un actif comptabilisé. En consolidation, IFRS 9 interdit en principe les éléments intragroupe comme éléments couverts, mais admet une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés à la consolidation. Dans cette situation, l’exposition porte sur un actif reconnu et relève du modèle de couverture de juste valeur.

**Implications pratiques**: Possible en consolidation si la créance de dividende en devise crée un risque de change résiduel au niveau consolidé.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ici, les dividendes intragroupe ne sont plus une transaction future hautement probable mais une créance déjà comptabilisée. Le risque de change porte donc sur un élément monétaire reconnu, non sur des flux futurs variables d’une transaction prévue. Dans ce cas précis, le modèle de flux de trésorerie n’est pas celui qui correspond au fait générateur décrit.

**Implications pratiques**: La comptabilité de couverture ne devrait pas être fondée ici sur un cash flow hedge.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise l’exposition de change d’une créance de dividende intragroupe déjà reconnue, et non le risque de change sur un investissement net dans une activité étrangère. Le modèle de couverture d’investissement net est réservé à ce dernier type d’exposition en consolidation. Les faits décrits ne renvoient pas à une telle relation de couverture.

**Implications pratiques**: Ce modèle n’est pas adapté à une créance de dividende intragroupe déjà constatée.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - 7
    >This Interpretation applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations