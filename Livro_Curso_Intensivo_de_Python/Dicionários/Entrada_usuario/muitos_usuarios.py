palavra = 'UM DICIONARIO EM UM DICIONARIO'
print('#'*70)
print(f'{(palavra.center(70))}')
print('#'*70)

usuarios = {
    'CR': {
        'primeiro': 'carlos',
        'segundo': 'conceicao',
        'cidade natal': 'petrolina',
        'idade': 36
    },
    
    'MR': {
        'primeiro': 'mayara',
        'segundo': 'ramos',
        'cidade natal': 'cabo',
        'idade': 37
    },
    
    'CN': {
        'primeiro': 'carlos',
        'segundo': 'neto',
        'cidade natal': 'cabo',
        'idade': 6
    },
    
    'LR': {
        'primeiro': 'luna',
        'segundo': 'ramos',
        'cidade natal': 'cabo',
        'idade': 4
    }
}

for pessoa, info in usuarios.items():
    print(f'Usuario: {pessoa}\n \tNome: {info["primeiro"].title()}\n \tSobre-nome: {info["segundo"].title()}\n \tIdade: {info["idade"]}\n \tNaturalidade: {info["cidade natal"].title()}')