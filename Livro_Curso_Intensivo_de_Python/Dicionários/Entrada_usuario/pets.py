palavra = 'Removendo todas as instâncias de valores específicos de uma lista.'
print('#'*len(palavra))
print(f'{(palavra.center(len(palavra)))}')
print('#'*len(palavra))

animais_de_estimacao = ['cachorro', 'gato', 'cachorro', 'golfinho', 'gato', 'coelho', 'gato']

while 'gato' in animais_de_estimacao:
    animais_de_estimacao.remove('gato')
    print(animais_de_estimacao)
    
