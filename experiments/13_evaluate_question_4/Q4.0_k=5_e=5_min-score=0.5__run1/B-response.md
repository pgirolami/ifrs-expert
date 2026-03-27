# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>I'm diving into IFRS 9 classification of financial assets, specifically debt instruments held by banks in securitisations that the bank retains or invests in.
Even though most tranches (especially mezzanine and junior/equity) are likely to fail the SPPI test, do we still have to perform the SPPI test every time? Or is there any implicit exemption for contractually linked instruments (CLIs)?

**Documentation consultée**
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - Les positions de titrisation concernées sont des actifs financiers entrant dans le champ d’application d’IFRS 9.
   - La question vise des tranches de titrisation de nature dette, et non l’élection OCI propre à certains instruments de capitaux propres.

## Recommandation

**OUI**

Oui. Pour des tranches de titrisation, IFRS 9 ne prévoit aucune exemption implicite au test SPPI pour les contractually linked instruments. Au contraire, il impose une analyse spécifique de la tranche et du pool sous-jacent; si cette analyse échoue ou ne peut pas être faite à l’origine, la tranche va au FVTPL.

## Points Opérationnels

   - L’analyse CLI/SPPI se fait par instrument ou par tranche à la comptabilisation initiale; il n’existe pas de dispense implicite pour les titrisations.
   - Pour un CLI, l’examen ne s’arrête pas au coupon de la tranche: il faut regarder la tranche, le rang de subordination et le pool sous-jacent jusqu’à identifier le pool pertinent.
   - Si le détenteur ne peut pas apprécier les conditions de B4.1.21 à l’origine, ou si le pool peut évoluer de façon à ne plus respecter les critères requis, la tranche doit être classée en FVTPL.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - le modèle économique est la détention pour encaissement<br>- la tranche satisfait aux conditions spécifiques des CLIs après analyse du pool sous-jacent dès la comptabilisation initiale |
| 2. Juste valeur par OCI | OUI SOUS CONDITIONS | - le modèle économique combine encaissement des flux contractuels et ventes<br>- la tranche satisfait aux conditions spécifiques des CLIs après analyse du pool sous-jacent dès la comptabilisation initiale |
| 3. Juste valeur par résultat | OUI | - (non spécifiées) |

### 1. Coût amorti
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - le modèle économique est la détention pour encaissement
   - la tranche satisfait aux conditions spécifiques des CLIs après analyse du pool sous-jacent dès la comptabilisation initiale

**Raisonnment**:
Pour une tranche de titrisation conservée ou achetée par une banque, le coût amorti n’est disponible que si l’actif est géré pour encaisser les flux contractuels et si la tranche passe l’analyse SPPI. Pour un CLI, IFRS 9 impose en plus un examen de la tranche et un look-through vers le pool sous-jacent; il n’existe donc pas de dispense implicite.

**Implications pratiques**: Sans analyse CLI/SPPI documentée, la banque ne peut pas soutenir une classification au coût amorti.

**Référence**:
 - 4.1.2
    >measured at amortised cost if both of the following conditions are met
 - B4.1.22
    >An entity must look through until it can identify the underlying pool

### 2. Juste valeur par OCI
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - le modèle économique combine encaissement des flux contractuels et ventes
   - la tranche satisfait aux conditions spécifiques des CLIs après analyse du pool sous-jacent dès la comptabilisation initiale

**Raisonnment**:
Pour une tranche de titrisation détenue par une banque, le FVOCI n’est possible que si le modèle économique combine encaissement et ventes, et si les flux contractuels respectent le SPPI. Pour un CLI, cette conclusion ne peut être atteinte qu’après l’analyse spécifique prévue par IFRS 9; il n’y a pas d’exemption implicite.

**Implications pratiques**: Le FVOCI reste possible pour certaines tranches, mais seulement après une analyse CLI/SPPI concluante et documentée.

**Référence**:
 - 4.1.2A
    >measured at fair value through other comprehensive income if both of the following conditions are met
 - B4.1.21
    >a tranche has cash flow characteristics that are payments of principal and interest

### 3. Juste valeur par résultat
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans cette situation, le FVTPL est la catégorie résiduelle et devient obligatoire si la tranche ne satisfait pas l’analyse CLI/SPPI ou si le porteur ne peut pas l’évaluer à l’origine. Cela couvre précisément beaucoup de tranches complexes de titrisation, notamment lorsque la subordination ou le pool sous-jacent empêchent de démontrer le SPPI.

**Implications pratiques**: À défaut d’analyse CLI/SPPI concluante à l’origine, la classification bascule en FVTPL.

**Référence**:
 - 4.1.4
    >shall be measured at fair value through profit or loss unless
 - B4.1.26
    >the tranche must be measured at fair value through profit or loss
