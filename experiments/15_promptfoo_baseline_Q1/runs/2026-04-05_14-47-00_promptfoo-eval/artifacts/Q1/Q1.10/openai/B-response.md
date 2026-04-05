# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Dans un contexte de consolidation IFRS, une relation de couverture peut-elle être documentée au titre du risque de change sur des dividendes intragroupe comptabilisés à recevoir ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question vise les états financiers consolidés établis selon les IFRS.
   - Le dividende intragroupe à recevoir est libellé dans une devise étrangère par rapport à la devise fonctionnelle de l'entité qui le comptabilise.
   - Le dividende à recevoir constitue un poste intragroupe reconnu, analysé sous l'angle du risque de change.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une couverture ne peut être documentée que de façon limitée pour un poste intragroupe. Ici, elle n'est envisageable que si le dividende à recevoir constitue un poste monétaire intragroupe dont le risque de change génère des écarts non intégralement éliminés en consolidation; dans ce cas, le modèle pertinent est la couverture de juste valeur.

## Points Opérationnels

   - En consolidation, la règle de base exclut les éléments intragroupe; il faut donc documenter explicitement l'exception applicable au poste monétaire intragroupe.
   - L'analyse doit être faite au niveau consolidé: il faut vérifier si les écarts de change sur le dividende à recevoir affectent encore le résultat consolidé.
   - Si cette condition n'est pas remplie, la réponse pratique est non: aucune relation de couverture IFRS 9 ne peut être documentée pour ce dividende intragroupe en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - Le dividende à recevoir doit constituer un poste monétaire intragroupe.<br>- Le risque de change doit produire des gains ou pertes non intégralement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'un investissement net dans une activité à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende à recevoir doit constituer un poste monétaire intragroupe.
   - Le risque de change doit produire des gains ou pertes non intégralement éliminés en consolidation.

**Raisonnment**:
Le dividende intragroupe à recevoir est un actif reconnu, donc il entre en principe dans le type d'éléments visés par la couverture de juste valeur. Toutefois, en consolidation, seuls des éléments avec des tiers externes sont normalement éligibles, sauf exception pour le risque de change d'un poste monétaire intragroupe lorsque les gains/pertes de change ne sont pas totalement éliminés.

**Implications pratiques**: La documentation n'est recevable en consolidation que si l'entité démontre l'application de l'exception relative aux postes monétaires intragroupe.

**Référence**:
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La situation décrite porte sur des dividendes déjà comptabilisés à recevoir, donc sur un actif reconnu, et non sur une transaction future hautement probable. Le modèle de cash flow hedge vise la variabilité de flux de trésorerie d'un élément reconnu ou d'une transaction future; ce n'est pas le cadrage le plus adapté à un dividende intragroupe déjà constaté.

**Implications pratiques**: La documentation en cash flow hedge ne correspond pas au fait générateur décrit, qui est un dividende déjà reconnu à recevoir.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d'un investissement net dans une activité à l'étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le risque visé ici porte sur un dividende intragroupe comptabilisé à recevoir, et non sur l'exposition de change attachée à un investissement net dans une activité étrangère. IFRIC 16 réserve ce modèle au risque de change sur les net assets d'une activité étrangère inclus dans les états financiers.

**Implications pratiques**: Ce modèle ne doit pas être utilisé pour documenter le risque de change d'un dividende intragroupe à recevoir.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - ifric-16.2
    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation
 - ifric-16.10
    >the hedged item can be an amount of net assets