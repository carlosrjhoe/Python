def pegar_pizza(tamanho, *coberturas):
    print(f'Fazendo {str(tamanho)} pizzas com os seguintes coberturas:')
    for sabor in coberturas:
        print(f'- {sabor}')