linguagem_de_programacao = {
    'carlos': 'python',
    'mayara': 'java',
    'neto': 'javaScript',
    'luna': 'go',
}

nomes_escolhidos = ['carlos', 'neto']

for key in linguagem_de_programacao.keys():
    """O método keys() é conveniente quando não precisamos trabalhar com todos os valores de um dicionário. """
    print(f'Nome: {key.title()}\t')

    if key in nomes_escolhidos:
        """No laço, exibimos o nome de cada pessoa. Então, verificamos se o nome com que estamos trabalhando (key) está na lista nomes_escolhidos."""
        print(f'Olá {key.title()}, Vi que sua linguagem de programação favoria é: {linguagem_de_programacao[key].title()}')
    