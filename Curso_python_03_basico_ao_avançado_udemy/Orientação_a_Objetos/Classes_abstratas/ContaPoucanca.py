from Conta import Conta

class ContaPoupanca(Conta):
    """ Classe apartir da herança de Conta """
    def sacar(self, valor):
        if self._saldo < valor:
            print(f'Saldo insuficiente.')
            return
        self._saldo -= valor
        self.detalhes()