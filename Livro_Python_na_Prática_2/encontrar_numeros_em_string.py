"""Crie um simples mecanismo que lê um determinado texto, nesse caso “Python 3.9”, retornando ao usuário a quantidade de números encontrados no texto e que números são estes, ordenados em ordem posicional (na exata ordem em que foram identificados no texto).
"""

import re

# def mostrarInformacao(encontarNumeros, texto):
#     print(f'Foram encontrados {len(encontarNumeros())} números no texto {texto}.')
#     print(f'Os números são {encontarNumeros} e {}, respectivamente.')

def encontarNumeros(texto):
    numeros = re.findall(pattern=r'\d',string=texto)
    return numeros

if __name__ == '__main__':
    texto = 'Python 3.9'
    print(encontarNumeros(texto))
