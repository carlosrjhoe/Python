""" Listagem 6.24 – Impressão de todos os elementos da lista com for"""

lista = [1,2,3,4,5,6,7,8,9]

procuro = int(input('Digite um numero: '))
for numero in lista:
    if procuro == numero:
        print('Número encontrado!')
        break
    else:
        print('Número não encontrado.')