'''Supondo que a lista data = [59.19, 72.05, 66.82, 81.15, 66.33, 94.87, 99.65, 70.13, 55.75, 87.71, 95.43, 93.17, 98.54, 68.31, 59.24, 88.94, 79.44, 83.91, 84.4, 68.21] é o retorno dos últimos 20 registros de um sensor qualquer, retorne a média simples, a média harmônica e a média geométrica destes valores. Os resultados devem conter a precisão de 5 casas decimais.
'''
import statistics
import numpy as np

def informacao_media_simples(lista):
    media_simples = round(statistics.mean(lista), 5)
    return media_simples

def informacao_harmonica(lista):
    media_harmonica = round(statistics.harmonic_mean(lista), 5)
    return media_harmonica

def informacao_geometrica(lista):
    '''Este processo visa converter a estrutura de dados de lista simples para uma array que nos trará, além de uma melhor performance de processamento, um leque maior de possibilidades.'''
    lista_geometrica = np.array(lista)
    media_geometrica = round(lista_geometrica.prod()**(1.0/len(lista_geometrica)), 5)
    return media_geometrica

if __name__ == '__main__':
    data = [59.19, 72.05, 66.82, 81.15, 66.33, 94.87, 99.65, 70.13, 55.75, 87.71, 95.43, 93.17, 98.54, 68.31, 59.24, 88.94, 79.44, 83.91, 84.4, 68.21]
    print(f'Média simples: {informacao_media_simples(data)}')
    print(f'Média harmônica: {informacao_harmonica(data)}')
    print(f'Média geométrica: {informacao_geometrica(data)}')