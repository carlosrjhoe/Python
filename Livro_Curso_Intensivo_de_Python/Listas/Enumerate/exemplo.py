"""Listagem 6.31 – Impressão de índices sem usar a função enumerate"""

lista = [1,2,3,4,5]
# x = 0
# for i in lista:
#     print(f'{x} - {i}')
#     x += 1
    
""" Listagem 6.32 – Impressão de índices usando a função enumerate"""

for x, i in enumerate(lista):
    print(f'{x} - {i}')