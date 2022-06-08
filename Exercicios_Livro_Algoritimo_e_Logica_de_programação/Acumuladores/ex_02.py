"""Exercício 5.12 Altere o programa anterior de forma a perguntar também o valor
depositado mensalmente. Esse valor será depositado no início de cada mês, e você
deve considerá-lo para o cálculo de juros do mês seguinte"""

deposito = float(input('Depósito inicial: '))
taxa = float(input('Taxa de juros: '))
investimento = float(input('Depósito mensal: '))

mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + investimento
    print(f'Slado do mes {mes}, é de R${saldo:.2f}')
    mes += 1
print(f'O ganho obtido com os juros foi de R${saldo-deposito:.2f}')