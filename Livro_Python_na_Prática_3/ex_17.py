"""17 – Crie uma classe base Calculadora com um método calcula( ) que retorna 0. Crie subclasses Adicao, Subtracao, Multiplicacao e Divisao que herdam de Calculadora. Sobrescreva o método calcula( ) nas subclasses para realizar as operações matemáticas correspondentes. Instancie objetos das subclasses e teste o método calcula( ) em diferentes operações:"""

class Calculadora:
    def calcular(self):
        return 0

class Adicao(Calculadora):
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def calcular(self):
        return f'{self.num_1} + {self.num_2} = {self.num_1 + self.num_2}'

class Subtracao(Calculadora):
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def calcular(self):
        return f'{self.num_1} - {self.num_2} = {self.num_1 - self.num_2}'

class Multiplicacao(Calculadora):
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def calcular(self):
        return f'{self.num_1} * {self.num_2} = {self.num_1 * self.num_2}'

class Divisao(Calculadora):
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def calcular(self):
        return f'{self.num_1} / {self.num_2} = {self.num_1 / self.num_2}'

if __name__ == '__main__':
    adicao = Adicao(5, 10)
    subtracao = Subtracao(20, 8)
    multiplicao = Multiplicacao(3, 7)
    divisao = Divisao(15, 3)    

    print(f'Adição: {adicao.calcular()}')    
    print(f'Subtração: {subtracao.calcular()}')    
    print(f'Multiplicação: {multiplicao.calcular()}')    
    print(f'Divisão: {divisao.calcular()}')

    # >>> Adição: 5 + 10 = 15
    # >>> Subtração: 20 - 8 = 12
    # >>> Multiplicação: 3 * 7 = 21
    # >>> Divisão: 15 / 3 = 5.0