class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def info(self):
        print(f'{self.nome}, {self.sobrenome}, {self.__class__.__name__}')

class Cliente(Pessoa):
    ...


class Aluno(Cliente):
    ...