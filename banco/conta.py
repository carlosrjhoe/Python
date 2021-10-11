from conta import Conta

class Conta:

    def __init__(Self, numero, titular, saldo, limite):
        print(f'Contruido objeto... {Self}')
        Self.numero = numero
        Self.titular = titular
        Self.saldo = saldo
        Self.limite = limite

# conta = Conta(321, 'Carlos', 100.0, 1000.0) 

def extrato(Self):
    print(f'Saldo de {Self.saldo} do titular {Self.titular}')

def deposita(Self,valor):
    Self.saldo += Valor

def saca(Self, valor):
    Self.saldo -= valor