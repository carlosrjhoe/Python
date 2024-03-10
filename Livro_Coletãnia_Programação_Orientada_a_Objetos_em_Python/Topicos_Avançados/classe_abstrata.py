from abc import ABC, abstractmethod
from math import pi

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return pi * pow(self.raio, 2)

    def perimetro(self):
        return 2 * pi * self.raio

if __name__ == "__main__":
    objeto_1 = Circulo(6)
    print(f'Área {objeto_1.area():.3f}')
    print(f'Perimetro {objeto_1.perimetro():.3f}')