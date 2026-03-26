{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà été comptabilisé comme une créance ou une dette monétaire en devise, et ne constitue plus une transaction future.",
    "La créance ou la dette existe entre des entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change ne sont pas totalement éliminés en consolidation."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "En consolidation, la règle générale exclut les éléments intragroupe, mais IFRS 9 prévoit une exception pour le risque de change d'un élément monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés. Un dividende intragroupe déjà comptabilisé en créance à recevoir peut donc être couvert, sous réserve de la désignation, de la documentation et de l'efficacité exigées par IFRS 9."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende intragroupe a déjà été comptabilisé en créance à recevoir, donc il s'agit d'un actif reconnu. En consolidation, IFRS 9 exclut en principe les éléments intragroupe, mais admet une exception pour le risque de change d'un élément monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Une couverture de juste valeur peut donc s'appliquer ici si la relation est formellement désignée et satisfait aux critères d'efficacité.",
      "conditions_fr": [
        "Le dividende est déjà comptabilisé en créance ou dette monétaire intragroupe.",
        "Les écarts de change sur cet élément monétaire ne sont pas totalement éliminés en consolidation.",
        "La relation de couverture respecte la désignation, la documentation et les tests d'efficacité d'IFRS 9."
      ],
      "practical_implication_fr": "Documenter dès l'origine la créance couverte, le risque de change visé et le hedge ratio retenu.",
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
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Les mêmes faits font entrer la créance de dividende dans l'exception visant les éléments monétaires intragroupe en devises. IFRS 9 prévoit aussi le modèle de cash flow hedge pour un risque particulier associé à un actif comptabilisé ; il peut donc être utilisé dans ce cas si l'entité le désigne ainsi et respecte la documentation et l'efficacité requises. L'applicabilité dépend donc de la désignation effectivement retenue pour cette créance.",
      "conditions_fr": [
        "Le dividende est déjà comptabilisé en créance ou dette monétaire intragroupe.",
        "Le risque de change sur cet élément monétaire affecte le résultat consolidé car il n'est pas totalement éliminé.",
        "La relation de couverture est formellement désignée en cash flow hedge et satisfait aux critères d'IFRS 9."
      ],
      "practical_implication_fr": "La documentation doit viser la variabilité en devise des flux de règlement de la créance et la méthode de test d'efficacité.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point de bascule est la comptabilisation du dividende en créance ou dette : l'analyse porte alors sur un élément monétaire intragroupe reconnu.",
    "En consolidation, il faut pouvoir démontrer que les écarts de change sur cette créance ou dette entre entités à monnaies fonctionnelles différentes ne sont pas totalement éliminés.",
    "Quelle que soit l'approche retenue, la documentation initiale doit identifier l'instrument de couverture, l'élément couvert, le risque de change et le hedge ratio."
  ]
}
