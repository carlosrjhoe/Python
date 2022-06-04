""" Exercício 4.6 Escreva um programa que pergunte a distância que um passageiro
deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
para viagens de até de 200 km, e R$ 0,45 para viagens mais longas """

km = int(input('Digite a distancia percorrida: '))
if km <= 200:
    print(f'A passagem vai custar R${km * 0.5:.2f}')
else:
    print(f'A passagem vai custar R${km * 0.45:.2f}')
    