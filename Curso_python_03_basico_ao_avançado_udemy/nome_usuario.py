texto = 'TAMANHO DO SEU NOME'
print('#' * len(texto))
print(f'{texto.center(len(texto))}')
print('#' * len(texto))

nome = input('Digite seu nome: ')
qtd_letras = len(nome)

if qtd_letras <= 4:
    print(f'O nome: {nome.title()}, tem {qtd_letras} letras\nSeu nome é curto.')
elif qtd_letras >= 5 and qtd_letras <= 6:
    print(f'O nome: {nome.title()}, tem {qtd_letras} letras\nSeu nome é normal.')
elif qtd_letras >= 7:
    print(f'O nome: {nome.title()}, tem {qtd_letras} letras\nSeu nome é muito grande')
    