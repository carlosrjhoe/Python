class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property 
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor
        
    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
fusca.fabricante = 'volkswagen'
fusca.motor = '1.0'
print(f'{fusca.nome}, {fusca.fabricante}, {fusca.motor}')

focus = Carro('Focus')
focus.fabricante = 'Ford'
focus.motor = '1.6'
print(f'{focus.nome}, {focus.fabricante}, {focus.motor}')

fiat = Carro('Uno')
fiat.fabricante = 'Fiat'
fiat.motor = fusca.motor
print(f'{fiat.nome}, {fiat.fabricante}, {fiat.motor}')




