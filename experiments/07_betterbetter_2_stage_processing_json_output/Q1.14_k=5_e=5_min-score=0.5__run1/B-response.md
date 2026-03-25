{
  "assumptions_fr": [
    "La question est appréciée au niveau des états financiers consolidés.",
    "Le dividende intragroupe a créé une créance/dette monétaire reconnue en devise entre des entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change ne sont pas totalement éliminés en consolidation.",
    "Les exigences générales de désignation, de documentation et d'efficacité prévues par IFRS 9 paragraphe 6.4.1 sont par ailleurs satisfaites."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Dans les comptes consolidés et sous les hypothèses retenues, l'exception d'IFRS 9 pour le risque de change d'un poste monétaire intragroupe rend l'exposition éligible comme élément couvert. Le poste reconnu peut alors être documenté soit en couverture de juste valeur, soit en couverture de flux de trésorerie."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du poste monétaire intragroupe",
      "applicability": "oui",
      "reasoning_fr": "Le fait générateur décrit est un dividende intragroupe déjà comptabilisé, donc un actif/passif monétaire reconnu au stade actuel. Compte tenu des hypothèses 1 et 2, IFRS 9 6.3.6 permet précisément que le risque de change d'un poste monétaire intragroupe soit un élément couvert en consolidation lorsqu'il n'est pas totalement éliminé. Comme la couverture de juste valeur vise un actif ou passif reconnu exposé à un risque particulier, cette voie est applicable ici, l'hypothèse 3 couvrant la désignation et l'efficacité.",
      "conditions_fr": [],
      "practical_implication_fr": "Il faut documenter la relation sur la créance/dette intragroupe reconnue et suivre l'inefficacité éventuelle pendant sa durée de vie.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie de l'exposition en devise",
      "applicability": "oui",
      "reasoning_fr": "Dans les faits donnés, la question porte non sur un dividende futur mais sur le règlement en devise du poste monétaire déjà reconnu. Avec les hypothèses 1 à 3, IFRS 9 6.3.6 admet cet élément couvert en consolidation et 6.5.2(b) prévoit la couverture de flux de trésorerie pour la variabilité des flux liés à un actif ou passif reconnu pouvant affecter le résultat. Cette approche reste donc applicable à ce stade de reconnaissance, sans revenir à un stade antérieur.",
      "conditions_fr": [],
      "practical_implication_fr": "La documentation doit viser les flux de règlement en devise du poste intragroupe reconnu jusqu'à son encaissement ou son paiement.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "En consolidation, la règle générale d'exclusion des éléments intragroupe est ici dépassée par l'exception relative au risque de change d'un poste monétaire intragroupe non totalement éliminé.",
    "La documentation doit être établie à l'inception de la relation de couverture et identifier l'instrument de couverture, l'élément couvert, le risque de change couvert et le ratio de couverture.",
    "Au stade décrit, la base de la couverture est le poste monétaire déjà comptabilisé; il ne faut pas documenter la relation comme si elle portait encore sur un dividende intragroupe simplement prévu."
  ]
}
