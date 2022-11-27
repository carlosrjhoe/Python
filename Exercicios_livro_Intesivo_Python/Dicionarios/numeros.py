numeros = {
    'carlos': 37,
    'carlos': 37,
    'mayara': 38,
    'neto': 7,
    'neto': 7,
    'luna': 5,
    'luna': 5,
    'luna': 5,
    'rose': 56,
    'lucia': 53,
    'alaide': 57,
    'valdênia': 35,
    'pedro': 37,
    'valéria': 39,
    'flávio': 37,
}

print(f'Mostrando chave e valor:')
for nome, numero in numeros.items():
    """Iterar sobre um dicionário mostrando chave e valor"""
    print(f'Nome: {nome.title()}, seu Número da sorte: {numero}')
    

print(f'\nMostrando chave:')
for nome in numeros.keys():
    """Iterar sobre um dicionário mostrando chave"""
    print(f'Nome: {nome.title()}')

print(f'\nMostrando valor:')
for numero in numeros.values():
    """Iterar sobre um dicionário mostrando valor"""
    print(f'Nome: {numero}')
    