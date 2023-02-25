def conte_palavras(file_name):
    """Conta o número aproximado de palavras no arquivo"""
    """A única diferença entre essa listagem e a listagem anterior está na
        instrução pass em u. Agora, quando um FileNotFoundError é levantado, o
        código no bloco except é executado, mas nada acontece. Nenhum
        traceback é gerado e não há nenhuma saída em resposta ao erro levantado."""
    try:
        with open(file_name) as object:
            contents = object.read()
    except FileNotFoundError:
        pass
    #   erro = f'Desculpe, o arquivo {file_name} não existe.'
    #   print(f'{erro}')
    else:
        palavras = contents.split()
        numeros_de_palavras = len(palavras)
        print(
            f'O arquivo {file_name} tem cerca de {numeros_de_palavras} palavras.')


if __name__ == '__main__':
    file_names = ['alice.txt', 'texto_trabalho.txt', 'programming.txt', 'pi_digits.txt']

    for file in file_names:
        """Escreve um laço simples para contar as palavras de qualquer texto"""
        conte_palavras(file)