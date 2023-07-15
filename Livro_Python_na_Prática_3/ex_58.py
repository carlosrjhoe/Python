"""Implemente uma função que identifique se um número é um quadrado perfeito:"""

import math

def quadrado_perfeito(numero):
    if numero < 0:
        return False

    raiz_quadrada = int(math.sqrt(numero))
    return raiz_quadrada * raiz_quadrada == numero

def informacao():
    numero = int(input('Digite um número: '))
    if quadrado_perfeito(numero):
        print(f'{numero} é um quadrado perfeito')
    else:
        print(f'{numero} não é um quadrado perfeito')
    


if __name__ == "__main__":
    informacao()