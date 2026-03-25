{
  "assumptions_fr": [
    "La créance de dividendes intragroupe est un poste monétaire reconnu, libellé dans une devise différente de la monnaie fonctionnelle d’au moins une entité du groupe.",
    "L’exposition de change mentionnée dans les comptes consolidés signifie que les écarts de change liés à cette créance ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. IFRS 9 prévoit une exception permettant de désigner le risque de change d’un poste monétaire intragroupe comme élément couvert en consolidation lorsque ce risque n’est pas totalement éliminé et affecte le résultat consolidé, ce qui correspond aux hypothèses retenues. La relation doit encore satisfaire aux exigences de désignation, de documentation et d’efficacité d’IFRS 9."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans le contexte fourni, la créance de dividendes est déjà reconnue et constitue, selon les hypothèses, un poste monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation. IFRS 9 6.3.6 permet alors que ce risque de change soit désigné comme élément couvert, et IFRS 9 6.5.2(a) vise précisément la couverture de juste valeur d’un actif reconnu. L’application dans ce cas reste subordonnée aux conditions de désignation, documentation et efficacité d’IFRS 9 6.4.1.",
      "conditions_fr": [
        "désignation formelle et documentation de la relation de couverture à son origine",
        "instrument de couverture éligible et relation économique avec la créance de dividendes",
        "le risque de crédit ne doit pas dominer les variations de valeur",
        "ratio de couverture cohérent avec la gestion effective du risque"
      ],
      "practical_implication_fr": "Le groupe peut documenter un fair value hedge sur la créance et devra suivre l’inefficacité de couverture en résultat.",
      "references": [
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
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le fait pattern décrit une créance intragroupe déjà reconnue ; IFRS 9 6.5.2(b) admet aussi une couverture de flux de trésorerie pour la variabilité de flux d’un actif reconnu attribuable à un risque particulier. Compte tenu des hypothèses selon lesquelles la créance est un poste monétaire et que le risque de change affecte le résultat consolidé, l’exception d’IFRS 9 6.3.6 permet en principe sa désignation dans ce modèle également. Il faut toutefois que la relation de couverture soit formellement documentée et satisfasse aux tests d’efficacité d’IFRS 9 6.4.1.",
      "conditions_fr": [
        "désignation formelle et documentation de la relation de couverture à son origine",
        "instrument de couverture éligible et relation économique avec la variabilité de change des flux de règlement",
        "le risque de crédit ne doit pas dominer les variations de valeur",
        "ratio de couverture cohérent avec la gestion effective du risque"
      ],
      "practical_implication_fr": "Le groupe devra documenter un cash flow hedge et suivre la part efficace en capitaux propres puis son recyclage selon la mécanique IFRS 9.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point clé de timing est que la créance de dividendes est déjà reconnue : l’analyse porte donc sur un poste monétaire existant en consolidation, non sur une transaction future.",
    "L’éligibilité provient de l’exception d’IFRS 9 pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé.",
    "Quel que soit le modèle retenu, la mise en œuvre exige une documentation initiale robuste, un instrument éligible et un suivi continu de l’efficacité et du ratio de couverture."
  ]
}
