# palavra = 'LACO WHILE EM ACAO'
# print('#'*len(palavra))
# print(f'{(palavra.center(len(palavra)))}')
# print('#'*len(palavra))

# msg = ''
# while msg != 'sair':
#     msg = input('Diga-me algo e eu repetirei para voce \nDigite "sair" para encerrar o programa: ')
#     print(msg)
    
palavra = 'USANDO UM FLAG'
print('#'*len(palavra))
print(f'{(palavra.center(len(palavra)))}')
print('#'*len(palavra))

ativo = True
while ativo:
    msg = input('Diga-me algo e eu repetirei para voce \nDigite "sair" para encerrar o programa: ')
    if msg == 'sair':
        ativo = False
    else:
        print(msg)