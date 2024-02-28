class Contato:
    def __init__(self, residencial, celular):
        self.residencial = residencial
        self.celular = celular

class Cliente:
    def __init__(self, nome, idade, fone=None):
        self.nome = nome
        self.idade = idade
        self.fone = []

    def addfone(self, residencial, celular):
        self.fone.append(Contato(residencial, celular))

    def listaFone(self):
        for fone in self.fone:
            print(f'{fone.residencial} - {fone.celular}')