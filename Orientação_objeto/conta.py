from _typeshed import Self
from conta import Conta

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print(f'Contruido objeto... {self}')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

conta = Conta(321, 'Carlos', 100.0, 1000.0)