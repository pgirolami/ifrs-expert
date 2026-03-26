{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a créé une créance et une dette intragroupe libellées en devise entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change sur cet élément monétaire intragroupe ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, les opérations intragroupe sont en principe exclues, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe si les écarts de change ne sont pas totalement éliminés. Dans cette situation, la comptabilité de couverture est donc possible sous réserve du respect des critères de désignation, documentation et efficacité; la couverture de juste valeur est la voie la plus directe."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe a déjà été comptabilisé en créance à recevoir, donc l’exposition porte sur un actif reconnu. Même si IFRS 9 exclut en principe les éléments intragroupe en consolidation, le paragraphe 6.3.6 ouvre une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Dans cette situation, une couverture de juste valeur peut donc s’appliquer si le risque de change couvert peut affecter le résultat consolidé et si les critères du paragraphe 6.4.1 sont respectés.",
      "conditions_fr": [
        "La créance de dividende doit constituer un élément monétaire intragroupe libellé en devise.",
        "Les écarts de change liés à cette créance ne doivent pas être totalement éliminés en consolidation et doivent pouvoir affecter le résultat consolidé.",
        "La relation de couverture doit être formellement désignée et documentée dès l’origine, avec relation économique, risque de crédit non dominant et ratio de couverture conforme."
      ],
      "practical_implication_fr": "C’est le modèle le plus naturel pour une créance de dividende déjà reconnue au bilan.",
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
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, l’item couvert est déjà une créance intragroupe reconnue et non une simple transaction future. Le texte permet néanmoins une couverture de flux de trésorerie pour une exposition à la variabilité des flux d’un actif ou passif reconnu, et l’exception de 6.3.6 enlève l’obstacle de consolidation pour le risque de change d’un élément monétaire intragroupe. Ce traitement n’est applicable ici que si l’entité documente bien la variabilité des flux de règlement en monnaie fonctionnelle et satisfait aux critères du paragraphe 6.4.1.",
      "conditions_fr": [
        "La créance de dividende doit être un actif monétaire intragroupe en devise dont le règlement expose le groupe à un risque de change affectant le résultat consolidé.",
        "La désignation doit viser la variabilité des flux de trésorerie attribuable au risque de change sur cette créance reconnue.",
        "La relation de couverture doit être formellement désignée et documentée dès l’origine, avec relation économique, risque de crédit non dominant et ratio de couverture conforme."
      ],
      "practical_implication_fr": "Ce modèle reste envisageable, mais sa désignation est plus exigeante qu’une couverture de juste valeur pour une créance déjà comptabilisée.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "B5.7.4",
          "excerpt": "changes in the foreign currency component of those financial instruments are presented in profit or loss"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier que le dividende déclaré a bien créé une créance/dette monétaire intragroupe en devise entre entités à monnaies fonctionnelles différentes.",
    "Démontrer en consolidation que les écarts de change sur cette créance/dette ne sont pas totalement éliminés et qu’ils peuvent affecter le résultat consolidé.",
    "Documenter à l’origine l’instrument de couverture, l’item couvert, le risque de change, la stratégie de gestion du risque et la méthode d’évaluation de l’efficacité.",
    "Pour une créance de dividende déjà reconnue, la couverture de juste valeur sera en pratique le choix le plus direct; la couverture de flux de trésorerie exige une désignation plus ciblée de la variabilité des flux de règlement."
  ]
}
