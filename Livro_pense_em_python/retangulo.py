class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def perimetro(self):
        return self.largura * 2 + self.altura * 2


if __name__ ==  '__main__':
    caixa = Retangulo(100, 200)
    caixa_1 = Retangulo(300, 400)
    print(f'Perimetro da caixa = {caixa.perimetro()}cm')
    print(f'Perimetro da caixa_1 = {caixa_1.perimetro()}cm')