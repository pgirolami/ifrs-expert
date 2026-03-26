{
  "assumptions_fr": [
    "Le dividende intragroupe décidé a créé une créance monétaire intragroupe comptabilisée et une dette correspondante.",
    "La créance existe entre des entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans cette situation, la créance est un actif comptabilisé et l’exception IFRS 9 visant le risque de change d’un élément monétaire intragroupe en consolidation peut s’appliquer. L’intégration dans une relation de couverture documentée est possible si la désignation initiale, la documentation et les critères d’efficacité sont respectés."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans ce cas précis, la créance issue du dividende décidé est un actif comptabilisé, mais elle est intragroupe : en principe elle serait exclue en consolidation. Toutefois, selon les hypothèses retenues, il s’agit d’un élément monétaire entre entités à monnaies fonctionnelles différentes et les écarts de change ne sont pas totalement éliminés ; l’exception IFRS 9 permet alors de désigner ce risque de change. La relation ne sera recevable que si elle est formellement documentée dès l’origine et satisfait aux critères d’efficacité.",
      "conditions_fr": [
        "La créance doit être un élément monétaire intragroupe générant des écarts de change non totalement éliminés en consolidation.",
        "La composante de risque de change désignée doit être séparément identifiable et mesurable de façon fiable.",
        "La relation de couverture doit être désignée et documentée dès l’origine avec l’instrument, l’élément couvert, le risque couvert et le ratio de couverture.",
        "Le risque couvert doit pouvoir affecter le résultat consolidé."
      ],
      "practical_implication_fr": "La documentation de couverture peut viser la composante de change de la créance intragroupe comme élément couvert dans une couverture de juste valeur, sous réserve de démontrer son éligibilité et l’efficacité de la relation.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.2",
          "excerpt": "The hedged item must be reliably measurable."
        },
        {
          "section": "B6.3.8",
          "excerpt": "a risk component must be a separately identifiable component ... and ... reliably measurable"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk and could affect profit or loss"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter la relation au démarrage : créance couverte, composante de change, instrument de couverture, objectif de gestion et ratio de couverture.",
    "Conserver la preuve que la créance est monétaire, intragroupe, et que les écarts de change ne sont pas totalement éliminés en consolidation.",
    "Vérifier et tracer la relation économique, l’absence de domination du risque de crédit et l’absence de ratio artificiellement déséquilibré.",
    "S’assurer que l’effet visé concerne bien le résultat consolidé."
  ]
}
