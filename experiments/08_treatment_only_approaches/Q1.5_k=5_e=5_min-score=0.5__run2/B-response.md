{
  "assumptions_fr": [
    "Le dividende intragroupe a été déclaré et comptabilisé comme une créance/dette intercompagnie monétaire.",
    "Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change sur cet élément monétaire intragroupe ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "Toute relation de couverture désignée satisfait aux exigences de désignation formelle, de documentation et d’efficacité d’IFRS 9 paragraphe 6.4.1."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Dans cette situation, IFRS 9 prévoit une exception explicite permettant de désigner le risque de change d’un élément monétaire intragroupe comme élément couvert en consolidation. Sous les hypothèses posées, une relation de couverture formellement documentée est donc possible."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Ici, le dividende déclaré est déjà une créance intragroupe reconnue, donc un actif monétaire intragroupe. IFRS 9 écarte en principe les postes intragroupe en consolidation, mais prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés, ce qui est précisément supposé. Comme il s’agit d’un actif reconnu exposé à un risque de change pouvant affecter le résultat consolidé, le modèle de couverture de juste valeur est applicable dans ce cas.",
      "conditions_fr": [
        "La créance de dividende doit être un élément monétaire intragroupe reconnu.",
        "Les écarts de change doivent ne pas être totalement éliminés en consolidation et affecter le résultat consolidé.",
        "La relation doit être formellement désignée et documentée conformément à IFRS 9.6.4.1."
      ],
      "practical_implication_fr": "Le groupe peut désigner la créance intragroupe comme élément couvert pour son risque de change dans une relation de couverture de juste valeur au niveau consolidé.",
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
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui",
      "reasoning_fr": "Dans cette situation, la créance de dividende est un actif reconnu dont l’encaissement en monnaie fonctionnelle varie avec le change. IFRS 9 permet une couverture de flux de trésorerie pour la variabilité de flux liée à un risque particulier sur un actif reconnu, et l’exception d’IFRS 9.6.3.6 rend ici le poste intragroupe éligible en consolidation. Sous les hypothèses retenues, ce traitement peut donc aussi être formellement documenté.",
      "conditions_fr": [
        "La variabilité des flux en monnaie fonctionnelle doit provenir du risque de change attaché à la créance reconnue.",
        "Le risque de change du poste intragroupe doit affecter le résultat consolidé car il n’est pas totalement éliminé en consolidation.",
        "La documentation de couverture doit identifier l’instrument, l’élément couvert, le risque couvert et l’évaluation de l’efficacité."
      ],
      "practical_implication_fr": "Le groupe peut documenter le risque de change sur l’encaissement futur de la créance intragroupe comme une couverture de flux de trésorerie en consolidation.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La désignation doit intervenir à l’origine de la relation de couverture, avec une documentation formelle du risque de change couvert, de l’instrument et du test d’efficacité.",
    "Au niveau consolidé, le point décisif est de démontrer que les écarts de change sur la créance de dividende intragroupe ne sont pas totalement éliminés et affectent bien le résultat consolidé.",
    "Le choix entre couverture de juste valeur et couverture de flux de trésorerie doit rester cohérent avec la stratégie de gestion du risque du groupe telle que documentée."
  ]
}
