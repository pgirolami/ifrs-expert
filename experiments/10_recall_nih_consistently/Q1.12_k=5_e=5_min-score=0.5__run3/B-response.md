{
  "assumptions_fr": [
    "La créance et la dette de dividende intragroupe créent une exposition de change entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "L’analyse vise la qualification en comptabilité de couverture dans les états financiers consolidés selon IFRS 9."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais par la voie d’une couverture de juste valeur, pas d’une couverture de flux de trésorerie. Cela suppose que la créance de dividende soit un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe a déjà été comptabilisé en créance à recevoir : on est donc face à un actif reconnu, et non à une transaction future seulement anticipée. Au niveau consolidé, IFRS 9 prévoit une exception permettant de désigner le risque de change d’un élément monétaire intragroupe comme élément couvert si ce risque génère des écarts de change non totalement éliminés en consolidation, ce qui correspond à la situation visée sous les hypothèses retenues.",
      "conditions_fr": [
        "La créance de dividende doit constituer un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation de couverture doit viser la créance de dividende comptabilisée et le risque de change affectant le résultat consolidé.",
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
          "section": "6.5.2",
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
      "applicability": "non",
      "reasoning_fr": "Cette approche vise la variabilité de flux de trésorerie d’un élément reconnu ou d’une transaction future hautement probable. Or, dans cette situation, le dividende intragroupe a déjà donné lieu à une créance à recevoir comptabilisée ; le sujet est donc la réévaluation de change d’un poste monétaire reconnu, non une transaction intragroupe future à couvrir.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette voie ne permet pas, dans ce cas, de qualifier formellement la couverture au niveau consolidé.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "B6.3.5",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in a cash flow hedge"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Au niveau consolidé, il faut d’abord qualifier la créance de dividende comme élément monétaire intragroupe exposé au change entre monnaies fonctionnelles différentes.",
    "La piste pertinente est la couverture de juste valeur du risque de change sur la créance déjà comptabilisée.",
    "La couverture de flux de trésorerie ne convient pas une fois le dividende constaté en créance ; elle vise plutôt une transaction intragroupe future hautement probable.",
    "La désignation et la documentation formelles doivent être établies dès l’origine de la relation de couverture."
  ]
}
