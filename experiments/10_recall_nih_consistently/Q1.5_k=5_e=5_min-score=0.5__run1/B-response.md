{
  "assumptions_fr": [
    "La question vise la comptabilité de couverture selon IFRS 9 au niveau des états financiers consolidés.",
    "La créance de dividende intragroupe crée une exposition au risque de change au sein du groupe."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais seulement via une couverture de juste valeur du risque de change d’un poste monétaire intragroupe. Il faut que la créance de dividende produise des écarts de change non totalement éliminés en consolidation."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans la situation décrite, la créance de dividende est déjà un actif reconnu. En consolidation, les éléments intragroupe sont en principe exclus, mais IFRS 9 prévoit une exception pour le risque de change d’un poste monétaire intragroupe lorsque les écarts de change ne sont pas totalement éliminés. Si cette condition est remplie, une relation de couverture formellement documentée peut être désignée.",
      "conditions_fr": [
        "La créance à recevoir est un poste monétaire intragroupe exposé à un risque de change.",
        "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation."
      ],
      "practical_implication_fr": "La documentation doit viser la créance reconnue comme élément couvert et le seul risque de change retenu.",
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
          "excerpt": "there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "non",
      "reasoning_fr": "Ici, le dividende est déjà comptabilisé en créance intragroupe. Le modèle de cash flow hedge, dans les extraits fournis, vise surtout la variabilité de flux ou les transactions intragroupe prévisionnelles hautement probables; ce n’est pas le cas d’une créance déjà constatée. L’exposition décrite est celle d’un poste monétaire reconnu, pas d’un flux futur intragroupe à venir.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas documenter cette exposition comme couverture de flux de trésorerie tant que l’élément couvert est la créance déjà reconnue.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’un investissement net à l’étranger",
      "applicability": "non",
      "reasoning_fr": "La couverture d’un investissement net vise le risque de change sur un montant de net assets d’une activité à l’étranger. Une créance de dividende intragroupe comptabilisée à recevoir n’est pas, dans les faits décrits, un montant de net assets constituant l’investissement net; c’est un poste monétaire de règlement intragroupe. Ce modèle ne correspond donc pas à cette situation.",
      "conditions_fr": [],
      "practical_implication_fr": "Ne pas qualifier la créance de dividende comme élément couvert au titre d’une couverture d’investissement net.",
      "references": [
        {
          "section": "11",
          "excerpt": "The hedged item can be an amount of net assets"
        },
        {
          "section": "10",
          "excerpt": "between the functional currency of the foreign operation and the parent entity’s functional currency"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Confirmer que les entités concernées ont des monnaies fonctionnelles différentes.",
    "Vérifier que les écarts de change sur la créance et le passif corrélatif ne sont pas totalement éliminés en consolidation.",
    "Mettre en place dès l’origine la désignation formelle, la documentation et l’analyse d’efficacité exigées par IFRS 9 6.4.1."
  ]
}
