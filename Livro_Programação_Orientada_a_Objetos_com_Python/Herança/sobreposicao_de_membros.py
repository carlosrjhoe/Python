class Pessoa:
    def __init__(self, name):
        self.name = name.title()

    def acao_1(self):
        print(f'{self.name} está acordado.')

class Jogador(Pessoa):
    def acao_2(self):
        print(f'{self.name} está dormindo.')

class SaveJogador1(Jogador):
    """Herda tudo de Jogador1 e de Pessoa."""
    def acao_1(self):
        super().acao_1()
        print(f'{self.name} está comendo.')
    pass

if __name__ == '__main__':
    p1 = SaveJogador1('carlos')
    print(p1.name)
    p1.acao_1()
    p1.acao_2()

# >>>Carlos
# >>>Carlos está acordado.
# >>>Carlos está comendo. 
# >>>Carlos está dormindo.