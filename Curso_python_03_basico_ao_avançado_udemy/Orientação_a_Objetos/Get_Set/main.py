class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def informacao(self):
        print(f'Produto: {self.nome} Valor: R${self.preco:.2f}')
        
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))
        print(f'Desconto de {percentual}% Valor atual R${self.preco:.2f}\n')
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor.replace('A', '@')
    
    # Getter
    @property
    def preco(self):
        return self._preco
    
    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
            
        self._preco = valor

produto_01 = Produto('CAFÉ', '5')
produto_01.informacao()
produto_01.desconto(10)

produto_02 = Produto('SABAO', '7')
produto_02.informacao()
produto_02.desconto(25)