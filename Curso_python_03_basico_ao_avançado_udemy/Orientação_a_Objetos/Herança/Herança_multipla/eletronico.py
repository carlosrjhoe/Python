from login  import LogFileMixin

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


class SmartPhone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._name} está ligado'
            self.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._name} está desligado'
            self.log_success(msg)
    