linguagem_de_programacao = {
    'carlos': ['python', 'java', 'javascript'],
    'mayara': ['java'],
    'neto': ['javaScript', 'python'],
    'luna': ['go', 'java'],
}

for kye, values in linguagem_de_programacao.items():
    print(f'{kye.title()}, você tem {len(values)} liguagens de programação, que são:')
    for linguagem in values:
        print(f'\t{linguagem.title()}')