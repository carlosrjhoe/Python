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
print(f'{palavra.center(70, "#")}')
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

