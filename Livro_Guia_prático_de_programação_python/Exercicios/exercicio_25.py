def tabuada(numero, numero_inicio, numero_final):
    for num in range(numero_inicio, numero_final+1):
        print(f'{numero} X {num} = {num*numero}')

if __name__ == '__main__':
    numero = int(input('Digite um número inicial de [0-10]: '))
    numero_inicio = int(input('Começar por qual número? '))
    numero_final = int(input('Terminar por qual número? '))
    tabuada(numero, numero_inicio, numero_final)