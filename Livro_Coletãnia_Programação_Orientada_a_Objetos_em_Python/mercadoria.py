class Mercadoria:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carnes(Mercadoria):
    def __init__(self, tipo, peso):
        self.tipo = tipo
        self.peso = peso

class Utensilios:
    def __init__(self, espetos, carvao):
        self.espetos = espetos
        self.carvao = carvao

class KitChurrasco(Carnes, Utensilios):
    pass