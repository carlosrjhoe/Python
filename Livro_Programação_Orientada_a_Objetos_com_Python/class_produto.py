class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        percent_desconto = self.preco - (self.preco*(percentual/100))
        return percent_desconto
    
if __name__ == '__main__':
    produto_01 = Produto('Processador', 370)
    print(f'{produto_01.preco}')
    print(f'{produto_01.desconto(15)}')

    produto_02 = Produto('Placa mãe', 450)
    print(f'{produto_02.preco}')
    print(f'{produto_02.desconto(20)}')