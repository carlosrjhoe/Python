from carro import Carro

class Carro_eletrico(Carro):
    
    def __init__(self, tipo, modelo, ano):
        super().__init__(tipo, modelo, ano)
        self.carga_bateria = 70
        
    def capacidade_bateria(self):
        print(f'Este carro tem {self.carga_bateria}-kwh')
        pass
    
    def encher_tanque_gasolina(self):
        print('Este carro não precisa de um tanque de gasolina.')
        pass
        
carro_neto = Carro_eletrico('tesla', 'fuderozo', 2022)

print(carro_neto.descricao_carro())
carro_neto.capacidade_bateria()



