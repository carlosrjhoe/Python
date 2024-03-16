def cabecalho():
    texto = 'PAR OU IMPAR'
    print('#' * len(texto))
    print(texto.center(len(texto)))
    print('#' * len(texto))

def par_ou_impar():
    num = input('Digite um número: ')
    if not num.isdigit():
        print('O número digitado não é inteiro')
    else:
        num = int(num)
        if num % 2 == 0: print('Par')
        else: print('Impar')
def main():
    cabecalho()
    par_ou_impar()

if __name__ == "__main__":
    main()