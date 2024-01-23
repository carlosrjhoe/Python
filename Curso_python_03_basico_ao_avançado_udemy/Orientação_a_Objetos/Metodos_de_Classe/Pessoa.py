from random import randint

class Pessoa:
    ANO_ATUAL = 2022
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        print(f'{self.ANO_ATUAL - self.idade}')
        
    @classmethod
    def por_ano_nascimento(cls, nome, idade, ano_nascimento):
        idade = cls.ANO_ATUAL - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def gera_id():
        numero_randomico = randint(10000, 19999)
        return numero_randomico