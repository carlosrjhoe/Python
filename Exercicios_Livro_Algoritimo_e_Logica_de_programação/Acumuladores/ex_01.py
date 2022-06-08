"""Exercício 5.11 Escreva um programa que pergunte o depósito inicial e a taxa de
juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período"""

deposito_inicial = float(input('Digite o valor do deposito em R$: '))
taxa_de_juros = int(input('Qual a taxa de juros: '))

saldo = deposito_inicial
mes = 1

while mes <= 24:
    saldo = saldo + (saldo * (taxa_de_juros / 100))
    print(f'Saldo do mês {mes}, é de R${saldo:.2f}')
    mes = mes + 1
print(f'Saldo total é R${saldo:.2f}')
print(f'O ganho obtido com os juros foi de R${saldo-deposito_inicial:.2f}')
