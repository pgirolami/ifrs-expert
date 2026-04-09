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
   - La créance de dividende intragroupe est libellée dans une devise créant un risque de change dans les comptes consolidés.
   - La question porte sur une documentation de couverture IFRS en comptes consolidés visant spécifiquement la partie change de cette créance de dividende intragroupe.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, une documentation de couverture sur la partie change est envisageable pour la créance de dividende intragroupe via un fair value hedge ou un cash flow hedge, uniquement si le risque de change sur cet élément intragroupe affecte le résultat consolidé. En revanche, la couverture de net investment ne vise pas, dans cette situation, la créance de dividende comptabilisée.

## Points Opérationnels

   - Le point clé en consolidation est de démontrer que le risque de change sur la créance de dividende intragroupe n’est pas totalement éliminé et affecte bien le résultat consolidé.
   - La documentation de couverture doit être établie dès l’origine de la relation, avec identification de l’instrument de couverture, de l’élément couvert, du risque de change couvert et de l’évaluation de l’efficacité.
   - Si le dividende intragroupe est déjà comptabilisé en créance, la couverture de net investment n’est pas la bonne base documentaire pour cet élément précis.
   - La présentation en résultat ou en OCI dépendra du modèle retenu : fair value hedge versus cash flow hedge.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - Le risque de change sur la créance intragroupe doit affecter le résultat consolidé.<br>- La relation de couverture doit satisfaire aux critères formels de désignation et de documentation d’IFRS 9. |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La variabilité des flux en devise liés à la créance doit affecter le résultat consolidé.<br>- La relation de couverture doit satisfaire aux critères formels de désignation et de documentation d’IFRS 9. |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le risque de change sur la créance intragroupe doit affecter le résultat consolidé.
   - La relation de couverture doit satisfaire aux critères formels de désignation et de documentation d’IFRS 9.

**Raisonnment**:
La créance de dividende est un actif reconnu ; IFRS 9 permet une fair value hedge d’un actif reconnu pour un risque particulier affectant le résultat. En consolidation, cela n’est recevable ici que si la partie change de cette créance intragroupe constitue un risque qui n’est pas totalement éliminé et affecte le résultat consolidé.

**Implications pratiques**: La variation de change couverte sur la créance et l’effet du dérivé de couverture seront comptabilisés en résultat consolidé selon la logique de fair value hedge.

**Référence**:
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La variabilité des flux en devise liés à la créance doit affecter le résultat consolidé.
   - La relation de couverture doit satisfaire aux critères formels de désignation et de documentation d’IFRS 9.

**Raisonnment**:
IFRS 9 prévoit une cash flow hedge pour la variabilité de flux de trésorerie d’un actif reconnu pouvant affecter le résultat. Dans ce cas, elle n’est envisageable en consolidation que si la variabilité liée au change sur l’encaissement du dividende intragroupe se traduit bien par une exposition de change affectant le résultat consolidé.

**Implications pratiques**: La part efficace de la couverture sera comptabilisée en autres éléments du résultat global puis reclassée selon les règles IFRS 9 lorsque le risque couvert affecte le résultat.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.5
    >only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette méthode vise le risque de change sur un investissement net dans une activité à l’étranger, c’est-à-dire les net assets de l’entité étrangère. Ici, le fait décrit est une créance de dividende intragroupe déjà comptabilisée ; ce n’est pas, en tant que tel, l’élément couvert relevant du modèle de net investment hedge.

**Implications pratiques**: Cette approche ne doit pas être retenue pour documenter la partie change de la créance de dividende intragroupe elle-même.

**Référence**:
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.
 - 11
    >the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation