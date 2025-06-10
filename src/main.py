import os
from loader import ResponseLoader
from scorer import Scorer
from plotter import Plotter

BASE_DIR = r"C:\Users\Vinícius Andrade\Desktop\neo-pi-r-score-indicators-with-python"

if __name__ == '__main__':
    # Carrega respostas
    filepath = os.path.join(BASE_DIR, 'questionario', 'respostas.json')
    respostas = ResponseLoader.load_from_json(filepath)

    # Gera histograma geral
    resultado_dir = os.path.join(BASE_DIR, 'resultado')
    Plotter.plot_response_distribution(respostas, resultado_dir)

    # Calcula escores e gera gráfico por domínio
    scorer = Scorer()
    facet_scores = scorer.compute_facet_scores(respostas)
    domain_scores = scorer.compute_domain_scores(facet_scores)
    Plotter.plot_domain_scores(domain_scores, resultado_dir)
