import os
import matplotlib.pyplot as plt
from typing import List, Dict


class Plotter:
    """Gera gráficos para respostas e escores do NEO PI-R."""

    @staticmethod
    def plot_response_distribution(responses: List[int], save_dir: str):
        freq = [responses.count(i) for i in range(1, 6)]
        os.makedirs(save_dir, exist_ok=True)
        plt.figure(figsize=(8, 6))
        plt.bar(range(1, 6), freq)
        plt.xlabel('Resposta (1–5)')
        plt.ylabel('Frequência')
        plt.title('Distribuição de Respostas NEO PI-R')
        plt.tight_layout()
        plt.savefig(os.path.join(save_dir, 'distribuicao_respostas.png'))
        plt.close()

    @staticmethod
    def plot_domain_scores(domain_scores: Dict[str, int], save_dir: str):
        os.makedirs(save_dir, exist_ok=True)
        domains = list(domain_scores.keys())
        values = [domain_scores[d] for d in domains]
        plt.figure(figsize=(10, 6))
        plt.bar(domains, values)
        plt.xticks(rotation=45, ha='right')
        plt.ylabel('Escore Bruto')
        plt.title('Escore por Fator dos Cinco Grandes')
        plt.tight_layout()
        plt.savefig(os.path.join(save_dir, 'escores_dominios.png'))
        plt.close()
