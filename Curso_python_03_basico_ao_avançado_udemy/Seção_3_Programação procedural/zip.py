lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9, 10]

soma_lista = list(zip(lista_1, lista_2))
print(soma_lista)

soma_lista = [x + y for x, y in zip(lista_1, lista_2)]
print(soma_lista)
