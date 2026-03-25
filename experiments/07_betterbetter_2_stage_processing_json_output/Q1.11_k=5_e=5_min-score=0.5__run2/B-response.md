{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà été déclaré et a créé une créance/dette intragroupe comptabilisée.",
    "Cette créance/dette est libellée de façon à créer un risque de change entre entités du groupe ayant des monnaies fonctionnelles différentes, et les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Sous ces hypothèses, l’exception d’IFRS 9 6.3.6 permet de désigner en consolidation le risque de change d’une créance/dette monétaire intragroupe déjà comptabilisée. Le fair value hedge est la voie la plus directe; un cash flow hedge reste envisageable si la relation est documentée comme couverture des flux de règlement."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui",
      "reasoning_fr": "Le dividende intragroupe déjà déclaré a, selon les hypothèses, créé une créance/dette monétaire intragroupe déjà comptabilisée. Bien que la règle générale vise des éléments avec des tiers, IFRS 9 6.3.6 permet en consolidation de désigner le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés, ce qui est posé ici. Comme l’exposition porte sur un actif/passif déjà reconnu, le modèle de fair value hedge de 6.5.2(a) correspond directement au stade de reconnaissance décrit.",
      "conditions_fr": [],
      "practical_implication_fr": "Le groupe peut documenter la créance/dette de dividende comme élément couvert en consolidation selon un modèle de fair value hedge.",
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
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie des flux de règlement en devise",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La même créance/dette de dividende déjà comptabilisée peut aussi être analysée comme un actif/passif reconnu dont les flux de règlement en monnaie fonctionnelle varient avec le change. L’exception de 6.3.6 rend l’élément éligible en consolidation dans les hypothèses données; toutefois, cette voie n’est adaptée que si la relation est effectivement documentée comme couverture de la variabilité des flux de trésorerie au sens de 6.5.2(b), dès l’inception de la couverture. Cette condition ne modifie pas le stade de reconnaissance décrit, mais impose un cadrage documentaire précis.",
      "conditions_fr": [
        "La stratégie documentée doit viser la variabilité des flux de règlement en monnaie fonctionnelle liée au change.",
        "La désignation initiale, la documentation et les critères d’efficacité d’IFRS 9 6.4.1 doivent être satisfaits."
      ],
      "practical_implication_fr": "Si le risque géré est celui des flux de règlement en devise, le groupe peut mettre en place une documentation de cash flow hedge et suivre l’ineffectivité conformément à IFRS 9.",
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
    "En consolidation, la règle générale de 6.3.5 vise des contreparties externes, mais 6.3.6 ouvre une exception pour les éléments monétaires intragroupe exposés à des écarts de change non totalement éliminés.",
    "Le cas d’un dividende déjà déclaré relève ici d’une créance/dette intragroupe reconnue; ce n’est pas le régime des transactions intragroupe seulement prévues.",
    "La documentation doit être établie à l’inception de la relation de couverture sur la créance/dette déjà comptabilisée; pas de désignation rétroactive.",
    "Le choix entre fair value hedge et cash flow hedge doit rester cohérent avec le risque effectivement géré, le hedge ratio et l’évaluation de l’ineffectivité exigés par IFRS 9 6.4.1."
  ]
}
