"""Reorganize os elementos da lista [-1, 6, -9, -8, 4, 0, -3, 2, 7, 1, 8, -2] em ordem crescente e a partir da mesma, gere duas novas listas, uma contendo apenas os elementos negativos e outra contendo apenas os elementos positivos. Por fim, exiba em tela o conteúdo da lista original e das 3 novas listas geradas.
"""
def listaOriginal(lista):
    print(f'Lista original: {lista}')
    return

def listaOrganizada(lista):
    lista_1 = [x for x in lista if x < 0] + [x for x in lista if x >= 0]
    print(f'Lista organizada: {lista_1}')
    return

def listaComNumerosNegativos(lista):
    lista_2 = [x for x in lista if x < 0]
    print(f'Lista com números negativos: {lista_2}')
    return

def listaComNumerosPositivos(lista):
    lista_3 = [x for x in lista if x > 0]
    print(f'Lista com números positivos: {lista_3}')
    return

if __name__ == '__main__':
    lista = [1,-2,3,-4,5,0,-6,7,-8,9,-10,11,]
    listaOriginal(lista)
    listaOrganizada(lista)
    listaComNumerosNegativos(lista)
    listaComNumerosPositivos(lista)