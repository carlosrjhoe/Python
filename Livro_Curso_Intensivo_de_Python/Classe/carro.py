class Carro():
    
    def __init__(self, tipo, modelo, ano):
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.odometro = 1000
        
    def descricao_carro(self):
        tipagem_carro = f'Tipo: {self.tipo.title()}\nModelo: {self.modelo.title()}\nFabricação: {self.ano}'
        return tipagem_carro
    
    def ler_odometro(self):
        print(f'O carro tem {self.odometro:.2f}km rodados.')
        
    def atualizar_odometro(self, kilometragem):
        if kilometragem >= self.odometro:
            self.odometro = kilometragem
        else:
            print('Você não pode reverter um odômetro!')
    
    
meu_carro = Carro('utilitário', 'spacefox', 2000)


print(meu_carro.descricao_carro())
meu_carro.atualizar_odometro(9000)
meu_carro.ler_odometro()
meu_carro.atualizar_odometro(5000)
meu_carro.ler_odometro()
