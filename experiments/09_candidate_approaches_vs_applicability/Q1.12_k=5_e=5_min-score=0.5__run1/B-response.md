{
  "assumptions_fr": [
    "Le dividende intragroupe a déjà été déclaré et comptabilisé en créance et dette monétaires.",
    "La créance et la dette existent entre des entités du groupe ayant des monnaies fonctionnelles différentes, de sorte que les écarts de change sur ce poste monétaire intragroupe ne sont pas totalement éliminés en consolidation.",
    "L’analyse porte sur la comptabilité de couverture dans les états financiers consolidés au titre d’IFRS 9."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, en principe. Une créance de dividende intragroupe déjà comptabilisée peut entrer dans l’exception IFRS 9 pour les postes monétaires intragroupe au niveau consolidé si le risque de change affecte encore le résultat consolidé. La qualification formelle suppose toutefois une désignation et une documentation conformes à IFRS 9."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans cette situation, le dividende déclaré a créé une créance/dette intragroupe déjà comptabilisée, donc un poste monétaire intragroupe. IFRS 9 prévoit explicitement qu’au niveau consolidé le risque de change d’un tel poste peut être un élément couvert lorsqu’il génère des écarts non totalement éliminés. Cela cadre avec une couverture de juste valeur d’un actif ou passif reconnu, sous réserve d’une désignation formelle et d’une documentation adéquate.",
      "conditions_fr": [
        "La relation de couverture est désignée et documentée formellement dès son origine.",
        "L’instrument et le ratio de couverture permettent de démontrer l’efficacité de la couverture pour cette créance de dividende."
      ],
      "practical_implication_fr": "La créance de dividende déjà reconnue peut être désignée comme élément couvert au titre de son risque de change en consolidation.",
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
      "label_fr": "Couverture de flux de trésorerie",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "La même exception de l’article 6.3.6 rend éligible, en consolidation, le risque de change d’une créance intragroupe monétaire lorsque ce risque affecte le résultat consolidé. IFRS 9 autorise aussi une couverture de flux de trésorerie pour la variabilité des flux liés à un actif ou passif reconnu. Dans ce cas, la variabilité en monnaie fonctionnelle du règlement du dividende en devise peut être formellement désignée, si la relation est correctement documentée et testée.",
      "conditions_fr": [
        "La relation de couverture est désignée et documentée formellement dès son origine.",
        "La désignation vise explicitement la variabilité en monnaie fonctionnelle des flux de règlement de la créance de dividende."
      ],
      "practical_implication_fr": "La désignation porte alors sur la variabilité du flux de règlement en devise de la créance de dividende reconnue.",
      "references": [
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "6.4.1",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Vérifier que la créance de dividende est bien un poste monétaire intragroupe entre entités à monnaies fonctionnelles différentes et que les écarts de change affectent le résultat consolidé.",
    "Mettre en place dès l’origine une documentation IFRS 9 identifiant l’instrument de couverture, la créance de dividende couverte, le risque de change couvert et la méthode d’évaluation de l’efficacité.",
    "Choisir un modèle de couverture cohérent avec la désignation retenue pour cette créance de dividende et l’appliquer de manière disciplinée."
  ]
}
