print('###################################################')
print('#### Percorrendo um dicionário com um laço FOR ####')
print('###################################################')

# usuario_0 = {
#     'username': 'carlosrjhoe',
#     'primeiro': 'carlos',
#     'segundo': 'roberto'
# }

# podemos percorrer o dicionário com um laço for:
# for chave, valor in usuario_0.items():
#     print(f'Chave = {chave}, Valor = {valor}')
    
# for nome in usuario_0.keys():
#     print(f'{nome}')
    
# for nome in usuario_0.values():
#     print(f'{nome}')


linguagem_favorita = {
    'carlos': 'python',
    'mayara': 'java',
    'neto': 'python',
    'luna': 'javascript'
}

amigos = ['carlos', 'neto']

for nome in linguagem_favorita.keys():
    print(f'{nome}')
    if nome not in amigos:
        print(f'Oi, {nome.title()}, por favor responda nossa enquete!')
        # print(f'Oi {nome.title()}, vejo que sua linguagem de programação favorita é {linguagem_favorita[nome].title()}')

palavra = 'Percorrendo um dicionário com um laço em ordem usando FOR'
print('#'*70)
print(f'{(palavra.center(70, "#"))}')
print('#'*70)

for nome in sorted(linguagem_favorita.keys()):
    print(f'Oi, {nome.title()}, obrigado por fazer a enquete...')

print('#'*70)

print(f'Os seguintes idiomas foram mencionados:')
for linguagem in sorted(linguagem_favorita.values()):
    print(f'{linguagem}')
    
print('#'*70)

"""Quando colocamos set() em torno de uma lista que contenha itens
duplicados, Python identifica os itens únicos na lista e cria um conjunto a
partir desses itens."""

print(f'Os seguintes idiomas foram mencionados:')
for linguagem in set(linguagem_favorita.values()):
    print(f'{linguagem}')



palavra = 'Informações aninhadas(Uma lista de dicionários)'
print('#'*70)
print(f'{(palavra.center(70))}')
print('#'*70)

pessoa_1 = {'nome': 'carlos', 'cor': 'azul', 'nota': 8}
pessoa_2 = {'nome': 'mayara', 'cor': 'azul-marinho', 'nota': 9}
pessoa_3 = {'nome': 'neto', 'cor': 'mervelho', 'nota': 10}
pessoa_4 = {'nome': 'luna', 'cor': 'amarelo', 'nota': 9.8}

pessoas = [pessoa_1, pessoa_2, pessoa_3, pessoa_4]

# Cria uma lista vazia para armazenar pessoas_alienígenas
pessoas_alienígenas = []
pessoas_alienígenas_azuis = []

# Cria 30 pessoa alienígenas verdes
for numero_aliens in range(0, 30):
    novo_alien = {'cor': 'verde', 'ponto': 5, 'velocidade': 'lento'}
    pessoas_alienígenas_azuis.append(novo_alien)
    
# Modifica os 5 primeiros pessoas_alieniginas para cor azul.
for alien in pessoas_alienígenas_azuis[0:3]:
    if alien['cor'] == 'verde':
        alien['cor'] = 'azul'
        alien['ponto'] = 10
        alien['velocidade'] = 'medio'

# Mostra as 15 primeiras pessoas em pessoas_alienigenas_azuis
for alien1 in pessoas_alienígenas_azuis[0:30]:
    if alien1['ponto'] == '5':
        alien1['cor'] = 'amarelo'
        alien1['ponto'] = 15
        alien1['velocidade'] = 'rapido'
    print(f'{alien1}')
        
print(f'Total de alienigenas: {len(pessoas_alienígenas_azuis)}')
print('#' * 70)