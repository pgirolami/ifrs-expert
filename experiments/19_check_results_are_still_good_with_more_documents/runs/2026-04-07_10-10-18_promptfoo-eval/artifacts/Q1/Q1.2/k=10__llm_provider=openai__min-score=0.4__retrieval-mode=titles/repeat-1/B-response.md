# Analyse d'une question comptable

**Date**: 2026-04-07

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ifric17`
   - `ifrs8`
   - `ifrs9`
   - `ifrs13`
   - `ias28`
   - `ifrs12`
   - `ias21`
   - `ifric16`
   - `ias16`
   - `ifric22`

## Hypothèses
   - La créance de dividende intragroupe est libellée dans une devise étrangère par rapport à la devise fonctionnelle d’au moins une entité du groupe.
   - L’analyse vise les comptes consolidés, où la créance et la dette intragroupe sont éliminées mais où des écarts de change peuvent subsister si les devises fonctionnelles diffèrent.
   - L’instrument de couverture envisagé est conclu avec une contrepartie externe au groupe.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la partie change d’un dividende intragroupe peut être documentée en couverture seulement si le dividende est un poste monétaire intragroupe générant des écarts de change non totalement éliminés. Dans ce cas, une fair value hedge ou une cash flow hedge peut être envisagée; la net investment hedge ne vise pas ce dividende en tant que tel.

## Points Opérationnels

   - Vérifier d’abord si le dividende intragroupe est bien un poste monétaire et si des écarts de change subsistent réellement après éliminations de consolidation.
   - La documentation de couverture doit être faite dès l’origine de la relation et identifier précisément le risque de change couvert, l’instrument externe et le test d’efficacité.
   - Si les deux entités ont la même devise fonctionnelle ou si les écarts de change sont entièrement éliminés en consolidation, il n’y a pas de base pour une couverture comptable sur ce dividende dans les comptes consolidés.
   - La couverture d’investissement net doit être réservée au risque de change de l’investissement net dans l’activité étrangère, pas au dividende intragroupe comptabilisé en créance.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - Le dividende intragroupe constitue un poste monétaire.<br>- Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation.<br>- L’instrument de couverture est avec une partie externe au groupe.<br>- La désignation et la documentation formelles IFRS 9 sont établies dès l’origine. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - Le dividende intragroupe constitue un poste monétaire.<br>- Les écarts de change sur ce poste affectent le résultat consolidé car ils ne sont pas totalement éliminés.<br>- L’instrument de couverture est avec une partie externe au groupe.<br>- La relation satisfait aux critères de documentation et d’efficacité IFRS 9. |
| 3. Couverture d’un investissement net dans une activité à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende intragroupe constitue un poste monétaire.
   - Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation.
   - L’instrument de couverture est avec une partie externe au groupe.
   - La désignation et la documentation formelles IFRS 9 sont établies dès l’origine.

**Raisonnment**:
Dans cette situation, la créance de dividende est un poste reconnu, mais en consolidation un poste intragroupe n’est en principe pas éligible sauf exception de change. L’exception existe pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés; une relation de fair value hedge peut donc être documentée si ce fait est bien présent.

**Implications pratiques**: Possible en consolidation, mais à documenter strictement sur le risque de change résiduel reconnu au niveau consolidé.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.2.3
    >only contracts with a party external to the reporting entity ... can be designated as hedging instruments

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le dividende intragroupe constitue un poste monétaire.
   - Les écarts de change sur ce poste affectent le résultat consolidé car ils ne sont pas totalement éliminés.
   - L’instrument de couverture est avec une partie externe au groupe.
   - La relation satisfait aux critères de documentation et d’efficacité IFRS 9.

**Raisonnment**:
Cette approche peut aussi convenir si l’objectif est de couvrir la variabilité en devise fonctionnelle des flux de règlement du dividende déjà comptabilisé. En comptes consolidés, elle n’est recevable que si le dividende est un poste monétaire intragroupe dont le risque de change affecte encore le résultat consolidé malgré les éliminations.

**Implications pratiques**: Souvent plus intuitif si la couverture vise la variabilité des flux de règlement en devise fonctionnelle du groupe.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 3. Couverture d’un investissement net dans une activité à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette méthode ne couvre pas la partie change d’un dividende intragroupe en tant que telle. Elle vise le risque de change sur un investissement net dans une activité à l’étranger; or un dividende à recevoir correspond normalement à un flux à régler, pas à un élément de net investment.

**Implications pratiques**: À écarter pour couvrir le change d’une créance de dividende intragroupe prise isolément.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation as defined in IAS 21
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity