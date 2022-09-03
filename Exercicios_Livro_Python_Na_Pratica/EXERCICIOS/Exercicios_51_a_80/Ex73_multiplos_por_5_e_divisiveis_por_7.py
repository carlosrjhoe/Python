from ntpath import join


lista = [] # Lista vazia

for numero in range(2000, 2201):
    if (numero % 7 == 0) and (numero % 5 != 0):
        lista.append(numero)

print(f'{lista}')