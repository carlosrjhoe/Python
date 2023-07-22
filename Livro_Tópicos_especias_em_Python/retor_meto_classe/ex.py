class Pessoa:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def __repr__(self) -> str:
        '''__repr__( ) Basicamente retorna qualquer tipo de dado para qualquer escopo quando a classe for instanciada por uma variável/objeto externo.'''
        return f'{self.name.title()} é {self.profession.title()}'

if __name__ == '__main__':
    pessoa = Pessoa('carlos', 'encarregado de manutenção')
    pessoa1 = Pessoa('mayara', 'auxiliar de dp')
    print(pessoa)
    print(pessoa1)