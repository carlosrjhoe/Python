"""11 - Some os valores das variáveis num1 e num2: Sendo num1 = 52 e num2 = 106. Por fim exiba em tela o resultado da soma.

Feltrin, Fernando. Python na Prática: Aprenda Python Através de Exercícios Comentados (p. 27). Uniorg. Edição do Kindle. """

class Calculadora: 
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        

    def soma(self):
        return f"{self.num_1 + self.num_2}"

    def subratacao(self):
        return f"{self.num_1 - self.num_2}"

    def multiplicacao(self):
        return f"{self.num_1 * self.num_2}"

    def divisao(self):
        return f"{self.num_1 / self.num_2}"


if __name__ == '__main__':
    conta = Calculadora(2, 4)
    print(f"Soma = {conta.soma()}")
    print(f"Subtração = {conta.subratacao()}")
    print(f"Multiplicação = {conta.multiplicacao()}")
    print(f"Divisão = {conta.divisao()}")