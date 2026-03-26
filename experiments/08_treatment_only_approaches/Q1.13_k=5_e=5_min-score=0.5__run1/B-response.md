{
  "assumptions_fr": [
    "On suppose que la créance/dividende intragroupe constitue un poste monétaire en devise entre des entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "On suppose que l'entité dispose d'un instrument de couverture éligible et que la désignation formelle ainsi que la documentation exigées par IFRS 9.6.4.1 sont en place."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans cette situation, l'interdiction générale visant les éléments intragroupe est levée par l'exception IFRS 9 applicable aux postes monétaires intragroupe exposés au change en consolidation. La composante de risque de change de la créance peut donc être intégrée dans une relation de couverture documentée, sous réserve du respect des critères de désignation, de mesurabilité et d'efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans ce cas, la créance de dividende est déjà comptabilisée et, selon l'hypothèse posée, c'est un poste monétaire intragroupe en devise dont l'effet de change subsiste en consolidation.\nMême si la règle générale exclut les éléments intragroupe, l'exception d'IFRS 9.6.3.6 permet alors de désigner ce risque de change comme élément couvert, et la couverture de juste valeur correspond bien à une exposition sur un actif comptabilisé.",
      "conditions_fr": [
        "La créance doit être un poste monétaire intragroupe en devise dont les écarts de change ne sont pas totalement éliminés en consolidation.",
        "La composante de risque de change désignée doit être séparément identifiable et mesurable de façon fiable.",
        "La relation doit être désignée et documentée dès l'origine avec test d'efficacité et hedge ratio conforme."
      ],
      "practical_implication_fr": "La documentation doit viser la variation de valeur de la créance attribuable au risque de change en consolidation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "changes in the cash flows or fair value of an item attributable to a specific risk or risks"
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
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance intragroupe reconnue donnera lieu à un encaissement futur dont l'équivalent en monnaie fonctionnelle varie avec le change jusqu'au règlement.\nSous l'hypothèse que ce risque de change affecte le résultat consolidé et que l'exception des postes monétaires intragroupe s'applique, IFRS 9 permet aussi d'analyser cette exposition comme une variabilité de flux sur un actif comptabilisé, à documenter et tester formellement.",
      "conditions_fr": [
        "La variabilité de change des flux liés à la créance doit pouvoir affecter le résultat consolidé dans les comptes consolidés.",
        "La créance doit relever de l'exception IFRS 9 pour les postes monétaires intragroupe en devise.",
        "La relation doit satisfaire à la désignation, à la documentation initiale et aux exigences d'efficacité d'IFRS 9.6.4.1."
      ],
      "practical_implication_fr": "La documentation doit démontrer que la variabilité de change des flux de règlement de la créance est bien l'exposition couverte.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier en priorité que la créance de dividende est bien un poste monétaire en devise entre entités aux monnaies fonctionnelles différentes et que son écart de change n'est pas totalement éliminé en consolidation.",
    "La relation de couverture doit être formellement désignée dès son inception, avec identification de l'instrument, de la créance couverte, du risque de change, du hedge ratio et de la méthode d'évaluation de l'efficacité.",
    "Le choix entre couverture de juste valeur et couverture de flux de trésorerie doit être aligné sur l'objectif de gestion du risque effectivement documenté pour cette créance."
  ]
}
