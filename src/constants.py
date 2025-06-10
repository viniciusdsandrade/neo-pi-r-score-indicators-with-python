from typing import List, Dict

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

REVERSED_ITEMS = {
    # Neuroticismo: Ansiedade        (itens recomendados = 5)
    0, 60, 180,
    # Neuroticismo: Hostilidade      (itens recomendados = 5)
    35, 95, 125, 155,
    # Neuroticismo: Depressão        (itens recomendados = 5)
    10, 70,
    # Neuroticismo: Embaraço         (itens recomendados = 5)
    45, 105, 165,
    # Neuroticismo: Impulsividade    (itens recomendados = 5)
    20, 80, 140, 230,
    # Neuroticismo: Vulnerabilidade  (itens recomendados = 5)
    55, 115, 175, 205, 235,
    # Extroversão: Acolhimento        (recomendados = 2 → reverse)
    31, 91,
    # Extroversão: Gregariedade      (recomendados = 2 → reverse)
    6, 66, 126, 186,
    # Extroversão: Assertividade     (recomendados = 1 → reverse)
    41, 161, 191, 221,
    # Extroversão: Atividade         (recomendados = 1 → reverse)
    136,
    # Extroversão: EmoçõesPositivas  (recomendados = 2 → reverse)
    86, 146, 206,
    # Amabilidade: Franqueza        (recomendados = 2 → reverse)
    38, 98, 158, 188,
    # Amabilidade: Altruísmo        (recomendados = 2 → reverse)
    13, 73, 133,
    # Amabilidade: Modéstia         (recomendados = 2 → reverse)
    23, 83, 173, 233,
    # Amabilidade: Sensibilidade    (recomendados = 2 → reverse)
    58, 118, 178, 208,
    # Conscienciosidade: Competência (recomendados = 1 → reverse)
    34, 94, 154,
    # Conscienciosidade: Ordem       (recomendados = 2 → reverse)
    9, 129, 189, 219,
    # Conscienciosidade: Dever       (recomendados = 1 → reverse)
    44, 104,
    # Conscienciosidade: Realização  (recomendados = 2 → reverse)
    19, 79, 139, 229,
    # Conscienciosidade: Autodisciplina (recomendados = 1 → reverse)
    54, 114, 174, 204,
    # Conscienciosidade: Ponderação  (recomendados = 2 → reverse)
    89, 149
}
