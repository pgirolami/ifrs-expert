{
  "assumptions_fr": [
    "La question vise une exposition de change identifiée au niveau des comptes consolidés sur une créance de dividendes intragroupe déjà comptabilisée.",
    "L’analyse est limitée aux dispositions d’IFRS 9 section 6 et d’IFRIC 16 fournies dans le contexte."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Au niveau consolidé, la seule voie pertinente ici est l’exception IFRS 9 relative au risque de change d’un élément monétaire intragroupe. Donc l’exposition n’est éligible que si la créance sur dividendes génère des écarts de change non totalement éliminés en consolidation."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture du risque de change d’un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La créance sur dividendes intragroupe, telle que décrite, relève de la logique d’un élément monétaire intragroupe déjà comptabilisé. En consolidation, IFRS 9 pose une interdiction générale pour les éléments intragroupe, mais prévoit une exception précise pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés.",
      "conditions_fr": [
        "la créance sur dividendes constitue bien un élément monétaire intragroupe",
        "les gains ou pertes de change correspondants ne sont pas totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "La documentation de couverture doit qualifier l’objet couvert comme exposition de change sur élément monétaire intragroupe et démontrer le caractère résiduel des écarts de change en consolidation.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "forecast_intragroup_hedge",
      "label_fr": "Couverture de flux de trésorerie d’une transaction intragroupe future",
      "applicability": "non",
      "reasoning_fr": "La situation décrite ne porte pas sur une transaction intragroupe future hautement probable, mais sur une créance sur dividendes déjà comptabilisée. Le régime IFRS 9 applicable aux transactions intragroupe futures vise des flux futurs dont le risque de change affectera le résultat consolidé, ce qui n’est pas le fait visé ici.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette approche ne constitue pas la base technique appropriée pour couvrir une créance de dividendes déjà enregistrée.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "B6.3.5",
          "excerpt": "If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify as a hedged item"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net dans une activité à l’étranger",
      "applicability": "non",
      "reasoning_fr": "L’exposition mentionnée provient d’une créance de dividendes intragroupe et non d’un montant de net assets d’une activité étrangère. IFRIC 16 encadre la couverture d’investissement net autour du risque de change sur l’investissement net lui-même; ce n’est pas le modèle décrit par la question.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas assimiler la créance de dividendes à l’objet couvert d’une couverture d’investissement net.",
      "references": [
        {
          "section": "2",
          "excerpt": "the foreign currency risk arising from the net investment in a foreign operation may be an amount of net assets"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier dès l’origine si la créance sur dividendes produit, en consolidation, des écarts de change non totalement éliminés; c’est le point décisif.",
    "Si l’exposition n’est qu’un effet intragroupe entièrement éliminé, la réponse pratique est non au niveau consolidé.",
    "Ne pas documenter cette situation comme transaction intragroupe future ni comme couverture d’investissement net si l’objet couvert est uniquement la créance sur dividendes comptabilisée."
  ]
}
