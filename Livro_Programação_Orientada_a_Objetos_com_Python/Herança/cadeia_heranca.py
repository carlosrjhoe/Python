from heranca_simples import Carro

class Gasolina(Carro):
    """Cadeia de herança"""
    def __init__(self, tipo_gasolina=True, tipo_alcool=False):
        self.tipo_gasolina = tipo_gasolina
        self.tipo_alcool = tipo_alcool

class Jeep(Gasolina):
    """Cadeia de herança"""
    pass

if __name__ == '__main__':
    carro_01 = Jeep()
    print(f'{carro_01.tipo_gasolina}')
    print(f'{carro_01.tipo_alcool}')