"""7 – A partir de duas listas de números, use a função zip( ) e uma list comprehension para criar uma nova lista contendo a soma dos elementos correspondentes das listas originais. Imprima a nova lista no console:"""

def somar_listas(lista_01, lista_02):
    """list comprehension - Para criar uma nova lista onde cada elemento é a soma dos elementos correspondentes das listas originais. A variável x e y são usadas para iterar sobre cada tupla da sequência retornada pela função zip( )."""
    
    soma_lista = [x + y for x, y in zip(lista_01, lista_02)]
    print(f'Soma das listas: {soma_lista}')

if __name__ == '__main__':
    lista_01 = [1,2,3,4,5]
    lista_02 = [10,20,30,40,50]
    somar_listas(lista_01, lista_02)
    
    # >>> Lista de soma: [11, 22, 33, 44, 55]