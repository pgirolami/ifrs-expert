# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>Des dividendes intragroupe ont été comptabilisés à recevoir, ce qui fait naître une variation potentielle liée au change dans les comptes consolidés. Est-il alors possible de mettre en place une relation de couverture sur cette seule composante de change ?

**Documentation consultée**
   - `ifric-16`
   - `ifrs-9`

## Hypothèses
   - La question vise les états financiers consolidés et un dividende intragroupe déjà comptabilisé en créance/dette, libellé dans une devise créant un effet de change potentiel.
   - L’enjeu porte sur l’éligibilité de la seule composante de change comme élément couvert au sens d’IFRS 9.
   - On suppose que l’effet de change sur cette créance/dette intragroupe n’est pas automatiquement intégralement éliminé en consolidation et peut affecter le résultat consolidé ; sinon, aucune relation de couverture ne serait possible.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance/dette de dividende intragroupe constitue, dans les comptes consolidés, un poste intragroupe monétaire dont le risque de change n’est pas totalement éliminé et affecte le résultat consolidé. Dans ce cas, seule la composante de change peut être désignée comme élément couvert.

## Points Opérationnels

   - Le point décisif est de démontrer que le dividende intragroupe constitue un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation.
   - La documentation de couverture doit viser explicitement la seule composante de change, IFRS 9 autorisant la désignation d’une composante de risque séparément identifiable et mesurable.
   - Si l’effet de change ne touche pas le résultat consolidé, l’élément n’est pas éligible comme élément couvert malgré l’existence d’une créance/dette intragroupe.
   - Le modèle de couverture d’investissement net n’est pas adapté à une créance de dividende intragroupe isolée.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance/dette de dividende est un poste monétaire intragroupe dans les comptes consolidés.<br>- Le risque de change génère des gains ou pertes non totalement éliminés en consolidation.<br>- Cette exposition affecte le résultat consolidé. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance/dette de dividende intragroupe produit une variabilité de flux en devise pertinente au niveau consolidé.<br>- Le poste entre dans l’exception des postes monétaires intragroupe dont l’effet de change n’est pas totalement éliminé.<br>- La composante de change est séparément identifiable et mesurable. |
| 3. Couverture d’un investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende est un poste monétaire intragroupe dans les comptes consolidés.
   - Le risque de change génère des gains ou pertes non totalement éliminés en consolidation.
   - Cette exposition affecte le résultat consolidé.

**Raisonnment**:
Un élément couvert peut être un actif ou passif comptabilisé, et seulement une composante de risque peut être désignée si elle est séparément identifiable et mesurable. En consolidation, les éléments intragroupe sont en principe exclus, sauf l’exception visant un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé. Si le dividende à recevoir répond à ce cas, la seule composante de change peut être couverte.

**Implications pratiques**: Une relation de couverture peut être documentée sur la seule composante de change du dividende intragroupe, si l’exception intragroupe est démontrée.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.3.7
    >only changes in the cash flows or fair value of an item attributable to a specific risk or risks
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance/dette de dividende intragroupe produit une variabilité de flux en devise pertinente au niveau consolidé.
   - Le poste entre dans l’exception des postes monétaires intragroupe dont l’effet de change n’est pas totalement éliminé.
   - La composante de change est séparément identifiable et mesurable.

**Raisonnment**:
IFRS 9 permet une couverture de flux sur un actif ou passif comptabilisé ou sur une transaction prévue. Pour un dividende intragroupe déjà comptabilisé, l’obstacle principal reste l’inéligibilité intragroupe en consolidation, sauf si le poste est monétaire et que son risque de change affecte le résultat consolidé. Dans cette hypothèse, la composante de change peut être isolée comme risque couvert.

**Implications pratiques**: Cette voie n’est envisageable que si le risque de change du dividende intragroupe subsiste réellement dans le résultat consolidé.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.3.7
    >only changes in the cash flows or fair value of an item attributable to a specific risk or risks

### 3. Couverture d’un investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise uniquement le risque de change sur un investissement net dans une activité à l’étranger, c’est-à-dire un montant de net assets de l’activité étrangère. Un dividende intragroupe à recevoir est ici une créance spécifique, non un montant de net assets désigné comme investissement net. Le cas décrit ne relève donc pas de ce modèle.

**Implications pratiques**: La relation de couverture ne doit pas être structurée comme une couverture d’investissement net pour ce dividende intragroupe.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 7
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16 10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets