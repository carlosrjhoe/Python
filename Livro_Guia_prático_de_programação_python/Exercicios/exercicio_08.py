'''João tem de seu salário, um desconto de 10% de imposto. Vamos calcular o valor desse imposto? Escreva um código que: 
    1) Solicita o valor do salário. 
    2) Calcula o valor do imposto de 10%. 
    3) Imprima o resultado.
'''

salario = float(input('Valor do salário: '))
imposto = lambda salario, imposto=0.10: salario * imposto
print(f'O valor do imposto: R${imposto(salario):.2f}')