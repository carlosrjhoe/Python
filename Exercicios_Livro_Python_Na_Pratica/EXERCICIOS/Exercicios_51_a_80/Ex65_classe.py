class Carro:

    def __init__(self, nome, ano, cor):
        self.nome = nome
        self.ano = ano
        self.cor = cor


carro_carlos = Carro('serato', 2008, 'prata')
carro_mayara = Carro('tucson', 2010, 'branco')

print(f'{carro_carlos.nome}\n{carro_carlos.ano}\n{carro_carlos.cor}.')
print(f'{carro_mayara.nome}\n{carro_mayara.ano}\n{carro_mayara.cor}.')
