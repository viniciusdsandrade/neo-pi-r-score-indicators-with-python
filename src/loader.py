import json
from typing import List


class ResponseLoader:
    """Carrega respostas do NEO PI-R a partir de JSON."""

    @staticmethod
    def load_from_json(path: str) -> List[int]:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [int(data[q]) for q in sorted(data, key=lambda x: int(x))]
