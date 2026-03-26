{
  "assumptions_fr": [
    "La question porte sur un risque de change identifié dans des états financiers consolidés.",
    "La créance sur dividendes intragroupe est traitée comme un solde monétaire intragroupe comptabilisé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais seulement via l’exception visant le risque de change d’un élément monétaire intragroupe en consolidation. Il faut que les écarts de change sur cette créance ne soient pas totalement éliminés en consolidation; les modèles de couverture de flux de trésorerie et d’investissement net ne correspondent pas aux faits décrits."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, l’exposition provient d’une créance sur dividendes déjà comptabilisée, donc d’un actif monétaire intragroupe existant. La règle générale exclut les éléments intragroupe en consolidation, mais IFRS 9 prévoit une exception pour le risque de change d’un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés en consolidation. Dans cette situation, cette voie est celle qui correspond le mieux au fait générateur décrit.",
      "conditions_fr": [
        "les écarts de change sur la créance intragroupe ne sont pas totalement éliminés en consolidation"
      ],
      "practical_implication_fr": "La désignation doit viser spécifiquement le risque de change de la créance intragroupe comptabilisée dans les comptes consolidés.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities ... with a party external to the reporting entity can be designated as hedged items"
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
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Les faits décrits concernent une créance sur dividendes déjà comptabilisée, et non une transaction intragroupe future hautement probable. Dans le contexte fourni pour la consolidation, l’exception explicitement développée pour les transactions intragroupe relevant d’une couverture de flux de trésorerie vise les opérations prévisionnelles qui affecteront le résultat consolidé. Ce n’est pas la situation décrite ici.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas analyser cette exposition comme un flux intragroupe futur à couvrir au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "B6.3.5",
          "excerpt": "If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "La question vise une créance de dividendes intragroupe identifiée séparément, pas un montant de net assets d’une activité étrangère. Le modèle de couverture d’investissement net s’applique au risque de change sur un investissement net dans une activité à l’étranger, non à un solde intragroupe de dividendes. Les faits décrits sortent donc de ce périmètre.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette exposition ne doit pas être documentée comme une couverture d’investissement net dans une activité étrangère.",
      "references": [
        {
          "section": "2",
          "excerpt": "will apply only when the net assets of that foreign operation are included in the financial statements"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier en consolidation que la créance sur dividendes intragroupe génère bien des écarts de change non totalement éliminés.",
    "Documenter dès l’origine la désignation, le risque couvert, l’instrument de couverture et le hedge ratio conformément à IFRS 9.6.4.1.",
    "Limiter l’analyse au risque de change du solde monétaire intragroupe comptabilisé, sans le requalifier en transaction future ni en investissement net."
  ]
}
