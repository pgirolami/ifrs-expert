{
  "assumptions_fr": [
    "La question est analysée au niveau des états financiers consolidés.",
    "La créance et la dette de dividende intragroupe sont exposées au change parce que les entités concernées ont des monnaies fonctionnelles différentes."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, une couverture de la seule composante de change est envisageable si le dividende intragroupe comptabilisé constitue un élément monétaire dont les écarts de change ne sont pas totalement éliminés en consolidation. Le modèle de couverture d’investissement net ne convient pas ici."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "risk_component_hedge",
      "label_fr": "Couverture d’une composante de risque",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, IFRS 9 permet de désigner une composante de risque plutôt que l’élément entier. La seule composante de change d’une créance de dividende intragroupe peut donc être désignée si cette créance/dette est un élément monétaire intragroupe dont les écarts de change subsistent en consolidation.",
      "conditions_fr": [
        "Les écarts de change sur la créance/dette de dividende intragroupe ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation doit viser explicitement uniquement le risque de change de la créance/dette de dividende.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le dividende déjà comptabilisé à recevoir est un actif reconnu. Si seul le risque de change de cet élément monétaire intragroupe affecte le résultat consolidé, une couverture de juste valeur de cette composante est cohérente avec les faits décrits.",
      "conditions_fr": [
        "La créance/dette de dividende intragroupe génère des écarts de change qui affectent le résultat consolidé."
      ],
      "practical_implication_fr": "Le poste couvert serait la variation de valeur attribuable au change sur la créance/dette reconnue.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 admet aussi une couverture de flux de trésorerie pour un actif ou passif reconnu. Ici, le montant en monnaie fonctionnelle de l’encaissement du dividende varie avec le change jusqu’au règlement; ce traitement n’est pertinent que si c’est bien cette variabilité qui est suivie dans les comptes consolidés.",
      "conditions_fr": [
        "L’exposition couverte est la variabilité des flux en monnaie fonctionnelle jusqu’au règlement du dividende."
      ],
      "practical_implication_fr": "Il faut rattacher la relation de couverture à la variabilité du montant encaissé en monnaie fonctionnelle, et non à une logique d’investissement net.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "non",
      "reasoning_fr": "Les faits décrivent une créance de dividende intragroupe comptabilisée, pas un montant de net assets d’une activité étrangère. IFRIC 16 réserve ce modèle aux couvertures d’investissement net et précise qu’il ne doit pas être appliqué par analogie à d’autres types de couverture.",
      "conditions_fr": [],
      "practical_implication_fr": "Ce modèle doit être écarté pour ce dividende intragroupe.",
      "references": [
        {
          "section": "8",
          "excerpt": "it should not be applied by analogy to other types of hedge accounting"
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier dès l’origine que le dividende comptabilisé crée bien un écart de change non totalement éliminé en consolidation.",
    "Documenter à l’inception la désignation de la seule composante de change, l’instrument de couverture et le ratio de couverture.",
    "Choisir entre juste valeur et flux de trésorerie selon l’exposition réellement suivie jusqu’au règlement du dividende.",
    "Si les écarts de change sont entièrement éliminés en consolidation, aucune relation de couverture ne peut être soutenue sur ce poste."
  ]
}
