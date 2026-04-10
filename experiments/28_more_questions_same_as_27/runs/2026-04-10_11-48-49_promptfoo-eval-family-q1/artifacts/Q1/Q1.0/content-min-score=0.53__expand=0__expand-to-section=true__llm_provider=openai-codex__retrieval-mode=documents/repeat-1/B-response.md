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
   - La créance de dividende intragroupe est libellée dans une devise étrangère par rapport à au moins une entité du groupe.
   - La question vise l’éligibilité à la comptabilité de couverture dans les comptes consolidés au titre d’IFRS 9.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, potentiellement via une couverture de juste valeur si la créance intragroupe en devise est un élément monétaire dont le risque de change génère des écarts non totalement éliminés en consolidation. En revanche, ce n’est pas un cash flow hedge sur transaction future si la créance est déjà comptabilisée, ni une couverture d’investissement net.

## Points Opérationnels

   - Le point décisif est le niveau de reporting : en comptes consolidés, les éléments intragroupe sont en principe exclus, sauf exception de change sur élément monétaire intragroupe.
   - Le timing est déterminant : une créance de dividende déjà comptabilisée relève d’un poste reconnu, pas d’une transaction future hautement probable.
   - Il faut vérifier si les écarts de change sur cette créance/payable intragroupe sont non totalement éliminés en consolidation ; sans cela, l’exception IFRS 9 ne joue pas.
   - Si la couverture est retenue, la documentation doit viser précisément le risque de change de la créance reconnue et non le dividende comme simple flux futur.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un élément monétaire intragroupe<br>- Le risque de change doit produire des gains ou pertes non totalement éliminés en consolidation<br>- La relation de couverture doit être formellement désignée et documentée selon IFRS 9 |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un élément monétaire intragroupe
   - Le risque de change doit produire des gains ou pertes non totalement éliminés en consolidation
   - La relation de couverture doit être formellement désignée et documentée selon IFRS 9

**Raisonnment**:
Dans vos comptes consolidés, la règle générale limite les éléments couverts aux expositions avec des tiers externes. Toutefois, IFRS 9 prévoit une exception pour un élément monétaire intragroupe si le risque de change crée des gains ou pertes qui ne sont pas totalement éliminés en consolidation. Une créance de dividende déjà comptabilisée peut entrer dans ce cas si ces écarts de change subsistent au niveau consolidé.

**Implications pratiques**: La documentation de couverture est envisageable sur la créance reconnue, mais seulement si l’exception intragroupe pour le risque de change s’applique effectivement en consolidation.

**Référence**:
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 6.3.6
    >if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise une transaction future hautement probable. Or, dans votre situation, le dividende intragroupe a déjà donné lieu à la comptabilisation d’une créance à recevoir : l’exposition n’est donc plus une transaction future mais un poste reconnu. L’exception IFRS 9 sur les transactions intragroupe futures ne correspond pas à ce fait précis.

**Implications pratiques**: Vous ne devriez pas documenter cette exposition comme cash flow hedge dès lors que la créance de dividende est déjà enregistrée.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d’investissement net concerne l’exposition de change liée aux actifs nets d’une activité étrangère. Une créance de dividende intragroupe déjà comptabilisée correspond à un poste à recevoir, pas à l’investissement net dans l’activité étrangère. Le fait générateur et l’objet couvert sont donc différents dans votre cas.

**Implications pratiques**: Cette documentation n’est pas la bonne base pour couvrir le change d’un dividende intragroupe à recevoir.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability ... or a net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 17
    >the amount included in that parent’s foreign currency translation reserve in respect of that foreign operation