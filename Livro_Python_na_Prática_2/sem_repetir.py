"""A partir da lista lista=['a', 'a', 'a', 'b', 'c', 'k', 'a', 1, 2, 3, 4, 'j', 'l', 'm'] gere uma nova lista porém sem elementos repetidos.
"""

def retornarListaSemRepeticoes(lista):
    lista_2 = list(set(lista))
    return lista_2

def mostraListas(lista, retornarListaSemRepeticoes):
    print(f'Lista original: \n{lista}')
    print(f'Lista verificada: \n{retornarListaSemRepeticoes(lista)}')

if __name__ == '__main__':
    lista = ['a', 'a', 'a', 'b', 'c', 'k', 'a', 1, 2, 3, 4, 'j', 'l', 'm']
    mostraListas(lista, retornarListaSemRepeticoes)