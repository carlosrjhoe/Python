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

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.nome}, {self.idade})'
        return f'{class_name} - {attrs}'

class Cliente(Pessoa):
    def __init__(self, nome=str, idade=int) -> None:
        super().__init__(nome, idade)
        self.conta = None


if __name__ == '__main__':
    carlos = Cliente('carlos', 37)
    print(carlos)
    print(carlos.conta)