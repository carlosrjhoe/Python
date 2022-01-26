carteira = int(input('Quanto eu tenho? '))
tenis = int(input('Quanto custa o tenis? '))
necessidade = input('Preciso mesmo disso? ')

if carteira >= tenis and necessidade == 's':
    print('Luxei, comprei um boot novo!')
else:
    print('É, deixa pro mês que vem...')
 
