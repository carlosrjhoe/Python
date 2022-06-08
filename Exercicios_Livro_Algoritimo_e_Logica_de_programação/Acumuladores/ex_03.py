"""Exercício 5.13 Escreva um programa que pergunte o valor inicial de uma dívida e
o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número
de meses para que a dívida seja paga, o total pago e o total de juros pago"""

divida = float(input('Dívida: '))
taxa = float(input('Juros: '))
pagamento = float(input('Pagamento mensal: '))

mes = 1
if divida * (taxa/100) > pagamento:
    print('Sua dívida nunca será paga. Juros são superiores ao pagamento mensal.')
else:
    saldo = divida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa/100
        saldo = saldo + juros  - pagamento
        juros_pago = juros_pago + juros
        print(f'Saldo da dívisa do mês {mes} é de R${saldo:.2f}')
        mes = mes + 1
    print(f'Para pagar uma dívida de R${divida:.2f}, a {taxa:.2f}% de juros.')
    print(f'Você precisará de {mes-1} meses, pagando um total de R${juros_pago:.2f} de juros.')
    print(f'No ultimo mês, você teria saldo de R${saldo:.2f} a pagar.')