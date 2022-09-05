from itertools import groupby
from time import sleep

alunos = [
    {'nome': 'carlos', 'nota': 'A'},
    {'nome': 'mayara', 'nota': 'B'},
    {'nome': 'neto', 'nota': 'C'},
    {'nome': 'luna', 'nota': 'A'},
    {'nome': 'rosiclé', 'nota': 'B'},
    {'nome': 'valdênia', 'nota': 'A'},
    {'nome': 'pedro', 'nota': 'C'},
    {'nome': 'valeria', 'nota': 'A'},
    {'nome': 'flavio', 'nota': 'B'},
    {'nome': 'david', 'nota': 'A'},
    {'nome': 'milena', 'nota': 'A'},
    {'nome': 'emilly', 'nota': 'A'},
]

def ordena(item):
    return item['nota']

alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    valores = list(valores_agrupados)
    
    print(f'Agrupamento: {agrupamento}')
    for aluno in valores:
        print(f'\t{aluno}')
    print(f'\t{len(valores)} alunos tiraram nota {agrupamento}')
    sleep(1)