''' Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem '''

import string


distancia = int(input('Digite a distância da viagem em [km]: '))
velocidade = int(input('Digite a velocidade da viagem em [Kmh]: '))

velocidade_media = distancia / velocidade
print(f'O tempo de viagem foi de: {velocidade_media:.0f}h {velocidade_media}')
