"""Exercício 4.3 Escreva um programa que leia três números e que imprima o maior
e o menor."""

lista = []

for i in range(3):
   numero = int(input('Digite um numero: '))
   lista.append(numero)

print(f'O maior é: {max(lista)}')
print(f'O menor é: {min(lista)}')
