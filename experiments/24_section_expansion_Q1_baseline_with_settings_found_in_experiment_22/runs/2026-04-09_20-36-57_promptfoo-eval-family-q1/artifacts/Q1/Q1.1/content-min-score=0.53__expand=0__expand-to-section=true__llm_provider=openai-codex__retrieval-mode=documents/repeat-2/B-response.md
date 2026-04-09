# Analyse d'une question comptable

**Date**: 2026-04-09

**Question**:
>Un dividende intragroupe a été comptabilisé en créance.
De quelles manières pouvons-nous appliquer une documentation de couverture dans les comptes consolidés sur la partie change ?

**Documentation consultée**
   - `ias32`
   - `ifrs19`
   - `ifrs18`
   - `ifric17`
   - `ifric2`
   - `ias7`
   - `sic25`
   - `ifrs9`
   - `ifrs12`
   - `ias37`
   - `ifric19`
   - `ifric16`

## Hypothèses
   - La créance de dividende intragroupe crée une exposition de change parce que les entités concernées ont des monnaies fonctionnelles différentes.
   - La question porte sur l'application de la comptabilité de couverture IFRS dans les comptes consolidés pour cette seule composante de change.

## Recommandation

**OUI SOUS CONDITIONS**

Dans cette situation, la voie IFRS la plus défendable en consolidation est la couverture de juste valeur, sous réserve que la créance de dividende soit un poste monétaire intragroupe dont le risque de change affecte encore le résultat consolidé. La couverture de flux de trésorerie et la couverture d'investissement net ne ressortent pas comme adaptées aux faits décrits.

## Points Opérationnels

   - Le point clé en consolidation est de démontrer que la créance de dividende est un poste monétaire intragroupe dont le risque de change affecte encore le résultat consolidé.
   - La documentation doit être mise en place au niveau de la relation de couverture pertinente en consolidation, pas seulement dans les comptes individuels.
   - Si la créance est déjà comptabilisée, la logique opérationnelle à tester en priorité est la couverture de juste valeur, pas la couverture de flux de trésorerie.
   - À défaut de documentation IFRS 9 robuste, il faut rester en absence de comptabilité de couverture.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire intragroupe exposé au change.<br>- Les écarts de change sur ce poste doivent affecter le résultat consolidé et ne pas être totalement éliminés en consolidation.<br>- La relation de couverture doit être formellement désignée et documentée en IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |
| 4. Sans comptabilité de couverture | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire intragroupe exposé au change.
   - Les écarts de change sur ce poste doivent affecter le résultat consolidé et ne pas être totalement éliminés en consolidation.
   - La relation de couverture doit être formellement désignée et documentée en IFRS 9.

**Raisonnment**:
Ici, la créance de dividende est déjà comptabilisée : il s'agit donc d'un poste reconnu, ce qui cadre avec le modèle de couverture de juste valeur. En consolidation, un poste intragroupe n'est normalement pas éligible, sauf pour le risque de change d'un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés ; c'est précisément l'hypothèse retenue.

**Implications pratiques**: La documentation doit viser le risque de change de la créance reconnue dans les comptes consolidés, avec un instrument de couverture et une désignation formelle.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le modèle de flux de trésorerie vise un flux futur ou une transaction future hautement probable. Or, dans les faits décrits, le dividende intragroupe est déjà comptabilisé en créance ; l'exposition n'est plus celle d'une transaction future mais d'un poste reconnu.

**Implications pratiques**: Cette documentation n'est pas la bonne base pour une créance de dividende déjà enregistrée.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise la couverture d'un investissement net dans une activité étrangère, pas la couverture ordinaire d'une créance de dividende intragroupe. Les faits fournis ne disent pas que cette créance fait partie de l'investissement net ni qu'elle serait traitée comme telle en consolidation.

**Implications pratiques**: En l'état des faits, il ne faut pas documenter la partie change du dividende intragroupe comme une couverture d'investissement net.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability ... or a net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation

### 4. Sans comptabilité de couverture
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Si aucune documentation de couverture n'est mise en place, le dérivé éventuel reste comptabilisé sans hedge accounting. Dans ce cas, les variations de valeur du dérivé et les effets de change de la créance suivront leur traitement normal en résultat selon les normes applicables.

**Implications pratiques**: Option simple d'exécution, mais avec une volatilité potentielle accrue du résultat consolidé.

**Référence**:
 - B72
    >a derivative that is not designated as a hedging instrument
 - 5.7.1
    >A gain or loss on a financial asset or financial liability that is measured at fair value shall be recognised in profit or loss