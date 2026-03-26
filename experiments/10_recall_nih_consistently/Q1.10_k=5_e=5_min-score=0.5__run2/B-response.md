{
  "assumptions_fr": [
    "La question porte sur la comptabilité de couverture selon IFRS 9 dans des états financiers consolidés.",
    "La position de dividende intragroupe crée une exposition au risque de change au sein du groupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais seulement via une couverture de juste valeur du risque de change si la créance de dividende constitue un élément monétaire intragroupe dont les écarts de change ne sont pas entièrement éliminés en consolidation. Une couverture de flux de trésorerie ne convient pas à un dividende déjà comptabilisé à recevoir."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende est déjà comptabilisé à recevoir, donc il s’agit d’un actif reconnu et non d’une transaction future.\nEn consolidation, un item intragroupe est en principe exclu, mais IFRS 9 admet une exception pour le seul risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas entièrement éliminés.",
      "conditions_fr": [
        "La créance de dividende et la dette correspondante constituent un élément monétaire intragroupe.",
        "Les écarts de change sur cet élément ne sont pas entièrement éliminés en consolidation parce que les entités concernées ont des monnaies fonctionnelles différentes."
      ],
      "practical_implication_fr": "La relation doit être documentée comme couverture du seul risque de change sur la créance reconnue, et non comme couverture d’une transaction future.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item"
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
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Dans cette situation, le dividende est déjà comptabilisé à recevoir; ce n’est plus une transaction future hautement probable.\nLe modèle de cash flow hedge et l’exception intragroupe correspondante visent des flux variables ou des transactions intragroupe prévues, pas une créance déjà constatée.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter cette relation comme cash flow hedge lorsque le dividende est déjà constaté en créance intragroupe.",
      "references": [
        {
          "section": "6.3.3",
          "excerpt": "that transaction must be highly probable"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter la relation dès l’origine en identifiant l’instrument de couverture, la créance de dividende couverte, le risque de change et le ratio de couverture.",
    "Vérifier en consolidation que les écarts de change sur la créance/dette intragroupe affectent bien le résultat consolidé et ne sont pas entièrement éliminés.",
    "Si le dividende est déjà comptabilisé à recevoir, écarter le modèle de cash flow hedge et analyser uniquement la voie de la couverture de juste valeur."
  ]
}
