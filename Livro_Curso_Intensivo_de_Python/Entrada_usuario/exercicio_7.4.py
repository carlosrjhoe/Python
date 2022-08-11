"""7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza"""

palavra = 'SABORES DE UMA PIZZA'
print('#'*len(palavra))
print(f'{(palavra.center(len(palavra)))}')
print('#'*len(palavra))

ingredientes = []
while True:
    ingrediente = input(f'Digite um ingrediente da pizza: \nDigite [sair] para encerrar o programa ')
    print(f'{ingrediente.title()} adicionado!')
    if ingrediente == 'sair':
        break
    else:
        # Adicionando os ingredientes a lista (ingredientes)
        ingredientes.append(ingrediente.title())
print(f'{ingredientes}')