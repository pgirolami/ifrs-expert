{
  "assumptions_fr": [
    "Le dividende intragroupe comptabilisé crée une créance/dette monétaire intragroupe entre des entités ayant des monnaies fonctionnelles différentes, et les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. Sous l’hypothèse retenue, l’exception d’IFRS 9.6.3.6 permet de désigner en consolidation le risque de change d’un élément monétaire intragroupe. Une fois la créance de dividende enregistrée, elle peut être documentée en hedge accounting, en fair value hedge ou en cash flow hedge selon le modèle choisi."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui",
      "reasoning_fr": "En consolidation, la règle générale exclut les éléments intragroupe, mais IFRS 9.6.3.6 ouvre une exception explicite pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Ici, la créance de dividende est déjà comptabilisée comme actif/passif reconnu, ce qui correspond au champ du fair value hedge pour un risque particulier affectant le résultat.",
      "conditions_fr": [
        "La créance/dette de dividende est un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes",
        "Les écarts de change sur cet élément ne sont pas totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "Le groupe peut désigner formellement la créance/dette de dividende et le risque de change couvert dès la mise en place de la relation de couverture.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items."
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
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
      "reasoning_fr": "Dans cette situation, l’exposition peut aussi être analysée comme une variabilité des flux de règlement en monnaie fonctionnelle d’une créance/dette déjà reconnue. IFRS 9.6.5.2(b) vise justement la variabilité de flux associée à un actif ou passif reconnu, et l’exception de 6.3.6 permet ici de surmonter l’obstacle intragroupe en consolidation.",
      "conditions_fr": [
        "La créance/dette de dividende est un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes",
        "Les écarts de change sur cet élément affectent le résultat consolidé parce qu’ils ne sont pas totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "Le groupe peut documenter la couverture comme une couverture de la variabilité des flux de règlement liés au change sur la créance/dette de dividende.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d’abord en consolidation que les écarts de change sur la créance/dette de dividende ne sont pas entièrement éliminés ; sinon l’exception d’IFRS 9.6.3.6 ne s’applique pas.",
    "La documentation doit être établie à l’inception de la relation de couverture et identifier l’instrument de couverture, la créance/dette de dividende et le risque de change couvert.",
    "Le choix entre fair value hedge et cash flow hedge doit rester cohérent avec la manière dont le groupe gère effectivement cette exposition après comptabilisation du dividende."
  ]
}
