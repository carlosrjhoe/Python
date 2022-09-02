class Carro:

    def __init__(self, nome, ano, cor):
        self.nome = nome
        self.ano = ano
        self.cor = cor

    def informacao(self):
        print(f'Carro: {self.nome}')
        print(f'Ano: {self.ano}')
        print(f'Cor: {self.cor}')
        
carro_carlos = Carro('serato', 2008, 'prata')
carro_mayara = Carro('tucson', 2010, 'branco')

carro_carlos.informacao()
carro_mayara.informacao()