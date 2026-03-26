{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a créé une créance/dette intragroupe comptabilisée, constituant un poste monétaire.",
    "Cette créance/dette est libellée dans une monnaie qui génère une exposition de change dans les comptes consolidés, car les entités concernées ont des monnaies fonctionnelles différentes.",
    "La question porte sur l’application du hedge accounting au risque de change dans des comptes consolidés selon IFRS 9."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. Une créance/dette de dividende intragroupe déjà comptabilisée peut entrer dans l’exception applicable aux postes monétaires intragroupe en consolidation si les écarts de change ne sont pas entièrement éliminés. La relation doit en outre être formellement désignée et documentée dès son inception."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans les comptes consolidés, l’intragroupe est en principe exclu, mais votre cas correspond à l’exception visant un poste monétaire intragroupe. Une créance de dividende déjà comptabilisée est un actif reconnu ; si ses écarts de change ne sont pas entièrement éliminés en consolidation, le risque de change peut être désigné. C’est la lecture la plus directe ici pour un poste déjà enregistré.",
      "conditions_fr": [
        "Les écarts de change sur la créance/dette de dividende intragroupe ne sont pas entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "La couverture peut être documentée en consolidation sur la créance/dette déjà comptabilisée, avec une désignation formelle du risque de change couvert.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ce modèle reste envisageable car IFRS 9 vise aussi un actif ou passif reconnu lorsqu’il existe une variabilité des flux de trésorerie attribuable au risque couvert. Dans votre situation, cela suppose de documenter que le risque de change couvert est la variabilité des flux de règlement de la créance/dette de dividende en consolidation, tout en satisfaisant l’exception applicable aux postes monétaires intragroupe.",
      "conditions_fr": [
        "Les écarts de change sur la créance/dette de dividende intragroupe ne sont pas entièrement éliminés en consolidation.",
        "La relation désignée vise la variabilité des flux de règlement en monnaie fonctionnelle liée au change sur l’actif/passif intragroupe reconnu."
      ],
      "practical_implication_fr": "La documentation doit viser les flux de règlement futurs de la créance/dette de dividende et non un simple principe général de couverture intragroupe.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation de couverture doit être établie à l’inception de la relation ; elle ne se rétrodate pas.",
    "Il faut démontrer en consolidation que la créance/dette de dividende intragroupe génère bien des écarts de change non entièrement éliminés.",
    "Parmi les traitements identifiés, la couverture de juste valeur est la lecture la plus directe pour une créance de dividende déjà comptabilisée."
  ]
}
