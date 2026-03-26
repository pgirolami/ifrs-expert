{
  "assumptions_fr": [
    "La créance/dette de dividende intragroupe est libellée dans une devise différente de la monnaie fonctionnelle d'au moins une entité du groupe, de sorte que des écarts de change naissent.",
    "La demande vise à identifier les modèles de comptabilité de couverture à évaluer pour l'exposition de change dans les comptes consolidés, et non à conclure qu'un modèle s'applique automatiquement."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Dans les comptes consolidés, la voie la plus directement pertinente est la couverture de juste valeur de la créance/dette de dividende en devise si elle constitue un élément monétaire intragroupe dont l'effet de change n'est pas totalement éliminé. Une couverture de flux de trésorerie peut aussi être documentée seulement si l'exposition visée est bien la variabilité des flux de règlement en monnaie fonctionnelle; la couverture d'investissement net ne correspond pas aux faits décrits."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende intragroupe a déjà été comptabilisé en créance/dette: on est donc face à un actif/passif reconnu. En consolidation, cette voie devient pertinente si la créance/dette est un élément monétaire intragroupe et si le risque de change correspondant n'est pas totalement éliminé, car IFRS 9 prévoit alors l'exception permettant de désigner cet item en couverture.",
      "conditions_fr": [
        "La créance/dette de dividende constitue un élément monétaire intragroupe.",
        "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation viserait la variation de change de la créance/dette reconnue dans les comptes consolidés.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.5.2",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Cette voie n'est envisageable dans ce cas que si l'exposition couverte est formulée comme la variabilité, en monnaie fonctionnelle, des flux de règlement du dividende en devise. Elle reste conditionnée au même point clé de consolidation: l'item doit relever de l'exception visant le risque de change d'un élément monétaire intragroupe non totalement éliminé.",
      "conditions_fr": [
        "La documentation désigne la variabilité des flux de règlement en monnaie fonctionnelle du dividende en devise.",
        "Les écarts de change de l'élément monétaire intragroupe ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation doit cibler les flux de règlement futurs de la créance/dette plutôt que la seule réévaluation comptable du poste.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.4.1",
          "excerpt": "there is formal designation and documentation of the hedging relationship"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "Les faits décrits portent sur une créance/dette de dividende intragroupe déjà comptabilisée, pas sur les net assets d'une foreign operation. Or le modèle IFRIC 16 vise le risque de change d'un investissement net dans une activité à l'étranger; sur ces faits, la créance de dividende ne correspond pas à cet objet de couverture.",
      "conditions_fr": [],
      "practical_implication_fr": "Cette voie ne permet pas, sur les faits fournis, de documenter la partie change de la créance de dividende elle-même.",
      "references": [
        {
          "section": "7",
          "excerpt": "applies to an entity that hedges the foreign currency risk arising from its net investments in foreign operations"
        },
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount of the net assets"
        },
        {
          "section": "10",
          "excerpt": "Hedge accounting may be applied only to the foreign exchange differences arising between the functional currency of the foreign operation and the parent entity’s functional currency"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Documenter dès l'origine l'élément couvert, le risque de change couvert, l'instrument de couverture et la méthode d'évaluation de l'efficacité.",
    "Vérifier en consolidation que la créance/dette de dividende est bien un élément monétaire intragroupe entre entités ayant des monnaies fonctionnelles différentes et que son effet de change n'est pas totalement éliminé.",
    "Si la voie retenue est la couverture de flux de trésorerie, formuler explicitement dans la documentation que le risque couvert est la variabilité des flux de règlement en monnaie fonctionnelle.",
    "Ne pas utiliser le modèle de couverture d'investissement net pour cette créance de dividende sauf si l'exposition documentée porte en réalité sur les net assets d'une activité étrangère, ce qui n'est pas le cas dans les faits fournis."
  ]
}
