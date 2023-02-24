"""Vamos obter o texto dentro de um arquivo [txt] e tentar contar o número de palavras do texto."""

file_name = 'alice.txt'

try:
    with open(file_name) as object:
        contents = object.read()
except FileNotFoundError as erro:
    erro = f'Desculpe, o arquivo {file_name} não existe.'
    print(f'{erro}')
else:
    """Conta o número aproximado de palavras no arquivo"""
    palavras = contents.split()
    numeros_de_palavras = len(palavras)
    print(f'O arquivo {file_name} tem cerca de {numeros_de_palavras} palavras.')