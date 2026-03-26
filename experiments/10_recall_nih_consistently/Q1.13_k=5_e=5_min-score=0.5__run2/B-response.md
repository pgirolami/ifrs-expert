{
  "assumptions_fr": [
    "La créance à recevoir issue du dividende décidé est un poste monétaire intragroupe libellé en devise étrangère.",
    "La question est analysée dans les comptes consolidés.",
    "La créance est déjà comptabilisée au moment où la relation de couverture serait documentée."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en consolidation, le risque de change d’une créance intragroupe peut être intégré dans une relation de couverture documentée par exception. En pratique, cela vise la désignation de la composante de risque de change d’un actif reconnu, plutôt dans une couverture de juste valeur que dans une couverture de flux de trésorerie."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, la créance de dividende est déjà reconnue et constitue, selon l’hypothèse retenue, un poste monétaire intragroupe en devise. En consolidation, IFRS 9 admet par exception le risque de change d’un tel poste si les écarts de change ne sont pas totalement éliminés ; ce schéma correspond à la couverture d’un actif reconnu pour un risque particulier affectant le résultat.",
      "conditions_fr": [
        "les écarts de change sur cette créance ne sont pas totalement éliminés en consolidation",
        "la relation documentée vise le seul risque de change attaché à la créance reconnue"
      ],
      "practical_implication_fr": "La désignation doit porter sur la créance comptabilisée et sur sa composante de risque de change au niveau consolidé.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.3.6",
          "excerpt": "not fully eliminated on consolidation"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Dans les faits décrits, le dividende a déjà été décidé et la créance a déjà été comptabilisée. Les extraits fournis rattachent la cash flow hedge à la variabilité de flux d’un élément ou à une transaction future hautement probable, y compris certains flux intragroupe futurs, mais pas à une créance intragroupe déjà reconnue comme telle.",
      "conditions_fr": [],
      "practical_implication_fr": "La documentation ne devrait pas traiter cette créance reconnue de dividende comme élément couvert dans une cash flow hedge.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.5.2",
          "excerpt": "or a highly probable forecast transaction"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "risk_component_designation",
      "label_fr": "Désignation d’une composante de risque",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 permet de désigner une composante d’un item, notamment les variations attribuables à un risque spécifique. Pour cette créance intragroupe en devise, la composante \"risque de change\" est précisément le risque visé par l’exception applicable aux postes monétaires intragroupe en consolidation ; elle peut donc être intégrée à la relation si ce risque subsiste au niveau consolidé.",
      "conditions_fr": [
        "la composante désignée est limitée au risque de change de la créance",
        "le groupe reste exposé à des gains ou pertes de change sur ce poste au niveau consolidé"
      ],
      "practical_implication_fr": "La documentation doit isoler explicitement la composante de change de la créance comme élément couvert.",
      "references": [
        {
          "section": "6.3.7",
          "excerpt": "an entity may designate only the following types of components"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "B6.3.8",
          "excerpt": "separately identifiable ... and reliably measurable"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier en consolidation que les écarts de change sur la créance de dividende ne sont pas totalement éliminés.",
    "Documenter dès l’origine l’instrument de couverture, la créance couverte, la nature du risque de change et le ratio de couverture.",
    "Pour ce fait générateur déjà comptabilisé, l’analyse pertinente est celle d’un actif reconnu et de sa composante de change, non celle d’un flux futur hautement probable."
  ]
}
