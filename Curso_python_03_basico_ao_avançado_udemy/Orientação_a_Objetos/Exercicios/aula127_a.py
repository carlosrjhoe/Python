import json

CAMINH0_ARQUIVO = 'aula127.json'

class Pessoa:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Pessoa('carlos', 38)
p2 = Pessoa('mayara', 39)
p3 = Pessoa('neto', 8)
p4 = Pessoa('luna', 6)

bd = [vars(p1), vars(p2), vars(p3), vars(p4)]

with open(CAMINH0_ARQUIVO, 'w') as file:
    json.dump(bd, file, ensure_ascii=False, indent=2)