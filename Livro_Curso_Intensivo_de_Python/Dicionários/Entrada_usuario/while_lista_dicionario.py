palavra = 'Transferindo itens de uma lista para outra!!!'
print('#'*len(palavra))
print(f'{(palavra.center(len(palavra)))}')
print('#'*len(palavra))

"""Começa com os usuários que precisam ser verificados"""
Usuarios_nao_confirmados = ['carlos', 'mayara', 'neto', 'luna']
"""Lista vazia para armazenar os usuários confirmados"""
Usuarios_confirmados = []

while Usuarios_nao_confirmados:
    """Verificar cada usuário até que não haja mais usuários não confirmados"""
    Usuario_atual = Usuarios_nao_confirmados.pop()
    print(f'Verificando usuário: {Usuario_atual.title()}')
    """Transfere cada usuário verificado para a lista de usuários confirmados"""
    Usuarios_confirmados.append(Usuario_atual)
    
# Exibe todos os usuários confirmados
print('Os seguintes usuários foram confirmados:')
for usuario in Usuarios_confirmados:
    print(f'{usuario.title()},', end=" ")