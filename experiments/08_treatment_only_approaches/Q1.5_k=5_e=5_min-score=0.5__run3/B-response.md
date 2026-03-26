{
  "assumptions_fr": [
    "Le dividende intragroupe est déjà comptabilisé comme une créance/dette en devise entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Pour cette analyse de couverture, ce solde de dividende reconnu est traité comme un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Sous les hypothèses retenues, une relation de couverture au niveau consolidé est possible, car l’IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe non totalement éliminé en consolidation.\nCela reste subordonné à une désignation et une documentation formelles dès l’origine, ainsi qu’au respect des critères d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende intragroupe est supposée être un élément monétaire en devise dont les écarts de change ne sont pas totalement éliminés en consolidation.\nElle peut donc être un élément couvert au niveau consolidé par l’exception de l’IFRS 9 6.3.6, et il s’agit d’un actif reconnu entrant dans le champ d’une couverture de juste valeur.\nL’applicabilité dépend ensuite de la désignation formelle, de la documentation initiale et des critères d’efficacité prévus par l’IFRS 9 6.4.1.",
      "conditions_fr": [
        "La créance de dividende doit constituer un élément monétaire intragroupe en devise.",
        "Les écarts de change doivent ne pas être totalement éliminés en consolidation.",
        "La relation doit être désignée et documentée dès l’origine avec démonstration de l’efficacité."
      ],
      "practical_implication_fr": "Il faut une documentation de couverture au niveau consolidé identifiant la créance de dividende, le risque de change couvert et l’instrument de couverture.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
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
      "reasoning_fr": "Dans cette situation, la créance reconnue expose le groupe à une variabilité des flux de trésorerie en monnaie fonctionnelle jusqu’au règlement, du fait du risque de change.\nL’IFRS 9 6.5.2(b) vise aussi les actifs reconnus, et l’exception de 6.3.6 permet ici de traiter l’élément monétaire intragroupe comme élément couvert en consolidation.\nCette voie n’est toutefois disponible que si la relation est formellement documentée dès l’origine et satisfait aux exigences d’efficacité de l’IFRS 9 6.4.1.",
      "conditions_fr": [
        "La variabilité des flux en monnaie fonctionnelle du groupe doit provenir du risque de change sur la créance de dividende.",
        "L’élément doit relever de l’exception applicable aux éléments monétaires intragroupe en consolidation.",
        "La documentation initiale doit préciser le risque couvert, le ratio de couverture et l’évaluation de l’efficacité."
      ],
      "practical_implication_fr": "Le groupe doit démontrer que le risque de change sur le dividende affecte bien les flux de trésorerie consolidés couverts jusqu’au règlement.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "However, as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Au niveau consolidé, le point clé est l’exception de l’IFRS 9 6.3.6 aux règles générales sur les éléments intragroupe.",
    "La documentation de couverture doit exister dès l’origine et identifier l’instrument de couverture, l’élément couvert, le risque de change et la méthode d’évaluation de l’efficacité.",
    "Le groupe doit pouvoir étayer que les écarts de change sur la créance de dividende affectent le résultat consolidé et ne sont pas totalement éliminés en consolidation."
  ]
}
