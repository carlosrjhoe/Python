class Caneta:

    def __init__(self, cor):
        self._cor = cor
        self._cor_tampa = None
        

    @property
    def cor(self):
        print('PROPETY')
        return self._cor

    @cor.setter
    def cor(self, value):
        print(f'ESTOU NO SETTER {value}')
        self._cor = value

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, value):
        self._cor_tampa = value

    def mostrar(caneta):
        return caneta.cor

caneta = Caneta('Azul')
# caneta.cor = 'Rosa'
caneta.cor_tampa = 'Marron'
print(caneta.cor)
print(caneta.cor_tampa)