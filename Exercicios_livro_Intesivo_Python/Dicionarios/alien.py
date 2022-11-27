alien_0 = {'color': 'green', 'points': 5, 'velocidade': 'rapido'}
alien_0['posicao_x'] = 0
alien_0['posicao_y'] = 10
print(f'{alien_0}')

# alien_0['posicao_x'] = 0
# alien_0['posicao_y'] = 25

# novo_ponto = alien_0['points']
# # print(f'{alien_0["color"]}')
# # print(f'{alien_0["points"]}')

# print(f'{alien_0}')
# print(f'{len(alien_0)}')

# if len(alien_1) <= 0:
#     print(f'Dicionario vazio!')

# alien_0['color'] = 'red'
# print(f'{alien_0}')

if alien_0['velocidade'] == 'devagar':
    incrementa = 1
elif alien_0['velocidade'] == 'medio':
    incrementa = 2
else:
    # Este deve ser um alienígena rápido
    incrementa = 3

# A nova posição é a posição antiga somada ao incremento
alien_0['posicao_x'] = alien_0['posicao_x'] + incrementa

# Removendo pares chave-valor
del alien_0['points']

print(f'{alien_0}')