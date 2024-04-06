"""Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
casa a comprar dividido pelo número de meses a pagar."""

valor_casa = float(input('Nos informe o valor da casa: '))
salario = float(input('Informe seu salario: '))
anos = float(input('Informe quantos anos gostaria de pagar o empréstimo: '))

meses = int(anos * 12)
prestacao = valor_casa / meses
parcela_minimo = salario * 0.3

if prestacao < parcela_minimo:
    print(f'Salário: \t\tR$ {salario:.2f}')
    print(f'Prestação: \t\tR$ {prestacao:.2f}')
    print(f'30% do salário: \tR$ {parcela_minimo:.2f}')
    print(f'Emprestimo APROVADO...')
else:
    print(f'Emprestimo NEGADO...')