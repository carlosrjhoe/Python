class Caixa:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def __add__(self, other):
        largura_1 = self.largura + other.largura
        altura_01 = self.altura + other.altura
        return Caixa(largura_1, altura_01)
    
    def __repr__(self):
        return f"<class'Caixa({self.largura}, {self.altura})'>"


if __name__ == '__main__':
    caixa_01 = Caixa(10, 10)
    caixa_02 = Caixa(10, 20)
    caixa_03 = caixa_01 + caixa_02
    print(f'{caixa_03}')
    