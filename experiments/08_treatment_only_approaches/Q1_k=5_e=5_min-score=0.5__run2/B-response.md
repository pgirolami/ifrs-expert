{
  "assumptions_fr": [
    "Le dividende intragroupe a été déclaré et a donné lieu à la comptabilisation d’une créance/dette intragroupe monétaire libellée en devise.",
    "Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change liés à cette créance/dette ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions, en comptes consolidés si la créance de dividende intragroupe est un élément monétaire en devise et si ses écarts de change affectent le résultat consolidé.\nDans cette situation, le traitement pertinent est la couverture de juste valeur, avec désignation formelle, documentation initiale et respect des critères d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende intragroupe déjà comptabilisée est un actif monétaire reconnu.\nEn comptes consolidés, IFRS 9 permet par exception de désigner le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé, ce qui correspond aux hypothèses.\nLe modèle adapté est donc la couverture de juste valeur d’un actif reconnu exposé au risque de change.",
      "conditions_fr": [
        "La créance de dividende intragroupe doit être un élément monétaire libellé en devise.",
        "Les écarts de change doivent ne pas être totalement éliminés en consolidation et affecter le résultat consolidé.",
        "La relation de couverture doit être désignée et documentée dès l’origine, avec identification du risque couvert, du ratio de couverture et de l’évaluation de l’efficacité."
      ],
      "practical_implication_fr": "Vous pouvez documenter une couverture en consolidation sur la composante change de cette créance, sous le modèle de juste valeur.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
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
      "applicability": "non",
      "reasoning_fr": "Dans cette situation, la question vise une créance de dividende intragroupe déjà reconnue, et non une transaction future hautement probable.\nLe risque traité en consolidation est la revalorisation de change d’un élément monétaire intragroupe reconnu.\nAu vu des textes fournis, ce profil correspond au schéma d’un actif reconnu à couvrir en juste valeur, pas à une variabilité de flux futurs à traiter en cash flow hedge.",
      "conditions_fr": [
        "Ce modèle viserait une variabilité de flux de trésorerie, ce qui ne correspond pas ici à une créance de dividende déjà comptabilisée."
      ],
      "practical_implication_fr": "La documentation de couverture ne devrait pas être structurée ici comme une couverture de flux de trésorerie.",
      "references": [
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être établie à l’inception de la relation de couverture, pas a posteriori.",
    "La désignation doit viser explicitement le risque de change sur la créance/dette intragroupe, et non le dividende intragroupe éliminé en lui-même.",
    "La condition clé en consolidation est que les écarts de change sur l’élément monétaire intragroupe affectent le résultat consolidé.",
    "Il faut documenter l’instrument de couverture, l’élément couvert, le risque couvert, le ratio de couverture et la manière d’apprécier l’efficacité."
  ]
}
