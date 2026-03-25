{
  "assumptions": [],
  "recommendation": {
    "answer": "oui_sous_conditions",
    "justification": "Oui, mais uniquement dans le cadre IFRS 9 et si le risque de change affecte le résultat consolidé. Les voies pertinentes sont la couverture de juste valeur de la créance/dette intragroupe reconnue ou, selon le stade, une couverture de flux de trésorerie; la couverture d'investissement net ne vise pas une créance de dividende intragroupe."
  },
  "approaches": [
    {
      "id": "approach_1",
      "normalized_label": "fair_value_hedge",
      "label_fr": "Couverture de juste valeur de la créance/dette intragroupe",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 permet une fair value hedge sur un actif ou passif reconnu exposé à un risque particulier affectant le résultat. En consolidation, un poste intragroupe n'est éligible sur la partie change que s'il s'agit d'un poste monétaire dont les écarts de change ne sont pas totalement éliminés; la composante change peut être désignée si elle est identifiable et mesurable, avec documentation et test d'efficacité à l'origine.",
      "conditions_fr": [
        "La créance/dette de dividende est un poste monétaire",
        "Les écarts de change correspondants ne sont pas totalement éliminés en consolidation",
        "Seule la composante risque de change est désignée si elle est séparément identifiable et fiable à mesurer",
        "La désignation formelle, la documentation et les critères d'efficacité sont en place dès l'inception"
      ],
      "practical_implication_fr": "Applicable surtout si le dividende intragroupe est déjà comptabilisé en créance/dette et que l'on veut documenter la partie change de ce poste reconnu.",
      "references": [
        {
          "section": "IFRS 9 6.5.2(a)",
          "excerpt": "fair value hedge: a hedge of the exposure to changes in fair value of a recognised asset or liability"
        },
        {
          "section": "IFRS 9 6.3.6",
          "excerpt": "the foreign currency risk of an intragroup monetary item ... may qualify as a hedged item in the consolidated financial statements"
        },
        {
          "section": "IFRS 9 6.3.7(a)",
          "excerpt": "provided that ... the risk component is separately identifiable and reliably measurable"
        },
        {
          "section": "IFRS 9 6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_2",
      "normalized_label": "cash_flow_hedge",
      "label_fr": "Couverture de flux de trésorerie des flux en devise",
      "applicability": "oui_sous_conditions",
      "reasoning_fr": "IFRS 9 autorise une cash flow hedge pour la variabilité de flux d'un actif/passif reconnu ou d'une transaction future hautement probable. En consolidation, la partie change d'un item ou flux intragroupe n'est éligible que si elle affecte le résultat consolidé; avant comptabilisation, la transaction doit être hautement probable et libellée dans une devise autre que la monnaie fonctionnelle de l'entité concernée.",
      "conditions_fr": [
        "Si la couverture vise un item intragroupe déjà reconnu, les effets de change ne sont pas totalement éliminés en consolidation",
        "Si la couverture vise la transaction avant comptabilisation, cette transaction intragroupe est hautement probable",
        "La transaction intragroupe future est libellée dans une devise autre que la monnaie fonctionnelle de l'entité qui la conclut",
        "Le risque de change affectera le résultat consolidé",
        "La désignation formelle, la documentation et les critères d'efficacité sont en place dès l'inception"
      ],
      "practical_implication_fr": "Voie pertinente si la documentation est posée sur les flux en devise, soit sur un poste reconnu, soit en amont si le dividende intragroupe reste au stade de transaction hautement probable.",
      "references": [
        {
          "section": "IFRS 9 6.5.2(b)",
          "excerpt": "cash flow hedge: a hedge of the exposure to variability in cash flows"
        },
        {
          "section": "IFRS 9 6.3.6",
          "excerpt": "the foreign currency risk of a highly probable forecast intragroup transaction may qualify as a hedged item"
        },
        {
          "section": "IFRS 9 6.4.1(b)",
          "excerpt": "at the inception of the hedging relationship there is formal designation and documentation"
        }
      ]
    },
    {
      "id": "approach_3",
      "normalized_label": "net_investment_hedge",
      "label_fr": "Couverture d'investissement net",
      "applicability": "non",
      "reasoning_fr": "IFRIC 16 réserve ce modèle à la couverture du risque de change d'un investissement net dans une activité étrangère et exclut son usage par analogie pour d'autres cas. Une créance de dividende intragroupe n'est pas, en elle-même, un montant de net assets d'une activité étrangère; cette voie ne devient pertinente que si l'objet couvert est redéfini comme tel.",
      "conditions_fr": [
        "Cette voie ne deviendrait pertinente que si l'élément couvert était un montant de net assets d'une activité étrangère, et non la créance de dividende"
      ],
      "practical_implication_fr": "À écarter pour la créance de dividende intragroupe telle que décrite.",
      "references": [
        {
          "section": "IFRIC 16 8",
          "excerpt": "This Interpretation applies only to hedges of net investments in foreign operations"
        },
        {
          "section": "IFRIC 16 11",
          "excerpt": "The hedged item can be an amount of net assets equal to or less than the carrying amount"
        }
      ]
    }
  ],
  "operational_points_fr": [
    "La documentation doit être finalisée dès l'inception de la relation de couverture, avec identification de l'instrument, de l'élément couvert, du risque de change et du hedge ratio.",
    "En consolidation, le point clé est de démontrer que les écarts de change sur la créance/dette ou sur la transaction intragroupe affectent le résultat consolidé et ne sont pas totalement éliminés.",
    "Si le dividende est déjà comptabilisé en créance/dette, la lecture la plus directe est la couverture de juste valeur; s'il est seulement hautement probable avant reconnaissance, la couverture de flux de trésorerie peut être documentée.",
    "La couverture d'investissement net ne doit pas être utilisée pour documenter la partie change d'une créance de dividende intragroupe."
  ]
}
