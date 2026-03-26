{
  "assumptions_fr": [
    "La question porte sur la comptabilité de couverture en comptes consolidés selon IFRS 9.",
    "Le dividende intragroupe a créé une créance monétaire libellée en devise entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation et peuvent donc affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, dans cette situation, une couverture du risque de change est recevable en comptes consolidés si la créance de dividende constitue bien un poste monétaire intragroupe dont les écarts de change affectent le résultat consolidé. IFRS 9 permet alors une documentation en couverture de juste valeur ou en couverture de flux de trésorerie, sous réserve des critères formels de désignation, de documentation et d’efficacité."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe a déjà donné lieu à une créance reconnue, donc à un actif reconnu dans le périmètre consolidé. IFRS 9 autorise une couverture de juste valeur d’un actif reconnu et prévoit expressément qu’un poste monétaire intragroupe en devise peut être un élément couvert si les écarts de change ne sont pas totalement éliminés en consolidation, ce qui correspond aux hypothèses retenues.",
      "conditions_fr": [
        "La créance de dividende est un poste monétaire libellé en devise.",
        "Les entités concernées ont des monnaies fonctionnelles différentes.",
        "Les écarts de change sur la créance affectent le résultat consolidé.",
        "La relation de couverture est désignée et documentée à l’origine et respecte les critères d’efficacité."
      ],
      "practical_implication_fr": "Le groupe peut documenter la créance de dividende reconnue comme élément couvert d’une couverture de juste valeur du risque de change.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item"
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
      "reasoning_fr": "Dans cette situation, la créance intragroupe en devise expose le groupe à une variabilité des flux en monnaie fonctionnelle jusqu’à son règlement. IFRS 9 permet une couverture de flux de trésorerie d’un actif reconnu et l’exception applicable aux postes monétaires intragroupe permet la désignation si le risque de change affecte le résultat consolidé, ce qui est supposé ici.",
      "conditions_fr": [
        "La variabilité couverte porte sur les flux en monnaie fonctionnelle liés au règlement futur de la créance en devise.",
        "Le risque de change sur le poste monétaire intragroupe affecte le résultat consolidé.",
        "L’élément couvert est mesurable de façon fiable.",
        "La relation de couverture est formellement désignée, documentée et efficace au sens d’IFRS 9."
      ],
      "practical_implication_fr": "Le groupe peut aussi documenter une couverture de flux de trésorerie du règlement futur de la créance en devise si la variabilité des flux est clairement identifiée.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item"
        },
        {
          "section": "6.3.2",
          "excerpt": "The hedged item must be reliably measurable."
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following criteria"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif, dans ce cas précis, est que la créance de dividende soit un poste monétaire intragroupe en devise dont les écarts de change ne sont pas totalement éliminés en consolidation.",
    "La documentation de couverture doit être établie dès l’origine de la relation et identifier l’instrument de couverture, l’élément couvert, le risque couvert et la manière d’apprécier l’efficacité.",
    "L’IFRIC 16 ne doit pas être transposé par analogie à ce cas, car son champ vise uniquement les couvertures d’un investissement net dans une activité à l’étranger."
  ]
}
