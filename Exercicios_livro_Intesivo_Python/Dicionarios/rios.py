rios = {
    'mississipi': 'estados unidos',
    'amazonas': 'cordilheira dos andes',
    'panamá': 'america do sul',
    'dánubio': 'europa',
    'volga': 'europa',
    'huang-ho': 'china',
    'congo': 'africa',
    'nilo': 'egito',
    'tigre': 'oriente médio',
}

print(f'\nMostrando chave e valor:')
for key, value in rios.items():
    """Use um laço para exibir uma frase sobre cada rio"""
    print(f'O Rio {key.title()} corre pelo {value.title()}')

print(f'\nMostrando chave:')
for key in rios.keys():
    """Use um laço para exibir o nome de cada rio incluído no dicionário"""
    print(f'O rio {key.title()}')

print(f'\nMostrando valor:')
for value in rios.values():
    """Use um laço para exibir o nome de cada país incluído no dicionário"""
    print(f'{value.title()}')