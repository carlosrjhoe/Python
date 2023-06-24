class Carro:
    def __init__(self, modelo, ano_fabricacao):
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao

    def inf(self):
        print(f'Modelo:{self.modelo}\nFabricação:{self.ano_fabricacao}')
    
class Chevrolet(Carro):
    """Herança simples: Se dá quando estruturalmente um objeto é outro objeto, no sentido de que ele literalmente herda todas características e funcionalidades do outro, para que o código fique mais enxuto."""
    pass

class Wolksvagem(Carro):
    """Herança simples"""
    pass

if __name__ == '__main__':
    carro_01 = Wolksvagem('gol', 1980)
    carro_02 = Chevrolet('corsa', 1978)
    carro_01.inf()
    carro_02.inf()