{
  "assumptions_fr": [
    "On suppose que la créance de dividendes intragroupe est un poste monétaire reconnu entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "On suppose que les écarts de change correspondants ne sont pas totalement éliminés en consolidation et affectent donc le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Dans ce cas précis, l’exception d’IFRS 9 pour le risque de change d’un poste monétaire intragroupe en consolidation permet de documenter la créance comme élément couvert malgré la règle générale applicable aux éléments intragroupe. La voie la plus directe est la couverture de juste valeur; une couverture de flux de trésorerie peut aussi être envisagée si la documentation vise bien la variabilité des flux d’encaissement."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change de la créance",
      "applicability": "oui",
      "reasoning_fr": "La créance de dividende intragroupe est déjà un actif monétaire reconnu dans les états financiers consolidés. Sous les hypothèses retenues, son risque de change n’est pas totalement éliminé en consolidation et affecte le résultat consolidé; l’exception d’IFRS 9 6.3.6 permet donc sa désignation malgré la règle générale de 6.3.5. Comme l’exposition porte sur un actif reconnu exposé à des variations de valeur liées au change, la couverture de juste valeur répond directement au stade actuel, sous réserve des critères de documentation et d’efficacité de 6.4.1.",
      "conditions_fr": [
        "La relation de couverture est formellement désignée et documentée dès son inception.",
        "La documentation identifie la créance, le risque de change couvert, l’instrument de couverture et la méthode d’évaluation de l’efficacité.",
        "La relation respecte les critères d’efficacité d’IFRS 9 6.4.1, y compris la relation économique et un hedge ratio approprié."
      ],
      "practical_implication_fr": "Vous pouvez documenter dès maintenant la créance consolidée comme élément couvert du risque de change et organiser les tests d’efficacité sur cette base.",
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
      "label_fr": "Couverture de flux de trésorerie du risque de change à l’encaissement",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La même créance reconnue peut aussi être analysée sous l’angle de la variabilité des flux d’encaissement en monnaie de consolidation due au change. Sous les hypothèses données, l’exception de 6.3.6 rend le poste intragroupe éligible en consolidation, et 6.5.2(b) admet une couverture de flux de trésorerie sur un actif reconnu. Cette approche n’est applicable ici que si la documentation vise explicitement cette variabilité de flux au stade actuel de la créance déjà reconnue, sans reformuler le cas en transaction future, et si 6.4.1 est respecté.",
      "conditions_fr": [
        "La documentation identifie le risque couvert comme la variabilité de change des flux d’encaissement de la créance reconnue.",
        "La relation de couverture est formellement désignée et documentée dès son inception.",
        "La relation respecte les critères d’efficacité d’IFRS 9 6.4.1."
      ],
      "practical_implication_fr": "Il faut construire la documentation autour du flux d’encaissement en devise de la créance reconnue et de sa variabilité de change jusqu’au règlement.",
      "references": [
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
    "Au stade actuel, l’analyse porte sur une créance déjà reconnue en consolidation; il ne faut pas requalifier le cas en transaction intragroupe future.",
    "L’éligibilité repose sur l’exception visant le risque de change d’un poste monétaire intragroupe non totalement éliminé en consolidation, et non sur une ouverture générale à tous les postes intragroupe.",
    "La documentation initiale doit identifier l’instrument de couverture, la créance couverte, le risque de change visé, le hedge ratio et la méthode d’évaluation de l’efficacité.",
    "Le choix entre juste valeur et flux de trésorerie doit suivre la manière exacte dont l’exposition de change de la créance est gérée et documentée."
  ]
}
