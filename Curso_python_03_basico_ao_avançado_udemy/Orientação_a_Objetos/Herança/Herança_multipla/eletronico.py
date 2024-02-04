class Eletronico:
    def __init__(self, name):
        self._name = name
        self._ligado = False


    def ligar(self):
        if not self._ligado: 
            self._ligado = True 
            print('ligado')

    def desligar(self):
        if not self._ligado:
            self._ligado = False


class SmartPhone(Eletronico):
    def ligar(self):
        super().ligar()

    def desligar(self):
        super().desligar()
    