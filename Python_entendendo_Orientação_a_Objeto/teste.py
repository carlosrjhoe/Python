def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def depositar(conta, valor):
    conta['saldo'] += valor

def sacar(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f'Saldo: {conta["saldo"]}')
    

if __name__ == '__main__':
    conta_01 = cria_conta(123, 'Carlos', 1000, 1100)
    extrato(conta_01)
    depositar(conta_01, 1000)
    extrato(conta_01)
    sacar(conta_01, 500)
    extrato(conta_01)