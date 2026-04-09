# Analyse d'une question comptable

**Date**: 2026-04-09

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
   - La créance de dividende intragroupe est libellée dans une devise autre que la monnaie fonctionnelle de l’une des entités concernées.
   - L’analyse est faite dans les comptes consolidés IFRS du groupe.
   - La créance de dividende est déjà comptabilisée à recevoir ; il s’agit donc d’un poste intragroupe reconnu et non d’une transaction future encore non comptabilisée.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, en principe, mais seulement si la créance de dividende constitue un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation. Dans ce cas, seule la composante de change peut être désignée comme risque couvert ; en pratique, le modèle le plus cohérent ici est la couverture de juste valeur.

## Points Opérationnels

   - Le point décisif est de qualifier la créance de dividende comme poste monétaire intragroupe et de vérifier que l’écart de change affecte bien le résultat consolidé.
   - Si ce critère est rempli, seule la composante de change peut être désignée comme risque couvert, car IFRS 9 autorise la désignation d’une composante de risque séparément identifiable et mesurable.
   - La documentation de couverture doit être en place dès l’origine de la relation et inclure l’instrument de couverture, le poste couvert, le risque de change couvert et la manière d’évaluer l’efficacité.
   - Si le dividende n’est pas encore comptabilisé mais seulement prévu, l’analyse bascule vers une transaction future intragroupe hautement probable ; ce n’est pas le cas retenu ici.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende est un poste monétaire intragroupe.<br>- Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation.<br>- La relation de couverture satisfait aux critères de désignation, documentation et efficacité d’IFRS 9. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d’investissement net | NON | - (non spécifiées) |
| 4. Comptabilisation ordinaire du change | OUI | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende est un poste monétaire intragroupe.
   - Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation.
   - La relation de couverture satisfait aux critères de désignation, documentation et efficacité d’IFRS 9.

**Raisonnment**:
Ici, la créance de dividende déjà comptabilisée est un actif reconnu. IFRS 9 permet de couvrir un actif reconnu et aussi de désigner uniquement une composante de risque, y compris le risque de change, si cette composante est identifiable séparément et mesurable de façon fiable. En consolidation, cela n’est possible pour un poste intragroupe que si l’écart de change sur ce poste monétaire n’est pas totalement éliminé.

**Implications pratiques**: Possible de désigner uniquement le risque de change de la créance intragroupe, sous réserve de documenter formellement la relation de couverture.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.3.7
    >only changes in the cash flows or fair value ... attributable to a specific risk or risks
 - 6.5.2(a)
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset
 - 45
    >an intragroup monetary asset (or liability) ... cannot be eliminated ... without showing the results of currency fluctuations

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation précise, le dividende est déjà comptabilisé à recevoir ; l’exposition porte donc sur une créance monétaire reconnue, et non sur une transaction future hautement probable. Le modèle de couverture des flux de trésorerie vise surtout la variabilité des flux futurs ou des transactions prévues ; il ne correspond pas le mieux au fait décrit.

**Implications pratiques**: Ce modèle n’est pas le bon véhicule pour couvrir le risque de change d’une créance de dividende déjà reconnue.

**Référence**:
 - 6.5.2(b)
    >cash flow hedge: a hedge of the exposure to variability in cash flows
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify

### 3. Couverture d’investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Une créance de dividende intragroupe à encaisser correspond en principe à un règlement attendu entre entités du groupe, et non à un élément faisant partie de l’investissement net dans une activité à l’étranger. Le traitement de couverture d’investissement net vise les expositions sur l’investissement net lui-même, pas une créance de dividende ordinaire.

**Implications pratiques**: À défaut de démontrer que le poste fait partie de l’investissement net, ce modèle n’est pas disponible.

**Référence**:
 - 32
    >a monetary item that forms part of a reporting entity’s net investment in a foreign operation
 - 6.5.2(c)
    >hedge of a net investment in a foreign operation
 - 10
    >Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency.

### 4. Comptabilisation ordinaire du change
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
À défaut de relation de couverture qualifiante, les écarts de change sur le poste monétaire intragroupe restent comptabilisés selon IAS 21. En consolidation, ces écarts peuvent subsister précisément parce qu’un poste monétaire intragroupe ne s’élimine pas sans faire apparaître l’effet de change.

**Implications pratiques**: En l’absence de hedge accounting qualifiant, la variation de change sur la créance sera traitée en résultat selon IAS 21.

**Référence**:
 - 28
    >Exchange differences arising on the settlement of monetary items ... shall be recognised in profit or loss
 - 45
    >cannot be eliminated ... without showing the results of currency fluctuations