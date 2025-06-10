from typing import List, Dict
from constants import FACET_ITEMS, REVERSED_ITEMS


class Scorer:
    """Calcula escores de facetas e domínios do NEO PI-R."""

    @staticmethod
    def reverse_score(value: int) -> int:
        return 6 - value

    def compute_facet_scores(self, responses: List[int]) -> Dict[str, int]:
        scores: Dict[str, int] = {}
        for facet, indices in FACET_ITEMS.items():
            total = 0
            for idx in indices:
                val = responses[idx]
                if idx in REVERSED_ITEMS:
                    val = self.reverse_score(val)
                total += val
            scores[facet] = total
        return scores

    @staticmethod
    def compute_domain_scores(facet_scores: Dict[str, int]) -> Dict[str, int]:
        domain_map = {
            'Neuroticismo': [f for f in facet_scores if f.startswith('N')],
            'Extroversão': [f for f in facet_scores if f.startswith('E')],
            'Abertura': [f for f in facet_scores if f.startswith('O')],
            'Amabilidade': [f for f in facet_scores if f.startswith('A')],
            'Conscienciosidade': [f for f in facet_scores if f.startswith('C')],
        }
        return {dom: sum(facet_scores[f] for f in facs) for dom, facs in domain_map.items()}
