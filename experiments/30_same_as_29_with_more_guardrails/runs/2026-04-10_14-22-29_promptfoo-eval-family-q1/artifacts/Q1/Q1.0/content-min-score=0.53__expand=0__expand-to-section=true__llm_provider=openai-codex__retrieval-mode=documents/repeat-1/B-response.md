# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Est-ce que je peux appliquer une documentation de couverture dans les comptes consolidés sur la partie change relative aux dividendes intragroupe pour lesquels une créance à recevoir a été comptabilisée ?

**Documentation consultée**
   - `ias32`
   - `ifrs19`
   - `ifric17`
   - `ifrs9`
   - `ifrs18`
   - `ifrs12`
   - `ias7`
   - `ias37`
   - `sic25`
   - `ifric16`
   - `sic29`
   - `ifric19`

## Hypothèses
   - La créance de dividende intragroupe est libellée dans une devise différente de la monnaie fonctionnelle d’au moins une des entités concernées.
   - La question vise les comptes consolidés IFRS et une relation de couverture du risque de change sur cette créance déjà comptabilisée.
   - La créance de dividende constitue un poste monétaire intragroupe dont les écarts de change ne sont pas entièrement éliminés en consolidation lorsque les entités ont des monnaies fonctionnelles différentes.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en consolidation, seulement si la créance de dividende est un poste monétaire intragroupe exposé à un risque de change qui n’est pas entièrement éliminé en consolidation. Dans cette situation, le modèle pertinent est la couverture de juste valeur, pas la cash flow hedge ni la couverture d’investissement net.

## Points Opérationnels

   - Le point clé en consolidation est le niveau de reporting : les éléments intragroupe sont en principe exclus, sauf exception pour le risque de change sur postes monétaires intragroupe non entièrement éliminés.
   - Le timing est déterminant : avant comptabilisation du dividende, on analyse éventuellement une transaction future; après comptabilisation de la créance, le modèle pertinent devient celui d’un poste reconnu.
   - La documentation doit cibler uniquement la composante change qui affecte le résultat consolidé.
   - Il faut vérifier concrètement si les entités ont des monnaies fonctionnelles différentes, car c’est ce fait qui fonde l’exception en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire intragroupe<br>- Les entités concernées doivent avoir des monnaies fonctionnelles différentes<br>- Le risque de change doit affecter le résultat consolidé car il n’est pas entièrement éliminé en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire intragroupe
   - Les entités concernées doivent avoir des monnaies fonctionnelles différentes
   - Le risque de change doit affecter le résultat consolidé car il n’est pas entièrement éliminé en consolidation

**Raisonnment**:
Ici, la créance de dividende est déjà comptabilisée, donc on est face à un actif reconnu et non à une transaction future. En comptes consolidés, un poste intragroupe ne peut être couvert que s’il est avec une partie intragroupe mais génère des écarts de change non entièrement éliminés; le texte vise précisément les postes monétaires intragroupe entre entités à monnaies fonctionnelles différentes.

**Implications pratiques**: Si ces conditions sont remplies, une documentation de couverture en consolidation peut viser le risque de change de la créance reconnue.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise les transactions prévues hautement probables. Or, dans votre cas, une créance à recevoir a déjà été comptabilisée au titre du dividende intragroupe; on n’est donc plus au stade d’un flux futur non reconnu mais d’un poste existant.

**Implications pratiques**: La cash flow hedge n’est pas le bon modèle une fois le dividende devenu une créance comptabilisée.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur le change d’une créance de dividende intragroupe déjà reconnue, pas sur l’exposition de conversion liée à un investissement net dans une activité étrangère. Le modèle de couverture d’investissement net vise la différence de change sur les net assets d’une foreign operation, ce qui est distinct d’un dividende à recevoir.

**Implications pratiques**: Il ne faut pas documenter cette couverture comme une couverture d’investissement net.

**Référence**:
 - 11
    >the hedged item can be an amount of net assets
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation