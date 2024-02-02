class Carro:
    def __init__(self, name):
        self.name = name
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, value):
        self._motor = value

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, value):
        self._fabricante = value

    def info(self):
        print(f'Nome: {self.name}\nMotor: {self.motor.name}\nfabricante: {self.fabricante.name}')

class Motor:
    def __init__(self, name):
        self.name = name

class Fabricante:
    def __init__(self, name):
        self.name = name

        