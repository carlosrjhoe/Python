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
            
            
class Carro_eletrico(Carro):
    
    def __init__(self, tipo, modelo, ano):
        super().__init__(tipo, modelo, ano)
        self.carga_bateria = 70
        
    def capacidade_bateria(self):
        print(f'Este carro tem {self.carga_bateria}-kwh')
        pass
        
carro_neto = Carro_eletrico('tesla', 'fuderozo', 2022)

print(carro_neto.descricao_carro())
carro_neto.capacidade_bateria()



