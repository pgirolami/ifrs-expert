# Analyse d'une question comptable

**Date**: 2026-04-05

**Question**:
>Une créance relative à des dividendes intragroupe figure désormais dans les états financiers consolidés, avec une sensibilité corrélative aux fluctuations de change. Peut-on couvrir cette exposition dans le cadre d’une documentation de hedge accounting ?

**Documentation consultée**
   - `ifrs-9`
   - `ifric-16`

## Hypothèses
   - La question est analysée au niveau des états financiers consolidés sous IFRS 9.
   - L’exposition visée correspond à un risque de change sur une créance de dividendes intragroupe désormais comptabilisée comme un poste monétaire en consolidation.
   - La sensibilité de change mentionnée est supposée pouvoir affecter le résultat consolidé.

## Recommandation

**OUI SOUS CONDITIONS**

Oui, seulement si la créance de dividendes intragroupe constitue un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation et affecte le résultat consolidé. Dans ce cas, une documentation de hedge accounting est envisageable; en revanche, une couverture de net investment n’est pas adaptée à ce fait précis.

## Points Opérationnels

   - Il faut démontrer dès l’origine que la créance de dividendes est bien un poste monétaire intragroupe avec effet de change résiduel en résultat consolidé.
   - La documentation doit identifier précisément l’élément couvert, le risque de change couvert et le mode d’évaluation de l’efficacité selon IFRS 9.6.4.1.
   - Si l’exposition de change est totalement éliminée en consolidation, la relation de couverture ne sera pas éligible.
   - Le choix entre fair value hedge et cash flow hedge doit rester cohérent avec la nature exacte de l’exposition de change portée par la créance reconnue.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance doit être un poste monétaire intragroupe<br>- Les gains ou pertes de change ne doivent pas être totalement éliminés en consolidation<br>- Le risque de change doit affecter le résultat consolidé |
| 2. Couverture de flux de trésorerie | OUI SOUS CONDITIONS | - La créance doit être un poste monétaire intragroupe reconnu<br>- Le risque de change doit créer une variabilité pertinente des flux en monnaie fonctionnelle<br>- Cette exposition doit affecter le résultat consolidé et ne pas être totalement éliminée |
| 3. Couverture d’investissement net à l’étranger | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un poste monétaire intragroupe
   - Les gains ou pertes de change ne doivent pas être totalement éliminés en consolidation
   - Le risque de change doit affecter le résultat consolidé

**Raisonnment**:
La créance est un actif reconnu, ce qui est compatible avec un fair value hedge d’un risque particulier. Toutefois, en consolidation, un élément intragroupe n’est éligible que s’il entre dans l’exception des postes monétaires intragroupe dont le risque de change génère des écarts non totalement éliminés et affectant le résultat consolidé.

**Implications pratiques**: La documentation doit viser spécifiquement le risque de change de la créance reconnue en consolidation.

**Référence**:
 - 6.3.5
    >only assets, liabilities... with a party external to the reporting entity can be designated
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.1
    >fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability

### 2. Couverture de flux de trésorerie
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance doit être un poste monétaire intragroupe reconnu
   - Le risque de change doit créer une variabilité pertinente des flux en monnaie fonctionnelle
   - Cette exposition doit affecter le résultat consolidé et ne pas être totalement éliminée

**Raisonnment**:
IFRS 9 permet un cash flow hedge sur la variabilité des flux de trésorerie d’un actif ou passif reconnu attribuable à un risque particulier. Dans cette situation, cela n’est recevable en consolidation que si la créance intragroupe est éligible au titre de l’exception sur les postes monétaires intragroupe exposés au change avec effet en résultat consolidé.

**Implications pratiques**: La relation de couverture devra être calibrée sur l’exposition de change résiduelle réellement visible en consolidation.

**Référence**:
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item
 - 6.5.1
    >cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability
 - 6.4.1
    >the hedging relationship consists only of eligible hedging instruments and eligible hedged items

### 3. Couverture d’investissement net à l’étranger
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le fait décrit porte sur une créance de dividendes intragroupe et non sur un montant de net assets d’une activité étrangère. Le modèle de net investment hedge vise le risque de change attaché à l’investissement net dans une opération étrangère, pas une créance de dividendes isolée.

**Implications pratiques**: Cette exposition ne doit pas être documentée comme une couverture d’investissement net.

**Référence**:
 - 6.5.1
    >hedge of a net investment in a foreign operation as defined in IAS 21
 - ifric-16.2
    >The item being hedged ... may be an amount of net assets
 - ifric-16.10
    >the hedged item can be an amount of net assets equal to or less than the carrying amount