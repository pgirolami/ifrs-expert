{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a déjà créé une créance et une dette intragroupe monétaires comptabilisées, libellées dans une devise générant un risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "Comme le dividende est déjà comptabilisé en créance, l'analyse porte sur la couverture d'un élément comptabilisé et non sur une transaction intragroupe future."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Sous ces hypothèses, le risque de change peut être formellement documenté en relation de couverture en consolidation grâce à l'exception visant les postes monétaires intragroupe. La couverture de juste valeur est la plus directement adaptée ici; la couverture de flux de trésorerie n'est envisageable que si la variabilité des flux de règlement est explicitement démontrée et documentée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe a déjà donné naissance à une créance monétaire comptabilisée. Sous l'hypothèse que les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé, l'exception de l'IFRS 9 permet de désigner ce risque de change intragroupe comme élément couvert en consolidation. Il faut ensuite satisfaire aux exigences formelles de désignation, de documentation et d'efficacité.",
      "conditions_fr": [
        "Les écarts de change sur la créance ou dette intragroupe affectent le résultat consolidé.",
        "La relation de couverture est désignée et documentée à l'origine.",
        "Une relation économique, un effet du risque de crédit non dominant et un hedge ratio approprié sont démontrés."
      ],
      "practical_implication_fr": "Le groupe peut documenter formellement une couverture du risque de change sur la créance de dividende déjà reconnue, si le dossier IFRS 9 est complet dès l'origine.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
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
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, l'item n'est plus une transaction future mais une créance intragroupe déjà comptabilisée. Le modèle de cash flow hedge n'est donc recevable que si l'entité documente que la variabilité des flux de règlement en devise de cette créance affecte le résultat consolidé. Le texte vise bien un actif ou passif comptabilisé, mais cette voie est moins directement alignée que la couverture de juste valeur sur les faits décrits.",
      "conditions_fr": [
        "La variabilité des flux de règlement en devise de l'actif ou passif comptabilisé est identifiée comme risque couvert.",
        "Cette variabilité affecte le résultat consolidé.",
        "La documentation initiale et les exigences d'efficacité d'IFRS 9.6.4.1 sont respectées."
      ],
      "practical_implication_fr": "Ce modèle reste possible, mais il exige de démontrer et de documenter précisément la variabilité des flux de règlement liés au dividende comptabilisé.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le dossier doit être établi à l'origine de la relation de couverture et identifier l'instrument de couverture, l'élément couvert, le risque de change couvert et le hedge ratio.",
    "Il faut conserver une démonstration que les écarts de change sur la créance ou dette intragroupe ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
    "Comme le dividende est déjà comptabilisé, l'analyse doit être menée comme couverture d'un poste monétaire intragroupe reconnu, non comme couverture d'une transaction future intragroupe.",
    "En pratique, la couverture de juste valeur est plus simple à rattacher aux faits décrits; la couverture de flux de trésorerie demande un effort probatoire supplémentaire sur la variabilité des flux de règlement."
  ]
}
