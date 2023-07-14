"""Implemente um algoritmo de busca binária:"""

def busca_binaria(lista, busca):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        valor_meio = lista[meio]

        if valor_meio == busca:
            return meio
        elif valor_meio < busca:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1
    
if __name__ == "__main__":
    lista = [1,3,4,6,8,9,11,14,15]
    busca = 16
    print(f'Lista: {lista}')
    print(f'Valor {busca}, encontrado na posição {busca_binaria(lista, busca)}' if busca_binaria(lista, busca) != -1 else f'Valor {busca} não encontrado.')