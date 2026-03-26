{
  "assumptions_fr": [
    "Le dividende intragroupe a été comptabilisé en créance/dette monétaire libellée en devise entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Au niveau consolidé, IFRS 9 admet par exception le risque de change d’un élément monétaire intragroupe comme élément couvert s’il affecte le résultat consolidé. Une relation de couverture est donc possible si elle est désignée et documentée dès l’origine et satisfait aux critères d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende est supposé déjà comptabilisé en créance intragroupe en devise, donc en actif reconnu. IFRS 9 permet, par exception en consolidation, de couvrir le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. Cette voie correspond directement à la couverture de juste valeur d’un actif reconnu, sous réserve de la documentation et de l’efficacité.",
      "conditions_fr": [
        "La créance ou dette de dividende est un élément monétaire intragroupe libellé en devise.",
        "Les écarts de change correspondants affectent le résultat consolidé car ils ne sont pas totalement éliminés.",
        "La relation est formellement désignée et documentée à l’origine et respecte les critères d’efficacité d’IFRS 9."
      ],
      "practical_implication_fr": "La documentation de couverture au niveau consolidé doit viser le risque de change du poste intragroupe reconnu et démontrer l’efficacité de la relation.",
      "references": [
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
      "reasoning_fr": "Dans cette situation, la créance de dividende est un actif reconnu dont la contre-valeur en monnaie fonctionnelle varie avec le cours de change jusqu’au règlement. IFRS 9 définit aussi la couverture de flux de trésorerie pour la variabilité des flux d’un actif reconnu, et l’exception relative aux éléments monétaires intragroupe en consolidation reste nécessaire. Cette qualification est donc possible si ce risque de change est précisément documenté et si les tests d’efficacité sont satisfaits.",
      "conditions_fr": [
        "La variabilité des flux liée au change sur la créance reconnue peut affecter le résultat consolidé.",
        "Le poste reste un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation.",
        "La désignation, la documentation initiale et les critères d’efficacité d’IFRS 9 sont respectés."
      ],
      "practical_implication_fr": "Si ce modèle est retenu, la documentation doit relier la variabilité de change des encaissements du dividende au résultat consolidé attendu.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the nature of the risk being hedged and how the entity will assess whether the hedging relationship meets the hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La relation de couverture doit être formellement désignée et documentée dès l’origine, au niveau des états financiers consolidés.",
    "Le point clé est de démontrer que les écarts de change sur la créance ou dette de dividende ne sont pas totalement éliminés et affectent bien le résultat consolidé.",
    "Parmi les traitements identifiés, la couverture de juste valeur correspond le plus directement à une créance intragroupe déjà reconnue."
  ]
}
