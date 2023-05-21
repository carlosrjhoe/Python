"""Uma vez que temos dois conjuntos numéricos iniciais c1 = (2, 4, 6, 8, 10) e c2 = (2, 4, 6, 8, 10) e um terceiro conjunto nomeado como c3, gerado a partir do conteúdo de c2. Equiparando os três conjuntos, verifique se os mesmos possuem mesmo conteúdo e mesmo identificador de memória.
"""

import collections

def mostrar_conjuntos(dc_conj_1,dc_conj_2,conj_3):
    print(f'Conjunto 1: {dc_conj_1}')
    print(f'Endereço de conjunto 1: {id(dc_conj_1)}')
    print(f'Conjunto 2: {dc_conj_2}')
    print(f'Endereço de conjunto 2: {id(dc_conj_2)}')
    print(f'Conjunto 3: {conj_3}')
    print(f'Endereço de conjunto 3: {id(dc_conj_3)}')
    
def verificar_conjuntos(dc_conj_1,dc_conj_2,conj_3):
    if (dc_conj_1 == dc_conj_2) and (id(dc_conj_1) == id(dc_conj_2)):
        print('Conjunto 1 e Conjunto 2 possuem os mesmos elementos e são o mesmo objeto alocado em memória')
    if (dc_conj_1 == conj_3) and (id(dc_conj_1) == id(conj_3)):
        print('Conjunto 1 e Conjunto 3 possuem os mesmos elementos e são o mesmo objeto alocado em memória')
    if (dc_conj_2 == conj_3) and (id(dc_conj_2) == id(conj_3)):
        print('Conjunto 2 e Conjunto 3 possuem os mesmos elementos e são o mesmo objeto alocado em memória')
    if (dc_conj_1 == dc_conj_2) and (id(dc_conj_1) != id(dc_conj_2)):
        print('Conjunto 1 e Conjunto 2 possuem os mesmos elementos, porem são objeto diferentes alocados em memória')
    if (dc_conj_1 == conj_3) and (id(dc_conj_1) != id(conj_3)):
        print('Conjunto 1 e Conjunto 3 possuem os mesmos elementos, porem são objeto diferentes alocados em memória')
    if (dc_conj_2 == conj_3) and (id(dc_conj_2) != id(conj_3)):
        print('Conjunto 2 e Conjunto 3 possuem os mesmos elementos, porem são objeto diferentes alocados em memória')
        
if __name__ == '__main__':
    conj_1 = (2, 4, 6, 8, 10)
    dc_conj_1 = collections.deque(conj_1)
    conj_2 = (2, 4, 6, 8, 10)
    dc_conj_2 = collections.deque(conj_2)
    conj_3 = dc_conj_2
    dc_conj_3 = collections.deque(conj_3)
    
    mostrar_conjuntos(dc_conj_1,dc_conj_2,conj_3)
    verificar_conjuntos(dc_conj_1,dc_conj_2,conj_3)