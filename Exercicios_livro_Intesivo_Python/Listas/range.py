numeros_impares = []
numeros_pares = []

for numero in range(1, 20+1):
    if numero % 2 == 0:
        numeros_pares.append(numero**2)
    elif numero % 2 != 0:
        numeros_impares.append(numero**2)

print(f'Números ímpares: {numeros_impares}')
print(f'Números pares: {numeros_pares}')