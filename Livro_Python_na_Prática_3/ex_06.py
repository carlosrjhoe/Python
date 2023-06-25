"""6 – Dadas duas listas de números, use a função zip( ) para criar uma nova lista de tuplas contendo os elementos correspondentes das listas originais. Exiba em tela a nova lista através de uma função print( ):"""

def criar_lista_tupla(a, b):
    """A função zip( ) para criar uma sequência de tuplas, onde cada tupla contém os elementos correspondentes das listas originais. Em seguida, convertemos essa sequência em uma lista usando a função list( ) e armazenamos o resultado na variável lista_tuplas."""
    
    lista_de_tuplas = list(zip(a, b))
    print(f'Listas de tuplas: {lista_de_tuplas}')

if __name__ == '__main__':
    lista_01 = [1,2,3,4,5]
    lista_02 = [10, 20, 30, 40, 50]
    criar_lista_tupla(lista_01, lista_02)

    # >>> Listas de tuplas: [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]