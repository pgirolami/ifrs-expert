# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Des dividendes intragroupe ont été comptabilisés à recevoir, ce qui fait naître une variation potentielle liée au change dans les comptes consolidés. Est-il alors possible de mettre en place une relation de couverture sur cette seule composante de change ?

**Documentation consultée**
   - `ifrs9`
   - `ias21`
   - `ifric17`
   - `ifrs19`
   - `ifrs2`
   - `ias24`
   - `sic25`
   - `ifric16`
   - `ifrs12`
   - `ifric1`
   - `ias37`
   - `sic7`
   - `ifric23`
   - `sic29`
   - `ias26`
   - `ifric22`

## Hypothèses
   - La créance de dividende intragroupe est libellée dans une devise différente de la monnaie fonctionnelle d’au moins une entité du groupe, de sorte qu’elle crée un risque de change.
   - La question vise les comptes consolidés.
   - La créance de dividende comptabilisée est traitée comme un poste monétaire intragroupe, dont l’effet de change n’est pas entièrement éliminé en consolidation.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais seulement si la créance de dividende constitue bien un poste monétaire intragroupe générant des écarts de change non totalement éliminés en consolidation. Dans ce cas, seule la composante de change peut être désignée comme élément couvert; en pratique, le modèle le plus cohérent est la couverture de juste valeur, et non la couverture de flux de trésorerie ni la couverture d’investissement net.

## Points Opérationnels

   - Il faut d’abord vérifier que le dividende intragroupe à recevoir est bien un poste monétaire générant encore un effet de change en consolidation.
   - La désignation doit viser uniquement la composante de change; cela est cohérent avec l’idée de composante d’un élément couvert.
   - Si l’exposition correspond à une créance déjà comptabilisée, la logique est celle d’une couverture de juste valeur plutôt que d’une couverture de flux de trésorerie.
   - Si l’écart de change est au contraire éliminé intégralement en consolidation, il n’y a pas d’élément couvert éligible dans cette situation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Comptabilisation du change selon IAS 21 | OUI | - (non spécifiées) |
| 2. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire intragroupe.<br>- Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation.<br>- La relation de couverture doit être formellement désignée et documentée conformément à IFRS 9. |
| 3. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 4. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Comptabilisation du change selon IAS 21
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, IAS 21 donne le traitement de base: les écarts de change sur postes monétaires sont en résultat, et un poste monétaire intragroupe ne peut pas être éliminé sans laisser apparaître l’effet des fluctuations de change en consolidation. C’est précisément ce traitement de base qui explique l’existence du risque à couvrir.

**Implications pratiques**: À défaut de couverture qualifiante, la variation de change sur la créance/dividende intragroupe reste comptabilisée en résultat consolidé.

**Référence**:
 - 28
    >shall be recognised in profit or loss in the period in which they arise
 - 45
    >cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire intragroupe.
   - Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation.
   - La relation de couverture doit être formellement désignée et documentée conformément à IFRS 9.

**Raisonnment**:
Cette approche peut s’appliquer ici si la désignation porte uniquement sur le risque de change du poste monétaire intragroupe. IFRS 9 admet qu’un élément couvert puisse être une composante d’un poste et prévoit explicitement, en consolidation, l’éligibilité du risque de change d’un poste monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés.

**Implications pratiques**: La seule composante de change de la créance de dividende peut être désignée comme élément couvert dans une relation de couverture de juste valeur.

**Référence**:
 - 6.3.1
    >A hedged item can also be a component
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 27
    >IFRS 9 applies to hedge accounting for foreign currency items

### 3. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Les textes fournis réservent, pour l’intragroupe en consolidation, l’ouverture de la couverture de flux de trésorerie aux transactions intragroupe hautement probables dont le risque de change affectera le résultat consolidé. Ici, le fait décrit est une créance de dividende déjà comptabilisée, donc un poste reconnu et non une transaction future hautement probable.

**Implications pratiques**: Cette situation ne doit pas être traitée comme une couverture de flux de trésorerie du dividende déjà comptabilisé.

**Référence**:
 - 6.3.3
    >that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 4. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d’investissement net vise le risque de change sur un investissement net dans une activité à l’étranger, pas sur une créance de dividende intragroupe isolée. Les textes IFRIC 16 et IAS 21 rattachent ce modèle aux écarts de conversion de l’investissement net et à leur recyclage lors de la cession de l’activité étrangère, ce qui ne correspond pas au cas posé.

**Implications pratiques**: La créance de dividende intragroupe ne doit pas être assimilée à une couverture d’investissement net.

**Référence**:
 - 7
    >hedges the foreign currency risk arising from its net investments in foreign operations
 - 10
    >may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency
 - 32
    >forms part of a reporting entity’s net investment in a foreign operation