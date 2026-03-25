{
  "assumptions_fr": [
    "Le dividende intragroupe à recevoir/à payer est un poste monétaire intragroupe libellé en devise et il génère des écarts de change qui ne sont pas totalement éliminés en consolidation.",
    "L'analyse est faite au niveau des états financiers consolidés du groupe."
  ],
  "recommendation": {
    "answer": "oui",
    "justification": "Oui. En consolidation, l'exception d'IFRS 9 pour le risque de change d'un poste monétaire intragroupe rend l'élément éligible si les écarts de change affectent le résultat consolidé. La seule composante de change peut ensuite être désignée comme élément couvert, en couverture de juste valeur ou de flux de trésorerie."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur de la composante de change",
      "applicability": "oui",
      "reasoning_fr": "Ici, le dividende intragroupe est déjà comptabilisé à recevoir : au stade retenu, il s'agit donc d'un actif reconnu. Sous l'hypothèse qu'il s'agit d'un poste monétaire intragroupe en devise dont les écarts de change ne sont pas totalement éliminés en consolidation, l'exception de 6.3.6 permet son éligibilité comme élément couvert. IFRS 9 autorise en outre la désignation d'une seule composante de risque, et une couverture de juste valeur vise précisément un actif reconnu ou une composante d'un tel actif qui peut affecter le résultat.",
      "conditions_fr": [],
      "practical_implication_fr": "Le groupe peut documenter une relation ciblant uniquement le risque de change du dividende intragroupe reconnu, sans couvrir les autres composantes de l'actif.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "an entity may designate only ... changes in the cash flows or fair value of an item attributable to a specific risk"
        },
        {
          "section": "6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability ... or a component"
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
      "label_fr": "Couverture de flux de trésorerie de la composante de change",
      "applicability": "oui",
      "reasoning_fr": "Le fait que le dividende intragroupe soit déjà reconnu n'empêche pas cette voie, car IFRS 9 admet aussi une couverture de flux de trésorerie sur un actif ou passif reconnu. Sous les hypothèses données, le poste monétaire intragroupe est éligible en consolidation par l'exception de 6.3.6, et 6.3.7 permet de ne désigner que le risque de change. Cette approche répond donc aussi au cas présent, dès lors que la variabilité de flux liée au change est celle que le groupe cherche à couvrir et qu'elle affecte le résultat consolidé.",
      "conditions_fr": [],
      "practical_implication_fr": "Le groupe peut structurer la couverture sur la variabilité des flux en devise du dividende intragroupe reconnu, avec la mécanique OCI/résultat propre à une couverture de flux de trésorerie.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "an entity may designate an item in its entirety or a component of an item as the hedged item"
        },
        {
          "section": "6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "En consolidation, la règle générale exclut les éléments intragroupe, mais le risque de change d'un poste monétaire intragroupe redevient éligible par l'exception de 6.3.6 si l'effet n'est pas totalement éliminé.",
    "Comme le dividende est déjà comptabilisé à recevoir, l'analyse porte bien sur un actif reconnu au stade actuel ; il n'est pas nécessaire de reformuler le cas comme une transaction future.",
    "La couverture peut viser la seule composante de change, à condition qu'elle soit séparément identifiable et fiable à mesurer dans ce contexte.",
    "Quel que soit le type de couverture retenu, la relation doit être formellement désignée et documentée à l'origine, avec identification du risque couvert, de l'instrument et du hedge ratio."
  ]
}
