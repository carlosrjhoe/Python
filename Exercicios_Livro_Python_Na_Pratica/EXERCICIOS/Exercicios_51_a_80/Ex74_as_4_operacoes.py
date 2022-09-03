texto = 'As quatro operações'
print(f'#' * len(texto))
print(f'{texto.center(len(texto))}')
print(f'#' * len(texto))

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))

operacao = input('Qual opéração deseja realiza?\n\tSoma[+]\n\tSubtração[-]\n\tmultiplicação[*]\n\tDivisão[/]\n')

if operacao == '+':
    soma = a + b
    print(f'A soma de {a}+{b}={soma}')
elif operacao == '-':
    subtracao = a - b
    print(f'A subtração de {a}-{b}={subtracao:.1f}')
elif operacao == '*':
    multiplicacao = a * b
    print(f'A multiplicação de {a}x{b}={multiplicacao}')
elif operacao == '/':
    divisao = a / b
    print(f'A divisão de {a}/{b}={divisao}')
else:
    print('Operação invalida!')
