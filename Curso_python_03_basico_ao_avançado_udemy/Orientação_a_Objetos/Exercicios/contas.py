from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'DEPOSITANDO R${valor:.2f}')

    def detalhes(self, msg=None):
        return f'O seu saldo: R${self.saldo:.2f} - {msg}'