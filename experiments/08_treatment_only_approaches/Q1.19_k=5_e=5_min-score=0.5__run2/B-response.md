{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà créé une créance et une dette intragroupe monétaires entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, ce risque de change peut être formellement documenté en consolidation grâce à l’exception IFRS 9 sur les éléments monétaires intragroupe. La couverture de juste valeur est la voie la plus directement alignée avec une créance déjà reconnue, sous réserve de la désignation initiale, de la documentation et des critères d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le poste visé est déjà une créance intragroupe monétaire reconnue. IFRS 9 exclut en principe les postes intragroupe, mais prévoit en consolidation une exception explicite pour le risque de change d’un élément monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés et affectent le résultat.\nLe modèle de juste valeur correspond directement à un actif reconnu exposé à un risque particulier. Il peut donc être formellement documenté ici si la relation est désignée à l’origine et satisfait aux exigences d’efficacité.",
      "conditions_fr": [
        "La créance de dividende est un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes.",
        "Les écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
        "La relation de couverture est désignée et documentée dès l’inception avec instrument, élément couvert, risque couvert et méthode d’évaluation de l’efficacité."
      ],
      "practical_implication_fr": "En pratique, c’est le modèle le plus naturel pour documenter le risque de change d’une créance de dividende déjà comptabilisée en consolidation.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, IFRS 9 permet aussi une couverture de flux de trésorerie pour un actif ou passif reconnu lorsque la variabilité de flux liée à un risque particulier peut affecter le résultat. L’exception visant l’élément monétaire intragroupe permet donc d’envisager une documentation formelle aussi sous ce modèle.\nCette voie est toutefois plus conditionnelle ici: il faut documenter le risque de change comme une variabilité de flux du poste reconnu et démontrer, en plus, que les critères de désignation et d’efficacité sont respectés en consolidation.",
      "conditions_fr": [
        "La créance de dividende intragroupe entre dans l’exception de l’élément monétaire intragroupe en consolidation.",
        "L’exposition est documentée comme une variabilité de flux de trésorerie liée au risque de change du poste reconnu.",
        "La relation de couverture est désignée et documentée dès l’inception et satisfait aux critères d’efficacité."
      ],
      "practical_implication_fr": "Cette documentation est possible, mais elle demande un cadrage plus soigneux de l’exposition couverte que dans une couverture de juste valeur.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        },
        {
          "section": "6.3.2",
          "excerpt": "The hedged item must be reliably measurable."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être mise en place à l’inception de la relation de couverture, avec identification de l’instrument, du poste couvert, du risque couvert et du test d’efficacité.",
    "Le dossier de consolidation doit démontrer que la créance de dividende est bien un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé.",
    "Entre les deux modèles, la couverture de juste valeur est la plus directement cohérente avec une créance intragroupe déjà reconnue."
  ]
}
