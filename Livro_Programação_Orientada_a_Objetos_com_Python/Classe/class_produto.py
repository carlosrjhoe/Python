class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        percent_desconto = self.preco - (self.preco*(percentual/100))
        return percent_desconto

    @property
    def preco(self):
        return self.preco_valido

    @preco.setter
    def preco(self, valor):
        """se o valor da instância for do tipo str, valor será convertido para float assim como os caracteres desnecessários serão removidos."""
        if isinstance(valor, str):
            valor = float(valor.replace('R$',''))
            self.preco_valido = valor
    
if __name__ == '__main__':
    produto_01 = Produto('Processador', '370')
    print(f'Preço original: {produto_01.preco:.2f}')
    print(f'Preço com desconto: {produto_01.desconto(15):.2f}')

    produto_02 = Produto('Placa mãe', 'R$450')
    print(f'Preço original: {produto_02.preco:.2f}')
    print(f'Preço com desconto: {produto_02.desconto(20):.2f}')