"""Supondo que temos uma lista composta por ['Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda'], 
reordene os elementos da lista de modo a obter a sequência ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo'].
"""

from collections import deque

def reordenar_lista(lista_de_semana):
    lista = deque(lista_de_semana)
    lista.rotate(1)
    return lista

if __name__ == '__main__':
    lista_de_semana = deque(['Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo', 'Segunda'])
    print(reordenar_lista(lista_de_semana))