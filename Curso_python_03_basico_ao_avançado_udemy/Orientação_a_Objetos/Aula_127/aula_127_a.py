import json
ARQUIVO = 'aula_127.json'


class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('carlos', 37)
p2 = Pessoa('mayara', 37)
p3 = Pessoa('neto', 7)
p4 = Pessoa('luna', 5)

banco_dados = [p1.__dict__, p2.__dict__, p3.__dict__, p4.__dict__]

with open(ARQUIVO, 'w') as arquivo:
    json.dump(banco_dados, arquivo, ensure_ascii=False, indent=2)