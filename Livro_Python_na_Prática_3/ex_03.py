"""Crie duas listas de números inteiros e, em seguida, crie uma terceira lista que contenha apenas os elementos comuns das duas listas (sem duplicatas) e exiba em tela o conteúdo desta terceira lista:"""

def soma_listas(lista_01, lista_02):
    lista_comum = list(set(lista_01) & set(lista_02))
    return f'Elementos comuns: {lista_comum}'

if __name__ == "__main__":
    lista_01 = [1, 3, 5, 7, 9, 11, 13]
    lista_02 = [2, 4, 5, 6, 7, 8, 9, 12, 13, 14]
    print(soma_listas(lista_01, lista_02))

    #>>> Elementos comuns: [9, 13, 5, 7]