linguagem_de_programacao = {
    'carlos': 'python',
    'mayara': 'java',
    'neto': 'javaScript',
    'luna': 'go',
}

for key in linguagem_de_programacao.keys():
    """O método keys() é conveniente quando não precisamos trabalhar com todos os valores de um dicionário. """
    print(f'Linguagem de programação: {key.title()}\t')