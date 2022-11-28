from time import sleep

usuarios_nao_confirmados = ['carlos', 'mayara', 'neto', 'luna']
usuarios_confirmados = []

while usuarios_nao_confirmados:
    """ Verifica cada usuário até que não haja mais usuários não confirmados Transfere cada usuário verificado para a lista de usuários confirmados"""
    usuario_atual = usuarios_nao_confirmados.pop() # Sempre irá remover o ultimo da lista.
    sleep(1)

    print(f'Verificando usuário: {usuario_atual.title()}')
    usuarios_confirmados.append(usuario_atual)
    sleep(1)

print('\nOs seguintes usuários foram confirmados:')
for usuario in usuarios_confirmados:
    print(f'{usuario.title()}', end=', ')