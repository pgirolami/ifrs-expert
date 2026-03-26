{
  "assumptions_fr": [
    "La créance de dividendes intragroupe est un élément monétaire entre entités du groupe ayant des monnaies fonctionnelles différentes ; les écarts de change correspondants ne sont donc pas totalement éliminés en consolidation.",
    "Toute relation de couverture envisagée doit satisfaire aux exigences d’IFRS 9 en matière de désignation formelle, de documentation initiale et d’efficacité."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, au niveau consolidé, le risque de change d’une créance intragroupe monétaire peut être éligible par exception. La documentation n’est conforme aux IFRS que si ce risque n’est pas totalement éliminé en consolidation et si les critères d’IFRS 9 sont respectés dès l’origine."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividendes intragroupe est un actif comptabilisé exposé au risque de change au niveau consolidé.\nIFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés en consolidation ; une couverture de juste valeur peut donc être documentée si la relation est formellement désignée et efficace.",
      "conditions_fr": [
        "Démontrer que les écarts de change sur la créance ne sont pas totalement éliminés en consolidation.",
        "Documenter dès l’origine l’élément couvert, l’instrument de couverture, le risque de change couvert et la méthode d’évaluation de l’efficacité."
      ],
      "practical_implication_fr": "La documentation devra viser la créance reconnue et organiser un suivi d’efficacité conforme à IFRS 9.",
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
      "reasoning_fr": "Dans cette situation, la créance est déjà reconnue et son équivalent en monnaie fonctionnelle varie avec le change au niveau consolidé.\nComme IFRS 9 autorise une cash flow hedge d’un risque particulier associé à un actif comptabilisé, et maintient l’exception pour un élément monétaire intragroupe en consolidation, cette documentation est aussi possible sous réserve de satisfaire aux critères IFRS 9.",
      "conditions_fr": [
        "Démontrer que la variabilité des flux en monnaie fonctionnelle liée au change est bien le risque couvert dans cette situation.",
        "Respecter dès l’inception les exigences de désignation, de documentation et d’efficacité prévues par IFRS 9."
      ],
      "practical_implication_fr": "La documentation doit expliciter que le risque couvert est la variabilité liée au change sur les flux rattachés à la créance intragroupe.",
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
    "La désignation et la documentation doivent être établies dès l’inception de la relation de couverture, pas a posteriori.",
    "L’analyse doit être menée au niveau consolidé, car l’éligibilité repose sur le fait que les écarts de change intragroupe ne soient pas totalement éliminés.",
    "Le choix entre juste valeur et flux de trésorerie doit être cohérent avec le risque effectivement documenté et avec la démonstration d’efficacité requise par IFRS 9."
  ]
}
