{
  "assumptions_fr": [
    "La créance de dividendes intragroupe est supposée être un poste monétaire libellé en devise.",
    "Les écarts de change correspondants sont supposés ne pas être entièrement éliminés en consolidation et affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, un élément intragroupe est en principe exclu comme élément couvert, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsqu’il n’est pas totalement éliminé et affecte le résultat consolidé. Une documentation de hedge accounting est donc possible, sous réserve des critères de désignation, de documentation et d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, la créance de dividendes est un actif reconnu dans les comptes consolidés. Sous les hypothèses retenues, son risque de change relève de l’exception applicable aux postes monétaires intragroupe et peut être désigné en couverture de juste valeur si ce risque affecte le résultat consolidé et si la relation remplit les critères IFRS 9.",
      "conditions_fr": [
        "La créance doit constituer un poste monétaire intragroupe exposé à un risque de change non entièrement éliminé en consolidation.",
        "Le risque couvert doit pouvoir affecter le résultat consolidé.",
        "La relation de couverture doit être formellement désignée et documentée dès l’origine, avec instrument, élément couvert, risque, hedge ratio et test d’efficacité."
      ],
      "practical_implication_fr": "Ce traitement permet de documenter la couverture du risque de change sur une créance déjà comptabilisée en consolidation.",
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
      "reasoning_fr": "Dans cette situation, la créance reconnue donne lieu à un encaissement futur dont la contre-valeur varie avec le change. Le texte fourni admet une cash flow hedge sur un actif reconnu et l’exception sur les postes monétaires intragroupe permet la désignation en consolidation, à condition que les écarts de change affectent le résultat consolidé et que la documentation IFRS 9 soit complète.",
      "conditions_fr": [
        "L’exposition doit être documentée comme une variabilité de flux liée au risque de change sur la créance reconnue.",
        "Les écarts de change doivent affecter le résultat consolidé et ne pas être entièrement éliminés en consolidation.",
        "Les exigences de désignation, de documentation et d’efficacité de la relation doivent être satisfaites."
      ],
      "practical_implication_fr": "Ce traitement est possible si l’entité formalise la couverture comme une variabilité de flux futurs de règlement due au change.",
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
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier avant la désignation que la créance de dividendes crée bien un écart de change non totalement éliminé au niveau consolidé.",
    "Choisir un seul modèle de hedge accounting cohérent avec le risque documenté : juste valeur ou flux de trésorerie.",
    "Constituer dès l’inception une documentation formelle couvrant l’instrument de couverture, l’élément couvert, le risque de change, le hedge ratio et l’évaluation de l’efficacité."
  ]
}
