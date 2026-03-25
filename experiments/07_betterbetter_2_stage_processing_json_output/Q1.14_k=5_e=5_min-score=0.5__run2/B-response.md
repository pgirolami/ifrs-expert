{
  "assumptions_fr": [
    "Le dividende intragroupe a créé une créance/dette monétaire intragroupe reconnue et libellée en devise.",
    "Les entités concernées ont des monnaies fonctionnelles différentes, de sorte que les écarts de change correspondants ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé.",
    "Les exigences d’IFRS 9 relatives à la désignation initiale, à la documentation et à l’efficacité de la couverture peuvent être satisfaites."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. En consolidation, les éléments intragroupe sont en principe exclus, mais IFRS 9 prévoit une exception explicite pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés et affectent le résultat consolidé. Sous les hypothèses posées, cette exposition peut donc être documentée comme relation de couverture."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur de la créance monétaire intragroupe",
      "applicability": "oui",
      "reasoning_fr": "Le fait décrit est un montant à recevoir intragroupe déjà comptabilisé ; on est donc au stade d’un actif monétaire reconnu dans le périmètre consolidé. La règle générale d’exclusion des éléments intragroupe en consolidation est écartée, selon les hypothèses retenues, parce que les entités ont des monnaies fonctionnelles différentes et que les écarts de change ne sont pas totalement éliminés. Dans ce cadre, IFRS 9 permet un fair value hedge d’un actif reconnu au titre du risque de change.",
      "conditions_fr": [],
      "practical_implication_fr": "Il faut formaliser au niveau consolidé la désignation du montant à recevoir comme élément couvert, du risque de change couvert, de l’instrument de couverture et du hedge ratio.",
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
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie de la créance monétaire intragroupe",
      "applicability": "oui",
      "reasoning_fr": "Le fait décrit est le même actif monétaire intragroupe déjà reconnu ; la question se situe donc au stade d’un actif existant et non d’une transaction intragroupe future. Sous les hypothèses retenues, l’exception IFRS 9 applicable aux éléments monétaires intragroupe est satisfaite et la variabilité des flux de règlement en monnaie fonctionnelle due au change peut affecter le résultat consolidé. IFRS 9 admet alors un cash flow hedge portant sur un actif reconnu.",
      "conditions_fr": [],
      "practical_implication_fr": "La documentation devra viser la variabilité des flux de règlement de la créance due au change et prévoir son suivi d’efficacité au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of ... a recognised asset or liability ... and could affect profit or loss."
        },
        {
          "section": "6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le fondement d’éligibilité ici est l’exception d’IFRS 9 relative à l’élément monétaire intragroupe déjà comptabilisé ; ce n’est pas le régime des transactions intragroupe futures hautement probables.",
    "La désignation et la documentation doivent être établies à l’inception de la relation de couverture au niveau consolidé, avec identification de l’instrument, de l’élément couvert, du risque couvert et du hedge ratio.",
    "L’analyse repose sur l’hypothèse essentielle que les différences de change sur la créance/dette intragroupe ne sont pas totalement éliminées en consolidation parce que les entités ont des monnaies fonctionnelles différentes."
  ]
}
