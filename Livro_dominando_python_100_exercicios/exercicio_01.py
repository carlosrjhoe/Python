class Calculadora:
    def __init__(self, fator_1, fator_2):
        self.fator_1 = fator_1
        self.fator_2 = fator_2
        
    def soma(self):
        return  self.fator_1 + self.fator_2 

    def subtracao(self):
        return self.fator_1 - self.fator_2

    def multiplicacao(self):
        return self.fator_1 * self.fator_2

    def divisao(self):
        return self.fator_1 / self.fator_2
        
    def resulmo(self):
        print(f'A soma dos números {self.fator_1} e {self.fator_2}')
        print(f'A subitração dos números {self.fator_1} e {self.fator_2}')
        print(f'A multiplicação dos números {self.fator_1} e {self.fator_2}')
        print(f'A divisão dos números {self.fator_1} e {self.fator_2}')

    
if __name__ == '__main__':
    num_1 = int(input('Digite o 1º número: '))
    num_2 = int(input('Digite o 2º número: '))
    resulmo()