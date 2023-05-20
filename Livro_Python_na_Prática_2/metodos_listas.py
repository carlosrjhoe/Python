"""20 – Uma vez apresentada a lista x = [10, 12, 35], apresente ao menos 5 formas de retornar ao usuário a soma dos elementos dessa lista.
"""

lista = [10, 12, 35]

soma_1 = lista[0] + lista[1] + lista[2]
print(f'{soma_1}')

soma_2 = 0
for i in lista:
    soma_2 += i
print(f'{soma_2}')

soma_3 = sum([i for i in lista])
print(f'{soma_3}')

soma_4 = sum(lista)
print(f'{soma_4}')

num1, num2, num3 = lista
soma_5 = num1 + num2 + num3
print(f'{soma_5}')