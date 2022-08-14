palavra = 'PAR OU IMPAR'
print('#'*len(palavra))
print(f'{(palavra.center(len(palavra)))}')
print('#'*len(palavra))

numero = int(input('Digite um número, e eu vou te dizer se é par ou ímpar: '))
if numero % 2 == 0:
    print(f'O numero e PAR')
else:
    print(f'O numero e IMPAR')
    