class Carro:
    
    def __init__(self, marca,modelo, ano, cor, valor):
        self.texto = 'Exercicio estrutura de molde(Orientação a Objetos)'
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.valor = valor
        
    def cabecalho(self):
        print(f'{"#"*len(self.texto)}')
        print(f'{self.texto.center(len(self.texto))}')
        print(f'{"#"*len(self.texto)}')
        
        
    def descricao(self):
        print(f'Marca: \t\t\t{self.marca}\nModelo: \t\t{self.modelo}\nAno Fabricação: \t{self.ano}\nCor: \t\t\t{self.cor}\nValor: \t\t\tR${self.valor:.3f}')
        print(f'{"#"*len(self.texto)}')
        
    
        