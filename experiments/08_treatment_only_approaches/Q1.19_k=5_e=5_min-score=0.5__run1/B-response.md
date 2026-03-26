{
  "assumptions_fr": [
    "Le dividende intragroupe déclaré a déjà créé une créance et une dette intragroupe monétaires comptabilisées.",
    "Cette créance/dette est libellée dans une devise qui génère des écarts de change non totalement éliminés en consolidation parce que les entités du groupe concernées ont des monnaies fonctionnelles différentes."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, dans cette situation le risque de change peut être formellement désigné dans une relation de couverture en consolidation grâce à l’exception visant les éléments monétaires intragroupe. Il faut toutefois respecter la désignation formelle initiale, la documentation et les critères d’efficacité d’IFRS 9."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ici, le dividende déclaré a déjà donné naissance à une créance/dette intragroupe reconnue, donc à un actif/passif éligible au sens d’IFRS 9.\nSous l’hypothèse que le risque de change sur cet élément monétaire n’est pas totalement éliminé en consolidation, l’exception de 6.3.6 permet sa désignation comme élément couvert, et le modèle de juste valeur correspond directement à un actif/passif reconnu exposé à un risque particulier affectant le résultat.",
      "conditions_fr": [
        "La créance/dette intragroupe est un élément monétaire reconnu et fiable à mesurer.",
        "Le risque de change crée des gains ou pertes non totalement éliminés en consolidation.",
        "La relation est formellement désignée et documentée dès l’inception.",
        "La relation économique, le hedge ratio et l’absence de domination du risque de crédit sont démontrés."
      ],
      "practical_implication_fr": "Le groupe peut documenter en consolidation une couverture de juste valeur du risque de change attaché à la créance de dividende intragroupe.",
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
      "reasoning_fr": "Même si le dividende n’est plus une transaction future mais une créance déjà reconnue, IFRS 9 6.5.2(b) vise aussi un actif ou passif reconnu lorsque la variabilité des flux liée au risque couvert peut affecter le résultat.\nDans cette situation et sous les hypothèses données, la documentation d’une couverture de flux de trésorerie reste donc envisageable pour le risque de change de l’élément monétaire intragroupe, sous réserve du respect intégral des critères de 6.4.1.",
      "conditions_fr": [
        "Le risque couvert est formulé comme une variabilité des flux de règlement attribuable au change et affectant le résultat consolidé.",
        "L’élément monétaire intragroupe bénéficie bien de l’exception de 6.3.6 en consolidation.",
        "La désignation et la documentation sont établies à l’inception.",
        "Les exigences d’efficacité de la relation de couverture sont satisfaites."
      ],
      "practical_implication_fr": "Une documentation en cash flow hedge est possible, mais elle doit être précisément articulée autour de la variabilité des flux en monnaie fonctionnelle liée au change.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item"
        },
        {
          "section": "6.4.1",
          "excerpt": "the documentation shall include identification of the hedging instrument, the hedged item, the nature of the risk being hedged"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être mise en place à l’inception de la relation de couverture, avec identification de l’instrument, de l’élément couvert, du risque de change et de la méthode d’évaluation de l’efficacité.",
    "L’analyse doit être menée au niveau des comptes consolidés, car l’exception de 6.3.6 vise spécifiquement l’élément monétaire intragroupe en consolidation.",
    "Au vu des faits décrits, la couverture de juste valeur est l’approche la plus directement alignée avec une créance de dividende déjà comptabilisée; la couverture de flux de trésorerie exige une justification plus précise de la variabilité des flux."
  ]
}
