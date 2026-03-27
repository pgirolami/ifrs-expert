# Analyse d'une question comptable

**Date**: 2026-03-27

**Question**:
>I'm diving into IFRS 9 classification of financial assets, specifically debt instruments held by banks in securitisations that the bank retains or invests in.
Even though most tranches (especially mezzanine and junior/equity) are likely to fail the SPPI test, do we still have to perform the SPPI test every time? Or is there any implicit exemption for contractually linked instruments (CLIs)?

**Documentation consultée**
   - `ifric-16-hedges-of-a-net-investment-in-a-foreign-operation`
   - `ifrs-9-financial-instruments 2025 required`

## Hypothèses
   - Les instruments visés sont des actifs financiers entrant dans le champ d’application d’IFRS 9.
   - La question porte sur la classification ultérieure de tranches de dette en titrisation, et non sur la comptabilité de couverture ni sur la décomptabilisation.
   - Le modèle économique de la banque et les caractéristiques détaillées du pool sous-jacent ne sont pas précisés pour chaque tranche.

## Recommandation

**OUI**

Oui, il faut faire l’analyse SPPI pour chaque tranche pertinente, sans exemption implicite pour les instruments contractuellement liés. Pour les CLIs, IFRS 9 impose même une analyse supplémentaire en look-through; si elle ne peut pas être effectuée à l’origine, la tranche est à la juste valeur par résultat.

## Points Opérationnels

   - L’analyse CLI/SPPI se fait à la comptabilisation initiale de chaque tranche retenue ou acquise; elle n’est pas facultative.
   - Pour un instrument contractuellement lié, il faut aller au-delà de la tranche et remonter jusqu’au pool d’instruments qui crée les flux.
   - Le fait qu’une tranche soit mezzanine ou junior peut conduire souvent à une conclusion JVR en pratique, mais seulement après l’analyse requise par IFRS 9, pas par présomption.
   - Si le détenteur ne peut pas apprécier les conditions de B4.1.21 à l’origine, la conséquence opérationnelle est directement la juste valeur par résultat.

## Approches évaluées

| Approche | Applicabilité | Conditions |
| --- | --- | --- |
| 1. Coût amorti | OUI SOUS CONDITIONS | - Le modèle économique de la banque est de détenir l’actif pour encaisser les flux contractuels.<br>- La tranche satisfait aux conditions spécifiques des instruments contractuellement liés et cette analyse peut être démontrée à la comptabilisation initiale. |
| 2. Juste valeur par autres éléments du résultat global | OUI SOUS CONDITIONS | - Le modèle économique de la banque est atteint par la collecte des flux contractuels et par la vente des actifs financiers.<br>- La tranche satisfait aux conditions spécifiques des instruments contractuellement liés et cette analyse peut être démontrée à la comptabilisation initiale. |
| 3. Juste valeur par résultat | OUI | - (non spécifiées) |

### 1. Coût amorti
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le modèle économique de la banque est de détenir l’actif pour encaisser les flux contractuels.
   - La tranche satisfait aux conditions spécifiques des instruments contractuellement liés et cette analyse peut être démontrée à la comptabilisation initiale.

**Raisonnment**:
Dans votre cas de tranches de titrisation détenues ou retenues par une banque, le coût amorti n’est possible que si la tranche passe l’analyse spécifique des instruments contractuellement liés et si la banque est dans un modèle de détention pour encaisser. Il n’existe pas de dispense implicite pour les CLIs : IFRS 9 exige au contraire de regarder la tranche et le pool sous-jacent; à défaut d’évaluation possible à l’origine, ce classement tombe.

**Implications pratiques**: Documenter dès l’origine le look-through sur le pool sous-jacent et le modèle « détenir pour encaisser ».

**Référence**:
 - 4.1.2
    >held within a business model whose objective is to hold financial assets in order to collect contractual cash flows
 - B4.1.21
    >a tranche has cash flow characteristics that are payments of principal and interest on the principal amount outstanding only if
 - B4.1.26
    >If the holder cannot assess the conditions in paragraph B4.1.21 at initial recognition, the tranche must be measured at fair value through profit or loss.

### 2. Juste valeur par autres éléments du résultat global
**Applicabilité**: OUI SOUS CONDITIONS

**Conditions**:
   - Le modèle économique de la banque est atteint par la collecte des flux contractuels et par la vente des actifs financiers.
   - La tranche satisfait aux conditions spécifiques des instruments contractuellement liés et cette analyse peut être démontrée à la comptabilisation initiale.

**Raisonnment**:
Dans cette situation, la FVOCI n’est ouverte que si la tranche de titrisation satisfait d’abord l’analyse CLI/SPPI, puis si elle est gérée dans un modèle de collecte et vente. Là encore, il n’y a aucune exemption implicite pour les CLIs : l’évaluation de la tranche et du pool sous-jacent reste nécessaire avant d’envisager ce classement.

**Implications pratiques**: Documenter dès l’origine le look-through et un modèle « collecte et vente » cohérent avec la gestion du portefeuille.

**Référence**:
 - 4.1.2A
    >objective is achieved by both collecting contractual cash flows and selling financial assets
 - B4.1.21
    >a tranche has cash flow characteristics that are payments of principal and interest on the principal amount outstanding only if
 - B4.1.26
    >If the holder cannot assess the conditions in paragraph B4.1.21 at initial recognition, the tranche must be measured at fair value through profit or loss.

### 3. Juste valeur par résultat
**Applicabilité**: OUI

**Conditions**:
   - (conditions non spécifiées)

**Raisonnment**:
Dans votre cas, la juste valeur par résultat est la catégorie résiduelle et devient l’issue obligatoire dès que la tranche ne satisfait pas l’analyse CLI/SPPI ou que cette analyse ne peut pas être faite à l’origine. C’est précisément le point clé pour les tranches de titrisation : IFRS 9 ne crée pas d’exemption, mais une règle explicite de bascule en JVR en cas d’échec ou d’impossibilité d’évaluation.

**Implications pratiques**: Si la tranche échoue au test CLI/SPPI ou si l’information initiale est insuffisante, la classer en juste valeur par résultat.

**Référence**:
 - 4.1.4
    >A financial asset shall be measured at fair value through profit or loss unless
 - B4.1.26
    >the tranche must be measured at fair value through profit or loss
