from soma import soma

def calculo_soma():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    resultado = soma(num1, num2)

    print(f'O resultado da soma entre {num1} e {num2} é: {resultado}')
    print(f'Documentação do modulo soma:\n{soma.__doc__}')

if __name__ == '__main__':
    calculo_soma()