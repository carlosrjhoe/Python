palavra = 'Uma lista em um dicionário'
print('#'*70)
print(f'{(palavra.center(70))}')
print('#'*70)

# Armazena informações sobre uma pizza que está sendo pedida
pizza = {
    'borda': 'grossa',
    'recheio': ['cogumelos', 'queijo extra']
}

# Resume o pedido
print(f'Você pediu uma pizza de massa {pizza["borda"]} com os seguintes recheios:')

for recheio in pizza['recheio']:
    print(f'\t{recheio}')