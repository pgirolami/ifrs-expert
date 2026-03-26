{
  "assumptions_fr": [
    "Le dividende intragroupe a été comptabilisé en créance à recevoir et crée un risque de change dans les états financiers consolidés.",
    "La question porte sur la comptabilité de couverture selon IFRS 9 dans les états financiers consolidés."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Dans les hypothèses retenues, une créance de dividende intragroupe peut être un item couvert en consolidation si elle constitue un item monétaire dont le risque de change n’est pas totalement éliminé à la consolidation. Le modèle le plus direct est la couverture de juste valeur; la couverture d’investissement net ne s’applique pas ici."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Ici, le dividende intragroupe est déjà comptabilisé en créance à recevoir, donc en actif reconnu. IFRS 9 admet en consolidation, par exception, qu’un item monétaire intragroupe soit un item couvert lorsque ses écarts de change ne sont pas totalement éliminés. Ce modèle correspond directement à la variation de valeur de la créance attribuable au risque de change.",
      "conditions_fr": [],
      "practical_implication_fr": "Documenter la créance de dividende comme item couvert et mesurer l’inefficacité sur la variation de change de cet actif reconnu.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ce modèle peut aussi être retenu si la relation est documentée comme couverture de la variabilité du flux d’encaissement en monnaie fonctionnelle attaché à la créance de dividende. La créance reste un item monétaire intragroupe admissible en consolidation si ses écarts de change subsistent au niveau consolidé. En revanche, ce modèle n’est pertinent que si l’exposition visée est bien la variabilité des flux futurs, et non seulement la réévaluation de l’actif reconnu.",
      "conditions_fr": [
        "La documentation doit viser la variabilité du flux d’encaissement en monnaie fonctionnelle attaché à la créance."
      ],
      "practical_implication_fr": "Si ce modèle est choisi, la désignation doit porter sur le risque de change affectant le flux d’encaissement futur de la créance.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Un dividende intragroupe comptabilisé en créance à recevoir n’est pas un investissement net dans une activité étrangère, mais une créance intragroupe distincte. IFRIC 16 limite expressément ce modèle aux couvertures d’investissements nets. Ce traitement ne peut donc pas être utilisé pour la situation décrite.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter cette exposition comme couverture d’investissement net au niveau consolidé.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "2",
          "excerpt": "Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier et conserver la preuve que la créance de dividende est un item monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation.",
    "Choisir dès l’origine un seul modèle de couverture cohérent avec l’exposition suivie: juste valeur de la créance ou variabilité du flux d’encaissement.",
    "Documenter à l’inception l’item couvert, le risque de change désigné, l’instrument de couverture et la manière d’évaluer l’efficacité de la relation.",
    "Écarter le modèle de couverture d’investissement net, qui est réservé aux seules expositions sur investissements nets dans des activités étrangères."
  ]
}
