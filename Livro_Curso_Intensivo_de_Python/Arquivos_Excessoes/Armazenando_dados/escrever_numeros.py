import json

numeros = [2, 3, 5, 7, 11, 13]

arquivo = 'numeros.json'
with open(arquivo, 'w') as objeto_do_arquivo:
    """Abrir o arquivo em modo de escrita.
        A função json.dump() é para armazenar a lista numeros no arquivo numeros.json"""
    json.dump(numeros, objeto_do_arquivo)
    