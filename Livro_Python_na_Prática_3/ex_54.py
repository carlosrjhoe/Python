"""Implemente um algoritmo de ordenação quick sort:"""

def ordena(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < pivo]
    meio = [x for x in lista if x == pivo]
    direita = [x for x in lista if x > pivo]

    return ordena(esquerda) + meio + ordena(direita)
    
if __name__ == "__main__":
    lista = [3,6,8,10,1,2,4,1,9]
    print(f'Array desordenado: {lista}')
    print(f'Array ordenado: {ordena(lista)}')