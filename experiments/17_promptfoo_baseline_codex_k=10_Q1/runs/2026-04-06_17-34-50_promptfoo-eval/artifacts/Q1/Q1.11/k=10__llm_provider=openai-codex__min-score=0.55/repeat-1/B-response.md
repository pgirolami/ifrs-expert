# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>L’exposition au change générée par des dividendes intragroupe, une fois la créance correspondante enregistrée, peut-elle être couverte et documentée en hedge accounting dans les comptes consolidés ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question vise les comptes consolidés établis selon IFRS 9.
   - Le dividende intragroupe a déjà été décidé et la créance correspondante est comptabilisée ; il s'agit donc d'un poste monétaire intragroupe exposé au risque de change.
   - L'analyse porte sur le risque de change attaché à cette créance, et non sur la couverture d'un investissement net dans une activité à l'étranger.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance de dividende est un poste monétaire intragroupe générant des écarts de change non intégralement éliminés en consolidation, typiquement entre entités de devises fonctionnelles différentes. Dans ce cas, une relation de couverture peut être documentée ; sinon, non.

## Points Opérationnels

   - Point clé en consolidation : vérifier d'abord si la créance de dividende crée réellement des écarts de change non totalement éliminés.
   - La documentation doit identifier l'instrument de couverture, la créance de dividende couverte, le risque de change couvert et la manière d'apprécier l'efficacité.
   - Si la créance est entre entités de même monnaie fonctionnelle, ou si l'effet de change n'affecte pas le résultat consolidé, la couverture comptable n'est pas disponible.
   - Le choix entre fair value hedge et cash flow hedge doit être cohérent avec le risque effectivement géré sur cette créance reconnue.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende constitue un poste monétaire intragroupe.<br>- Les entités concernées ont des monnaies fonctionnelles différentes.<br>- Les écarts de change correspondants ne sont pas intégralement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire intragroupe reconnu.<br>- Le risque de change sur ce poste affecte le résultat consolidé car il n'est pas totalement éliminé.<br>- La relation est formellement désignée et documentée à l'origine. |
| 3. Couverture d'un investissement net à l'étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende constitue un poste monétaire intragroupe.
   - Les entités concernées ont des monnaies fonctionnelles différentes.
   - Les écarts de change correspondants ne sont pas intégralement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, la créance de dividende est un actif reconnu. En consolidation, un élément intragroupe n'est en principe pas éligible, sauf pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Si cette exception est remplie, une couverture de juste valeur peut être documentée sur ce risque de change.

**Implications pratiques**: Si ces conditions sont remplies, le gain ou la perte sur l'instrument de couverture et l'ajustement de l'élément couvert sont comptabilisés en résultat.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.5.8
    >the gain or loss on the hedging instrument shall be recognised in profit or loss

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire intragroupe reconnu.
   - Le risque de change sur ce poste affecte le résultat consolidé car il n'est pas totalement éliminé.
   - La relation est formellement désignée et documentée à l'origine.

**Raisonnment**:
IFRS 9 permet une couverture de flux de trésorerie sur la variabilité des flux d'un actif reconnu attribuable à un risque particulier. Ici, cela n'est envisageable en consolidation que si la créance de dividende intragroupe bénéficie de l'exception visant les postes monétaires intragroupe avec effet de change non éliminé. Sans cette exception, l'élément couvert n'est pas éligible.

**Implications pratiques**: La part efficace irait en autres éléments du résultat global, puis serait recyclée en résultat selon les règles des cash flow hedges.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows ... of, a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.11
    >the portion of the gain or loss on the hedging instrument that is determined to be an effective hedge ... shall be recognised in other comprehensive income

### 3. Couverture d'un investissement net à l'étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur une créance de dividende intragroupe déjà comptabilisée, donc sur un poste monétaire précis, et non sur le risque de change attaché à un investissement net dans une activité à l'étranger. Ce modèle de couverture ne vise pas ce type d'exposition ponctuelle sur dividende à recevoir.

**Implications pratiques**: Cette voie ne doit pas être retenue pour documenter la couverture du change sur une créance de dividende intragroupe.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation as defined in IAS 21
 - ifric-16 6
    >This Interpretation applies only to hedges of net investments in foreign operations