alien_0 = {'cor': 'verde', 'pontos': 5}
alien_1 = {'cor': 'amarelo', 'pontos': 10}
alien_2 = {'cor': 'vermelho', 'pontos': 15}

aliens_verdes = []
aliens_amarelos = []
aliens_vermelhos = []

# Cria 30 alienígenas verdes
for numero_alien in range(30):
    novo_alien = {'cor': 'verde', 'pontos': 5, 'velocidade': 'lento'}
    aliens_verdes.append(novo_alien)

# Cria 30 alienígenas amarelos
for numero_alien in range(20):
    novo_alien = {'cor': 'amarelo', 'pontos': 10, 'velocidade': 'medio'}
    aliens_amarelos.append(novo_alien)

# for alien in aliens_verdes[:5]:
#     if alien['cor'] == 'verde':
#         """transformando os 5 primeiros aliens em amarelo, e modificando seus atributos"""
#         alien['cor'] = 'amarelo'
#         alien['pontos'] = '10'
#         alien['velocidade'] = 'medio'

# for alien in aliens_amarelos[:8]:
#     """transformando os 8 primeiros aliens em vermelho, e modificando seus atributos"""
#     if alien['cor'] == 'amarelo':
#         alien['cor'] = 'vermelho'
#         alien['pontos'] = 15
#         alien['velocidade'] = 'rápido'
    
# for alien in aliens_verdes:
#     """Mostrando os 5 primeiros alienigenas verdes"""
#     print(f'{alien}')

# for alien in aliens_amarelos:
#     """Mostrando os 8 primeiros alienigenas vermelhos"""
#     print(f'{alien}')

print(f'Total de alienigenas verdes: {len(aliens_verdes)}')
print(f'Total de alienigenas amarelos: {len(aliens_amarelos)}')