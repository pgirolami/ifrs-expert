# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>La comptabilisation d’une créance sur dividendes intragroupe dans les comptes consolidés conduit à identifier une exposition de change distincte. Cette exposition est-elle éligible à la comptabilité de couverture au niveau consolidé ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question porte sur des comptes consolidés établis selon IFRS 9.
   - La créance sur dividendes intragroupe est libellée dans une devise différente de la monnaie fonctionnelle d’au moins une des entités concernées.
   - L’exposition visée est celle née du caractère monétaire de la créance/dette de dividendes intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance/dette de dividendes intragroupe constitue un élément monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation et affecte le résultat consolidé. À défaut, l’exposition n’est pas éligible.

## Points Opérationnels

   - Point clé : vérifier si la créance de dividendes intragroupe est bien un élément monétaire créant des écarts de change non totalement éliminés en consolidation.
   - Si les écarts de change n’affectent pas le résultat consolidé, l’exposition n’est pas éligible au niveau consolidé.
   - La documentation de couverture doit être faite dès l’origine et identifier précisément l’instrument de couverture, l’élément couvert et le risque de change visé.
   - Le traitement en couverture d’investissement net n’est pas approprié pour une créance sur dividendes distincte.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividendes est un élément monétaire intragroupe.<br>- Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.<br>- Le risque de change affecte le résultat consolidé. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - L’exposition couverte est bien le risque de change sur un élément monétaire intragroupe reconnu.<br>- Ce risque de change affecte le résultat consolidé.<br>- La relation est documentée comme couverture de la variabilité des flux liée au change. |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividendes est un élément monétaire intragroupe.
   - Les écarts de change correspondants ne sont pas totalement éliminés en consolidation.
   - Le risque de change affecte le résultat consolidé.

**Raisonnment**:
Dans cette situation, la créance sur dividendes est un actif reconnu ; en principe les éléments intragroupe ne sont pas éligibles en consolidation. Toutefois, IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsqu’il génère des écarts de change non totalement éliminés en consolidation. Si cette condition est remplie et que le risque affecte le résultat consolidé, une couverture est possible.

**Implications pratiques**: Il faut documenter la relation de couverture au niveau consolidé en visant uniquement le risque de change qui subsiste en résultat consolidé.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - L’exposition couverte est bien le risque de change sur un élément monétaire intragroupe reconnu.
   - Ce risque de change affecte le résultat consolidé.
   - La relation est documentée comme couverture de la variabilité des flux liée au change.

**Raisonnment**:
La comptabilisation de la créance peut révéler une variabilité de flux en monnaie fonctionnelle liée au change. Mais au niveau consolidé, l’obstacle intragroupe demeure, sauf si l’exposition correspond au risque de change d’un élément monétaire intragroupe non totalement éliminé et affectant le résultat consolidé. Dans ce cas seulement, la couverture de flux peut être envisagée pour cette exposition spécifique.

**Implications pratiques**: L’entité doit démontrer que la variabilité de change sur la créance de dividendes se répercute bien en résultat consolidé.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.5
    >Hedge accounting can be applied to transactions between entities in the same group only in the individual or separate financial statements
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
L’exposition décrite provient d’une créance sur dividendes intragroupe comptabilisée, non d’un investissement net dans une activité à l’étranger. Le modèle de couverture d’investissement net vise le risque de change sur les net assets d’une activité étrangère inclus dans les états financiers, ce qui ne correspond pas ici à une créance de dividendes distincte.

**Implications pratiques**: Cette exposition doit être analysée, le cas échéant, dans les modèles de couverture de juste valeur ou de flux, pas comme couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation as defined in IAS 21
 - ifric-16 2
    >Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation will apply only when the net assets of that foreign operation are included in the financial statements