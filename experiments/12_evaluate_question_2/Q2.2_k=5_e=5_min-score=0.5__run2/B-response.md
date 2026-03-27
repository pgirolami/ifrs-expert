# Analyse d'une question comptable

**Date**: 2026-03-27T09:20:15.887741+00:00
**Question**:
>Question not provided

**Documentation consultée**
   - (documentation non disponible)

## Hypothèses
La question porte sur le classement et l’évaluation d’un actif financier selon IFRS 9.
L’enjeu est de déterminer si une clause contractuelle pouvant modifier le calendrier ou le montant des flux remet en cause la condition SPPI et, par conséquent, les bases d’évaluation possibles.

## Recommandation

**oui_sous_conditions**
La présence d’une clause modifiant les flux ne fait pas échouer automatiquement le test SPPI. Dans cette situation, il faut analyser les flux avant et après le changement, ainsi que la nature du déclencheur ; si les flux restent compatibles avec principal et intérêt, le critère de prêt basique peut être respecté.

## Approches évaluées

### Coût amorti
**Applicabilité**: oui_sous_conditions

**Conditions**:
   - L’analyse de la clause montre que les flux avant et après le déclenchement restent compatibles avec un prêt basique.
   - Le modèle économique applicable permet la mesure au coût amorti.

**Raisonnment**:
Dans cette situation, le coût amorti reste possible si la clause de déclenchement ne fait pas sortir les flux contractuels d’un schéma de principal et intérêt. Le texte impose d’examiner les flux susceptibles de naître avant et après le changement, de sorte que la seule existence de la clause ne suffit pas à exclure ce traitement.

**Implications pratiques**: Une analyse contractuelle détaillée de la clause est nécessaire avant de conclure au coût amorti.

**Référence**:
 - B4.1.10
    >the entity must assess the contractual cash flows that could arise both before, and after, the change in contractual cash flows.
 - B4.1.11
    >contractual terms that result in contractual cash flows that are solely payments of principal and interest

### Juste valeur par OCI
**Applicabilité**: oui_sous_conditions

**Conditions**:
   - L’analyse de la clause confirme que les flux avant et après le déclenchement restent compatibles avec un prêt basique.
   - Le modèle économique applicable permet la mesure à la juste valeur par OCI.

**Raisonnment**:
Dans cette situation, la FVOCI peut aussi rester ouverte si, malgré la clause susceptible d’altérer les flux, ceux-ci demeurent des paiements de principal et d’intérêt. Le fait qu’un événement déclencheur existe impose une évaluation ciblée des flux potentiels, mais n’emporte pas à lui seul l’échec du SPPI.

**Implications pratiques**: La conclusion SPPI sur la clause est un préalable avant d’examiner l’éligibilité à la FVOCI.

**Référence**:
 - B4.1.10
    >the entity must determine whether the contractual cash flows that could arise over the life of the instrument due to that contractual term are solely payments of principal and interest
 - B4.1.11
    >a contractual term that permits the issuer or the holder to extend the contractual term

### Juste valeur par résultat
**Applicabilité**: oui_sous_conditions

**Conditions**:
   - La clause a un effet authentique et plus que de minimis sur les flux contractuels.
   - Cet effet conduit les flux potentiels à ne plus être compatibles avec un prêt basique.

**Raisonnment**:
Dans cette situation, la juste valeur par résultat s’impose si l’analyse de la clause montre que les flux pouvant résulter du déclenchement ne sont plus uniquement du principal et de l’intérêt. Le texte indique aussi que la nature du déclencheur est un indicateur utile : un déclencheur lié à un indice actions est plus problématique qu’un ajustement lié à des impayés.

**Implications pratiques**: Si la clause introduit une exposition incompatible avec principal et intérêt, l’actif doit être mesuré à la juste valeur par résultat.

**Référence**:
 - B4.1.10
    >The entity may also need to assess the nature of any contingent event (ie the trigger)
 - B4.1.18
    >could have only a de minimis effect on the contractual cash flows of the financial asset
