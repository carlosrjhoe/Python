# numeros = [numero**2 for numero in range(1, 11)]
contagem = []

numero_impar = []
for numero in range(0, 11):
    numero_impar.append(numero**3)

print(f'{numero_impar}')

numero_elevado_ao_cubo = [numero**3 for numero in range(0, 11)]
numero_elevado_ao_quadrado = [numero**2 for numero in range(0, 11)]

print(f'{numero_elevado_ao_cubo}')
print(f'{numero_elevado_ao_quadrado}')