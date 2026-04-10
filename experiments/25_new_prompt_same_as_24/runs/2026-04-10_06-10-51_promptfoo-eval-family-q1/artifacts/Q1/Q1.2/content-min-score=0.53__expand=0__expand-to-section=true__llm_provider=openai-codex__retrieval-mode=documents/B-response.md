# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change de ce dividende ?

**Documentation consultée**
   - `ifrs19`
   - `ias32`
   - `ifric17`
   - `ifrs17`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ifrs12`
   - `ifrs9`
   - `ifric19`
   - `ias37`
   - `ifric16`

## Hypothèses
   - La question vise les comptes consolidés IFRS et la possibilité de documenter une couverture de change sur un dividende intragroupe déjà comptabilisé en créance.
   - La créance de dividende est supposée être un élément monétaire intragroupe libellé dans une devise différente de la monnaie fonctionnelle d'au moins une entité du groupe.
   - L'analyse porte uniquement sur les trois modèles de comptabilité de couverture fournis.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais en pratique seulement via une couverture de juste valeur si la créance de dividende intragroupe constitue un élément monétaire dont le risque de change génère des écarts non entièrement éliminés en consolidation. La couverture de flux de trésorerie ne convient plus une fois la créance comptabilisée, et la couverture d'investissement net ne vise pas ce dividende en tant que tel.

## Points Opérationnels

   - Le point clé en consolidation est l'exception IFRS 9 sur les éléments monétaires intragroupe en devise ; sans elle, l'intragroupe n'est pas éligible.
   - Le moment de la désignation est déterminant : une fois le dividende comptabilisé en créance, la logique 'transaction prévue' n'est plus adaptée.
   - Il faut vérifier que les écarts de change sur la créance ne sont pas totalement éliminés en consolidation, sinon la base IFRS 9 de couverture disparaît.
   - La documentation doit être strictement limitée au risque de change de la créance de dividende, et non au flux de distribution intragroupe de manière générale.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un élément monétaire intragroupe.<br>- Le risque de change doit produire des gains ou pertes non entièrement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un élément monétaire intragroupe.
   - Le risque de change doit produire des gains ou pertes non entièrement éliminés en consolidation.

**Raisonnment**:
Dans cette situation, le dividende a déjà été comptabilisé en créance : il s'agit donc d'un actif reconnu. En consolidation, un élément intragroupe n'est en principe pas éligible, sauf pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. C'est le seul fondement du dossier fourni permettant de documenter une couverture sur cette créance.

**Implications pratiques**: La documentation devrait viser le risque de change de la créance reconnue, et non le dividende intragroupe en général.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Ce modèle vise une transaction prévue hautement probable. Or, ici, le dividende intragroupe est déjà comptabilisé en créance : il n'est plus au stade de transaction future. L'exception IFRS 9 pour les transactions intragroupe hautement probables ne permet donc pas de couvrir, dans cette situation précise, une créance déjà reconnue.

**Implications pratiques**: Ce modèle aurait été à analyser avant la comptabilisation de la créance, pas après.

**Référence**:
 - 6.3.1
    >A hedged item can be a ... forecast transaction
 - 6.3.3
    >that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le modèle de couverture d'investissement net porte sur un investissement net dans une activité à l'étranger, pas sur une créance de dividende intragroupe déjà enregistrée. D'après les faits décrits, l'objet à couvrir est le change sur le dividende comptabilisé en créance ; ce n'est pas, en soi, l'investissement net étranger.

**Implications pratiques**: Ce modèle ne répond pas à l'objectif décrit, qui vise la créance de dividende et non l'investissement net.

**Référence**:
 - 6.3.1
    >The hedged item can be: ... a net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation