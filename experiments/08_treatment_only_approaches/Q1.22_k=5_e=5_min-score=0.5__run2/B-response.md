{
  "assumptions_fr": [
    "Le dividende intragroupe est devenu une créance/dette monétaire intragroupe reconnue entre des entités ayant des monnaies fonctionnelles différentes.",
    "Les gains ou pertes de change correspondants ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui. Dans cette situation, IFRS 9 permet en consolidation de désigner le risque de change d’un poste monétaire intragroupe reconnu lorsqu’il n’est pas totalement éliminé et affecte le résultat consolidé. Le fair value hedge est la lecture la plus directe; un cash flow hedge peut aussi être documenté si la désignation vise la variabilité des flux."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 pose en principe qu’un élément couvert doit être externe au groupe, mais le §6.3.6 crée une exception pour le risque de change d’un poste monétaire intragroupe. Avec les hypothèses données, la créance de dividende reconnue entre dans cette exception et, comme il s’agit d’un actif/passif reconnu dont la variation de change affecte le résultat consolidé, une couverture de juste valeur peut être documentée si les critères de désignation, de mesure et d’efficacité sont respectés.",
      "conditions_fr": [
        "La créance/dette de dividende est un poste monétaire intragroupe reconnu.",
        "Les écarts de change ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé.",
        "Le risque de change désigné est séparément identifiable et mesurable de façon fiable.",
        "La relation de couverture est formellement désignée et documentée dès l’origine.",
        "La relation satisfait aux exigences d’efficacité et de hedge ratio."
      ],
      "practical_implication_fr": "La couverture peut être documentée en consolidation sur la créance/dette intragroupe au titre du seul risque de change.",
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
      "reasoning_fr": "Le §6.5.2(b) permet une couverture de flux de trésorerie pour un risque particulier associé à un actif ou passif reconnu. Dans cette situation, si la documentation vise la variabilité des flux de règlement en monnaie fonctionnelle de la créance/dette intragroupe reconnue, et que le risque de change affecte le résultat consolidé au sens du §6.3.6, ce modèle est aussi permis sous réserve des mêmes exigences de documentation, de mesure et d’efficacité.",
      "conditions_fr": [
        "La désignation porte sur la variabilité des flux de règlement liée au risque de change.",
        "La créance/dette intragroupe reconnue entre dans l’exception du §6.3.6.",
        "Le risque de change peut être isolé et mesuré de façon fiable.",
        "La documentation initiale précise l’instrument, l’élément couvert, le risque et le hedge ratio.",
        "La relation présente une relation économique et le risque de crédit ne domine pas."
      ],
      "practical_implication_fr": "Le modèle cash flow hedge est envisageable si l’objet documenté est la variabilité des flux en monnaie fonctionnelle du règlement du dividende intragroupe.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with ... a recognised asset or liability"
        },
        {
          "section": "6.3.7(a)",
          "excerpt": "specific risk or risks ... separately identifiable and reliably measurable"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La preuve clé en consolidation est que l’écart de change sur la créance/dette de dividende n’est pas totalement éliminé et affecte le résultat consolidé.",
    "La documentation doit être mise en place dès l’origine de la relation de couverture avec identification explicite du risque de change couvert.",
    "Si seule la composante change est désignée, elle doit être séparément identifiable et mesurable de façon fiable.",
    "Pour une créance déjà reconnue, la couverture de juste valeur est généralement le cadrage le plus direct."
  ]
}
