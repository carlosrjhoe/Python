"""Exercício 5.15 Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade
comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto

Código Preço
    1 0,50
    2 1,00
    3 4,00
    5 7,00
    9 8,00
"""
codigo = int(input('Digite o código do produto: '))
quantidade = int(input('Digite a quantidade: '))

if codigo == 1:
    preco = 0.50
elif codigo == 2:
    preco = 1.00
elif codigo == 3:
    preco = 4.00
elif codigo == 5:
    preco = 7.00
elif codigo == 9:
    preco = 8.00
print(f'Total do produto solicitado R${quantidade*preco:.2f}')


