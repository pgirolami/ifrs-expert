{
  "assumptions_fr": [
    "La question porte sur la comptabilité de couverture dans des comptes consolidés.",
    "L'exposition de change provient d'une créance ou d'une dette de dividende intragroupe traitée comme un élément monétaire."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "La règle générale exclut les éléments intragroupe en consolidation, mais IFRS 9 prévoit une exception pour le risque de change d'un élément monétaire intragroupe.\nDonc, oui si la créance/dette de dividende est bien monétaire et si les écarts de change ne sont pas entièrement éliminés en consolidation."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le dividende intragroupe reconnu en créance est un actif ou passif comptabilisé.\nDans cette situation, une couverture de juste valeur n'est envisageable en consolidation que via l'exception de l'article 6.3.6, c'est-à-dire si le poste est un élément monétaire intragroupe générant un risque de change non entièrement éliminé.",
      "conditions_fr": [
        "la créance ou dette de dividende constitue un élément monétaire intragroupe",
        "les écarts de change sur ce poste ne sont pas entièrement éliminés en consolidation"
      ],
      "practical_implication_fr": "Possible en consolidation, mais seulement pour le risque de change résiduel du poste intragroupe.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Le texte permet une couverture de flux de trésorerie sur un actif ou passif comptabilisé lorsqu'un risque particulier fait varier les flux pouvant affecter le résultat.\nDans ce cas, cette voie n'est ouverte en consolidation que si le dividende intragroupe reconnu relève aussi de l'exception applicable aux éléments monétaires intragroupe.",
      "conditions_fr": [
        "la créance ou dette de dividende constitue un élément monétaire intragroupe",
        "les écarts de change sur ce poste ne sont pas entièrement éliminés en consolidation"
      ],
      "practical_implication_fr": "Si ce modèle est retenu, la documentation doit viser la variabilité de change des flux du poste reconnu.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "La situation décrite porte sur une créance ou dette de dividende intragroupe, pas sur un montant de net assets d'une activité étrangère.\nIFRIC 16 limite expressément cette mécanique aux couvertures d'investissement net et interdit son extension par analogie à d'autres cas.",
      "conditions_fr": [],
      "practical_implication_fr": "Il ne faut pas documenter cette créance de dividende comme une couverture d'investissement net.",
      "references": [
        {
          "section": "8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations; it should not be applied by analogy to other types of hedge accounting."
        },
        {
          "section": "11",
          "excerpt": "the hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets of the foreign operation"
        }
      ]
    },
    {
      "id": "approach_4",
      "normalized_label": "risk_component_hedge",
      "label_fr": "Couverture d'une composante de risque",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 permet de désigner seulement une composante de risque d'un poste, si elle est séparément identifiable et mesurable de façon fiable.\nDans cette situation, la composante de change du dividende intragroupe reconnu peut être visée, mais seulement si le poste sous-jacent est lui-même admissible en consolidation au titre de l'exception des éléments monétaires intragroupe.",
      "conditions_fr": [
        "seule la composante de change du poste est désignée",
        "la composante de change est séparément identifiable et mesurable de façon fiable",
        "le poste sous-jacent remplit l'exception intragroupe de 6.3.6"
      ],
      "practical_implication_fr": "La documentation peut viser uniquement le risque de change, sans couvrir l'intégralité du poste.",
      "references": [
        {
          "section": "6.3.7",
          "excerpt": "only changes in the cash flows or fair value of an item attributable to a specific risk or risks (risk component)"
        },
        {
          "section": "B6.3.8",
          "excerpt": "a risk component must be a separately identifiable component of the financial or the non-financial item, and the changes in the cash flows or the fair value of the item attributable to changes in that risk component must be reliably measurable"
        }
      ]
    },
    {
      "id": "approach_5",
      "normalized_label": "intragroup_monetary_hedge",
      "label_fr": "Couverture d'un élément monétaire intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "C'est l'approche la plus directement alignée sur les faits décrits.\nLa règle générale exclut les postes intragroupe en consolidation, mais IFRS 9 admet expressément le risque de change d'un élément monétaire intragroupe lorsque les gains ou pertes de change ne sont pas entièrement éliminés à la consolidation.",
      "conditions_fr": [
        "la créance ou dette de dividende est un élément monétaire intragroupe",
        "le poste est entre entités ayant des monnaies fonctionnelles différentes ou dans une configuration produisant un risque de change non entièrement éliminé en consolidation"
      ],
      "practical_implication_fr": "C'est la base la plus solide pour documenter la couverture dans le cas décrit.",
      "references": [
        {
          "section": "6.3.5",
          "excerpt": "only assets, liabilities, firm commitments or highly probable forecast transactions with a party external to the reporting entity can be designated as hedged items"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item (for example, a payable/receivable between two subsidiaries) may qualify as a hedged item in the consolidated financial statements if it results in an exposure to foreign exchange rate gains or losses that are not fully eliminated on consolidation"
        }
      ]
    },
    {
      "id": "approach_6",
      "normalized_label": "forecast_intragroup_hedge",
      "label_fr": "Couverture d'une transaction intragroupe prévue",
      "applicability": "non",
      "reasoning_fr": "Cette voie vise une transaction intragroupe future hautement probable.\nIci, l'hypothèse de départ est au contraire qu'un dividende intragroupe est déjà reconnu en créance; le sujet est donc un poste monétaire comptabilisé, pas une transaction future.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas utiliser la voie de la transaction future intragroupe si le dividende est déjà comptabilisé en créance.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item in consolidated financial statements"
        },
        {
          "section": "B6.3.5",
          "excerpt": "If the foreign currency risk of a forecast intragroup transaction does not affect consolidated profit or loss, the intragroup transaction cannot qualify as a hedged item"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier d'abord que la créance ou dette de dividende est bien un élément monétaire intragroupe.",
    "Confirmer que les écarts de change sur ce poste ne sont pas entièrement éliminés en consolidation; c'est le verrou principal de l'exception.",
    "La désignation et la documentation formelles de la relation de couverture doivent exister dès l'inception de la couverture.",
    "Si seule la composante de change est couverte, la documentation doit limiter explicitement l'élément couvert à ce risque.",
    "Ne pas qualifier ce cas de couverture d'investissement net ni de transaction intragroupe future si le dividende est déjà comptabilisé."
  ]
}
