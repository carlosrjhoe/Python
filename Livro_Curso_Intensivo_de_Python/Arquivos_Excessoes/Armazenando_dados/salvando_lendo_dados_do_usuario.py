import json

username = input('What is your name? ').title()

filename = 'username.json'
with open(filename, 'w') as file_object:
    """Usei json.load() para ler as informações armazenadas em
        username.json na variável username. Agora posso recuperar o nome do
        usuário, e lhe desejar as boas-vindas de volta"""
    json.dump(username, file_object)
    print(f"We'll remember you when come back, {username}!")