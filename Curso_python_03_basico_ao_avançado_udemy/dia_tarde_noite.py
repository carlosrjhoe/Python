texto = 'DIA TARDE OU DE NOITE'
print('#' * len(texto))
print(texto.center(len(texto)))
print('#' * len(texto))

numero = input('Digite um numero entre [1-24]: ')

if numero.isdigit():
    numero = int(numero)
    if numero <= 12: print('Bom dia!')
    elif numero <= 18: print('Boa tarde!')
    else: print('Boa noite!')