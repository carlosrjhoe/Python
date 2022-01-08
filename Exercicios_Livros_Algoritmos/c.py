from math import pi
from math import pow

def volume():
    return pi * pow(r, 2) * alt

r = float(input('Digite o raio do cilindo: '))
alt = int(input('Digite a altura do cilindro: '))
print(f'O volume é igual a {volume():.1f}cm³')

