import json
from aula_127_a import ARQUIVO, Pessoa

with open(ARQUIVO, 'r') as arquivo:
    dados = json.load(arquivo)

    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])
    p4 = Pessoa(**dados[3])

print(f'{p1.nome}, {p1.idade}')
print(f'{p2.nome}, {p2.idade}')
print(f'{p3.nome}, {p3.idade}')
print(f'{p4.nome}, {p4.idade}')