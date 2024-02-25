from datetime import date

class Pessoa:
    ano_atual = date.today()
    ano = ano_atual.year
    def __init__(self, nome, idade, sexo='não definido', altura='não definido', login=False, logoff=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        self.login = login
        self.logoff = logoff
    
    def acao1(self) -> str:
        print(f'{self.ano} - Bem vindo {self.nome.title()}, você tem {self.idade} anos, seu sexo é {self.sexo}, e sua altura é {self.altura}!')

    def ano_nascimento(self):
        ano_nascimento = self.ano - self.idade
        print(f'Seu ano de nascimento é {ano_nascimento}')

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

if __name__ == "__main__":
    pessoa01 = Pessoa('carlos', 38, 'M', 1.81)
    pessoa02 = Pessoa('mayara', 39, 'F', 1.70)
    pessoa01.deslogar()
    pessoa01.logar()
    pessoa01.deslogar()
    pessoa02.deslogar()
    pessoa02.logar()
    pessoa02.logar()
    pessoa02.deslogar()
    