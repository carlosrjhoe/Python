"""10 - Mostre o tamanho da lista nomes / o número de elementos da lista nomes: Mostre separadamente apenas o terceiro elemento dessa lista:

Feltrin, Fernando. Python na Prática: Aprenda Python Através de Exercícios Comentados (p. 26). Uniorg. Edição do Kindle. """

nomes = ['Ana', 'Carlos', 'Daiane', 'Fernando', 'Maria']

def mostar_tamanho_da_lista():
    return f"{len(nomes)}"
    

def mostrar_o_terceiro_da_lista():
    return f"{nomes[2]}"
    

if __name__ == '__main__':
    print(mostar_tamanho_da_lista())
    print(mostrar_o_terceiro_da_lista())