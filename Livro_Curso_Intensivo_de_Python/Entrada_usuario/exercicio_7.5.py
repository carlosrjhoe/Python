"""7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3
anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso
custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15 dólares.
Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes
o preço do ingresso do cinema."""

palavra = 'Seja bem vndo ao cinema do parque!!!'
print('#'*len(palavra))
print(f'{(palavra.center(len(palavra)))}')
print('#'*len(palavra))

from time import sleep

print('PREÇOS DOS INGRESSOS:')

while True:
    print('Crianças até 3 anos = R$0,00\nEntre 3 - 12 anos = R$10,00\nA cima de 12 anos = R$15,00')
    idade = int(input('Informe sua idade: '))
    if idade == str('sair'):
        break
    elif idade <= 3:
        print(f'Olá, o ingrésso cursta R$0,00\nTenha uma bom filme!')
    elif idade > 3 and idade <= 12:
        print(f'Olá, o ingrésso cursta R$10,00\nTenha uma bom filme!')
    else:
        print(f'Olá, o ingrésso cursta R$15,00\nTenha uma bom filme!')
    print('#'*len(palavra))
    sleep(1)
