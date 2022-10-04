from Conta import Conta

class ContaCorrente(Conta):
    """ Classe a partir de herança da Conta e colocando mais um atributo(limite) """
    def __init__(self, conta, agencia, saldo, limite=100):
        super().__init__(conta, agencia, saldo)
        self._limite = limite
            
    @property
    def limite(self):
        return self._limite    
    
    def sacar(self, valor):
        if (self._saldo + self._limite) < valor:
            print(f'Saldo insuficiente.')
            return
        self._saldo -= valor
        self.detalhes()