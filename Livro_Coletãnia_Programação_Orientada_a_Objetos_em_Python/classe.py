from datetime import date
from random import randint

class Pessoa:
    ano_atual = date.today()
    ano = ano_atual.year
    def __init__(self, nome, idade, preco, sexo='não definido', altura='não definido', login=False, logoff=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        self.login = login
        self.logoff = logoff
        self.preco = preco

    @property
    def preco(self):
        return self.preco_valido

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self.preco_valido = valor

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco*(percentual/100))
    
    def acao1(self) -> str:
        print(f'{self.ano} - Bem vindo {self.nome.title()}, você tem {self.idade} anos, seu sexo é {self.sexo}, e sua altura é {self.altura}!')

    @staticmethod
    def gerador_id():
        gerador = randint(100, 999)
        return gerador
    
    @classmethod
    def ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano - ano_nascimento  
        return cls(nome, idade)

    def logar(self):
        if not self.login:
            print(f'Bem vindo {self.nome}, você está logado no sistema.')
            self.login = True
        else:
            print(f'{self.nome} você já está logado no sistema.')

    def deslogar(self):
        if not self.login:
            print(f'Bem vindo {self.nome.title()}, você já está deslogado do sistema.')
        else:
            print(f'{self.nome.title()} deslogando do sistema.')
            self.login = False

    