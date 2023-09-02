class Conta():
    # Define a classe
    def __init__(self, numero, titular, saldo, limite):
        # Define a função construtora da classe com atributos
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        # Metodo depositar
        self.__saldo += valor
    
    def sacar(self, valor):
        # Metodo sacar
        self.__saldo -= valor
    
    def extrato(self):
        # Metodo extrato
        return f'Titular: {self.__titular.title()} - Saldo: {self.__saldo}'