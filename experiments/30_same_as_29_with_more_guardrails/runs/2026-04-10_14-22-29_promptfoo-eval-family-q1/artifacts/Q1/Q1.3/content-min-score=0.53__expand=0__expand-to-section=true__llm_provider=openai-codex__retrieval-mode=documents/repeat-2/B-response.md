# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Peut-on désigner, dans les comptes consolidés, le risque de change afférent à des dividendes intragroupe donnant lieu à la comptabilisation d’une créance à recevoir dans une relation de couverture documentée ?

**Documentation consultée**
   - `ifrs9`
   - `ias21`
   - `ifrs12`
   - `ifrs19`
   - `ifrs7`
   - `ifric17`
   - `ifric16`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ias37`
   - `sic7`

## Hypothèses
   - Le dividende intragroupe a été déclaré, de sorte qu’une créance à recevoir et une dette correspondante sont comptabilisées entre deux entités du groupe.
   - La créance/dette de dividende est libellée dans une devise autre que la monnaie fonctionnelle d’au moins l’une des entités concernées.
   - La question porte sur les comptes consolidés et non sur les comptes individuels ou séparés.
   - La créance de dividende intragroupe ne fait pas partie d’un investissement net dans une activité étrangère au sens d’IAS 21.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en comptes consolidés, le risque de change d’une créance intragroupe de dividende peut être désigné si cette créance est un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation. En pratique, cela renvoie au modèle de fair value hedge plutôt qu’à une cash flow hedge ou à une net investment hedge.

## Points Opérationnels

   - Le point décisif est le niveau de reporting : l’exception vise les comptes consolidés, pas la consolidation d’un simple flux intragroupe éliminé sans effet de change résiduel.
   - Le timing est essentiel : avant déclaration, on serait sur une transaction prévue ; après constatation d’une créance de dividende, on est sur un poste monétaire reconnu.
   - Il faut démontrer que les écarts de change sur la créance/dette intragroupe ne sont pas totalement éliminés en consolidation, typiquement lorsque les monnaies fonctionnelles diffèrent.
   - La documentation de couverture doit être établie de façon concomitante et alignée sur le risque effectivement couvert en résultat consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende est un poste monétaire intragroupe reconnu<br>- les entités concernées ont des monnaies fonctionnelles différentes<br>- les écarts de change sur ce poste affectent le résultat consolidé et ne sont pas totalement éliminés |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende est un poste monétaire intragroupe reconnu
   - les entités concernées ont des monnaies fonctionnelles différentes
   - les écarts de change sur ce poste affectent le résultat consolidé et ne sont pas totalement éliminés

**Raisonnment**:
Ici, le dividende déclaré a donné lieu à une créance intragroupe comptabilisée, donc à un poste monétaire reconnu. En comptes consolidés, IFRS 9 permet exceptionnellement de désigner le risque de change d’un poste monétaire intragroupe si les gains/pertes de change ne sont pas totalement éliminés en consolidation, ce qui est le cas entre entités à monnaies fonctionnelles différentes selon IAS 21.

**Implications pratiques**: La désignation est envisageable en consolidation comme couverture d’un poste reconnu, sous documentation formelle de la relation de couverture.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations
 - 6.3.1
    >A hedged item can be a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise une transaction prévue hautement probable. Or la question vise des dividendes intragroupe ayant déjà donné lieu à la comptabilisation d’une créance à recevoir ; à ce stade, on n’est plus sur une transaction future prévue mais sur un poste monétaire reconnu. En outre, le contexte fourni ne permet pas d’établir que le dividende intragroupe prévu affecterait le résultat consolidé.

**Implications pratiques**: Pour le cas décrit, la relation ne doit pas être structurée comme une couverture de flux futurs mais comme une couverture d’un poste reconnu, si les conditions sont remplies.

**Référence**:
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify ... provided that ... the foreign currency risk will affect consolidated profit or loss

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d’investissement net concerne le risque de change afférent à un investissement net dans une activité étrangère. Une créance de dividende intragroupe née d’une distribution déclarée correspond ici à un montant à recevoir, non à un montant de capitaux propres ou de net assets de l’activité étrangère. Le fait pattern décrit ne relève donc pas de cette catégorie.

**Implications pratiques**: Le traitement ne doit pas être documenté comme une couverture d’investissement net pour une créance de dividende déclarée.

**Référence**:
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - 32
    >Exchange differences arising on a monetary item that forms part of a reporting entity’s net investment in a foreign operation