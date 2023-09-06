class Conta():
    # Define a classe
    def __init__(self, numero, titular, saldo, limite):
        # Define a função construtora da classe com atributos
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}

    def extrato(self):
        return f'Nome: {self.__titular.title()} - Saldo: R${self.__saldo}'

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular.title()
        
    @property
    def saldo(self):
        # Metodo extrato
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def __pode_sacar(self, valor):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor <= valor_disponivel_a_sacar
    
    def sacar(self, valor):
        # Metodo sacar
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor R${valor:.2f} passou o limite.')
    
    def depositar(self, valor):
        # Metodo depositar
        self.__saldo += valor
        
    def __pode_transferir(self, valor):
        valor_disponivel_a_transferir = self.__saldo + self.__limite
        return valor <= valor_disponivel_a_transferir

    def transferir(self, valor, destino):
        if (self.__pode_transferir(valor)):
            self.sacar(valor)
            destino.depositar(valor)
        msg = f'Transferindo R${valor:.2f} para {destino.__titular.title()}'
        return msg
