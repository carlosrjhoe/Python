"""Listagem 5.11 – Soma de 10 números"""

# n = 1
# soma = 0
# while n < 10:
#     x = int(input(f'Digite o {n}° numero: '))
#     soma = soma + x
#     n = n + 1
# print(f'Soma: {soma}')

""" Listagem 5.12 – Cálculo de média com acumulador"""

x = 1
soma = 0
while x <= 5:
    n = int(input(f'{x} Digite o número:'))
    soma = soma + n
    x += 1
print(f'Média: {soma/5:.2f}')