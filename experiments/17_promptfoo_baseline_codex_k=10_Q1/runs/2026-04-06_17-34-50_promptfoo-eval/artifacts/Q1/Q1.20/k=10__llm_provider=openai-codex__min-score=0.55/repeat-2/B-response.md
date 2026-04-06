# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Une créance relative à des dividendes intragroupe figure désormais dans les états financiers consolidés, avec une sensibilité corrélative aux fluctuations de change. Peut-on couvrir cette exposition dans le cadre d’une documentation de hedge accounting ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - L’exposition examinée est un risque de change constaté dans des états financiers consolidés.
   - La question porte sur l’éligibilité conceptuelle au hedge accounting selon IFRS 9, et non sur la démonstration complète de tous les tests d’efficacité.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, potentiellement, mais seulement si la créance de dividendes intragroupe constitue un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation. Dans ce cas, la couverture viserait le risque de change de ce poste; en revanche, une couverture de net investment n’est pas le bon modèle.

## Points Opérationnels

   - Le point clé est de qualifier la créance de dividendes comme poste monétaire intragroupe et de démontrer que son risque de change subsiste en consolidation.
   - La documentation doit être établie dès l’origine de la relation de couverture avec identification de l’instrument, de l’élément couvert, du risque couvert et de l’évaluation de l’efficacité.
   - Si l’exposition ne correspond pas à un poste monétaire intragroupe non totalement éliminé, la réponse devient négative en consolidation.
   - Le modèle de couverture à privilégier, si les conditions sont remplies, est la couverture de juste valeur plutôt qu’une cash flow hedge ou une net investment hedge.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividendes doit constituer un poste monétaire intragroupe.<br>- Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividendes doit constituer un poste monétaire intragroupe.
   - Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation.

**Raisonnment**:
Dans les comptes consolidés, un élément intragroupe n’est en principe pas éligible. Toutefois, IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Si la créance de dividendes est bien un tel poste et que son risque de change affecte le résultat consolidé, une documentation en fair value hedge peut être envisagée.

**Implications pratiques**: Il faut documenter explicitement le risque de change du poste monétaire intragroupe comme élément couvert dans les comptes consolidés.

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
Les extraits fournis réservent expressément l’exception intragroupe en consolidation aux postes monétaires intragroupe et aux transactions intragroupe hautement probables. Ici, les faits décrivent une créance de dividendes déjà comptabilisée, non une transaction future hautement probable. Dans cette situation précise, le modèle cash flow hedge n’est donc pas le plus adapté.

**Implications pratiques**: La documentation ne devrait pas être structurée comme une cash flow hedge pour cette créance déjà reconnue.

**Référence**:
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividendes intragroupe figurant en consolidation, donc un poste monétaire/une créance, et non un investissement net dans une activité à l’étranger. IFRS 9 et IFRIC 16 réservent ce modèle au risque de change lié à des net assets d’une foreign operation. Ce n’est pas le cas décrit ici.

**Implications pratiques**: Ce modèle ne doit pas être retenu pour couvrir une créance de dividendes intragroupe.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 2
    >The item being hedged ... may be an amount of net assets
 - ifric-16 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation