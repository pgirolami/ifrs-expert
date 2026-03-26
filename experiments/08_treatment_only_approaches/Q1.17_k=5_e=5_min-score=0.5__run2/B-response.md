{
  "assumptions_fr": [
    "La question est analysée en comptes consolidés selon IFRS 9.",
    "Le dividende intragroupe comptabilisé à recevoir / à payer constitue un poste monétaire intragroupe reconnu.",
    "Les effets de change sur ce poste ne sont pas totalement éliminés en consolidation et affectent le résultat consolidé."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. Dans cette situation, l’exception IFRS 9 pour le risque de change d’un poste monétaire intragroupe en consolidation permet de désigner la seule composante de change si elle affecte le résultat consolidé. Le schéma le plus direct est la couverture de juste valeur, mais une couverture de flux de trésorerie peut aussi être retenue si l’exposition est définie comme la variabilité du règlement en monnaie fonctionnelle."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, la créance de dividende intragroupe est un actif reconnu, et l’hypothèse donnée est que son risque de change crée des écarts non totalement éliminés en consolidation. L’exception de 6.3.6 permet alors de traiter ce risque de change intragroupe comme élément couvert en comptes consolidés. Comme IFRS 9 autorise aussi la désignation d’une seule composante de risque, une couverture limitée à la composante de change est possible si la relation est formellement documentée et efficace.",
      "conditions_fr": [
        "La créance de dividende est un poste monétaire intragroupe reconnu.",
        "Le risque de change génère des gains ou pertes non totalement éliminés en consolidation.",
        "La seule composante de change est séparément identifiable et mesurable de façon fiable.",
        "La désignation, la documentation initiale et les critères d’efficacité de 6.4.1 sont respectés."
      ],
      "practical_implication_fr": "Possible de couvrir en consolidation uniquement la variation de valeur liée au change sur cette créance intragroupe.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks (risk component)"
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
      "reasoning_fr": "Dans cette situation, la même exposition peut aussi être lue comme une variabilité des flux de règlement en monnaie fonctionnelle due au change sur une créance reconnue. IFRS 9 admet une couverture de flux de trésorerie sur un actif reconnu pour un risque particulier affectant le résultat, et l’exception de 6.3.6 maintient l’éligibilité du risque de change intragroupe en consolidation. La couverture de la seule composante de change est donc envisageable si cette variabilité est bien l’exposition documentée et si les critères d’efficacité sont satisfaits.",
      "conditions_fr": [
        "L’exposition couverte est définie comme la variabilité des flux de règlement en monnaie fonctionnelle due au change.",
        "Le poste intragroupe affecte le résultat consolidé via des écarts de change non totalement éliminés.",
        "La composante de change seule est désignée comme composante de risque identifiable et mesurable.",
        "La relation respecte la documentation initiale et les tests d’efficacité de 6.4.1."
      ],
      "practical_implication_fr": "Possible si l’objectif est de couvrir la variabilité du règlement en monnaie fonctionnelle plutôt que la seule réévaluation de l’actif.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks (risk component)"
        },
        {
          "section": "6.5.2(b)",
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
    "Vérifier d’abord que le dividende à recevoir / à payer est bien un poste monétaire intragroupe dont les écarts de change ne sont pas totalement éliminés en consolidation.",
    "Documenter dès l’origine l’élément couvert, l’instrument de couverture, la seule composante de change visée et le hedge ratio retenu.",
    "En pratique, la couverture de juste valeur est le cadrage le plus direct pour une créance reconnue; la couverture de flux de trésorerie suppose de formaliser l’exposition comme une variabilité des flux de règlement.",
    "Si les critères de relation économique, de non-domination du risque de crédit et de ratio de couverture ne sont pas remplis, la désignation ne tient pas."
  ]
}
