class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_class(self):
        print(f'{self.nome}, {self.sobrenome}, {self.__class__.__name__}')

class Cliente(Pessoa):
    ...


class Aluno(Cliente):
    ...

carlos = Cliente('carlos', 'conceição')
print(f'{carlos.nome.title()} {carlos.sobrenome.title()}')
carlos.falar_nome_class()

mayara = Aluno('mayara', 'ramos')
print(f'{mayara.nome.title()} {mayara.sobrenome.title()}')
mayara.falar_nome_class()
