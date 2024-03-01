from abc import ABC, abstractclassmethod

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def acao_1(self):
        print(f'{self.nome} está dormindo.')

class Jogador(Pessoa):
    def acao_2(self):
        print(f'{self.nome} está comendo.')

class SaveJogador(Jogador):
    def acao_1(self):
        super().acao_1()
        print(f'{self.nome} está acordando.')

class PessoaABC(ABC):
    @abstractclassmethod
    def logar(self, chaveSeguranca):
        pass

class Usuario(PessoaABC):
    def logar(self, chaveSeguranca):
        print('Usuário logado no sistemas')

class Bot(PessoaABC):
    def logar(self, chaveSeguranca):
        print('Sistema rodando em segundo plano')