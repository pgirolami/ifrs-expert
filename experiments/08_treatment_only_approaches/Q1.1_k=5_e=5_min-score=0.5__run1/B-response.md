{
  "assumptions_fr": [
    "Le dividende intragroupe a été déclaré et comptabilisé en créance/dette monétaire entre des entités du groupe ayant des monnaies fonctionnelles différentes.",
    "Les gains ou pertes de change correspondants ne sont pas totalement éliminés en consolidation, de sorte que le poste monétaire intragroupe peut, par exception, être éligible comme élément couvert en comptes consolidés.",
    "Si une couverture d’investissement net est envisagée, le groupe détient une activité étrangère dont les actifs nets sont inclus dans les comptes consolidés."
  ],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, sous conditions. Dans cette situation, la documentation la plus directement alignée est la couverture de juste valeur de la créance/dette monétaire intragroupe sur son risque de change. La couverture de flux de trésorerie reste possible si la documentation vise la variabilité du règlement en devise, tandis que la couverture d’investissement net n’est pertinente que si l’exposition couverte est la net investment dans l’activité étrangère, et non la créance de dividende elle-même."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Dans ce cas, le dividende intragroupe déjà comptabilisé en créance est un actif monétaire reconnu; avec des monnaies fonctionnelles différentes, son risque de change peut exister en consolidation.\nComme l’hypothèse précise que les écarts de change ne sont pas totalement éliminés, l’exception IFRS 9 pour les postes monétaires intragroupe permet ce traitement, sous réserve d’une désignation formelle, de la documentation et de l’efficacité de la couverture.",
      "conditions_fr": [
        "La créance/dette de dividende est un poste monétaire intragroupe entre entités à monnaies fonctionnelles différentes.",
        "Les écarts de change sur ce poste ne sont pas totalement éliminés en consolidation.",
        "La relation de couverture est désignée et documentée dès l’origine, avec identification de l’instrument, du risque de change couvert, du hedge ratio et de la méthode de test d’efficacité."
      ],
      "practical_implication_fr": "C’est la voie la plus directe pour documenter la partie change de la créance/dette de dividende en comptes consolidés.",
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
      "reasoning_fr": "Dans cette situation, IFRS 9 permet aussi une couverture de flux de trésorerie sur un actif ou passif reconnu lorsque la variabilité des flux due au risque couvert peut affecter le résultat.\nCela n’est pertinent ici que si la documentation vise la variabilité du flux de règlement du dividende en monnaie fonctionnelle liée au change; sinon, la mécanique est moins directement rattachée à une créance déjà comptabilisée.",
      "conditions_fr": [
        "La documentation vise la variabilité des flux de règlement en monnaie fonctionnelle liée au risque de change sur la créance/dette de dividende.",
        "Cette variabilité de change peut affecter le résultat consolidé.",
        "La relation de couverture satisfait aux exigences de désignation formelle, de documentation, d’existence d’une relation économique et de hedge ratio."
      ],
      "practical_implication_fr": "Le suivi documentaire portera sur la variabilité du règlement en devise jusqu’au paiement du dividende.",
      "references": [
        {
          "section": "6.5.2",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows ... of a recognised asset or liability"
        },
        {
          "section": "6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "6.4.1",
          "excerpt": "the hedging relationship meets all of the following hedge effectiveness requirements"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d’investissement net",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "Ce traitement ne s’applique à cette situation que si le groupe documente le risque de change au niveau de la net investment dans une activité étrangère incluse en consolidation, et non au niveau de la créance de dividende elle-même.\nIl peut donc être pertinent en arrière-plan d’une exposition de conversion sur les actifs nets de l’activité étrangère, mais il ne qualifie pas la créance intragroupe de dividende comme élément couvert de cette catégorie.",
      "conditions_fr": [
        "L’exposition couverte est une net investment dans une activité étrangère dont les actifs nets sont inclus dans les comptes consolidés.",
        "Le risque désigné est un risque de change entre la monnaie fonctionnelle de l’activité étrangère et celle d’une société mère pertinente.",
        "La relation est documentée conformément à IFRS 9 et ne duplique pas une autre couverture du même risque dans les comptes consolidés."
      ],
      "practical_implication_fr": "La documentation porterait sur l’investissement net dans l’activité étrangère; la créance de dividende resterait un élément distinct.",
      "references": [
        {
          "section": "2",
          "excerpt": "Hedge accounting of the foreign currency risk arising from a net investment in a foreign operation will apply only when the net assets of that foreign operation are included in the financial statements"
        },
        {
          "section": "12",
          "excerpt": "The hedged risk may be designated as the foreign currency exposure arising between the functional currency of the foreign operation and the functional currency of any parent entity"
        },
        {
          "section": "13",
          "excerpt": "may qualify for hedge accounting only once in the consolidated financial statements"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "Qualifier d’abord la créance/dette de dividende comme poste monétaire intragroupe entre monnaies fonctionnelles différentes et vérifier que les écarts de change ne sont pas totalement éliminés en consolidation.",
    "La désignation et la documentation doivent exister dès l’inception de la relation de couverture; elles doivent identifier l’instrument de couverture, l’élément couvert, le risque couvert, le hedge ratio et la méthode d’évaluation de l’efficacité.",
    "Si vous retenez la couverture de juste valeur ou de flux de trésorerie, le périmètre documentaire doit viser explicitement la créance/dette de dividende et son risque de change en consolidation.",
    "Si vous retenez la couverture d’investissement net, l’élément couvert devient la net investment dans l’activité étrangère, pas la créance de dividende elle-même.",
    "Pour une couverture d’investissement net, l’instrument de couverture peut être détenu par une autre entité du groupe, mais la stratégie de groupe doit être clairement documentée et le même risque ne peut qualifier qu’une seule fois dans les comptes consolidés."
  ]
}
