{
  "assumptions_fr": [
    "Le dividende intragroupe décidé fait naître une créance intragroupe monétaire comptabilisée.",
    "Cette créance est libellée dans une monnaie différente de la monnaie fonctionnelle de l’entité du groupe concernée.",
    "L’analyse est limitée aux comptes consolidés et suppose que les écarts de change liés à cette créance ne sont pas totalement éliminés en consolidation et peuvent affecter le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en consolidation, l’exception d’IFRS 9 pour le risque de change d’un élément monétaire intragroupe permet en principe d’inclure cette créance, ou sa composante de change, dans une relation de couverture.\nCela reste subordonné à une désignation/documentation formelle et au respect des critères d’efficacité de la relation."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "En principe, les éléments intragroupe ne sont pas éligibles en consolidation, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe.\nIci, la créance de dividende est une créance comptabilisée et monétaire ; sous l’hypothèse que son risque de change n’est pas totalement éliminé et affecte le résultat consolidé, elle peut être désignée comme élément couvert.\nLe modèle de juste valeur est cohérent car il vise un actif comptabilisé exposé à une variation de valeur attribuable au risque de change, à condition que la relation soit documentée et efficace.",
      "conditions_fr": [
        "La créance doit constituer un élément monétaire intragroupe.",
        "Le risque de change doit générer des gains ou pertes non totalement éliminés en consolidation.",
        "La composante de change doit être séparément identifiable et mesurable de façon fiable.",
        "La relation doit être formellement désignée et documentée dès son inception.",
        "Les critères d’efficacité d’IFRS 9 doivent être respectés."
      ],
      "practical_implication_fr": "La documentation devra viser la créance comptabilisée, le risque de change couvert, l’instrument de couverture et le hedge ratio retenu.",
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
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk"
        },
        {
          "section": "B6.3.8",
          "excerpt": "a risk component must be a separately identifiable component ... and ... reliably measurable"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception ... there is formal designation and documentation of the hedging relationship"
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
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La même exception d’IFRS 9 rend éligible en consolidation le risque de change d’une créance intragroupe monétaire lorsque ce risque affecte le résultat consolidé.\nDans cette situation, la créance comptabilisée peut aussi être analysée sous l’angle de la variabilité des flux de trésorerie en monnaie fonctionnelle liés au règlement futur du dividende.\nCette voie n’est possible que si la relation est documentée dès l’origine et si l’entité démontre l’éligibilité, l’identification du risque couvert et l’efficacité de la couverture.",
      "conditions_fr": [
        "La créance doit être un actif comptabilisé exposé à un risque de change pertinent en consolidation.",
        "Les effets de change doivent pouvoir affecter le résultat consolidé.",
        "La composante de change couverte doit être séparément identifiable et mesurable de façon fiable.",
        "La relation de couverture doit être formellement désignée et documentée.",
        "Les exigences d’efficacité et de hedge ratio d’IFRS 9 doivent être respectées."
      ],
      "practical_implication_fr": "Si ce modèle est retenu, il faut démontrer que la variabilité des flux de règlement de la créance, attribuable au change, est bien l’exposition gérée.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk"
        },
        {
          "section": "B6.3.8",
          "excerpt": "a risk component must be a separately identifiable component ... and ... reliably measurable"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is an economic relationship between the hedged item and the hedging instrument"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La règle générale d’exclusion des opérations intragroupe en consolidation doit être neutralisée par l’exception spécifique du paragraphe 6.3.6, documentée sur les faits du dossier.",
    "La désignation et la documentation doivent être établies dès l’inception de la relation de couverture, en identifiant précisément la créance, le risque de change et l’instrument de couverture.",
    "Il faut démontrer que les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation et qu’ils affectent bien le résultat consolidé.",
    "Le choix entre juste valeur et flux de trésorerie doit être aligné sur l’objectif de gestion du risque et sur la manière dont l’exposition est suivie."
  ]
}
