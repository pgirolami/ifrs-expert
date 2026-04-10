# Analyse d'une question comptable

**Date**: 2026-04-10

**Question**:
>Une créance relative à des dividendes intragroupe figure désormais dans les états financiers consolidés, avec une sensibilité corrélative aux fluctuations de change. Peut-on couvrir cette exposition dans le cadre d’une documentation de hedge accounting ?

**Documentation consultée**
   - `ias39`
   - `ifrs9`
   - `ias21`
   - `ifric16`
   - `ifrs19`
   - `ias24`
   - `ifrs18`
   - `ias29`
   - `ifrs12`
   - `ifric17`
   - `ifric21`
   - `sic25`
   - `sic29`

## Hypothèses
   - La créance de dividendes intragroupe est un élément monétaire libellé en devise étrangère et elle est comptabilisée dans les états financiers consolidés.
   - La question vise la possibilité d'appliquer une relation de couverture au risque de change porté par cette position reconnue dans les comptes consolidés.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, une désignation de hedge accounting est envisageable en consolidation uniquement si la créance intragroupe relève de l'exception visant les éléments monétaires intragroupe dont le risque de change n'est pas totalement éliminé en consolidation. Dans ce cas, un fair value hedge ou un cash flow hedge peut être documenté; un net investment hedge n'est pas adapté à cette créance de dividendes en tant que telle.

## Points Opérationnels

   - Le point décisif en consolidation est de démontrer que le risque de change sur cette créance intragroupe n'est pas totalement éliminé conformément à IAS 21.
   - La documentation doit être formalisée dès l'origine et identifier l'instrument de couverture, l'élément couvert, le risque de change couvert et le test d'efficacité.
   - Si les conditions de qualification cessent d'être remplies, la comptabilité de couverture doit être arrêtée prospectivement.
   - Le choix entre fair value hedge et cash flow hedge doit être cohérent avec la manière dont l'exposition de change de cette créance affecte le résultat consolidé.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit constituer un élément monétaire intragroupe dont les gains/pertes de change ne sont pas totalement éliminés en consolidation.<br>- Le risque couvert doit être le risque de change affectant le résultat consolidé. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance doit relever de l'exception applicable aux éléments monétaires intragroupe en devise dans les comptes consolidés.<br>- La variabilité de flux couverte doit pouvoir affecter le résultat consolidé. |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit constituer un élément monétaire intragroupe dont les gains/pertes de change ne sont pas totalement éliminés en consolidation.
   - Le risque couvert doit être le risque de change affectant le résultat consolidé.

**Raisonnment**:
En consolidation, un item intragroupe ne peut être couvert que s'il entre dans l'exception des éléments monétaires intragroupe exposés à des écarts de change non totalement éliminés. Si cette créance de dividendes reste bien porteuse d'un risque de change en résultat consolidé, elle peut être un élément couvert au titre d'un risque particulier sur un actif reconnu.

**Implications pratiques**: Si la relation est qualifiée, les variations de valeur du dérivé et celles de l'élément couvert au titre du risque couvert sont reconnues en résultat.

**Référence**:
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 86
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 89
    >the gain or loss on the hedged item attributable to the hedged risk shall adjust the carrying amount

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit relever de l'exception applicable aux éléments monétaires intragroupe en devise dans les comptes consolidés.
   - La variabilité de flux couverte doit pouvoir affecter le résultat consolidé.

**Raisonnment**:
La norme permet une couverture de la variabilité des flux de trésorerie attachés à un actif reconnu. Pour cette créance de dividendes intragroupe, cela n'est possible en consolidation que si l'exposition de change sur l'élément monétaire n'est pas totalement éliminée et affecte le résultat consolidé.

**Implications pratiques**: La part efficace de la couverture est comptabilisée en autres éléments du résultat global, puis reclassée lorsque les flux couverts affectent le résultat.

**Référence**:
 - 80
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements
 - 86
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 95
    >the portion of the gain or loss on the hedging instrument that is determined to be an effective hedge shall be recognised in other comprehensive income

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
La question porte sur une créance de dividendes intragroupe reconnue en consolidation, non sur un investissement net dans une activité étrangère. Le modèle de net investment hedge vise le risque de change attaché aux net assets d'une activité étrangère, pas une créance de dividende isolée.

**Implications pratiques**: Ce modèle ne doit pas être retenu pour documenter la couverture de cette créance de dividendes.

**Référence**:
 - 86
    >hedge of a net investment in a foreign operation
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets
 - 12
    >The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity