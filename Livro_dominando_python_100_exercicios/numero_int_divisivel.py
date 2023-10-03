def verificar_numero(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        print('O número é divisivel por 3 e 5 ao mesmo tempo.')
    else:
        print('O número não é divisivel por 3 por 5 ao mesmo tempo.')

if __name__ == "__main__":
    numero = int(input('Digite um número inteiro: '))
    verificar_numero(numero)