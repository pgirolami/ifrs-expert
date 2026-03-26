{
  "assumptions_fr": [
    "La question vise les états financiers consolidés.",
    "Le dividende intragroupe a donné lieu à la comptabilisation d’une créance intragroupe correspondante.",
    "Le risque visé est un risque de change lié à des monnaies fonctionnelles différentes au sein du groupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous condition que la documentation vise la créance monétaire intragroupe reconnue et son risque de change. Dans cette situation, l’approche cohérente est la couverture de juste valeur, pas la couverture de flux de trésorerie du dividende intragroupe."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la possibilité existe si l’élément couvert est la créance sur dividende déjà comptabilisée, donc un élément monétaire intragroupe reconnu. En consolidation, IFRS 9 permet de couvrir le risque de change d’un tel élément lorsqu’il génère des écarts de change non totalement éliminés entre entités de monnaies fonctionnelles différentes. La lecture la plus cohérente est alors une couverture de juste valeur du risque de change de la créance.",
      "conditions_fr": [
        "La documentation doit viser la créance monétaire intragroupe reconnue, et non le dividende comme transaction future."
      ],
      "practical_implication_fr": "Documenter l’élément couvert comme la créance intragroupe reconnue en devise, avec la composante change identifiée.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
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
      "applicability": "non",
      "reasoning_fr": "Cette approche n’est pas adaptée ici, car le fait déterminant est qu’une créance correspondant au dividende a déjà été reconnue. L’exposition à documenter n’est donc plus un dividende intragroupe futur, mais un élément monétaire intragroupe existant. En consolidation, l’exception relative aux transactions intragroupe futures ne correspond pas à ce cas.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter la relation comme une couverture de transaction intragroupe future si la créance est déjà constatée.",
      "references": [
        {
          "section": "B6.3.5",
          "excerpt": "If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify as a hedged item."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Mettre en place la documentation à l’inception de la relation de couverture; elle ne couvre pas rétroactivement les écarts de change déjà enregistrés.",
    "Décrire l’élément couvert comme la créance de dividende intragroupe reconnue, avec la devise et les monnaies fonctionnelles concernées.",
    "Éviter une documentation en cash flow hedge du dividende si l’événement générateur est déjà passé et la créance déjà comptabilisée."
  ]
}
