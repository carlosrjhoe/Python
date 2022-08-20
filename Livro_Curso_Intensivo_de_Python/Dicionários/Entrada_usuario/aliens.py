alien_0 = {'cor': 'verde', 'ponto': 5}

# print(alien_0['cor'])
# print(alien_0['ponto'])

print(f'Você acabou de ganhar {alien_0["ponto"]} pontos')


alien_0['posicao_x'] = 10 # Adicionar nova chave


aliens = {} # Criar um dicionário vazio
print(f'Dicionario vazio {aliens}')
aliens = {'nome': 'carlos'}
print(aliens['nome'])

aliens['nome'] = 'Mayara' # Modificando valores em um dicionário
print(aliens['nome'])

print('###############################################')

alien_1 = {'Nome': 'Neto', 'idade': 6, 'posição': 3}

if alien_1['posição'] == 1:
    incremento = 0
elif alien_1['posição'] == 3:
    incremento = 2
    
alien_1['posição'] = alien_1['posição'] + incremento # A nova posição é a posição antiga somada ao incremento

print(f'{alien_1}')

print('###############################################')

"""Removendo pares chave-valor"""

pessoa = {'Nome': 'Luna', 'Idade': 4}
print(pessoa)

del pessoa['Idade'] # Deletar uma chave de um dicionário

print(pessoa)
print('###############################################')

"""Um dicionário de objetos semelhantes"""

linguagem_favorita = {
    'carlos': ['python'],
    'mayara': ['java'],
    'neto': 'c++',
    'luna': ['javascript']
}

print(linguagem_favorita)
for nome, linguagens in linguagem_favorita.items():
    print(f'Para {nome.title()}, suas linguagens de programação favoritas são:')
    for linguagem in linguagens:
        print(f'{linguagem.title()}')
