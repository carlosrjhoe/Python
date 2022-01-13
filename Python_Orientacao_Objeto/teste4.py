class Carro:

    def __init__(self, fabricante, modelo, anoCarro, valorVenda):
        self.fabricante = fabricante
        self.modelo = modelo
        self.anoCarro = anoCarro
        self.valorVenda = valorVenda


    def LigarCarro(self):
        print('Carro ligado')

    def DirigindoCarro(self):
        print('Carro em movimento')

    def DesligaCarro(self):
        print('Carro desligado')

    def Informacaocarro(self):
        print(self.fabricante, self.modelo, self.anoCarro, self.valorVenda)


carro_01 = Carro('Renault', 'Clio Sedan', 2009, 20.000)
carro_02 = Carro('Fiat', 'Uno', 2021, 35.000)


carro_01.Informacaocarro()
carro_02.Informacaocarro()
