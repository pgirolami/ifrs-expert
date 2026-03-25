{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a créé une créance et une dette monétaires intragroupe reconnues entre des entités ayant des monnaies fonctionnelles différentes.",
    "Les écarts de change liés à cette créance/dette ne sont pas totalement éliminés en consolidation et affectent donc les états financiers consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Sous les hypothèses données, l’exception d’IFRS 9 pour un élément monétaire intragroupe en consolidation permet en principe de désigner le risque de change comme élément couvert. La désignation reste toutefois subordonnée au respect des critères de documentation et d’efficacité de la relation de couverture."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "En retenant les hypothèses fournies, la créance de dividende est déjà un actif monétaire intragroupe reconnu, et son risque de change n’est pas totalement éliminé en consolidation. IFRS 9 §6.3.6 permet alors qu’un tel poste soit un élément couvert dans les comptes consolidés; comme il s’agit d’un actif reconnu, ce risque peut être structuré en couverture de juste valeur au sens du §6.5.2(a). Il faut encore satisfaire, au moment de la désignation de la relation, aux exigences de documentation et d’efficacité du §6.4.1.",
      "conditions_fr": [
        "Désignation formelle et documentation de la relation de couverture à son inception.",
        "Démonstration d’une relation économique, d’un hedge ratio approprié et de l’absence de domination du risque de crédit.",
        "Identification du risque de change comme composante de risque séparément identifiable et fiable à mesurer."
      ],
      "practical_implication_fr": "Il faut monter une documentation de fair value hedge ciblant le risque de change de la créance intragroupe reconnue et en suivre l’efficacité pendant la vie du poste.",
      "references": [
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
      "label_fr": "Couverture de flux de trésorerie du risque de change",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Au même stade de reconnaissance, IFRS 9 §6.5.2(b) vise aussi la variabilité des flux de trésorerie d’un actif reconnu attribuable à un risque particulier. Si, comme posé en hypothèse, la créance monétaire intragroupe expose le groupe à un effet de change non totalement éliminé en consolidation, l’exception du §6.3.6 permet également sa désignation comme élément couvert dans une cash flow hedge. Cette voie reste conditionnée au respect des critères de désignation, de documentation et d’efficacité du §6.4.1.",
      "conditions_fr": [
        "Désignation formelle et documentation de la relation de couverture à son inception.",
        "Justification que la variabilité des flux en monnaie fonctionnelle liée au change peut affecter le résultat consolidé.",
        "Démonstration d’une relation économique, d’un hedge ratio approprié et de l’absence de domination du risque de crédit."
      ],
      "practical_implication_fr": "Il faut documenter une cash flow hedge du risque de change sur la créance reconnue et démontrer que la variabilité couverte est bien celle des flux en monnaie fonctionnelle du groupe.",
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
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Le point décisif est l’exception IFRS 9 applicable à un élément monétaire intragroupe dont le risque de change n’est pas totalement éliminé en consolidation.",
    "La question porte sur une créance déjà reconnue: l’analyse doit donc être menée au niveau d’un actif reconnu, et non d’une transaction future.",
    "Quel que soit le type de couverture retenu, la conclusion pratique dépendra de la documentation initiale et des tests d’efficacité exigés par IFRS 9 §6.4.1."
  ]
}
