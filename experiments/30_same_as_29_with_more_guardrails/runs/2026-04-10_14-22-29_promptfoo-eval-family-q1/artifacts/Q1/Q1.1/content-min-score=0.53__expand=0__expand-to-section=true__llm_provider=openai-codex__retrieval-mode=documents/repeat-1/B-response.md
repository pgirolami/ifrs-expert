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
   - Le dividende intragroupe a déjà été décidé et comptabilisé en créance dans les comptes individuels avant consolidation.
   - La créance et la dette de dividende sont libellées dans une devise différente de la monnaie fonctionnelle d'au moins une des entités concernées.
   - La question vise la comptabilité de couverture dans les comptes consolidés sur le risque de change attaché à cette créance intragroupe, et non la couverture d'un investissement net au sens large.

## Recommandation

**OUI SOUS CONDITIONS**

En consolidation, la voie pertinente est la fair value hedge sur le risque de change de la créance intragroupe, mais seulement si la créance est un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés. La cash flow hedge n'est pas adaptée à une créance déjà comptabilisée, et la net investment hedge ne vise pas, en l'état des faits, cette créance de dividende.

## Points Opérationnels

   - Le point clé en consolidation est la visibilité résiduelle des écarts de change : sans effet change non totalement éliminé, la désignation de la créance intragroupe ne tient pas.
   - Le timing compte : une fois le dividende comptabilisé en créance, on bascule d'une logique de transaction future éventuelle à une logique de poste reconnu.
   - La documentation doit être établie au niveau consolidé et alignée sur l'élément couvert réellement admissible dans ce périmètre.
   - Si l'objectif économique porte sur l'investissement dans la filiale étrangère plutôt que sur la créance de dividende, il faut une documentation distincte de net investment hedge ; ce n'est pas la situation décrite ici.


## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Couverture de juste valeur | OUI SOUS CONDITIONS | - La créance de dividende doit être un poste monétaire intragroupe exposé au change.<br>- Les écarts de change sur ce poste ne doivent pas être totalement éliminés en consolidation. |
| 2. Couverture de flux de trésorerie | NON | - (non spécifiées) |
| 3. Couverture d'investissement net | NON | - (non spécifiées) |

### 1. Couverture de juste valeur
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - La créance de dividende doit être un poste monétaire intragroupe exposé au change.
   - Les écarts de change sur ce poste ne doivent pas être totalement éliminés en consolidation.

**Raisonnment**:
Ici, la créance de dividende est déjà comptabilisée : on est donc face à un élément reconnu, ce qui correspond au modèle de couverture d'un actif ou passif reconnu. En consolidation, un poste monétaire intragroupe peut être désigné en couverture seulement si son risque de change génère des écarts non totalement éliminés au niveau consolidé, notamment entre entités de monnaies fonctionnelles différentes.

**Implications pratiques**: Documenter la relation de couverture au niveau consolidé sur la créance intragroupe et limiter le risque couvert à la composante change réellement visible en consolidation.

**Référence**:
 - 6.3.1
    >A hedged item can be a recognised asset or liability
 - 6.3.6
    >the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements

### 2. Couverture de flux de trésorerie
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Cette approche vise des transactions futures ou des flux variables, notamment une transaction intragroupe hautement probable en devise. Or, dans votre cas, le dividende est déjà comptabilisé en créance : il ne s'agit plus d'une transaction future hautement probable mais d'un poste reconnu. La qualification IFRS du cas décrit ne correspond donc pas à une cash flow hedge.

**Implications pratiques**: Ne pas retenir ce modèle pour la partie change d'une créance de dividende déjà enregistrée.

**Référence**:
 - 6.3.1
    >The hedged item can be ... a forecast transaction
 - 6.3.3
    >If a hedged item is a forecast transaction ... that transaction must be highly probable.
 - 6.3.6
    >the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item

### 3. Couverture d'investissement net
**Applicabilité**: NON

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Le modèle de net investment hedge concerne l'exposition de change sur un investissement net dans une activité à l'étranger, pas la couverture ciblée d'une créance de dividende intragroupe déjà comptabilisée. Les faits fournis décrivent un poste de dividende à recevoir, et non une documentation portant sur l'investissement net lui-même. Dans cette situation précise, cette approche n'est donc pas la bonne base de désignation.

**Implications pratiques**: À écarter sauf si la documentation de couverture vise en réalité l'investissement net dans l'entité étrangère, ce qui n'est pas le cas décrit.

**Référence**:
 - 6.3.1
    >The hedged item can be ... a net investment in a foreign operation.
 - 14
    >may be designated as a hedging instrument in a hedge of a net investment in a foreign operation