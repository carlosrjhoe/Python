palavra = 'LACO WHILE EM ACAO'
print('#'*len(palavra))
print(f'{(palavra.center(len(palavra)))}')
print('#'*len(palavra))

numero_atual = 1
while numero_atual <= 5:
    print(f'{numero_atual}')
    numero_atual += 1