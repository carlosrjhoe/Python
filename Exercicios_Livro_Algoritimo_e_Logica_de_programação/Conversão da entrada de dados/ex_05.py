''' Exercício 3.10 Faça um programa que calcule o aumento de um salário. Ele deve
solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
e do novo salário '''

salario = float(input('Informe seu salario: '))
porcentagem = float(input('Informe a porcentagem do almento: '))
aumento = salario * porcentagem / 100

print(f'O aumento será de R${aumento:.2f}')
print(f'E seu novo salario será de R${salario+aumento:.2f}')