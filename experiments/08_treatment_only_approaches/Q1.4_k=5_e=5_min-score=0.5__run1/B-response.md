{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a donné lieu à une créance et à une dette intragroupe comptabilisées constituant un élément monétaire.",
    "Cette créance/dette existe entre entités ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change correspondants ne sont pas totalement éliminés en consolidation.",
    "La relation de couverture serait formellement désignée et documentée à l'origine et satisferait par ailleurs aux critères d'IFRS 9."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, la règle générale d'externalité est écartée pour le risque de change d'un élément monétaire intragroupe. Ainsi, une créance de dividende intragroupe reconnue peut être documentée en couverture si les écarts de change ne sont pas totalement éliminés et si les exigences IFRS 9 sont respectées."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende déclaré a créé une créance intragroupe reconnue, donc un élément monétaire intragroupe. Sous l'hypothèse de monnaies fonctionnelles différentes, le risque de change n'est pas totalement éliminé en consolidation et peut être désigné comme élément couvert. La documentation est donc possible dans cette situation si elle est mise en place à l'origine et respecte IFRS 9.",
      "conditions_fr": [
        "La créance/dette de dividende est un élément monétaire intragroupe reconnu.",
        "Les entités concernées ont des monnaies fonctionnelles différentes.",
        "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
        "La désignation, la documentation et le test d'efficacité sont établis dès l'origine selon IFRS 9."
      ],
      "practical_implication_fr": "Ce modèle permet de documenter en consolidation la composante change de la créance de dividende reconnue, sous réserve du respect formel d'IFRS 9.",
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
      "reasoning_fr": "Dans cette situation, la créance de dividende reconnue expose le groupe à une variabilité des flux en monnaie fonctionnelle liée au change jusqu'au règlement. Le contexte fourni admet qu'un actif reconnu puisse relever d'un cash flow hedge si cette variabilité peut affecter le résultat. Ce traitement est donc envisageable en consolidation, sous réserve de démontrer cet effet et de documenter la relation conformément à IFRS 9.",
      "conditions_fr": [
        "La variabilité des flux liée au change de la créance reconnue peut affecter le résultat consolidé.",
        "L'élément couvert reste le risque de change d'un élément monétaire intragroupe non totalement éliminé en consolidation.",
        "La documentation IFRS 9 identifie clairement l'instrument de couverture, l'élément couvert, le risque couvert et l'efficacité.",
        "La relation est désignée à l'origine de la couverture."
      ],
      "practical_implication_fr": "Ce modèle est possible si l'entité peut étayer que la composante change fait varier des flux affectant le résultat consolidé.",
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
          "excerpt": "there is formal designation and documentation of the hedging relationship"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être préparée à l'origine de la relation de couverture, et non après coup.",
    "Le dossier doit montrer que la créance de dividende est bien un élément monétaire intragroupe entre entités à monnaies fonctionnelles différentes.",
    "Il faut démontrer que le risque de change n'est pas totalement éliminé en consolidation et qu'il affecte le résultat consolidé.",
    "Le choix entre couverture de juste valeur et couverture de flux de trésorerie doit rester cohérent avec le risque documenté et la manière de tester l'efficacité."
  ]
}
