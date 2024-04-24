from random import randint

class Pessoa:
    ANO_ATUAL = 2024
    
    def __init__(self, nome=str, idade=int) -> None:
        self.nome = nome
        self.idade = idade
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome=str, idade=int) -> None:
        super().__init__(nome, idade)
        self.conta = None