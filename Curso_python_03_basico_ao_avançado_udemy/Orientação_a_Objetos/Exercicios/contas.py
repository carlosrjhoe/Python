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

    def detalhes(self, msg=''):
        print(f'O seu saldo: R${self.saldo:.2f} - {msg}')

class ContaPoupanca(Conta):
    
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'SACANDO R${valor:.2f}')
            return self.saldo
        print(f'Não foi possivel sacar')
        self.detalhes(f'SAQUE NEGADO')