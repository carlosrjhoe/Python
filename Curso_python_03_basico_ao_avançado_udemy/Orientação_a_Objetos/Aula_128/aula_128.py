from datetime import datetime
class Pessoa:
    
    ano = datetime.now().year
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        print(f'Nome: {self.nome.title()}, idade: {self.idade}')
        
    def data_nascimento(self, idade):
        print(f'{self.nome.title()} nasceu em {self.ano - idade}')
        return


if __name__ == '__main__':
    p1 = Pessoa('carlos', 37)
    p1.apresentacao()
    p1.data_nascimento(37)