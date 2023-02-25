def conte_palavras(file_name):
    """Conta o número aproximado de palavras no arquivo"""
    try:
        with open(file_name) as object:
            contents = object.read()
    except FileNotFoundError:
        # pass
        erro = f'Desculpe, o arquivo {file_name} não existe.'
        print(f'{erro}')
    else:
        palavras = contents.split()
        numeros_de_palavras = len(palavras)
        print(f'O arquivo {file_name} tem cerca de {numeros_de_palavras} palavras.')


if __name__ == '__main__':
    file_names = ['alice.txt', 'texto_trabalho.txt',
                  'programming.txt', 'pi_digits.txt']

    for file in file_names:
        """Escreve um laço simples para contar as palavras de qualquer texto"""
        conte_palavras(file)
