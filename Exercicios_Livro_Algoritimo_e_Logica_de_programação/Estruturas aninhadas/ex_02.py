""" Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada """

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

operacao = int(input('Qual operação você deseja fazer[1-SOMA, 2-SUBTRAÇÃO, 3-MULTIPLICAÇÃO, 4-DIVISÃO]? '))

if operacao == 1:
    print(f'A soma de {num1} com {num2} = {num1+num2}')
elif operacao == 2:
    print(f'A subtração de {num1} com {num2} = {num1-num2}')
elif operacao == 3:
    print(f'A multiplicação de {num1} com {num2} = {num1*num2}')
elif operacao == 4:
    print(f'A divisão de {num1} com {num2} = {num1/num2}')
else:
    print('Operação invalida, digite um valor entre [1 e 5]')

