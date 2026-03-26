{
  "assumptions_fr": [
    "La question porte sur la comptabilité de couverture selon IFRS 9 dans des états financiers consolidés.",
    "La créance de dividende intragroupe comptabilisée est un poste monétaire intragroupe exposé à un risque de change."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, si la créance intragroupe est un poste monétaire dont les écarts de change ne sont pas entièrement éliminés en consolidation. Dans ce cas, la composante de risque de change peut être documentée comme élément couvert, la couverture de juste valeur étant ici la voie la plus directement cohérente; ce n'est pas une couverture d'investissement net."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "risk_component_designation",
      "label_fr": "Désignation de la composante de risque",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance de dividende intragroupe est, selon les hypothèses, un poste monétaire déjà reconnu. En consolidation, sa composante de risque de change peut être isolée comme risque couvert si ce risque produit des écarts de change non entièrement éliminés; dans cette situation, le risque de change est une composante identifiable et mesurable de la créance.",
      "conditions_fr": [
        "La créance est entre des entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change ne sont pas entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation peut viser uniquement le risque de change de la créance, sans couvrir l'intégralité du dividende intragroupe.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Cette approche correspond directement à une créance intragroupe reconnue: IFRS 9 vise un actif reconnu ou un composant de cet actif. Dans ce cas précis, une relation documentée est possible si la créance de dividende est un poste monétaire intragroupe dont le risque de change affecte le résultat consolidé parce qu'il n'est pas totalement éliminé.",
      "conditions_fr": [
        "Le risque de change sur la créance intragroupe affecte le résultat consolidé car les écarts de change ne sont pas entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation doit identifier la créance à recevoir comme élément couvert et le risque de change comme risque couvert.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Cette voie n'est envisageable que si la relation documentée vise la variabilité, en monnaie fonctionnelle, des flux de règlement futurs de la créance reconnue due au change. Dans la situation décrite, cela reste possible mais plus conditionnel, car le fait générateur principal est une créance déjà comptabilisée plutôt qu'une transaction intragroupe encore future.",
      "conditions_fr": [
        "L'objectif documenté porte sur la variabilité des flux de règlement de la créance reconnue due au risque de change.",
        "Les écarts de change liés à cette créance intragroupe ne sont pas entièrement éliminés en consolidation."
      ],
      "practical_implication_fr": "Si ce modèle est retenu, il faut documenter précisément que le risque couvert est la variabilité des flux de règlement et non une transaction future intragroupe.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'un investissement net",
      "applicability": "non",
      "reasoning_fr": "La question vise une créance de dividende intragroupe reconnue, et non un montant de net assets d'une activité étrangère. IFRIC 16 réserve ce modèle aux couvertures d'investissements nets dans des opérations étrangères et précise qu'il ne faut pas l'appliquer par analogie à d'autres couvertures.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette créance ne doit pas être documentée comme élément couvert dans une couverture d'investissement net.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency."
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être établie dès l'inception de la relation de couverture et identifier l'instrument de couverture, la créance, le risque couvert et le ratio de couverture.",
    "Le point clé à vérifier en consolidation est que les écarts de change sur la créance intragroupe ne sont pas entièrement éliminés, ce qui est typiquement le cas entre entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Pour ce fait pattern, la désignation de la composante de change dans une couverture de juste valeur est la lecture la plus directe; la couverture d'investissement net doit être écartée."
  ]
}
