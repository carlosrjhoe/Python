from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, conta, agencia, saldo):
        self._conta = conta
        self._agencia = agencia
        self._saldo = saldo
        
    @property
    def conta(self):
        return self._conta
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        """ Verificar se o saldo é numérico """
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico')
        self._saldo = valor
        
    def depositar(self, valor):
        """ Verifica se o deposito é um valor numérico """
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numérico')
        self._saldo += valor
        self.detalhes()
    
    def detalhes(self):
        """ Informa detalhes da conta """
        print(f'Agencia: {self._agencia}')
        print(f'Conta: {self._conta}')
        print(f'Saldo: R${self._saldo:.2f}')
    
    @abstractmethod
    def sacar(self, valor):
        pass