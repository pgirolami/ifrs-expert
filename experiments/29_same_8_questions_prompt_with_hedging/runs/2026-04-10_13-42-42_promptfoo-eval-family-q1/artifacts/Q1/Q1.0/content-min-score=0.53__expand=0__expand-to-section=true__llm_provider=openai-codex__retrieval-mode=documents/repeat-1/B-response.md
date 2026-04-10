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
   - La question vise les comptes consolidés IFRS.
   - Le dividende intragroupe a été déclaré et a donné lieu à la comptabilisation d'une créance/dividende à recevoir.
   - La créance et la dette de dividende correspondante sont libellées dans une devise créant un risque de change entre entités du groupe.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, mais en pratique seulement via une couverture de juste valeur de la créance intragroupe si cette créance est un élément monétaire intragroupe dont le risque de change n'est pas totalement éliminé en consolidation. La couverture de flux de trésorerie ne correspond pas à une créance déjà comptabilisée, et la couverture d'investissement net ne vise pas ce dividende à recevoir.

## Points Opérationnels

   - Le point clé est le niveau de reporting : en consolidation, les éléments intragroupe sont exclus sauf exception spécifique pour le risque de change sur un élément monétaire intragroupe.
   - Le timing est déterminant : avant comptabilisation d'une créance, on pourrait analyser une transaction future hautement probable ; après comptabilisation de la créance, l'analyse porte sur un poste reconnu.
   - Il faut documenter précisément que le risque couvert est uniquement le risque de change de la créance de dividende et démontrer que les écarts correspondants ne sont pas totalement éliminés en consolidation.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - la créance de dividende constitue un élément monétaire intragroupe<br>- le risque de change sur cette créance génère des écarts non totalement éliminés en consolidation |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - la créance de dividende constitue un élément monétaire intragroupe
   - le risque de change sur cette créance génère des écarts non totalement éliminés en consolidation

**Raisonnment**:
Dans votre cas, la créance de dividende est déjà comptabilisée : on est donc sur un actif reconnu et non sur une transaction future. En comptes consolidés, un élément intragroupe n'est en principe pas éligible, sauf pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés en consolidation.

**Implications pratiques**: La documentation de couverture peut viser le risque de change porté par la créance de dividende reconnue, si ces conditions sont remplies.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated as hedged items
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise des transactions futures hautement probables. Or, dans votre situation, le dividende a déjà été déclaré et une créance à recevoir a été comptabilisée : l'exposition n'est plus un flux futur non reconnu mais un poste monétaire reconnu.

**Implications pratiques**: Une fois la créance de dividende enregistrée, la logique de couverture de flux futurs n'est plus la bonne dans cette situation.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability, an unrecognised firm commitment, a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La couverture d'investissement net concerne le risque de change attaché à la participation nette dans une activité à l'étranger. Ici, vous parlez d'une créance de dividende intragroupe déjà reconnue, qui est distincte de l'exposition de conversion sur l'investissement net lui-même.

**Implications pratiques**: Cette documentation ne doit pas être utilisée pour couvrir la créance de dividende à recevoir en tant que telle.

**Référence**:
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity