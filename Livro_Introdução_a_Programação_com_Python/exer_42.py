"""Exercício 3.12 Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada para a viagem."""

tempo_de_viagem = int(input('Digite o tempo da viagem[H]: '))
distancia = int(input('Distancia percorrida: '))

velocidade_media = int(distancia / tempo_de_viagem)

print(f'A velocidade média esperada para a viagem: {velocidade_media} Km/h')