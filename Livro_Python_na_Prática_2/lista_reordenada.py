'''Dada a lista ['python', 'java', 'php', 'c++', 'c#', 'javascript', 'kotlin', 'r'], retorne duas novas listas geradas a partir da lista inicial, com seus elementos reordenados de forma aleatória, porém reproduzível.
'''

import random

def organizar_lista_01(lista):
    random.seed(32)
    random.shuffle(lista)
    return lista

def organizar_lista_02(lista):
    random.seed(42)
    random.shuffle(lista)
    return lista

if __name__ == '__main__':
    linguagens = ['python', 'java', 'php', 'c++', 'c#', 'javascript', 'kotlin', 'r']
    print(f'{organizar_lista_01(linguagens)}')
    print(f'{organizar_lista_02(linguagens)}')