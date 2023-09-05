class Conta():
    # Define a classe
    def __init__(self, numero, titular, saldo, limite):
        # Define a função construtora da classe com atributos
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

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
    
    def sacar(self, valor):
        # Metodo sacar
        self.__saldo -= valor
    
    def depositar(self, valor):
        # Metodo depositar
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        msg = f'Transferindo R${valor:.2f} para {destino.__titular.title()}'
        return msg