class Conta():
    # Define a classe
    def __init__(self, numero, titular, saldo, limite):
        # Define a função construtora da classe com atributos
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        # Metodo depositar
        self.saldo += valor
    
    def sacar(self, valor):
        # Metodo sacar
        self.saldo -= valor
    
    def extrato(self):
        # Metodo extrato
        return f'Titular: {self.titular} - Saldo: {self.saldo}'