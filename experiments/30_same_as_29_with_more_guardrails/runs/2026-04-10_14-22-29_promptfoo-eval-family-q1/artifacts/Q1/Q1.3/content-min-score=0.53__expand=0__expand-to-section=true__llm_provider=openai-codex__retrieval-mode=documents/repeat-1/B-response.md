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
   - Le dividende intragroupe a été décidé et a donné lieu à la comptabilisation d’une créance et d’une dette intragroupe monétaires.
   - La créance et la dette sont libellées dans une devise qui crée un risque de change entre deux entités du groupe ayant des monnaies fonctionnelles différentes.
   - La question porte sur les comptes consolidés et non sur les comptes individuels ou séparés.
   - La créance de dividende à recevoir ne fait pas partie d’un investissement net dans une activité à l’étranger au sens d’IAS 21.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en pratique via une couverture de juste valeur du risque de change de la créance intragroupe, si l’élément est un poste monétaire intragroupe entre entités à monnaies fonctionnelles différentes et si les écarts de change ne sont pas totalement éliminés en consolidation. En revanche, la couverture de flux de trésorerie n’est pas adaptée une fois la créance comptabilisée, et la couverture d’investissement net ne vise pas ce cas sauf faits très particuliers.

## Points Opérationnels

   - Le point clé est le niveau de reporting : l’exception IFRS 9 pour les postes monétaires intragroupe vaut en comptes consolidés.
   - Le moment de la désignation compte : une fois la créance de dividende comptabilisée, l’exposition pertinente est celle d’un poste monétaire reconnu.
   - Il faut démontrer que les écarts de change sur la créance/dette intragroupe ne sont pas totalement éliminés en consolidation, typiquement parce que les deux entités ont des monnaies fonctionnelles différentes.
   - La documentation de couverture doit identifier précisément le risque couvert comme étant le risque de change de la créance intragroupe.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance intragroupe est un poste monétaire entre entités ayant des monnaies fonctionnelles différentes.<br>- Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.<br>- La relation de couverture est documentée conformément aux exigences de la comptabilité de couverture. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance intragroupe est un poste monétaire entre entités ayant des monnaies fonctionnelles différentes.
   - Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation.
   - La relation de couverture est documentée conformément aux exigences de la comptabilité de couverture.

**Raisonnment**:
Dans cette situation, la créance de dividende à recevoir est un poste monétaire reconnu. En comptes consolidés, IFRS 9 n’autorise en principe que des éléments couverts avec des tiers externes, mais prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation.
IAS 21 confirme qu’un actif/passif monétaire intragroupe entre entités à monnaies fonctionnelles différentes laisse subsister un effet de change en consolidé. Le modèle de couverture de juste valeur est donc le modèle pertinent pour un risque de change portant sur une créance reconnue.

**Implications pratiques**: La désignation peut viser le risque de change de la créance de dividende dans les comptes consolidés, sous réserve du respect des conditions ci-dessus.

**Référence**:
 - 6.3.5
    >only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations
 - 6.3.1
    >A hedged item can be a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question vise des dividendes intragroupe ayant déjà donné lieu à la comptabilisation d’une créance à recevoir. À ce stade, l’exposition n’est plus une transaction future hautement probable mais un actif monétaire reconnu.
Le texte IFRS 9 sur les transactions intragroupe futures hautement probables concerne le risque de change d’une transaction prévisionnelle affectant le résultat consolidé ; ce n’est plus le cas une fois la créance de dividende enregistrée.

**Implications pratiques**: Ce modèle n’est pas le bon véhicule si la créance de dividende est déjà comptabilisée.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d’investissement net vise le risque de change lié aux net assets d’une activité à l’étranger inclus dans les états financiers consolidés. Une créance de dividende à recevoir née d’une distribution intragroupe n’est pas, dans les faits décrits, l’investissement net lui-même.
Les références fournies sur IAS 21 et IFRIC 16 concernent les différences de conversion relatives à un investissement net dans une activité à l’étranger, pas une créance intragroupe de dividende déjà reconnue.

**Implications pratiques**: Ce modèle n’est pas approprié pour couvrir une créance de dividende intragroupe reconnue.

**Référence**:
 - 32
    >a monetary item that forms part of a reporting entity’s net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation