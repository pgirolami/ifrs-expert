# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>L’exposition au change générée par des dividendes intragroupe, une fois la créance correspondante enregistrée, peut-elle être couverte et documentée en hedge accounting dans les comptes consolidés ?

**Documentation consultée**
   - `ias39`
   - `ifrs9`
   - `ifric16`
   - `ias21`
   - `ifrs19`
   - `ifrs18`
   - `ifric17`
   - `ias29`
   - `ifrs12`
   - `sic7`

## Hypothèses
   - La question vise les états financiers consolidés établis selon les IFRS.
   - Le dividende intragroupe a déjà été déclaré et une créance/dette intragroupe correspondante est déjà comptabilisée.
   - Le risque visé est exclusivement le risque de change sur cette créance/dette intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement via la couverture du risque de change d’un élément monétaire intragroupe dans les comptes consolidés si ce risque n’est pas totalement éliminé en consolidation, en pratique lorsque les entités ont des monnaies fonctionnelles différentes. Dans cette situation, le modèle pertinent est la fair value hedge ; les deux autres approches ne correspondent pas aux faits décrits.

## Points Opérationnels

   - Le point déterminant est de vérifier si la créance/dette de dividende est un élément monétaire intragroupe dont les écarts de change ne sont pas intégralement éliminés en consolidation.
   - La documentation de couverture doit être en place dès l’inception de la relation et identifier clairement l’instrument de couverture, l’élément couvert et le risque de change couvert.
   - Si la condition d’exception intragroupe n’est pas remplie, aucun hedge accounting n’est possible en consolidé pour cette créance/dette de dividende.
   - Le modèle à privilégier dans ce cas est la fair value hedge ; les modèles cash flow hedge et net investment hedge ne correspondent pas aux faits décrits.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende constitue un élément monétaire intragroupe.<br>- Le risque de change génère des gains ou pertes non totalement éliminés en consolidation.<br>- Les autres critères de désignation et d’efficacité de la relation de couverture sont respectés. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende constitue un élément monétaire intragroupe.
   - Le risque de change génère des gains ou pertes non totalement éliminés en consolidation.
   - Les autres critères de désignation et d’efficacité de la relation de couverture sont respectés.

**Raisonnment**:
Ici, la créance/dette sur dividende est déjà comptabilisée : il s’agit donc d’un élément reconnu, ce qui correspond au champ de la fair value hedge. En consolidé, un élément intragroupe n’est normalement pas éligible, sauf exception pour le risque de change d’un élément monétaire intragroupe lorsque les gains/pertes de change ne sont pas totalement éliminés à la consolidation. Si cette condition est remplie, la relation peut être documentée en hedge accounting.

**Implications pratiques**: Possible en consolidé si l’exposition de change subsiste à la consolidation ; les variations de l’instrument de couverture et de l’élément couvert seraient alors reconnues en résultat selon le modèle de fair value hedge.

**Référence**:
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 86(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les faits décrits portent sur une créance/dette de dividende déjà reconnue, donc sur une exposition existante d’un élément monétaire comptabilisé. Dans le corpus fourni, la cash flow hedge vise surtout la variabilité de flux de trésorerie d’éléments reconnus ou de transactions futures hautement probables ; ce n’est pas le modèle directement décrit pour ce cas précis d’une créance de dividende intragroupe déjà enregistrée en consolidé.

**Implications pratiques**: Cette voie ne doit pas être retenue pour documenter la couverture du cas décrit.

**Référence**:
 - 86(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 88(c)
    >For cash flow hedges, a forecast transaction ... must be highly probable
 - 95
    >the portion of the gain or loss on the hedging instrument that is determined to be an effective hedge ... shall be recognised in other comprehensive income

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le cas décrit ne porte pas sur la couverture d’un investissement net dans une activité à l’étranger, mais sur une créance/dette de dividende intragroupe après déclaration. Les textes sur la net investment hedge visent les net assets d’une activité étrangère et le risque de change entre la devise fonctionnelle de cette activité et celle du parent, pas un dividende intragroupe payable/receivable déjà comptabilisé.

**Implications pratiques**: Le traitement de hedge of a net investment n’est pas adapté au dividende intragroupe déjà constaté.

**Référence**:
 - 86(c)
    >hedge of a net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity