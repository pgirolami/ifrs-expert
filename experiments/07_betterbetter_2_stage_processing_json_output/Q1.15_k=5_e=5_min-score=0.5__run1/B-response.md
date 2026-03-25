{
  "assumptions_fr": [
    "La créance de dividende reconnue est un poste monétaire intragroupe libellé en devise.",
    "Les écarts de change correspondants affectent le résultat consolidé parce qu’ils ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Sous les hypothèses données, IFRS 9 6.3.6 permet qu’un poste monétaire intragroupe en devise soit désigné comme élément couvert en comptes consolidés lorsque son risque de change affecte le résultat consolidé. Cette désignation peut être structurée en couverture de juste valeur ou en couverture de flux de trésorerie, avec respect des critères de 6.4.1."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Ici, la créance de dividende intragroupe est déjà reconnue en consolidé et, selon les hypothèses, constitue un poste monétaire intragroupe en devise dont les écarts de change affectent le résultat consolidé. L’exception d’IFRS 9 pour ce type de poste permet sa désignation comme élément couvert en consolidé, et un actif reconnu peut être couvert en juste valeur au titre d’un risque particulier. La relation doit ensuite être formellement documentée et satisfaire aux tests d’efficacité d’IFRS 9 6.4.1.",
      "conditions_fr": [
        "Documenter dès l’origine de la relation l’élément couvert, le risque de change couvert, l’instrument de couverture et le ratio de couverture.",
        "Démontrer une relation économique entre l’élément couvert et l’instrument de couverture, sans domination du risque de crédit."
      ],
      "practical_implication_fr": "L’entité peut mettre en place une couverture de juste valeur du risque de change de la créance intragroupe en consolidé, avec suivi de l’inefficacité et de la documentation IFRS 9.",
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
      "applicability": "oui",
      "reasoning_fr": "Dans les faits décrits, la créance intragroupe est déjà reconnue et l’exposition de change associée affecte, selon les hypothèses, le résultat consolidé. IFRS 9 autorise aussi une couverture de flux de trésorerie sur un actif reconnu pour la variabilité de flux attribuable à un risque particulier, et l’exception de 6.3.6 permet qu’un poste monétaire intragroupe soit l’élément couvert en consolidé. La mise en œuvre reste soumise à la désignation formelle et aux critères d’efficacité de 6.4.1.",
      "conditions_fr": [
        "Documenter dès l’origine de la relation la variabilité de flux en monnaie fonctionnelle couverte et le ratio de couverture retenu.",
        "Utiliser un instrument de couverture éligible et démontrer que la relation remplit les critères d’efficacité d’IFRS 9."
      ],
      "practical_implication_fr": "L’entité peut traiter l’exposition de change de la créance comme une couverture de flux de trésorerie, sous réserve d’une documentation et d’un suivi d’efficacité adaptés.",
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
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La désignation doit intervenir à l’origine de la relation de couverture, même si la créance est déjà comptabilisée au moment où la relation est mise en place.",
    "En consolidé, il faut conserver la démonstration que les écarts de change sur la créance intragroupe ne sont pas totalement éliminés et affectent bien le résultat consolidé.",
    "Le choix entre couverture de juste valeur et couverture de flux de trésorerie détermine la mécanique comptable des variations de change et le suivi de l’inefficacité."
  ]
}
