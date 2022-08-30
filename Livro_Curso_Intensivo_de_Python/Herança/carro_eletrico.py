from carro import Carro, Bateria

class Carro_eletrico(Carro):
    
    def __init__(self, tipo, modelo, ano):
        super().__init__(tipo, modelo, ano)
        self.bateria = Bateria()

    def capacidade_bateria(self):
        print(f'{self.bateria.descricao_bateria()}')
    
    def encher_tanque_gasolina(self):
        print('Este carro não precisa de um tanque de gasolina.')
        
        
carro_neto = Carro_eletrico('tesla', 'fuderozo', 2022)
carro_neto.bateria.get_alcance()



