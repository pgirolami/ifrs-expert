# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Dans les comptes consolidés, la variation de change relative à des dividendes intragroupe pour lesquels un receivable a été constaté est-elle éligible à une désignation en comptabilité de couverture ?

**Documentation consultée**
   - `ifric17`
   - `ifrs9`
   - `ifrs19`
   - `ias21`
   - `ias7`
   - `sic25`
   - `ifric16`
   - `ias37`

## Hypothèses
   - La créance de dividende intragroupe déjà comptabilisée est un poste monétaire exposé au risque de change dans les comptes consolidés.
   - La question porte sur l’éligibilité de cette exposition en tant qu’élément couvert en comptabilité de couverture, et non sur la comptabilisation initiale du dividende.

## Recommandation

**OUI SOUS CONDITIONS**

Dans les comptes consolidés, le risque de change d’une créance de dividende intragroupe peut être éligible à une désignation de couverture si ce poste monétaire génère des écarts de change non intégralement éliminés en consolidation, typiquement entre entités de monnaies fonctionnelles différentes. En revanche, la qualification en couverture d’investissement net n’est pas la réponse normale pour une créance de dividende, sauf si elle fait partie de l’investissement net au sens d’IAS 21.

## Points Opérationnels

   - Le point décisif en consolidation est l’exception IFRS 9 pour le risque de change d’un poste monétaire intragroupe, et non le caractère intragroupe du dividende pris isolément.
   - Il faut vérifier la monnaie fonctionnelle des deux entités : sans monnaies fonctionnelles différentes, l’argument d’un écart de change non éliminé devient difficile.
   - Si la créance est déjà comptabilisée à la clôture, l’analyse porte sur le poste monétaire reconnu et sur ses écarts de change en consolidation.
   - La couverture d’investissement net ne doit être retenue que si la créance relève réellement de l’investissement net ; sinon, l’analyse doit rester sur les modèles fair value hedge ou cash flow hedge.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire intragroupe.<br>- Le risque de change sur ce poste n’est pas totalement éliminé en consolidation. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance de dividende intragroupe donne lieu à une exposition de change affectant le résultat consolidé.<br>- Le poste est entre entités de monnaies fonctionnelles différentes, de sorte que l’écart de change n’est pas totalement éliminé. |
| 3. Couverture d’investissement net | OUI SOUS CONDITIONS | - La créance de dividende doit former partie de l’investissement net dans une activité à l’étranger au sens d’IAS 21. |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire intragroupe.
   - Le risque de change sur ce poste n’est pas totalement éliminé en consolidation.

**Raisonnment**:
La créance de dividende reconnue est un actif comptabilisé, donc une catégorie d’élément potentiellement couverte. En consolidation, un poste intragroupe n’est normalement pas éligible, sauf exception pour le risque de change d’un poste monétaire intragroupe lorsque les gains/pertes de change ne sont pas totalement éliminés. C’est le cas visé si la créance et la dette correspondante sont entre entités de monnaies fonctionnelles différentes.

**Implications pratiques**: La désignation est envisageable en consolidation pour le seul risque de change résiduel sur la créance intragroupe.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 45
    >cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende intragroupe donne lieu à une exposition de change affectant le résultat consolidé.
   - Le poste est entre entités de monnaies fonctionnelles différentes, de sorte que l’écart de change n’est pas totalement éliminé.

**Raisonnment**:
IFRS 9 traite aussi les actifs comptabilisés comme éléments couverts possibles, et l’exception pour le risque de change sur un poste monétaire intragroupe vaut en consolidation. Ainsi, si l’encaissement futur du dividende en devise crée une variabilité de contre-valeur en monnaie fonctionnelle qui affecte le résultat consolidé, cette exposition peut être désignée. L’éligibilité reste toutefois bornée au cas où l’effet de change n’est pas entièrement éliminé en consolidation.

**Implications pratiques**: Une désignation en cash flow hedge peut être envisagée si l’objectif est de couvrir la variabilité de la contre-valeur de l’encaissement futur.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 28
    >Exchange differences ... shall be recognised in profit or loss

### 3. Couverture d’investissement net
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit former partie de l’investissement net dans une activité à l’étranger au sens d’IAS 21.

**Raisonnment**:
Ce modèle ne vise pas un simple dividende intragroupe du seul fait qu’une créance a été comptabilisée. Il n’est pertinent que si le poste monétaire fait partie de l’investissement net dans une activité à l’étranger ; dans ce cas, IAS 21 prévoit une comptabilisation spécifique en OCI dans les comptes incluant la filiale. Sans ce lien avec l’investissement net, ce n’est pas l’approche adaptée à la situation décrite.

**Implications pratiques**: En pratique, cette voie sera exceptionnelle pour une créance de dividende intragroupe ordinaire.

**Référence**:
 - 32
    >a monetary item that forms part of a reporting entity’s net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation