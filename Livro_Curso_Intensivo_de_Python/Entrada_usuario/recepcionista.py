palavra = 'ESCREVENDO PROMPTS CLAROS'
print('#'*70)
print(f'{(palavra.center(70))}')
print('#'*70)

nome = input('Por favor insira seu nome: ')
altura = float(input('Insira sua altura: '))
if altura >= 1.00:
    print(f'Ola, {nome.title()}, voce tem {altura}m, voce e alto!')
else:
    print(f'{nome.title()}, voce e baixinho.')

