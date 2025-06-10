from typing import List, Dict
import json
import os
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# 1) MAPEAMENTO DE FACETAS → ITENS (0-based indices)
# -----------------------------------------------------------------------------
FACET_ITEMS: Dict[str, List[int]] = {
    # Neuroticismo
    "N1_Ansiedade": [0, 30, 60, 90, 120, 150, 180, 220],
    "N2_Hostilidade": [5, 35, 65, 95, 125, 155, 185, 215],
    "N3_Depressão": [10, 40, 70, 100, 130, 160, 190, 220],
    "N4_Embaraço": [15, 45, 75, 105, 135, 165, 195, 225],
    "N5_Impulsividade": [20, 50, 80, 110, 140, 170, 200, 230],
    "N6_Vulnerabilidade": [25, 55, 85, 115, 145, 175, 205, 235],
    # Extroversão
    "E1_Cordialidade": [1, 31, 61, 91, 121, 151, 181, 211],
    "E2_Gregariedade": [6, 36, 66, 96, 126, 156, 186, 216],
    "E3_Assertividade": [11, 41, 71, 101, 131, 161, 191, 221],
    "E4_Atividade": [16, 46, 76, 106, 136, 166, 196, 226],
    "E5_Excitação": [21, 51, 81, 111, 141, 171, 201, 231],
    "E6_EmoçõesPositivas": [26, 56, 86, 116, 146, 176, 206, 236],
    # Abertura
    "O1_Fantasia": [2, 32, 62, 92, 122, 152, 182, 212],
    "O2_Estética": [7, 37, 67, 97, 127, 157, 187, 217],
    "O3_Sentimentos": [12, 42, 72, 102, 132, 162, 192, 222],
    "O4_AçõesVariadas": [17, 47, 77, 107, 137, 167, 197, 227],
    "O5_Ideias": [22, 52, 82, 112, 142, 172, 202, 232],
    "O6_Valores": [27, 57, 87, 117, 147, 177, 207, 237],
    # Amabilidade
    "A1_Confiança": [3, 33, 63, 93, 123, 153, 183, 213],
    "A2_Retidão": [8, 38, 68, 98, 128, 158, 188, 218],
    "A3_Altruísmo": [13, 43, 73, 103, 133, 163, 193, 223],
    "A4_Complacência": [18, 48, 78, 108, 138, 168, 198, 228],
    "A5_Modéstia": [23, 53, 83, 113, 143, 173, 203, 233],
    "A6_Sensibilidade": [28, 58, 88, 118, 148, 178, 208, 238],
    # Conscienciosidade
    "C1_Competência": [4, 34, 64, 94, 124, 154, 184, 214],
    "C2_Ordem": [9, 39, 69, 99, 129, 159, 189, 219],
    "C3_Dever": [14, 44, 74, 104, 134, 164, 194, 224],
    "C4_Realização": [19, 49, 79, 109, 139, 169, 199, 229],
    "C5_Autodisciplina": [24, 54, 84, 114, 144, 174, 204, 234],
    "C6_Ponderação": [29, 59, 89, 119, 149, 179, 209, 239],
}

# -----------------------------------------------------------------------------
# Itens de pontuação reversa (conforme manual)
# -----------------------------------------------------------------------------
REVERSED_ITEMS = {
    0, 60, 180, 35, 95, 125, 155, 10, 70, 45, 105, 165,
    20, 80, 140, 230, 55, 115, 175, 205, 235, 31, 91,
    6, 66, 126, 186, 41, 161, 191, 221, 136, 86, 146,
    206, 38, 98, 158, 188, 13, 73, 133, 23, 83, 173,
    233, 58, 118, 178, 208, 34, 94, 154, 9, 129, 189,
    219, 44, 104, 19, 79, 139, 229, 54, 114, 174, 204,
    89, 149
}


# -----------------------------------------------------------------------------
# Carregamento de respostas JSON
# -----------------------------------------------------------------------------
def load_responses_json(path: str) -> List[int]:
    """Lê JSON de respostas e retorna lista ordenada."""
    with open(path, 'r', encoding='utf-8') as f:
        data: Dict[str, int] = json.load(f)
    return [int(data[q]) for q in sorted(data, key=lambda x: int(x))]


# -----------------------------------------------------------------------------
# Cálculo de escores
# -----------------------------------------------------------------------------
def reverse_score(value: int) -> int:
    return 6 - value


def compute_facet_scores(responses: List[int]) -> Dict[str, int]:
    scores: Dict[str, int] = {}
    for facet, indices in FACET_ITEMS.items():
        total = 0
        for idx in indices:
            val = responses[idx]
            if idx in REVERSED_ITEMS:
                val = reverse_score(val)
            total += val
        scores[facet] = total
    return scores


def compute_domain_scores(facet_scores: Dict[str, int]) -> Dict[str, int]:
    # Cada domínio é a soma das suas 6 facetas intermediárias
    domains = {
        "Neuroticismo": [f for f in facet_scores if f.startswith("N")],
        "Extroversão": [f for f in facet_scores if f.startswith("E")],
        "Abertura": [f for f in facet_scores if f.startswith("O")],
        "Amabilidade": [f for f in facet_scores if f.startswith("A")],
        "Conscienciosidade": [f for f in facet_scores if f.startswith("C")],
    }
    return {dom: sum(facet_scores[f] for f in facs) for dom, facs in domains.items()}


# -----------------------------------------------------------------------------
# Plotagem
# -----------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------
# Função main
# -----------------------------------------------------------------------------
def main():
    base = r"C:\Users\Vinícius Andrade\Desktop\neo-pi-r-score-indicators-with-python"
    respostas = load_responses_json(os.path.join(base, 'questionario', 'respostas.json'))
    # Histograma geral
    plot_response_distribution(respostas, os.path.join(base, 'resultado'))
    # Cálculo e gráfico por fator
    facet_scores = compute_facet_scores(respostas)
    domain_scores = compute_domain_scores(facet_scores)
    plot_domain_scores(domain_scores, os.path.join(base, 'resultado'))


# -----------------------------------------------------------------------------
# Execução
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
