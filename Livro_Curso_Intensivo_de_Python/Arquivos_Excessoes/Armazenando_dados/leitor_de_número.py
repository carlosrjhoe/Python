import json

arquivo = 'username.json'
with open(arquivo) as objeto_do_arquivo:
    """Usamos a função json.load() para carregar as informações armazenadas em numeros.json e as guardamos na     variável numeros."""
    numeros = json.load(objeto_do_arquivo)

print(f'{numeros}')