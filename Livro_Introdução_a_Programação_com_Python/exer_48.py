"""Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada"""

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))
operacao = input('Escolha qual operação matemática gostaria de realizar [+, -, * ou /]: ')

if operacao == '+':
    resultado = num_1 + num_2
elif operacao == '-':
    resultado = num_1 - num_2
elif operacao == '*':
    resultado = num_1 * num_2
elif operacao == '/':
    resultado = num_1 / num_2
print(f'{num_1} {operacao} {num_2} = {resultado}')
    