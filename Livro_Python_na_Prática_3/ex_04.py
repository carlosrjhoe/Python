"""4 – Dada uma matriz (lista de listas) de números, crie uma nova lista contendo todos os elementos da matriz de origem usando list comprehension e mostre via terminal o conteúdo desta matriz:"""

def listas_de_listas(matriz):
    """A variável lista itera sobre cada sublista da matriz em questão e, em seguida, a variável temporária numero itera sobre cada elemento dessas sublistas. Cada elemento numero é adicionado à nova lista elementos a cada ciclo de repetição deste laço."""
    
    elementos = [numero for lista in matriz for numero in lista] 
    print(f'Elementos da matriz: {elementos}')

if __name__ == '__main__':
    matriz = [[1,2,3],[4,5,6],[7,8,9]]
    listas_de_listas(matriz)