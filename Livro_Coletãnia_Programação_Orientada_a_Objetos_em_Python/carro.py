class Carro:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

class Corsa(Carro):
    pass

class Gol(Carro):
    pass

class Carro_gasolina(Carro):
    def __init__(self, tipo_gasolina=True, tipo_alcool=False):
        self.tipo_gasolina = tipo_gasolina
        self.tipo_alcool = tipo_alcool

class Jeep(Carro_gasolina):
    pass