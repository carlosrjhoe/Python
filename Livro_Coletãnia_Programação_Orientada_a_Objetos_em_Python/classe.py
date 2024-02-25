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

if __name__ == "__main__":
    pessoa01 = Pessoa.ano_nascimento('Carlos', 1985)
    print(pessoa01.idade)
    