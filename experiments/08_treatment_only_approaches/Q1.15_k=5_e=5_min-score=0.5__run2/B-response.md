{
  "assumptions_fr": [
    "La créance de dividende intragroupe reconnue est un élément monétaire entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change liés à cette créance ne sont pas entièrement éliminés en consolidation et peuvent donc affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. En consolidé, IFRS 9 prévoit une exception permettant de désigner le risque de change d’un élément monétaire intragroupe comme élément couvert lorsque les écarts de change ne sont pas entièrement éliminés. La relation doit aussi être formellement désignée, documentée et satisfaire aux critères d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "En consolidé, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe.\nAvec les hypothèses retenues, la créance de dividende est un actif monétaire reconnu dont les écarts de change affectent le résultat consolidé; elle peut donc être désignée en couverture de juste valeur, sous réserve de la documentation et de l’efficacité.",
      "conditions_fr": [
        "La créance de dividende est bien un élément monétaire intragroupe reconnu.",
        "Les écarts de change ne sont pas entièrement éliminés en consolidation et affectent le résultat consolidé.",
        "La relation de couverture est formellement désignée, documentée et satisfait aux critères d’efficacité."
      ],
      "practical_implication_fr": "La désignation porte sur les variations de valeur de la créance reconnue attribuables au risque de change.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items."
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
      "reasoning_fr": "La même exception d’IFRS 9 rend d’abord la créance monétaire intragroupe éligible comme élément couvert en consolidé dans cette situation.\nUne couverture de flux de trésorerie est aussi envisageable si le risque désigné est la variabilité des flux de règlement en monnaie fonctionnelle affectant le résultat consolidé, avec désignation, documentation et efficacité conformes à IFRS 9.",
      "conditions_fr": [
        "La créance de dividende reste un élément monétaire intragroupe dont le risque de change affecte le résultat consolidé.",
        "Le risque couvert est défini comme la variabilité des flux de règlement liée au change.",
        "La relation de couverture est formellement désignée, documentée et satisfait aux critères d’efficacité."
      ],
      "practical_implication_fr": "La désignation vise la variabilité, en monnaie fonctionnelle, des flux de règlement de la créance jusqu’à son encaissement.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items."
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
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter, au niveau consolidé, pourquoi les écarts de change sur cette créance intragroupe ne sont pas entièrement éliminés et affectent le résultat.",
    "Mettre en place la désignation et la documentation de couverture dès l’origine de la relation, en identifiant l’élément couvert, le risque de change, l’instrument de couverture et le ratio de couverture.",
    "Choisir le modèle de couverture cohérent avec l’objectif de gestion du risque: variations de valeur de la créance reconnue ou variabilité de ses flux de règlement."
  ]
}
