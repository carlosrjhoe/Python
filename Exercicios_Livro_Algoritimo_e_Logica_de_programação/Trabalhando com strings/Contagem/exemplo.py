"""Listagem 7.8 – Contagem de letra e palavras"""

nome = 'um tigre, dois tigres, três tigres'
# print(nome.count('tigre'))
# print(nome.count('um'))
# print(nome.count('dois'))

"""Listagem 7.9 – Pesquisa de strings com find"""

# print(nome.find('tigre'))
# print(nome.find('tiges'))

"""Listagem 7.10 – Pesquisa de strings com rfind"""

# print(nome.rfind('t'))
# print(nome.find('e'))

"""Listagem 7.12 – Pesquisa de todas as ocorrências"""

p = 0
while( p > -1 ):
    p = nome.find('tigre', p)
    if p >= 0:
        print(f'Posição: {p}')
        p += 1
