texto = 'PAR OU IMPAR'
print('#' * len(texto))
print(texto.center(len(texto)))
print('#' * len(texto))

num1 = input('Digiteum número: ')

if not num1.isdigit():
    print('O número digitado não é inteiro')
else:
    num1 = int(num1)
    if num1 % 2 == 0: print('Par')
    else: print('Impar')