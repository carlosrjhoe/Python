import re

class Estoque:
    def __init__(self, item, preco):
        self.item = item
        self.preco = preco

    def aplica_desconto(self, percentual) -> float:
        self.preco = self.preco - (self.preco * (percentual / 100))
        return

    @property
    def preco(self) -> float:
        return self._preco

    @preco.setter
    def preco(self, value) -> float:
        if isinstance(value, str):
            value == re.search(r'\d+', value)
        self._preco = value

if __name__ == "__main__":
    calcado001 = Estoque('Tenis Adidas 41', 299.0)
    calcado001.aplica_desconto(20)
    print(f'{calcado001.item} // Valor com desconto: R${calcado001.preco:.2f}')