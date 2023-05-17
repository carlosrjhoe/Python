"""
    1 – Na frase “A Radiologia é a ciência que estuda a anatomia por meio de exames de imagem.” realize a contagem dos caracteres de sua composição, retornando quais os 6 caracteres mais recorrentes, e quantas vezes os mesmos aparecem na frase acima:
"""

from collections import Counter

def recorrecia_letras(frase):
    a2,a3,a4,a5,a6 = Counter(frase).most_common(5)

    print(f'A letra mais recorrente é: {a2[0].upper()}, e se repete {a2[1]} vezes.')
    print(f'A letra mais recorrente é: {a3[0].upper()}, e se repete {a3[1]} vezes.')
    print(f'A letra mais recorrente é: {a4[0].upper()}, e se repete {a4[1]} vezes.')
    print(f'A letra mais recorrente é: {a5[0].upper()}, e se repete {a5[1]} vezes.')
    print(f'A letra mais recorrente é: {a6[0].upper()}, e se repete {a6[1]} vezes.')

if __name__ == '__main__':
    frase = 'A Radiologia é a ciência que estuda a anatomia por meio de exames de imagem.'
    recorrecia_letras(frase)