import json

filename = 'Carlos Roberto.json'

try:
    with open(filename) as object_username:
        username = json.load(object_username)
        print(f'Welcome back, {username}')
except FileNotFoundError as erro:
    erro = 'Arquivo não encontrado'
    print(f'Error: {erro}')
    username = input('Whats your name? ')
    with open(username, 'w') as object_username:
        json.dump(username, object_username)
        print(f'Welcome back, {username}')
else:
    print(f'Nós lembraremos de você quando você voltar, {username}')