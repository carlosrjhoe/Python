"""Exercício 4.3 Escreva um programa que leia três números e que imprima o maior
e o menor"""

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite um número: '))
num_3 = int(input('Digite um número: '))

maior = 0
if num_1 > num_2 and num_1 > num_3:
    maior = num_1
if num_2 > num_1 and num_2 > num_3:
    maior = num_2
if num_3 > num_1 and num_3 > num_2:
    maior = num_3
print(f'{maior}')