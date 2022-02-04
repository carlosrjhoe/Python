class Computador:
    def __init__(self, marca, memoria):
        self.marca = marca
        self.memoria = memoria


    def Ligar(self):
        print('Ligado')

    def Desligar(self):
        print('Desligado')

    def ExibisImformação(self):
        print(self.marca, self.memoria)


computador_01 = Computador('Asus', '16gb')
computador_01.Ligar()
computador_01.Desligar()
computador_01.ExibisImformação()