{
  "assumptions_fr": [
    "La créance de dividendes intragroupe est un élément monétaire reconnu entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les gains ou pertes de change liés à cette créance ne sont pas entièrement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans cette situation, l'exposition de change peut être éligible au niveau consolidé grâce à l'exception visant les éléments monétaires intragroupe dont le risque de change n'est pas totalement éliminé. L'application suppose ensuite une désignation formelle, une documentation initiale et le respect des critères d'efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, la créance de dividendes intragroupe est un actif monétaire reconnu. Comme l'hypothèse retenue est que son risque de change subsiste en consolidation et affecte le résultat consolidé, l'exception de 6.3.6 écarte la règle générale de 6.3.5. Le risque de change distinct peut donc être désigné comme composante de risque d'un actif reconnu dans une couverture de juste valeur, sous réserve de la documentation et de l'efficacité.",
      "conditions_fr": [
        "La créance doit être un élément monétaire intragroupe dont le risque de change n'est pas entièrement éliminé en consolidation.",
        "Le risque de change désigné doit constituer une composante distincte et mesurable de la créance.",
        "La relation de couverture doit être désignée et documentée dès l'origine avec un hedge ratio cohérent et une démonstration d'efficacité."
      ],
      "practical_implication_fr": "Traitement adapté si l'objectif est de couvrir la variation de valeur de la créance due au change.",
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
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks (risk component)"
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
      "reasoning_fr": "Dans cette situation, la créance reconnue produit un encaissement fixe en devise mais variable en monnaie fonctionnelle jusqu'au règlement. Dès lors que ce risque de change sur l'élément monétaire intragroupe affecte encore le résultat consolidé, l'exception de 6.3.6 rend l'élément admissible au niveau consolidé. Le modèle de couverture de flux de trésorerie peut donc aussi être retenu pour cette variabilité, sous réserve de la documentation et de l'efficacité.",
      "conditions_fr": [
        "La variabilité visée doit être celle du montant encaissé en monnaie fonctionnelle du fait du change sur la créance intragroupe.",
        "Le risque de change désigné doit être une composante distincte et mesurable de l'actif reconnu.",
        "La relation doit être formellement désignée, documentée à l'origine et satisfaire aux critères d'efficacité d'IFRS 9."
      ],
      "practical_implication_fr": "Traitement pertinent si l'objectif est de couvrir la variabilité du montant encaissé en monnaie fonctionnelle au règlement.",
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
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks (risk component)"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier en premier lieu que la créance sur dividendes est bien un élément monétaire intragroupe et que ses écarts de change ne sont pas totalement éliminés en consolidation.",
    "Documenter dès l'origine l'instrument de couverture, l'élément couvert, le risque de change visé, la stratégie de gestion du risque et le hedge ratio.",
    "Choisir un seul modèle cohérent avec l'objectif de gestion du risque : juste valeur si l'on vise la variation de valeur de la créance, flux de trésorerie si l'on vise le montant encaissé en monnaie fonctionnelle.",
    "Limiter la désignation à l'exposition de change distincte et mesurable identifiée sur la créance."
  ]
}
