"""Exercício 5.8 Escreva um programa que leia dois números. Imprima o resultado da
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 x 5 = 5
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4"""

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
x = 1
r = 0
while x <= num2:
    r = r + num1
    x = x + 1
print(f'{num1} x {num2} = {r}')
