jogadores = ['charles', 'martina', 'michael', 'florence', 'eli', 'carlos', 'mayara', 'alice', 'neto', 'luna']

print(f'{jogadores}')
print(f'Os três primeiros da lis são: {jogadores[:3]}')
print(f'Três itens do meio da lista são: {jogadores[3:6]}')
print(f'Os três últimos itens da lista são:: {jogadores[7:]}')

for nome in jogadores:
    print(f'{nome.title()}')