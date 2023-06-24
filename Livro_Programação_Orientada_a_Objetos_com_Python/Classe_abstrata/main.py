from abc import ABC, abstractclassmethod

class Pessoa(ABC):
    @abstractclassmethod
    def logar(self):
        pass

class Usuario(Pessoa):
    def logar(self):
        print('Usuário logado no sistema.')

if __name__ == '__main__':
    user_01 = Usuario()
    user_01.logar()