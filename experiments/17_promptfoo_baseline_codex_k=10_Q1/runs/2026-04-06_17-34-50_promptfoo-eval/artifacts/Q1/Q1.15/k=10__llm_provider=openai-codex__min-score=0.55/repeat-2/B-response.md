# Analyse d'une question comptable

**Date**: 2026-04-06

**Question**:
>La distribution de dividendes intragroupe a été reconnue sous la forme d’une créance dans les états financiers consolidés. Cette exposition de change peut-elle, en IFRS, être désignée comme élément couvert dans une relation de couverture ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La créance de dividendes intragroupe crée une exposition au risque de change au sens d’IFRS 9.
   - La question est analysée dans le contexte des états financiers consolidés.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance de dividendes constitue un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation et affecte le résultat consolidé. Dans ce cas, la désignation est envisageable comme élément couvert, mais pas au titre d’une couverture d’investissement net.

## Points Opérationnels

   - Le point déterminant est le traitement en consolidation : la règle générale exclut les éléments intragroupe, sauf l’exception limitée au risque de change sur un poste monétaire intragroupe.
   - Il faut vérifier que la créance de dividendes est bien monétaire et que les écarts de change correspondants affectent le résultat consolidé.
   - La relation de couverture retenue doit être formellement désignée et documentée à l’origine, avec identification de l’instrument de couverture, de l’élément couvert et du risque de change couvert.
   - Une couverture d’investissement net n’est pas appropriée pour une simple créance de dividendes intragroupe reconnue.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit être un poste monétaire intragroupe.<br>- Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation.<br>- Cette exposition doit affecter le résultat consolidé. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance doit être un poste monétaire intragroupe.<br>- Le risque de change doit entraîner une variabilité des flux en monnaie fonctionnelle affectant le résultat consolidé.<br>- Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un poste monétaire intragroupe.
   - Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation.
   - Cette exposition doit affecter le résultat consolidé.

**Raisonnment**:
La créance de dividendes reconnue est un actif comptabilisé, donc elle entre en principe dans la catégorie des éléments pouvant être couverts en juste valeur. En consolidation, un élément intragroupe n’est normalement pas éligible, sauf pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé.

**Implications pratiques**: Si ces conditions sont remplies, l’exposition de change sur la créance peut être documentée comme élément couvert dans une relation de couverture de juste valeur.

**Référence**:
 - 6.5.2
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un poste monétaire intragroupe.
   - Le risque de change doit entraîner une variabilité des flux en monnaie fonctionnelle affectant le résultat consolidé.
   - Les écarts de change correspondants ne doivent pas être totalement éliminés en consolidation.

**Raisonnment**:
IFRS 9 permet une couverture de flux de trésorerie d’une variabilité de flux liée à un risque particulier sur un actif comptabilisé. Pour cette créance intragroupe, l’obstacle consolidé reste le même : elle n’est éligible que si son risque de change relève de l’exception visant les postes monétaires intragroupe dont les effets subsistent en résultat consolidé.

**Implications pratiques**: La désignation en cash flow hedge n’est envisageable que si l’entité démontre que la variabilité de change de cette créance affecte bien le résultat consolidé.

**Référence**:
 - 6.5.2
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise une créance de dividendes intragroupe reconnue, non un investissement net dans une activité à l’étranger. IFRS 9 et IFRIC 16 réservent ce modèle à la couverture du risque de change sur des actifs nets d’une activité étrangère; une créance de dividendes n’est pas cet élément.

**Implications pratiques**: Cette exposition ne doit pas être traitée comme une couverture d’investissement net.

**Référence**:
 - 6.5.2
    >hedge of a net investment in a foreign operation
 - ifric-16 6
    >This Interpretation applies only to hedges of net investments in foreign operations
 - ifric-16 10
    >the hedged item can be an amount of net assets