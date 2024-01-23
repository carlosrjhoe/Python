import json
from aula127_a import CAMINH0_ARQUIVO, Pessoa

with open(CAMINH0_ARQUIVO, 'r') as file:
    pessoas = json.load(file)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])
    p4 = Pessoa(**pessoas[3])
    
    print(p1.name, p1.age)
    print(p2.name, p2.age)
    print(p3.name, p3.age)
    print(p4.name, p4.age)