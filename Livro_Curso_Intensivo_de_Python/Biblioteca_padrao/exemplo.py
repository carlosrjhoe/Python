from collections import OrderedDict

idiomas_favoritos = OrderedDict()
# idiomas_favoritos = {'carlos': 'python', 'mayara': 'c', 'neto': 'ruby', 'luna': 'python'}
idiomas_favoritos['carlos'] = 'python'
idiomas_favoritos['mayara'] = 'c'
idiomas_favoritos['neto'] = 'ruby'
idiomas_favoritos['luna'] = 'python'

for nome, linguagem in idiomas_favoritos.items():
    print(f'Para {nome.title()}, a linguagem de programação favorito é: {linguagem.title()}')
    
