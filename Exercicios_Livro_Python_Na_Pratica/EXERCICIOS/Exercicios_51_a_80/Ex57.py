def pessoa(nome, idade=36, funcao='Líder'):
    return f'{nome}, tem {idade} anos, e sua função é {funcao}'

p1 = pessoa('Carlos',funcao='Gerente')
print(p1)