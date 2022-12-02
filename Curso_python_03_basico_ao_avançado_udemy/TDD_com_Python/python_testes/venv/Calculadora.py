class Calculadora:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def soma(self, num):
        return self.x + num


if __name__ == "__main__":
    soma = Calculadora
    print(f'{soma.soma(10, 20)}')