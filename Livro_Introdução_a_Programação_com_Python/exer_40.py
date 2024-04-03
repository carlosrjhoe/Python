"""Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve
solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
e do novo salário"""

salario = float(input('Informe o salário: '))
porcentagem = float(input('Informe o aumento em porcentagem: '))

aumento = salario * porcentagem / 100
novo_salario = aumento + salario

print(f'Novo salário: R$ {novo_salario:.2f}')