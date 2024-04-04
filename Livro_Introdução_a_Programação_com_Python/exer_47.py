"""Exercício 4.4 Escreva um programa que pergunte o salário do funcionário e calcule
o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
10%. Para os inferiores ou iguais, de 15%"""

salario = float(input('Informe seu salário: '))
SALARIO_BASE = 1.250
BASE_15 = 0.15
BASE_10 = 0.10

if salario < SALARIO_BASE:
    print(f'Salário de R$ {salario:.2f} terá aumento de 0.15%, passará a ser de R$ {(salario*BASE_15)+salario:.2f} um aumento de R$ {(salario*BASE_15):.2f}')
if salario > SALARIO_BASE:
    print(f'Salário de R$ {salario:.2f} terá aumento de 0.10%, passará a ser de R$ {(salario*BASE_10)+salario:.2f} um aumento de R$ {(salario*BASE_10):.2f}')