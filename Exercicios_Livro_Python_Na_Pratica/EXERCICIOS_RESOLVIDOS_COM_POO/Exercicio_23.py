"""23 - Verifique se o valor de num1 consta nos elementos de lista1. 
        Sendo num1 = 100 e lista1 = [10, 100, 1000, 10000, 100000].
        Feltrin, Fernando. Python na Prática: Aprenda Python Através de Exercícios Comentados (p. 34). Uniorg. Edição do Kindle.
"""

num1 = 101
lista1 = [1, 10, 100, 1000, 10000, 100000]

def mostra_lista():
    print(f'{num1 in lista1}')


if __name__ == '__main__':
    mostra_lista()