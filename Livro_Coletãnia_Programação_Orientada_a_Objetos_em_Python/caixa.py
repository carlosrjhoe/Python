class Caixa:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def __add__(self, other):
        largura_total = self.largura + other.largura
        altura_tital = self.altura + other.altura
        return Caixa(largura_total, altura_tital)

    def __repr__(self):
       return f'<class "Caixa({self.largura, self.altura})"' 