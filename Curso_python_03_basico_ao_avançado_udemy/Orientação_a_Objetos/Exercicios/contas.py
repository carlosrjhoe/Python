from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
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
        print(f'O seu saldo: R${self.saldo:.2f} {msg}')

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'SACANDO R${valor:.2f}')
            return self.saldo
        print(f'Não foi possivel sacar valor desejado.')
        self.detalhes(f'SAQUE DE R${valor:.2f} NEGADO')

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
        
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo =- self.limite
        
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'SACANDO R${valor:.2f}')
            return self.saldo
        
        print(f'Seu limite é {self.limite}')
        print(f'Não foi possivel sacar')
        self.detalhes(f'SAQUE NEGADO')