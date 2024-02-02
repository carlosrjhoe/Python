from carros import Carro, Fabricante, Motor

fusca = Carro('Fusca')
volkswagem = Fabricante('Volkswagem')
motor = Motor(1.0)
fusca.fabricante = volkswagem
fusca.motor = motor
fusca.info()

clio = Carro('Clio')
renault = Fabricante('Renault')
motor = Motor(1.0)
clio.fabricante = renault
clio.motor = motor
clio.info()