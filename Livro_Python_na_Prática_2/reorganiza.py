"""Considerando a lista [11, 22, 33, 44, 55, 66, 77, 88, 99, 'X'], reorganize seus elementos de forma a inverter o primeiro e o último elemento de posição, sem alterar a ordem dos demais elementos.
"""

lista = [11,22,33,44,55,66,77,88,99,'X']
print(f'Lista original: {lista}')

temp = lista[0]
lista[0] = lista[-1]
lista[-1] = temp

print(f'Lista alterada: {lista}')