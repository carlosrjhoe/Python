class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.logar = None

    @property
    def nome(self):
        return self.__nome

    @property
    def logar(self):
        return self.__logar

    @logar.setter
    def logar(self, logar):
        self.__logar = logar

class Identificador:
    def __init__(self, numero):
        self.numero = numero

    @property
    def numero(self):
        return self.__numero

    def logar(self):
        print('Logando no sistema...')