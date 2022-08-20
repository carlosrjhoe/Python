from collections import OrderedDict

texto = 'Linguagens favoritas'
print(f'#' * len(texto))
print(f'{texto.center(len(texto))}')
print(f'#' * len(texto))

linguagem_favorita = OrderedDict()

linguagem_favorita = {
    'carlos': ['python'],
    'mayara': ['java'],
    'neto': ['c++'],
    'luna': ['javascript']
}

for nome, linguagens in linguagem_favorita.items():
    print(f'Para {nome.title()}, suas linguagens de programação favoritas são:')
    for linguagem in linguagens:
        print(f'{linguagem.title()}')