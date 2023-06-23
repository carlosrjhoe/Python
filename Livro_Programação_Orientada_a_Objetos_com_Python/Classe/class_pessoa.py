from random import randint

class Pessoa:
    ano_atual = 2023
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def ano_do_nascimento(cls, nome, ano_do_nascimento):
        idade = cls.ano_atual - ano_do_nascimento
        return cls(nome, idade)

    @classmethod
    def gerador_id(self):
        gerador = randint(100, 999)
        return gerador


if __name__ == '__main__':
    pessoa_01 = Pessoa('carlos', 38)
    pessoa_02 = Pessoa('mayara', 39)
    print(f'{pessoa_01.idade}')
    print(f'{pessoa_01.gerador_id()}')
    print(f'{pessoa_02.idade}')
    print(f'{pessoa_02.gerador_id()}')