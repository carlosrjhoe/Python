"""As tuplas permitir fazer exatamente isso. Python refere-se a valores
que não podem mudar como imutáveis, e uma lista imutável é chamada de
tupla"""

dimensao = (300, 50)
print(f'Tupla original')
for dados in dimensao:
    print(f'{dados}', end=' ')


dimensao = (200, 150)
print(f'\nTupla modificada')
for dados in dimensao:
    print(f'{dados}', end=' ')
    
# dimensao[0] = 100 # objeto não suporta atribuição de item
# print(f'{dimensao[0]}')
# print(f'{dimensao[1]}')

