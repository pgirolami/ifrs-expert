{
  "assumptions_fr": [
    "La créance de dividende intragroupe est un élément monétaire intragroupe comptabilisé dans les comptes consolidés.",
    "Cette créance expose le groupe à des écarts de change parce que les entités concernées ont des monnaies fonctionnelles différentes.",
    "Cette exposition de change n’est pas totalement éliminée en consolidation et est donc analysée au regard de la comptabilité de couverture d’IFRS 9."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Sous les hypothèses retenues, IFRS 9 6.3.6 permet de désigner le risque de change d’un élément monétaire intragroupe dans les comptes consolidés lorsqu’il génère des écarts non totalement éliminés. La composante de risque de change de cette créance peut donc être intégrée dans une relation de couverture formellement documentée."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "Dans cette situation, la créance de dividende est un actif comptabilisé, mais intragroupe. La règle générale de 6.3.5 écarte l’intragroupe en consolidation, puis 6.3.6 crée précisément une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts ne sont pas totalement éliminés; cela correspond aux hypothèses retenues. Le modèle de couverture de juste valeur vise justement un actif comptabilisé exposé à un risque particulier affectant le résultat.",
      "conditions_fr": [],
      "practical_implication_fr": "La documentation doit viser la variation de valeur de la créance attribuable au risque de change couvert.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
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
      "applicability": "oui",
      "reasoning_fr": "Dans cette situation, la créance de dividende donne aussi lieu à un encaissement futur dont la contre-valeur en monnaie fonctionnelle varie avec le change. IFRS 9 6.5.2(b) vise la variabilité des flux de trésorerie d’un actif comptabilisé, et 6.3.6 lève ici l’obstacle intragroupe en consolidation puisque l’élément monétaire crée des écarts de change non totalement éliminés. La composante de risque de change peut donc aussi être documentée dans ce modèle.",
      "conditions_fr": [],
      "practical_implication_fr": "La documentation doit viser la variabilité du montant encaissé en monnaie fonctionnelle lors du règlement de la créance.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter la relation dès l’origine avec l’identification de l’instrument de couverture, de la créance de dividende, du risque de change couvert et du mode d’évaluation de l’efficacité.",
    "Conserver l’analyse montrant que l’écart de change sur la créance n’est pas totalement éliminé en consolidation; c’est le point d’ancrage de l’exception IFRS 9 6.3.6.",
    "Le choix entre couverture de juste valeur et couverture de flux de trésorerie doit être cohérent avec l’exposition effectivement documentée pour cette créance."
  ]
}
