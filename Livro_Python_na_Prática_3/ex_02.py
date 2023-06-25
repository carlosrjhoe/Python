"""Crie uma lista de números inteiros e, em seguida, imprima os números em ordem crescente e decrescente no console:"""

def crescente(lista):
    num_crescente = sorted(lista)
    return num_crescente

def decrescente(lista):
    num_decrescente = sorted(lista, reverse=True)
    return num_decrescente

def inf_listas(crescente, decrescente, lista):
    print(f'Números em ordem crescente: {crescente(lista)}\nNúmeros em ordem decrescente: {decrescente(lista)}')

if __name__ == "__main__":
    lista = [21,43,24,1,34,12,76,9,21,54]
    crescente(lista)
    decrescente(lista)
    inf_listas(crescente, decrescente, lista)
    
    #>>> Números em ordem crescente: [1, 9, 12, 21, 21, 24, 34, 43, 54, 76]
    #>>> Números em ordem decrescente: [76, 54, 43, 34, 24, 21, 21, 12, 9, 1]