from datetime import date

class Pessoa:
    ano_atual = date.today()
    ano = ano_atual.year
    def __init__(self, nome, idade, sexo='não definido', altura='não definido'):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
    
    def acao1(self) -> str:
        print(f'{self.ano} - Bem vindo {self.nome.title()}, você tem {self.idade} anos, seu sexo é {self.sexo}, e sua altura é {self.altura}!')

if __name__ == "__main__":
    pessoa01 = Pessoa('carlos', 38, 'M', 1.81)
    pessoa02 = Pessoa('mayara', 39, 'F', 1.70)
    pessoa01.acao1()
    pessoa02.acao1()
    