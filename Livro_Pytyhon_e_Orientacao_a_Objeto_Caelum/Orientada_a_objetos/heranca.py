class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def informacao_carro(self):
        print(f'O carro: {self.modelo}, Ano: {self.ano}, cor: {self.cor}')

class VolksWagem(Carro):
    def __init__(self, modelo, ano, cor):
        super().__init__(modelo, ano, cor)

class Fiat(Carro):
    def __init__(self, modelo, ano, cor):
        super().__init__(modelo, ano, cor)


if __name__ == '__main__':
    carro_01 = VolksWagem('gol', 2017, 'vermelho')
    carro_01.informacao_carro()
    carro_02 = Fiat('Uno', 2009, 'branco')
    carro_02.informacao_carro()
    