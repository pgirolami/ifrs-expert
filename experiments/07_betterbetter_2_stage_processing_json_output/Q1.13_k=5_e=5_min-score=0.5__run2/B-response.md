{
  "assumptions_fr": [
    "La créance de dividende intragroupe déjà comptabilisée est un poste monétaire entre entités du groupe ayant des monnaies fonctionnelles différentes.",
    "La désignation vise uniquement la composante de risque de change de cette créance, et cette composante est séparément identifiable et mesurable de façon fiable.",
    "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, IFRS 9 admet par exception le risque de change d’un poste monétaire intragroupe comme élément couvert, y compris sous forme de composante de risque. Il faut ensuite documenter la relation à son inception et satisfaire aux critères d’efficacité de la couverture."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, la créance de dividende est déjà comptabilisée, donc il s’agit d’un actif reconnu au stade actuel des faits. Sous les hypothèses retenues, l’exception d’IFRS 9 pour le risque de change d’un poste monétaire intragroupe en consolidation permet de traiter cette exposition comme élément couvert, et une composante de risque peut être désignée si elle est identifiable et mesurable. Cette voie est donc ouverte si la relation est formellement documentée à l’inception et remplit les critères d’efficacité de 6.4.1.",
      "conditions_fr": [
        "Documenter formellement à l’inception la relation de couverture, en identifiant l’instrument de couverture, la créance, le risque de change couvert et la méthode d’évaluation de l’efficacité.",
        "Démontrer une relation économique entre l’élément couvert et l’instrument de couverture, l’absence de domination du risque de crédit et un hedge ratio cohérent."
      ],
      "practical_implication_fr": "L’équipe peut documenter la créance intragroupe comme élément couvert en juste valeur pour sa seule composante de change, puis suivre l’efficacité et l’inefficacité de la couverture en consolidation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "an entity may designate an item in its entirety or a component of an item as the hedged item"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans ce même contexte, la créance est déjà reconnue et IFRS 9 6.5.2(b) permet aussi une couverture de la variabilité des flux de trésorerie attribuable à un risque particulier associé à un actif reconnu. En retenant les hypothèses posées sur le caractère monétaire intragroupe, la composante de change et l’absence d’élimination complète en consolidation, cette approche reste compatible avec les faits. Elle n’est toutefois recevable que si la documentation initiale et les tests d’efficacité de 6.4.1 sont satisfaits.",
      "conditions_fr": [
        "Documenter formellement à l’inception la relation de couverture, en identifiant l’instrument de couverture, la créance, le risque de change couvert et la méthode d’évaluation de l’efficacité.",
        "Démontrer une relation économique entre l’élément couvert et l’instrument de couverture, l’absence de domination du risque de crédit et un hedge ratio cohérent."
      ],
      "practical_implication_fr": "L’entité peut structurer la relation comme une couverture des flux de trésorerie liés au règlement en devise de la créance, avec suivi de l’efficacité selon la documentation de couverture.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
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
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La possibilité existe uniquement en consolidation et uniquement pour la composante de risque de change du poste monétaire intragroupe visé par l’exception d’IFRS 9 6.3.6.",
    "Le stade des faits est compatible avec une désignation sur une créance déjà comptabilisée ; il ne faut pas reformuler l’opération comme une simple transaction prévisionnelle.",
    "Le choix entre juste valeur et flux de trésorerie doit suivre l’objectif de gestion du risque et être arrêté dès l’inception dans la documentation de couverture."
  ]
}
