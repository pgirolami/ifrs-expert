{
  "assumptions_fr": [
    "L’analyse est faite au niveau des états financiers consolidés.",
    "La créance de dividende intragroupe est un poste monétaire comptabilisé, libellé dans une devise qui génère des écarts de change non totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, un élément intragroupe est en principe exclu, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsqu’il crée des écarts non totalement éliminés. Une couverture peut donc être documentée, sous réserve des critères formels de désignation, documentation et efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende est un actif comptabilisé et, sous l’hypothèse retenue, son risque de change relève de l’exception IFRS 9 applicable aux postes monétaires intragroupe en consolidation.\nLa couverture de juste valeur est adaptée si l’exposition documentée est la variation de valeur de cette créance due au change, avec incidence sur le résultat consolidé.",
      "conditions_fr": [
        "Démontrer que les écarts de change sur la créance intragroupe ne sont pas totalement éliminés en consolidation.",
        "Désigner et documenter formellement dès l’inception l’instrument de couverture, la créance couverte, le risque de change et le hedge ratio.",
        "Montrer l’existence d’une relation économique et que le risque de crédit ne domine pas les variations de valeur."
      ],
      "practical_implication_fr": "Le dossier de couverture doit viser la créance déjà comptabilisée et expliquer pourquoi le risque couvert est une variation de valeur liée au change.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "as an exception to paragraph 6.3.5, the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
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
      "reasoning_fr": "Dans cette même situation, l’exception relative au poste monétaire intragroupe permet aussi d’envisager une désignation en couverture si le risque de change affecte le résultat consolidé.\nCette voie n’est pertinente que si la relation documentée vise la variabilité des flux de règlement de la créance de dividende, exprimés dans la monnaie de consolidation, et non seulement sa variation de valeur.",
      "conditions_fr": [
        "Démontrer que la créance intragroupe entre bien dans l’exception IFRS 9 pour le risque de change des postes monétaires intragroupe.",
        "Formuler le risque couvert comme une variabilité de flux de trésorerie attribuable au change pouvant affecter le résultat consolidé.",
        "Respecter dès l’inception les exigences de documentation, de relation économique, de non-domination du risque de crédit et de hedge ratio."
      ],
      "practical_implication_fr": "La documentation doit expliquer pourquoi, pour cette créance de dividende reconnue, l’objectif est de couvrir des flux variables de change jusqu’au règlement.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
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
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La désignation et la documentation doivent exister dès l’inception de la relation de couverture ; une formalisation a posteriori ne suffit pas.",
    "Le point clé, en consolidation, est de prouver que la créance de dividende intragroupe génère bien des écarts de change non totalement éliminés.",
    "Le choix entre juste valeur et flux de trésorerie doit suivre l’objectif réel de gestion du risque et la manière dont l’exposition affecte le résultat consolidé."
  ]
}
