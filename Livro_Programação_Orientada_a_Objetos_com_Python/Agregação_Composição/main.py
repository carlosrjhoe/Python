"""Agregação e composição de classe"""

class Contato:
    def __init__(self, residencial, celular):
        self.residencial = residencial
        self.celular = celular

class Cliente:
    def __init__(self, nome, idade, fone=None):
        self.nome = nome
        self.idade = idade
        self.fone = []

    def addFone(self, residencial, celular):
        self.fone.append(Contato(residencial, celular))

    def infoCliente(self):
        print(f'Nome: {self.nome.title()}\nIdade: {self.idade}')
        return
    
    def listaFone(self):
        print('Contato:')
        for fone in self.fone:
            print(f'Tel.:{fone.residencial}')
            print(f'Cel.:{fone.celular}')
        return

if __name__ == '__main__':
    cliente_01 = Cliente('carlos', 38)
    cliente_01.addFone(8135219090, 81988887777)
    cliente_01.infoCliente()
    cliente_01.listaFone()