"""Exercício 8.1 Escreva uma função que retorne o maior de dois números.
Valores esperados:
máximo(5,6) == 6
máximo(2,1) == 2
máximo(7,7) == 7"""

def maximo(a,b):
    if a > b:
        return a
    else:
        return b
    
print(f'Máximo de [5,9] é: {maximo(5,9)}')
print(f'Máximo de [10,4] é: {maximo(10,4)}')
print(f'Máximo de [48,35] é: {maximo(48,35)}')