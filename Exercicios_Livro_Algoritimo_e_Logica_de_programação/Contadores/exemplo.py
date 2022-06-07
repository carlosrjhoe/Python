""" Listagem 5.6 – Impressão de 1 até um número digitado pelo usuário"""

# fim = int(input('Digite p último numero a imprimir: '))
# x = 1
# while x <= fim:
#     print(x)
#     x += 1

"""Listagem 5.7 – Impressão de números pares de 0 até um número digitado pelo usuário"""

fim = int(input('Digite o último numero a imprimir: '))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x += 1

