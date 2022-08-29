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
            

class Bateria():
    
    def __init__(self, tamanho_da_bateria=100):
        self.tamanho_da_bateria = tamanho_da_bateria
        
    def descricao_bateria(self):
        print(f'Este carro tem {(str(self.tamanho_da_bateria))}-kwh')