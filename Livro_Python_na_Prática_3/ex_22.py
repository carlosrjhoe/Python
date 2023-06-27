"""22 - Utilizando de recursos da biblioteca random, simule o lançamento de dois dados de 20 faces e calcule a probabilidade de cada combinação de resultados simulando 20 lançamentos destes dados:"""

import random
from collections import defaultdict

def calcular_probabilidade():
    resultados = defaultdict(int)

    n_lancamento = int(input('Digite a quantidade de lançamentos: '))
    total_faces = int(input('Digite a quantidade de faces: '))

    for _ in range(n_lancamento):
        dado_01 = random.randint(1, total_faces)
        dado_02 = random.randint(1, total_faces)
        combinacao = (dado_01 + dado_02)
        resultados[combinacao] += 1

    for combinacao, ocorrencias in resultados.items():
        probabilidade = ocorrencias / n_lancamento
        print(f'A combinação: {combinacao} ocorreu {ocorrencias} vezes.')
        print(f'Probabilidade: {probabilidade:.2f}%')

if __name__ == '__main__':
    calcular_probabilidade()