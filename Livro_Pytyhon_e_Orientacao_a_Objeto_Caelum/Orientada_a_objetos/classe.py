class Usuario:

    def __init__(self, nome, idade):
        """construtor da classe"""
        self.nome = nome
        self.idade = idade

    def informacao(self):
        print(f'Meu nome é {self.nome.title()} e eu tenho {self.idade} anos de idade.')



if __name__ == '__main__':
    carlos = Usuario('carlos', 37)
    carlos.informacao()