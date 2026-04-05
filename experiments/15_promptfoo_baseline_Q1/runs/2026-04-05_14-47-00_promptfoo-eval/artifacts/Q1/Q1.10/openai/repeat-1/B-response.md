# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Dans un contexte de consolidation IFRS, une relation de couverture peut-elle être documentée au titre du risque de change sur des dividendes intragroupe comptabilisés à recevoir ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question vise les états financiers consolidés IFRS du groupe.
   - Le dividende intragroupe a déjà été comptabilisé en créance chez une entité du groupe et en dette correspondante chez une autre.
   - Le risque visé est un risque de change sur cette créance/dette intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture n’est envisageable que si le dividende intragroupe constitue un élément monétaire intragroupe dont les écarts de change ne sont pas entièrement éliminés en consolidation. Dans ce cas, l’approche pertinente est la couverture de juste valeur, pas la couverture de flux ni la couverture d’investissement net.

## Points Opérationnels

   - Le point décisif en consolidation est de démontrer que la créance/dette de dividende intragroupe est un poste monétaire générant des écarts de change non totalement éliminés.
   - Si les écarts de change n’affectent pas le résultat consolidé, l’élément ne peut pas être désigné comme élément couvert en consolidation.
   - La documentation doit être établie dès l’origine de la relation de couverture et identifier clairement l’instrument de couverture, l’élément couvert et le risque de change couvert.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende intragroupe est un élément monétaire entre entités du groupe.<br>- Les entités concernées ont des devises fonctionnelles différentes.<br>- Les écarts de change sur cette créance/dette ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende intragroupe est un élément monétaire entre entités du groupe.
   - Les entités concernées ont des devises fonctionnelles différentes.
   - Les écarts de change sur cette créance/dette ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé.

**Raisonnment**:
Ici, le dividende est déjà comptabilisé à recevoir : il s’agit donc d’un actif reconnu, ce qui correspond au modèle de couverture de juste valeur. En consolidation, cela n’est admis pour un poste intragroupe que si la créance/dette monétaire génère des écarts de change non totalement éliminés, notamment entre entités de devises fonctionnelles différentes.

**Implications pratiques**: Documenter la relation comme couverture de juste valeur du risque de change du dividende intragroupe reconnu, seulement si l’exception intragroupe en consolidation est satisfaite.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, le dividende est déjà comptabilisé à recevoir et ne correspond pas à une transaction future hautement probable. Le risque porte sur une créance en devise déjà reconnue, ce qui relève d’un changement de valeur d’un poste existant plutôt que d’une variabilité de flux futurs au sens du modèle de cash flow hedge.

**Implications pratiques**: Ne pas documenter cette relation comme couverture de flux de trésorerie pour un dividende intragroupe déjà reconnu en créance.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé ici est celui d’un dividende intragroupe à recevoir, non celui des net assets d’une activité étrangère. La couverture d’investissement net concerne l’exposition de change sur un investissement net dans une opération étrangère, pas une créance de dividende intragroupe reconnue.

**Implications pratiques**: Écarter le modèle de couverture d’investissement net pour ce dividende intragroupe comptabilisé à recevoir.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 2
    >The item being hedged ... may be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation.