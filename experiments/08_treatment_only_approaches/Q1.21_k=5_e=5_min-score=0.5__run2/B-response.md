{
  "assumptions_fr": [
    "On suppose que le receivable de dividendes intragroupe est un élément monétaire comptabilisé dont les écarts de change ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidation, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés. Dans cette situation supposée, la désignation est donc possible, sous réserve des critères de documentation et d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le receivable de dividendes intragroupe est un actif comptabilisé.\nLa règle générale exclut les éléments intragroupe en consolidation, mais IFRS 9 admet une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés.\nSous cette hypothèse, une couverture de juste valeur du risque de change peut être désignée si elle affecte le résultat consolidé et respecte les critères de qualification.",
      "conditions_fr": [
        "Le receivable est un élément monétaire intragroupe comptabilisé.",
        "Les écarts de change ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé.",
        "La relation de couverture satisfait aux exigences d’IFRS 9.6.4.1, notamment désignation formelle, documentation, relation économique et hedge ratio."
      ],
      "practical_implication_fr": "Le groupe peut traiter l’exposition comme élément couvert au titre d’une fair value hedge du risque de change, si la documentation et l’efficacité sont établies dès l’origine.",
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
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... attributable to a particular risk and could affect profit or loss."
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
      "reasoning_fr": "Dans cette situation, IFRS 9 permet aussi une couverture de flux de trésorerie d’un actif comptabilisé pour la variabilité des flux attribuable à un risque particulier.\nSi l’encaissement du dividende en devise crée une variabilité des flux en monnaie fonctionnelle qui affecte le résultat consolidé, l’exception applicable aux éléments monétaires intragroupe permet la désignation.\nCe traitement reste subordonné à la documentation initiale et aux exigences d’efficacité de la relation de couverture.",
      "conditions_fr": [
        "Le receivable est un actif comptabilisé dont les flux en monnaie fonctionnelle varient du fait du risque de change.",
        "Les écarts de change liés à l’élément monétaire intragroupe affectent le résultat consolidé car ils ne sont pas entièrement éliminés.",
        "La relation de couverture remplit les critères d’IFRS 9.6.4.1, y compris la documentation formelle et le hedge ratio approprié."
      ],
      "practical_implication_fr": "Le groupe peut retenir le modèle de cash flow hedge pour cette exposition si sa gestion du risque vise la variabilité des flux liés à l’encaissement en devise.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.3.2",
          "excerpt": "The hedged item must be reliably measurable."
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter dès l’origine l’élément couvert, l’instrument de couverture, le risque de change couvert et la méthode d’évaluation de l’efficacité.",
    "Établir de façon probante que les écarts de change du receivable intragroupe ne sont pas totalement éliminés en consolidation et affectent bien le résultat consolidé.",
    "Choisir un seul modèle de couverture cohérent avec la gestion du risque du groupe sur cette exposition et avec le hedge ratio effectivement utilisé."
  ]
}
