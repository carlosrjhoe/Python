def tabuada(numero):
    for num in range(11):
        print(f'{num} X {numero} = {num*numero}')

if __name__ == '__main__':
    numero = int(input('Digite um número de [0-10]: '))
    tabuada(numero)