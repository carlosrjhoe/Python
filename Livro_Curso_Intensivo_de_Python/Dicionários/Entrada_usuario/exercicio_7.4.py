"""7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza"""

palavra = 'SABORES DE UMA PIZZA'
print('#'*len(palavra))
print(f'{(palavra.center(len(palavra)))}')
print('#'*len(palavra))

from time import sleep

ingredientes = []
while True:
    ingrediente = input(f'Digite um ingrediente da pizza: \nDigite [sair] para encerrar o programa ')
    print(f'{ingrediente.title()} adicionado!')
    # Adicionado sleep(1) para que demore 1seg para que o programa pergunte o ingrediente novamente 
    sleep(1)
    if ingrediente == 'sair':
        break
    else:
        # Adicionando os ingredientes a lista (ingredientes)
        ingredientes.append(ingrediente.title())
print(f'{ingredientes}')