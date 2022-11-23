jogadores = ['charles', 'martina', 'michael', 'florence', 'eli']

print(f'Here are the first three players on my team:')
for jogador in jogadores[:3]:
    print(f'{jogador.title()}')



novos_jogadores = jogadores[:]
print(novos_jogadores)