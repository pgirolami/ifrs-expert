# Analyse d'une question comptable

**Date**: 2026-04-10

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
   - La question vise les comptes consolidés et uniquement la couverture du risque de change attaché à une créance intragroupe de dividende déjà comptabilisée.
   - La créance de dividende est supposée être un poste monétaire libellé dans une devise créant potentiellement des écarts de change.
   - L’analyse porte sur les modèles de comptabilité de couverture IFRS possibles au niveau consolidé, sans conclure sur toute la documentation détaillée ni sur les tests d’efficacité.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la voie pertinente sur une créance de dividende déjà comptabilisée est la couverture de juste valeur, mais seulement si la partie change de ce poste monétaire intragroupe génère des écarts non totalement éliminés en consolidation. La couverture de flux de trésorerie vise une transaction future, et la couverture d’investissement net vise une exposition différente.

## Points Opérationnels

   - Le niveau d’analyse est la consolidation : la règle générale exclut les éléments intragroupe, sauf l’exception change sur poste monétaire intragroupe.
   - Le fait que le dividende soit déjà comptabilisé en créance est décisif : cela oriente vers un poste reconnu, pas vers une transaction future.
   - La documentation de couverture doit être alignée sur les écarts de change qui subsistent en consolidation ; si tout est éliminé, il n’y a pas d’objet couvert au niveau consolidé.
   - La couverture d’investissement net doit rester séparée conceptuellement de la couverture de la créance de dividende ; ce ne sont pas la même exposition ni le même objet couvert.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire intragroupe.<br>- Le risque de change doit produire des gains ou pertes non totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire intragroupe.
   - Le risque de change doit produire des gains ou pertes non totalement éliminés en consolidation.

**Raisonnment**:
La créance de dividende est déjà comptabilisée, donc on est bien sur un actif reconnu plutôt que sur une transaction future. En comptes consolidés, un élément intragroupe ne peut être désigné que par exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés à la consolidation. Dans cette situation, la couverture de juste valeur peut donc être envisagée sur la composante change, sous cette limite de consolidation.

**Implications pratiques**: La documentation doit cibler la composante change de la créance reconnue au niveau consolidé, et non le dividende intragroupe en tant que flux interne éliminé.

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
Ce modèle vise une transaction prévue ou hautement probable. Or, dans les faits posés, le dividende intragroupe a déjà été comptabilisé en créance, donc l’exposition n’est plus une transaction future mais un poste reconnu. L’exception consolidation pour transactions intragroupe hautement probables ne correspond donc pas à cette situation déjà cristallisée en créance.

**Implications pratiques**: Ce modèle n’est pas adapté à la créance de dividende déjà enregistrée ; il viserait en amont un dividende futur hautement probable, pas la créance existante.

**Référence**:
 - 6.3.1
    >The hedged item can be: ... a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur une créance intragroupe de dividende déjà reconnue, donc sur une exposition transactionnelle de change attachée à un receivable. Le modèle de couverture d’investissement net vise une exposition de nature différente, liée à un investissement net dans une activité à l’étranger. Sur les faits donnés, rien n’indique que la créance de dividende constitue l’objet couvert de ce type.

**Implications pratiques**: Ce modèle ne répond pas directement à la créance de dividende comptabilisée ; il couvrirait l’investissement net dans l’entité étrangère, pas la créance de dividende en tant que telle.

**Référence**:
 - 6.3.1
    >a hedged item can be ... a net investment in a foreign operation
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation