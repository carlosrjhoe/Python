def desempacotar(args):
    primeiro,*intermediario, ultimo = args

    print(f'O primeiro número é: {primeiro}')
    print(f'Os números intermediários são: {intermediario}')
    print(f'O último é: {ultimo}')

if __name__ == '__main__':
    numeros = (1,2,3,4,5,6,7,8,9,10)
    desempacotar(numeros)

    # O primeiro número é: 1
    # Os números intermediários são: [2, 3, 4, 5, 6, 7, 8, 9]
    # O último é: 10